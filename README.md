[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=36BCF7F1&width=435&lines=Welcome+To+Adavance+MD+Auto+Delete+Bot;Bot+is+Made+By+Mohammed)](https://git.io/typing-svg)

---

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3"/>
  </a>
  <a href="https://docs.pyrogram.org/" target="_blank">
    <img src="https://img.shields.io/badge/Framework-Pyrogram-brightgreen?style=for-the-badge&logo=pyrogram&logoColor=white" alt="Pyrogram"/>
  </a>
  <a href="https://t.me/Mr_Mohammed_29" target="_blank">
    <img src="https://img.shields.io/badge/Developer-Mohammed-purple?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer"/>
  </a>
  <a href="https://t.me/+7fPakZrGvAg5OTM1" target="_blank">
    <img src="https://img.shields.io/badge/Support-Group-blueviolet?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group"/>
  </a>
</p>

## 🚀 Project Status

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Telegram-blue)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)

# 🤖 MD Auto Delete Bot

![Repo Size](https://img.shields.io/github/repo-size/MohammedDev-yt/MD-Auto-Delete-Bot)
![Stars](https://img.shields.io/github/stars/MohammedDev-yt/MD-Auto-Delete-Bot?style=social)
![Forks](https://img.shields.io/github/forks/MohammedDev-yt/MD-Auto-Delete-Bot?style=social)
![Last Commit](https://img.shields.io/github/last-commit/MohammedDev-yt/MD-Auto-Delete-Bot)

## ✨ Features

- 🕒 Auto-delete group messages after custom time (seconds)
- 🔐 Admin-only controls (`/set_time`, `/disable`, `/status`)
- 📌 Force Subscribe system (channel join required)
- 👮 Admin messages are never deleted
- 💾 MongoDB-based storage system
- 📊 Per-group delete timer settings
- 📢 Broadcast system (users & groups)
- 🎛 Inline button UI (Start / Help / About / Back)
- ⚡ Flask keep-alive server (24/7 uptime support)
- 🚀 Fully async and high-performance bot

---

## 🧰 Tech Stack

- Python 3
- Pyrogram 2.x
- MongoDB (Motor async driver)
- Flask (Keep-alive server)

---

# Environment Variables 

| Variable        | Description                                  | Example / Format              |
|----------------|----------------------------------------------|-------------------------------|
| API_ID         | Your Telegram API ID                         | 123456                        |
| API_HASH       | Your Telegram API Hash                       | abcdef1234567890abcdef       |
| BOT_TOKEN      | Bot token from BotFather                     | 123456:ABC-DEF1234ghIkl      |
| DATABASE_URL      | MongoDB connection string                    | mongodb+srv://user:pass@...  |
| OWNER_ID       | Telegram user ID of bot owner                | 987654321                    |
| BOT_USERNAME   | Bot username (without @)                     | AU_AutoDelete_bot
| FORCE_SUB_CHANNEL | Without @ | Anime_UpdatesAU       |
| PORT  | 8080 |


---

## 📚 Commands

```
- start - check bot is alive or not
- set_time 10 - set auto delete timer [Owner Only]
- disable - disable auto delete [Owner Only]
- status - show current timer [Owner Only]
- broadcast <msg>` - send message to users [Owner Only]
- users - total users [Owner Only]
```
---

<details>
<summary><h3>
- <b> ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs </b>
</h3></summary>

<h3 align="center">
    ─「 ᴅᴇᴘʟᴏʏ ᴏɴ ʀᴇɴᴅᴇʀ 」─
</h3>

<p align="center">
<a href="https://render.com/deploy?repo=https://github.com/MohammedDev-yt/MD-Auto-Delete-Bot">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>
</p>

---

<h3 align="center">
    ─「 ᴅᴇᴘʟᴏʏ ᴏɴ ʀᴇᴘʟɪᴛ 」─
</h3>

<p align="center">
<a href="https://replit.com/github/MohammedDev-yt/MD-Auto-Delete-Bot">
<img src="https://img.shields.io/badge/Deploy%20on-Replit-black?style=for-the-badge&logo=replit" alt="Deploy on Replit">
</a>
</p>

---

<h3 align="center">
    ─「 ᴅᴇᴘʟᴏʏ ᴏɴ ʀᴀɪʟᴡᴀʏ 」─
</h3>

<p align="center">
<a href="https://railway.com/new/github/MohammedDev-yt/MD-Auto-Delete-Bot">
<img src="https://img.shields.io/badge/Deploy%20on-Railway-purple?style=for-the-badge&logo=railway" alt="Deploy on Railway">
</a>
</p>

</details>

<details><summary>How To Keep Your Bot Alive</summary>
<br>
<b>Use these settings while deploying on Render:</b>
<br><br>
• Runtime: <code>Docker</code>
<br><br>
• Build Command:
<code>pip install -r requirements.txt</code>
<br><br>
• Start Command:
<code>python main.py</code>
<br><br>
<b>🌐 Keep Bot Alive 24/7 Using UptimeRobot</b>
<br><br>
Go to:
https://uptimerobot.com/
<br><br>
Click:
<b>Add New Monitor</b>
<br><br>
Use these settings 👇
<br><br>
<img src="https://telegra.ph/file/a79a156e44f43c9833b50.jpg">
<br><br>
<b>Type:</b>
<code>HTTP(s)</code>
<br><br>
<b>URL:</b>
<code>https://your-render-app.onrender.com</code>
<br><br>
<b>Monitoring Interval:</b>
<code>5 Minutes</code>
<br><br>
After adding monitor click:
<b>Create Monitor</b>
<br><br>
✅ Your bot will stay alive 24/7.
</details>
