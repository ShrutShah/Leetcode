def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pointer1= list1
        count1 = 0 
        while pointer1 != None:
          count1+=1
          pointer1 = pointer1.next
       
        pointer2= list2
        count2 = 0 
        while pointer2 != None:
          count2+=1
          pointer2 = pointer2.next
        
        if count1 == 0 and count2 == 0:
          return None

        elif count1 == 0:
          p= list2
          return p
          
        elif count2 == 0:
          p= list1
          return p
          
        else:
            p= list1
            q= list2
            rpoint = h = ListNode()
            while p != None and q!= None:
              if p.val < q.val:
                h.next = ListNode(p.val)
                h = h.next
                p = p.next
              elif p.val > q.val:
                h.next = ListNode(p.val)
                h = h.next
                q = q.next
              else:
                h.next = ListNode(p.val)
                h = h.next
                p = p.next

                h.next = ListNode(q.val)
                h = h.next
                q = q.next
            
            while q!= None:
              h.next = ListNode(q.val)
              h = h.next
              q = q.next  

            while p!= None:
              h.next = ListNode(p.val)
              h = h.next
              p = p.next

            
            return rpoint.next