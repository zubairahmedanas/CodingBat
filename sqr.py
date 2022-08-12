
def sqr(arr):
	for i in range(len(arr)):
		if i%2 == 0:
			arr[i] = arr[i]*arr[i]

	print(arr)



sqr([9, -2, -9, 11, 56, -12, -3])