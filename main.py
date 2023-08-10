import requests
import datetime
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# --- VARIABLES ---
today = datetime.datetime.today().date()
yesterday1x = datetime.datetime.today().date() - datetime.timedelta(days=1)
yesterday2x = datetime.datetime.today().date() - datetime.timedelta(days=2)

# --- STOCK PRICE API - Alpha Vantage API ---
stock_price_api_url = "https://www.alphavantage.co/query"
stock_price_api_key = "key"
parameters_for_stock_price_api = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": f"{STOCK}",
    "interval": "60min",
    "apikey": stock_price_api_key,
}

stock_price_data_request = requests.get(stock_price_api_url, params=parameters_for_stock_price_api)
stock_price_data_request.raise_for_status()
stock_price_data_5days = stock_price_data_request.json()

# ---NEWS API - NEWSAPI ---
news_api_url = "https://newsapi.org/v2/everything"
news_api_key = "key"
parameters_for_news_api = {
    "q": "Tesla",
    "from": f"{yesterday2x}",
    "searchIn": "description",
    "sortBy": "relevancy, popularity, publishedAt",
    "language": "en",
    "apiKey": news_api_key,
}

news_data_request = requests.get(news_api_url, params=parameters_for_news_api)
news_data_request.raise_for_status()
news_data = news_data_request.json()
news_to_transmit = news_data["articles"][:3]
# print(news_to_transmit)

# --- EMAIL HANDLING ---
email_to_send_from = "dummy@Gmail.com"
password_for_email = "password"

# --- DATA HANDLING ---
# print(stock_price_data_5days)
stock_price_data_opening = {"yesterday1x": stock_price_data_5days["Time Series (60min)"][f"{yesterday1x} 05:00:00"],
                            "yesterday2x": stock_price_data_5days["Time Series (60min)"][f"{yesterday2x} 05:00:00"]}
# print(stock_price_data_opening)
stock_price_data_closing = {"yesterday1x": stock_price_data_5days["Time Series (60min)"][f"{yesterday1x} 19:00:00"],
                            "yesterday2x": stock_price_data_5days["Time Series (60min)"][f"{yesterday2x} 19:00:00"]}
difference_in_opening_values = float(stock_price_data_opening["yesterday1x"]["1. open"]) - \
                               float(stock_price_data_opening["yesterday2x"]["1. open"])
difference_in_closing_values = float(stock_price_data_closing["yesterday1x"]["4. close"]) - \
                               float(stock_price_data_closing["yesterday2x"]["4. close"])
difference_in_opening_values_percentage = (float(stock_price_data_opening["yesterday1x"]["1. open"]) /
                                           float(stock_price_data_opening["yesterday2x"]["1. open"]) - 1) * 100
difference_in_closing_values_percentage = (float(stock_price_data_closing["yesterday1x"]["4. close"]) /
                                           float(stock_price_data_closing["yesterday2x"]["4. close"]) - 1) * 100

if abs(difference_in_closing_values_percentage) > 0.1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email_to_send_from, password_for_email)
        for news in range(0, 3):
            message = f"Subject:Tesla stocks are {'down🔻' if difference_in_closing_values_percentage < 0 else 'up🔺'}"\
                      f"{difference_in_closing_values_percentage}% -> {news_to_transmit[news]['title']}\n\n" \
                      f"Brief: {news_to_transmit[news]['description']}\n" \
                      f"Here is the article link: {news_to_transmit[news]['url']}"
            message_encoded = message.encode('utf-8')
            connection.sendmail(from_addr=email_to_send_from,
                                to_addrs=email_to_send_from,
                                msg=message_encoded)
