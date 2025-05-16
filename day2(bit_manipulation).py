

#  5->101
#    2->10
    

# 15   1111
#1110

#4    100
'''print(5>>2)
print(153*(2**14))'''
#print(5//(2**3))
'''print(178<<13)

print(178*(2**13)'''

#
'''n = 32
if n & 1 == 0:
    print("even")
else:
    print("odd")'''    

#using Xor
'''n = 42
l = n ^ 1
k = bin(l)[2:]
p = k[-1]
print(p)
if  p == 0:
    print("odd")
else:
    print("even") '''

#find sum of xor in a given range
'''def xor_fun(k):
    if k  % 4 == 1:
        return 1
    elif k % 4 == 2:
        return k + 1  
    elif k % 4 == 3:
        return 0  
    else:
        return k 


n = int(input()) 
m = int(input())


p = xor_fun(n-1)
l = xor_fun(m)
print(p^l)'''

'''n = 5
m = 10
s = 0
for i in range(n,m+1):
    s =s ^ i

print(s) '''



'''k = int(input())
i = 0
while 1:
    if 2 ** i == k:
        print("true")
    elif 2** i > k:
        print("false") 
        break 
    i += 1'''  
      
'''
k = int(input())
p = bin(k)[2:]
if p[-1] == 0 or p[-1:-3] == 0 or p[-4] == '''

'''k = int(input())
p = k & (k-1)
if p == 0:
    print("power of 2")
else:
    print("not a power of 2")'''    


'''k = [2,2,3,3,4,4,5,5,6,7,7,8,8]  
for i in range(0,len(k)):
    if k[i] == k[i+1]:
        i+=2
    else:
        print(k[i])   
        break'''

#sliding window
'''p = [2,2,3,3,4,4,6,6,7,7,8] 

i = 0
while i < len(p)-1: #
    if p[i] == p[i+1]:
        i = i+2
    else:
        print(p[i])
        break
else:
    print(p[-1])'''

p = [2,2,3,3,4,6,6,7,7,8,8] 
l = 0
r = len(p)-1


while l <= r:
    mid = (l + r) // 2
    if mid > 0 and p[mid] == p[mid - 1]:
        if (mid - l + 1) % 2 == 0:
            l = mid + 1
        else:
            r = mid - 2
    elif mid < len(p) - 1 and p[mid] == p[mid + 1]:
        if (r - mid + 1) % 2 == 0:
            r = mid - 1
        else:
            l = mid + 2
    else:
        # Found the unique element
        print(p[mid])
        break    
   
1

      

'''k = [1,2,3,4,1,2,3,4,5,6,7,8,4,7]
#k= [1,2,3,2,3,4,5,6,7,8,9]
m = 1
conmax = 1

for i in range(len(k)-1):
    if k[i]+1 == k[i+1]:
        conmax += 1
    else:
        m = max(conmax,m)
        conmax = 1
m = max(conmax,m)        
print(m)'''

#k = "aaabbaaaacccddeeff"
'''k = "abbacbababc"
s = ""
m = 1 
l= []
for i in range(len(k)-1):
    if k[i] == k[i+1]:
        m = m + 1
    else:
        l.append(str(k[i]))
        l.append(str(m))
        
        m = 1

l.append(k[-1])
l.append(str(m))
print(s.join(l))'''


'''k = "abbacbababc"
s = ""
m = 1 

for i in range(len(k)-1):
    if k[i] == k[i+1]:
        m = m + 1
    else:
        s += k[i] + str(m)
        m = 1

s += k[i+1] + str(m)
print(s)'''















    

def qwer(x):
    if x ==1:
        return 3
    if x==2:
        return 1
    return qwer(x-1)+qwer(x-2)+2
print(qwer(5))


