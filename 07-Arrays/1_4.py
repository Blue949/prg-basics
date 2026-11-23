###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
c = len(arr)
print('Last but one value', arr[c-2])
print('Sum of the first and last value', arr[0]+arr[-1])
middle_value = len(arr) / 2
middle_value = int(middle_value)
print('Middle value',arr[middle_value])
print('All array values separated by a single space ', end="")
a = 0
b = len(arr)
while b > 0:
    print(arr[a], end="")
    print(' ', end="")
    a = a + 1
    b = b - 1
print()
