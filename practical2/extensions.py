class Option:
    def __init__(self, name, price, children):
        self.name = name
        self.price = float(price)
        self.children = children
    def Execute(self):
        if len(self.children) == 0:
            print "You have selected a",self.name, ", the bill is: £"+string(self.price)
            return self.price
        else:
            print "Please choose a number corresponding to a choice:"
            for idx in range(len(self.children)):
                print "["+string(idx)+"] -", self.children[idx].Show()
            choice = int(raw_input("Enter Choice: "))
            if not(choice in range(len(self.children))):
                print "Please Enter a real choice!"
                return self.Execute()
            else:
                return self.children[choice].Execute()
    def Show(self):
        print self.name
    def AddChild(self, child):
        self.children.append(child)
    def AddChildren(self, children):
        for child in children:
            self.AddChild(child)
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
item.Execute()
