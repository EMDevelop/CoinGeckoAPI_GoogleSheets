# CoinGeckoAPI_GoogleSheets

This is a simple API call to CoinGecko, using Python, to fetch the latest information about every Crypto project on the CoinGecko "Market View" listing. 

I've also included a free starter Portfolio checker - I use this to keep track of how my crypto assets are performing, and this Python script feeds directly into this format. 

The script will fetch 300 coins at a time (seems to be the maximum that coingecko allows) and then loop through each page (does 30 pages but you can change this to something more sophisticated)

What you need to use this: 
- A code editor (I use VS Code)
- The latest version of Python installed
- A Google sheet, ideally in the format I've shown in my template below, here's the documentation https://developers.google.com/sheets/api/
- Set up an API to your google sheet 


Google Sheet Template
https://docs.google.com/spreadsheets/d/1jnWPmBrEhn5VHj0_BIfi-s_ctAEP_j3snebRS6TQiIk/edit?usp=sharing
Feel free to make a copy. 
On the "Portfolio" tab, Column C and E pre-fill based on column B. There are a few other tabs in there, 1 is a futures trading file - be responsible with it ;) 

Thanks all! 
