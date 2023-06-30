# Convolutional Neural Networks:
- Dense Layers, receive inputs from each previous neurons.
- Convolutional Layers are different. 
- Dense Layers calculate by dot products. 
- Vector: Point with direction and magnitude. OH yeah! 
- |Vector1| * |Vector2| * cos(angle)
- Cosign is biggest when the angle is the smallest. 
- The closer together they are the bigger they are. 
- MNIST Dataset is simething to test.

### Actual Convolutional stuff
- Different neurons are going to look at different spots in the neuron 
- Set of neurons look for the same thing in different spots to prevent overfitting. 
- Filter or Kernel, it's like the weighting over each section of the image. 
- Moving the kernal around is called a convolution. 
- It produces a feature map. 
- Window is what you apply it to. 
- Numeric values telling you how strong a pixel value is -> Feature map 
- Feature map is essentially a heat map. 
- Padding = one extra pixel on each corner. 
- Stride is how many pixels you move by.  
- Pooling / Downscaling
- We increase the complexity of things up until the end and then decrease the specificity of the locations of the pixels until the end. 

# 2.1 Theory
### Image Recognition: 
- Treat the image as a [Size here] array of pixel values. 
- The neurons correspond with the size of the array 
### Brute Force Idea 1: 
- Search with a sliding window. 

### Brute Force Idea 2: 
- More data and deeper neural network. 

### Convolution:
- Humans recognize hierarchy in images that we see. 
- We don't have to relearn the idea of a child in every image that we see of a different child. 
- We need to give our network an idea of translation invariance. Essentially understanding what an image is. 

Convolution Step by Step: 
1. Break the image into overlapping tiles. 
2. Feed each tile into a small neural network. Twist: keep the same neural network weights for every single tile in the same original image 
3. Save the results from each tile in a new array
4. Downsampling. We use an algorithm called max pooling. Max pooling looks at a 2x2 of the array and keeps the biggest number 
5. Make a prediction. We send that pool into a small neural network. This final neural network is called a fully-connected neural network. 

- We can stack any of those steps as many times as we want in order to enhance our precision. 
- More convolution steps = more likely your network will get the more complicated features. 
- A realistic Convoluted Network has multiple layers of math pooling. 
- Having more data is more important than having a better model. 
- Not all mistakes are created equal. 
- Precision: If we predicted 'yes' how many times was it really a yes? 
- Recall: Out of all the actual yes' did we get? 


## MIT Lecture Notes: 
- Images are just numbers to a computer 
- Regression & Classification both exist in Computer Vision. 
- It needs to understand the uniqueness of features between images. 

```py
from tensor-flow import keras

tf.keras.layers.Conv2D(filters=d, kernel_size=(h,w), strides =s)
```

- pooling reduces dimensionality. 
- Input -> Convolution & Relu -> Pooling -> Convolution & Relu -> Pooling... repeat as many times as necessary 
- classification: Flatten -> fully-connected -> softmax