import os
import logging
from pathlib import Path
from dotenv import load_dotenv

class Config:
    """Main configuration class that handles environment and logging setup."""
    """Maj = var env"""
    """Min = classic var"""

    def __init__(self) -> None:
        log_dir: str = "logs"
        log_file: str = "boallt.log"
        logger: logging.logger | None = None
        DISCORD_TOKEN = load_env("DISCORD_TOKEN")

        self.setup_logger()


def load_env(name: str) -> str:
    """Load the Discord token from the .env file."""
    
    load_dotenv()
    
    token = os.getenv(name)
    
    if not token:
        raise RuntimeError("⚠️ Missing {token} in environment variables")
    return token


def setup_logger(self) -> logging.Logger:
    """Configure and return the main logger."""
    
    Path(self.log_dir).mkdir(exist_ok=True)

    log_path = Path(self.log_dir) / self.log_file

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger("BOALLT")
    logger.info("Logger init")
    return logger