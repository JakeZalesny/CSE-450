# Artificial Neural Networks
- Deep Learning, subset of Machine Learning. 
- Neurons and Synapses
- Synapses connect neurons 
- Neurons are organized into layers. 
- Connections between neurons control how important decisions are. The stronger the connection, the stronger the importance. 
- Strength of connections = Weights. 
- Wx * x + Wy *y + b = 0 Equation for a line. 
- Wx * x + Wy * y + Wz * z + b = 0 Equation for a plane. 
- Normal vector is the individual component separated and put in the opposite space. 

1. Input into Neural Network, it spits out garbage answer 
2. Calculate loss comparing the input vs the actual (the error)

- Apple vector - Banana vector = Normal Vector. 

- We take a weighted summation (plane, line, etc.) and pass it into a non linear function (a greater than or lest than) that's an activation. 
- Sigmoidal Logistic Activiation, it's like a tangent rotated on it's side. 

Step by step. 

1. Pass point [x, y, z] into neuron 1 which multiplies it's weights [wx, wy, wz] then pass [x, y, z] to neuron 2 which multiplies it by it's own [wx, wy, wz] 

2. This outputs a whole nother matrix

3. In between plugging it into another neuron you have to do a nonlinear activation function so it bends a bit. 


 ^ It's matrix multiplication, this is essentially all linear algebra. 
Parentheses represent nonlinear activation function 

([x1] * [w1]) * ([w2]) * ([w3]) ... * ([wn])

- Going through a whole dataset is called an Epoch
- 
