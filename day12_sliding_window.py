#afternoon
# find longest cosecutive one which 
#leetcode 1004
'''a = [1,1,0,1,0,0,1,1,1,1,0]

l=0
r=0
zero=0
maxi=0
k=2

for r in  range(len(a)):
    if a[r] == 0:
        zero+=1
    if zero>k:
        if a[l]==0:
            zero-=1
        l=l+1    
    if zero <= k:
        maxi=max(maxi,r-l+1)
print(maxi)   '''             

#to get the subarray which has 2 unique elements
#leetcode904


'''def totalFruit(fruits):
        if len(set(fruits)) <= 2:
            return len(fruits)
        d = {}
        l =0 
        maxi=0
        for i in range(len(fruits)):
            if fruits[i] not in d:
                d[fruits[i]] = 1    
            else:
                d[fruits[i]] +=1

            if len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]]== 0:
                    del d[fruits[l]]
                l = l + 1
            if len(d)<=2:
                
                maxi=max(maxi,i-l+1)    
        return maxi


l = []
'''


#given two array start=[900,945,1110,1230,1235,1300,1340,1700] end=[930,1130,1120,1245,1250,1415,1400,1730]
#maximum how many doctors required to check all the paitents

start=[900,945,1110,1230,1235,1300,1340,1700]
end=[930,1130,1120,1245,1250,1415,1400,1730]
k = start+end

maxi=0
l = 0
r = 0
doct = 0
doct2 = 0
doc = 0
merge = []


while l < len(start) and r < len(end):
    if start[l] < end[r]:
        merge.append(start[l])
        l = l + 1
    else:
        merge.append(end[r]) 
        doc +=1
        r = r + 1

while l < len(start):
    
    merge.append(start[l])
    l = l + 1


while r < len(end):
    
    merge.append(end[r])
    
    r = r + 1

print(doc)    


