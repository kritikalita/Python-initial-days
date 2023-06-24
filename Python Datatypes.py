list

declaring list
l=[]
l1=list()

#initialization & declaration
n=["yash",2,"yay"]

#for addition of values to list append is used
l.append("eat")
l.append("eat")
l.append("eat")
l.append("bat")
l.append("cat")
l.append("apple")
l1.append(2)
l1.append(4)
l1.append(7)
l1.append(1)
print(l,l1)
print(len(l1))

#sorting ascending
l1.sort()
print(l1)
#by default it will sort in ascending, descending
l1.sort(reverse=True)
print(l1)

#printing elements in list in lexographical manner
l.sort()
print(l)
l.reverse()
print(l)

#removes last element from list on basis of indexing
l.pop()
print(l)
l.pop(0)
print(l)

#counts no of times an element is in the list
a=l.count("eat")
print(a)

#to find index by element's name
g=l.index("bat")
print(g)

#if there are multiple occurances of the value we are trying to find then it will return index of first matching value
g=l.index("eat")
print(g)

#removing on basis of values
l.remove("cat")
print(l)


#create a list of names of the guys i met till now
#also maintain one list to store their ages and sort the names in reverse lexographical order
#print no of ex i have and remove 2 most hated guys from the list
list1=["Sebastian","Ali","Surajit","Fardin","Rhythm","Sohail","Manik","Rajan","Aditya","Prateek","Deepak","Nilesh","Yash","Anubhav"]
list2=[14,17,18,16,19,26,23,17,17,18,23,36,24,25]

list1.sort(reverse=True)
print(list1)

list1.remove("Nilesh")
list1.remove("Rhythm")
print(list1)
g=len(list1)
print(g)

list1.pop(4)
list1.pop(8)
print(list1)
