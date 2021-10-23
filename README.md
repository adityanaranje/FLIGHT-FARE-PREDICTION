<p align="center" >
    PERSONAL PROJECT
  </p>

# Project Title : FLIGHT FARE PREDICTION
# Technologies : Machine Learning (XGBoost)
# Domain : Transport


## Problem Statement:
* Create a maching learning model to predict the flight fare and deploy it.


## Aim/Goal :
* To create an end to end api for prediction of flight fare using regression.

## Approach :
* Performs basic machine learning operations like data collection, data transformation , data cleaning, feature extraction, feature scaling , feature selection and model training on dataset. 

## Dataset
* The data set consists of csv file.. Get dataset from [Here](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)





## Tools Used:
  * Python 
  * Pandas
  * Numpy
  * Sklearn
  * Flask
  * Pickle
  * HTML
  * Heroku




## Platforms Used:
*  Jupyter Notebook
*  VS Code
*  Github
*  Heroku


## What is regression?
* Regression analysis is a statistical method that helps us to analyze and understand the relationship between two or more variables of interest. The process that is adapted to perform regression analysis helps to understand which factors are important, which factors can be ignored, and how they are influencing each other.

* Regression consists of two main terms:
  * Dependent Variable: This is the variable that we are trying to understand or forecast/predict.
  * Independent Variable: These are factors that influence the analysis or target variable and provide us with information regarding the relationship of the variables with the target variable.

## What is XGBOOST?
* XGBoost is an ensemble learning method. Sometimes, it may not be sufficient to rely upon the results of just one machine learning model. Ensemble learning offers a systematic solution to combine the predictive power of multiple learners. The resultant is a single model which gives the aggregated output from several models. The models that form the ensemble, also known as base learners, could be either from the same learning algorithm or different learning algorithms. Bagging and boosting are two widely used ensemble learners. Though these two techniques can be used with several statistical models, the most predominant usage has been with decision trees.
 
* Bagging
  * While decision trees are one of the most easily interpretable models, they exhibit highly variable behavior. Consider a single training dataset that we randomly split into two parts. Now, let’s use each part to train a decision tree in order to obtain two models. When we fit both these models, they would yield different results. Decision trees are said to be associated with high variance due to this behavior. Bagging or boosting aggregation helps to reduce the variance in any learner. Several decision trees which are generated in parallel, form the base learners of bagging technique. Data sampled with replacement is fed to these learners for training. The final prediction is the averaged output from all the learners.

* Boosting
  * In boosting, the trees are built sequentially such that each subsequent tree aims to reduce the errors of the previous tree. Each tree learns from its predecessors and updates the residual errors. Hence, the tree that grows next in the sequence will learn from an updated version of the residuals. The base learners in boosting are weak learners in which the bias is high, and the predictive power is just a tad better than random guessing. Each of these weak learners contributes some vital information for prediction, enabling the boosting technique to produce a strong learner by effectively combining these weak learners. The final strong learner brings down both the bias and the variance. In contrast to bagging techniques like Random Forest, in which trees are grown to their maximum extent, boosting makes use of trees with fewer splits. Such small trees, which are not very deep, are highly interpretable. Parameters like the number of trees or iterations, the rate at which the gradient boosting learns, and the depth of the tree, could be optimally selected through validation techniques like k-fold cross validation. Having a large number of trees might lead to overfitting. So, it is necessary to carefully choose the stopping criteria for boosting. - AnalyticsVidhya


* Steps Performed
  * Data Collection
  * Data Preprocessing 
  * Data Cleaning
  * Feature Engineering
  * Feature Selection
  * Feature Scaling
  * Model Training
  * Model Evaluation
  * Model Deployment


* Python Version Used
  > Python 3.8.8
* Libraries Used

  * `numpy 1.20.1`
  * `pandas 1.2.4`
  * `pickle-mixin 1.0.2`
  * `scikit-learn 0.24.1`
  * `flask 1.1.2`
  * `xgboost 1.50.0`

* Install Libraries Using
  > pip install library_name

* or For anaconda
  > conda install library_name


## Deployment Link
### Click [Here](https://flight-fare-prediction-an.herokuapp.com/)


## User Interface

![](https://github.com/adityanaranje/FLIGHT-FARE-PREDICTION/blob/main/static/flight.jpg)
