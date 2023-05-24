# Post Notes
- Make a Vanilla tree and compare against that. 
- Pay attention to the one-hot encoding. You will run into issues of that. 
- Vanilla tree is basically running comparisons without modifying anything. 
- Compare against the vanilla model. 
- Use seaborn. 
- Data exploration needs to be much more in depth than what I did
- If the data's in chronological order you'll learn a lot more about it. 
- Map works with objects to
- from google.colab import drive 
- from
- If you ever oversample or undersample, do it after the train test split and only on the Test. 
 

1. Import all the libraries. 
2. Figure out which features are the best to use. 
3. Use several folds. Preferably 5 (test that bad boy 5 times) 
4. Run the metrics. Train Test and Validate data.  
5. Is it in the top 10% of the ones I've seen before. 


## For next time: 
- Model next time as quick as you can. 
- Get the context of the data as quick as you can. 
- Holdout on the vanilla tree immediately too. 
- Learn when to use which tool. 
- Deeper Data exploration. 

## Hyperparameters: 
- Number of trees & depth 
- 2 Hyper-parameters can test pretty much anything. 
- Hyperparameter Grid and Hyper Parameter Grid Search. 
- Checks all options. 
- Grid Search tools are super useful. It brute force searches pretty much all of the options. 
- Randomly search in different areas. Narrow it down by area. 
- Guided Hyperparameter Grid search. 

## Regression Task: 
- How wrong was I? 
- Absolute Error: Absolute value of subtracting the actual value and the predicted value. 
- Mean Abs. Error (MAE)
- Squared Error: Useful for the things that are really further away. It gives your model a higher penalty. Helps fit the model better. 
- Mean Sqd. Error. (MSE)
- (NOT IN THE ORIGINAL UNITS) Can't really eyeball it and tell if it's a good number. 
- Root MSE (RMSE)
- r^2 = 1 - (MSEmodel / MSEguessed or MSE(guessing the mean everytime))
- Don't be less than 0, 1 is perfect, 0 is guessing. 

