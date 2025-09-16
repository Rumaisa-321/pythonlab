num = int(input("enter a number:"))
temp=num
power=len(str(num))
armstrong_sum=0
while temp>0:
   digit=temp%10
   armstrong_sum+=digit**power
   temp//=10
   if num==armstrong_sum:
      print(num,"is an  armstrong number:")
   else:
      print(num,"is not an armstrong number:")
