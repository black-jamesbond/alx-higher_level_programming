cont =len(sys.argv)
result = 0
i = cont-1
while i != 0:
    result+= sys.argv[i]
    i-=1

print (result)
