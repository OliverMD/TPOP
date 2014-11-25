
## import all the classes from the file practical_7_datastructure
##(change the name of the file to your file containing YOUR
## classes Item, Member, Library, ...). We assume both files are in
## the same directory.

from solution import *

## Create a new instance of library
main_library = Library()

UID_base = 1

## This is a method to generate unique identifier. It is NOT a good one
## at all, but it is enough for now. In addition it should not be part
## of any of the classes Member, Item, and Library. It is better to leave
## this classes independent from the creation of UIDs in case we want to change
## in the future.
def getUniqueIdentifier(prefix):
    global UID_base
    UID_base += 1
    return str(prefix)+'%010d' % UID_base
    return


def addNewMember(library):
    while True:
        print "\n\n\n"
        fname = raw_input('Enter member\'s firstname: ')
        sname = raw_input('Enter member\'s surname: ')
        postcode = raw_input('Enter member\'s postcode: ')

        ## Here use YOUR class Member constructor
        try:
            library.add_member(fname, sname, postcode, getUniqueIdentifier('usr_'))
            print 'member added successfully.'
            return
        except Exception as err:
            print '\n\n',err.message,'\n\n'
            again = raw_input('An error has occurred, do you want to try again (y/n)? ')
            if again.lower() != 'y':
                return


def addNewItem(library):
    while True:
        print "\n\n\n"
        title = raw_input('Enter item\'s title: ')
        author = raw_input('Enter item\'s Author: ')
        media = raw_input('Enter item\'s media type: ')

        ## Here use YOUR class Item constructor
        try:
            library.add_item(title, author, media, getUniqueIdentifier(media))
            print 'Item added successfully.'
            return
        except Exception as err:
            print '\n\n',err.message,'\n\n'
            again = raw_input('An error has occurred, do you want to try again (y/n)? ')
            if again.lower() == 'n':
                return





## In my class library I have added a 'convenience' method getMembers() to
## return the list of all members object. If you have not done so you must
## change the code below.
def printMembers(library):
    print '\n\n\t      ------------------     \n'
    print '\t Library\'s member list:\n'
    for member in library.getMembers():
        displayMember(member)

    print '\n\t      ------------------     \n\n'


## change the accessors name to make it compatible to YOUR code
## in class Member
def displayMember(member):
    assert isinstance(member, Member)
    print '\t[', member.getUID(), '] name: ', member.getFirstname(),
    print member.getSurname(),
    print ',  borrowed item(s):', len(member.getBorrowed())


def main():
    while True:
        print "Select the action to be performed:"
        print "\t 1 - Return Item"
        print "\t 2 - Borrow Item"
        print "\t 3 - Add New Item"
        print "\t 4 - Add New Member"
        print "\t 5 - Delete Member"
        print "\t 6 - Delete Item"
        print "\t 7 - Print all members"
        print "\t 0 - Exit"

        type_action = raw_input("Enter your choice: ")

        if (type_action == '1'):
            pass
        elif  (type_action == '2'):
            pass
            
        elif  (type_action == '3'):
            addNewItem(main_library)
            
        elif  (type_action == '4'):
            addNewMember(main_library)
            
        elif  (type_action == '5'):
            pass
            
        elif  (type_action == '6'):
            pass
            
        elif  (type_action == '7'):
            printMembers(main_library)
            
        elif (type_action == '0'): #exit the menu
            break
        
        else:
            print "The choice you made was not recognised"
            continue # restart at the begining of the iteration for another input

if __name__ == '__main__':
    main()

