
def two_sum_On2(arr, S):
  outputList=[]
  for item in arr:
      for item2 in arr:
          if item!=item2 and item+item2==S:
              outputList.append([item, item2])
  return outputList

def two_sum_On(arr, S):
  outputList=[]
  hashTable = dict()

  for item in arr: 

    diffItem = S - item
    if diffItem in hashTable.keys():
      outputList.append([item, diffItem])

    hashTable[item] = item

  return outputList
  
  
if __name__ == '__main__':
    print(two_sum_On2([3,5,2,-4,8,11],7))
