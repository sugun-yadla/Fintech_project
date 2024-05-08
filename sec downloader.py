import os
from sec_edgar_downloader import Downloader

# List of company tickers
companies = ['AAPL', 'MSFT']  # replace with your companies

# Directory to save filings
dir_to_save = 'sec_filings'

# Ensure the directory exists
os.makedirs(dir_to_save, exist_ok=True)


# Loop over each company
for company in companies:
    dl = Downloader("University of Massachusetts Amherst", 'syadla@umass.edu', dir_to_save)
    for year in range(1995, 2024):
    # Loop over each year from 1995 through 2023
        # Download the 10-K filings
        dl.get("10-K", company, limit=29, after=f"{year}-01-01", before=f"{year}-12-31")