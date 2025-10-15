nums = list(map(int,input("enter numbers:").split()))
for n in nums:
  if n % 2 == 0:
    nums.remove(n)
print(nums)

