list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
 
diff1= list(set(list1) - set(list2))
diff2=list(set(list2) - set(list1)) 
print(diff1)
print (diff2)