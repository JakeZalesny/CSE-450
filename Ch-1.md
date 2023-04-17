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
