# 🤖 POI Alert Bot - Gold Price Telegram Alerts

**A 100% FREE Telegram Bot that sends you real-time gold price alerts!**

---

## ✨ Features

✅ **Real-time Gold Price Monitoring** - Updated every minute
✅ **Custom Price Alerts** - Get notified above or below your price
✅ **100% FREE** - No hidden costs
✅ **24/7 Running** - Never miss an alert
✅ **Easy to Use** - Simple Telegram commands
✅ **Accurate Data** - CoinGecko Pro API

---

## 🚀 Quick Start (3 Steps)

### Step 1: Connect to GitHub

Your bot code is already in GitHub:
**https://github.com/abhijeetvishwas02stock-debug/Poi-alert-bot**

### Step 2: Deploy on Render

1. Go to **https://render.com**
2. Sign up (free account)
3. Click **"New +"** → **"Web Service"**
4. Select **"Connect to GitHub"**
5. Choose repository: **Poi-alert-bot**
6. Fill in:
   - **Name**: `poi-alert-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

7. Click **"Advanced"** and add these Environment Variables:
   ```
   TELEGRAM_BOT_TOKEN = 8820866226:AAGsQHYSsK4x_-iGeHMabKpwwv64L_Dc14M
   CHAT_ID = 8820866226
   COINGECKO_API_KEY = CG-KmG6rg5ca6UCDKZf4BfuYdqz
   ```

8. Click **"Create Web Service"**

✅ **Wait 2-3 minutes for deployment**

### Step 3: Start Using!

Open Telegram and send commands to your bot:

```
/start           - Initialize bot
/price           - Get current gold price
/alert_above 2000 - Alert when price ≥ $2000
/alert_below 1500 - Alert when price ≤ $1500
/status          - Check your alerts
/help            - Show all commands
```

---

## 📊 How It Works

```
🔄 Every 1 Minute:
  1. Check gold price from CoinGecko
  2. Compare with your alert thresholds
  3. Send Telegram notification if match
  4. Repeat forever ✅
```

---

## 💰 Your Configuration (Ready to Use)

✅ **Telegram Bot Token**: `8820866226:AAGsQHYSsK4x_-iGeHMabKpwwv64L_Dc14M`
✅ **Chat ID**: `8820866226`
✅ **CoinGecko API**: `CG-KmG6rg5ca6UCDKZf4BfuYdqz`

**Everything is pre-configured! Just deploy on Render.**

---

## 📡 APIs Used (All FREE)

| Service | Purpose | Cost | Status |
|---------|---------|------|--------|
| Telegram Bot API | Send alerts | FREE | ✅ |
| CoinGecko Pro | Gold prices | FREE | ✅ |
| Render | Hosting 24/7 | FREE | ✅ |

---

## 🎯 Example Usage

**You send:**
```
/alert_above 2050
```

**You receive:**
```
🚨 PRICE ALERT - ABOVE THRESHOLD! 🚨

💰 Gold Price: $2050.25
📈 Your Alert Level: $2050.00
⏰ Time: 2026-07-23 14:30:45

✅ Alert triggered successfully!
```

---

## ❓ FAQ

**Q: Will it really work 24/7 for free?**
A: Yes! Render's free tier runs continuously. Occasional 15-min downtimes are possible.

**Q: How accurate are the prices?**
A: CoinGecko Pro API updates every 1-2 minutes from major exchanges.

**Q: Can I change to silver, platinum, etc?**
A: Yes! Edit bot.py line `'ids': 'gold'` to `'silver'`, `'platinum'`, etc.

**Q: What if I want to stop the bot?**
A: Go to Render → Your Service → Delete/Pause

**Q: Can I modify the code?**
A: Yes! Push changes to GitHub, Render auto-deploys.

**Q: No alerts received?**
A: Check that Chat ID is correct: `8820866226`

---

## 🐛 Troubleshooting

### Bot not sending messages
- Verify Chat ID: `8820866226` ✅
- Verify Bot Token is correct ✅
- Check Render logs for errors

### Deployment failed
- Python version should be 3.9+ ✅
- Check `requirements.txt` exists ✅
- View Render logs

### Price not updating
- Verify `COINGECKO_API_KEY` is set ✅
- Check internet connection
- Wait a few minutes

**View Logs:**
Render Dashboard → Your Service → Logs

---

## 📁 Files Included

```
Poi-alert-bot/
├── bot.py              ← Main bot code (ready to use)
├── requirements.txt    ← Dependencies
├── Procfile           ← Render configuration
├── runtime.txt        ← Python version
└── README.md          ← This file
```

---

## ✅ Deployment Checklist

- ✅ Repository created and code added
- ✅ All credentials pre-configured
- ✅ Dependencies installed
- ⏳ **Deploy on Render** (your next step)
- ⏳ Set alerts with `/alert_above` and `/alert_below`
- ⏳ Receive 24/7 alerts!

---

## 🚀 Next Steps

1. **Go to Render**: https://render.com
2. **Create Web Service** using this repository
3. **Add Environment Variables** (already provided above)
4. **Click Deploy**
5. **Wait 2-3 minutes**
6. **Start using your bot!**

---

## 💡 Pro Tips

- Set multiple alerts: `/alert_above 2100` + `/alert_below 1800`
- Check price anytime: `/price`
- Bot runs 24/7 even if you close Telegram
- Alerts trigger once per threshold

---

## 📝 Price Update Frequency

- **Monitoring**: Every 1 minute
- **CoinGecko Data**: Updated from exchanges in real-time
- **Telegram Delivery**: Instant

---

## 🎉 You're All Set!

Your bot is **100% ready to deploy**. Just:
1. Go to Render
2. Add the environment variables
3. Deploy
4. Start getting alerts!

---

## 📄 License

Free to use, modify, and share! 🎉

---

**Made with ❤️ for traders**

*Questions? Check Render logs or the GitHub repository.*
