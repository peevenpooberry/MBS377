# Homework 10: Continued MLOps

## Summary
In this homework I trained two linear classifiers using the `training.py` script.

Both classifiers were trained using the UCI Breast Cancer Wisconsin Dataset and are scikit-learn `SGDClassifers` using a loss function of `log_loss` for prediction confidence output with an alpha of 0.1.

I test both models with `accuracy_score` and then save both of these models to `.pkl` files.

`20260413_BreastCancer_clf.pkl`
- Accuracy on trained data 77.14
- Accuary on test data 63.33

`20260413_BreastCancer_normalized_clf.pkl`
- Accuracy on trained data 95.71
- Accuracy on test data 96.67

In my `inference.py` script I take in these models and a `.csv` of sample rows and output each model's prediction per row given.

## How to Run

First create a python venv, source the virtual environment, and then pip install the requirements file with:
```
pip install -r requirements.txt
```

### `training.py`
The global variables of output files names can be modified before running. Then to run the models to begin training, testing, and saving run the command:
```
./training.py
```

### `inference.py`
This script has an arg parser that requires the paths to model `.pkl` files and a path to the rows of sample-data that will have predictions ran on.

I included the script I used to make the `sample_data.csv` file `make_sample_data.py`.

Example command to run script:
```
./inference.py \
-m path/to/model1.pkl path/to/model2.pkl \
-i path/to/sample_data.csv
```

The final output will then look something like this
```
$ ./inference.py \
-m /home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl /home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl \
-i /home/ubuntu/mbs-337/hw/homework10/sample_data.csv

Sample Data contains 6 entries

----------------------------
Row #1
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [0] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [0] 80.49% Confidence

----------------------------
Row #2
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [1] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [1] 99.62% Confidence

----------------------------
Row #3
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [0] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [1] 85.78% Confidence

----------------------------
Row #4
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [1] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [1] 88.59% Confidence

----------------------------
Row #5
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [0] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [1] 95.63% Confidence

----------------------------
Row #6
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_clf.pkl            prediction: [0] 100.00% Confidence
/home/ubuntu/mbs-337/hw/homework10/20260413_BreastCancer_normalized_clf.pkl prediction: [0] 87.51% Confidence
```