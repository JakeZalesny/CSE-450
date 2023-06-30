# Recurrent Neural Network Notes
- Instead of convolving through space, you convolve through time. You essentially go all the way back to the beginning of time. 
- The weights don't change throughout all of the neurons. 
- It's essentially averaging all of the gradients. 
- use tanh instead of relu, relu will let the values get too big. 
- Pretty much a game of madlib. 


1. Runs through a tanh activation 
2. Runs through sigmoidal to see whether or not it's useful or lot. 
3. Runs through sigmoidal to check it against old memory and forget potentially items of old memory. It's the forget gate
4. Update gate, if it needs to update the memory. 
5. It then runs new memory through ta tan and the input again through a sigmoidal function to determine the hidden input that will get fed back through the cell. 

The hidden input is short term memory, the long term memory is also present. 

When you back propagate through time, it only passes through the Tanh activation once, from then on out its only adding and multiplying. 

^ LSTM Cell

- One hot encoding is probably not where it's at. 
- integer labeling? A bit naive but can work. 
- 4 dimensional embedding. learns which networks are closer to each other. 


# Video Notes: 
- Sequences are all around us. Audio has it, text does: working with letters or words. 
- Can't really do a bag of words, because it doesn't handle preservation of time or space. 
- RNNs are really good for Many to One inputs to outputs relationships. 
- They're also really good for Many to Many input to output relationships. 

Recurrence Relation: ht (cell state) = fw(ht-1, xt)

### RNN intuition: 
```py 
myrnn = RNN() 
hidden_state = [0, 0, 0, 0]

sentence = ["I", "love", "recurrent", "neural"]

for word in sentence: 
    prediction, hidden_state = myrnn(hidden_state, word)

next_word = prediction
# >>> networks!
``` 
- Update the hidden state: using a tanh activation function. 

## Code Examples: 
```py 
class MyRNNCell(tf.keras.layers.Layer):
    def __init__(self, rnn_units, input_dim, output_dim):
        super(MyRNNCell, self).__init__()

        # Weight Matrices: 
        self.W_xh = self.add_weight([rnn_units, input_dim])
        self.W_hh = self.add_weight([rnn_units, rnn_units])
        self.W_hy = self.add_weight([output_dim, rnn_units])

        self.h = tf.zeros([rnn_units, 1])
    def call(self, x):
        
        # Update hidden state (aka update long term memory)
        self.h = tf.math.tanh(self.W_hh * self.hh * x)
        
        # compute output
        output = self.W_hy * self.h

        # Return the current output and hidden state
        return output, self.h
```
- Tensorflow implementation
```py
tf.keras.layers.SimpleRNN(rnn_units)
```

## Backpropagation Through Time
- How do we actually train the models for improvement? 

Backpropagations actual Algorithm: 
1. Take derivative (gradient) of the loss with respect to each weight parameter. 
2. Shift parameters over time

Essentially how this thing knows when it's wrong 

## Gradient calculations 
- Computing the Gradient wrt h0 involves many factors of Whh + repeated gradient computation

Many values > 1 = Exploding Gradients problem, gradients become too large and we can't optimize them. Fix this with Gradient Clipping to scale big gradients. 


Many values < 1 = Vanishing Gradients. Fix By: 
1. Activation Function 
2. Weight initialization 
3. Network Architecture. 


1. Activation function of ReLu has a higher derivative so vanishing gradient won't be an issue 

2. Initialize weights to identity matrix, initialize biases to zero. This helps prevent the weights from shrinking to zero. 

3. Most robust solution: Gated cells, they control what information is passed through. 


## LSTM: Long Short Term Memory Network

```py
tf.keras.layers.LSTM(num_units)
```

### How LSTMS work: 
1. Forget irrelevant information through multiplication of a sigmoidal function. 
2. Store by also multiplying a Sigmoidal function.
3. Update gets relevant parts of both past memory and  current memory 
4. Output, output gate controls what information is sent to the next step.  

LSTM Gradient flow: Allows uninterrupted Gradient Flow
from the furthest in time to the most ancient. 


# Questions for class: 
- LSTM, why do we determine on a sigmoidal basis whether or not something is included in memory. Wouldn't it be better to weigh the memory on something like a really small basis, so like normalize the derivative on a scale of [0, 1]? That way it wouldn't entirely forget something, it would weigh that memory and see if it's relevant on the off chance that something exactly like that situation occurs. 

```py
loss = tf.nn.softmax_cross_entropy_with_logits(y, predicted)
```
Input: sequence of words
Output: Probability of having positive sentiment