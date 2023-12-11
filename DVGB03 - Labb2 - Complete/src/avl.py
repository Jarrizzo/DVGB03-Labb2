#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        return super().add(v).balance()
    

    def delete(self, v):
        '''
        Calls the super class delete fubnction and then balances
        '''
        return super().delete(v).balance()      
    
    def balance_factor(self):

        #Returns the balance factor that determins the "wheighting" of the tree

        return self.get_lc().height() - self.get_rc().height()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if not self.is_empty():
            if self.balance_factor() == -2:             #Tree is rightside eavy
                if self.get_rc().balance_factor() >= 1:    #Innerside heavy
                    return self.dlr()
                else:
                    return self.slr()                     #Outerside heavy
                
            elif self.balance_factor() == 2:            #Tree is leafside heavy
                if self.get_lc().balance_factor() <= -1:
                    return self.drr()                     #innerside heavy
                else:
                    return self.srr()                     #Outerside heavy
        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        tmp = self.get_rc()
        self.set_rc(tmp.get_lc())
        tmp.set_lc(self)

        return tmp

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        tmp = self.get_lc()
        self.set_lc(tmp.get_rc())
        tmp.set_rc(self)

        return tmp

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.get_rc().srr())

        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.get_lc().slr())

        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
