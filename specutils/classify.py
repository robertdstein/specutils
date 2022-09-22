import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def run_snid(
        file_path: Path | str
):
    cmd = f"snid {file_path}"

    logger.info(f"Exectuing: '{cmd}'")

    subprocess.run(cmd, shell=True)
