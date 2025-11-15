import sys
import argparse

from bot.client import Client 
from bot.utils.logger import configure_logging, get_logger
from bot.utils.config import Config

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log_level",
        "-l",
        choices=["DEBUG", "INFO"], 
        default="INFO", 
        help="Set the logging level (default: INFO)"
    )
    return parser.parse_args()


def main():
    """Main entry point for the Discord bot."""

    # Parse command-line arguments
    args = parse_args()

    # Setup logging
    configure_logging(log_level=args.log_level)
    logger = get_logger(__name__)
    
    try:
        # Load configuration
        config = Config()
         
        # Create and run the client
        logger.info("Starting Discord bot...")
        client = Client(config)
        client.run(config.token)
        
    except KeyboardInterrupt:
        logger.info("Bot shutdown requested by user.")
    except Exception as error:
        logger.error(f"Fatal error occurred: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
