"""
Configuration management for the Discord bot.
Handles environment variables and bot settings.
"""

import os
from bot.utils.logger import get_logger
from dotenv import load_dotenv

class Config:
    """Config class to load environment variables into the bot."""

    def __init__(self,):
        """Initialize configuration from environment variables."""
        self.logger = get_logger(__name__)
        
        # Fetching environment variables
        load_dotenv(".config")
        self.token = self.fetch_var("TOKEN")
        self.guild_id = self.fetch_var("GUILD_ID")

        # Validate config
        if self._validate():
            self.logger.info("Configuration complete")


# ────────────────────────────────────────────────────────────────
# Helper methods
# ────────────────────────────────────────────────────────────────

    def fetch_var(self, var_name):
        """Fetch variable from environment."""
        self.logger.info(f"Fetching {var_name}")
        return os.getenv(var_name)


    def _validate(self):
        """Validate critical configuration values."""
        if not self.token:
            self.logger.error("TOKEN environment variable is required!")
            return False
        if self.guild_id is not None:
            self.logger.debug(f"Fetched Guild ID: {self.guild_id}")
        return True
