def fun():                              #Function to generate a dictionary consisting of all alphabet-number pair
	allvalues = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	MappingKey = dict([(allvalues[i], i*1) for i in range(len(allvalues))])
	return MappingKey
			
def search(alist):
	at=list()
	for i in alist:
		for j in MappingKey:
			if i==MappingKey[j]:
				at.append(j)
	return at			

def encry(plaintext, key): #Encryption algorithm
	ciphertext = list()
	ct = list()
	plaintext=plaintext.upper()
	for i in plaintext:
		for j in MappingKey:
			if i==j:
				x = (MappingKey[j]+key)%26
				ciphertext.append(x)		
	ct=search(ciphertext)			
	c = "".join(ct)		
	print "The cipher text after encryption is :",c
	decry(c,key)	

		
def decry(ciphertext, key): #Decryption algorithm
	ct = ciphertext
	plaintext = list()
	pt=list()
	for i in ct:
		for j in MappingKey:
			if i==j:
				x=(MappingKey[j]-key)%26
				plaintext.append(x)
	pt=search(plaintext)			
	p = "".join(pt)

	print "The ciphertext after decryption is :", p.lower()				
		


plaintext=raw_input("Enter the plain text\n") 
key=int(raw_input("Enter the substitution key size\n"))
print "The plaintext is :",plaintext
MappingKey=fun()
encry(plaintext,key)