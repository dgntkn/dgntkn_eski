
import sys

numArg = len(sys.argv) - 1
#print (numArg)
print (" ")
print ("There are " + str(numArg) + " arguments")
print (" ")
if str(sys.argv[1]) == "-help":
    print ("this is help message")
    print ("enter a string, any string")
    print (" ")
else:
    a = str(sys.argv[2])
    print (a)
    
