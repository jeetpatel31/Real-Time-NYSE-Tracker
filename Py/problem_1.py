import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['stock_data']
stock_collection = db['nyse_stocks']

def fetch_stock_data():
    url = 'https://finance.yahoo.com/most-active'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            stocks_table = soup.find('table', {'class': 'W(100%)'})
            
            for row in stocks_table.find_all('tr')[1:]: 
                columns = row.find_all('td')
                stock_symbol = columns[0].text.strip()
                stock_name = columns[1].text.strip()
                stock_price = columns[2].text.strip()
                stock_change = columns[3].text.strip()
                stock_volume = columns[6].text.strip()

                
                stock_data = {
                    'Symbol': stock_symbol,
                    'Name': stock_name,
                    'Price': stock_price,
                    'Change': stock_change,
                    'Volume': stock_volume
                }
                stock_collection.insert_one(stock_data)
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Request error:", e)

while True:
    fetch_stock_data()
    time.sleep(180)  
