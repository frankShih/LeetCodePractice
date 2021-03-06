class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        
        '''
        # implement comparator solution
        strNums = map(str, nums)    # iterator
        strNums = sorted(strNums, key=LargerNumKey)
        largest_num = ''.join(strNums)
        
        return '0' if largest_num[0] == '0' else largest_num
        '''
        
        length = len(nums)
        nums = list(map(str, nums))

        # bubbleSort
        # for i in range(length):
        #     for j in range(length-i-1):
        #         if nums[j]+nums[j+1] < nums[j+1]+nums[j] :
        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # selection sort, less swap    
        # for i in range(length-1):
        #     maxInd = i
        #     for j in range(i+1, length):
        #         if nums[j]+nums[maxInd] > nums[maxInd]+nums[j]:
        #             maxInd = j
            
        #     nums[i], nums[maxInd] = nums[maxInd], nums[i]
        
        # insertion sort, much less swap    
        for i in range(length):
            ind = i
            temp = nums[ind]
            while ind >0 and temp+nums[ind-1] > nums[ind-1]+temp:
                nums[ind] = nums[ind-1]
                ind-=1
            nums[ind] = temp

            # print(nums)
        
        return str(int("".join(nums)))
        