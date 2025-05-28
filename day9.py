#given a 2d matrix you need to search a given element 

'''def binarysearch(a,search):
    l= 0
    r = len(a)-1
    while l <= r:
        m = (l+r)/2
        if a[m] == search:
            return 1
        elif a[m] < search:
            l = m + 1
        elif a[m] > search:
            r = m -1
    return 0            
        
    
a=[[2,8,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
search = 23
for i in a:
    f = 1
    if a[0] <= search and a[-1] >= search:
        if binarysearch(a,search):
            f = 0
            print("found")
if f == 1:
    print("not found")            '''


'''def binary_search(a,search,n,m):
    l = 0
    r = (n*m)-1
    while l <= r:
        mid = (l+r)//2
        if a[mid//m][mid%m] == search:
            return "found"
        elif a[mid//m][mid%m] < search:
            l = mid + 1
        elif a[mid//m][mid%m] > search:
            r = mid -1
    return "not found"            


a=[[2,8,7,8,10],[9,15,20,21,22],[23,26,35,36,37],[38,39,42,43,44]]
search = 5
n = 4
m =5
print(binary_search(a,search,n,m))'''








'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.sort()
capacity = 2
cap = capacity
days = 1  # Start with day 1

for i in l:
    if i > capacity:
        print("not possible")
        break
    elif i > cap:
        # Not enough space, start a new day
        days += 1
        cap = capacity - i
    else:
        cap -= i
else:
    print(days)'''



# given 5 x 4 ma

'''l = [2,7,11,15]
t = 9
p1 = 0
p2 = len(l)-1
while p1 < p2:
    if l[p1] + l[p2] == t:
        print(l[p1],l[p2])
        break
    elif l[p1] + l[p2] > t:
        p2 = p2 - 1
    elif [p1] + l[p2] < t:
        p1 = p1 + 1'''

'''
n = len(nums)
        nums.sort()
        r = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t < 0:
                    left += 1
                elif t > 0:
                    right -= 1
                else:
                    r.append([nums[i], nums[left], nums[right]]) 
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


                    
                
    
        return r                              



'''
              



'''
E = 6 #int(input())
N = 2 #int(input())
val = [1,2] #list(map(int,input().split()))

count = 0
i = 0
while i < 2:
    if E == 0:
        print("count") 
        break
    else:
        for i in val:
            E = E - i
            count += 1
    i = i + 1
else:
    print(-1)            



    '''


def fun(x,pre):
    l = 1
    r = x // 2
    t =False
    val = 0
    while l <= r:
        mid = (l+r) // 2
        if mid * mid == x:
            return round(mid,pre)     
        elif mid * mid > x:
            r = mid - 1
        elif mid * mid < x:
            l = mid + 1
    val = r
    incre = 0.1
    for _ in range(pre):
        while ((val + incre) * (val + incre)) <= x:
            val += incre
        incre = incre / 10
    return round(val,pre)    
    
x = 50
pre = 3
print(fun(x,pre))



 




     
     

         
 




