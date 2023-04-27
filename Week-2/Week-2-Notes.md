# Reading 2 Notes
## Advanced Data Exploration
- How to examine pairs of features 
- Scatter plots are key for analyzing relationships 
### Positively Covariant Features: 
- A strong positive colinear relationship between two features, Ex. Height and Weight. 
- A SPLOM (Scatter Plot Matrix) Shows scatter plots for a whole collection of features arranged into a matrix. This is useful for exploring the relationships between groups of features. 
- The effectiveness of SPLOMs is diminshed once we start getting past 8 features... The graph gets too small. 

### Categorical Features: 
- Use Small Multiples visualization. It's a bunch of bar plots. 
- If there's a strong relationship, the Bar Plots will look noticeably different.
- If there's no relationship, there will be an even distribution of the levels. 
- If there are only 3 levels or less being compared, stacked bar plots are not a bad idea to use. 

# Visualization between Categorical and Continuous features: 
- The best way to do it is through small multiples. 
- If the features are unrelated, the graphs will be the same
- If the features are related, the graphs will be different. 
- Histograms show more details of a relationship between two features. 

### Covariance and how it's calculated: 
- It's calculated the same as variance it just has the the a feature x the b feature instead of just the a feature. 
- Negative values infer a negative relationship, and positive values infer a positive relationship. 
- Correlation = Cov(a, b) / sd(a) x sd(b)
- Correlation, due to it being normalized is dimensionless, so it doesn't get the same interpretability issues that Covariance has. 
- If there's no correlation the features are independence. 
- SPLOMs are really a visualization of the Correlation Matrixes. 
- It's important to note, correlation is just a number and there can be very different relationships 
- Correlation != Causation
- Confounding feature: it's basically a poor assumption that that stems from a lack of bad context and poor research. Essentially pulling things out of the context and claiming the isolated environment is a real life situation.  

# Data preparation
- Two main techniques of Data preparation
1. Binning
2. Normalization

## Normalization: 
- Normalization techniques can be used to change a continuous feature to fall within a specified range while maintaining the relative differences between the values for the feature.
- Range normalization is the simplest approach to normalization

a'i = ((ai - min(a))/(max(a) - min(a))) x (high - low) + low

- Range Normalization is extremely sensitive to outliers 
- Standardizing data is another way to normalize something. 

a' = (ai - a~) / sd(a)

## Binning: 
- Converting a continuous feature into a categorical feature. 
- Define a series of ranges called bins. 
- Equal-width binning and Equal-frequency binning 
- Low bin numbers will cause us to lose a lot of data. 
- However this has a large number of instances in each bin. 
- Higher bin amounts => more correlation to actual data. 

### Equal-Width Binning: 
- Simple and intuitive, Some bins are going to have very few values in them. 
- The closer to the mean you get the more instances per bin you will have. 

### Equal-Frequency Binning: 
- Sorts everything into ascending values 
- Equal number of instances per bin. 

## Sampling: 
- Top Sampling: Select the top 5% of instances from a dataset. Running a huge risk of introducing bias. 
- Random Sampling: Randomly selects a proportion of 5% 
- Stratified sampling is a sampling method that ensures that the relative frequencies of the levels of a specific stratification feature are maintained in the sampled dataset.
- If we want to make sure that the data is distributed equally, we'll use Under-Sampling or Over-Sampling. 
- The number of instances in the smallest group is the under-sampling group 
- Under and Over sampling is essentially stacking the instances of a certain group and modifying the samples taken whether they be in the largest group or the smallest and making sure that there's equal representation. 

# Day 3 Notes:
- We have 4 categories need them to be numbers 
- We can assign them to number values arbitrarily 
- Binary data comes in 'n' dimensions, 4 categories, 4 dimensions. 
- Make a split in the space. 
- You can always split up a dimension with a smaller dimension. 
- A hyperspace is a large amount of dimensions, can be split with a hyperplane. 100 dimension hyperspace, 99 dimension hyperplane. 

Population: Big group of something -> Set or Dataset in Machine Learning

Sample: a group of the population in Statistics
Sample in Machine Learning is one singular Data Point.

Predictor: One of the columns in Statistics in Machine Learning its a feature. 

Target: What we're trying to get, in Statistics it's response variable. 

- To visualize something we flatten them. 
- Different Perspectives of the same space can help you split up the data. 

# Reading 2
## Similarity Based Learning
- Best way to make predictions is to look at what has worked well in the past and predict the same thing. 

### Fundamental Concepts: 
1. Feature Spaces
2. Measures of Similarity
3. The Nearest Neighbor Algorithm
k -> Nearest Neighbor 

Built to handle features with measures of similarity. 
Introduce Data Normalization and Feature Selection. 

