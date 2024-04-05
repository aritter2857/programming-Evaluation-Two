#________________EVAL 2_______________________________

#ask to input grades

c1 = int(input("Enter course 1 grade: "))
c2 = int(input("Enter course 2 grade: "))
c3 = int(input("Enter course 3 grade: "))
c4 = int(input("Enter course 4 grade: "))

#calculate average
avg = (c1+c2+c3+c4)/4

#print average
print ("\n Your average is", avg)

if avg >=95:
  print ("\n Your grade is an A+")

elif avg >87 and avg <94:
  print ("\n Your grade is an A")

elif avg >80 and avg <86:
  print ("\n Your grade is an A-")

elif avg >77 and avg <79:
  print ("\n Your grade is a B+")

elif avg >72 and avg <76:
  print ("\n Your grade is a B")

elif avg >70 and avg <71:
  print ("\n Your grade is a B-")

elif avg >67 and avg <69:
  print ("\n Your grade is a C+")

elif avg >63 and avg <66:
  print ("\n Your grade is a C")

elif avg >60 and avg <62:
  print ("\n Your grade is a C-")

elif avg >57 and avg <61:
  print ("\n Your grade is a D+")

elif avg >54 and avg <56:
  print ("\n Your grade is a D")

elif avg >50 and avg <56:
  print ("\n Your grade is a D-")

elif  avg >0 and avg <49:
  print ("\n Your grade is a F")
