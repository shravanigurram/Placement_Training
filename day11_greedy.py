#1]you have two list one isthemeetig starting time and other is meeting ending time count the maximum no.of meeting will happen
#  if the one meeting held at  a time and the other starts only after the ending of previous meeting and make sure 1 hour break between any two meetings
'''def f(x):
    return x[1]

start = [0,3,8,1,5,7,9]
last = [5,6,10,2,6,9,11]

k=[]
i=0
j=0
while i<len(start) and j<len(last):
    k.append([start[i],last[j]])
    i+=1
    j+=1

k.sort(key=f) 
print(k)

c=0
ith=0
val=float('-inf')
for i in k:
    if i[0]>=val:
        val=i[1]+1
        c=c+1
print(c)            
'''

#2] you  are  given input "hippopotamus" reverse the string  keeping vowel with out changing   its  positionn

'''s = "hippopotamus"
s=list(s)
k='aeiou'
print(s)
i=0
j=len(s)-1
print(j)
while i<j  and i < len(s)-1:
    if (s[i] not in k) and (s[j] not in k):
        s[i],s[j]=s[j],s[i]
        i+= 1
        j-= 1
    elif s[i] in k:
        i=i+1
    elif s[j] in k:
        j = j - 1    

print(''.join(s))
'''


#3] you are visiting lirary where the books and prices are given l
# the store says you can pick any k books but the rule is to choose consequence

l = [2,1,6,4,2,3,1,1,4,2,6,7,3]

'''i = 0
j = 4
M = float('-inf')
while i < len(l) and j < len(l):
    s = sum(l[i:j+1])
    if s > M:
        M = s
    i+=1
    j+=1    
print(M)  '''      
    

#or
   
'''l = [2,1,6,4,2,3,1,1,4,2,6,7,3]
s = sum(l[0:5])
M = float('-inf')
if s > M:
    M=s
   
i = 1
j = 5  
while i < len(l) and j < len(l):
    s = (s - l[i-1]) +l[j]
    
    if s > M:
        M = s    
    i+=1
    j+=1    
print(M)'''


#
'''l=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=7
s=0
v=0
maxi=float('-inf')
for i in l:
    if s <k:
        s=s+i
        v=v+1
    else:
        if v > maxi:
            maxi = v

        v = 0
        s=0
        s+=i
        v=v+1
           
print(maxi)
'''

#longest sum whose length is <= k
'''arr=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=7
s=0

maxi=float('-inf')
l=0
r=0
while l<len(arr) and  r<len(arr):
    s =s+arr[r]
    if s <= k:
        maxi=max(maxi,r-l+1)
        
    elif s>k:
        s=s-arr[l]
        l=l+1
    r=r+1

print(maxi)  '''         

            
# return the longest paliandrome substring

'''str="ababba"
st = 0
p=len(str)
count = 0
maxi = 0
for i in range(len(str)):
    #for even length
    l = i
    r = i+1
    while l>=0 and r<len(str) and str[l] == str[r] :
        count = count + 1
        if r-l+1 > maxi:
            maxi = r-l+1
            st = l
        l = l -1
        r = r + 1   
    l = i
    r = i
    while l>=0 and r<len(str) and str[l] == str[r]:
        count = count + 1
        if r-l+1 > maxi:
            maxi = r-l+1
            st = l
        l = l -1
        r = r + 1
                  
print(maxi)

print(str[st:st+maxi])
print(count)'''

#given a string "abcdaecdb" print the length of longest substring without 
'''str ="abcdaecdb"

l = 0
r = 0
c = 0
d = {}
while l < len(str) and r < len(str):

    for i in range(l,r+1):
        if str[i] not in d:
            d[str[i]] = i
            
        else :
            d[str[i]] = l
            get = d.keys(str[i])
            if get > l:
                l = l + get  
            if length > c:
                c = length
            d.
        r = r + 1    

print(c) '''           



def subsets(s,i=0,l=[],final=[]):
        if i == len(s):
            if len(l) !=0:
                final.append(l)
        
            return

        subsets(s,i+1,l+[s[i]],final)    
        subsets(s,i+1,l,final)

        return final
def longestPalindromeSubseq(s):
        lst = list(s)
        val = subsets(lst)
        final = 0
        for i in val:
            #print(i)
            p = ''.join(i)
            if p == p[::-1]:
                final = max(final,len(p))
        return final  

s= "cbbd"
print(longestPalindromeSubseq(s))

                 

        