## Fundamentals: 
- We have to compute the distance between instances 
- If we're going to do this we need to have a concept of space 
### Feature Space: 
- If we have the Speed and Agility of athletes, we need to put that into the Feature Space. 
- This is done by taking each of the Descriptive Features and putting them into the axes of a coordinate system. 
- Each Descriptive feature is a dimension. 
- The distance of two points is a useful measure of similarity between these two entities. 
### Distance Metrics: 
1. Non-Negativity: metric(a, b) >= 0 
2. Identity: metric(a, b) <==> a = b
3. Symmetry: metric(a, b) = metric(b, a)
4. Triangular Inequality: metric(a, b) <= metric(a, c) + metric(b, c)
- One of the best known Distance Metrics is Euclidean Distance
- Euclidean is the length of a straight line between two points: 

sqrt(a[i]-b[i])

- Manhattan Distance: 

ABS(a[i] - b[i])

- Minkowski Difference between two instances a and b is as follows: 

(ABS(a[i] - b[i])^P)^1/P

- Euclidian Difference is influence a lot more by one large feature that's much different than a bunch of small differences. 

## Standard Approach: 
- Put the last two sections together: A place to put/visualize the data (A feature space representation) and A measure of the similarity between the features. 
- This involves primarily, storing all of the training instances in memory. 
- When running the Nearest Neighbor algorithm, it partions the data into what's know as the Voronoi Tesselation. The algorithm then tries to decide which Voronoi region the query feature responds to. 
- The algorithm creates a set of local models, or neighborhoods, accross the feature space, each model is defined by a subset of the set of data. 
- The algorithm also implicitly creates a global prediction model. 
- Advantage of Nearest Neighbor approach: Straightforward updating process to the model. 

## Handling noisy data: 
- Noise: Fallacy or error in the data collected. 
- If there's any noise in the data it'll throw off the predictions. 
- Kronecker delta function. It essentially goes through all the data and calculates the distance from the query instance. It returns 1 if the distances are equal 0 otherwise. 
- k in the equation for it, is how many of the nearest instances are we using. 
- If we set it too low, the algorithm can potentially be sensitive to noise in the data.
- If we set it too high, we run the risk of losing the true pattern of the data. 
- This risk only increases if we have an inbalanced data set where there's more of one type of data than another. 
- When we have inbalanced datasets we can use a weighted nearest neighbor algorithm. 
### Weighted Nearest Neighbor: 
- Essentially set k to a higher value and let it handle itself. 
- One way to counterbalance the tendency of taking into account things that are too far away, is to use a distance weighted k nearest neighbor approach. 
- The easiest way to implement this is to weigh each neighbor by the following: 
(1 / (dist(q,d))^2) 
- If we weight everything we can set the k = the size of the data set and it will be immensely accurate. 

## Efficient Memory Searches. 
- Computing the weight of something is taxing. 
- We need to make a k-d tree or a Binary Tree. 
- Split the tree at the median value. 
- Recursively split each of the two new partitions. 
- The recursion only stops when there are less than two instances in the partition 

## Data Normalization
- If we have a value that is much larger in a feature, that feature will dominate (Ex. Age vs. Salary)
- Range normalization is going to be key to solve this predicament. 
- It will put everything on a [0,1] range. 

## Evaluation
- We need to make sure that our experiments are designed to produce completely appropriate results. 
- Situational Accuracy is absolutely key. You would want a Healthcare AI model to be much more accurate than a prediction model for a marketing agency. 

## Standard Approach: Missclassification Rate on a Hold-Out Test Set
- Performance measure on a test set: Basically we know the results already and we're testing to see if the machine gets them right. 
- Hold-Out Test Set: Is a random sample of the ABT we create in the Data Preparation phase. 
- This isn't used in the training phase. 
- This is essentially supervised learning. 
 ### Missclassification rate: Number of incorrect predictions / total predictions

- Confusion Matrix: Calculates the frequencies of each possible outcome of the predictions made by a model for a test dataset in order to show, in detail, how the model is performing.
 
Four possible outcomes in the confusion matrix
1. True Positive
2. True Negative
3. False Positive
4. False Negative

### Classification accuracy = Correct Guesses / Total Guesses

## Designing Evaluation Experiments 
- Hold-Out Sampling is sometimes extended to include a third set or a validation set. 

### k-fold Cross Validation
- Avoids lucky splits and data availability issues. 
- Available data is folded into equal sized folds. 

1st Fold is the Test Set 
The remaining data in the k - 1 folds is the training set. 
2nd Fold is the 2nd evaluation experiment 
This is done the same way as the 1st fold.

### Leave-one-out cross validation or Jacknifing
- Each fold of the test only comes out once. 
- Really good for small amounts of data 

### Bootstrapping
- Preferred for very small data sets. 
(less than 300 instances)
- It's like k-fold cross with more folds


### Out-of-time sampling
- If we have a time dimension included, we can use this method. 

# Day 2: 
- K-values
- Underfitting & Overfitting Review

Overfitting: The decision boundary fits too good to the model and causes problems. It essentially caters to the outliers. 

Training Set -> Build Model

Validation Set -> Tweak Model 

Testing Set -> Determine Accuracy

Validation Set influences Model, can't report that accuracy. 

K-Nearest Neighbor
K is the amount closest neighbors

Precision: Predicted Yes, how many were correct. 

Recall: True Yes, out of the people that were yes, how many did I guess right. 

### REREAD F-1 Score