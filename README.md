# 🎬 OTT PosterBot — Prime Video, ZEE5, AirtelXstream, YouTube & GDFlix Scraper 🤖

A powerful Telegram bot to **scrape high-quality OTT posters** (movies, series, and seasons) from  
**🎬 Prime Video**, **📺 ZEE5**, **📡 AirtelXstream**, **📹 YouTube**, and **📁 GDFlix/GDLink downloaders**, and auto-post them to your Telegram channel — with just a link or command.

> ⚡ Built with Pyrogram, MongoDB & BeautifulSoup  
> 🚀 Maintained by [@PBX1_BOTS](https://t.me/PBX1_BOTS) × [HG BOTZ](https://t.me/HGBOTZ)

---

## 📌 Features

- 🖼️ Poster extraction from:
  - 🎬 **Prime Video** (Movies & Series)
  - 📺 **ZEE5**
  - 📡 **AirtelXstream**
  - 📹 **YouTube** *(auto-thumbnail fetch from videos)*
- 📁 File Link Extraction from:
  - 🌐 **GDFlix** / **GDLink** (full scraping with resume links, mirrors, gofile, pixeldrain, etc.)
- 🎯 Season-specific poster support (`/poster s01 <link>`)
- 🔗 Auto-post to Telegram channel via `/post <link>`
- 🔍 Prime Video search via `/search <title>`
- 🔐 MongoDB-based user authorization
- 📊 Admin-only usage stats
- 📤 ImgBB integration for fast poster hosting
- 💨 Deployable to Heroku, Railway, Render, Docker, Replit, Glitch, Fly.io

---

## 💬 Commands

| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `/start`                 | Start the bot                                    |
| `/help`                  | Show available commands                          |
| `/prime <link>`          | Get **Prime Video** poster                       |
| `/zee5 <link>`           | Get **ZEE5** poster                              |
| `/airtel <link>`         | Get **AirtelXstream** poster                     |
| `/yt <youtube_link>`     | Get **YouTube** video poster (thumbnail)         |
| `/poster s01 <link>`     | Fetch specific season poster                     |
| `/post <link>`           | Auto-post any OTT or YouTube poster              |
| `/search <title>`        | Prime Video title search                         |
| `/scrape <gdflix_link>`  | Extract direct download links from GDFlix/GDLink |
| `/authorize <user_id>`   | ➕ (Admin) Authorize a user                       |
| `/unauthorize <id>`      | ➖ (Admin) Revoke access                          |
| `/authlist`              | List of authorized users                         |
| `/stats`                 | Show usage stats (Admin only)                    |

---

## 🔎 GDFlix / GDLink Scraper (Advanced) 🎯

Use the `/scrape <gdflix_link>` command to extract all **actual download links** from GDFlix-style pages like:

- `https://gdlink.dev/...`
- `https://gdflix/...`
- `https://vifix.site/...`
- `https://new10.gdflix.dad/...`

### ✅ What it extracts:

- **Direct cloud buttons**: `INSTANT DL`, `CLOUD DOWNLOAD`, `DRIVEBOT`, `TELEGRAM FILE`, `LOGIN TO DL`
- **Fast cloud redirect**: Follows `FAST CLOUD` → `XFile` → `CLOUD RESUME DOWNLOAD`
- **Mirror pages**: Detects and extracts from mirror hosts like:
  - 🗂 **GOFILE**
  - 🌀 **PIXELDRAIN**
  - 💨 Others can be extended...

### 📦 Output Format:

```text
📁 Title
🎥 Movie.Name.2024.1080p.WEB-DL

📦 Size :- 1.2GB

☁️ CLOUD DOWNLOAD : Click Here  
⚡ INSTANT DL : Click Here  
🗂 GOFILE : Click Here  
🌀 PIXELDRAIN : Click Here  

━━━━━━━━━━━━━━━━━━  
⚡ Powered By @PBX1_BOTS🚀
```

### 🔹 Heroku

```bash
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
```
## 🔹 Railway
```
Go to railway.app

Create new project → GitHub repo

Add ENV variables and deploy
```
## 🔹 Render
```
Visit render.com

New Web Service → Connect GitHub

Set start command: python3 bot.py

Add ENV vars and deploy
```
## 🔹 Docker
```
git clone https://github.com/yourusername/ott-posterbot
cd ott-posterbot
docker build -t posterbot .
docker run -d \
  -e API_ID=... \
  -e API_HASH=... \
  -e BOT_TOKEN=... \
  -e MONGO_URL=... \
  -e CHANNEL_ID=... \
  posterbot
  ```
## 📚 Dependencies
```
pyrogram
tgcrypto
pymongo
requests
beautifulsoup4
python-dotenv
```

## 👨‍💻 Maintainer

Made with ❤️ by [PBX1_BOTS](https://t.me/PBX1_BOTS) X [HG BOTZ](https://t.me/HGBOTZ)

