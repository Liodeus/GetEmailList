#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import mechanize
import time
import connection
from bs4 import BeautifulSoup

urlToConnect = "https://cas.univ-valenciennes.fr/cas/login?service=https://listemeletu.univ-valenciennes.fr/wws/sso_login_succeeded/CAS-UVHC"

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open(urlToConnect)

connection.connect(browser) # Connection 

print("\nYou are now connected, wait a few seconds work in progress !\n")

# Link where you can get the email list of all students
link = "https://listemeletu.univ-valenciennes.fr/wws/review/etudiants/"

file = open("studentsEmail.txt", 'w')

start = time.time()  # Start the timer

# Go through all pages (1-35) and get the student email
emailCount = 0
for page in range(1, 35):
    pageToOpen = browser.open(link + str(page) + "/500/email") # link format -> link/pageNumber/500/email
    soup = BeautifulSoup(pageToOpen.read(), "html.parser")  # Html parser
    for student in soup.find_all("td", {"class": "text_left"}):
        file.write(student.text.strip() + "\n")
        emailCount += 1

file.close()

print("Time elapsed : {} seconds".format(int(time.time() - start)))
print("Email count : {}".format(emailCount))
print("You can now find all the emails in studentsEmail.txt")
