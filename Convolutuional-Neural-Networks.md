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