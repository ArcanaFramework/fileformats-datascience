import os
import logging
from pathlib import Path
import typing as ty
import tempfile
import pytest

# Set DEBUG logging for unittests

log_level = logging.WARNING

logger = logging.getLogger("fileformats")
logger.setLevel(log_level)

sch = logging.StreamHandler()
sch.setLevel(log_level)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sch.setFormatter(formatter)
logger.addHandler(sch)


# For debugging in IDE's don't catch raised exceptions and let the IDE
# break at it
if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)  # type: ignore[misc]
    def pytest_exception_interact(call: ty.Any) -> None:
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)  # type: ignore[misc]
    def pytest_internalerror(excinfo: ty.Any) -> None:
        raise excinfo.value


@pytest.fixture
def work_dir() -> Path:
    work_dir = tempfile.mkdtemp()
    return Path(work_dir)
