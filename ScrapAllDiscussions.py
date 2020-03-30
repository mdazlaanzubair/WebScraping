import requests
from bs4 import BeautifulSoup
import json
import os

def datasetFinder(disease):

    # GETTING GROUP FROM THE DISEASE NAME
    group = disease[:1].lower()

    # CREATING PATH TO FILE WHICH CONTAIN USER DEMANDED DISEASE DATA
    disease_dir = 'group_' + group + '/' + disease + '_dataset.json'

    # IF THE DIRECTORY OF DEMANDED DISEASE DOESN'T EXIST
    if not os.path.exists(disease_dir):

        # ERROR MESSAGE TO SHOW IF DIRECTORY DOESN'T EXIST
        print("")
        print("Nothing found in our record.\n")
        print('To country this error run this file first. "Scrap.py"')
        print("")

    # IF DEMANDED DISEASE DIRECTORY EXISTS LOAD THE DATASET
    else:

        # LOADING ALL DISEASE DATASET TO FIND DEMANDED DISEASE
        with open(disease_dir, 'r') as f:
            diseases_dataset = json.load(f)

    # RETURNING THE DATASET WHICH CONTAIN THE DISEASE
    return diseases_dataset


def scrapAllDiscussions(dataset, disease):

    # DISCUSSION HOLDER OF DEMANDED DISEASE
    discussions_holder = []

    # LOOPING THROUGH DISCUSSIONS DATASET TO GET ALL THE DISCUSSION OF DEMANDED DISEASE
    for discussion in dataset:

        # GETTING URL TO THE MAIN DISCUSSION PAGE
        url = discussion["discussion_link"]

        # GRABBING PAGE CONTENT OF DISEASE DISCUSSIONS FROM URL OF DEMANDED DISEASE
        plainContent = requests.get(url)

        # CONVERTING PLAIN CONTENT TO HTML CONTENT
        htmlContent = plainContent.content

        # PARSING HTML CONTENT INTO SOUP
        soup = BeautifulSoup(htmlContent, 'html.parser')

        # GETTING ELEMENT THAT CONTAIN ALL THE DISCUSSION REGARDING THE DEMANDED DISEASE
        get_discussion_div = soup.find('div', attrs={"id": "post_content", "class": "post__content"})
        get_discussion_paras = get_discussion_div.findAll('p', attrs={'class': None})
        p_content = ""

        for get_p_content in get_discussion_paras:
            if p_content == "":
                p_content = get_p_content.text
            else:
                p_content = p_content + get_p_content.text

        data = {
            "discussion_title": discussion["discussion_title"],
            "discussion_link": discussion["discussion_link"],
            "discussion": p_content
        }

        # APPENDING DICTIONARY TO LIST OF DISCUSSIONS HOLDER
        discussions_holder.append(data)

    # MAKE DIRECTORY OF EACH GROUP IF DOES'NT EXIST
    disease_group = 'group_' + disease[:1].lower()

    # CREATING PATH WHERE TO SAVE DATASET
    file_path = disease_group + '/' + disease + '_discussions_dataset.json'

    # WRITING JSON FILE OF EACH GROUP TO THE RESPECTIVE DIRECTORY
    with open(file_path, 'w') as f:
        json_formatted_str = json.dumps(discussions_holder, indent=4)
        f.write(json_formatted_str)

    print("")
    print("Task Completed Successfully!")
    print("For results please navigate to this directory. [/" + file_path + "]")


# ASKING USER ABOUT THE DISEASE TO SEARCH
disease = input("Enter disease you want to explore : ")

# FINDING DATASET THAT CONTAIN THE DEMANDED DISEASE
discussions_dataset = datasetFinder(disease.title())

scrapAllDiscussions(discussions_dataset, disease.title())
