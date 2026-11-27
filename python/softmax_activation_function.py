import numpy as np

x1 = 2

x2 = [4.8,1.21,2.385]

x3 = [[4.8,1.21,2.385],
          [8.9,1.81,0.2],
          [1.41,1.051,0.026]]
          
#exp_value = np.exp(x3)

#print(x1)
#print()


#print(exp_value)
#print()

#sum = np.sum(exp_value,axis=1,keepdims=True)
#print(sum)

#norm_value = exp_value / sum
#print(norm_value)

#print(np.sum(norm_value,axis=1))


class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs-np.max(inputs, axis=1, keepdims=True))
        probabilities = exp.values / np.sum(exp_values,axis=1,keepdims=True)
        self.output = probabolities
        
activation = Activation_Softmax()
activation.forward(x3)