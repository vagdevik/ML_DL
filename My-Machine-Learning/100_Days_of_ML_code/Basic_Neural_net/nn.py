import numpy as np

def sigmoid(x):
	return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
	return x*(1-x)


np.random.seed(0)	
#input
X = np.array([[1,0,0],[0,0,1],[0,1,0],[1,0,1],[1,1,1]])
Y = np.array([[1],[0],[0],[1],[1]])

	
#initialize neurons and learning rate 
input_neurons = X.shape[1] #number of features in data set
first_hidden_neurons = 4
second_hidden_neurons = 1	
alpha = 0.5

#initialize synapses weights and biases 
syn_w0 = np.random.rand(input_neurons,first_hidden_neurons)
syn_w1 = np.random.rand(first_hidden_neurons,second_hidden_neurons)
b0 = np.random.rand(1,first_hidden_neurons)
b1 = np.random.rand(1,second_hidden_neurons)
	
for i in range(2000):
	
	#forward propagation	
	#activations
	net0 = np.dot(X,syn_w0) + b0 
	out0 = sigmoid(net0)
	net1 = np.dot(out0,syn_w1) + b1
	out1 = sigmoid(net1)
	#total error
	E_total = (1/np.floor(2))*np.square(Y-out1)
	if(i%100==0):
		print "Error at epoch "+str(i)+" :"
		print np.sum(np.square((Y-E_total)))
		print "______________"
	
	#backward propagation
	E = -(Y-out1)
	delta_output = E*derivative_sigmoid(out1)
	delta_hidden = delta_output.dot(syn_w1.T)*derivative_sigmoid(out0)
	syn_w1 = syn_w1 - (out1.T.dot(delta_output)*alpha)
	syn_w0 = syn_w0 - X.T.dot(delta_hidden)*alpha
	b1 = b1 - np.sum(delta_output)*alpha
	b0 = b0 - np.sum(delta_hidden)*alpha
print out1
