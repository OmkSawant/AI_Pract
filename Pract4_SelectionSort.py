def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        # Swap the found minimum element with the first element
        array[step], array[min_idx] = array[min_idx], array[step]

# Take input from user
data = []

# Ask for number of elements
size = int(input("Enter the number of elements: "))

# Take array elements as input
print("Enter the elements:")
for _ in range(size):
    element = int(input())
    data.append(element)

# Call the selectionSort function
selectionSort(data, size)

# Print the sorted array
print('Sorted Array in Ascending Order:')
print(data)


# OUTPUT--->
# Enter the number of elements: 5
# Enter the elements:
# 0
# 2
# 45
# 11
# 9
# Sorted Array in Ascending Order:
# [0, 2, 9, 11, 45]
