hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragon'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_1 = hobbits.union(dunedain).union(elf).union(human).union(maiar)
print("fellowship_1:", fellowship_1)

hobbits = {'frodo', 'sam', 'merry', 'pippin'}