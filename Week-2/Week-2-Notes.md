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
- 
