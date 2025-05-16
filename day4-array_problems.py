#1] find frequency of a number in a given array
'''
def countk(l,k,i,p):
    if i == len(l):
        return p
    if l[i] == k:
        p = p + 1
    return countk(l,k,i+1,p)    
     
l = [2,4,5,6,4,5,4,5,4,6,7,6,5]
k = 0
print(countk(l,k,0,0))
'''
#3] find the array number which has occurance n using recursion for both traversing array and counting frequency of every elemnet in array
'''def countk(l,k,i,p):
    if i == len(l):
        return p
    if l[i] == k:
        p = p + 1
    return countk(l,k,i+1,p)

def find_frequency(l,val,j):
    if j == len(l):
        return -1
    qq= countk(l,l[j],0,0)
    if qq == val:
        return l[j]
    return find(l,val,j+1)  
 
l = [2,5,6,4,5,4,5,4,6,7,6,5]
val = 4
print(find_frequency(l,val,0))'''




#3i] find the array number which has occurance n using recursion with dictionary( recursion for building dictionary and finding key of given frequency using for)
 
'''def find_frequency_valued_key(d,val):
    for key,value in d.items():
        if value == val:
            return key
    return -1 

def recursion_dictionary(l,d,val,i):
    if i == len(l):
        return find_frequency_valued_key(d,val)    
    if l[i] not in d:
        d[l[i]] = 1    
    else:
        d[l[i]] += 1
    return recursion_dictionary(l,d,val,i+1)
l = [2,5,6,4,5,4,5,4,6,7,6,5]
val = 90
d = {}
x = recursion_dictionary(l,d,val,0)
if x == -1:
    print("Not find")
else:
    print(x)
'''

#3ii] find the array number which has occurance n using recursion with dictionary( recursion for building dictionary and finding key of given frequency)

'''def find_frequency_valued_key(d,dkeys ,val,j = 0):
    if j == len(d):
        return "-1"
    if d[dkeys[j]] == val:
        return dkeys[j]
    return find_frequency_valued_key(d,dkeys ,val,j+1)
   

def recursion_dictionary(l,d,val,i):
    if i == len(l):
        return find_frequency_valued_key(d,list(d.keys()),val)    
    if l[i] not in d:
        d[l[i]] = 1    
    else:
        d[l[i]] += 1
    return recursion_dictionary(l,d,val,i+1)
l = [2,5,6,5,4,5,4,6,7,6,5,5,5,5]
val = 7
d = {}
x = recursion_dictionary(l,d,val,0)
if x == -1:
    print("Not find")
else:
    print(x)'''



def printing_subsets(array,l = [],i=0):
    if i == len(array):
        print(l)
        return l
    
    printing_subsets(array,l+[array[i]],i + 1)
    return printing_subsets(array,l,i+1)

array = [2,3,4]

printing_subsets(array)


'''def subset_sum(a,k,i=0):
    if k == 0:
        return True
    if i == len(a):
        return False
    return subset_sum(a,k-a[i-1],i+1) or subset_sum(a,k,i+1)

a = [1,2,3,5] 
k = 7 
print(subset_sum(a,k,0)) '''


# to get subarray which sum ==  given value
'''def subset_sum(a,k,l=[],i=0):
    if i == len(a):
        if k == 0:
            print(l)
        return 
    if a[i] <= k:
        subset_sum(a,k-a[i],l+[a[i]],i+1)
    subset_sum(a,k,l,i+1)
    

a = [1,2,3,5] 
k = 7 
subset_sum(a,k)'''



#
'''def subset_sum(a,k,l=0,i=0,m=float('inf')):
    if i == len(a):
        if k == 0:
            print(l)
            if l < m:
                m =l
        return m        
     
    if a[i] <= k:
        m = subset_sum(a,k-a[i],l+1,i+1,m)
    m = subset_sum(a,k,l,i+1,m)
    return m
    
a = [1,2,3,5,0] 
k = 5
x = subset_sum(a,k)
print("")
if x == float('inf'):
    print("Not found")
else:
    print(x)'''

# Greedy algorithm for finding largest even, smallest odd 
'''def evenodd(l):
    odd = float('inf')
    even = float('-inf')
    for i in range(len(l)):
        if l[i] & 1 == 0:
            if even < l[i]:
                even = l[i]
        else:
            if odd > l[i]:
                odd = l[i]
    print(even)
    print(odd)            


l = list(map(int,input().split()))
evenodd(l)'''


'''def evenodd(l):
    second = float('-inf')
    first = float('-inf')
    for i in range(0,len(l)):
        if l[i] > first:
            second = first
            first = l[i]
        elif l[i] > second and l[i] != first:
            second = l[i]   

        
    print("second highest", second)    
    print("higest", first)
        
                


l = list(map(int,input().split()))
evenodd(l)'''
