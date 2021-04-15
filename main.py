# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import time
start = time.time()
def sorting(filename):
  infile = open('20k.txt')
  seq = []
  for line in infile:
    temp = line.split()
    for i in temp:
      seq.append(i)
  infile.close()

  def merge_sort(seq, key=lambda x: x):
    if len(seq) == 1:
        return seq
    else:
        # recursive step. Break the list into chunks of 1
        mid_index = len(seq) // 2
        left  = merge_sort( seq[:mid_index])
        right = merge_sort( seq[mid_index:])

    left_counter, right_counter, master_counter = 0, 0, 0

    while left_counter < len(left) and right_counter < len(right):
      if key(left[left_counter]) < key(right[right_counter]):
        seq[master_counter] = left[left_counter]
        left_counter += 1
      else:
        seq[master_counter] = right[right_counter]
        right_counter += 1

      master_counter += 1



    # Handle the remaining items in the remaining_list
    # Either left or right is done already, so only one of these two
    #    loops will execute

    while left_counter < len(left):  # left list isn't done yet
        seq[master_counter] = left[left_counter]
        left_counter   += 1
        master_counter += 1

    while right_counter < len(right):  # right list isn't done yet
        seq[master_counter] = right[right_counter]
        right_counter   += 1
        master_counter  += 1

    return seq


  merge_sort(seq)
  print("Sorted words list is:")
  for i in range(len(seq)):
    print("%s" % seq[i])



  
sorting("sample.txt")

end = time.time()
print("Execution time:", end-start)
