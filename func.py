#function for addimg matrices
def addM(m1,m2):
	rno=len(m1)
	cno=len(m1[0])
	returnM=[]
	for r in range(rno):
		returnM.append([])
		for c in range(cno):
			s=m1[r][c]+m2[r][c]
			returnM[r].append(s)
			#end of for
		#end of for	
	return returnM

#function for subtracting matrices
def subM(m1,m2):
	rno=len(m1)
	cno=len(m1[0])
	returnM=[]
	for r in range(rno):
		returnM.append([])
		for c in range(cno):
			s=m1[r][c]-m2[r][c]
			returnM[r].append(s)
			#end of for
		#end of for	
	return returnM

#function for doing a transpose of matrix
def transpose(m):
	rno=len(m)
	cno=len(m[0])
	returnM=[]
	for c in range(cno):
		returnM.append([])
		for r in range(rno):
			returnM[c].append(m[r][c])
			#end of for
		#end of for
	return returnM

#function for multiplying two matrices
def mulM(m1,m2):
	if(len(m1[0])!=len(m2)):
		return False
		#end of if
	returnM=[]
	rno1=len(m1)
	cno1=len(m1[0])
	rno2=len(m2)
	cno2=len(m2[0])
	for r1 in range(rno1):
		returnM.append([])
		for c2 in range(cno2):
			s=0
			for c1 in range(cno1):
				s+=m1[r1][c1]*m2[c1][c2]
				#end of for
			returnM[r1].append(s)
			#end of for
		#end of for	
	return returnM	

#function for dividing the while matrix by a constant
def divByConstM(m,const):
	rno=len(m)
	cno=len(m[0])
	returnM=[]
	for r in range(rno):
		returnM.append([])
		for c in range(cno):
			returnM[r].append(m[r][c]/const)
			#end of for
		#end of for	
	return returnM;		

def I(x):
	returnM=[]
	for r in range(x):
		returnM.append([])
		for c in range(x):
			if(r==c):
				returnM[r].append(1)
				#endofif
			else:
				returnM[r].append(0)
				#endofelse
			#endoffor
		#endoffor		
	return returnM

def convertToDiagonal(m):
	o=len(m)
	returnM=[]
	for r in range(o):
		returnM.append([])
		for c in range(o):
			if(r==c):
				returnM[r].append(m[r][c])
			else:
				returnM[r].append(0)
	return returnM

def inverse(m):
	const=m[0][0]*m[1][1]-m[0][1]*m[1][0]
	temp=m[0][0]
	m[0][0]=m[1][1]
	m[1][1]=temp

	m[0][1]=-m[0][1]
	m[1][0]=-m[1][0]

	m=divByConstM(m,const)
	return m

def g(x,co,me):
	temp=subM(x,me)
	returnM=mulM(mulM(transpose(temp),inverse(co)),temp)
	return -0.5*returnM[0][0]

def runClassifier(data,hitRate,me,cov):
	length=len(data)
	count=0
	while(count<length):
		length1=len(data[count])
		count1=0
		
		count1=int(math.floor(0.75*length1))

		while(count1<length1):
			p=[]
			for count2 in range(length):
				p.append(g(data[count][count1],cov[count],me[count2]))
				#endoffor
			if(count==p.index(max(p))):
				hitRate[p.index(max(p))]+=1	
			count1+=1	
			#endofwhile
		count+=1
		#endofwhile
