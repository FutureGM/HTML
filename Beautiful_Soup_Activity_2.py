from os import getcwd
from os.path import join
from bs4 import BeautifulSoup as bs
import requests


#URL to be scraped
url= "https://www.nfl.com/"

#Retrieve page with requests

response = requests.get(url)

#Create BeautifulSoup object(response.text, "html.parser")
soup = bs(response.text, "html.parser")

#Examine the results, then determine element that contains sought infro
print(soup.prettify())

#results are returned as an iterable list
results = soup.find_all("link")
print(results)

# #Loop through returned results
# for result in results:
#     #Errof handling
#     try:
#         #Identify and return 