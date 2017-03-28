import random
import datetime
import fractions
import math


def check_prime(a):
	for i in range(2,a):
		if a%i==0:
			return False
	return True		

def lcm(x, y):
   if x > y:
       grt = x
   else:
       grt = y

   while(True):
       if((grt % x == 0) and (grt % y == 0)):
           lcm = grt
           break
       grt += 1

   return lcm



def extEuc(a, b) :
    if b == 0 :
        return 1,0,a
    else :
        x, y, gcd = extEuc(b, a % b)
        return y, x - y * (a // b),gcd
 
def modInv(a,m) :
    x,y,gcd = extEuc(a,m)
    if gcd == 1 :
        return x % m
    else :
        return None


def keypair_gen(x,y):
	n=x*y
	#lcm is optional, the value of p can taken as be p=(x-1)*(y-1)
	phi=lcm(x-1, y-1)
	
	seed=datetime.datetime.now()
	seed=int(seed.microsecond)
	random.seed(seed)
	
	e= random.randrange(1,phi)
	while fractions.gcd(e,phi)!= 1 and fractions.gcd(e,n)!=1:
		e=random.randrange(1,phi)
	
	d=modInv(e,phi)
	while(d==e):
		d=modInv(e,phi)
	
	tup=(e,d,n)
	
	return tup
	

def encrypt(pkey,plain_text):
	key,n=pkey
	cipher=[pow(ord(x),key,n) for x in plain_text]
	return cipher

def decrypt(pkey, cipher_text):
	key,n=pkey
	plain = [chr((x ** key) % n) for x in cipher]
	return ''.join(plain)


print "RSA algorithm - encryption and Decryption"
x = input("Enter a prime number: ")
x1=check_prime(x)
while x1!=True:
	print "Not a prime"
	x=input("Retry with new value: ")
	x1=check_prime(x)

y = input ("Enter the next number: ")
y1=check_prime(y)
while y1!=True or y==x:
	if y1!=True:
		print "Not a prime"
	else:
		print "Values should not be equal"	
	y=input("Retry with new value: ")
	y1=check_prime(y)


#Key pair generation
plain=raw_input("Enter the plain text: ")
key=keypair_gen(x,y)
public_key=(key[0], key[2])
private_key=(key[1],key[2])
print "Public key is: ",public_key,"\nPrivate key is: ", private_key

cipher=encrypt(public_key, plain)
print "Encrypted text is: "
print ''.join(map(lambda x: str(x), cipher))

print "\nText after decryption: "
print decrypt(private_key, cipher)








