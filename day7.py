# merge two sorted list 
'''first = [2,4,5,8,9]
second = [3,5,6,9,11,12,13]
#f = [0]*(len(k)+len(p))
final = []
i = 0
j = 0

while i < len(first) and j < len(second):
    if first[i] < second[j]:
        #f[h] = k[q]
        final.append(first[i])
        i = i + 1
    else:
        final.append(second[j])
        j = j + 1
    #h += 1

while i < len(first):
    #f[h] = k[q]
    final.append(first[i])
    i = i + 1
    #h = h + 1

while j < len(second):
    final.append(second[j])
    j = j + 1
    #h = h + 1
print(final) '''




'''def mergesort(l):
    if len(l) > 1:
        mid = len(l) // 2
        L = l[:mid]
        R = l[mid:]
        mergesort(L)
        mergesort(R)
        i,j,k = 0,0,0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:   
                l[k] = L[i]
                i = i + 1
            else:
                l[k] = R[j]
                j = j + 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            l[k] = R[j]
            k += 1
            j += 1

    return l    
    




l = [4,6,2,8,9,2,8,0,4,8,9,9,0,45,2,3]
l.sort()
print(l)
print(mergesort(l))'''

# given unsorted find kth largest element using bucket  sort

'''def find_kth_largest(l,k):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1


    n = max(l)
    bucket = []  
    for i  in range(n):
        bucket.append([])   

    print(bucket)   
    print(d)
    for keys in d.keys():
        bucket[keys-1].append(keys)
    print(bucket)     

    for i in bucket:
        if len(i) == 0:
            bucket.remove(i)  
    print(bucket)  
    print(bucket[len(bucket)-k])      
    

l = [4,6,2,8,9,2,8,0,4,8,9,9,0,2,3]
find_kth_largest(l,3)'''

# kth largest element considering the frequency also means len(l) - k = x

'''def find_kth_largest(l,k):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    n = max(l) + 1
    bucket = []  
    for i  in range(n):
        bucket.append(0)   

    print(bucket)   #[[], [], [], [], [], [], [], [], [], []]
    print(d)   #{4: 2, 6: 1, 2: 3, 8: 3, 9: 3, 0: 2, 3: 1}

    for keys,values in d.items():
         
        for _ in range(values):
            bucket[keys].append(keys)
            
    print(bucket)  #[[0, 0], [], [2, 2, 2], [3], [4, 4], [], [6], [], [8, 8, 8], [9, 9, 9]]  
    for i in bucket:
        if len(i) == 0:
            bucket.remove(i) 
    print(bucket)   #[[0, 0], [2, 2, 2], [3], [4, 4], [6], [8, 8, 8], [9, 9, 9]]


    p = []
    for i in bucket:
        p = p + i
    print(p) 

    print(p[len(p) - k]) 

l = [4,6,2,8,9,2,8,0,4,8,9,9,0,2,3]
find_kth_largest(l,3)'''



# finding kth largest element with considering frequency
'''def find_kth_largest(l,k):
    b = [0] * (max(l)+1)
    print(b)
    
    for i in l:
        b[i] += 1
    print(b)

    for i in range(len(b)-1,-1,-1):
        if b[i] != 0:
            k = k - b[i]
        if k <= 0:
            print(i)
            break

    

l = [4,6,2,8,9,2,8,0,4,8,9,9,0,2,3]
find_kth_largest(l,3)'''


# print largest frequency element 
'''def largest_freq_ele(a):
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)
    m = 0 
    p = 0

    for keys,values in d.items():
        if values > m:
            m = values
            p = keys
    print(p) 

    for keys,values in d.items():
        if values == m:
            print(keys)       
a = [0,2,2,2,3,3,4,4,4]
a.sort()
print(a)
largest_freq_ele(a)'''

# print kth largest element

'''def kth_largest_freq_ele(a,k):
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)

    m = max(d.values())

    b = [0] * (m+1)
    for keys,values in d.items():
        b[values] = keys

    print(b[-k])     

a = [0,2,2,2,3,3,4,4,4]
kth_largest_freq_ele(a,3)'''

# you ar given an input find with dictionary print element which frequency has > half of the length

