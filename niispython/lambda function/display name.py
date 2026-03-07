def reverse_string(s):
	if len(s)==0:#base condition
		return s
	return reverse_string(s[1:])+s[0]
name="little"
print(reverse_string(name))		