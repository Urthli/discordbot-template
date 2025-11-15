# Discord Bot Template

A lightweight Discord bot template built with Python/3.11 and `discord.py`.  
This template can serve as a starting point for you to create your own discord bot.

---

## Features

### Cogs
In ``discord.py``, cogs are a way to organize and modularize your bot’s commands and event listeners. 
They allow you to separate functionality into different classes and files, making your bot more easily maintainable.
You can import new functionalities into your bot by introducing a new cog file.
Cogs are automatically recognized and loaded into the client via the ``client.py`` script.

### Configuration
The ``bot/utils/config.py`` utility script is responsible for reading and storing the bot TOKEN stored in the ``.config`` file.

### Logging
When the bot is running, the logger will write events to the terminal and to a log file stored in ``logs/``.
You can set the log level via the ``--log_level`` argument.

---

## Directory Structure
```bash
template/
├── .config
├── main.py
├── bot/
│ ├── client.py
│ ├── cogs/
│ │ └── hellocog.py
│ ├── res/
│ └── utils/
│ ├── config.py
│ └── logger.py
└── logs/
```

| File / Folder          | Description                                                 |
| ---------------------- | ------------------------------------------------------------|
| `.config`              | Environment variables (bot token, guild ID, etc.)           |
| `main.py`              | Entry point of the bot; starts the bot client.              |
| `bot/client.py`        | Initializes the Discord bot client and loads cogs.          |
| `bot/cogs/`            | Folder containing command modules (cogs).                   |
| `bot/cogs/hellocog.py` | Example cog with a simple hello command.                    |
| `bot/utils/`           | Utility scripts for the bot (configuration, logging, etc.). |
| `bot/utils/config.py`  | Loads and validates environment variables for the bot.      |
| `bot/utils/logger.py`  | Sets up logging for the bot with console and file handlers. |
| `bot/res/`             | Resource folder for assets like images, audio, etc.         |
| `logs/`                | Folder where rotating logs are stored.                      |


---

## Prerequisites

- **Python 3.11+** installed on your system.
- **WSL2** (Windows Subsystem for Linux) if running on Windows.  
  For detailed installation instructions, see the official guide: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

---

## Setup Instructions

### Discord Developer Portal
Follow [these instructions](https://discordpy.readthedocs.io/en/stable/discord.html) to register your bot on the discord developer portal.

> **Note:** When selecting the **scopes** for your bot, be sure to select both the **bot** and **applications.commands** scopes.
> ![bot scopes](https://i.imgur.com/mEev4QD.png)

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/Urthli/discordbot-template.git
cd template
```

2. **install dependencies**

The following setup was tested on WSL2.
To setup WSL2, see: 

```bash
python -m venv .venv
source venv/bin/activate

pip install -U discord.py python-dotenv
```

3. **Create your** ``.config`` **file**
```env
TOKEN=your_discord_bot_token
GUILD_ID=your_guild_id  # optional, for slash command syncing
```

4. **Run the bot**
```bash
python main.py
```

