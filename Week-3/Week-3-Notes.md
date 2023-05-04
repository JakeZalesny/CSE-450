# Week 3 Notes: 
- The questions that we ask are key to building a model. 
- A question that splits the game into a smaller set and a large set is much better than an even two sets. 
- It's much more likely to get a smaller decision tree than a larger one. 

## Key Terms: 
- Entropy: Computational measure of impurity of the elements in a set. It's the uncertainty of guessing the result. 
- Information Gain.
- Decision Trees. The Prediction models we're trying to build. Carry out a series of tests to determine the qualitative features of the desired features in order to make a prediction. 
- Basically a series of yes or no questions or True or False questions. 
- Tree Nodes, Leaf Nodes, Branches
- Branches connect modes
- Leaf Nodes are nodes that are connected to the Root node by branches
- Rectangular leaf nodes are the final decision or sort. 
- A value with a low entropy value should map to a value with a high probability. 
- The log of a entropy does that trick 
- Binary Logarithm: Log base 2 of a probability [0,1]
- Large negative numbers for low probabilities. 
- Entropy is measured in bits. 

(P(t=i) x Log s(P(t=i)))
- It's important to find which feature pretty much determines a negative or positive every time and use that to indicate information gain. 
- Information Gain is the measure of informativeness a feature gives. 

1. Calculate the entropy. 
2. Partition
3. Calculate the partitioned entropy. 

## ID3 Algorithm. 
- Iterative Dichotomizer Algorithm. 
- Builds the tree in a depth first recursive manner. 
- Compute Information Gain of the descriptive features of a set. 
- ID3 uses the information gain metric to choose the best feature to test at each node of the tree. 

## CH 8
- Check 8.4.2.1 for Confusion rate calculations 

Training -> Validation -> Testing (Can't influence model)