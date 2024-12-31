outputFile = []

with open('Village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
    
with open('Village/out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))
