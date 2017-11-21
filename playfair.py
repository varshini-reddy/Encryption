def matrix(key):						#Function to create key matrix 
	matrix=[]
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
	for e in alphabet:
		if e not in matrix:
			matrix.append(e)	
	matrix_group=[]
	for e in range(5):
		matrix_group.append('')		#Creating a (5X5) matrix 
	matrix_group[0]=matrix[0:5]		
	matrix_group[1]=matrix[5:10]
	matrix_group[2]=matrix[10:15]
	matrix_group[3]=matrix[15:20]
	matrix_group[4]=matrix[20:25]
	return matrix_group


def message_to_digraphs(message_original):	#Function to create digraphs given text
	message=[]
	for e in message_original:
		message.append(e)
	for unused in range(len(message)):		#Remove spaces
		if " " in message:
			message.remove(" ")
i=0							#If consecutive letters are same, add X 
	for e in range(len(message)/2):
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
		i=i+2

	if len(message)%2==1:				#Add X if there are odd characters
		message.append("X")
i=0
	new=[]
	for x in xrange(1,len(message)/2+1):
		new.append(message[i:i+2])
		i=i+2
	return new


def findpos(p,matrix):					#Function to find position of characters
	t=[]
	for i in range(5):
		for j in range(5):
			if p==matrix[i][j]:
				t.append(i)
				t.append(j)	
				return t			


def encry(p,key):						#Function to perform encryption
	cipher=[]
	m=matrix(key)
	pt=message_to_digraphs(p)
	for i in pt:	
		x=findpos(i[0],m)
		a=x[0]
		b=x[1]
		x=findpos(i[1],m)
		c=x[0]
		d=x[1]
		if a==c:
			ct1=m[a][(b+1)%5]
			ct2=m[a][(c+1)%5]
		elif b==d:
			ct1=m[(a+1)%5][b]
			ct2=m[(c+1)%5][b]
		else:
			ct1=m[a][d]
			ct2=m[c][b]
		cipher.append(ct1)
		cipher.append(ct2)
		ct="".join(cipher)			
	return ct
	

def decry(c,key):						#Function to perform decryption
	plain=[]
	m=matrix(key)
	ct=message_to_digraphs(c)
	for i in ct:	
		x=findpos(i[0],m)
		a=x[0]
		b=x[1]
		x=findpos(i[1],m)
		c=x[0]
		d=x[1]
		if a==c:
			pt1=m[a][(b-1)%5]
			pt2=m[a][(c-1)%5]
		elif b==d:
			pt1=m[(a-1)%5][b]
			pt2=m[(c-1)%5][b]
		else:
			pt1=m[a][d]
			pt2=m[c][b]
		plain.append(pt1)
		plain.append(pt2)
		pt="".join(plain)			
	return pt


def main():							#Main function to take input values
key=raw_input("Please input the key : ")
message=raw_input("Please input the message : ")
if message.islower():	
	message=message.upper()
		flag=1
cipher= encry(message,key)
print "The text ciphertext after encryption is: ", cipher	
plain = decry(cipher,key)
if flag==1:
		plain=plain.lower()
print "The plaintext after decryption is: ",plain

main()

