'''
@summary: Python Intro - References 
'''

# ---------------------------
# Immutable data types numbers, string, tuples
# When assigning one name to another bint=aint and then changing either one of them that changed value will only be referenced by the name used  
# ---------------------------
print "\n--- numbers ---"
aint = 5
bint = aint
print "%s,%s | id %s,%s" % (aint, bint, id(aint), id(bint))  # result 5  -  5
aint = 6
print "%s,%s | id %s,%s" % (aint, bint, id(aint), id(bint))  # result 6  -  5



print "\n--- tuples ---"
atu = (1, 2, 3)
btu = atu
print "%s,%s | id %s,%s" % (atu, btu, id(atu), id(btu))  # (1, 2, 3, 4)  -  (1, 2, 3)
atu = atu + (4,)
print "%s,%s | id %s,%s" % (atu, btu, id(atu), id(btu))  # (1, 2, 3, 4)  -  (1, 2, 3)


# ---------------------------
# Mutable data types list, dictionary, classes etc.
# Changes will be shared between names referencing the same data/values 
# ---------------------------
print "\n--- lists ---"
ali = [1, 2, 3]
bli = ali
print "%s,%s | id %s,%s" % (ali, bli, id(ali), id(bli))  # [1, 2, 3, 4]  -  [1, 2, 3, 4]
ali.append(4)
print "%s,%s | id %s,%s" % (ali, bli, id(ali), id(bli))  # [1, 2, 3, 4]  -  [1, 2, 3, 4]
