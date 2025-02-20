# Configuration settings for the Terminator AI Agent
import os
from dotenv import load_dotenv, dotenv_values 

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LangChain settings
LANGCHAIN_API_KEY = "your_langchain_api_key_here"

# Memory settings
MEMORY_FILE_PATH = "memory.json"

# Reminder settings
REMINDER_FILE_PATH = "reminders.json"

# Listening settings
LISTENING_LANGUAGE = "en-US"

# Speaking settings
SPEAKING_LANGUAGE = "en-US"
SPEECH_RATE = 1.0  # Normal speech rate

# Real-time data settings
DEFAULT_LOCATION = "San Francisco, CA"  # Default location for weather data

# Logging settings
LOGGING_LEVEL = "DEBUG"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Raspberry Pi specific settings
USE_GPIO_FOR_INPUT = True  # Set to True if using GPIO for input
GPIO_PIN_NUMBER = 17  # Example GPIO pin number for input