import os
from pyrogram import Client, filters
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie, TV

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID", "24196359"))
API_HASH = os.getenv("API_HASH", "20a1b32381ed174799e8af8def3e176b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "744cb86428114a0aab28286b9687bbfe")

# TMDB setup
tmdb = TMDb()
tmdb.api_key = TMDB_API_KEY
tmdb.language = "en"

movie_api = Movie()
tv_api = TV()

# Create Pyrogram Client
app = Client(
    "OTT-Poster-Scrapper-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ------------------- Handlers ------------------- #

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention},\n\n"
        "I am an **OTT Poster Scrapper Bot** 🎬\n"
        "Send me a movie/series name with `/poster <name>` to get posters and info!"
    )

@app.on_message(filters.command("poster") & filters.private)
async def poster_handler(client, message):
    query = message.text.split(maxsplit=1)
    if len(query) < 2:
        await message.reply_text("❌ Please give me a movie/series name.\n\nExample: `/poster Inception`")
        return
    
    title = query[1]
    results = movie_api.search(title)

    if not results:
        results = tv_api.search(title)

    if not results:
        await message.reply_text("❌ No results found.")
        return

    first = results[0]
    poster_url = f"https://image.tmdb.org/t/p/w500{first.poster_path}"

    caption = (
        f"🎬 **{first.title if hasattr(first,'title') else first.name}**\n"
        f"⭐ {first.vote_average}/10\n"
        f"📅 {first.release_date if hasattr(first,'release_date') else first.first_air_date}"
    )

    await message.reply_photo(poster_url, caption=caption)

# ------------------- Run Bot ------------------- #
if __name__ == "__main__":
    print("🚀 Bot Started...")
    app.run()
