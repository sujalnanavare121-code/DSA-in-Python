# Python program to insert given element at the beginning 

# 1) Built in Module

# arr = [10,20,30,40]
# element = 50

# print("Array Before Insertion")
# for i in range (len(arr)):
#     print(arr[i], end=" ")

# arr.insert(0, 50)

# print("\nArray After insertion")
# for i in range (len(arr)):
#     print(arr[i], end=" ")

# 2) Custom Module

# arr = [10,20,30,40,0]
# n = 4
# element = 50

# print("Array before insertion")
# for i in range (n):
#     print(arr[i], end=" ")

# # Shift all elements to the right
# for i in range((n-1), -1, -1):
#     arr[i+1] = arr[i]    # Most Important

# arr[0] = element


# print("\nArray After Insertion")
# for i in range (n+1):
#     print(arr[i], end=" ")


# Python program to insert given element at a given position

# 1) Built in Function

arr = [10,20,30,40,50]
pos = 3
element = 25

print("Array Before Insertion")
print(arr)

arr.insert(pos-1,element)