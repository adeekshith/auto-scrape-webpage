#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WebScrape/GoogleSearch  Copyright (C) 2015  Deekshith Allamaneni
# License: GNU GPLv3

from bs4 import BeautifulSoup
import urllib2
import urllib


def siblingCount(soupBowl):
    numSiblings = 0
    thisSiblings = soupBowl.next_siblings
    for eachSibling in thisSiblings:
        print "\n\n-> "+str(eachSibling)
        print "\t " + str(eachSibling.string)
        numSiblings += 1
    return numSiblings


def answer(firstContent, numSiblings):
    with open("test/test-file3.html", "r") as myfile:
        html_doc = myfile.read().replace('\n', '')
    soup = BeautifulSoup(html_doc, "html.parser")
    fadTitle = soup.find_all("a", text=firstContent)
    while True:
        if isinstance(fadTitle, list):
            if len(fadTitle) < 1:
                return -1
            fadTitle = fadTitle[0]
        if (siblingCount(fadTitle) + 1 == numSiblings):
            return fadTitle
        fadTitle = fadTitle.parent
    return fadTitle
    # return fadTitle[0].get_text(', ').encode("utf-8")


if __name__ == "__main__":
    print("Testing Element Extraction")
    print("________________________")
    firstContent = "Privacy policy"
    print(answer(firstContent, 6))
    print("________________________")
    # print(amazonProductInfo('http://goo.gl/qOvGmp'))
