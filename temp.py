import sys
import math
import matplotlib.pyplot as plt

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
		#endoffor
	#endoffor	
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
		#endoffor
	#endoffor	
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
		#endoffor
	#endoffor
	return returnM

#function for multiplying two matrices
def mulM(m1,m2):
	if(len(m1[0])!=len(m2)):
		return False
	#endofif
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
			#endoffor
			returnM[r1].append(s)
		#endoffor
	#endoffor	
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
		#endoffor
	#endoffor	
	return returnM;		

#returns identity matrix for given order as argument
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

#converts a normal matrix to identity matrix
def convertToDiagonal(m):
	o=len(m)
	returnM=[]
	for r in range(o):
		returnM.append([])
		for c in range(o):
			if(r==c):
				returnM[r].append(m[r][c])
			#endofif
			else:
				returnM[r].append(0)
			#endofelse
		#endoffor
	#endoffor		
	return returnM

#to update, currently only for 2X2 matrix
def inverse(m):
	returnM=[[0,0],[0,0]]
	const=m[0][0]*m[1][1]-m[0][1]*m[1][0]
	returnM[1][1]=m[0][0]
	returnM[0][0]=m[1][1]

	returnM[0][1]=-m[0][1]
	returnM[1][0]=-m[1][0]

	returnM=divByConstM(m,const)

	return returnM

def det(m):
	return m[0][0]*m[1][1]-m[1][0]*m[0][1]

#discriminating function
def g(x,co,me):
	temp=subM(x,me)
	returnM=mulM(mulM(transpose(temp),inverse(co)),temp)
	return (-0.5*returnM[0][0]-0.5*math.log(det(co)))

#function that classifies the data point
def classify(data,me,cov):
	p=[]
	length=len(me)
	#checking for every class
	for cl in range(length):
		p.append(g(data,cov[cl],me[cl]))
	#endoffor
	return p.index(max(p))

#classifies a large data set
def runClassifier(data,hitRate,me,cov,subplot):
	clsno=len(data)
	#for data of every class
	for cl in range(clsno):
		dtpntno=len(data[cl])	
		#dtpnti=int(math.floor(0.75*length1))
		#for every data point of that class
		for dtpnti in range(int(math.floor(0.75*dtpntno)),dtpntno):
			clas=classify(data[cl][dtpnti],me,cov)
			subplot.plot(data[cl][dtpnti][0][0],data[cl][dtpnti][1][0],color=color1[cl],marker='o')
			if(cl==clas):
				hitRate[cl]+=1
			#enfofif	
		#endoffor
	#endoffor

def plotBoundries(subplot,me,cov):
	x=minx
	print minx,miny,maxx,maxy
	while (x < maxx):
		y=miny
		while (y < maxy):
			#print x,y
			subplot.plot(x,y,color=color[classify([[x],[y]],me,cov)],marker="o")
			y=y+increamentory
		#print "came out"	
		x=x+increamentorx

#universal matrices
data=[]
mean=[]
covariance=[]
dtdim=0
fig=plt.figure()
fig1=plt.figure()
ax1=fig.add_subplot(221)
ax1.set_title(" 1 a i ")
ax2=fig.add_subplot(222)
ax2.set_title(" 1 b ")
ax3=fig1.add_subplot(221)
ax3.set_title(" 2 a ")
ax4=fig1.add_subplot(222)
ax4.set_title(" 2 b ")
ax5=fig1.add_subplot(223)
ax5.set_title(" 2 c ")

#ranges of data
minx=0
maxx=0
miny=0
maxy=0

color1=["#E21818","#17E81F","#252BDF","#D2C81D"]
color=["#CD5C5C","#6ED377","#6A6DDA","#E9E97E"]

#reading files and storing data in data[]
datavalueseparator=" "
nooffiles=len(sys.argv)
#for each file
for filei in range(1,nooffiles):
	with open(sys.argv[filei]) as curFile:
		data.append([])
		mean.append([])
		covariance.append([])
		content = curFile.read().splitlines()
		lineno=len(content);
		#for each line
		for linei in range(lineno):
			value=content[linei].split(datavalueseparator);
			data[filei-1].append([])
			
			#for each data value in data point
			for valuei in range(len(value)):
				try:
					data[filei-1][linei].append([float(value[valuei])])	
				except ValueError:
					continue	
			dtdim=len(data[0][0][0])		
			#endoffor
			#checking for ranges of data
			if(float(value[0])<minx):
				minx=float(value[0])
			if(float(value[0])>maxx):
				maxx=float(value[0])
			if(float(value[1])<miny):
				miny=float(value[1])
			if(float(value[1])>maxy):
				maxy=float(value[1])
		#endoffor
	#endofwith
#endoffor

#no of classes
clsno=len(data)
increamentorx=(maxx-minx)/25
increamentory=(maxy-miny)/25

