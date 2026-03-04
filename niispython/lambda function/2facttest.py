def facttest(no):
	f=1
	if no>0:
		f=f*no
		no=no-1
		facttest(no)
	return f
print(facttest(3))		