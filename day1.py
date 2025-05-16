# using in and not in using in list,string,tuples have O(n) as time complexity
# but using with dictionary and set have O(1) as it time complexity
#                                     1  2  3  4  5  6
# in c we can take a hash table like [0][0][0][0][0][0] like this if we have [2,4,1,1,3,6] it just check directly value a sindex and write 1 if it is 0 and add it in to a new list else it pass the element 

'''
k =  int(input())
p = 0
for j in range(2,k):
    if j * j <  k ** 0.5:
        if k % j ==0:
            p+=1
            break
if p > 0:
    print("not a prime")    
else:
    print("prime")        
'''
'''a=178
b=14
print(a<<b)   '''


'''k = [8,2,3,4,3,3,4,5,6,7,9,2,4]
p=[]
for i in k:    #O(n**2)
    if i not in p: 
        p.append(i)

print(p) '''
# sum of number in a given range

'''n = 10
p = n * (( n + 1) // 2)
print(p)
'''

# to find unique element
'''lst = [2,3,4,3,2,5,5]

d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

#k = min(d,key= d.get)   
#print(k) 

print(d)
for key,value in d.items():
    if value == 1:
        print(key)

s = 0
for i in lst:
    s = s ^ i
print(s)  '''         


'''a = 5 
b = a + 1
print()

'''

k = [2,3,4,1,2,3,4,1,2,3,4,5,6,7,8,4,7]

m = 1
conmax = 1

for i in range(0,len(k)-1):
    if k[i] - k[i-1] == 1:
        conmax += 1
    else:
        m = max(conmax,m)
        conmax = 1

    
              

print(m)