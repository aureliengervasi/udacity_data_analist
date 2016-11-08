# udacity_data_analyst

This repository hosts my projects developed during the data analyst nanodegree I followed with Udacity.
Feel free to share some feedback or constructive remarks!

Udacity data analyst nanoprogram: [link](https://www.udacity.com/course/data-analyst-nanodegree--nd002)


## Repo structure

Each folder represents a project concluding a chapter in the Udacity Data Analyst Nanodegree.

### [P1 - Perceptual phenomenon](P1 - Perceptual phenomenon/README.md)

**Analyzed the Stroop effect using descriptive statistics to provide an intuition about the data, and inferential statistics to draw a conclusion based on the results.**

A Student's t-test has been conducted using Python Numpy and Scipy libraries. It showed that the average recorded time for congruent words is lower than for incongruent words and we can estimate this difference between 4.2s and 11.7s with a 99.9% confidence interval.

***topics: statistics, hypothesis testing, measure of central tendency, measure of variability***

### [P2 - Investigate the Titanic Dataset](P2 - Investigate the Titanic Dataset/README.md)

**Posed a question about a dataset, then used NumPy and Pandas to answer that question based on the data and created a report to share the results.**

Data set: Titanic Dataset from Kaggle

Question: "What factors made people more likely to survive?"

The correlation of the survival rate with each independent variable was studied, and visualizations were made to help the analyze. For a few unexpected results, additional Data manipulation was done to try to get some clues about possible explanations.

***topics: Python, NumPy, Pandas, Matplotlib***

### [P3 - Wrangle OpenStreetMap Data with MongoDB - Paris Metroline](P3 - Wrangle OpenStreetMap Data/)

**Chose a region and used data munging techniques to assess the quality of the data for validity, accuracy, completeness, consistency and uniformity.**

In this project, I used geographical data from the Paris area gathered by the Open Street Map community. I assessed data quality, cleaned entries when needed, and stored it in a MongoDB database for further auditing.

***topics: Python, data verification, data cleaning, MongoDB***

### [P4 - Explore and Summarize Data](P4 - Explore and Summarize Data/P4.Rmd)

**Investigated a dataset using R and exploratory data analysis techniques, exploring both single variables and relationships between variables.**

The goal of the following work is to explore the Red Wine Dataset from [Cortez et al., 2009] in order to identify which chemicals play a role on wine quality ratings.

Univariate and multi-variate analysis are conducted with Rstudio. Several visualization are made for exploratory data analysis. Three final plots are chosen to summarize the main findings. 

***topics: RStudio, R, plotting in R, exploratory data analysis techniques***

### [P5 - Identify Fraud from Enron Email](P5 - Identify Fraud from Enron Email/README.md)

**Identified which Enron employees are more likely to have committed fraud using machine learning and public Enron financial and email data.**


Different machine learning pipelines are developed, using PCA, Random forest, SVC or logistic regression. Several grid-search optimizations are conducted in order to fine-tune the main pipelines parameters.

The major challenge is the low number of entries in the dataset (145 entries with 18 related to fraud) which led me to use a stratified shuffle split with 10-folds to 1000-folds cross-validation in order to limit the risk of over-fitting.

In the end, the best classifier achieved a precision of 33% and a recall of 60%.

*topics: Python, scikit-learn, machine learning, natural language processing, feature selection, hyper-parameter tuning, verifying machine learning performance*

### [P6 - Make Effective Data Visualization](P6 - Make Effective Data Visualization/Readme.md)

**Created a polished data visualization that tells a story, allowing a reader to explore trends or patterns.**

I choose to use the monthly TGV train line regularity statistics from the French railway company (SNCF) with a "martini-glass" map visualization. The main message that should be communicated is that disturbances related to weather events or strikes tend to have the strongest impact on train regularity.

The visualization is implemented in an html page, using the D3.js library and geojson data for drawing the map of France.

[Link to the HTML visualization](http://aureliengervasi.github.io/udacity_data_analist/P6/index.html)

***topics: Dimple.js, D3.js, visualization design principles, visual encodings, HTML, CSS, SVG, geojson***


	