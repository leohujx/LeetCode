# coding:utf-8


# 493. Reverse Pairs

# https://leetcode.com/problems/reverse-pairs/description/

'''
这是个很不错的题目,不会做- -
大致上有三种做法,从 https://leetcode.com/problems/reverse-pairs/solution/ 学习而来
这里大致就说两种方法(在原文中是后两种)

第一种:利用树状数组,边插入边查询,插入的时候用二分,找的是第一个>=目标数的位置
需要两个数组,一个是题中给的数组num,另外一个是原数组的拷贝num_cp,并且将其进行从小到大的排序
然后设一个self.rp[len(num)+1]的数组来作为树状数组的存储空间
还有确定树状数组查询和更新的顺序,一般来说是向下查询,向上更新.
对于这个题目来说,因为要求比它大的,那么我们需要向上查询,向下更新.
首先循环num数组,
第一步:查询(query),它的参数是index和len(num),也就是下标以及数组长度,
那么下标为 self.binaryySearch(2*num[i]+1, num_cp),也就是说求出num[i]*2+1这个数在该序列的有序状态中的位置p,
即比它小的数有p个.此时向上统计,看比这个数大的数有多少(已经插入的,即在这个数的前面),直到len(num)

第二部:更新(update), 它的参数是index和val,即下标和某个值,下标为self.binarySearch(num[i], num_cp),也就是求出num[i]在
这个数组中的有序状态中的位置p,此时再向下更新,更新到每个位置比插入的数小的有多少个.
'''

class Solution(object):
    def binarySearch(self,val, nums):   # 找到第一个 >= 它的位置
        nlen = len(nums)
        l = 0
        r = nlen
        while l < r:
            mid = (l+r)>>1
            if nums[mid] == val:
                return mid
            if nums[mid] < val:
                l = mid+1
            else:
                r = mid
        return l

    def lowbit(self, val):
        return val & (-val)

    def update(self, index, val):  # 向下更新
        while index > 0:
            self.rp[index] += val
            index -= self.lowbit(index)

    def query(self, index, nlen):   # 向上搜索
        res = 0
        while index <= nlen:
            res += self.rp[index]
            index += self.lowbit(index)
        return res

    def reversePairs(self, nums):
        nlen = len(nums)
        self.rp = [0 for _ in range(nlen+3)]
        num_cp = nums[:]
        num_cp.sort()
        res = 0
        for i in range(0, nlen):
            res += self.query(self.binarySearch(2*nums[i]+1, num_cp)+1, nlen)
            self.update(self.binarySearch(nums[i], num_cp)+1, 1)

        return res

s = Solution()
res = s.reversePairs([-5,-5])

print(res)



'''
第二种思路是利用归并排序,因为我们知道在归并排序中,是将所有的数一直二分到只有一个数为止,然后再一一合并,
那么在这个过程中,在合并之前,数组的相对顺序是不变的,所以我们可以在这个点上进行计算
'''

'''
class Solution{
public:
	void merge(vector<int>& nums, int start, int mid, int end){
		int l = start;
		int tmp[int(nums.size())+5];
		int i = start,j = mid+1;
		int p = 0;
		while(i <= mid && j <= end){
			if(nums[i] <= nums[j]){
				tmp[p++] = nums[i++];
			}else{
				tmp[p++] = nums[j++];
			}
		}
		while(i <= mid){
			tmp[p++] = nums[i++];
		}
		while(j <= end){
			tmp[p++] = nums[j++];
		}
		for(int i=0;i<p;i++){
			nums[i+start] = tmp[i];
		}
	}
	int mergesort_and_count(vector<int>& nums, int start, int end){
		if(start < end){
			int mid = (start+end)>>1;
			int ct = mergesort_and_count(nums, start, mid) + mergesort_and_count(nums, mid+1, end);
			int j = mid+1;
			for(int i=start;i<=mid;i++){    //在合并之前统计
				while(j <= end && nums[i] > nums[j] * 2ll){ //因为是相对有序的,所以用while统计一遍即可
					j++;
				}
				ct += (j-(mid+1));
			}
			merge(nums, start, mid, end);
			return ct;
		}else{
			return 0;
		}
	}
	int reversePairs(vector<int>& nums)
	{
	    return mergesort_and_count(nums, 0, nums.size() - 1);
	}
};
'''