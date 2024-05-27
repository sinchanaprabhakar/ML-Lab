def listOp(arr):
  print("List: ",arr)
  #List insert
  num=int(input("Enter a number to insert: "))
  arr.append(num)
  print(arr)
  #List update
  ind=int(input("Enter index to update: "))
  val=int(input("Enter value to update: "))
  if ind>=0 and ind<len(arr):
    arr[ind]=val
  else:
    print("Invalid index")
  print(arr)
  #List delete
  ind=int(input("Enter index to delete: "))
  if ind>=0 and ind<len(arr):
    del arr[ind]
  else:
    print("Invalid index")
  print(arr)
  #List sort
  arr.sort()
  print("Sorted list: ",arr)
  #List search
  key=int(input("Enter key to search: "))
  if key in arr:
    print("Key found")
  else:
    print("Key not found")

def tupleOp(tup):
  print("Tuple: ",tup)
  #tuple search
  key=int(input("Enter key to search: "))
  if key in tup:
    print("Key found")
  else:
    print("Key not found")
  print("Tuple does not support insert, update, delete and sorting operations")

def setOp(setarr):
  print("Set: ",setarr)
  #Set insert
  num=int(input("Enter a number to insert: "))
  setarr.add(num)
  print(setarr)
  #Set update not applicable
  #Set delete
  val=int(input("Enter value to delete: "))
  setarr.remove(val)
  print(setarr)
  #Set sorting not applicable as it sorts automatically
  #Set search
  key=int(input("Enter key to search: "))
  if key in setarr:
    print("Key found")
  else:
    print("Key not found")

def dictionaryOp(dict):
  print("Dictionary: ",dict)
  #Dictionary insert
  key,val=input("Enter a key value pair to insert: ").split()
  dict[key]=int(val)
  print(dict)
  #Dictionary update not applicable
  #Dictionary delete
  key=input("Enter key to delete from dictionary: ")
  if key in dict:
    del dict[key]
  else:
    print("Key not found")
  print(dict)
  #Dictionary search
  key=input("Enter key to search: ")
  if key in dict:
    print("Key found")
  else:
    print("Key not found")

def main():
  arr=[1,2,3,4]
  print("List Operations:")
  listOp(arr)
  tup=(5,6,7,8)
  print("Tuple Operations:")
  tupleOp(tup)
  setarr={9,10,11,12}
  print("Set Operations:")
  setOp(setarr)
  dict={"one":1, "two":2}
  print("Dictionary Operations:")
  dictionaryOp(dict)

#if __name__=="__main__":
main()
