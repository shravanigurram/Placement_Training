#bubble sort code
'''def bubble_sort(l):
    n = len(l)
    for i in range(n):
        flag = True
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                flag = False
         
        if flag == True:
            break
    return l            

  
l = [3,2,6,1,0,9]
print(bubble_sort(l))'''

# given number k you should touch up to k range from in the first and last 
'''def bubble_sort(l,k):
    n = len(l)
    for i in range(k,n-k-1):
        flag = 0
        for j in range(k,n-i-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                flag = 1
        print(l)        
        if flag == 0:
            break
         

    print("final:", l)            

  
l = [67,21,7,4,8,3,78,45]
k = 2
bubble_sort(l,k)'''


# you should sort the array up to kth largest element and stop the process  
'''def bubble_sort(l,k):
    n = len(l)
    for i in range(0,n-1):
        flag = 0
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                flag = 1
        if flag == 0:
            break
        print(l)
        if i == k:
            print("final:", l) 
            return (l[n-k])
        
        

#l = [2,3,6,0,1,9]
l = [4, 0, 8, 22, 9, 6, 1]
#l = [3,8,2,1,4,7,9,3]
print(bubble_sort(l,2))'''

# sort the alphabetic list
'''def bubble_sort(l):
    n = len(l)
    for i in range(n):
        flag = 0
        for j in range(0,n-i-1):
            if ord(l[j]) > ord(l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                flag = 1
        if flag == 0:
            break

    print(l)            

  
l = ['e','a','t','q','s','l']
bubble_sort(l)'''



# sort the list which consists of nested lists or a 2D list on bases of second element in each list 
'''def bubble_sort(l):
    for k in range(len(l)-1):
        flag = 0
        for i in range(len(l)-1-k):
            if l[i][1] > l[i+1][1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                flag = 1
        if flag == 0:
            break

    print(l)            

  
l = [[2,3],[5,1],[1,4],[2,7],[1,3]]
bubble_sort(l)'''


'''def lexiograpic_sort(l):
    for k in range(len(l)-1):
        for i in range(len(l)-1-k):
            for j in range(len(l)-1):
                if l[j][j] > l[j+1][j]:
                    temp = l[i]
                    l[i] = l[i+1]
                    l[i+1] = temp
                    
             
    print(l)           

'''    
'''

def lexiographic_sort(l):
    for k in range(len(l)-1):
        for i in range(len(l)-1-i)
            for j in range(len(l[i])):
                if l[i][j] > l [i+1][j]:
                    l[i],l[i+1] = l[i+1],l[i]
                else:
                    l[i],l[]    

    print(l)            

l = ['bat','bannana']
lexiographic_sort(l)'''


def lexicographic_sort(l):
    n = len(l)
    for k in range(n - 1):
        flag = 0
        for i in range(n - 1 - k):
            if l[i] > l[i + 1]:  # full string comparison
                l[i], l[i + 1] = l[i + 1], l[i]
                flag = 1
        if flag == 0:
            break
    print(l)

#l = ['hello', 'zebra', 'hey', 'zeepty','apple']
l = ['apples','apple','an','ane']
lexicographic_sort(l)


    

#l = [[4,13,12],[8,10,5],[14,8,3]] each row has exactly one prime number now sort the rows in order to get asending order of prime number 
'''
def find_prime(i,j=2):
    if j == int(i ** 0.5) + 1: # to find wheather it is prime or not
        return True
    if i == 0 or i == 1:
        return False
    if i == 2:
        return True
    if i % j == 0:
        return False
    return find_prime(i,j+1) 

def get_prime(lst):
    for i in lst:
        p = find_prime(i)  #pass  element to check wheather it is prime or not 
        if p == True:
            return i
    

def sort_rows_prime(l):
    prime = []
    for i in l:
        # pass each list present in the list
        k = get_prime(i) # get the prime number in the list 
        prime.append(k)  # append the returned prime number to prime
    print(prime) 

    for i in range(len(prime)-1):
        flag = 0
        for j in range(0,len(prime)-i-1):  # sort the prime number lst along with the actual list
            if prime[j] > prime[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                prime[j], prime[j+1] = prime[j+1],prime[j] 
                flag = 1
        if flag == 0:
            break                 
    print(l)                 

l = [[4,13,12],[8,10,5],[14,8,3],[7,9,30]]
#function call
sort_rows_prime(l)'''


# afternoon 


# a string is given from the user you need to return string
# which is sorted in such a way that length of each words places in assending order 

'''s = "An apple a day keeps doctor away"
s = list(s.split())
print(s)
l = []
for i in s:
    l.append(len(i))
print(l)  #Op[2, 5, 1, 3, 5, 6, 4]
for i in range(len(l)-1):
    flag = 0
    for j in range(0,len(l)-1-i):
        if l[j] > l[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
            l[j], l[j+1] = l[j+1],l[j] 
            flag = 1
    if flag == 0:
        break                 
print(' '.join(s)) #OP a An day away apple keeps doctor
'''

#----------------------------------------------------------------
# you are given unsorted array with duplicate elements 

#l = [5,6,3,6,3,5,7,9,3,5,9,5]
'''l = [7,2,6,3,6,7,7,2,2,2]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

freq = list(d.values())
keys = list(d.keys())

print("intial keys:", keys)
print("dictionary", d)

for i in range(len(freq)-1):
    flag = 0
    for j in range(0,len(freq)-1-i):
        if freq[j] > freq[j+1]:
            keys[j], keys[j+1] = keys[j+1], keys[j]
            freq[j], freq[j+1] = freq[j+1],freq[j] 
            flag = 1
    if flag == 0:
        break                 
print("sorted order:", keys)

final = []
for i in range(0,len(keys)):
    final.extend([keys[i]]*freq[i])

print("final sorted array:",final) ''' 
# output   
'''intial keys: [7, 2, 6, 3]
dictionary {7: 3, 2: 4, 6: 2, 3: 1}
sorted order: [3, 6, 7, 2]
final sorted array: [3, 6, 6, 7, 7, 7, 2, 2, 2, 2]'''

#-----------------------------------------------------------------------------------

# bucket sort 
'''
def bucketsort(l):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    n = max(d.values())
    bucket = [[0]] * 10
    print(bucket)
    print(d)
    for keys,values in d.items():
        bucket[values] = [keys]
        if not bucket[values]:
            bucket[values] = bucket[values]+[keys]
    print(bucket)


    final = []
    for i in range(0,len(bucket)):
        if bucket[i] != [0]:
            for j in bucket[i]:
                final.extend(bucket[i] * i)


    print("final sorted array:",final)

l = [5,6,3,6,3,5,7,9,3,5,9,5]
bucketsort(l)'''



a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)

# to elements from second index of 2d list
'''def fun(x):
    return x[-1]
l = [[4,13,12,33],[8,5],[14,8,3],[7,9,30]]
l.sort(key=fun) #[[14, 8, 3], [8, 5], [7, 9, 30], [4, 13, 12, 33]]
print(l)'''

    

'''def fun(x):
    return x[0]
l = [[4,13,12,33],[8,5],[14,8,3],[7,9,30]]
l.sort(key=fun) #[[4, 13, 12, 33], [7, 9, 30], [8, 5], [14, 8, 3]]
print(l)'''


'''def fun(x):
    return x[0]
l = [[4,13,12,33],[8,5],[14,8,3],[7,9,30]]
l.sort(key=fun,reverse = True) #[[14, 8, 3], [8, 5], [7, 9, 30], [4, 13, 12, 33]]
print(l)
'''
'''
def fun(x):
    for i in x:
        for j in range(0, int(i**0.5)+1):
            if '''





