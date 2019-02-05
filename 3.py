filec="codefile.py"
f=open(filec,'r')
lines=f.readlines()
f.close()
f=open(filec,'w')
for line in lines:
    x=line.strip()
    y=x.startswith("#")
    if y==False:
        f.write(line)
f.close()
f=open(filec,"r")
print "comments removed :)"
