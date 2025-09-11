# app.py
import os
import re
import logging
import requests
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup

# ----------------- CONFIG -----------------
load_dotenv()
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_ID = os.getenv("CHANNEL_ID", None)

# Admins (comma separated user IDs in .env)
ADMINS = [int(x) for x in os.getenv("ADMINS", "").split(",") if x.strip().isdigit()]

# TMDB API
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")
TMDB_URL = "https://api.themoviedb.org/3"

if not (API_ID and API_HASH and BOT_TOKEN):
    raise SystemExit("Please set API_ID, API_HASH and BOT_TOKEN in environment")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client("posterbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# ----------------- HELPERS -----------------
def is_admin(user_id: int) -> bool:
    return user_id in ADMINS


def get_tmdb_data(query: str, search_type: str = "multi"):
    """
    Search TMDB and return first result dict.
    search_type: multi, movie, tv
    """
    if not TMDB_API_KEY:
        return None
    try:
        resp = requests.get(
            f"{TMDB_URL}/search/{search_type}",
            params={"api_key": TMDB_API_KEY, "query": query, "language": "en-US"},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        if data.get("results"):
            return data["results"][0]
    except Exception as e:
        logger.error(f"TMDB search error: {e}")
    return None


def format_tmdb_result(item: dict):
    """Return nicely formatted caption + poster URL"""
    title = item.get("title") or item.get("name") or "Unknown"
    date = item.get("release_date") or item.get("first_air_date") or "N/A"
    overview = item.get("overview") or "No overview available."
    poster_path = item.get("poster_path")
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    caption = f"🎬 **{title}**\n📅 {date}\n\n{overview}"
    return poster_url, caption


async def send_poster(message: Message, url: str, caption: str):
    if url:
        await message.reply_photo(url, caption=caption)
    else:
        await message.reply_text(caption)


# ----------------- COMMANDS -----------------
@app.on_message(filters.command(["start", "help"]))
async def start_cmd(client, message: Message):
    txt = (
        "👋 Hello! I am an **OTT Poster Scraper Bot**.\n\n"
        "✨ Features:\n"
        "• Scrape posters from Prime, Zee5, Airtel, YouTube etc.\n"
        "• Search and fetch posters from **TMDB**\n"
        "• Auto-post posters to your channel (admins only)\n\n"
        "📌 Commands:\n"
        "/tmdb <title> - Get poster & details from TMDB\n"
        "/post <link> - Post OTT poster to channel (admin only)\n"
        "/broadcast <msg> - Send message to all users (admin only)\n"
    )
    await message.reply_text(txt)


@app.on_message(filters.command("tmdb"))
async def tmdb_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/tmdb Inception`", quote=True)
    query = " ".join(message.command[1:])
    item = get_tmdb_data(query)
    if not item:
        return await message.reply("No results found on TMDB.", quote=True)
    poster_url, caption = format_tmdb_result(item)
    await send_poster(message, poster_url, caption)


@app.on_message(filters.command("post"))
async def post_cmd(client, message: Message):
    if not is_admin(message.from_user.id):
        return await message.reply("🚫 You are not an admin.")
    if len(message.command) < 2:
        return await message.reply("Usage: `/post <link>`")
    url = message.command[1]
    # Here you can reuse your OTT scrapers (Prime, Zee5, Airtel, etc.)
    await message.reply(f"✅ Posted poster for: {url}")


@app.on_message(filters.command("broadcast"))
async def broadcast_cmd(client, message: Message):
    if not is_admin(message.from_user.id):
        return await message.reply("🚫 You are not an admin.")
    if len(message.command) < 2:
        return await message.reply("Usage: `/broadcast hello users`")
    text = " ".join(message.command[1:])
    # ⚠️ Replace with your MongoDB user list or saved users
    user_ids = ADMINS  # for demo, send only to admins
    for uid in user_ids:
        try:
            await client.send_message(uid, text)
        except Exception as e:
            logger.warning(f"Broadcast fail {uid}: {e}")
    await message.reply("📢 Broadcast completed.")


# ----------------- RUN -----------------
if __name__ == "__main__":
    print("✅ Bot started...")
    app.run()
