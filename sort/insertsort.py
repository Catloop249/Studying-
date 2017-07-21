def insertionsort(inputs):	
	#start at 1
	for i in range(1,len(inputs)):
		j = i -1;
		key = inputs[i];
		#repeat	
		while (j > -1 and key< inputs[j]) :
			inputs[j+1] = inputs[j];
			j = j-1;
		inputs[j+1] = key;
	print ("my list:", inputs);
# vice versa
def insertionsort2(inputs):	
	#start at 1
	for i in range(1,len(inputs)):
		j = i -1;
		key = inputs[i];
		#repeat	
		while (j > -1 and key > inputs[j]) :
			inputs[j+1] = inputs[j];
			j = j-1;
		inputs[j+1] = key;
	print ("my list:", inputs);
# puesodo code of liner search
def search(v,inputs):
	for i in range(len(inputs)):
		if inputs[i] == v:
			index = i;
			break;
	print("index: ",index);		
insertionsort([3,7,2,8,1,0,9,4]);
insertionsort2([3,7,2,8,1,0,9,4]);
search(7,[3,7,2,8,1,0,9,4])