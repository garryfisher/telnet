qtech = open('qtech.txt')

result = ''
for x in qtech:
    if 'STATIC' in x:
        result += x
        result += '\n'
qtech.closed

file = open('qtech1', 'w')
file.write(result)
file.closed
