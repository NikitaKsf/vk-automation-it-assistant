# config/vk_config.py
import os
from dotenv import load_dotenv

load_dotenv()

VK_ACCESS_TOKEN = os.getenv('VK_ACCESS_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')
VK_API_VERSION = os.getenv('VK_API_VERSION', '5.199')
VK_SECRET_KEY = os.getenv('VK_SECRET_KEY')

DATA_QUOTES_DIR = os.getenv('DATA_QUOTES_DIR', 'data/quotes')
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
CACHE_ENABLED_STR = os.getenv('CACHE_ENABLED', 'False')
CACHE_ENABLED = CACHE_ENABLED_STR.lower() in ('true', '1', 'yes')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

if not VK_ACCESS_TOKEN:
    print("FATAL ERROR: VK_ACCESS_TOKEN not found in .env file. Please set it.")
    exit()
if not VK_GROUP_ID:
    print("FATAL ERROR: VK_GROUP_ID not found in .env file. Please set it.")
    exit()

print("--- VK Configuration Loaded ---")
print(f"VK_ACCESS_TOKEN: {'...' + VK_ACCESS_TOKEN[-4:] if VK_ACCESS_TOKEN else 'Not Found'}")
print(f"VK_GROUP_ID: {VK_GROUP_ID}")
print(f"VK_API_VERSION: {VK_API_VERSION}")
print(f"VK_SECRET_KEY: {'Set' if VK_SECRET_KEY else 'Not Set'}")
print(f"DATA_QUOTES_DIR: {DATA_QUOTES_DIR}")
print(f"TG_BOT_TOKEN: {'Set' if TG_BOT_TOKEN else 'Not Set'}")
print(f"DATABASE_URL: {'Set' if DATABASE_URL else 'Not Set'}")
print(f"CACHE_ENABLED: {CACHE_ENABLED}")
print(f"LOG_LEVEL: {LOG_LEVEL}")
print("-----------------------------")




