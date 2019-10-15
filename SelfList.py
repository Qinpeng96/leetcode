'''链表及常见操作实现
@author:Mr Qi Xiao
@brief:Implement of List and List Operation
@data:2019.10.10
@right:All rights reserved
'''
from typing import List
#define list node structure
class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
#create list
def createList()->ListNode:
    head = ListNode(None);
    return head

#get list length    
def getListLength(head:ListNode)->int:
    num = 0;
    curr = head
    if head.value == None:
        return 0
    while curr!=None:
        num += 1
        curr = curr.next
    return num

#add a elem at end of list
def addNode(head:ListNode,value:int)->None:
    if head.value == None:
        head.value = value
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        newNode = ListNode(value)
        curr.next = newNode

#add node in Nth location
def addNthNode(head:ListNode,value:int,n:int)->ListNode:
    list_len = getListLength(head);
    if n > list_len:
        print('out of range to addNthNode')
        return
    elif n == 1: # add at head node
        new_node = ListNode(value)
        new_node.next = head
        head = new_node
    else:
        curr = head
        pre = curr.next
        for i in range(n-2):
            curr = curr.next
            pre = curr.next
        new_node = ListNode(value)
        curr.next = new_node
        new_node.next = pre  
    return head
#delete a elem at end of list
def removeNode(head:ListNode)->None:
    if getListLength(head) == 0:
        print('list is null')
    elif getListLength(head) == 1:
        head.value = None
    else:
        curr = head
        next = curr.next
        while next.next != None:
            curr = next
            next = next.next
        curr.next = None

#delete Nth Node 
def removeNthNode(head:ListNode,n:int)->ListNode:
    assert(n > 0)
    if n > getListLength(head):
        print('our of range to removeNthNode')
        return
    elif n == 1: #delete head node
        curr = head.next
        head = curr
    else:
        curr = head
        pre = curr.next
        for i in range(n-2):
            curr = curr.next
            pre = curr.next
        curr.next = pre.next    
    return head
#judge list is null
#if empty return true otherwise return false
def isEmpty(head:ListNode)->bool:
    return  0 == getListLength(head)

#get Nth element
def getNthElement(head:ListNode,n:int)->int:
    list_len = getListLength(head)

    if n > list_len:
        print('error:out of range to getNthElement')
        return None
    else:
        curr = head
        for i in range(n-1):
            curr = curr.next
        return curr.value

#get info about list
def printListInfo(head:List)->None:
    num = 0
    if head.value == None:
        num = 0
    else:
        curr = head
        while curr!= None:
            num += 1
            print(curr.value,"->",end="")
            curr = curr.next
        print(" ")
#covert list to a array
def coverToArray(head:ListNode)->List[int]:
    array = []
    curr = head
    while curr != None:
        curr = curr.next
        array.append(curr.value)
    return array

#Test SelfList
def TestList():
    print('this is a test of SelfList')
    head = createList()
    printListInfo(head)
    addNode(head,1)
    addNode(head,2)
    addNode(head,3)
    printListInfo(head)
    print(getNthElement(head,2))
    print(getListLength(head))
    print(isEmpty(head))
    printListInfo(head)
    addNthNode(head,5,2)
    printListInfo(head)
    removeNthNode(head,3)
    printListInfo(head)
    addNthNode(head,5,5)
    printListInfo(head)
    head = removeNthNode(head,1)
    printListInfo(head)
    head = addNthNode(head,7,1)
    printListInfo(head)
    removeNode(head)
    printListInfo(head)

if __name__ == '__main__':
    TestList()