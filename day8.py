
#given a number you need to return the sqrt of the number floor value  with linear search
'''
n = 4
for i in range(1,n//2+1):
    if i*i == n:
        print(i)
        break
    elif i*i > n:
        print(i-1)
        break '''
       

#given a number you need to return the sqrt of the number floor value  with binary search
'''n = 32 
i = 0
m = n//2
while i <= m:
    mid = (i+m)//2
    if (mid * mid)  == n:
        print(mid)
        break
    elif (mid * mid) > n:
        m = mid - 1
    elif (mid * mid) < n:
        i = mid + 1  

print(m) # if it is ceil print low(i) if floor print(m)

'''
# given rotated array print index where the inversions has done

#arr = [12,13,14,2,3,4,5,6,7,8,9]
#arr = [34,36,37,39,40,10,14,16,18,20]

'''for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        continue
    else:
        print(i+1)
        break'''


ip = [16,30,50,70,20,1,2,3,5,8,9,10,12,13,14,15]
l = 0
t = 12
r = len(ip)-1
while l < r:
    m = (l + r) // 2
    if ip[m] == t:
        print(m)
        break
    if ip[m] > ip[r] and ip[m]>t:
        l = m + 1
    else:
        r = m
print(l)





# given array [2,3,4,6,3,2,1,5,8,10,1,4,2] print the peak elements

#arr = [8,2,3,4,6,3,2,1,5,8,10,1,4,2,3]
'''arr =[5,2,4,6,7,8,6,5,4,6,7,8,9,10,8,6,5,4,7]
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(arr[i],i)
        break
l = 0
r = len(arr)-1 
while l < r:
    mid = (l+r) // 2
    if (mid == 0 or arr[mid] > arr[mid-1]  and arr[mid] > arr[mid+1] or mid == len(arr) - 1) :
        print(arr[mid]) 
        break
    if arr[l] > arr[mid]:
        r = mid
    else:
        l = mid + 1 '''        





'''import math
    
piles = [30,11,23,4,20]
h = 5
k = 1
t = False
l = 1
r = max(piles)
while l <= r:
    mid = (l+r) // 2 
    s = 0
    for i in piles:     
        s = s + (math.ceil(i/mid))      
        if s > h:
            l = mid + 1
        elif s <= h:
            r = mid - 1
print(l) '''



#l = stalls, miini = distance, cows = no.of cows should be placed, now tell  wheather it is possible or not 
l = [1,2,5,7,10]
mini = 3
cows = 3
i = 0
p = []
p.append(l[0])
k = 0
j = 1
while i < cows-1:
    for u in range(j,len(l)):
        if abs(p[k] - l[u]) >= mini:
            p.append(l[u])
            print(p)
            j = u
            k = k + 1
            break
    i = i + 1    
       
print(p)
if len(p) == cows:
    print(p)
    print("possible")
else:
    print("not possible")


'''l = [1,2,5,7,10]
mini = 1
k = 3

m = max(l)-1
val = []
while mini < m and k > 0:
    prev = l[0]
    for u in l:
        if u - prev >= mini:
            prev = u
            k = k - 1
    if k  <= 0:
        val.append(mini)
    else:
        mini += 1


print(val) '''       




 


       


