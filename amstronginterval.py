a1,b1=map(int,input().split())
for num1 in range(a1,b1):
   sum = 0
 
   
   temp = num1
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num1 == sum:
       print(num1)
