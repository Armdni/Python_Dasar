fellowship = {'aragron', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

res_1 = fellowship.isdisjoint({'aragon', 'gimli'})
print("res_1:", res_1)

res_1 = fellowship.isdisjoint({'pippin', 'bilbo'})