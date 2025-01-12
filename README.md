# Higher National Diploma in Science in Computing (Data Analytics)

## Programming for Data Analytics Module (4369: 2024-2025)

## Atlantic Technological University (ATU) Galway

## Author: Ebelechukwu Chidimma Igwagu

## Description

This repository contains my assignment and project for the module Programming for Data Analytics at ATU Galway. The objective of the assignments and project is to demonstrate my understanding of the key topics covered in this module. These include representing datasets, plotting, pandas, numpy and random numbers,introduction to machine learning and databases.

## Assignment

Four assignments covering data analytics concepts such as data representation, dealing with different data formats, data visualisation with plots, pandas, regular expression, numpy and random numbers were given.

- Assignment 2: weather plot can be accessed [here](https://github.com/Gtalen/PFDA/blob/main/pfda_assignment/assignment2_weather.ipynb)
- Assignment 3: Pie chart  can be accessed [here](https://github.com/Gtalen/PFDA/blob/main/pfda_assignment/assignment03_pie.ipynb)
- Assignment 5: Risk Board game in python  can be accessed [here](https://github.com/Gtalen/PFDA/blob/main/pfda_assignment/assignment_5_risk.ipynb)
- Assignment 6: weather plot data analysis can be accessed [here](https://github.com/Gtalen/PFDA/blob/main/pfda_assignment/assignment_6_weather.ipynb)

## Project Title

Integrating Traditional Health Data and Simulated Wearable Device Metrics for Stroke Prediction

### Project Overview

Stroke has been identified as the second leading cause of death and the third leading cause of both death and disability worldwide ([Feigin, 2022](https://www.dropbox.com/scl/fi/tiqrhvs06s58yamxa053x/World-Stroke-Organization-WSO-Global-Stroke-Fact-Sheet-2022.pdf?rlkey=pbndaqvaadzpij099dwe6psx5&e=1&dl=0)). The center for disease control has identified risk factors for stroke to include previous stroke or transient ischemic attack, heart disease, high cholesterol, hypertension, diabetes, sickle cell disease, smoking, Genetics and family history, age, sex and race ([CDC](https://www.cdc.gov/stroke/risk-factors/index.html)).

This project presents my analysis of the Kaggle Stroke dataset, which includes data from 5,110 subjects and can be accessed [here](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download). The original dataset was enhanced by adding three additional variables derived from wearable smart watches. This modification was essential to evaluate the influence of these variables on stroke prediction and to integrate concepts of random number generation covered in the Programming for Data Analytics module.

### Usage

1. Clone the repository[here](https://github.com/Gtalen/PFDA.git).

- Locate the pfda_project folder and the stroke_prediction.ipynb notebook
- Follow along with the steps and codes

### Dependencies

This project requires several Python libraries for data manipulation, machine learning, visualization, and database handling. These come pre-installed in Visual studio code, otherwise it can be installed  by running the following:

```pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn sqlite3
```

#### Libraries used:

1. Data Manipulation and Visualization:

- numpy: For numerical computations and array handling.
- pandas: For handling and manipulating dataplots
- matplotlib: Data visualizations
- seaborn: Advanced data visualizations

2. Database Handling: sqlite3

3. Machine Learning:

- sklearn (scikit-learn): For building and training machine learning models

- imblearn: For handling class imbalance- SMOTE

4. warnings: For suppressing warnings

### Exploratory Data Analysis

- Countplots
- Histplots
- Boxplots
- Pairplots
- Correlation heat map

### Data Pre-processing

- Handling missing values by imputation of missing BMI values with age-specific means
- Categorical variables encoding
- Feature scaling
- Splitting data into training and testing sets


### Feature Engineering

- Feature selection

### Model Evaluation

The Machine learning models tested for predictive analysis;

1. Decision tree
2. KNN
3. Support Vector Machines
4. Random forest
5. Logistic regression

Random forest model was the best model for correlation analysis.

### Other Technologies Used

- GitHub
- Visual Studio Code
- Python:

### Contributors

- Ebelechukwu Chidimma Igwagu: Project author

- Want to contribute?
  - This project is open to contributions. Feel free to submit issues or pull requests.

### License

This project is available under the MIT license.
