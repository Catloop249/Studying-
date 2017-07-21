def mergesort(inputs):	
	left = inputs[];
	right = inputs[];
	mergesort(left);
	mergesort(right);
	merge();
def merge(left,right):
	for i in range(len(left)):
		for j in range(len(right)):
			
