#!/usr/bin/env Python
# -*- coding: utf-8 -*-


import mechanize
from bs4 import BeautifulSoup

urlToConnect = "https://cas.univ-valenciennes.fr/cas/login?service=https://listemeletu.univ-valenciennes.fr/wws/sso_login_succeeded/CAS-UVHC"

browser = mechanize.Browser()
response = browser.open(urlToConnect)

# Fill the authentification form
browser.form = list(browser.forms())[0]
browser["username"] = "..."
browser["password"] = "..."

# Send the form you just fill
response = browser.submit()
browser.back()

# Link where you can get the email list of all students
link = "https://listemeletu.univ-valenciennes.fr/wws/review/etudiants/"

# Output file
file = open("studentsEmail.txt", 'w')

# Go through all page (1-30) and get the student email
for page in range(1, 31):
    pageToOpen = browser.open(link + str(page) + "/500/email") # format -> link/pageNumber/500/email
    soup = BeautifulSoup(pageToOpen.read(), "html.parser")  # Html parser
    for student in soup.find_all("td", {"class": "text_left"}):
        file.write(student.text.strip() + "\n")

file.close()
