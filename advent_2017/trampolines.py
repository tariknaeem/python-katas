import inputs

def update_one(jump):
    return jump + 1

def update_two(jump):
    if jump >= 3:
       return jump - 1 
    else:
       return jump + 1 

def solve(jumptable, update):
    offsets = list(jumptable)
    position = 0
    counter = 0
    while position >= 0 and position < len(offsets):
        offset = offsets[position]
        offsets[position] = update(offset) 
        position += offset
        counter += 1
    return counter

jumptable = [int(i) for i in inputs.trampolines.split()]

print(solve(jumptable, update_one), solve(jumptable, update_two))
