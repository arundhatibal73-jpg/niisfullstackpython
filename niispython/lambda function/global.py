f=1
def facttest(no):
	global f
	if no>0:
		f=f*no
		no=no-1
		facttest(no)
	return f
print(facttest(3))		