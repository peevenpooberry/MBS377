#!/usr/bin/env python3

import pickle
import argparse
import pandas as pd
import sys
import pathlib as Path

# -------------------------
# Arg Parser
# -------------------------
arg_parser = argparse.ArgumentParser(description="Makes Preditions on sample data based on given trained models")
arg_parser.add_argument(
    "-m", "--models",
    required=True,
    nargs="+",
    help="The path to the input models given as a list of strings" 
)
arg_parser.add_argument(
    "-i", "--inputdata",
    required=True,
    type=str,
    help="The path to the input CSV file of Sample Data rows" 
)
args = arg_parser.parse_args()


# -------------------------
# Functions
# -------------------------
def import_models(pickle_names: list[str])-> list[tuple]:
    pipelines = []
    for pickle_name in pickle_names:
        try:
            with open(pickle_name, "rb") as f:
                pipeline = pickle.load(f)
                pipelines.append((pickle_name, pipeline))
        except FileNotFoundError:
            print(f"Could not load model: {pickle_name}")
    return pipelines


def load_sample_data(sample_data: str)-> pd.DataFrame:
    sample_data_path = Path.Path(sample_data)
    if sample_data_path.is_file:
        try:
            sample_data = pd.read_csv(sample_data_path)
            return sample_data
        except Exception as e:
            print(f"Could not load sample data: {e}")
            sys.exit(1)
    else:
        print(f"Could not find file at {sample_data_path}")
        sys.exit(1)


def make_preditions(pipelines, sample_data):
    num_rows = len(sample_data)
    print(f"Sample Data contains {num_rows} entries\n")
    for i in range(num_rows):
        row = sample_data.iloc[i,]
        predict_row(pipelines, row, i)


def predict_row(pipelines: list[tuple], row, index: int):
    max_name_len = max(len(name) for name, _ in pipelines)
    print("----------------------------")
    print(f"Row #{index + 1}")
    for name, pipeline in pipelines:
        try:
            prediction = pipeline.predict([row])
            prob = pipeline.predict_proba([row]).max()
            print(f"{name:<{max_name_len}} prediction: {prediction} {prob*100:.2f}% Confidence")
        except:
            prediction = "error"
            print(f"{name:<{max_name_len}} prediction: {prediction}")
    print()
    

def main():
    pipelines = import_models(args.models)
    sample_data = load_sample_data(args.inputdata)
    make_preditions(pipelines, sample_data)

if __name__ == "__main__":
    main()