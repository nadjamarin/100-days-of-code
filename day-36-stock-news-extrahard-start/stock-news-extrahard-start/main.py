import requests
import datetime as dt
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MIN_STOCK_PERCENT_DIFF = 5

alpha_vantage_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_vantage_api_key}")
stock_response.raise_for_status()
stock_data = stock_response.json()

# Get today's date, then yesterday and day before yesterday
now = dt.datetime.now()
today_day = dt.date.today()
yest_day = today_day - dt.timedelta(days=1)
yest_day = str(yest_day)
before_yest_day = today_day - dt.timedelta(days=2)
before_yest_day = str(before_yest_day)

# Get stock data for yesterday and day before yesterday
yest_stock_data = stock_data["Time Series (Daily)"][yest_day]
before_yest_stock_data = stock_data["Time Series (Daily)"][before_yest_day]

# Get closing price for yesterday and day before yesterday
yest_close = float(yest_stock_data["4. close"])
before_yest_close = float(before_yest_stock_data["4. close"])

# yest_open = 1
# before_yest_open = 2
percent_diff = 100 * ((yest_close - before_yest_close) / before_yest_close)

# if abs(percent_diff) >= 5:
#     print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# percent_diff = 5
if abs(percent_diff) >= MIN_STOCK_PERCENT_DIFF:
    news_params = {
        "apiKey": news_api_key,
        "qinTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=f"https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    # print(news_data)

    top_three = news_data["articles"][0:3]
    # print(top_three)
    titles = [article["title"] for article in top_three]
    # print(titles)
    descriptions = [article["description"] for article in top_three]
    # print(descriptions)

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    if percent_diff > 0:
        arrow = "🔺"
    elif percent_diff < 0:
        arrow = "🔻"

    print(f"{STOCK}: {arrow}{abs(percent_diff)}%\n")

    for index in range(0, len(titles)):
        print(f"Headline: {titles[index]}")
        print(f"Brief: {descriptions[index]}\n")

else:
    print("Tesla stock changed by less than 5%")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

