f = open('_str_.py', 'r')

#print(f)
#print(f.read())
for line in f.readlines():
    print(line.strip())
#	print(line)