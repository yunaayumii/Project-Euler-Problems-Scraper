import requests
from bs4 import BeautifulSoup

#request to the website
url = 'https://projecteuler.net/problem='
problem_number = input("What problem number do you want to get: ")
url = url + problem_number
html = requests.get(url)

#parse the html content 
soup = BeautifulSoup(html.content, "html.parser")
print(soup)