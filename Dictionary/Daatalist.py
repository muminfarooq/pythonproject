# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:34:48 2020

@author: Mumin
"""

class Node:
    
    def __init__(self):
        self.next=None
    
    def insert_after(self,new_node):
        
        if not isinstance(new_node,Node):
            raise TypeError('new shoulde be a node')
        new_node.next=self.next
        self.next=new_node
    
    def remove_after(self):
        temp=self.next
        if temp:
            self.next=temp.next
            temp.next=None
        return temp
    def __str__(self):
        return f"id={id(self):#x}"


class LinkedList:
    
    def __init__(self):
       self.head=Node()
    
    def add_to_head(self,new_node):
        self.head.insert_after(new_node)
    
    
    def remove_from_head(self):
        self.head.remove_after()
    
    def isempty(self):
        self.head.next=None
    
    def __str_(self):
        SEPERATOR='=>'
        LEN_SEPERATOR=len(SEPERATOR)
        if self.isempty():
            return "\n [empty list] \n"
        ret_str="\n [START LIST] :"
        temp=self.head
        while temp.next:
            temp=temp.next
            ret_str+=(str(temp) +SEPERATOR)
        ret_str=ret_str[:-LEN_SEPERATOR] +"[END LIST]"
        return ret_str
    

    def reset_current(self):
        self.current=self.head
    
    def iterate(self):
        if not self.current:
            return None
        temp=self.current.next
        self.current=temp
        return temp
    
class DataNode(Node):
     """
     DataNode subclass of Node.
     It is the node class for a data list.
     Requires data item, data, be vetted by client (DataList)
     """
     def __init__(self,data):
        super().__init__()
        self.data=data
    
     def __str__(self):
        return str(self.data)
    
class DataList(LinkedList):
     """
    DataList can store arbitrary data
    """
     def add_to_head(self,data):
        return super().add_to_head(DataNode(data))
     def remove_after(self):
         return super().remove_from_head().data
     
     def insert_sorted(self,data):
         temp=self.head
         while temp.next:
             if data <=temp.next.data:
                 break
             temp=temp.next
         temp.insert_after(DataNode(data))    
         
     def remove(self,data):
         temp=self.head
         while temp.next:
             if temp.next.data==data:
                 temp.remove_after()
                 return True
             temp=temp.next
         return False
     
    
    
    
    
    
    
    
    


















    
        
    
