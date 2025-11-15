"""
Logging utilities for the Discord bot.
Provides centralized logging configuration and setup.
"""

import logging
import logging.handlers
import os
from datetime import datetime

def configure_logging(log_level: str = "INFO"):
    """
    Set up logging configuration for the bot.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path. If None, uses default location.
    """
    # Convert string level to logging constant
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Set log file
    timestamp = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(logs_dir, f"bot_{timestamp}.log")
    
    # Configure root logger
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5,
                encoding='utf-8'
            )
        ]
    )
    
    # Set specific logger levels
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.getLogger('discord.http').setLevel(logging.WARNING)
    logging.getLogger('discord.gateway').setLevel(logging.WARNING)
    
    # Create logger for this module
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized - Level: {log_level}, File: {log_file}")
    
    return logger

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
