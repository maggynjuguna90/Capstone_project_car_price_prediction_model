
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

url = "https://www.sbtjapan.com/"
r = requests.get(url)


soup = BeautifulSoup(r.text, "lxml")
tag =soup.header
atb=(tag.attrs)
print(tag["class"])

import pandas as pd

# Load Excel file
df = pd.read_excel("kenya_prices.xlsx")

# Save as CSV
df.to_csv("kenya_prices.csv", index=False)

print("Conversion done!")