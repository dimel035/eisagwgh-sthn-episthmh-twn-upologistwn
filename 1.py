def sumIntervals(a):
	ll=len(a)
	for i in range (0,ll):
		x=a[i]
		for k in range (x[0]+1,x[1]):
			x.append(k)
		x.sort()
		a[i]=x

	for i in range(0,ll):
		for k in range(0,ll):
			if i<>k:
				x=a[i]
				y=a[k]
				s=0
				for item in x:
					for item1 in y:
						if item==item1:
							s+=1
				if s>0:
					l1=len(x)
					l2=len(y)
					s1=0
					for q in range(0,l1):
						for d in range(0,l2):
							if x[q]==y[d]:
								s1=s1+1
								z=x[q]
					if s1>2:
						if q>d:
							for q in range(0,l1):
								for d in range(0,l2):
									if x[q]==y[d]:
										y[d]=0
						elif d>q:
							for q in range(0,l1):
								for d in range(0,l2):
									if x[q]==y[d]:
										x[q]=0
						hm1=0
						hm2=0
						for q in range (0,l1):
							if x[q]==0:
								hm1=hm1+1
						for d in range (0,l2):
							if y[d]==0:
								hm2=hm2+1
						for w in range(0,hm1):
							x.remove(0)
						for n in range (0,hm2):
							y.remove(0)
					elif s1==2:
						if x.index(z)==(l1-1) or x.index(z)==0:
							x.remove(z)
						elif y.index(z)==(l2-1) or y.index(z)==0:
							y.remove(z)
				a[i]=x
				a[k]=y
	ffs=0
	for i in range (0,ll):
		if a[i]==[]:
			ffs=ffs+1
	for i in range (0,ffs):
		a.remove([])
	ll=len(a)
	for i in range (0,ll):
		x=a[i]
		lx=len(x)
		y=[x[0],x[lx-1]]
		a[i]=y
	newl=len(a)
	sum=0
	for i in range (0,newl):
		x=a[i]
		c=x[1]-x[0]
		sum=sum+c
	print sum






a=[[1,2], [6, 10], [11, 15]]
sumIntervals(a)
