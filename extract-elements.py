#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WebScrape/GoogleSearch  Copyright (C) 2015  Deekshith Allamaneni
# License: GNU GPLv3

from bs4 import BeautifulSoup
import urllib2
import urllib


def printSiblings(soupBowl):
    numSiblings = 0
    thisSiblings = soupBowl.next_siblings
    for eachSibling in thisSiblings:
        numSiblings += 1
        print "\n\n-> "+str(eachSibling)
        print "\t " + eachSibling.get_text()
    return numSiblings


def siblingCount(soupBowl):
    numSiblings = 0
    thisSiblings = soupBowl.next_siblings
    for eachSibling in thisSiblings:
        numSiblings += 1
    return numSiblings


def checkGivenElementsFound(soupBowl, numSiblings):
    while True:
        if (siblingCount(soupBowl) + 1 == numSiblings):
            return soupBowl
        soupBowl = soupBowl.parent
    return -1


def answer(firstContent, numSiblings):
    with open("test/test-file2.html", "r") as myfile:
        html_doc = myfile.read().replace('\n', '')
    soup = BeautifulSoup(html_doc, "html.parser")
    matchedElements = soup.find_all("a", text=firstContent)
    if isinstance(matchedElements, list):
        for eachMatchedEle in matchedElements:
            thisResult = checkGivenElementsFound(eachMatchedEle, numSiblings)
            if thisResult != -1:
                return thisResult
    else:
        thisResult = checkGivenElementsFound(eachMatchedEle, numSiblings)
        if thisResult != -1:
            return thisResult
    return -1
    # return fadTitle[0].get_text(', ').encode("utf-8")


if __name__ == "__main__":
    print("Testing Element Extraction")
    print("________________________")
    firstContent = "Software Engineer"
    extractedMatchingElement = answer(firstContent, 6)
    # Printing extracted matching element
    print(extractedMatchingElement)
    # Printing siblings
    printSiblings(extractedMatchingElement)
    print("\n\n-=-=-=-=-=- Extracted Matching Element -=-=-=-=-=-\n\n")
    print(extractedMatchingElement.prettify())
    print("________________________")
    # print(amazonProductInfo('http://goo.gl/qOvGmp'))
