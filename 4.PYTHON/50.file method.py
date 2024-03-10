with open('mark.txt', 'r') as file:
    i = 0
    while True :
        i = i + 1
        line = file.readline()
        if not line :
            break
        marks = line.split(',')
        print(f"marks of student {i} are {marks[0]}")
        print(f"marks of student {i} are {marks[1]}")
        print(f"marks of student {i} are {marks[2]}")

with open('mark.txt', 'w') as file:
    lines = ['line1\n','line2\n','line3\n','line4\n']
    file.writelines(lines)
