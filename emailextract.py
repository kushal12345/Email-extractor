#!/usr/bin/python

from googlesearch import search
from socket import timeout
import http
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import URLError, HTTPError
import random
import os
import time
import sys
import re
from fake_useragent import UserAgent
from socket import timeout
from urllib.error import HTTPError, URLError

imageExt = ["jpeg", "exif", "tiff", "gif", "bmp", "png", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif", "bat", "bpg", "cgm", "svg"]
ua = UserAgent()
file = open('list.txt', 'w')

#try:
#    from googlesearch import search
#except ImportError:
#    print("No module named 'google' found")

# to search
print("Enter category of email you want to search")
print("_________________________________________________")
query = input()
print("_________________________________________________")
print("Results:")
print("___________")

list = []
file = open('list.txt', 'w')

def Googlesearch():
    for j in search(query, tld="com", num=100, stop=100, pause=2):
        print(j)
        Search_school_website(j)
        list.append(j)

def Search_school_website(url):
    try:
        print("Searching emails.... please wait")
        count = 0
        listUrl = []
        found = False

        req = urllib.request.Request(url,data=None,headers={'User-Agent':ua.random})

        try:
            conn = urllib.request.urlopen(req, timeout=100000000)
        except timeout:
            raise ValueError('Timeout ERROR')
        except (HTTPError, URLError):
            raise ValueError('Bad URL...')

        status = conn.getcode()
        contentType = conn.info().get_content_type()

        if(status!=200 or contentType == "audio/mpeg"):
            raise ValueError('Bad url....')

        html = conn.read().decode('utf-8')
        emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}',html)

        for email in emails:
            if (email not in listUrl and email[-3:] not in imageExt):
                count += 1
                print(str(count) + "-" + email)
                listUrl.append(email)
                with open('list.txt', "r") as Readfile:
                    for line in Readfile:
                        if email == line:
                            found=True
                            break
                if not found:
                    with open('list.txt',"a") as file:
                        file.write(email)
                        file.write('\n')

        print("")
        print("**********************************")
        print(str(count) + "emails were found")
        print("***********************************")

    except KeyboardInterrupt:
        input("press return key to continue")

    except Exception as e:
        print(e)
        input("press enter to continue")


Googlesearch()
file.close()
