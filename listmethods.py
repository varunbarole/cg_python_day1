alist = [10,10,10,20,30,40]
alist.append(50)
print("After appending :", alist)
alist.append(50)
alist.append(60)
alist.append(70)
print("After appending :", alist)
#alist.clear()
#print("After clearing :", alist)

getcount = alist.count(10)
print("Count the value :", getcount)

#append : passing one single object
#extend : passing list of tuple
alist.extend([70,80,90])
print("After extending :", alist)

## inserting at specific position
## syntax :  insert( where to insert , what to insert )
alist.insert(0,5)
print("After inserting :", alist)
alist.insert(2,15)
print("After inserting :", alist)

## pop        :  pop by default will remove the last element
## pop(index) :  will remove the value at that index
getvalue = alist.pop()
print("Removed element is :", getvalue )
print("After pop opertion :", alist)

alist.pop(2)
alist.pop(3)
alist.pop(5)
print("After pop opertion :", alist)

# display in reverse order
alist = [56,43,23,54,23,7,2,6,7,71,9]
alist.reverse()
print("Elements in reverse order :", alist)

# display in sorted order
alist = [56,43,23,54,23,7,2,6,7,71,9]
alist.sort()
print("Elements in reverse order :", alist)


alist = [56,43,23,54,23,7,2,6,7,71,9]
alist.sort(reverse = True)
print("Elements in reverse order :", alist)







