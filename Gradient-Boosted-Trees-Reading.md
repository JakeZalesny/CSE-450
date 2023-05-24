# Gradient Boosted Trees Reading

### Measures of Continuous Targets
- Sum of Squared Errors
- MSE Values have to be in the range [0, infinity]

### Model Ensemble: A group of models that all form into one model. 

### Group think: All the models have the same thought process leading to the same conclusions, which would be an issue. 

- Boosting: build multiple different models from the same dataset by inducing each model using a modified version of the dataset. (Essentially swaping the features)
- Bagging: Make a prediction by aggregating the predictions of the different models in the ensemble. For categorical target features, this can be done using different types of voting mechanisms, and for continuous target features, this can be done using a measure of the central tendency of the different model predictions, such as the mean or the median.

## Adaboost vs. Gradient Boost
- Adaboost builds on compensating for errors. 
- Stump = small tree. 
- First stump, builds off of this stump until it's done building or it has a perfect fit. The size each tree has to say in the model is how well it does compensating. 

- Gradient Boost builds a leaf initially. First leaf is the average value. 
- Builds a tree off of that based on the errors of that. 
- Does not build a stump. 
- Pseudo Residual = Observed Value - Predicted Value.
- Second tree is built to predict pseudoresiduals. 

## Building Trees. 
- If there are any multiple values at the ends, we replace them with their averages. 
- Uses a learning rate also to scale the contribution from the tree. 
- This results in a small step in the right direction. 

## Regression Details. 
- Loss Function: How well we can predict weight. 
- Most common equation: 1/2(Observed - Predicted)^2
- Loss function is just a squared residual, forget the 1/2
- Sum of squared residuals, whichever is smaller fits the data better. 

Step 1: Initialize the Model with a constant value. The constant is always the average of the observed values. 
Step 2: Make M trees. M = all trees, m = individual trees. 

- Derivative of the Loss function = -(Observation - Prediction)
2a. (Observation - Prediction) -> (Observation - Average)
2b. Get the residuals for each observed value. 
2c. Add it to the average 
