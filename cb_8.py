def merge(nums1, m, nums2, n):
	# while m > 0 and n > 0:
	if nums1[m-1] < nums2[n-1]:
		nums1[m+n-1] = nums2[n-1]
	m = m-1
	n= n-1
	print(nums1) 
		# else:
  #   		pass

nums1=[1,2,3,0,0,0]
m=3
nums2=[4,5,6]
n=3
merge(nums1, m, nums2, n)
