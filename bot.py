import os
import requests
import time
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError
import asyncio
from apscheduler.schedulers.background import BackgroundScheduler

# Get environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
PRICE_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Store alert thresholds
alert_thresholds = {}
last_prices = {}

# Initialize bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def get_gold_price():
    """Fetch gold price from CoinGecko (free API)"""
    try:
        params = {
            'ids': 'gold',
            'vs_currencies': 'usd'
        }
        response = requests.get(PRICE_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get('gold', {}).get('usd')
        return price
    except Exception as e:
        print(f"Error fetching gold price: {e}")
        return None

def send_telegram_message(message):
    """Send message to Telegram chat"""
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Message sent: {message}")
    except TelegramError as e:
        print(f"Telegram error: {e}")
    except Exception as e:
        print(f"Error sending message: {e}")

def check_price_alerts():
    """Check current price against set thresholds and send alerts"""
    price = get_gold_price()
    
    if price is None:
        print("Could not fetch price")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Current Gold Price: ${price:.2f}")
    
    last_prices['gold'] = price
    
    # Check all alert thresholds
    for key, threshold in alert_thresholds.items():
        if threshold is None:
            continue
            
        alert_type = key.split('_')[0]  # 'above' or 'below'
        
        if alert_type == 'above' and price >= threshold:
            message = f"🚨 PRICE ALERT 🚨\n\nGold price has reached ${price:.2f}\n(Above your set level of ${threshold:.2f})\n\nTime: {timestamp}"
            send_telegram_message(message)
            alert_thresholds[key] = None  # Reset alert
            
        elif alert_type == 'below' and price <= threshold:
            message = f"🔔 PRICE ALERT 🔔\n\nGold price has dropped to ${price:.2f}\n(Below your set level of ${threshold:.2f})\n\nTime: {timestamp}"
            send_telegram_message(message)
            alert_thresholds[key] = None  # Reset alert

def handle_set_alert_above(price):
    """Set alert for price above a level"""
    try:
        threshold = float(price)
        alert_thresholds['above_threshold'] = threshold
        message = f"✅ Alert set! You will be notified when Gold price goes ABOVE ${threshold:.2f}"
        send_telegram_message(message)
        print(f"Alert set (above): ${threshold}")
    except ValueError:
        send_telegram_message("❌ Invalid price. Please enter a valid number.")

def handle_set_alert_below(price):
    """Set alert for price below a level"""
    try:
        threshold = float(price)
        alert_thresholds['below_threshold'] = threshold
        message = f"✅ Alert set! You will be notified when Gold price drops BELOW ${threshold:.2f}"
        send_telegram_message(message)
        print(f"Alert set (below): ${threshold}")
    except ValueError:
        send_telegram_message("❌ Invalid price. Please enter a valid number.")

def start_scheduler():
    """Start background scheduler to check prices every minute"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_price_alerts, 'interval', minutes=1)
    scheduler.start()
    print("Price checker started - checking every minute")
    return scheduler

if __name__ == "__main__":
    print("Starting Gold Price Alert Bot...")
    
    # Verify bot connection
    try:
        bot.get_me()
        print(f"✅ Bot connected: {TELEGRAM_BOT_TOKEN[:20]}...")
    except Exception as e:
        print(f"❌ Bot connection error: {e}")
        exit(1)
    
    # Start scheduler
    scheduler = start_scheduler()
    
    # Keep the bot running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBot stopped")
        scheduler.shutdown()
