import sys
n,k=map(int,sys.stdin.readline().split())		#Test samples
mydict1={}
mydict2={}
string=[]
count1=0
count2=0
for x in range (0,n):
	string=input().split()
	dataset=string[0]
	del string[0]
	for token in string:
		if int(dataset)==1:
			count1=count1+1;
			if token in mydict1:
				mydict1[token]=mydict1[token]+1
			else:			#print "in 1"

				mydict1[token]=1
		else:
			count2=count2+1;
			if token in mydict2:
				mydict2[token]=mydict2[token]+1
			else:
				mydict2[token]=1

prob1=1.0
prob2=1.0
for y in range (0,k):
	s=input()
	string1=[]
	string1=s.split()
	for token in string1:
		total=0
		if token in mydict1:
			no_of_occurences1=mydict1[token]
		else:
			no_of_occurences1=0
		if token in mydict2:
			no_of_occurences2=mydict2[token]
		else:
			no_of_occurences2=0
		total=no_of_occurences1+no_of_occurences2;
		if total!=0 :
			prob1=prob1*(no_of_occurences1/total)
			prob2=prob2*(no_of_occurences2/total)
	prob1=prob1*(count1/n)
	prob2=prob2*(count2/n)
if (prob2>prob1):
	print ("2")
else:
	print ("1")
