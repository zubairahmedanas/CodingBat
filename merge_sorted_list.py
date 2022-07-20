def merge(nums1, m, nums2, n):
    nums3 = []
    nums4 = []
    nums4 = nums1[:-n]
    nums3 = nums4 + nums2

    nums3.sort()

    for i in range(0, len(nums3)):
        nums1[i] = nums3[i]

    return nums1