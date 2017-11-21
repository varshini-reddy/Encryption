def hill(message, key, decrypt = False):
from math import sqrt		  	#To check for key validity
n = int(sqrt(len(key)))
    	if n * n != len(key):
       		raise Exception("Invalid key")

alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-;|’ 
tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])

    	if len(message) % n > 0:		#Message padding if needed
message += '|' * (n - (len(message) % n))

keylist = []   				  	#Key matrix 
    	for a in key:
        		keylist.append(tonum[a])
keymatrix = [] 
   	for i in range(n):
        		keymatrix.append(keylist[i * n : i * n + n])
from numpy import matrix
from numpy import linalg
keymatrix = matrix(keymatrix).round().T

    if decrypt:					#Matrix determinant calculation 
        	determinant = linalg.det(keymatrix).round()
        	if determinant == 0:
           		raise Exception("Determinant ZERO, CHANGE THE KEY!")
        	elif determinant % len(alpha) == 0:
            		raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")

        	inverse = []
        	keymatrix =  matrix(keymatrix.getI() * determinant).round()

        	invdeterminant = 0			#Matrix indeterminant calculation
        	for i in range(10000):
         		 if (determinant * i % len(alpha)) == 1:
            		 invdeterminant = i
               	 break
        	for row in keymatrix.getA() * invdeterminant:
            		newrow = []
            		for i in row:
                		newrow.append( i.round() % len(alpha) )
          		inverse.append(newrow)
       	              keymatrix = matrix(inverse)

   	out = ''
    	for i in range(len(message) / n):
        	lst = matrix( [[tonum[a]] for a in message[i * n:i * n + n]] )
        	result = keymatrix * lst
        	out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in 
range(len(result))])
   	return out

#Take input values
key = raw_input("Enter the key: ")
key=key.upper()
msg = raw_input("Enter the plaintext: ")
print "The plaintext is: ", msg
if msg.islower():
	flag=1
	msg=msg.upper()
else:
	flag=2	

cipherText = hill(msg, key)
print "The ciphertext after encryption is: ",cipherText
decipherText = hill(cipherText, key, True)
if flag==1:
	decipherText=decipherText.lower()	
print "The plaintext after decryption is: ",decipherText
