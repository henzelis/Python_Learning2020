#my_file = open('test.txt')
#print(my_file.readlines())
#my_file.close()


with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(my_file.readlines())



