#THIS PROGRAM IS IMPORT A LIST CLASS AND SHOWING ITS WORKING...
import Making_a_List,sys
List=Making_a_List.MyList()
print(sys.getsizeof(List))
print(len(List))
List.append(12)
print(len(List))
List.append("Hello")
print(len(List))
List.append(1)
print(len(List))
print(List)
print(List[0])
print(List[3])
print(List.find("Hello"))
#print(List.find(0))
List.find(12)

List.pop()
List.pop()
List.pop()
List.pop()
print(List)
#List.clear()
#print(List)
#List.clear()
List.append(0.4)
List.append("Ramesh")
List.append(True)
List.append(False)
print(List)

List.find(True)


List.insert(1,21)
List.insert(5,19)
print(len(List))
print(sys.getsizeof(List))
print(List)
del List[0]
print(List)
del List[2]
print(List)
del List[1]
print(List)
#del List[5]
List.remove(110)
List.remove(0)
print(List)

List.clear()
print(List)
List.append(12)
List.append(0)
List.append(1)
List.append(-2)
List.append(5)
List.append(2)
print(List)
print(List.count(2))
List.sort()
print(List)
print(List.count(2))
print(List.count("Hello"))
print(sys.getsizeof(List))


List1=[1,32,14,53,11]
print(List1)
List1.extend([1,"Hello",-1])
print(List1)
print(List1.count("Namaste"))
List.extend([1,2,3])
List1.remove("Hello")
print(List)
List.extend([1,2,3,"hello"])
print(List)
print(List[-1])
print(List[-14])
List.remove("hello")
print(sys.getsizeof(List))