class Member:
    """
    class Member:
    A class that will describes a human member of a small library.
    Being a member means that they can loan items from said library
    """
    def __init__(self, uid, fName, sName, pCode, items = []):
        """
        __init__(self, uid int, fName string, sName string, pCode string, items [Item]) --> Member
        uid: A unique identifier for the member unique relative to the library at which they are registered
        fName: Member's first name.
        sName: Member's last name.
        pCode: Member's postcode.
        items: Items loaned to member

        Creates a Member object, an insatnce of the class Member
        """
        self.uid = uid
        self.fName = fName
        self.sName = sName
        self.pCode = pCode
        self.items = items
    def __repr__(self):
        return "<Member: uid = " + str(self.uid) + ", " + self.fName + ", " + str(self.items) + ">" 
class Item:
    """
    class Item:
    A class that represents an object that is loanable by the library.
    """
    def __init__(self, uid, title, author, media, available= True, loaneeId = None):
        """
        __init__(self, uid int, title string, author string, media string, available bool, loaneeId int) --> Item
        uid: A unique id that identifies the item in the library.
        title: The title of the item
        author: The author of the item
        media: The medium of the item, eg. book, dvd, cd, game.
        available: True if available for loan, false otherwise
        loaneeId: If loaned, the id of the loanee, None if not loaned
        """
        self.title = title
        self.author = author
        self.media = media
        self.available = available
        self.uid = uid
        self.loaneeId = loaneeId
    def __repr__(self):
        return "<Item: uid  = " + str(self.uid) + ", " + self.title + ", " + str(self.available) + ", " + str(self.loaneeId) + ">"
class Library:
    """
    class that rerpesents a library that has items for loan by it's members.
    Defines the operations:
     -- addMember: Adds a new member to the library
     -- removeMember: Removes a member from the library
     -- addItem: Adds an item to the library
     -- removeItem: Removes an ite from the library.
    """
    def __init__(self):
        """
        __init__(self, members [Member], items [Item]) --> Library
        """
        self.members = {}
        self.items = {}
    def __repr__(self):
        return "<Library members = " + str(self.members) + "|| items = " + str(self.items) + ">"
    def add_member(self, member):
        """
        addMember(self, member Member) --> Bool
        member: The member that needs to be added to the library
        
        returns True if succesfully added.
        returns False if the member is already present and the member is not added
        """
        if member.uid in self.members:
            return False
        else:
            self.members[member.uid] = member
            return True
            
    def add_item(self, item):
        """
        addItem(self, item Item) --> Bool
        item: The item that wants to be added to the library.
        
        returns True if successfully added to the collection
        Assigns a new uid to the Item for use within the library,
        doesn't change the Item passed.
        """
        try:
            self.items[item.title].append(Item(item.uid, item.title, item.author, item.media, item.available, item.loaneeId))
        except KeyError:
            self.items[item.title] = [Item(item.uid, item.title, item.author, item.media, item.available, item.loaneeId)]
        return True
    def remove_member(self, uid):
        """
        removeMember(self, uid) --> Bool
        uid: the id of the member to remove from the collection

        Returns True if member was successfully removed.
        Returns False if the member to delete doesn't exist
        """
        try:
            del self.members[uid]
            return True
        except KeyError:
            return False
    def remove_item(self, uid = None, title = ""):
        """
        removeItem(self, uid int, title string) --> Bool
        uid: The id of the item to be deleted
        title: the title of the item to be deleted.

        Only either title or uid can be set, returns false if both
        or none are set.

        Returns True if item successfully deleted
        Returns False if item doesn't exist or error in
        parameters.
        """
        if uid != None and title == "":
            for k in self.items:
                for i in range(len(self.items[k])):
                    if self.items[k][i].uid == uid:
                        del self.items[k][i]
            return True
        elif uid == None and title != "":
            del self.items[title]
            return True
        else:
            return False
    def borrow_item(self, name , member):
        if name != None and type(name) == str:
            try:
                possItems = self.items[name]
                for item in possItems:
                    if item.available == True:
                        item.available = False
                        item.loaneeId = member.uid
                        member.items.append(item.uid)
                        return item.uid
                #Here there is not a free item
                return -1
            except KeyError:
                #Item doesn't exist
                raise ValueError("Name is not valid!")

    def return_item(self, item_id):
        for item in self.items:
            for i in self.items[item]:
                if i.uid == item_id:
                    i.available = True
                    for j in range(len(self.members[i.loaneeId].items)):
                        if self.members[i.loaneeId].items[j] == item_id:
                            del self.members[i.loaneeId].items[j]
                            break
                    i.loaneeId = None
    def getMembers(self):
        return [self.members[mem] for mem in self.members]
lib = Library()
lib.add_item(Item(0, "TITLE", "AUTHOR", "MEDIA"))
lib.add_member(Member(0,"NAME", "LNAME", "PostCode"))
print lib
bid = lib.borrow_item("TITLE", lib.getMembers()[0])
print lib
lib.return_item(bid)
print lib
