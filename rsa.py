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
	p=lcm(x-1, y-1)
	
	seed=datetime.datetime.now()
	seed=int(seed.microsecond)
	random.seed(seed)
	print seed
	
	e= random.randrange(1,p)
	while fractions.gcd(e,p)!= 1:
		e=random.randrange(1,p)
	
	
	d=modInv(e,p)
	while(d==e):
		d=modInv(e,p)
	
	tup=(e,d,n)
	
	return tup
	

def encrypt(pkey,plain_text):
	key,n=pkey
	cipher=[pow(ord(char),key,n) for char in plain_text]
	return cipher

def decrypt(pkey, cipher_text):
	key,n=pkey
	plain = [chr((char ** key) % n) for char in cipher]
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
		print "Values have be equal"	
	y=input("Retry with new value: ")
	y1=check_prime(y)

r1=datetime.datetime.now()
r1=r1.second
#Key pair generation
plain=raw_input("Enter the plain text: ")
key=keypair_gen(x,y)
public_key=(key[0], key[2])
private_key=(key[1],key[2])
print public_key, private_key

cipher=encrypt(public_key, plain)
print "Encrypted text is: "
print ''.join(map(lambda x: str(x), cipher))

print "\n\n", "Text after decryption: "
print decrypt(private_key, str(cipher))
r2=datetime.datetime.now()
r2=r2.second







