import os
import logging
import discord
from discord.ext import commands
from bot.utils.config import Config


class Client(commands.Bot):
    def __init__(self, config):
        intents = discord.Intents.all()

        super().__init__(
                command_prefix="!",
                intents=intents,
                help_command=None
                )

        self.config = config
        self.logger = logging.getLogger(__name__)
        self.guild_id = config.guild_id


    async def setup_hook(self):
        """Load all cogs and sync slash commands."""
        
        #load cogs
        for filename in os.listdir("./bot/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"bot.cogs.{filename[:-3]}")
                self.logger.info(f"Loaded {filename}")

        # sync slash commands to server
        try:
            guild = discord.Object(id=self.guild_id)
            self.tree.copy_global_to(guild=guild)
            synced_commands = await self.tree.sync(guild=guild)
            self.logger.debug(f"Synced {len(synced_commands)} commands to guild {guild.id}.")
        except Exception as e:
            self.logger.error(f"Failed to sync commands to guild {guild}")


    async def on_ready(self):
        """Event handler for when the bot is ready."""
        if self.user:
            self.logger.info(f"Bot ready! Logged in as {self.user} (ID: {self.user.id})")
        guild_list = ", ".join(f"{g.name} ({g.id})" for g in self.guilds)
        self.logger.debug(f"Connected to {len(self.guilds)} guild(s): {guild_list}")


    async def on_guild_join(self, guild: discord.Guild):
        self.logger.info(f"Joined new guild: {guild.name} (ID: {guild.id})")


    async def on_guild_remove(self, guild: discord.Guild):
        self.logger.info(f"Removed from guild: {guild.name} (ID: {guild.id})")


    async def on_error(self, event, *args, **kwargs):
        self.logger.error(f"Error in event {event}", exc_info=True)


    async def close(self):
        self.logger.info("Bot is shutting down...")
        await super().close()
