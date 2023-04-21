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

# Reading 2 Notes: 
Quantitative Data: numbers 

Categorical Data: Comes from a finite set of possibilites. 

Ordinal Data: Numbers that come from a finite set of possibilities. 

## Heads up!
"Beware of categorical features that look like quantitative or ordinal features.

If students in our survey example live in three different apartment complexes, we might ask "Which apartment complex do you live in, 1, 2, or 3?".

Even though this is a numeric value, it's not an ordinal feature because there's no quantitative difference between the apartment complexes (living in building 2 isn't twice as important as living in building 1).

Later on, we'll see how to make sure our machine learning algorithms know that a feature really is a categorical feature, even when it uses numeric values."

## A.1 
### Central Tendency 
Arithmetic Mean: (Sample mean or Mean) is the best known measure of central tendency 

- You calculate it by calculating the average.
- The arithmetic mean is one measure of central tendency of a sample (a set of values)

Outlier: Unusually large or small value. 

- Means are very sensitive to Outliers, the data can be very easily skewed by outliers 
- Median is the value located in the middle. Be sure to organize your data from the smallest piece of data to the greatest. If the amount of values is even, then take the mean of the middle two 
- Mode: The most common occurring value in our data. 

### Most of Statistics / Analytics is about describing variation 

Variation: The differences in our data. How tightly the data clusters around the mean.

- The most easily calculated is Range: 
- Range for a feature 'a': range = max(a) - min(a)
- Range is very sensitive to outliers. 
- Variance is a whole lot more useful. 

Variance of this dataset would look like: 

Dataset: 192, 102, 145, 165, 126, 154, 122, 188 

Mean: 149.39

Calculation 

(192 - 149.39)^2 + (102 - 149.39)^2 +... (188 - 149.39)^2
_________________________________________________________
                            8 - 1

- Due to data being squared the units aren't in the original units, so it's not very informative. 


### The Standard Deviation is done by taking the square root of the variance. 

- Percentiles are another useful measure of variation. 
- To get the percentile of the n values of a, everything has to be in an ascending order. 
- Then multiply n by i (index) / 100 if the index is a whole number 
- if i isn't a whole number then we interpolate it as: 

ith percentile =  (1 - index_f) x a index_w + index_f + a index_w +1

index_w: Whole part of the index 
index_F: Fraction part of the index 
a index w: The value at a[w] 

## This is an example of calculating Percentiles: 

Dataset: 102, 122, 126, 145, 154, 165, 188, 192

25th Percentile: 25 ->i / 100 x 8 ->n = 2
SO the 25th Percentile = 122

80th Percentile: 80 ->i / 100 x 8 ->n = 6.4 

Because it's not a whole number we have to do this: 

a index w = 6

a index f = 0.4


(1 - 0.4 (a index_f)) x 165 (a index_w) + 0.4 (a index_f) x 188 (a index_w + 1)

### THE MEDIAN IS THE 50th PERCENTILE 

## Quartiles: 
- Another measure of variation is the inter-quartile range (IQR)
- Difference between the 25th percentile (lower quartile or 1st quartile) and the 75th percentile (upper quartile or 3rd quartile)

## A.2 Descriptive Statistics for Categorical Features
- The sections previously work well to describe quantitative features but not so well on categorical. 

### Frequency Counts and Proportions
- Frequency is how often a level pops up
- Proportion of a each level of a categorical feature is calculated by counting the number of times that level appears dividing by the sample size. Essentially Frequency / Sample Size 
- Frequencies and Proportions are represented in a frequency table 
- From a frequency table the mode can be calculated, given that the mode is just the most frequent level. 

## A.3 Populations and Samples 
- Population: All possible measurements or outcomes that are of interest to us in a particular study or piece of analysis. 
- Sample: The subset of the population that is selected for analysis. 
- 2,709 voters were taken out of 240,926,957 people. 
- Margin of error takes into account the fact that this is just a sample from a larger population. 
- The larger the sample the smaller the margin of error 
- In choosing a sample it's important that it be representative of the population. 
- If the sample isn't representative, the information may be called biased. 
- Using a simple random sample is the most straightforward way of avoiding biased samples 
- Population Parameters: Statistics that describe the population 
- Sample statistics are typically used for population parameters as estimates. 

### Population mean of a feature typically uses the sample mean as an estimate. 

### Population variance typically uses the sample variance as an estimate. 

### We say that an estimate is unbiased if it's variance, on average, equals that of population variance

## Chapter 3 Reading: 
- ABT Analytics Base Table. 
- Data Exploration is a key part in understanding the data that we have. 

We have 2 goals in Data Exploration: 
1. Fully understand the data
2. Determine if there are any Data Quality Issues 

### Data Quality Report: 
Includes tabular reports (one for continuous features and one for categorical features)

Included in Data Quality Reports:
- Central Tendency (Mean, Mode, Median) 
- Variation (Standard Deviation, Percentiles)
- Standard Data Visualization plots (Bar Plots, Histograms, and Box Plots)

### Essential in Quality Reports: 
Quantitative Data (Continuous Features): 
1. Minimum 
2. 1st Quartile 
3. Mean
4. Median 
5. 3rd Quartile
6. Max 
7. Standard Deviation
8. Total number of instances in the ABT 
9. The percentages of instances in the ABT that are missing a value for each feature 
10. The cardinality of each feature. (Cardinality is the distinct features present.) 

Categorical Data: 
1. Row for each feature in the ABT that contains the 2 most frequent levels (Mode and 2nd Mode) 
2. Frequency that the levels above appear (Raw frequencies and proportions)
3. Percentage of instances that are missing a value for the feature 
4. Cardinality of the feature. 

Histogram for each continuous feature. For continuous features with a cardinality of less than 10, use a bar plot. 

# Day 2 Notes: 
Distribution: How spread out the data is. 

In Variance if you're doing the whole population you divide by n and not n-1. 

Why do we square everything on top in variance? 

- It's like the difference between speed and acceleration. 
- Because were talking about how much something is changing, we go a layer deeper and have a squared in the equation. 

Dice Distribution Example: 

For one dice, we have an equal probability of getting each number so it's uniform distribution (a constant on the graph)

36 options for 2 die, if you make a matrix of all the options, 7 is the most likely for you to get. 
Top of the distribution is the mean, the width is the variance. 

There's variance in every dimension, so in 3D you'll get something like a "Bell Hill" 