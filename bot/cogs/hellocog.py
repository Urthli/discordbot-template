import os
import discord
from discord import app_commands
from discord.ext import commands
from bot.utils.logger import get_logger

BASE_PATH = "res/scenarios"

class HelloCog(commands.Cog):
    def __init__(self, client):
        self.logger = get_logger(__name__)
        self.client = client

    @app_commands.command(name="hello", description="say hello")
    async def hello(self, interaction: discord.Interaction):
        """Say Hello to interaction.user"""
        msg = f"Hello {interaction.user.display_name}"
        try:
            self.logger.info(f"response: '{msg}'")
            await interaction.response.send_message(msg)
        except Exception as e:
            self.logger.error(f"Error: {e}", exc_info=True)


# ────────────────────────────────────────────────────────────────
# Load Cog into client
# ────────────────────────────────────────────────────────────────

async def setup(client):
    await client.add_cog(HelloCog(client))
