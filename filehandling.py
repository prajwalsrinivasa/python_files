import sys
import os

def hello(name):
    fw = open('sample.txt','w')
    fw.write("prajwal you should not think like that")
    fw.close()
    
    fr = open(name,'rU')
    text = fr.read()
    print(text,)

    fr.close()
def list_dir(name_file):
    
    
    filename = os.listdir(name_file)
    for fname in filename:
        path = os.path.join(name_file, fname)
        print (path)
        print(os.path.abspath(path))
        
    print (filename)
def main():
    hello(sys.argv[1])
    list_dir(sys.argv[2])

#found=fr.find('prajwal')
#print (text)
if __name__ == '__main__':
    main()
