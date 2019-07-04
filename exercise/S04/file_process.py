fr = open('input.txt')
fw = open('output.txt', mode='w')

the_number = int(fr.readline())
the_cha = fr.readline()

for i in range (1,the_number+1):
    val = the_cha * i + '\n'
    fw.write(val)

fr.close()
fw.close()



