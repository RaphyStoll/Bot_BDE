from dotenv import load_dotenv
import os
from logger import setup_logger
from config.py import Config




def main():
    logger = setup_logger()
    logger.info("Starting loading env")
    Config.DISCORD_TOKEN = load_env("DISCORD_TOKEN")

if __name__ == "__main__":
    main()