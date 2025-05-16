# pen brought on a day for x rupees and sold on another day but not on same day


'''def find(l):
    b = float('inf')
    profit = float('-inf')
    for i in range(len(l)):
        if l[i] < b:
            b = l[i]
        else:
            if l[i] - b > profit:
                profit = l[i] - b
    print(profit)


        
l=[4,5,6,2,3,14,5,6,4]
find(l)'''



#  to find sum of rows which is multipied every indiviudual value with corresponding index value in k
'''l = [[0,1,1,0,1],[1,1,0,0,1],[0,0,0,1,1],[0,1,0,0,0]]

k = [8,7,6,5,2]
o = []
for i in range(len(l)):
    s = 0
    for j in range(len(l[i])):
        if l[i][j] == 1:
            s = s + (l[i][j]*k[j])
    o.append(s)   
print(o)   '''  


# a rat is set in grid (row,colunms) path you need find many paths exists 
# and rats has to choose to either go to right or left from current position
'''def max_paths_rat_have(l,i=0,j=0,n=5):
    if i == n or j == n or l[i][j] == 0:
        return  0
    if i== n-1 and j == n-1 and l[i][j] == 1 :
        return 1
    
    return max_paths_rat_have(l,i,j+1,n) + max_paths_rat_have(l,i+1,j,n)
   
l = [[1,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]
print(max_paths_rat_have(l))
'''

# find distinck number of islands present in a matrix
'''def distinct_islands(l,i,j,n=5):
    if i == n or j == n or i < 0 or j < 0 or  l[i][j] == 0 or l[i][j] == 2 :
        return  0
    
    if l[i][j] == 1:
        l[i][j] = 2
        
    distinct_islands(l,i-1,j,n)
    distinct_islands(l,i,j-1,n)
    distinct_islands(l,i+1,j,n)
    distinct_islands(l,i,j+1,n) 

l = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,1]]
for i in l:
    print(i)
c = 0    
for i in range(5):
    for j in range(5):
        if l[i][j] == 1:
            distinct_islands(l,i,j,5)
            c = c+1
print(c) 
for i in l:
    print(i) '''          

#2] 1 is tree 0 is land. one tree catched fire then find how many no.of trees remains unburned in the final
# how it works if one tree catched fire ultimatly the treess connected in left right up,down will catch the fire.
# the trees do not have connected to recursive trees will remailed unfired 

# find the conneccted trees for the given tree locations. then connected trees will become 2 
'''def find_max_paths_tree(l,i,j,n=5):
    if i == n or j == n or i < 0 or j < 0 or  l[i][j] == 0 or l[i][j] == 2 :
        return  0
    
    if l[i][j] == 1:
        l[i][j] = 2
        
    find_max_paths_tree(l,i-1,j,n)
    find_max_paths_tree(l,i,j-1,n)
    find_max_paths_tree(l,i+1,j,n)
    find_max_paths_tree(l,i,j+1,n) 

l = [[1,0,0,1,1,1],[1,1,1,0,0,0],[0,0,1,1,1,1],[1,1,1,0,0,0],[0,0,1,0,0,1],[1,0,0,1,0,0]]
for i in l:
    print(i)
print("")    
n = 3
m = 6
# pass the location    
if l[n-1][m-1] == 1:
    find_max_paths_tree(l,n-1,m-1,6)   
             
c = 0 
for i in l:
    print(i)
    for j in i:
        if j == 1:
            c = c+1

print(c)

#output
[1, 0, 0, 1, 1, 1]
[1, 1, 1, 0, 0, 0]
[0, 0, 1, 1, 1, 1]
[1, 1, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 1]
[1, 0, 0, 1, 0, 0]

[2, 0, 0, 2, 2, 2]
[2, 2, 2, 0, 0, 0]
[0, 0, 2, 2, 2, 2]
[2, 2, 2, 0, 0, 0]
[0, 0, 2, 0, 0, 1]
[1, 0, 0, 1, 0, 0]
3

'''




# you have a box which have n rows and n columns and given a location(2,3). 
# there will be another list [] which has location that frog should not jump [(2,1),(4,1),(5,2),(3,5)]


'''def find_max_paths_frog(i,j,huddle,n):
    if i == n or j == n or (i+1,j+1) in huddle:
        return  0
    if i== n-1 and j == n-1:
        return 1
    return find_max_paths_frog(i,j+1,huddle,n) + find_max_paths_frog(i+1,j,huddle,n)
   

f_p= (2,3)
huddle = [(2,1),(4,1),(5,2),(3,5)]
      
print(find_max_paths_frog(1,2,huddle,5))'''



# input is 3 output is binary repressentation up to from 0 to 3
# input is 3 ouput should be 
# 0 0 
# 0 1
# 1 0 
# 1 1 

'''import math
def allbinary(a,n,s=''):
    if len(s) == n:
        if int(s,2) <= a:
            print("hi")
            print(s) 
            return 
        else:
            return
         
    allbinary(a,n,s+'0')
    all(a,n,s+'1')

a = 14
n = int(math.log(a,2)) + 1
allbinary(a,n)'''


# given a number and you need to print all the valid paranthesis exists '()' for given range
'''def allpara(a,s='',i=0,j=0):
    if  len(s) == a*2:           
        print(s)
     
    if i < a:
        allpara(a,s+'(',i+1,j)
    if j < i:
        allpara(a,s+')',i,j+1)

a = 3
s=''
allpara(a,s)'''



# 16 may 2025 exam
# tower of hanoi
'''
def tower_of_hanoi(n,source,destination,auxilary):
    if n == 0:
        
        return
    if n == 1:
        print(f'disk 1 moves from {source} to {destination}')  
        return

    tower_of_hanoi(n-1,source,auxilary,destination)   
    print(f'disk {n} moves from {source} to {destination}')
    tower_of_hanoi(n-1,auxilary,destination,source)

n = 3
tower_of_hanoi(n,'A','c','B') '''


#sum of subset value == k return true else return false
'''def subset_sum(l,k,i=0):
    if k == 0:
        return True
    if i == len(l):
        return False
    return subset_sum(l,k-l[i],i+1) or subset_sum(l,k,i+1) 
l = [1,2,3,5]
k = 7
print(subset_sum(l,k))'''



