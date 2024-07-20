from plyer import notification
import time
import yfinance as yf

# Define tickers and limits
tickers = ['^NSEI', 'META', 'NVDA', 'GS', 'WFC']
upper_limits = [24500, 800, 800, 800, 800]
lower_limits = [100, 130, 140, 280, 30]

def send_notification(ticker, last_price, action):
    """Send a notification based on the action."""
    if action == 'sell':
        message = f'{ticker} has reached a price of {last_price}. You might want to sell'
    elif action == 'buy':
        message = f'{ticker} has reached a price of {last_price}. You might want to buy'
    else:
        return

    print(f"Sending {action} notification for {ticker} at price {last_price}")  # Debugging line
    try:
        notification.notify(
            title=f'Price Alert For {ticker}',
            message=message,
            timeout=10  # Duration in seconds
        )
        print("Notification sent.")  # Debugging line
    except Exception as e:
        print(f"Failed to send notification: {e}")  # Error handling

while True:
    try:
        # Fetch last prices
        last_prices = [yf.Ticker(ticker).history(period='1d')['Close'].iloc[-1] for ticker in tickers]
        print("Last Prices:", last_prices)  # Debugging line

        # Check each ticker
        for i in range(len(tickers)):
            print(f"Checking {tickers[i]}: Last Price = {last_prices[i]}, Upper Limit = {upper_limits[i]}, Lower Limit = {lower_limits[i]}")  # Debugging line
            
            if last_prices[i] > upper_limits[i]:
                send_notification(tickers[i], last_prices[i], 'sell')
            elif last_prices[i] < lower_limits[i]:
                send_notification(tickers[i], last_prices[i], 'buy')
            else:
                print(f"No alert for {tickers[i]}")  # Debugging line
            
        time.sleep(60)  # Sleep to avoid hitting API rate limits
    except Exception as e:
        print(f"An error occurred: {e}")  # Print error message for debugging
        time.sleep(60)  # Sleep before retrying in case of an error
