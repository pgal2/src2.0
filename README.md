# 📥 Restricted Content Download Bot

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-Latest-green.svg)](https://github.com/pyrogram/pyrogram)
[![MongoDB](https://img.shields.io/badge/MongoDB-Compatible-green.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-Educational-red.svg)](#license)

**Professional Telegram Bot for Downloading Restricted Content**

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Configuration](#-configuration) • [Deployment](#-deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📋 Commands](#-commands)
- [💰 Premium Pricing](#-premium-pricing)
- [📥 How to Download](#-how-to-download)
- [⚙️ Configuration](#-configuration)
- [🗄️ Database Structure](#-database-structure)
- [📦 Installation](#-installation)
- [📂 Project Structure](#-project-structure)
- [🔧 Technical Details](#-technical-details)
- [🚀 Deployment](#-deployment)
- [🐛 Troubleshooting](#-troubleshooting)
- [📞 Support](#-support)

---

## Overview

A high-performance Telegram bot designed to download restricted content from private channels, groups, and bots with advanced features like:

- 🔐 **Secure Authentication** - Session-based login
- 💎 **Premium System** - Unlimited downloads for premium users
- 📤 **Channel Forwarding** - Auto-upload with custom settings
- 📝 **Smart Captions** - Dynamic variables support
- 🎬 **Media Control** - Custom thumbnails & metadata
- 🏷️ **File Filters** - Choose which content types to forward
- ⚡ **Batch Processing** - Download up to 20,000 files at once (Premium)
- 📦 **Send as Document/Media** - Toggle upload type
- ♻️ **Word Replacement** - Auto replace/remove words in captions and filenames

**Made by:** [@tataa_sumo](https://t.me/tataa_sumo)  
**Channel:** [@idfinderpro](https://t.me/idfinderpro)

---

## ✨ Features

### 🔐 **Authentication System**
- ✅ Secure login with Telegram account
- ✅ Session-based authentication
- ✅ Auto-join private channels via invite links
- ✅ Session management with `/login` and `/logout`

### 💎 **Premium Membership**
| Plan | Downloads/Day | Features |
|------|:-------------:|----------|
| **Free** | 10 | Basic downloads, 10 files/batch |
| **Premium** | Unlimited | Advanced settings + 20,000 files/batch |

**Pricing:**
- ₹10 - 1 Day
- ₹40 - 7 Days
- ₹100 - 30 Days

**Code Redemption:** Codes EXTEND existing subscriptions!

### 📥 **Download Capabilities**
- ✅ Download from private channels
- ✅ Download from public channels
- ✅ Download from bots
- ✅ Batch download support (ranges)
- ✅ Original filename preservation
- ✅ Auto file cleanup
- ✅ Horizontal progress bars
- ✅ Real-time speed display

### 📤 **Advanced Channel Forwarding**
- ✅ Auto-forward downloaded files to your channel
- ✅ Custom destination channel setup
- ✅ Admin verification
- ✅ Full permission checks

### 📝 **Smart Caption System**
- ✅ Custom captions with dynamic variables:
  - `{caption}` - Original file caption
  - `{filename}` - File name with suffix
  - `{IndexCount}` - Auto-incrementing counter
- ✅ Customizable caption templates

### 🎬 **Media Processing**
- ✅ Custom video thumbnails
- ✅ Custom PDF thumbnails
- ✅ Filename suffixes (copyright protection)
- ✅ Space-formatted suffixes: `Name @Suffix .mp4`
- ✅ **Send as Document/Media toggle** - Choose upload method
- ✅ **Word Replacement** - Auto replace/remove words

### 🏷️ **Content Filters**
Choose which file types to forward:
- ✅ Text
- ✅ Documents
- ✅ Videos
- ✅ Photos
- ✅ Audio
- ✅ Voice Messages
- ✅ Animations
- ✅ Stickers
- ✅ Polls

**All enabled by default** - Toggle on/off as needed!

### 🔒 **Force Subscription**
- ✅ Users must join @idfinderpro channel
- ✅ Automatic membership verification
- ✅ Join button for easy subscription

### 👨‍💻 **Admin Panel**
- ✅ Generate redeem codes (1-50 codes at once)
- ✅ Manage premium users
- ✅ View statistics
- ✅ Broadcast messages

### 🚀 **Performance Optimizations**
- ✅ Per-file download counting (accurate tracking)
- ✅ Batch size limits (10 free, 20,000 premium)
- ✅ Download timeout protection (10 minutes)
- ✅ Improved cancellation (<5 seconds)
- ✅ Multi-user file isolation (no conflicts)
- ✅ Automatic file cleanup on cancel/error

---

## 🚀 Quick Start

### **For Users:**

1. **Start the bot**
   ```
   /start
   ```

2. **Join channel** (Required)
   ```
   @idfinderpro
   ```

3. **Login**
   ```
   /login
   ```

4. **Send any Telegram post link**
   ```
   https://t.me/channel/123
   ```

5. **Get your content!** ✅

### **For Premium Features:**

```
/settings          # Configure forwarding
/premium           # Check pricing & upgrade
/redeem <code>     # Activate premium code
```

---

## 📋 Commands

### **Main Commands**
| Command | Description |
|---------|-------------|
| `/start` | Start bot & check status |
| `/help` | Interactive help guide |
| `/login` | Authenticate with Telegram |
| `/logout` | Logout from account |
| `/cancel` | Stop ongoing download |

### **Premium Commands**
| Command | Description |
|---------|-------------|
| `/premium` | View pricing & upgrade |
| `/redeem <code>` | Redeem premium code |

### **Advanced Features**
| Command | Description |
|---------|-------------|
| `/settings` | Configure forwarding settings |
| `/batch` | Batch download guide |

### **Admin Commands**
| Command | Description |
|---------|-------------|
| `/admin` | Admin panel |
| `/generate` | Generate redeem codes (1-50) |
| `/premiumlist` | Manage premium users |

---

## 💰 Premium Pricing

| Duration | INR | USDT (approx) | Benefits |
|----------|:---:|:-------------:|----------|
| **1 Day** | ₹10 | ~$0.12 | Unlimited downloads |
| **7 Days** | ₹40 | ~$0.48 | Unlimited downloads |
| **30 Days** | ₹100 | ~$1.20 | Unlimited downloads |

### **Payment Methods**
- UPI
- Bank Transfer
- Cryptocurrency
- Telegram Stars

**Contact:** [@tataa_sumo](https://t.me/tataa_sumo) for payment details

---

## 📥 How to Download

### **Public Channels**
```
https://t.me/channelname/123
```

### **Private Channels**
1. Send invite link:
   ```
   https://t.me/+InviteHash
   ```
2. Then send post link:
   ```
   https://t.me/c/123456789/100
   ```

### **From Bots**
```
https://t.me/b/botusername/4321
```

### **Batch Download (Multiple Files)**
```
https://t.me/channel/100-110
```
This downloads messages 100 to 110!

### **Examples**
```
📌 Download 10 files:
https://t.me/mychannel/1-10

📌 Download 50 files:
https://t.me/c/1234567890/500-550

📌 Download from private:
https://t.me/c/1234567890/1-100
```

---

## ⚙️ Configuration

### **Environment Variables**

Create a `.env` file or set these variables:

```env
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
ADMINS=your_admin_user_id
DB_URI=your_mongodb_connection_string
DB_NAME=idfinderpro
FORCE_SUB_CHANNEL=idfinderpro
FORCE_SUB_CHANNEL_ID=-1002441460670
ERROR_MESSAGE=True
```

### **config.py Structure**

```python
# Bot Configuration
BOT_TOKEN = "your_token"
API_ID = 12345678
API_HASH = "your_hash"

# Database
DB_URI = "mongodb://localhost:27017"
DB_NAME = "idfinderpro"

# Admin
ADMINS = [123456789]

# Force Subscription
FORCE_SUB_CHANNEL = "idfinderpro"
FORCE_SUB_CHANNEL_ID = -1002441460670

# Error Messages
ERROR_MESSAGE = True
```

---

## 🗄️ Database Structure

### **User Collection**

```json
{
    "_id": "user_id",
    "name": "user_name",
    "session": "session_string",
    "is_premium": false,
    "premium_expiry": 1234567890,
    "downloads_today": 0,
    "last_download_date": "2025-11-02",
    "forward_destination": "channel_id",
    "custom_caption": "caption_template",
    "custom_thumbnail": "file_id",
    "filename_suffix": "@Suffix",
    "index_count": 0,
    "filter_text": true,
    "filter_document": true,
    "filter_video": true,
    "filter_photo": true,
    "filter_audio": true,
    "filter_voice": true,
    "filter_animation": true,
    "filter_sticker": true,
    "filter_poll": true,
    "send_as_document": false,
    "replace_caption_words": "find:replace",
    "replace_filename_words": "find:replace"
}
```

**Database:** MongoDB  
**Collections:** users

---

## 📦 Installation

### **1. Clone Repository**

```bash
git clone https://github.com/suryapaul01/save-restricted-bot.git
cd save-restricted-bot
```

### **2. Create Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure Bot**

Edit `config.py` with your credentials:
- Get `BOT_TOKEN` from [@BotFather](https://t.me/botfather)
- Get `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)
- Set `ADMINS` with your Telegram user ID
- Configure MongoDB connection string

### **5. Run Bot**

```bash
python bot.py
```

---

## 📂 Project Structure

```
save-restricted-bot/
├── bot.py                      # Main bot initialization
├── config.py                   # Configuration variables
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
│
├── database/
│   └── db.py                  # MongoDB operations
│
└── IdFinderPro/
    ├── start.py               # Main handlers & download logic
    ├── generate.py            # Login/Logout handlers
    ├── premium.py             # Premium system
    ├── settings.py            # Channel forwarding settings
    ├── broadcast.py           # Broadcast feature
    └── strings.py             # Help texts & messages
```

---

## 🔧 Technical Details

### **Built With**

- **[Pyrogram](https://docs.pyrogram.org/)** - MTProto API Client
- **[MongoDB](https://www.mongodb.com/)** - NoSQL Database
- **[Motor](https://motor.readthedocs.io/)** - Async MongoDB Driver
- **[Python 3.13+](https://www.python.org/)** - Programming Language

### **Architecture**

- **Async/Await** - Concurrent operations
- **Session-based Auth** - Secure authentication
- **Rate Limiting** - Prevent abuse
- **Premium System** - Tiered access
- **Force Subscription** - Channel enforcement
- **Auto Cleanup** - Storage management
- **Batch Processing** - Multiple downloads
- **Progress Tracking** - Real-time updates

### **Key Dependencies**

```txt
pyrogram==2.0.102
pymongo==4.6.0
motor==3.3.2
python-dotenv==1.0.0
```

---

## 🚀 Deployment

### **On VPS (Linux)**

```bash
# Install Python 3.13+
sudo apt update
sudo apt install python3 python3-pip

# Clone and setup
git clone https://github.com/suryapaul01/save-restricted-bot.git
cd save-restricted-bot
pip install -r requirements.txt

# Create systemd service
sudo nano /etc/systemd/system/idfinderpro.service
```

**Service file:**
```ini
[Unit]
Description=Restricted Content Download Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/save-restricted-bot
ExecStart=/usr/bin/python3 /home/ubuntu/save-restricted-bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable idfinderpro
sudo systemctl start idfinderpro
```

### **On Heroku/Koyeb**

1. Set environment variables
2. Create `Procfile`:
   ```
   worker: python bot.py
   ```
3. Deploy using Git

### **Using Docker** (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

```bash
docker build -t idfinderpro .
docker run -e BOT_TOKEN="your_token" idfinderpro
```

---

## 🐛 Troubleshooting

### **SESSION_REVOKED Error**

If you get `SessionRevoked` error:

**On Linux/VPS:**
```bash
rm -f idfinderpro.session
rm -f idfinderpro.session-journal
python3 bot.py
```

**On Windows:**
```bash
del idfinderpro.session
del idfinderpro.session-journal
python bot.py
```

### **MongoDB Connection Error**

- Verify MongoDB is running
- Check connection string in `config.py`
- Ensure IP whitelist on MongoDB Atlas

### **Bot Not Responding**

1. Check if bot is running
2. Verify `BOT_TOKEN` is correct
3. Check logs for errors
4. Restart the bot

### **WinError 32: File in use**

This occurs on Windows with file operations. The bot now includes:
- Automatic retry logic
- Proper file handle cleanup
- Sleep delays for Windows file system

---

## 📊 Rate Limits

### **Daily Limits**

| User Type | Limit |
|-----------|:-----:|
| **Free Users** | 10 downloads/day, 10 files/batch |
| **Premium Users** | Unlimited downloads, 20,000 files/batch |

**Resets:** Daily at midnight (UTC)  
**Tracking:** Per user basis

### **API Limits**

- Telegram API: 30+ requests/second
- File upload: No limit (respects Telegram)
- Download speed: Network dependent

---

## 🔒 Security

- ✅ Secure session storage in MongoDB
- ✅ Admin-only commands protected
- ✅ Force subscription enforcement
- ✅ Rate limiting to prevent abuse
- ✅ Auto file cleanup
- ✅ Encrypted session data
- ✅ No plain-text credentials in code

---

## 💡 Tips & Best Practices

- **Login First** - Always use `/login` before downloading
- **Check Premium** - Use `/premium` to verify your limits
- **Join Channel** - @idfinderpro for updates and support
- **Small Batches** - Start with small ranges (1-10) to test
- **Use Settings** - Configure channel forwarding for automation
- **Read Help** - Use `/help` for interactive guide

---

## 📞 Support

- **Channel:** [@idfinderpro](https://t.me/idfinderpro)
- **Developer:** [@tataa_sumo](https://t.me/tataa_sumo)
- **GitHub:** [suryapaul01](https://github.com/suryapaul01)

---

## 📝 License

This project is for **educational purposes only**.

**Disclaimer:** Respect Telegram's Terms of Service and local laws.

---

## 🆕 Recent Updates

### **Version 3.0 (Current)**
- ✅ **Channel Forwarding** - Auto-upload with custom settings
- ✅ **Custom Captions** - Dynamic variable support
- ✅ **Smart Filters** - Choose file types to forward
- ✅ **Thumbnails** - Custom video/PDF thumbnails
- ✅ **Filename Suffix** - Copyright protection
- ✅ **Index Counting** - Auto-increment numbers
- ✅ **Horizontal Progress Bars** - Real-time speed display
- ✅ **Bulk Code Generation** - Generate up to 50 codes at once
- ✅ **Voice/Animation/Sticker Support** - Complete media coverage
- ✅ **Send as Document/Media Toggle** - Control upload type
- ✅ **Word Replacement** - Auto replace/remove words in captions/filenames
- ✅ **Unlimited Premium** - Changed from 1000/day to unlimited
- ✅ **Batch Size Limits** - 10 free, 20,000 premium
- ✅ **Download Timeout** - 10-minute protection against stuck downloads
- ✅ **Improved Cancellation** - Stops within 5 seconds
- ✅ **File Cleanup** - Auto-cleanup on cancel/error/timeout
- ✅ **Multi-user Isolation** - User-specific filenames prevent conflicts
- ✅ **Time-Until-Reset** - Shows when free users can download again

### **Version 2.0**
- Premium membership system
- Force subscription
- Rate limiting
- Admin panel
- Redeem code system

---

## 🙏 Credits

**Developer:** Surya Paul  
**Telegram:** [@tataa_sumo](https://t.me/tataa_sumo)  
**Channel:** [@idfinderpro](https://t.me/idfinderpro)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[GitHub Repository](https://github.com/suryapaul01/save-restricted-bot) • [Channel](https://t.me/idfinderpro) • [Developer](https://t.me/tataa_sumo)

</div>
