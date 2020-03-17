import requests
from bs4 import BeautifulSoup


# FUNCTION TO GRAB PAGE SOURCE OF THE POINTED URL
def fetchUrlContent(url_extension):

    # GRABBING CONTENT FROM URL
    plainContent = requests.get(base_url + url_extension)

    # CONVERTING PLAIN CONTENT TO HTML CONTENT
    htmlContent = plainContent.content

    # PARSING HTML CONTENT
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # RETURNING WHOLE CONTENT
    return soup


# FUNCTION TO FIND INFORMATION OF ELEMENTS OF EACH GROUP
def findElementsInfo(group):

    # URL EXTENSION TO NAVIGATE IN GROUPS
    route_to_group = "/forums/index-" + str(group.lower())

    # CALLING FUNCTION TO GRAB PAGE CONTENT
    soup = fetchUrlContent(route_to_group)

    # GETTING LINKS OF GROUPS
    get_anchors_table = soup.find('table', class_='table')

    # COUNTER INCREMENT
    i = 0

    # GENERATING LIST OF ELEMENTS OF EACH GROUP
    anchorsList = []

    # LOOPING THROUGH ALL ANCHOR TAGS TO FETCH INFORMATION
    for anchor in get_anchors_table.find_all('a'):

        # COUNTER INCREMENT
        i += 1

        # GETTING NO. OF PAGES OF EACH ELEMENT OF GROUP
        route_to_element = anchor.get("href")

        # CALLING FUNCTION TO BROWSE TO THE ELEMENT PAGE
        soup = fetchUrlContent(route_to_element)

        # GETTING HTML ELEMENT THAT CONTAIN PAGES COUNT
        get_pages_count = soup.find('select', attrs={"name": "page"})

        if(get_pages_count):
            # GRABBING PAGE COUNT
            get_pages_count.find('option')
            page_count = get_pages_count.text
            page_count = page_count.rsplit('/')[-1]
            page_count = page_count.replace('\n', '')
        else:
            page_count = "0"

        # CREATING DICTIONARY OF EACH GROUP ELEMENT SEPARATELY
        data = {
                 'id': i,
                 'title': anchor.text,
                 'link': base_url + route_to_element,
                 'pages': page_count
                }

        # APPENDING DICTIONARY TO LIST OF ELEMENTS
        anchorsList.append(data)

    # PRINTING-OUT THE LIST OF ELEMENTS
    # print(anchorsList)

    # RETURNING LIST OF ELEMENTS
    return anchorsList


# BASE URL OF MAIN SITE
base_url = "https://patient.info"

# ASKING USER WHERE TO BROWSE
group = input("Enter alphabet of group you want to search: ")

# START SCRAPING
elements_of_groups = findElementsInfo(group)

# WRITING CSV
from csv import DictWriter

with open('dataset.csv', 'w') as outfile:
    writer = DictWriter(outfile, ('id', 'title', 'pages', 'link'))
    writer.writeheader()
    writer.writerows(elements_of_groups)
