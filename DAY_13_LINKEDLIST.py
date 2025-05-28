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
    def sum_all_node(self):    #1]sum of all nodes
        s=0
        temp=self.head
        while temp != None:
            s=s+temp.data
            temp=temp.next
        print("sum of all nodes:",s) 
    def sum_all_even_node(self):    #2]sum of all even nodes
        s=0
        temp=self.head
        while temp != None:
            if temp.data % 2==0:
                s=s+temp.data
            temp=temp.next
        print("sum of even nodes",s) 

    def sum_all_even_position(self):    #3]sum of nodes present at even positions
        s=0
        i=1
        temp=self.head
        while temp != None:
            if i % 2==0:
                s=s+temp.data
            i=i+1
            temp=temp.next
            
        print("sum of nodes present at even positions:",s)   

    def second_largest_num(self):    #4]finding second largest num  
        first =float('-inf')
        sec=float('-inf')
        temp=self.head
        while temp != None:
            if temp.data > first:
                sec=first
                first=temp.data
            if temp.data >sec and temp.data != first:
                sec=temp.data   
            temp=temp.next
        print("first largest:",first)      
        print("second largest:",sec)

    def sum_consecutive_pair_target(self,k):    #5]sum_consecutive_pair whose sum <=  k
        temp=self.head
        c=0
        s=0
        while temp.next != None:
            s=temp.data+temp.next.data
            if s<=k:
                print(temp.data,end=",")
                print(temp.next.data)
                c=c+1

            temp=temp.next
        print("pairs:",c)   
    def sum_all_pair_target(self,k):    #6]sum_of_all_pair whose sum <=  k
        temp=self.head
        c=0
       
        while temp != None:
            s=0
            temp1=temp.next
            while temp1 != None:
                s=temp.data+temp1.data
                if s<=k:
                    print(temp.data,end=",")
                    print(temp1.data)
                    c=c+1    
                temp1=temp1.next     
            temp=temp.next
        print("pairs:",c)    

    def print_sec_half_brute(self):     #print second half list
        i=1
        temp=self.head
        while temp!=None:
            i=i+1
            temp=temp.next
        j=1    
        temp1=self.head
        while temp1!=None:
            if j>i//2:
                print(temp1.data)
            j=j+1

            temp1=temp1.next
    def find_middle_print_sec_half(self):  #7]find middle element and print second half list
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            print(slow.data,end="->")
    
            slow=slow.next
        print(slow.data)
        while slow!= None:
            print(slow.data,end="->")
            slow=slow.next
        print("None")

    def print_kth_element_from_last_brute(self,k):   #8] print_kth_element_from_last_brute
        i=1
        temp=self.head
        while temp!=None:
            i=i+1
            temp=temp.next
        j=1    
        temp1=self.head
        while temp1!=None:
            if j==i-k:
                print("print_kth_element_from_last:",temp1.data)
                break
            j=j+1

            temp1=temp1.next
    def print_kth_element_from_last(self,k): #print_kth_element_from_last
        fast=self.head
        slow=self.head
        for i in range(k):
            if fast!=None:
                fast=fast.next

        while fast!= None:
            fast=fast.next
            slow=slow.next
        if slow!=None:
            print(slow.data)      

    def delete_kth_element_from_last(self,k): #delete_kth_element_from_last
        fast=self.head
        slow=self.head
        self.prev=slow
        for _ in range(k):
            if fast!=None:
                fast=fast.next

        while fast!= None:
            self.prev=slow
            fast=fast.next
            slow=slow.next
        self.prev.next = slow.next

    def swap_pairs(self):#swap_pairs
        temp=self.head
        
        while temp!=None and temp.next!=None:
            temp.data,temp.next.data=temp.next.data,temp.data
            temp=temp.next.next
            

    def bubblesort(self):  #perform bubblesort
        temp=self.head
        while temp.next!=None:
            t=self.head
            flag=0
            while t.next!= None:
                if t.data >t.next.data:
                    t.data,t.next.data=t.next.data,t.data
                    flag=1
                t=t.next   
            if flag==0:
                break
            temp=temp.next 

    def bubblesort_kth_largest_element(self,k):  #perform bubblesort_kth_largest_element
        temp=self.head
        k1=k
        while temp.next!=None:
            t=self.head
            flag=0
            while t.next!= None:
                if t.data >t.next.data:
                    t.data,t.next.data=t.next.data,t.data
                    flag=1
                t=t.next   
            if flag==0:
                break
            if k1==0:
                break

            k1=k1-1
            temp=temp.next
        self.print_kth_element_from_last(k)

    def find_cycle(self):
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

    def find_junction_cycle(self):
        fast=self.head
        slow=self.head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
            else:
                return ("no loop")

        fast=self.head
        while fast!=slow:
            slow=slow.next
            fast=fast.next
        return slow.data   



l1=LinkedList() 
l1.head=node(10)
l1.add_end(8)
l1.add_end(7)
l1.add_end(6)
l1.add_end(5)
l1.add_end(4)
l1.add_end(3)

#l1.display()
'''l1.sum_all_node()
l1.sum_all_even_node()
l1.sum_all_even_position()
l1.second_largest_num()
l1.sum_consecutive_pair_target(10)
l1.sum_all_pair_target(10)
#l1.print_sec_half()
l1.find_middle_print_sec_half()
l1.print_kth_element_from_last_brute(3)
l1.print_kth_element_from_last(8)
#l1.delete_kth_element_from_last(3)
l1.swap_pairs()
l1.display()
#l1.add_front(123)
#l1.bubblesort()
l1.bubblesort_kth_largest_element(3)
l1.display()
l1.find_cycle()'''

l1.swap_pairs()
#l1.display()



l2=LinkedList()
l2.head=node(100)
l2.head.next=node(200)
l2.head.next.next=node(300)
l2.head.next.next.next=node(400)
l2.head.next.next.next.next=node(500)
l2.head.next.next.next.next=l2.head.next
print(l2.find_junction_cycle())