
import heapq

def two_sum_On2(arr, S):
  # naive solution having quadratic complexity O(n^2)
  outputList=[]
  for item in arr:
      for item2 in arr:
          if item!=item2 and item+item2==S:
              outputList.append([item, item2])
  return outputList

def two_sum_Onlog2n(arr, S):
  # average solution having logarithmic complexity O(nlogn + nlogn)
  # uses a binary search tree to represent arr, then for each item of arr, we search for S minus item within bst in O(logn) time
  outputList=[]
  # https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
  heapq.heapify(arr) # inplace operation, at worst O(nlogn), from now on arr is a heap
  for item in arr:
    if S-item in arr:
         outputList.append([item, S-item])

  return outputList

def two_sum_On(arr, S):
  # best solution having linear complexity O(n)
  # uses a dictionary to store elements of arr as key, val pair
  # we iterate over all items, and if S minus item is present in the dictionary, insert it into output list
  outputList=[]
  hashTable = dict()
  for item in arr: 
    diffItem = S - item
    if diffItem in hashTable.keys():  # searching a dictionary has O(1) time complexity
      outputList.append([item, diffItem])
    hashTable[item] = item
  return outputList
  
def two_sum_On_worst_space(arr, S):
   # constraint: 0 < arr[i] < M = 10**6 for any i
   # this also has O(n) time complexity but space complexity of O(M) where M >> n
   # additional O(M) https://stackoverflow.com/questions/55896618/python-list-declaration-without-initialization
   # https://stackoverflow.com/questions/50198421/complexity-of-initializing-a-list
   auxillaryList = [0] * 10**6 
   outputList = []
   for item in arr:
      auxillaryList[item] = 1
   for item in arr:
      if S>item and auxillaryList[S-item]==1:
          outputList.append([item, S-item])
   return outputList


# A recursive solution for subset sum problem
# Returns true if there is a subset 
# of set[] with sun equal to given sum

# https://www.interviewbit.com/blog/subset-sum-problem/
def isSubsetSum(set, n, sum) :
 
    # Base Cases
    if (sum == 0) :
        return True
    if (n == 0 and sum != 0) :
        return False
   
    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum) :
        return isSubsetSum(set, n - 1, sum);
   
    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element   
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
  
if __name__ == '__main__':
    print(two_sum_On2([3,5,2,-4,8,11],7))

    #     set = [3, 34, 4, 12, 5, 2]
    #     sum = 9
    #     n = len(set)
    #     if (isSubsetSum(set, n, sum) == True) :
    #         print("Found a subset with given sum")
    #     else :
    #         print("No subset with given sum")
