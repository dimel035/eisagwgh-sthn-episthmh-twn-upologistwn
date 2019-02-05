import random

def tableprint(a,b,mines):
    p=b*"0"
    g=""
    for i in range(0,a):
        g=g+(p+'\n')
    g=getmines(g,mines)
    g=getneighbours(g,b)
    print g

def getmines(g,mines):
    new_list=(list(g))
    ties=len(new_list)
    newg=""
    for i in range(0,mines):
        pos=random.randint(0,ties-1)
        while new_list[pos]=="\n":
                pos=random.randint(0,ties-1)
        new_list[pos]="X"
    for i in range (0,ties-1):
        newg=newg+new_list[i]
    g=newg
    return g

def getneighbours(g,b):
    new_list=(list(g))
    ties=len(new_list)
    newg=""
    b=b+1
    for i in range(0,ties):
        if new_list[i]!="X" and new_list[i]!="\n":
            new_list[i]=0
    for i in range(0,ties):
        if new_list[i]=="X":

            if i == 0:
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1
                if new_list[i+b+1]!="X" and new_list[i+b+1]!="\n":
                    new_list[i+b+1]=new_list[i+b+1]+1

            elif i<=b-2:
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1
                if new_list[i+b+1]!="X" and new_list[i+b+1]!="\n":
                    new_list[i+b+1]=new_list[i+b+1]+1
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i+b-1]!="X" and new_list[i+b-1]!="\n":
                    new_list[i+b-1]=new_list[i+b-1]+1

            elif i==b-1:
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i+b-1]!="X" and new_list[i+b-1]!="\n":
                    new_list[i+b-1]=new_list[i+b-1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1

            elif (ties-1)-i<=b-1:
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[(i-b)+1]!="X" and new_list[(i-b)+1]!="\n":
                    new_list[(i-b)+1]=new_list[(i-b)+1]+1
                if new_list[(i-b)-1]!="X" and new_list[(i-b)-1]!="\n":
                    new_list[(i-b)-1]=new_list[(i-b)-1]+1

            elif i==(ties)-b:
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[(i-b)+1]!="X" and new_list[(i-b)+1]!="\n":
                    new_list[(i-b)+1]=new_list[(i-b)+1]+1

            elif i==ties-1:
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[(i-b)-1]!="X" and new_list[(i-b)-1]!="\n":
                    new_list[(i-b)-1]=new_list[(i-b)-1]+1

            elif new_list[i-1]=="\n":
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[(i-b)+1]!="X" and new_list[(i-b)+1]!="\n":
                    new_list[(i-b)+1]=new_list[(i-b)+1]+1
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[i+b+1]!="X" and new_list[i+b+1]!="\n":
                    new_list[i+b+1]=new_list[i+b+1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1

            elif new_list[i+1]=="\n":
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[(i-b)-1]!="X" and new_list[(i-b)-1]!="\n":
                    new_list[(i-b)-1]=new_list[(i-b)-1]+1
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i+b-1]!="X" and new_list[i+b-1]!="\n":
                    new_list[i+b-1]=new_list[i+b-1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1
            else:
                if new_list[i-b]!="X" and new_list[i-b]!="\n":
                    new_list[i-b]=new_list[i-b]+1
                if new_list[(i-b)-1]!="X" and new_list[(i-b)-1]!="\n":
                    new_list[(i-b)-1]=new_list[(i-b)-1]+1
                if new_list[i-1]!="X" and new_list[i-1]!="\n":
                    new_list[i-1]=new_list[i-1]+1
                if new_list[i+b-1]!="X" and new_list[i+b-1]!="\n":
                    new_list[i+b-1]=new_list[i+b-1]+1
                if new_list[i+b]!="X" and new_list[i+b]!="\n":
                    new_list[i+b]=new_list[i+b]+1
                if new_list[(i-b)+1]!="X" and new_list[(i-b)+1]!="\n":
                    new_list[(i-b)+1]=new_list[(i-b)+1]+1
                if new_list[i+1]!="X" and new_list[i+1]!="\n":
                    new_list[i+1]=new_list[i+1]+1
                if new_list[i+b+1]!="X" and new_list[i+b+1]!="\n":
                    new_list[i+b+1]=new_list[i+b+1]+1

    for i in range(0,ties):
		if new_list[i]!="X":
			if new_list[i]==None:
				new_list[i]="0"
			new_list[i]=str(new_list[i])
    for i in range (0,ties):
        newg=newg+new_list[i]
    g=newg
    return g



def check(invar):
    while invar<=0:
        message="please give number greater than 0: "
        invar=input(message)
    return invar


height=input("please give height: ")
height=check(height)
width=input("please give width: ")
width=check(width)
mines=input("please give number of mines: ")
mines=check(mines)
tableprint(height,width,mines)
