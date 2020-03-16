import requests
from bs4 import BeautifulSoup

url = "https://patient.info"
pointer = "/forums/index-f"
# GRABBING PLAIN CONTENT FROM WEB
plainContent = requests.get(url + pointer)

# CONVERTING PLAIN CONTENT TO HTML CONTENT
htmlContent = plainContent.content

# PARSING HTML CONTENT
soup = BeautifulSoup(htmlContent, 'html.parser')

# GETTING LINKS OF CATEGORY
get_anchors_table = soup.find('table', class_='table')

i = 0
anchorsList = []
for anchor in get_anchors_table.find_all('a'):
    i += 1
    data = {
             'id': i,
             'title': anchor.text,
             'link': url+anchor.get("href")
            }
    anchorsList.append(data)

print(anchorsList)