'''def freq(a):
    d = {}
    k = len(a) // 2
    print("k:", k)

    for i in a:
        if i not in d:
            d[i] = 1 
            if d[i] > k:
                print(i)     
        else:
            d[i] += 1    
            if d[i] > k:
                print(i)    

   


l = [2,1,2,1,1,2,1,2,2]  
freq(l)         
'''


# 
'''def freq(l):
    k = len(l) // 2
    f = 0
    for i in l:
        p = l.count(i)
        if p > k:
            f = i
    print(f)        
'''
# MORRIE's algorithm
'''def freq(l):
    c = 1
    res = l[0]
    for i in range(1,len(l)):
        if res == l[i]:
            c = c + 1
        elif c == 0:
            res = l[i]    
        else:
            c = c - 1
        #important    
            

    print(res)   
def freq1(l):
    c = 1
    res = l[0]
    for i in range(1,len(l)):
        if res == l[i]:
            c = c + 1    
        else:
            c = c - 1  
            if c == 0:
                res = l[i]  
                c = 1 
                
    print(res)            


l = [9,1,9,0,9,3,9,4,9]  
freq(l) 
freq1(l)'''



# return highest index value of k


'''l = [2,3,4,5,6,7,8,4,2,4,3,1]
k = 4
index = float('-inf')
t = False
for i in range(len(l)-1,-1,-1):
    if l[i] == k:
        index = i 
        t = True
        break
if t == False:
    print(-1)
else:
    print(index)'''    




# last occurace index of element using binary search
'''arr= [2,3,4,5,7,9,9,9,10,12]
l = 0
k = 9
n = len(arr)
res = 0
while l <= n:
    mid = (l + n) // 2
    if arr[mid] == k:
        res = mid    
        l = mid + 1       
    elif k > arr[mid]:
        l = mid + 1
    elif k < arr[mid]:
        n = mid - 1
print(res)'''

# last occurace index of element using binary search
'''arr= [2,3,4,5,7,9,9,9,10,12]
l = 0
k = 9
n = len(arr)
res = 0
while l <= n:
    mid = (l + n) // 2
    if arr[mid] == k:
        res = mid    
        l = mid + 1       
    elif k > arr[mid]:
        l = mid + 1
    elif k < arr[mid]:
        n = mid - 1
print(res)'''


# first occurace index of element using binary search
'''arr= [2,3,4,5,7,9,9,9,10,12]
l = 0
k = 9
n = len(arr)
res = 0
while l <= n:
    mid = (l + n) // 2
    if arr[mid] == k: 
        res = arr[mid] 
        n = mid - 1       
    elif k > arr[mid]:
        l = mid + 1
    elif k < arr[mid]:
        n = mid - 1
print(res)'''

#
# if element is found it gives the index or if element i not found then the l is always at the inserted position even though element is not present 
'''arr= [2,3,4,5,7,9,10,12]
l = 0
k = 1
n = len(arr)
t = False
index = float('-inf')
while l <= n:
    mid = (l + n) // 2
    if arr[mid] == k:
        t = True
        print(mid)
        break             
    elif k > arr[mid]:
        l = mid + 1
    elif k < arr[mid]:
        n = mid - 1
if t == False:
    print(l)
    '''
    

'''def first(nums,target):
    l = 0
    n = len(nums) -1 
    res = -1
    if l <= n:
        mid = (l+n)//2
        if nums[mid] == target:
            ress = mid
            n = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            n = mid - 1

    return res

def second(nums,target):
    i  = 0
    j = len(nums) -1
    resf = -1
    while i <= j:
        m = (i+j)//2
        if nums[m] == target:
            resf = m
            i = m + 1
        elif target > nums[m]:
            i = m + 1
        elif target < nums[m]:
            j = m - 1

    return resf

arr= [2,3,4,5,7,9,9,9,10,12]
n =len(arr)-1
print(first(arr,9))
print(second(arr,9))'''



l = [1,2,5,7,10]
mini = 1
k = 3

m = max(l)-1
while mini < m and k > 0:
    prev = l[0]
    for u in l:
        if u - prev >= mini:
            prev = u
            k = k - 1
    if k  <= 0:
        print(u)
    else:
        mini += 1


 