#1] you will given list of elements [2,31,4,2,3,1] intially a car doesn't have petrol
#  you can fill by exchanging what you have previously with the new petrol level 
# if you have currently and the pertol in the bunk is also zero you can not move further and it is not possible 

#l = [2,2,1,0,1,2,0]
#l = [2,2,1,0,1,3,0]
#l = [3,2,1,0,4]
'''l = [2,3,1,0,1,3,1]
s = 0
t = False
for i in range(len(l)):
    if l[i] == 0 and s == 0:
        t = False 
        break
    elif l[i] > s:
        s = l[i]
        #print(l[i],"->",s)
        t = True
        s = s - 1
        #print(s)
    elif l[i] <= s:
        s = s - 1
        t = True    
        #print(s)
    

if t == True:
    print("possible")
else:
    print("impossible") '''   



'''l = [5,10,5,10,5,20,5,10,5]
five = 0
ten = 0
t = True
for i in range(len(l)):
    if l[i] == 5:
        five += 1
    elif l[i] == 10:
        if five > 0:
            five -= 1 
        else:
            t = False 
        ten += 1              
    elif l[i] == 20:
        if five>= 3:
            five -= 3
        elif five >= 1 and ten >= 1:
            five -= 1
            ten -= 1 
        else:
            t = False
if t == True:
    print("True ")
else:
    print("False") '''                   

# to find shortest path 
'''l = [4,3,7,1,6,2]
l.sort()
s = 0
for i in range(len(l)):
    s = s + l[i]
print (s//len(l))'''
    
        
# you are given 2 lists people = [1,6,2,3,4,5], bundle = [4,2,3,1,1,2] these startup company and bundle of money
#the government should give money from the bundle now people can money if the people requirment.
# you need to give any bundle in any order but the one who is asking for a number they should get >= their requirements but not less.
# one bundle should be given to one person only.


'''people = [1,6,2,3,4,5]
bundle = [4,2,3,1,1,6]'''
'''people = [1,2,3,4,5]
bundle = [2,3,4,5,6]'''

'''people = [1,2]
bundle = [1,2,3]
people.sort(reverse=True)
bundle.sort(reverse = True)
print(people)
print(bundle)

count = 0
for i in range(len(people)):
    for j in bundle:
        if people[i] == j:
            count += 1
            bundle.remove(j)
            #people.remove(i)
        else:
            p = max(bundle)
            if people[i] < p:
                count = count + 1
                bundle.remove(p)          
            
            

print(bundle)          
print(count)'''



'''def fun(x,pre):
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
    for i in range(pre):
        while ((val + incre) * (val + incre)) <= x:
            val += incre
        incre = incre // 10
    return round(val,pre)    
    
x = 50
pre = 3
print(fun(x,pre))'''
'''a = list(map(int,input().split()))
b = list()'''


'''l = [2,1,6,4,2,3,1,1,4,2,6,7,3]



i = 0
j = 4
M = float('-inf')
while i < len(l) and j < len(l):
    s = sum(l[i:j+1])
    if s > M:
        M = s
print(M)  '''

print("hi")