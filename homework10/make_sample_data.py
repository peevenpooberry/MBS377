import csv
from sklearn.datasets import load_breast_cancer

output_name = "sample_data.csv"

data = load_breast_cancer()
X = data.data[100:106,:]
header = data.feature_names
with open(output_name, "w", encoding='utf-8') as out:
    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(X)
