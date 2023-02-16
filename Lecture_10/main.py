from typing import List
import requests
from bs4 import BeautifulSoup
import re
from models import Person
from db import DB




api_url = "http://127.0.0.1:8000"
# Site we want to scrape
url = "https://ecutbildning.se/utbildningar/data-scientist/"
# url2 = "https://svt.se"
# requet the url into variable
res = requests.get(url)
# save in text form?
page = res.text
# use method prettify to make the text more in accordance with html-convention
# soup.prettify()

soup = BeautifulSoup(page, "html.parser")

# Find tidle, this is what is shown in the tab
title = soup.find("title").text
# Header, shown on top of page
header = soup.find("h1").text
# .text shows only the text, and not the other parts of the code
# print(title)
# print(header)
h2 = soup.find_all("h2")
# h2 contains several things, we use find_all to get all.
# .text does not work on find_all, instead we loop over the results, using .text on each item.
# for i in h2:
#     print(i.text)

# Check that it works with other sites
# res2 = requests.get(url2)
# page2 = res2.text
# soup2 = BeautifulSoup(page2, "html.parser")
# title2 = soup2.find("title").text
# print(title2)

# See all h1 levels in soup. Should only be 1 h1.
# all = soup2.find_all("h1")
# # print(all)
# for i in all:
#     print(i.text)

p_tags = soup.find_all("p") # Finds all "p-tags"

# re. is regular expression. What is that?
# test = soup.find_all(string=re.compile("dator"))
# print(len(test))
# for i in test:
#     print(i.text)
#     print("________________")



# .parent goes up to the above level tag
# .child goes down a step
# If you are at parent and typ .child, you reach child
# If you are at child and type .parent, you reach parent.
# Typing .child.parent will not get you back to the origiinal place?
# This could be because there can be several children?
# <parent>
#   <child>
#   </child>
# </parent>
# a-tags are links. Annnchor tag
a_tag = soup.find_all("a")

people_soup = []
for i in a_tag:
    if i.has_attr("href"): # If the a-tag has "href", ie is a link. 
        if "mailto" in i["href"]: # or "tel" in i["href"]: # will result in everything being done twice since what we want fulfills both criteria
            if "card-body" in i.parent.parent.parent["class"]:
            # We want to reach "card" whatever that is
                i = i.parent.parent.parent
                people_soup.append(i)

# Create a variable that is a List of objects Person, defined at the start. Dataclass 
people:  List[Person] = []
# Since people_soup is now a list of tags??? we can use prettify() which is a BS-method
for i in people_soup:
    name = i.find("h3").text
    title = i.find("p", itemprop="jobTitle").text
    # two a-tags in every person
    person_links = i.find_all("a")
    # tel = ""
    # mail = ""
    for i in person_links:
        if i["href"].startswith("tel"):
            tel = i.text.strip()
        elif i["href"].startswith("mailto"):
            mail = i.text.strip()
    people.append(Person(name=name, title=title, mail=mail, tel=tel))

for i in people:
    requests.post(api_url + "/create_person", json=i.dict())

    # print(name)
    # print(title)
    # print(tel)
    # print(mail)

requests.delete(api_url + f"/delete_duplicates")