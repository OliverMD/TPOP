#!/usr/bin/python
# -*- coding: utf-8 -*-

import practical_4_part1 as tasks

def analayseText(text, n):
    text = text.lower()
    words = tasks.splitText(text)
    docLen = len(words)
    wordFreq = tasks.printWordsFrequency(text)
    total = 0.0
    for word in words:
        total += len(word)
    avgLen = total/float(len(words))
    totalWordsN = 0
    for el in wordFreq:
        if len(el[0]) == n:
            totalWordsN += el[1]
    print "Frequency of words:",wordFreq
    print "Total Number of words:", docLen
    print "Average word length:", avgLen
    print str(totalWordsN)+ " words of length "+str(n)+" in text"
analayseText("Lloyds Banking Group has confirmed 9,000 job losses and the net closure of 150 branches over the next three years.The latest job losses - representing about 10 of its workforce - come on top of 43,000 cuts made since 2008.The bank said it would concentrate on urban branch closures first and has abandoned its pledge to keep open 'the last branch in town'.The group is also setting aside another £900m to cover possible payouts for the PPI mis-selling scandal.",4)
