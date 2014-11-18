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
class Item:
    """
    class Item:
    A class that represents an object that is loanable by the library.
    """
    def __init__(self, uid, title, author, media, available, loaneeId = None):
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
class Store:
    """
    class that rerpesents a library that has items for loan by it's members.
    Defines the operations:
     -- addMember: Adds a new member to the library
     -- removeMember: Removes a member from the library
     -- addItem: Adds an item to the library
     -- removeItem: Removes an ite from the library.
    """
    def __init__(self, members= [], items = []):
        """
        __init__(self, members [Member], items [Item]) --> Store
        members: A list of members for the store to be initialised with
        items: A list of items for the store to be initialised with.
        """
        self.muid = 0
        self.members = {}
        for i in members:
            self.muid = max(self.muid, i.uid)
            try:
                self.members[i.uid]
            except KeyError:
                self.members[i.uid] = i
        self.muid += 1
        self.items = {}
        self.iuid = 0
        #Most likely searching by title.
        for i in items:
            self.iuid = max(self.iuid, i.uid)
            try:
                self.items[i.title].append(i)
            except KeyError:
                self.items[i.title] = [i]
        self.iuid += 1
    def addMember(self, member):
        """
        addMember(self, member Member) --> Bool
        member: The member that needs to be added to the library
        
        returns True if succesfully added.
        returns False if the member is already present.
        """
        if member.uid != None:
            try:
                self.members[member.uid]
            except:
                self.members[member.uid] = member
                return True
            return False
        else:
            self.members[self.muid] = member
            muid += 1
            return True
            
    def addItem(self, item):
        """
        addItem(self, item Item) --> Bool
        item: The item that wants to be added to the library.
        
        returns True if successfully added to the collection
        Assigns a new uid to the Item for use within the library,
        doesn't change the Item passed.
        """
        try:
            self.items[item.title].append(Item(self.iuid, item.title, item.author, item.media, item.available, item.loaneeId))
        except KeyError:
            self.items[item.title] = [Item(self.iuid, item.title, item.author, item.media, item.available, item.loaneeId)]
        self.iuid += 1
        return True
    def removeMember(self, uid):
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
    def removeItem(self, uid = None, title = ""):
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
mem1 = Member(0, "Oliver", "Downard", "TN13 2EE")
mem2 = Member(1, "Jeff", "Hurst", "FG56 6FP")
item1 = Item(0, "LOL", "LOLCAT", "DVD", True, None)
store = Store()
