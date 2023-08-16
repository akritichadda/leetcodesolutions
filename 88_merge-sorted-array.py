"""
Easiest way to think of this question is like a merge sort. 
If there was no restriction to update nums1 in place, you can take a new array and initialise it with the smaller element from nums1 or nums2 and continue.

However, since this needs to be done in place:
1) 3 pointer solution?
    > one pointer keeps track of nums1
    > one pointer keeps track of nums2
    > one pointer keeps track of the number in nums1 that needs to be swapped with a 0 

2) The above is a complicated solution. Now think of it as a descending solution from the end
    > since 0s have not been filled, we can start filling in reverse and will not have to keep track of extra elements
    > while nums2 has not been filled, keep comparing elements in nums1 and nums 2, fill larger element at the end of nums1
    > check if pointer in m1 > 0 or not

"""
def merge(nums1, m, nums2, n):
    
    if m == 0:
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
        return
    if n == 0:
        return

    m1 = m-1
    m2 = m+n-1
    n1 = n-1

    while n1 >= 0:
        if m1 >= 0 and nums1[m1] > nums2[n1]:
            nums1[m2] = nums1[m1]
            m1 -= 1
        else:
            nums1[m2] = nums2[n1]
            n1 -= 1
        m2 -= 1

    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print(nums1)

