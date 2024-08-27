# n =32
# l =[0] * ( n+1)
# l [-1] = 1  

# while l [0]==0:
#     m =[str(i) for i in l if i != 0]
#     print (' '. join (m ). center(n*5))
#     for i in range (n):
#         l[i] += l[i+1]












n =32 
l =[0] * ( n+1)
l [-1] = 1  
c = n
while l[0] == 0:
    m =[['  ', '$$'][i%2] for i in l if i != 0]
    c -=1
    print ((' '*c)+''. join (m ))
    for i in range (n):
        l[i] += l[i+1]