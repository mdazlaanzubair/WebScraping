INSTRUCTIONS TO RUN THE SCRAPER
===============================

Since this scraper is made to crawl on a site that is "PATIENT INFO" [https://patient.info/] which contain
information regarding health. So there were many cool things to scrap or mess around with.

This web scraper is consist of three files each files has it's own importance in fetching data from a site.
Purpose of each file is given below:

1_  "Scrap.py" is to fetch the dataset of Diseases by just providing Group Name in the Input Prompt (which
    can be any Alphabet from A to Z). By doing this, program will create a new directory in the root folder
    with the "Group Name" (which is alphabet obviously), and save dataset of diseases to in that directory.
    (the process is same for every alphabetical group of diseases)

2_  "ScrapDiscussionLinks.py" is to fetch the link of every discussion which was done on the Disease provided
    by user in the Input Prompt. By doing this, program will create a new file in the respective group folder
    which stores dataset of all the links and titles of the discussion and the pages count.
    (the process is same for every alphabetical group of diseases)

3_  "ScrapAllDiscussions.py" is to fetch all the discussion which is being done on the site regarding the
    disease provided by the user in the Input Prompt. By doing this, program will create a new file in the
    respective group folder which stores dataset of all the discussions.
    (the process is same for every alphabetical group of diseases)
 