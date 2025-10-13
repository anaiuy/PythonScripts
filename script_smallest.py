import two_smallest
import lists
my_file="result.txt"
file=open(my_file, 'w')
file.write(str(two_smallest.find_two_smallest(lists.list_1))+"\n")
file.write(str(two_smallest.find_two_smallest(lists.list_2))+"\n")
file.write(str(two_smallest.find_two_smallest(lists.list_3))+"\n")
file.close()
