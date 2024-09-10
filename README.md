## Stock Tracker
This project provides real-time updates on the most active stocks on the New York Stock Exchange (NYSE). Using web scraping, MongoDB, and an interactive web interface, users can view stock data including symbol, name, price, price change, and trading volume in a dynamic table.

## Features
Scrapes live data from Yahoo Finance’s "Most Active Stocks" page.
Stores stock data in a MongoDB database.
Updates stock information every 3 minutes.
Interactive, searchable, and sortable table for easy data access.
Technologies Used
Python: For scraping stock data using BeautifulSoup.
MongoDB: For data storage.
PHP: To retrieve and display data from MongoDB.
HTML & JavaScript: For the user interface, enhanced with DataTables and jQuery.
How It Works
Stock Scraping:

A Python script fetches stock data from Yahoo Finance, parses the data, and stores it in MongoDB.
The script runs continuously, updating the database every 3 minutes.
Data Display:

The front-end retrieves stored stock data from MongoDB using PHP.
The data is displayed in a table with an interactive interface powered by DataTables, allowing users to search and sort through the stock information.
Installation Guide
Prerequisites
Python 3.x
MongoDB (local instance)
PHP 7.x or above
Composer (for PHP dependency management)
Required Python libraries: requests, beautifulsoup4, pymongo
JavaScript libraries: jQuery and DataTables
Setup Instructions
Install Python dependencies:

Run the following command to install the necessary Python packages:
bash
Copy code
pip install requests beautifulsoup4 pymongo
Install PHP dependencies:

Use Composer to install MongoDB PHP libraries by running:
bash
Copy code
composer install
Configure MongoDB:

Ensure MongoDB is running locally on mongodb://localhost:27017/.
Create a database named stock_data and a collection named nyse_stocks to store stock data.
Run the stock scraper:

Execute the Python script to start fetching stock data:
bash
Copy code
python stock_scraper.py
Launch the web interface:

Deploy the PHP files to your web server (e.g., Apache or Nginx).
Access the web interface (e.g., localhost/stocktracker) to view the stock data in real-time.
Usage
Once the Python script is running, it will fetch updated stock data every 3 minutes and store it in the MongoDB database. You can access the web interface to view and interact with the data.