from sec_edgar_downloader import Downloader
import os

# Create a downloader instance
dl = Downloader()

# List of company tickers
companies = ['AAPL', 'MSFT', 'GOOG']  # replace with your companies

# Directory to save filings
dir_to_save = 'sec_filings'

# Ensure the directory exists
os.makedirs(dir_to_save, exist_ok=True)

# Loop over each company
for company in companies:
    # Loop over each year from 1995 through 2023
    for year in range(1995, 2024):
        # Download the 10-K filings
        dl.get("10-K", company, dir_to_save, after_date=f"{year}-01-01", before_date=f"{year}-12-31")
