# 🤖 Poi Alert Bot - Gold Price Telegram Alerts

A free Telegram bot that monitors gold prices and sends you alerts when the price reaches your set level.

## ✨ Features

- 📊 Real-time gold price monitoring (updated every minute)
- 🔔 Set custom price alerts (above or below)
- 💰 100% FREE (uses free APIs)
- 🚀 Deploy on Render for free
- ⚡ Runs 24/7

## 🛠️ Setup Instructions

### Step 1: Create Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/start` then `/newbot`
3. Follow the prompts:
   - Name: `Poi Alert Bot` (or anything you like)
   - Username: `poi_alert_bot_yourname` (must be unique and end with `_bot`)
4. Copy the **API Token** (looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### Step 2: Get Your Chat ID

1. Search for **@userinfobot** in Telegram
2. Send `/start`
3. Copy the **ID** number shown

### Step 3: Deploy on Render

1. Go to https://render.com (create free account if needed)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository (`Poi-alert-bot`)
4. Fill in details:
   - **Name**: `poi-alert-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
5. Click **"Advanced"** and add Environment Variables:
   - `TELEGRAM_BOT_TOKEN` = Your bot token from Step 1
   - `CHAT_ID` = Your chat ID from Step 2
6. Click **"Create Web Service"**

Wait 2-3 minutes for deployment. You should see "Your service is live" ✅

### Step 4: Use Your Bot

Send these commands to your bot on Telegram:

```
/start              - Start the bot
/price              - Get current gold price
/alert_above 2000   - Alert when price goes ABOVE $2000
/alert_below 1500   - Alert when price goes BELOW $1500
/status             - Check alert status
```

## 📡 API Used

- **Gold Price**: CoinGecko API (completely free, no API key needed)

## 🔧 How It Works

1. Bot checks gold price every 1 minute
2. If price reaches your alert threshold, you get a notification
3. Runs continuously on Render's free tier

## 📝 Price Data Source

- CoinGecko API: https://api.coingecko.com/api/v3/
- No API key required
- Free tier: Unlimited requests

## ❓ FAQ

**Q: Will this work 24/7?**
A: Yes! Render keeps it running. Note: Render free tier may have 15-minute downtimes per month.

**Q: How accurate are the prices?**
A: CoinGecko updates prices every minute with data from major exchanges.

**Q: Can I modify the bot?**
A: Yes! Edit `bot.py` and push to GitHub. Render will auto-deploy.

**Q: What if I want different commodities?**
A: Edit the `PRICE_API_URL` and `ids` parameter in bot.py to track: silver, platinum, etc.

## 🐛 Troubleshooting

**Bot not sending messages?**
- Check if `TELEGRAM_BOT_TOKEN` and `CHAT_ID` are correct
- Verify your Chat ID with @userinfobot

**Render deployment fails?**
- Check Python version is 3.9+
- Make sure requirements.txt is in the root folder
- Check Render logs for errors

## 📞 Support

For issues, check:
1. Render logs: Dashboard → Service → Logs
2. Telegram bot token validity: Send it to @BotFather
3. Make sure you're not blocked by Telegram

## 📄 License

Free to use and modify!

---

**Made with ❤️ for traders**
