#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
class Option:
    def __init__(self, name, price, children):
        self.name = name
        self.price = float(price)
        self.children = children
    def Execute(self):
        if self.name == "EXIT":
            return -1
        if len(self.children) == 0:
            print "You have selected a",self.name, u", the bill is: £"+ str(self.price) + "0\n"
            for i in range(30):
                print "-",
            print "\n"
            return self.price
        else:
            print "Please choose a number corresponding to a choice:"
            for idx in range(len(self.children)):
                print "["+ str(idx) + "] -", self.children[idx].str()
            choice = raw_input("Enter Choice: ")
            regexp = re.compile('^-?[0-9]+$')
            regres = regexp.match(choice)
            
            if (regres == None) or not(int(choice) in range(len(self.children))):
                print "Please Enter a real choice!"
                return self.Execute()
            else:
                return self.children[int(choice)].Execute()
    def str(self):
        return self.name
    def AddChild(self, child):
        self.children.append(child)
    def AddChildren(self, children):
        for child in children:
            self.AddChild(child)
def runStore():
    item = Option("Shop Item", 0.0,[])
    movie = Option("Movie",0.0,[])
    dvd = Option("DVD",2.5,[])
    blueRay = Option("Blue Ray", 3.5, [])
    game = Option("Game", 0.0, [])
    newGame = Option("New Game", 4.0, [])
    oldGame = Option("Old Game", 2.50, [])
    item.AddChildren([movie,game])
    movie.AddChildren([dvd,blueRay])
    game.AddChildren([newGame,oldGame])
    exit = Option("EXIT",0.0,[])
    item.AddChild(exit)
    res = 0
    while res != -1:
        res = item.Execute()
    return
