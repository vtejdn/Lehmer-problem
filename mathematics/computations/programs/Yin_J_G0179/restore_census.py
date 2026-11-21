"""Restore the fixed census reports to the directory used by the verifiers."""

import argparse
import json
import ntpath
import os
import tarfile
from pathlib import Path, PurePosixPath, PureWindowsPath
from tempfile import NamedTemporaryFile


PROGRAM = Path(__file__).resolve().parent
INPUTS = PROGRAM / "inputs"
OUTPUT = PROGRAM.parents[1] / "outputs" / PROGRAM.name
windows_reserved = getattr(ntpath, "isreserved", lambda part: PureWindowsPath(part).is_reserved())


def restore_report(destination, name, data):
    name = PurePosixPath(name.as_posix())
    if (name.is_absolute() or name.suffix != ".json" or "\\" in name.as_posix()
            or any(part == ".." or ":" in part or part.endswith((" ", ".")) or windows_reserved(part)
                   for part in name.parts)):
        raise ValueError(f"Invalid census report path: {name}")
    path = destination.joinpath(*name.parts)
    if not path.resolve().is_relative_to(destination.resolve()):
        raise ValueError(f"Census report escapes its destination: {name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        temporary = NamedTemporaryFile(dir=path.parent, prefix=".census-", suffix=".tmp", delete=False)
        try:
            with temporary:
                temporary.write(data)
            # Same-directory rename on Windows and hard linking on POSIX both
            # publish a completed file and fail if another writer won the race.
            publish = os.rename if os.name == "nt" else os.link
            try:
                publish(temporary.name, path)
            except FileExistsError:
                pass
            else:
                return
        finally:
            Path(temporary.name).unlink(missing_ok=True)
    existing = path.read_bytes()
    if existing != data:
        if json.dumps(json.loads(existing), sort_keys=True) != json.dumps(json.loads(data), sort_keys=True):
            raise ValueError(f"Existing report differs from fixed input: {path}")


def restore(destination):
    for path in sorted(INPUTS.rglob("*.json")):
        restore_report(destination, path.relative_to(INPUTS), path.read_bytes())
    for archive_name in ("degree-56-58-survivors.tar.xz", "census-verification.tar.xz"):
        with tarfile.open(INPUTS / archive_name, "r|xz") as archive:
            for member in archive:
                name = PurePosixPath(member.name)
                if not member.isfile():
                    raise ValueError(f"Invalid census report in {archive_name}: {name}")
                with archive.extractfile(member) as stream:
                    restore_report(destination, name, stream.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=OUTPUT,
                        help="J179 output directory or a separate verification directory")
    restore(parser.parse_args().destination)
