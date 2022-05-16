
def two_sum(arr, S):
  outputList=[]
  for item in arr:
      for item2 in arr:
          if item!=item2 and item+item2==S:
              outputList.append(item, item2)
  return outputList
  
if __name__ == '__main__':
    print(two_sum([3,5,2-4,8,11],7))
