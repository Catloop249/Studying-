#inputs : array of number 
#index in array
import math;
def binarysearch(inputs,x):
	
	r = len(inputs);
	p=1;		
	while(p<=r):
		q = int((p+r)/2);
		if(inputs[q] == x):
			return q;
		elif (x != inputs[q]):
			if(x<inputs[q]):				
				r=q-1;
			elif (x>inputs[q]):
				p=q+1;
	return -1;
def binarysearchrecursive(inputs,left,right,x):
	result = 0;		
	mid = math.floor((left+right)/2);
	if(left == right):
		return -1;
	# print ("mid:",mid);
	# print ("inputmid:",inputs[mid]);
	# print ("x:",x);
	# print ("left:",left);
	# print ("right:",right);
	if(inputs[mid] == x):		
		return mid;
	elif ( x > inputs[mid]):
		return binarysearchrecursive(inputs,mid+1,right,x);
	elif( x < inputs[mid]):
		return binarysearchrecursive(inputs,0,mid,x);

	
def sort(inputs):	
	#start at 1
	for i in range(2,len(inputs)):
		j = i -1;
		key = inputs[i];
		#repeat	
		while (j > -1 and key< inputs[j]) :
			inputs[j+1] = inputs[j];
			j = j-1;
		inputs[j+1] = key;
	return inputs;
inputs = sort([2,6,8,1,3,4,12,13,56,78,9]);
print ("sorted:",inputs);
print ("length:",len(inputs));
test= binarysearchrecursive(inputs,1,len(inputs),12);
# test = sort([2,6,8,1,2,3,4,12,13,56,78,9]);
# print ("sorted:",test);

if(test > -1):	
	print ("my index:", test);
else:
	print ("not found:",test);


