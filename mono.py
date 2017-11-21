MappingKey = {'A':'F', 'B':'E' , 'C':'J', 'D':'Z', 
'E':'L', 'F':'O', 'G':'K', 'H':'R', 'I':'S', 'J':'A', 
'K':'W', 'L':'T', 'M':'G', 'N':'U', 'O':'X', 'P':'V', 
'Q':'C', 'R':'H', 'S':'D', 'T':'M', 'U':'Y', 'V':'N', 
'W':'I', 'X':'B', 'Y':'Q', 'Z':'P', 'a':'g', 'b':'o', 
'c':'i', 'd':'q', 'e':'k', 'f':'b', 'g':'s', 'h':'y', 
'i':'u', 'j':'r', 'k':'v', 'l':'c', 'm':'h', 'n':'l', 
'o':'w', 'p':'a', 'q':'n', 'r':'x', 's':'e', 't':'z', 
'u':'t', 'v':'m', 'w':'p', 'x':'j', 'y':'d', 'z':'f'}


def encry(plaintext): #Encryption algorithm
	c=[]
	for i in plaintext:
		if i.isalpha() :
			for j in MappingKey:
				if i==j: 
					c.append(MappingKey[j])	
		else:
			c.append(i)			
	ct = "".join(c)
	print "The ciphertext text after encryption is :",ct
	decry(ct)

def decry(ciphertext):	#Decryption algorithm
	p=[]
	for i in ciphertext:
		for k in MappingKey.keys():
			if i == MappingKey[k]:
				p.append(k)		
	pt = "".join(p)
	print "The plaintext after decryption is :", pt		


plaintext=raw_input("Enter the plain text\n") 
encry(plaintext)