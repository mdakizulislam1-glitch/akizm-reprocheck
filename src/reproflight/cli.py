"""Command-line interface for ReproFlight."""

import argparse
import sys

from . import __version__


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="reproflight",
        description="A local-first Python research reproducibility tool.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return

    parser.parse_args()


if __name__ == "__main__":
    main()
