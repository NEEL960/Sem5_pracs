# from bplustree import BPlusTree
# import time
# tree = BPlusTree('/Users/neelgabani/Downloads/PRACS:b.db', order=50)
# for i in range(1000):
#     data = (2*i).to_bytes(10, 'big')
#     tree[i] = data
# data = int(input("Enter key : "))
# start_time = time.time()
# byte_data = tree.get(data)
# end_time = time.time()
# int_data = int.from_bytes(byte_data, 'big')
# print("Value : ", int_data)
# print("Time taken : ", (end_time-start_time)*1000, " ms")

# ----------------------------------------------------------------------------------------------------------------------------
from bplustree import BPlusTree
import time
tree = BPlusTree('D:/b1.db', order=50)
for i in range(1000):
    data = (2*i).to_bytes(10, 'big')
    tree[i] = data
try:
    data = int(input("Enter key : "))
    start_time = time.time()
    byte_data = tree.get(data)
    end_time = time.time()
    int_data = int.from_bytes(byte_data, 'big')
    print("Value : ", int_data)
    print("Time taken : ", (end_time-start_time)*1000, " ms")
except:
    print("Element not found")

# ----------------------------------------------------------------------------------------------------------------------------
# menu driven 
from bplustree import BPlusTree
import time
bptree = BPlusTree('/Users/neelgabani/Downloads/PRACS:b.db',order = 3)
while True:
    choice = int(input("Enter\n1.Insert Value in bptree\n2.Search element in bptree\n3.Print bptree\n4.Delete an element\n0.Exit:\n"))
    if choice ==1:
        value = int(input("Enter the value to be inserted in bptree: \n"))
        element = value.to_bytes(10,'big')
        bptree[value] = element
        print("Value inserted!")
    elif choice ==2:
        value = int(input("Enter the value to be searched in bptree: \n"))
        start_time = time.time()
        if value in bptree:
            print("Element if found in bptree.")
        else:
            print("Element not present in the bptree")
        end_time = time.time()
        print(f"Time of search: {round((end_time-start_time)*1000 , 3)} milliseconds")
    elif choice == 3:
        count = 0
        for key in bptree.keys():
            element = bptree[key]
            element = int.from_bytes(element,'big')
            print(f"value: {element}")
            count +=1
            if count == len(bptree):
                break
    elif choice == 4:
        value = int(input("Enter the value to be deleted from bptree: \n"))
        try:
            bptree.pop(value)
            print("Value deleted from the bptree")
        except:
            print("Value not present in the bptree")
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid input")