# Deep Learning:

### Why? 
 - Hard engineering stuff is a bit more brittle. 
 - Getting underlying features from data. 

 ### Forward Propogation. 
 Inputs: x0 -> xN
 
 Weights: w0 -> wN
 
 Sum these, then pass through Non-Linear activation and we get y^ and add in the bias. 

 Sigmoid function: Any real number turns into a scalar number 

 Code examples: 

 ```python
 tf.math.sigmoid(z) 
 tf.math.tanh(z)
 tf.nn.relu(z)
 ``` 

 ### Non-Linear functions
 - Introduce nonlinearity into the network. 
 - Most data we have nowadays is nonlinear.

 ### Multi Output Perceptron
 - All inputs are connected to all outputs, these are known as dense layers. 

 ## Dense Layer implementation: 

 ```py
 class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, input_dim, output_dim):
        super(MyDenseLayer, self).__init__()

        self.W = self.add_weight([input_dim, output_dim])
        self.b = self.add_weight([1, output_dim]) 
    
    def call(self, inputs): 
        z = tf.matmul(inputs, self.W) + self.b
        output = tf.math.sigmoid(z)
        return output
```

```py 
import tensorflow as tf 
layer = tf.layers.Dense(units = 2)
```

- Hidden layers exist too. Single input into single output. 

Implementation: 
```py
model = tf.keras.Sequential([ 
    tf.keras.layers.Dense(n),
    tf.keras.layers.Dense(2)
])
```
Deep networks have multiple versions of this, here's what that looks like: 

```py 
model = tf.keras.Sequential([ 
    tf.keras.layers.Dense(n),
    tf.keras.layers.Dense(n2),
    ..., 
    tf.keras.layers.Dense(2)
])

```

## How to teach a Neural Network: 
- It's essentially a baby. You have to define right and wrong. 
- This process is called quantifying loss. You do this by comparing it to the actual answer. 
- This is how you do it in code. 

This is specifically for binary classification (yes or no)
```py 
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, predicted))

```

MSE loss: 
```py 
loss = tf.reduce_mean(tf.square(tf.subtract(y, predicted)))
```

- We want to find the ones with the least amount of loss. 
- Gradient Descent is how we find the lowest loss (local minimum)

Here's how it looks in code: 
```py 

weights = tf.Variable([tf.random.normal()])

while True: 
    with tf.GradientTape() as g: 
        loss = compute_loss(weights)
        gradient = g.gradient(loss, weights)
    
    weights = weights - lr * gradient

```

### Back-Propogation
- How does a small change in a weight effect the total loss? 
- Chain rule 
- Setting the learning rate is the hardest part, you have 2 objectives: 
1. Don't get stuck in local minima 
2. Don't overshoot and diverge. 
- Adaptive Learning rates: 

```py 
tf.keras.optimizers.SGD
tf.keras.optimizers.Adam
tf.keras.optimizers.Adadelta
tf.keras.optimizers.Adagrad
tf.keras.optimizers.RMSProp
```

^ Try these out, they can be pretty problem dependent. 
SGD is the vanilla gradient descent

Putting it all together: 

```py 
import tensorflow as tf

model = tf.keras.Sequential([...])
optimizer = tf.keras.optimizers.SGD

while True: 
    prediction = model(x)
    with tf.GradientTape() as g: 
        loss = compute_loss(y, prediction)
        grads = tape.gradient(loss, model.trainable_values)
        optimizer.apply_gradients(zip(grads, model.trainable_values))
```

### Regularization
1. Dropout, randomly make a hidden neuron equal to zero. 50% of it's memory will be wiped out. This is really good at generalizing to test data. 
2. Early stopping, stop before the chance we have to overfit. 


### Extra Activation Notes: 
- The greater the number of activation that the neuron contains the greater the chance that it's that neuron if that makes sense 
- Bias is basically tells you how high the neuron needs to be for it to be active.
### Sigmoid is old school, reLU is way more used!

### Further Loss notes
- If you figure out the slope of where you are at any given point you can figure out which way to step. It's calculus. 
- Local Minimum is pretty easy to find. 
- Global is a lot more difficult. 
