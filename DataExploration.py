# https://www.thestreet.com/jim-cramer/mad-money

# How do I access this site?

#from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
#import pandas as pd

url = "https://www.thestreet.com/jim-cramer/mad-money"

# from bs4 import BeautifulSoup as bs
# import pandas as pd
# pd.set_option('display.max_colwidth', 500)
# import time
# import requests
# import random

# page = requests.get("https://www.thestreet.com/jim-cramer/mad-money")


import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

session.get(url)

WebClient client = new WebClient()
client.OpenRead(myUri)