# def longest_sub_array(arr):
#     # Check if all elements in the list are negative
#     if all(x < 0 for x in arr):
#         return len(arr)

#     # Initialize variables
#     max_length = 0
#     current_sum = 0
#     start = 0

#     # Iterate through the list and update the current sum and max length
#     for i, x in enumerate(arr):
#         current_sum += x
#         while current_sum <= 0:
#             current_sum -= arr[start]
#             start += 1
#         max_length = max(max_length, i - start + 1)

#     return max_length





def longest_subarray_with_sum_0(arr):
  # Store all prefix sums
  prefix_sums = {}
  prefix_sum = 0
  # Traverse through the array and store prefix sum
  # in a hash map
  for i in range(len(arr)):
    prefix_sum += arr[i]
    # If prefix sum is already present, then subarray
    # from index 0 to i is a valid subarray
    if prefix_sum == 0:
      max_len = i + 1
    # If prefix sum is not present, then store it
    # in the hash map
    elif prefix_sum not in prefix_sums:
      prefix_sums[prefix_sum] = i
    # If prefix sum is present, then update maximum
    # length of subarray with sum 0
    else:
      max_len = max(max_len, i - prefix_sums[prefix_sum])
  return max_len



# arr = [15,-2,2,-8,1,7,10,23]
arr = [2, 2, 1, -3, 4, 3, 1, -8, 6, -2, -1]
print(longest_subarray_with_sum_0(arr))