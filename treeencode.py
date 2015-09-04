import json
import struct


ka = ord('a')
kf = ord('f')
kA = ord('A')
kF = ord('F')
k0 = ord('0')
k9 = ord('9')
def hex2num ( c ) :
	a = ord(c)
	if 0<=a and a<=k9 :
		return a - k0
	if ka<=a and a<=kf :
		return a - ka + 10
	if kA<=a and a<=kA :
		return a - kA + 10
	assert False , '%s is an invalid hex character' % ( c )


def encodeTreeFile ( tree ) :
	tree = json.loads ( tree )
	
	
	data = ''
	
	# have to encode it as hex because you can't concatenate binary strings because python is stupid.
	
	for name,mode,hash in tree :
		data += ('%s %s\0'%(mode,name)).encode ( 'hex' )
		
		bytes	=	[ hash[i:i+2] for i in range(0,len(hash),2) ] # split into every two characters
		bytes	=	[ ( (hex2num(a)<<4) + hex2num(b) ) for a,b in bytes ]
		hash_e	=	struct.pack ( 'B'*20 , *bytes )
		hash_e	=	''.join ( hash_e )
		
		data += hash_e.encode ( 'hex' )
	
	return data.decode ( 'hex' )

