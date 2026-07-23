#!/usr/bin/env python3
import os
import requests
import time
from datetime import datetime
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.error import TelegramError
import logging
from apscheduler.schedulers.background import BackgroundScheduler

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration - Already set with your credentials
TELEGRAM_BOT_TOKEN = "8820866226:AAGsQHYSsK4x_-iGeHMabKpwwv64L_Dc14M"
CHAT_ID = 8820866226
COINGECKO_API_KEY = "CG-KmG6rg5ca6UCDKZf4BfuYdqz"
PRICE_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Store alert thresholds
alert_thresholds = {
    'above': None,
    'below': None
}
last_price = None
scheduler = None

def get_gold_price():
    """Fetch gold price from CoinGecko API"""
    try:
        params = {
            'ids': 'gold',
            'vs_currencies': 'usd',
            'x_cg_pro_api_key': COINGECKO_API_KEY
        }
        response = requests.get(PRICE_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get('gold', {}).get('usd')
        return price
    except Exception as e:
        logger.error(f"Error fetching gold price: {e}")
        return None

def send_message(context, text):
    """Send message to Telegram chat"""
    try:
        context.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='HTML')
        logger.info(f"Message sent: {text[:50]}...")
    except Exception as e:
        logger.error(f"Error sending message: {e}")

def check_price_alerts(context):
    """Check current price against thresholds"""
    global last_price
    
    price = get_gold_price()
    if price is None:
        logger.warning("Could not fetch price")
        return
    
    last_price = price
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] 💰 Gold Price: ${price:.2f}")
    
    # Check above threshold
    if alert_thresholds['above'] is not None and price >= alert_thresholds['above']:
        message = f"""🚨 <b>PRICE ALERT - ABOVE THRESHOLD!</b> 🚨

💰 <b>Gold Price:</b> ${price:.2f}
📈 <b>Your Alert Level:</b> ${alert_thresholds['above']:.2f}
⏰ <b>Time:</b> {timestamp}

✅ Alert triggered successfully!"""
        send_message(context, message)
        alert_thresholds['above'] = None
    
    # Check below threshold
    if alert_thresholds['below'] is not None and price <= alert_thresholds['below']:
        message = f"""🔔 <b>PRICE ALERT - BELOW THRESHOLD!</b> 🔔

💰 <b>Gold Price:</b> ${price:.2f}
📉 <b>Your Alert Level:</b> ${alert_thresholds['below']:.2f}
⏰ <b>Time:</b> {timestamp}

✅ Alert triggered successfully!"""
        send_message(context, message)
        alert_thresholds['below'] = None

def start(update: Update, context: CallbackContext):
    """Start command"""
    message = """🤖 <b>Welcome to POI Alert Bot!</b> 🤖

📊 Real-time Gold Price Alerts

<b>Commands:</b>
/price - Get current gold price
/alert_above [price] - Alert when gold goes above price
/alert_below [price] - Alert when gold goes below price
/status - Check current alerts
/help - Show all commands

💡 Example:
/alert_above 2000
/alert_below 1500

✅ Bot is running 24/7!"""
    send_message(context, message)

def price_command(update: Update, context: CallbackContext):
    """Get current price"""
    price = get_gold_price()
    if price:
        message = f"""💰 <b>Current Gold Price</b> 💰

<b>Price:</b> ${price:.2f} USD
⏰ <b>Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
    else:
        message = "❌ Could not fetch price. Try again later."
    send_message(context, message)

def alert_above(update: Update, context: CallbackContext):
    """Set alert above price"""
    if not context.args:
        send_message(context, "❌ Usage: /alert_above 2000")
        return
    
    try:
        price = float(context.args[0])
        alert_thresholds['above'] = price
        message = f"""✅ <b>Alert Set - ABOVE Threshold</b> ✅

🎯 <b>You will be notified when:</b>
 Gold price ≥ ${price:.2f}

📊 <b>Current Price:</b> ${last_price:.2f if last_price else 'Loading...'}"""
        send_message(context, message)
        logger.info(f"Alert set (above): ${price}")
    except ValueError:
        send_message(context, "❌ Invalid price! Use: /alert_above 2000")

def alert_below(update: Update, context: CallbackContext):
    """Set alert below price"""
    if not context.args:
        send_message(context, "❌ Usage: /alert_below 1500")
        return
    
    try:
        price = float(context.args[0])
        alert_thresholds['below'] = price
        message = f"""✅ <b>Alert Set - BELOW Threshold</b> ✅

🎯 <b>You will be notified when:</b>
 Gold price ≤ ${price:.2f}

📊 <b>Current Price:</b> ${last_price:.2f if last_price else 'Loading...'}"""
        send_message(context, message)
        logger.info(f"Alert set (below): ${price}")
    except ValueError:
        send_message(context, "❌ Invalid price! Use: /alert_below 1500")

def status(update: Update, context: CallbackContext):
    """Check alert status"""
    current_price = get_gold_price() or last_price
    above = alert_thresholds['above']
    below = alert_thresholds['below']
    
    message = f"""📊 <b>Alert Status</b> 📊

💰 <b>Current Price:</b> ${current_price:.2f if current_price else 'Loading...'}

🔺 <b>Above Alert:</b> {f'${above:.2f}' if above else '❌ Not Set'}
🔻 <b>Below Alert:</b> {f'${below:.2f}' if below else '❌ Not Set'}

⏰ <b>Last Updated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
    send_message(context, message)

def help_command(update: Update, context: CallbackContext):
    """Show help"""
    message = """📖 <b>POI Alert Bot - Help</b> 📖

<b>🎯 Available Commands:</b>

/start - Start the bot
/price - Show current gold price
/alert_above [price] - Get alert when price goes above
/alert_below [price] - Get alert when price goes below
/status - Check your current alerts
/help - Show this message

<b>💡 Examples:</b>
/alert_above 2050
/alert_below 1950

<b>✨ Features:</b>
✅ 24/7 Price Monitoring
✅ Real-time Alerts
✅ CoinGecko Data (Accurate)
✅ No API Key Limits

<b>📞 Need Help?</b>
Check Render logs at dashboard"""
    send_message(context, message)

def main():
    """Main function"""
    print("\n" + "="*60)
    print("🤖 POI ALERT BOT - Starting...")
    print("="*60)
    print(f"✅ Telegram Token: {TELEGRAM_BOT_TOKEN[:20]}...")
    print(f"✅ Chat ID: {CHAT_ID}")
    print(f"✅ CoinGecko API: {COINGECKO_API_KEY[:20]}...")
    print("="*60 + "\n")
    
    # Create updater
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("price", price_command))
    dispatcher.add_handler(CommandHandler("alert_above", alert_above))
    dispatcher.add_handler(CommandHandler("alert_below", alert_below))
    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    # Start scheduler for price checks
    global scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_price_alerts, 'interval', minutes=1, args=[updater.dispatcher])
    scheduler.start()
    print("⏱️  Price checker started - checking every 1 minute\n")
    
    # Send startup message
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, 
                        text="🤖 <b>POI Alert Bot Started!</b>\n✅ Ready to monitor gold prices\n\nSend /help for commands",
                        parse_mode='HTML')
        logger.info("✅ Startup message sent")
    except Exception as e:
        logger.error(f"Could not send startup message: {e}")
    
    # Start polling
    print("✅ Bot is polling for messages...\n")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
