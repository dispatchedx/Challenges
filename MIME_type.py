my_dict = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    ext, mt = input().split()
    my_dict[ext.lower()] = mt
for i in range(q):
    name = input()  # One file name per line.
    dot_index = name[::-1].find('.')
    if dot_index == -1:
        print('UNKNOWN')
    else:
        dot_index = len(name) - dot_index-1
        if name[dot_index+1::].lower() in my_dict:
            print(my_dict.get(name[dot_index+1::].lower()))


        else:
            print('UNKNOWN')

