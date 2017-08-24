#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import mechanize
import time
from bs4 import BeautifulSoup


def connection(browser):
    # Authentification
    username = raw_input("Username : ")
    password = raw_input("Password : ")

    # Fill the authentification form
    browser.form = list(browser.forms())[0]
    browser["username"] = username
    browser["password"] = password

    # Send the form you just fill
    response = browser.submit()
    cookies = browser._ua_handlers['_cookies'].cookiejar
    cookie_dict = {}
    for c in cookies:
        cookie_dict[c.name] = c.value
    print(cookie_dict)
    browser.back()

    # If len is more than 150 then you aren't connected
    if 1:
        print("")
        return connection(browser)


urlToConnect = "https://cas.univ-valenciennes.fr/cas/login?service=https://listemeletu.univ-valenciennes.fr/wws/sso_login_succeeded/CAS-UVHC"

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open(urlToConnect)

connection(browser)

print("\nYou are now connected, wait a few seconds work in progress !\n")

# Link where you can get the email list of all students
link = "https://listemeletu.univ-valenciennes.fr/wws/review/etudiants/"

file = open("studentsEmail.txt", 'w')

start = time.time()  # Start the timer

# Go through all pages (1-30) and get the student email
for page in range(1, 31):
    pageToOpen = browser.open(link + str(page) + "/500/email") # link format -> link/pageNumber/500/email
    soup = BeautifulSoup(pageToOpen.read(), "html.parser")  # Html parser
    for student in soup.find_all("td", {"class": "text_left"}):
        file.write(student.text.strip() + "\n")

file.close()

print("Time elapsed : {} seconds".format(int(time.time() - start)))
