
## dictionary methods
adict = {"chap1":10 ,"chap2":20 ,"chap3":30,"chap1":1000,1:2}

print(adict)

print("Only keys :", adict.keys())

print("Only values:", adict.values())

print("All Items  :", adict.items())

bdict = {"chap4":40}

#print(adict + bdict )
#combining dictionaries

adict.update(bdict)

print("After joining :", adict)

