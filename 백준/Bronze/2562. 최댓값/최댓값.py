import sys

nums = []

for i in range(9):
    nums.append(int(sys.stdin.readline()))

print(max(nums))
print(nums.index(max(nums)) + 1)