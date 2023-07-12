import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the artificial neuron class
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    
    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

# Define the AND gate using an artificial neuron
and_gate_weights = np.array([1, 1])
and_gate_bias = -1.5
and_gate_neuron = Neuron(and_gate_weights, and_gate_bias)

# Define the OR gate using an artificial neuron
or_gate_weights = np.array([1, 1])
or_gate_bias = -0.5
or_gate_neuron = Neuron(or_gate_weights, or_gate_bias)

# Define the NOT gate using an artificial neuron
not_gate_weights = np.array([-1])
not_gate_bias = 0.5
not_gate_neuron = Neuron(not_gate_weights, not_gate_bias)

# Test the gates
input1 = 0
input2 = 1

and_result = and_gate_neuron.feedforward(np.array([input1, input2]))
or_result = or_gate_neuron.feedforward(np.array([input1, input2]))
not_result = not_gate_neuron.feedforward(np.array([input1]))

print(f"AND Gate: {input1} AND {input2} = {and_result}")
print(f"OR Gate: {input1} OR {input2} = {or_result}")
print(f"NOT Gate: NOT {input1} = {not_result}")

#Footer
print("Question no.6")
print("Name: Saroj Pokharel ")
print("Roll no : 26 ")
print("Section:A")