class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_at_begining(self,data):
    node = Node(data, self.head)
    self.head = node

  
  def insert_at_end(self,data):
    if self.head == None:
      self.insert_at_begining(data)
    else:
      itr = self.head
      while itr.next:
          itr = itr.next
      
      itr.next = Node(data,None)

  def insert_values(self,data_list):
    self.head = None
    for i in data_list:
      self.insert_at_end(i) 
  def get_length(self):
    p = self.head 
    c = 0
    while p!= None:
      c+=1
      p = p.next
    return c

  def remove_at(self,index):
    if index <0 or index>=self.get_length():
      raise Exception("invalid index") 
    itr = self.head 
    counter = 0
    while(itr!= None):
      if counter == index-1:
         itr.next = itr.next.next
         break
      itr = itr.next
      counter+=1
    
  def insert_at(self,index, data):
    if index <0 or index>=self.get_length():
      raise Exception("invalid index")
    
    if index == 0:
      self.insert_at_begining(data)
    
    itr = self.head
    counter =0
    while itr!= None:
      if counter == index -1:
        t = Node(data,itr.next)
        itr.next = t      
      itr = itr.next
      counter +=1







  def print(self):
    if self.head == None:
      print("empty")
      return
    else:
      itr = self.head
      print_string = ''
      while itr:
        print_string += str(itr.data) + '-->'
        itr = itr.next

      print(print_string)
