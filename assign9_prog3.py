a = [35,23,35,20,10,20,40,50]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
 
print(dup_items)