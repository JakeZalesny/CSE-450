# Chapter 1 Notes: 
- Google came with a tool called Bard. Bard is ChatGPT with internet. 
- The big thing in the last two weeks: Teaching Large Language Models to Self-Debug. 
- It creates a self-feedback loop to run and debug with a master GPT getting smaller GPTS to do a task and then return and report. 
- If you have some data you can predict other data. It's a regression problem, picking a number based on another number. 
- Classification Task: Predict a category 
- Regression Task: Predict a number
- Generation Task: Produce something

## Helpful stuff for Assignments: 
- Data exists in dimensions
- 2D (X, Y), 3D (X, Y, Z)
- It's hard to visualize a 4D space.
- Concepts that apply in 2D spaces apply in 3D. 
- Decision Boundary: A line in a graph that helps us determine what category the data falls into. 

# Reading 1 Notes
Three Main Types of Learning: 

1. Reinforcement Learning
2. Unsupervised Learning
3. Supervised Learning

## Reinforcement Learning
- What most people think of when they think of AI 
- Train robots to respond to varying environmental factors in order to achieve a goal. 

## Unsupervised Learning 
- Uses a technique called cluster analysis, is an algorithm that determines which group would most likely respond to an action

- Dimensional Reduction: Aggregate groups by response patterns 
- Both of these are examples of unsupervised learning

## Supervised Learning
### Example: 
- Working with pre-analyzed data, it's like setting up a testing environment. 
- Attributes of each sample or instance of data are called Predictors, independent variables or features. 
- Response Variable: Essentially the test case that we are testing for, if we were looking for fraudulent purchases, it would be a fraudulent purchase. 

### Formal Definition: 
Supervised learning algorithms use labeled training data, (data that starts with known values for the target variable) to generate models that relate the features to the target.

More formally, given:

An 
n x m matrix, of 
X, where 
n is the number of samples, and 
m is the number of features

A vector of 
n target values, 
y
A supervised learning algorithm is one that "fits" 
X to 
y to create a model capable of predicting the target values of new samples.

- The whole point of these models is to accurately predict the future. 

## Regression and Classification: 
- Regression: Generate a number result
- Classification: Generate a categorical result

Examples of Regression: 

- Predicting the likelihood that someone will contract a disease
- Calculating the value of a house
- Predicting a student's most likely GPA based on their ACT scores

Examples of Classification: 

- Facial recognition software
- Fraud detection
- Disease diagnosis
- Text recognition

### Numeric vs. Categorical Features:
- A numeric feature can take on the range of the following quantitative values: Xmin <= X <= Xmax
- A categorical feature would be something like, what grade a student is in. It's essentailly a qualitative feature over quantitative. 

# Day 1 Notes
Tasks / Problems: 
1. Classification
2. Regression
3. Generation

Learning Methods: 
1. Supervised: Train model on data that we have the answers to so that when data comes in that we don't have the answers to, it knows it. 
2. Unsupervised: Use an algorithm to find answers / trends in data. You really have to focus on using the right algorithm to make sure that the data extracted is grouped well. 
3. Reinforcement Learning: It's a reward system essentially. The model does the right thing and it gets a positive reward. ITS NOT A SERIES OF IF ELSE, you let it explore and then in the feedback let it know if what it's doing is helping or hurting. 


Models: 
1. Decision Trees 
2. Neural Networks -> This is the big one, has been for about 5-6 years, essentially advanced Decision Trees. 
- Transformers are models essentially. 

Algorithms: 
1. Back Propogation
2. Spike Time Dependent Plasticity 
- Algorithms in this context: How are we changing the parameters of the model


- NVIDIA came out with a text to video. 

### AI vs. Machine Learning
Lots of facets of AI, Machine Learning is a facet of AI. 
- Machine Learning: Learn to manipulate data from a dataset. 
- Deep Learning: Deep neural networks. 
- The universe is not deterministic, even if you understood every single atom in the universe, you still wouldn't know what happens next perfectly, just because there's always an element of randomness. 
- Agency could be the act of allowing the quantum particles collapsing. You can't observe one single quantum particle. 

### Ensemble Learning:
- Different models that learn different ways and they correct each other. 