
#ntpServers = {"server1" : "172.24.32.32", "server2" : "172.24.32.33", "server3" : "172.24.32.34"}

#for key in ntpServers:
    #print (key + " = " + ntpServers[key])



#def someMath(x):
    #a = x * x
    #return a

#b = someMath(5)

#print (b)
import sys

numArg = len(sys.argv) - 1
print (numArg)
print (" ")
print ("There are " + str(numArg) + " arguments")
print (" ")
if str(sys.argv[1]) == "-help":
    print ("this is help message")
    print ("enter a string, any string")
    print (" ")
else:
    print("The input was " + str(sys.argv[1]))
