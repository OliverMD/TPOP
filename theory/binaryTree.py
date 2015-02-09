"""
TODO:
Add wrapper to binary tree in order to correctly implement ditcionary.
This is so that the rotations will work.
"""


class BinaryTree:
    """Implements the abstract class Tree and probides operations
    for keeping the height logn
    """
    
    def __init__(self):
        """creates and empty binary tree
        """
        self._parent = None
        self._key = None
        self._data = None
        self._left = None
        self._right = None

    def insert(self, key, data):
        self._insertRecurse(key, data, None);
    def _insertRecurse(self,key,data, parent):
        """
        Inserts an entry with a given key and a given data value.
        """
        if self._data == None:
            self._data = data
            self._key = key
            self._parent = parent
            
        else:
            if key < self._key:
                if self._left != None: #Check if left node exists
                    self._left._insertRecurse(key,data, self) #If it does recursively call it's insert
                    
                else:
                    self._left = BinaryTree() #If not create it and call it's insert, which is a tail call.
                    self._left._insertRecurse(key,data, self)
                    
            else:
                if self._right != None: #The sae process as above here. Check if the right node exists.
                    self._right._insertRecurse(key,data, self) #If it does recursively call insert
                    
                else:
                    self._right = BinaryTree() #If not then create it.
                    self._right._insertRecurse(key,data,self)
                    
        if abs(self._getBalanceFactor()) > 1: #Check if balancing is needed
            #balanceTree()
            pass

    def balanceTree(self):
        #Find which sub tree is larger than the other
        if self._right._getDepth() > self._left._getDepth():
            #If Right then check if right right or right left case
            if self._right._right._getDepth() > self._right._left._getDepth():
                self._leftRotate() #Left rotate around this nodes right child
            else:
                pass
            ##If right left case
            ###Right pivot around this nodes right child
            ###Then left pivot around the resulting right child.
        else:
            pass
            #If Left check if it is left left or left right case
    
    def _getDepth(self):
       if self._left != None and self._right != None:
           return max(self._left._getDepth() + 1, self._right._getDepth() + 1)
       
       elif self._left != None:
           return self._left._getDepth() + 1
       
       elif self._right != None:
           return self._right._getDepth() + 1
       
       else:
           return 1

    def _getBalanceFactor(self):
        if self._left != None and self._right != None:
            return self._left._getDepth() - self._right._getDepth()

        elif self._left != None:
            return self._left._getDepth() - 0
        
        elif self._right != None:
            return 0 - self._right._getDepth()
        
        else:
            return 0

    def _leftRotate(self):
        """Rotates left, with this node as the pivot and the it's right child becoming the root"""
        #This node is the root of the sub tree, we are pivoting around it's right child.
        #Take right child and set it as root, bear in mind the case where this node is root of the
        #entire tree and has no parent.
        parent = self._parent
        o = self
        r = self._right
        l = self._left
        rl = self._right._left
        self = r
        if parent != None:
            if parent._left == o:
                parent._left = self
            else:
                parent._right = self
        self._left = o
        o.right = rl
        o._parent = self._parent
        self._parent = parent
        #Take the right childs left node and make it right child of this node.
        #Make this child left child of the new root node. Remebering to set this nodes parent


    def _reprRecurse(self, cnt):
        if self._left != None and self._right != None:
            return "<{0} - [{3}, {4}]::: {1}, {2}>".format(cnt, self._left._reprRecurse(cnt+1), self._right._reprRecurse(cnt+1), self._key, self._data)
        
        elif self._left != None:
             return "<{0} - [{2}, {3}]::: {1}>".format(cnt, self._left._reprRecurse(cnt+1), self._key, self._data)
         
        elif self._right != None:
             return "<{0} - [{2}, {3}]::: {1}>".format(cnt, self._right._reprRecurse(cnt+1), self._key, self._data)
         
        else:
             return "<{0} - [{1}, {2}]>".format(cnt, self._key, self._data)
    
    def __repr__(self):
        return self._reprRecurse(0)
    
    def delete(self, key):
        pass

if __name__ =="__main__":
    a = BinaryTree()
    print a
    a.insert(4,"a")
    a.insert(5,"b")
    a.insert(6,"c")
    print a
    a._leftRotate()
