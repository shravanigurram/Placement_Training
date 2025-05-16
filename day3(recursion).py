
# 14/05/2025
'''def qwer(x):
    if x ==1:
        return 3
    if x==2:
        return 1
    return qwer(x-1)+qwer(x-2)+2
print(qwer(5))'''

# sum of even in a list using recursion
'''def sum_even(l,i,s):
    if i == len(l):
        return s
    if l[i] % 2 == 0:
        s = s + l[i] 
    return sum_even(l,i+1,s) 


l = [2,5,6,7,8]

print(sum_even(l,0,0))'''

# sum of even in a list using recursion 2
'''def sum_even(x,i):
    if len(x) == i:
        return 0
    if x[i] % 2 == 0:
        return x[i] + sum_even(x,i+1)
    else:
        return sum_even(x,i+1)
a = [2,5,6,7,1,4,3,6]
print(sum_even(a,0))'''

# reverse of a number
'''def reverse(k,re):
    if k == 0:
        return re
    return reverse(k//10, re*10 + k % 10)
       
k = 54227
re = 0
print(reverse(k,re))
'''


'''def primecheck(q,s,j):
    if j == q:
        return s
    if q % j == 0:
        s = s + 1
        return s
    return primecheck(q,s,j+1) 
 
    
#l = [2,4,3,6,7]
l = 61
p = primecheck(l,0,2)
if p == 0:
    print("prime ")
else:
    print("np")    
'''

'''#count of no.of prime numbers in a list
def primecheck(q,s,j):
    if q == 0 or q == 1:
        return 1
    if j == (q//2)+1:
        return s
    if q % j == 0:
        s = s + 1
        return s
    return primecheck(q,s,j+1)   
    
# prime or not 
def prime(l,i,count):
    if i == len(l):
        return count
    w = primecheck(l[i],0,2)
    if w == 0:
        count += 1 
    return prime(l,i+1,count)
       
l = [1,0,2,2,2,2]
print(prime(l,0,0))'''

# afternoon 
'''def find_path(k,q,p):
    if k == 1:
        return True
    if k <  1:
        return False
    
    return find_path(k-q,q,p) or find_path(k-p,q,p)
    

k = 20
q = 3
p = 5
print(find_path(k,q,p))
'''

'''def mini_find_path(k,q,p,c):


    

     
    
    k,q,p,c

k = 20
q = 3
p = 5
v = []

q = []
while k > 1:
    j = k - p'''



def printing_subsets(array,l = [],i=0):
    if i == len(array):
        print(l)
        return l
    
    printing_subsets(array,l+[array[i]],i + 1)
    return printing_subsets(array,l,i+1)

array = [2,3,4]

printing_subsets(array)



 

