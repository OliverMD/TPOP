class Member:
    def __init__(self, uid, fName, lName, pCode):
        self.uid = uid
        self.fName = fName
        self.lName = lName
        self.pCode = pCode
        self.loanItems = []
    def __repr__(self):
        return "<Member UID = " + str(self.uid) + ", " + self.fName + ", " + self.lName + ", " + self.pCode + ", " + str(self.loanItems)
    def getID(self):
        return self.uid
    def getFirstName(self, newName = ""):
        if newName != "":
            return self.fName = newName
        else:
            return self.fName
    def getLastName(self, newName = ""):
        if newName != "":
            return self.lName = newName
        else:
            return self.lName
    def getPostCode(self, newCode = ""):
        if newCode != "":
            return self.pCode = newCode
        else:
            return self.pCode
    def getLoanItems(self):
        return self.loanItems
    def addLoanItem(self, newItem):
        self.loanItems.append(newItem)

class Item:
    def __init__(self, uid, title, author, media, available = True, loaneeId = None):
        self.uid = uid
        self.title = title
        self.author = author
        self.media = media
        self.available = available
        self.loaneeId = None
    def __repr__(self):
        return "<Item UID = " + str(self.uid) + ", " + self.title + ", " + self.author + ", " + self.media + ", " str(self.available) + ", " + str(self.loaneeId) + ">"
    def getID(self):
        return self.uid
    def getTitle(self, title = ""):
        if title != "":
            return self.title = title
        else:
            return self.title
    def getAuthor(self, author = ""):
        if author != "":
            return self.author = author
        else:
            return self.author
    def getMedia(self, media = ""):
        if media != "":
            return self.media = media
        else:
            return self.media
    def getAvailable(self, available = None):
        if available != None:
            return self.available = available
        else:
            return self.available
    def getLoaneeId(self, id  = None):
        if id != None:
            return self.uid = id
        else:
            return self.uid

class
