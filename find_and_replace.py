import fileinput

f1= open('sample.txt','r')
f2 = open('sample.txt','w')
for line in f1:
    f2.write(line.replace('tuchi','prajwal'))
    f2.write(line.replace('taru','tushar'))
