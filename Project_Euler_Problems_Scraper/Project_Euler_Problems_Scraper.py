import requests
from bs4 import BeautifulSoup

#loop to numbers 1 to 900
for i in range(1, 900 + 1):
    print(f"problem {i}, parsing...")
    #request to the website
    url = 'https://projecteuler.net/problem='
    url = url + str(i)
    html = requests.get(url)

    #parse the html content 
    soup = BeautifulSoup(html.content, "html.parser")
    
    #create a new file corresponding ot the problem number
    new_filepath = "Problems/Problem" + str(i) + ".html"
    with open(new_filepath, "w") as file:
        file.write(str(soup))