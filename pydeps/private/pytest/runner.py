from __future__ import annotations

import logging
import sys

import pytest

log = logging.getLogger(__name__)


def run_pytest() -> None:
    logging.basicConfig(level=logging.INFO)

    # Switching sys.stdout for an unbuffered stream prevents PDB
    # output from being buffered when runnning the test with --pdb.
    #
    # See https://github.com/python/typeshed/issues/3049 on the mypy ignore.
    sys.stdout.reconfigure(line_buffering=True)  # type: ignore[union-attr]
    pytest_exit_code = pytest.main()
    if pytest_exit_code == pytest.ExitCode.NO_TESTS_COLLECTED:
        print(
            " == FAILURE == Pytest was unable to find any tests on the path",
            file=sys.stderr,
        )
    exit(pytest_exit_code)


if __name__ == "__main__":
    run_pytest()
