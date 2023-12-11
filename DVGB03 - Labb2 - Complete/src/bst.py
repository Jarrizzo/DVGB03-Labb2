#!/usr/bin/env python3

import collections
import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        if self.get_value() == v:
            return True
        if self.get_value() > v:
            return self.get_lc().is_member(v)
        elif self.get_value() < v:
            return self.get_rc().is_member(v)

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        else:
            return 1 + self.get_lc().size() + self.get_rc().size()
        
    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else:
            '''rekursivt anrop för att beräkna storlek'''
            rightNode = self.get_rc().height()
            leftNode = self.get_lc().height()
            return 1 + max(rightNode,leftNode)

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        else:
            return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        else:
            return self.get_lc().postorder() +  self.get_rc().postorder() + [self.get_value()]


    def bfs_order_star(self):
        if self.is_empty():
            return []
        
        Result = []
        bfsQ = [self]
        max_size = pow(2,self.height()) - 1

        firstElement = 0
        while len(bfsQ) <= max_size:
            tmp = BST(1)
            tmp.set_value(None)

            current_node = bfsQ.pop(firstElement)
            Result.append(current_node._value)

            if not current_node.get_lc().is_empty():
                bfsQ.append(current_node.get_lc())
            else:
                bfsQ.append(tmp)
            if not current_node.get_rc().is_empty():
                bfsQ.append(current_node.get_rc())
            else:
                bfsQ.append(tmp)

        return Result

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''

        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self


    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty():
            return self
        
        elif not self.is_member(v):
            print("That element does not exist")
            return self

        #recursevly constructs the tree backwards from the selected (to-be deleted) value
        elif self.get_value() > v:
            return self.cons(self.get_lc().delete(v),self.get_rc())
        elif self.get_value() < v:
            return self.cons(self.get_lc(),self.get_rc().delete(v))
        else:
            return self.delete_root()
           
    #Returns the lowes value, aka lowest child in left child-branch
    def LC_Min_Value(self):
        if self.get_lc().is_empty():
            return self
        else:
            return self.get_lc().LC_Min_Value()
        
    #Returns the highest value, aka lowest child in right child-branch
    def RC_Max_Value(self):
        if self.get_rc().is_empty():
            return self
        else:
            return self.get_rc().RC_Max_Value()

    def delete_root(self):
        #If root has no children then remove that node
        if self.get_rc().is_empty() and self.get_lc().is_empty():
            return self.set_value(None)
        #If root has 1 child and not LC, then remove RC
        elif self.get_lc().is_empty():
            tmp = self.get_rc()
            self.set_value(None)
            return tmp
        #If root has 1 child and not RC, then remove LC
        elif self.get_rc().is_empty():
            tmp = self.get_lc()
            self.set_value(None)
            return tmp
        #If root has 2 children, then check what to promote and then promote
        else:
            #If RC-branch is longer than LC-branch, promote RC
            if int(self.get_lc().height()) < int(self.get_rc().height()):
                current_root = self.get_rc().LC_Min_Value()
                val = current_root.get_value()
                self.set_value(int(val))
                self.set_rc(self.get_rc().delete(int(val)))

            #If LC-branch is longer than RC-branch, promote LC
            else:
                current_root = self.get_lc().RC_Max_Value()
                self.set_value(current_root.get_value())
                self.set_lc(self.get_lc().delete(current_root.get_value()))
            return self
 
if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
