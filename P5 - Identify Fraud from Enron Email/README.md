# P5 - Identify Fraud from Enron Email

## Motivation

This work is part of the Udacity Data Analyst Nanoprogram. This is the final project for the Machine Learning course. The goal of this project is to use machine learning algorithms to build an efficient classifier that can spot PoI (Person of Interest) in the Enron Dataset provided by the Udacity team.

## Dataset

The dataset used in this project has been extracted by the Udacity team from the huge Enron dataset. The original Enron dataset contains data from about 150 users, mostly senior management of Enron, organized into folders. The corpus contains a total of about 500 000 messages. This data was originally made public, and posted to the web, by the Federal Energy Regulatory Commission during its investigation.

https://www.cs.cmu.edu/~./enron/

The Udacity team extracted some useful features related to email correspondence for 145 users and enhanced it with financial data for these 145 users (salary, stock options, etc.).

## Summary

The first part is dedicated to analyze the features, get insights about the dataset, and spot the main outliers. Some feature engineering is done by adding 3 new features built out of existing ones. Their impact on the classifier performance seems to be positive.

Tree-based feature selection is implemented to reduce the number of features and limit the risk of overfitting. When calculating the impact of this selection on a RandomForest Classifier, it appears that the performance gain is also limited. As a consequence, the entire feature list is used in the rest of the work, combined with a Principal Component Analysis to reduce its dimensionality.

Different basic machine learning algorithms are then tested, with limited success. These algorithms are very dependent from hyper parameters. These can for instance play a strong role on overfitting. In order to determine the best parameters for this Enron Dataset, a Grid Search Analysis is done on different Classifiers. The Grid Search Analysis is done using a f-score as scorer similar to the one calculated by the tester.py file.

In order to take the best out of these Classifiers, feature preparation is integrated in a pipeline estimator. More specifically, features are first scaled with a MinMax Scaler, then their dimension is reduced with a Principal Component Analysis before supplying them to the Classification Algorithm.

Each classifier performance is calculated with the test_classifier function from the tester.py file. This function conducts a 1000-folds cross validation with the given classifier and the given feature list. It prints out different performance metrics (accuracy, precision, recall, f-scores) that help us assess the Classifier performance.

In the end, the best classifier that pops out is an optimized Logistic Regression Classifier using a L1 distance penalty. This is the algorithm that has been implemented in my poi_id.py file.

## Limitations and potentials

One of the major limitation of this work was the dataset size and the numurous missing data it contains. There were only 145 usable observations to build a classifier and most of them were missing values for one or more features. This increased a lot the risk of overfitting.

In order to tackle this issue, the StratifiedShuffleSplit function from the sickit learn cross-validation package was used to implement 10-folds to 1000-folds cross validation when developing and testing the different algorithms.

In order to improve further the classifier performance, it would be interesting to try to implement some specific ensemble classifiers combining for example logistic regression with SVC or decision trees.
