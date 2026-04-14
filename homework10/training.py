#!/usr/bin/env python3

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle


# -------------------------
# Output Names
# -------------------------
MODEL_NAME = "20260413_BreastCancer_clf.pkl"
NORMALIZED_MODEL_NAME = "20260413_BreastCancer_normalized_clf.pkl"


# -------------------------
# Functions
# -------------------------
def get_data()-> tuple:
    data = load_breast_cancer()
    X = data.data[0:100,:]
    y = data.target[0:100]
    return (X, y)


def test_model(pipeline: Pipeline, X_train, y_train, X_test, y_test):
    accuracy_train = accuracy_score(y_train, pipeline.predict(X_train))
    print(f"Accuracy on trained data {accuracy_train*100:.2f}")

    accuracy_test = accuracy_score(y_test, pipeline.predict(X_test))
    print(f"Accuary on test data {accuracy_test*100:.2f}")


def save_model(output_name:str, pipeline: Pipeline):
    with open(output_name, "wb") as out:
        pickle.dump(pipeline, out)


def main():
    X, y = get_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)


    classifier_pipeline = Pipeline([
        ('classifier', SGDClassifier(loss="log_loss", alpha=0.1))
    ])
    classifier_pipeline.fit(X_train, y_train)
    test_model(classifier_pipeline, X_train, y_train, X_test, y_test)
    save_model(MODEL_NAME, classifier_pipeline)


    normalized_classifier_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SGDClassifier(loss="log_loss", alpha=0.1))
    ])
    normalized_classifier_pipeline.fit(X_train, y_train)
    test_model(normalized_classifier_pipeline, X_train, y_train, X_test, y_test)
    save_model(NORMALIZED_MODEL_NAME, normalized_classifier_pipeline)

if __name__ == "__main__":
    main()