#2
nums = [3, 45, 32, 5, 7, 8, 4, 44, 5, 90, 17]


def mean_of_n(numbers):
     return sum(numbers) / len(numbers)


def max_of_n(numbers):
   return max(numbers)


def min_of_n(numbers):
   return min(numbers)

mean_value = mean_of_n(nums)
max_value = max_of_n(nums)
min_value = min_of_n(nums)

print(f"평균값은 {mean_value:.1f}")
print(f"최대값은 {max_value}")
print(f"최소값은 {min_value}")
