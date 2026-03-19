#min
s="Welcome"
print(min(s))

#max
s="Welcome"
print(max(s))

#len
s="Welcome"
print(len(s))

#sorted
s="dcab"
print(sorted(s))

s="welcome"
print(sorted(s))


#'all','any'
s="abcd"
print(all(s))
print(any(s))


s=""
print(all(s))
print(any(s))


#enumerate
s="abc"
print(list(enumerate(s)))


#reversed
s="abc"
print(list(reversed(s)))


#isalnum





#isalpha


#istitle


#isdigit




#islower





#isupper


#isspace


#capitalize
s="ram IS a Good Boy"
s=s.capitalize()
print(s)


#title (first letter capital)
s="rAm IS a Good Boy"
s=s.title()
print(s)


#lower (only english)
s="ram IS a Good Boy"
s=s.lower()
print(s)


#upper
s="ram IS a Good Boy"
s=s.upper()
print(s)


#casefold (foreign language)
s="ram IS a Good Boy"
s=s.casefold()
print(s)


#swapcase (capital-small, small-capital)
s="ram IS a Good Boy"
s=s.swapcase()
print(s)


#lstrip (remove leftside space)
s="   ram"
print(len(s))
s=s.lstrip()
print(len(s))

#rstrip (rightside space)
s="ram  "
print(len(s))
s=s.rstrip()
print(len(s))


#strip (remove both left-right side space)
s="   ram  "
print(len(s))
s=s.strip()
print(len(s))


#center
s="ram"
print(s.center(5))
print(s.center(5,"*"))


#ljust
s="ram"
print(s.ljust(5,"*"))


#rjust
s="ram"
print(s.rjust(5,"*"))


#count
s="welcome"
print(s.count("e"))


#index
s="welcome"
print(s.index("e"))
print(s.index("e",2))
print(s.index("e",2,7))


#rindex
s="welcome"
print(s.rindex("e"))


#find
s="welcome"
print(s.find("x")) #diff value= -1
print(s.rfind("e"))


#startswith
s="ram"
print(s.startswith("r"))#T
print(s.startswith("m"))#F
print(s.startswith("r",0))#T
print(s.startswith("r",3))#F

#endswith
s="ram"
print(s.endswith("m"))#T
print(s.endswith("a"))#F
print(s.startswith("m",4))#F


#split
s="ram is a good boy"
L=s.split()
print(L)

s="ram is a good boy"
L=s.split("a") #a is out from string
print(L)



#join
s="ram is a good boy"
L=s.split()
s1=" ".join(L)
print(s1)


#replace
s="ram is a good boy"
s=s.replace("boy","x")
print(s)


#encode
s="ram"
b=s.encode()
print(b)
s1=b.decode()
print(s1)















































