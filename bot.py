#Don't Remove Credit @Hgbotz 
# ===== COMMAND HANDLERS =====
@client.on_message(filters.command(["sunnext", "hulu", "stage", "adda", "wetv", "plex", "iqiyi", "aha", "shemaroo", "apple"]))
async def ott_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("ðŸ”— Please provide an OTT URL.\n\nExample:\n`/sunnext https://...`")

    ott_url = message.text.split(None, 1)[1].strip()
    api_url = f"https://hgbots.vercel.app/bypaas/asa.php?url={ott_url}"
    await handle_ott_command(message, api_url)

@client.on_message(filters.command("airtel"))
async def airtel_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("ðŸ”— Please provide an Airtel OTT URL.\n\nExample:\n`/airtel https://...`")
#Don't Remove Credit @Hgbotz 
    ott_url = message.text.split(None, 1)[1].strip()
    api_url = f"https://hgbots.vercel.app/bypaas/airtel.php?url={ott_url}"
    await handle_ott_command(message, api_url)

@client.on_message(filters.command("zee"))
async def zee_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("ðŸ”— Please provide a Zee OTT URL.\n\nExample:\n`/zee https://...`")
#Don't Remove Credit @Hgbotz 
    ott_url = message.text.split(None, 1)[1].strip()
    api_url = f"https://hgbots.vercel.app/bypaas/zee.php?url={ott_url}"
    await handle_ott_command(message, api_url)

@client.on_message(filters.command("prime"))
async def prime_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("ðŸ”— Please provide a Prime OTT URL.\n\nExample:\n`/prime https://...`")

    ott_url = message.text.split(None, 1)[1].strip()
    api_url = f"https://primevideo.pbx1bots.workers.dev/?url={ott_url}"
    await handle_ott_command(message, api_url)
#Don't Remove Credit @Hgbotz 
# ===== RUN BOT =====
client.run()
