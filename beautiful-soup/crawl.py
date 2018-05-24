#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('index.html',encoding='utf-8'),'lxml')
# tag = soup.div
print(soup.prettify())