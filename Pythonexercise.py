def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal
def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if b == c:
    return a
  if a == c:
    return b
  if a == b:
    return c
  return a + b + c
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(n):
  if n % 10 >= 5:
    return n + 10 - (n % 10)
  return n - (n % 10)
def close_far(a, b, c):
  cond1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
  cond2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
  return cond1 or cond2
def make_chocolate(small, big, goal):
  maxBig = goal / 5
  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1
def double_char(str):
  result = ''
  for char in str:
    result += char * 2
  return result
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      count_dog += 1
    if str[i:i+3] == 'cat':
      count_cat += 1
  return count_cat == count_dog
def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):]
def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False
def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count
def big_diff(nums):
  return max(nums) - min(nums)
def centered_average(nums):
  sum = 0
  for element in nums:
    sum += element
  return (sum - min(nums) - max(nums)) / (len(nums)-2)
def sum13(nums):
  if len(nums) == 0:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums):
        nums[i+1] = 0
  return sum(nums)
def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)
def has22(nums):
  for i in range(0, len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True
  return False
