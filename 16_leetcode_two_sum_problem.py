n = int(input("How many numbers? "))

nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

target = int(input("Enter target: "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Indices are:", [i, j])
            break