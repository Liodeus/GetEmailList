#!/usr/bin/env Python
# -*- coding: utf-8 -*-


import mechanize
from bs4 import BeautifulSoup

url = "https://cas.univ-valenciennes.fr/cas/login?service=https://listemeletu.univ-valenciennes.fr/wws/sso_login_succeeded/CAS-UVHC"

br = mechanize.Browser()
response = br.open(url)

br.form = list(br.forms())[0]
br["username"] = "..."
br["password"] = "..."

response = br.submit()
br.back()

link = "https://listemeletu.univ-valenciennes.fr/wws/review/etudiants/"

for page in range(1, 31):
    pageToOpen = br.open(link + str(page) + "/500/email")
    soup = BeautifulSoup(pageToOpen.read(), "html.parser")
    for x in soup.find_all("td", {"class": "text_left"}):
        print(x.text.strip())