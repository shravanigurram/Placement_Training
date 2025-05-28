class node:
    def __init__(self,data):   #bluprint for node creation
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None
    def add_end(self,data):
        newnode = node(data) #calling node to create newnode
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next= newnode
        
    def display(self):    #traversal all node
        temp=self.head
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def find_junction_cycle(self):   #1] find_junction_cycle 
        fast=self.head
        slow=self.head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return False

        fast=self.head
        while fast!=slow:
            slow=slow.next
            fast=fast.next
        return slow 
    
    def no_of_nodes_in_cycle(self):   #2] no_of_nodes_in_cycle
        '''p=1
        temp=self.find_junction_cycle()
        if temp==False:
            return 0
        temp2=temp.next

        while temp2!=temp:
            p=p+1
            temp2=temp2.next
        return p '''  

        fast=self.head
        slow=self.head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return False
        c=1
        fast=fast.next
        while fast!=slow:
            c=c+1
            fast=fast.next
        return c
    
    def find_cycle(self):    #3]find_cycle
        fast=self.head
        slow=self.head
        while fast!= None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next

            if fast == slow:
                print("cycle")
                break
        else:
            print("no loop")

    def deduct_cycle(self):     #4]deduct_cycle
        fast=self.head
        slow=self.head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return False

        slow=self.head
        while fast!=slow:
            prev=fast
            slow=slow.next
            fast=fast.next
        prev.next=None

    def reverse_using_stack(self):    #5]reverse   using stack
        stack=[]
        temp=self.head
        while temp!= None:
            stack.append(temp.data)
            temp=temp.next
        temp=self.head    
        while temp!=None:
            temp.data=stack.pop()
            temp=temp.next

    def reverse(self):      
        prev=None
        curr=self.head
        #last=curr.next
        while curr!=None:
            last=curr.next
            curr.next=prev
            prev=curr
            curr=last
            #if curr!=None:
                
        self.head=prev      

    def paliandrome_brute(self): #6] paliandrome_check_brute
        temp=self.head
        l=[]
        while temp != None:
            l.append(temp.data)
            temp=temp.next
        l1=[]    

        self.reverse() 
        temp1=self.head
        while temp1 != None:
            l1.append(temp1.data)
            temp1=temp1.next
        if  l==l1:
            print("yes")   
        else:
            print("false")    


    def paliandrome(self):#optimal
        fast=self.head
        slow=self.head

        while fast!=None and fast.next!= None:
            fast=fast.next.next
            pr=slow
            slow=slow.next  

        pr=slow
        prev=None
        curr=slow.next    
       
        while curr:
            last=curr.next
            curr.next=prev
            prev=curr
            curr=last
        pr.next=prev

        check=self.head
        t=True
        while prev!=None: 
            if check.data==prev.data:
                check=check.next
                prev=prev.next
            else:
                t=False
                break
        print(t)

            
            
            

           








l2=LinkedList()
l2.head=node(100)
l2.head.next=node(200)
l2.head.next.next=node(300)
l2.head.next.next.next=node(550)
l2.head.next.next.next.next=node(300)
l2.head.next.next.next.next.next=node(200)
l2.head.next.next.next.next.next.next=node(100)


#print(l2.find_junction_cycle())
#print(l2.no_of_nodes_in_cycle())
#l2.deduct_cycle()
#print(l2.find_junction_cycle())
#l2.display()
#l2.reverse_using_stack()
#l2.reverse()
l2.display()
#l2.paliandrome_brute()

l2.paliandrome()
l2.display()
