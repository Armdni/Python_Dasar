fellowship = {'aragron', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 =  hobbits_1.issubset(fellowship)
print("rest_1:", res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin', 'pippin'}
res_2 =  hobbits_2.issubset(fellowship)
print("rest_2:", res_2)
