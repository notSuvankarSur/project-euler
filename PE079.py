def check(element, number):
    index1 = str(number).index(str(element))
    index2 = nums.index(element)
    for j in range(index1):
        if int(str(number)[j]) not in nums[:index2]:
            nums.remove(element)
            nums.append(element)
            return False
    for j in range(index1 + 1, 3):
        if int(str(number)[j]) not in nums[index2 + 1:len(nums)]:
            nums.remove(element)
            nums.append(element)
            return False
    return True


fptr = open('p079_keylog.txt')
keys_str = fptr.read().split()
keys = []
for item in keys_str:
    keys.append(int(item))
del keys_str
nums = []
for key in keys:
    for num in str(key):
        if int(num) not in nums:
            nums.append(int(num))
passcode = ''
i = 0
while i < len(nums):
    flag = True
    for key in keys:
        if str(nums[i]) in str(key) and not check(nums[i], key):
            flag = False
            break
    if flag:
        passcode += str(nums[i])
        i += 1

print(nums)
print(passcode)
