# Gradient Boosted Trees
- Gradient ~= Slope
- Why different trees? Different perspectives and different features. 

## Subspace Sampling: 
Each tree looks at different features, same data. 

(This isn't subspace sampling below)
- Make the trees different from each other. Different rows of the data, different features. 
- Each tree will have different outliers. 

## Sampling with Replacement. 
- Guarantees that there's a bit of overlap 
- Guarantees duplicates between trees, some might get the same as other trees so it lets us explore possibilites. 


## Bootstrapping: 
- Each model gets a different task. 
- Putting all the results together is called aggregating. 

## Bootstrap + Aggregating = Bagging
- Decision trees + Subspace Sampling + Bagging = Random Forest. 
- There's a way to make it better.
- Grab the samples that it got incorrect.
- Oversample the mistakes to make the next tree. 
- Repeat the oversampling. 
- This is what Gradient Boosted Trees are all about. 

### Error metrics: 
- Error is how far off the predicted value is from the actual value. 
- Its yi - y^i
- Squared error looks like a square on the graph with the actual value on the bottom left corner. 
- Squared error helps us pull things in. 
- Predicting the median reduces your absolute error. Doesn't always give us the best big picture. You're predicting for the Absolute Error
- if you predict for the Squared error, you'll predict towards the mean not the median. 
- Then get Root Mean Squared Error. 