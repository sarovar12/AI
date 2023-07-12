import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize the weights with random values
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        
        # Initialize the biases with zeros
        self.bias1 = np.zeros((1, self.hidden_size))
        self.bias2 = np.zeros((1, self.output_size))
    
    def feedforward(self, X):
        # Compute the output of the neural network
        self.hidden_layer = sigmoid(np.dot(X, self.weights1) + self.bias1)
        self.output_layer = sigmoid(np.dot(self.hidden_layer, self.weights2) + self.bias2)
        return self.output_layer
    
    def backpropagation(self, X, y, learning_rate):
        # Compute the gradients
        output_error = y - self.output_layer
        output_delta = output_error * sigmoid_derivative(self.output_layer)
        
        hidden_error = np.dot(output_delta, self.weights2.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer)
        
        # Update the weights and biases
        self.weights2 += learning_rate * np.dot(self.hidden_layer.T, output_delta)
        self.weights1 += learning_rate * np.dot(X.T, hidden_delta)
        
        self.bias2 += learning_rate * np.sum(output_delta, axis=0)
        self.bias1 += learning_rate * np.sum(hidden_delta, axis=0)
    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward pass
            output = self.feedforward(X)
            
            # Backward pass
            self.backpropagation(X, y, learning_rate)
            
            # Compute and print the loss (mean squared error)
            loss = np.mean(np.square(y - output))
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")


# Example usage
# Define the input data and labels
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a neural network with 2 input units, 2 hidden units, and 1 output unit
network = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Train the neural network
network.train(X, y, epochs=10000, learning_rate=0.1)

# Test the trained network
output = network.feedforward(X)
print("Predictions:")
print(output)

#Footer
print("Question no.7")
print("Name: Saroj Pokharel ")
print("Roll no : 26 ")
print("Section:A")