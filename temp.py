import sys
import math

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

count=1
nooffiles=len(sys.argv)-1

data=[]
mean=[]
covariance=[]

#reading files and storing data in data[]
while(count<=nooffiles):
	with open(sys.argv[count]) as curFile:
		data.append([])
		mean.append([])
		covariance.append([])
		content = curFile.read().splitlines()
		length=len(content);
		count1=0
		while(count1<length):
			value=content[count1].split(" ");
			data[count-1].append([[float(value[0])],[float(value[1])]])
			count1+=1
			#end of while
		#end of with	
	count+=1
	#end of while

#calculating mean
length=len(data)
count=0
while(count<length):
	tempSum=[[0],[0]]
	#how much data to be taken as training	
	length1=0.75*len(data[count])-1
	count1=0
	while(count1<length1):
		tempSum=addM(data[count][count1],tempSum)
		count1+=1
		#end of while
	mean[count]=divByConstM(tempSum,length1)
	print "for file : "+str(sys.argv[count+1])+" mean is : "+str(mean[count])
	count+=1
	#end of while

#doing case 2
covariance2=[]
length=len(data)
count=0
while(count<length):
	covariance2.append([])
	covariance2[count]=[[0,0],[0,0]]
	#how much data to be taken as training	
	length1=0.75*len(data[count])-1
	count1=0
	while(count1<length1):
		covariance2[count]=addM(mulM(subM(data[count][count1],mean[count]),transpose(subM(data[count][count1],mean[count]))),covariance2[count])
		count1+=1
		#end of while
	covariance2[count]=divByConstM(covariance2[count],length1)	
	print covariance2[count]
	count+=1
	#end of while

#part 2 (a)
covariance2a=subM(I(2),I(2))
length=len(data)
count=0
while(count<length):
	covariance2a=addM(convertToDiagonal(covariance2[count]),covariance2a)
	count+=1
	#endofwhile
covariance2a=divByConstM(covariance2a,length)
print covariance2a

length=len(data)
count=0
hitRate=[0,0,0]
while(count<length):
	length1=len(data[count])
	count1=0
	
	count1=int(math.floor(0.75*length1))

	while(count1<length1):
		p=[]
		for count2 in range(length):
			p.append(g(data[count][count1],covariance2a,mean[count2]))
			#endoffor
		if(count==p.index(max(p))):
			hitRate[p.index(max(p))]+=1	
		count1+=1	
		#endofwhile
	count+=1
	#endofwhile
print "2 (a) hit rate "+str(hitRate[0])+" "+str(hitRate[1])+" "+str(hitRate[2])		

#part 2 (b)
covariance2b=subM(I(2),I(2))
length=len(data)
count=0
while(count<length):
	covariance2b=addM(covariance2[count],covariance2b)
	count+=1
	#endofwhile
covariance2b=divByConstM(covariance2b,length)
print covariance2b

length=len(data)
count=0
hitRate=[0,0,0]
while(count<length):
	length1=len(data[count])
	count1=0
	
	count1=int(math.floor(0.75*length1))

	while(count1<length1):
		p=[]
		for count2 in range(length):
			p.append(g(data[count][count1],covariance2b,mean[count2]))
			#endoffor
		if(count==p.index(max(p))):
			hitRate[p.index(max(p))]+=1	
		count1+=1	
		#endofwhile
	count+=1
	#endofwhile
print "2 (b) hit rate "+str(hitRate[0])+" "+str(hitRate[1])+" "+str(hitRate[2])	