import sys
f = 1

while(f<len(sys.argv)):
    file = open(sys.argv[f] , "r")
    sys.stdout.write(file.read())
    file.close
    f+=1