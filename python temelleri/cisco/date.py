#!/usr/bin/python
import sys
from datetime import date

todaysDate = str(date.today())
print (" ")
print ("Today is " + todaysDate)
myBirthdate = str(sys.argv[1])
print (" ")
print (" ")
if todaysDate == myBirthdate:
    print ("Whoa.. Happy Birthday!")
    print ("Check under the chair for prize")
else:
    print ("it is not your birthday")
print (" ")
print (" ")
