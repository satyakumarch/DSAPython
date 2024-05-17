# 217
# Given an interger array nums return true if any apperaRS at least 
# twice in the array and return false if every elememt is distince

# input num2=[1,2,3,1]
# output=True

# input:nums=[1,2,3,4]
# output:=False

# input:nums=[1,1,1,3,3,4,3,2,4,2]
# output:true
 class Solution:
     def containDuplicate(self,nums:List[int])->bool:
         for n in nums:
             if n in hashset:
                 hashset.add(n)
                 return False
