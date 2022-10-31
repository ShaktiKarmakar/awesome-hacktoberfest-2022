def countSort(arr,k):

	output = [0 for i in range(len(arr))]
	count = [0 for i in range(k)]

	# Store count of each character
	for i in arr:
		count[i] += 1

	for i in range(k):
		count[i] += count[i-1]
  #count[i] now contains actual position of this number in output array

	for i in range(len(arr)-1,-1,-1):
		output[count[arr[i]]-1] = arr[i]
		count[arr[i]] -= 1

	return output

# main
n=int(input("Enter the size of input array."))
k=int(input("Enter the maximum limit value for the array elements."))
arr = []
for i in range(n):
  e=int(input("Enter the array element."))
  arr.append(e)
ans = countSort(arr,k)
print("Sorted array is " , end="")
print(ans)

