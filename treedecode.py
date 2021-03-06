
import json

def decodeTreeFile ( tree ) :
	info = []
	
	while tree :
		iModeBegin	=	0
		iModeEnd	=	tree.find(' ')
		assert iModeEnd>iModeBegin , 'Failed to find next end-of-mode character (reported range was [%s,%s)' % ( iModeBegin , iModeEnd )
		mode		=	tree[iModeBegin:iModeEnd]
		iNameBegin	=	iModeEnd+1
		iNameEnd	=	tree.find ( '\0' )
		assert iNameEnd>iNameBegin , 'Failed to find next end-of-name character (reported range was [%s,%s)' % ( iNameBegin , iNameEnd )
		iHashBegin	=	iNameEnd+1
		iHashEnd	=	iHashBegin+20
		name		=	tree[iNameBegin:iNameEnd]
		hash_e		=	tree[iHashBegin:iHashEnd]
		
		hash		=	''.join ( [ '%02x'%(ord(x)) for x in hash_e ] )
		
		#info.append ( {
		#	'name' : name ,
		#	'mode' : mode ,
		#	'hash' : hash
		#} )
		# save characters
		info.append ( [
			name ,
			mode ,
			hash
		] )
		
		tree		=	tree[iHashEnd:]
	
	return json.dumps(info,indent=4)
