"""
Importing data from the Internet
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve, urlopen, Request

"""
Importing flat files from the web
"""

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# Opening and reading flat files from the web
df = pd.read_csv(url, sep=';')
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

# Importing non-flat files from the web
xl = pd.read_excel(url, sheetname=None)

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())

"""
HTTP requests to import files from the web
"""

# Performing HTTP requests in Python using urllib
url = "http://www.datacamp.com/teach/documentation"

request = Request(url)
response = urlopen(request)

print(type(response))

# Printing HTTP request results in Python using urllib
html = response.read()

# Print the html
print(html)

response.close()

# Performing HTTP requests in Python using requests
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

"""
Scraping the web in Python
"""

# Parsing HTML with BeautifulSoup
url = 'https://www.python.org/~guido/'

r = requests.get(url)
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
print(pretty_soup)

# Turning a webpage into data using BeautifulSoup: getting the text
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()
print(guido_text)

# Turning a webpage into data using BeautifulSoup: getting the hyperlinks
# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