#calculating mean
#for each class
for clsi in range(clsno):
	tempSum=data[clsi][0]
	#how much data to be taken as training	
	dtpntno=int(math.floor(0.75*len(data[clsi])))
	for dtpnti in range(1,dtpntno):
		tempSum=addM(data[clsi][dtpnti],tempSum)
	#endoffor
	mean[clsi]=divByConstM(tempSum,dtpntno)
#endoffor
#print mean
#findnig covariance matrix
#for each class
for clsi in range(clsno):
	covariance[clsi]=mulM(subM(data[clsi][0],mean[clsi]),transpose(subM(data[clsi][0],mean[clsi])))
	#how much data to be taken as training
	dtpntno=int(math.floor(0.75*len(data[clsi])))
	#for each data point
	for dtpnti in range(1,dtpntno):
		covariance[clsi]=addM(mulM(subM(data[clsi][dtpnti],mean[clsi]),transpose(subM(data[clsi][dtpnti],mean[clsi]))),covariance[clsi])
	#endoffor
	covariance[clsi]=divByConstM(covariance[clsi],dtpntno)	
#endoffor
print covariance

hitRate=[]
#initialising hitRate
for i in range(clsno):
	hitRate.append(0)
#endoffor


#part 1 (a) (i)
covariance1ai=[]
covariance1ai.append([])
covariance1ai[0]=covariance[0]
#average of each class
for clsi in range(1,clsno):
	covariance1ai.append([])
	covariance1ai[0]=addM(covariance[clsi],covariance1ai[0])
#endoffor
covariance1ai[0]=divByConstM(covariance1ai[0],clsno)
#making cov for each class same
for clsi in range(1,clsno):
	covariance1ai[clsi]=covariance1ai[0]
#endoffor
#-------------------------------------------------------------------
plotBoundries(ax1,mean,covariance1ai)
#-------------------------------------------------------------------
runClassifier(data,hitRate,mean,covariance1ai,ax1)
print "1 (a) (i) hit rate "
print hitRate

#part 1 (b)
#initialising hitRate
for i in range(clsno):
	hitRate[i]=0
#endoffor
#-------------------------------------------------------------------
plotBoundries(ax2,mean,covariance)
#-------------------------------------------------------------------

runClassifier(data,hitRate,mean,covariance,ax2)
print "1 (b) hit rate "
print hitRate

#part 2 (a)
covariance2a=[]
covariance2a.append([])
covariance2a[0]=convertToDiagonal(covariance[0])
#average of each class
for clsi in range(1,clsno):
	covariance2a.append([])
	covariance2a[0]=addM(convertToDiagonal(covariance[clsi]),covariance2a[0])
#endoffor
covariance2a[0]=divByConstM(covariance2a[0],clsno)
covAvg=0
#taking average of diagonal values
for r in range(dtdim):
	covAvg+=covariance2a[0][r][r]
#endoffor
covAvg/=dtdim
#setting diagonals elements to avg
for r in range(dtdim):
	covariance2a[0][r][r]=covAvg	
#endoffor
for clsi in range(1,clsno):
	covariance2a[clsi]=covariance2a[0]
#eendoffor
#initialising hitRate
for i in range(clsno):
	hitRate[i]=0
#endoffor
#-------------------------------------------------------------------
plotBoundries(ax3,mean,covariance2a)
#-------------------------------------------------------------------
runClassifier(data,hitRate,mean,covariance2a,ax3)
print "2 (a) hit rate "
print hitRate

#part 2 (b)
covariance2b=[]
covariance2b.append([])
covariance2b[0]=convertToDiagonal(covariance[0])
#taking average of each class
for clsi in range(1,clsno):
	covariance2b.append([])
	covariance2b[0]=addM(convertToDiagonal(covariance[clsi]),covariance2b[0])
#endoffor
covariance2b[0]=divByConstM(covariance2b[0],clsno)
#setting each class to same cov
for clsi in range(1,clsno):
	covariance2b[clsi]=covariance2b[0]
#initialising hitRate
for i in range(clsno):
	hitRate[i]=0
#endoffor
#-------------------------------------------------------------------
plotBoundries(ax4,mean,covariance2b)
#-------------------------------------------------------------------
runClassifier(data,hitRate,mean,covariance2b,ax4)
print "2 (b) hit rate "
print hitRate

#part 2 (c)
covariance2c=covariance
#coverting cov to diagonal for each class
for clsi in range(clsno):
	covariance2c[clsi]=convertToDiagonal(covariance2c[clsi])
#endoffor
#initialising hitRate
for i in range(clsno):
	hitRate[i]=0
#endoffor
#-------------------------------------------------------------------
plotBoundries(ax5,mean,covariance2c)
#-------------------------------------------------------------------
runClassifier(data,hitRate,mean,covariance2c,ax5)
print "2 (c) hit rate "
print hitRate

#-------------------------------------------------------------------
plt.axis([minx,maxx,miny,maxy])	
plt.show()
#-------------------------------------------------------------------

