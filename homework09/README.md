# Homework 9: MLOps

## Overview
In this homework I trained a basic machine learning classifier model to predict whether a tumor is benign or malignant based on the parameters of:
- mean texture
- mean area
- mean smoothness
- mean symmetry
- worst texture
- worst area
- worst smoothness
- worst symmetry

The model was trained and tested off of data from the UCI Breast Cancer Wisconsin Dataset, and shows a testing accuracy of 93.33%.

## How to Run
Using the `requirements.txt` file create and load the dependent libraries.

Navigate to the `homework09/` directory and either create a virtual environment or install to your global environment with the command:
```
pip install -r requirements.txt
```

Next load the jupyter notebook in the environment you just installed the libraries to, using the command:
```
jupyter notebook Notebook.ipynb
```

Select the kernel that the required libraries were installed to and begin running the cells in order.