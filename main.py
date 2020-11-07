from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
data = pd.read_csv('london.line.csv')

colors = data.iloc[:, 2]
print(colors)

for i in range(len(colors)):

    source = requests.get('https://www.htmlcsscolor.com/hex/' + str(colors[i])).text

    soup = BeautifulSoup(source, 'lxml')

    stuff = soup.find('small')
    print(stuff.text)
    colors[i] = str(stuff.text)
data.iloc[:, 2] = colors
print(data)
