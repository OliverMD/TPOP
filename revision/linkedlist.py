class List:
    """
    A linked list that is unsorted.
    It has volatile indices.
    """
    class _Node:
        def __init__(self, val, tail):
            self.tail = tail
            self.val = val
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def insertByElement(self, element):
        """
        Inserts the given element at the front of the list
        Returns True if added
        Returns False if it fails
        """
        node = List._Node(element, None)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.tail = self.head
            self.head = node
        self.length += 1
        return True
            
    def insertByIndex(self, index, element):
        """
        Inserts the element at the given index, replacing element already there.
        Returns True if added successfully
        Returns False if index doesn't exist
        """

        #Init loop variables
        head = self.head
        cnt = 0
        
        while head != None and cnt != index:
            cnt += 1
            head = head.tail
        if head == None:#The case where the index does not exist
            return False
        else:#The case where the index is found
            head.val = element #Just need to replace the value, pointers are still useful
            self.length += 1
            return True
            
    def removeByElement(self, element):
        """
        Removes all occurances of element that it finds
        Returns how many occurances are deleted
        """
        #Init loop variables
        head = self.head
        prevHead = None #Will act as the k-1 node where head is the k node tested
        cnt = 0 #How many have we deleted
        
        while head != None:
            if head.val == element:
                #Needs deleteing
                if self.head == head:
                    self.head = head.tail
                    head = self.head
                else:
                    prevHead.tail = head.tail
                    head = prevHead.tail
                cnt += 1
                self.length -= 1
            else:
                prevHead = head
                head = head.tail
                
        return cnt
                    
        
    def removeByIndex(self, index):
        """
        Removes the element at the index given
        Returns True if deleted
        Returns False if it's not deleted
        """
        head = self.head
        prevHead = None
        cnt = 0 #Acts as the index count for the loop

        while head != None and cnt != index:
            prevHead = head
            head = head.tail
            cnt += 1
            
        if head == None:
            return False
        else:
            prevHead.tail = head.tail
            self.length -= 1
            return True
        
    def findByIndex(self, index):
        """
        Finds the element at the specified index
        Retuns element
        Returns None if not found
        """
        head = self.head
        cnt = 0

        while head != None and cnt != index:
            cnt += 1
            head = head.tail

        if head == None:
            return None
        else:
            return head.val
    
        
    def find(self, element):
        """
        Finds the indices of all occurences of the  element
        Returns tuple of all found indices
        Returns None if not found
        """
        head = self.head
        found = []
        cnt = 0

        while head != None:
            if head.val == element:
                found.append(cnt)
            cnt +=1
            head = head.tail

        return tuple(found)
    
    def findMin(self):
        """
        Finds the smallest element in the list, defined by gt and lt.
        Retuns (index, element) pair
        Returns None if list is empty
        """
        head = self.head
        minVal = None
        minIdx = 0
        cnt = 0
        if head != None:
            minVal = head.val
        else:
            return None

        while head != None:
            if minVal > head.val:
                minVal = head.val
                minIdx = cnt
            cnt += 1
            head = head.tail

        return (minIdx, minVal)

    def findMax(self):
        """
        Finds the largest element in the list, defined by gt and lt.
        Returns (index, element) pair
        Returns None if list is empty
        """
        head = self.head
        maxVal = None
        maxIdx = 0
        cnt = 0
        if head != None:
            maxVal = head.val
        else:
            return None

        while head != None:
            if maxVal < head.val:
                maxVal = head.val
                maxIdx = cnt
            cnt += 1
            head = head.tail

        return (maxIdx, maxVal)

if __name__ == "__main__":
    list1 = List()
    list1.insertByElement(34)
