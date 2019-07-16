e,y=map(int,input().split())
for j in range(e+1,y):
  
  
   for i in range(2,j):  
       if (j % i) == 0:  
           break  
   else:  
       print(j,end=" ") 
