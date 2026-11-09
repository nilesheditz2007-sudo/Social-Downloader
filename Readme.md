# 🚀 Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ Dᴏᴡɴʟᴏᴀᴅᴇʀ API 📥

**« ⚡ Fᴀsᴛ • Lɪɢʜᴛᴡᴇɪɢʜᴛ • Pᴏᴡᴇʀғᴜʟ • Vᴇʀᴄᴇʟ Rᴇᴀᴅʏ »**

A ᴘᴏᴡᴇʀғᴜʟ ᴀɴᴅ ғᴀsᴛ Fʟᴀsᴋ-ʙᴀsᴇᴅ Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ Dᴏᴡɴʟᴏᴀᴅᴇʀ API ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴅɪʀᴇᴄᴛ ᴍᴇᴅɪᴀ ʟɪɴᴋs ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ᴘʟᴀᴛғᴏʀᴍs. 🚀

!
━━━━━━━━━━━━━━━━━━━━━━━━

## ✨ Fᴇᴀᴛᴜʀᴇs

- 📸 **Iɴsᴛᴀɢʀᴀᴍ** — Rᴇᴇʟs • Pᴏsᴛs • Sᴛᴏʀɪᴇs • Hɪɢʜʟɪɢʜᴛs • Pʀᴏғɪʟᴇs
- 👥 **Fᴀᴄᴇʙᴏᴏᴋ** — HD • SD Vɪᴅᴇᴏ Lɪɴᴋs
- 👻 **Sɴᴀᴘᴄʜᴀᴛ** — Dɪʀᴇᴄᴛ Vɪᴅᴇᴏ • Iᴍᴀɢᴇ
- 📌 **Pɪɴᴛᴇʀᴇsᴛ** — Vɪᴅᴇᴏ • Hɪɢʜ-Rᴇsᴏʟᴜᴛɪᴏɴ Pʜᴏᴛᴏ
- ▶️ **YᴏᴜTᴜʙᴇ** — Vɪᴅᴇᴏ Dᴏᴡɴʟᴏᴀᴅ
- ⚡ **Fᴀsᴛ & Lɪɢʜᴛᴡᴇɪɢʜᴛ**
- ☁️ **Vᴇʀᴄᴇʟ Rᴇᴀᴅʏ**
- 🔗 **Sɪᴍᴘʟᴇ REST API**

━━━━━━━━━━━━━━━━━━━━━━━━

## 📡 Aᴘɪ Eɴᴅᴘᴏɪɴᴛs

### 🏠 1. Rᴏᴏᴛ / Hᴇᴀʟᴛʜ Cʜᴇᴄᴋ

> Gᴇᴛ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴇɴᴅᴘᴏɪɴᴛs ᴀɴᴅ Dᴇᴠᴇʟᴏᴘᴇʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ.

```http
GET /
```

### 📘 2. Fᴀᴄᴇʙᴏᴏᴋ

```http
GET /facebook?video=URL
```

### 📸 3. Iɴsᴛᴀɢʀᴀᴍ

```http
GET /Instagram?video=URL
```

### 📌 4. Pɪɴᴛᴇʀᴇsᴛ

```http
GET /Pinterest?video=URL
GET /youtube?video=URL
```

### 👻 5. Sɴᴀᴘᴄʜᴀᴛ

```http
GET /snap?video=URL
```

━━━━━━━━━━━━━━━━━━━━━━━━

## 📦 Rᴇsᴘᴏɴsᴇ Exᴀᴍᴘʟᴇ

```json
{
  "Developer": "t.me/dg_drift",
  "Endpoints": {
    "Facebook": "/facebook?video=URL",
    "Instagram": "/Instagram?video=URL",
    "Pinterest": "/Pinterest?video=URL",
    "Snapchat": "/snap?video=URL"
  },
  "Main Channel": "@DGDRIFT",
  "Owner": "@DG_DRIFT"
}
```

━━━━━━━━━━━━━━━━━━━━━━━━

## 📋 Eɴᴅᴘᴏɪɴᴛ Sᴜᴍᴍᴀʀʏ

| Endpoint | Method | Parameter | Description |
|----------|--------|-----------|-------------|
| `/` | `GET` | — | Health check & endpoint list |
| `/facebook` | `GET`, `POST` | `video` | Facebook video downloader |
| `/Instagram` | `GET`, `POST` | `video` | Instagram Reels / Post / Story / Profile |
| `/snap` | `GET`, `POST` | `video` | Snapchat video & image |
| `/Pinterest` | `GET`, `POST` | `video` | Pinterest video & photo |
| `/youtube` | `GET`, `POST` | `video` | YouTube video downloader |

━━━━━━━━━━━━━━━━━━━━━━━━

## 💻 Rᴜɴɴɪɴɢ Lᴏᴄᴀʟʟʏ

**1️⃣ Clone or download this project folder.**

**2️⃣ Install dependencies:**

```bash
pip install -r requirements.txt
# YouTube support uses yt-dlp
```

**3️⃣ Run the Flask server:**

```bash
python api.py
```

**4️⃣ Access the API locally:**

```
http://127.0.0.1:5150/
```

━━━━━━━━━━━━━━━━━━━━━━━━

## ☁️ Dᴇᴘʟᴏʏᴍᴇɴᴛ

- 🚀 **Vᴇʀᴄᴇʟ Rᴇᴀᴅʏ**
- ⚙️ **Fʟᴀsᴋ + Pʏᴛʜᴏɴ**
- 🔗 **REST API Sᴜᴘᴘᴏʀᴛ**

### 🔧 Option A — Vercel CLI

```bash
npm install -g vercel
vercel
```

### 🐙 Option B — GitHub + Vercel Dashboard

1. Upload this project to **GitHub**
2. Import on the [Vercel Dashboard](https://vercel.com/dashboard)
3. Click **Deploy** 🚀

━━━━━━━━━━━━━━━━━━━━━━━━

## ⚠️ Iᴍᴘᴏʀᴛᴀɴᴛ Nᴏᴛᴇs

- 📌 All endpoints accept the URL via the **`video`** parameter.
- 📌 Use **query string** or **form-data / x-www-form-urlencoded** for POST requests. JSON body is **not** supported.
- 📌 Flask routes are **case-sensitive** — `/Instagram` and `/instagram` are treated differently.

━━━━━━━━━━━━━━━━━━━━━━━━

## 👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ Iɴғᴏ
👤 Nᴀᴍᴇ : Dɢ Dʀɪғᴛ
⚡ Bʀᴀɴᴅ : Dɢ Dʀɪғᴛ
💻 Rᴏʟᴇ : Fᴜʟʟ Sᴛᴀᴄᴋ Dᴇᴠᴇʟᴏᴘᴇʀ
🚀 Pʀᴏᴊᴇᴄᴛ : Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ Dᴏᴡɴʟᴏᴀᴅᴇʀ Aᴘɪ
📡 Sᴜᴘᴘᴏʀᴛ : @DG_DRIFT

━━━━━━━━━━━━━━━━━━━━━━━━

## ⚡ Dʀɪғᴛ Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ Dᴏᴡɴʟᴏᴀᴅᴇʀ

**« 🔥 Fᴀsᴛ • Sᴍᴏᴏᴛʜ • Sɪᴍᴘʟᴇ • Pᴏᴡᴇʀғᴜʟ 🚀 »**

━━━━━━━━━━━━━━━━━━━━━━━━
🙂🙂 ##  padhai hogya to channel per jao https://t.me/dgdrift
