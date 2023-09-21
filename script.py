import pandas as pd
import mylib.lib as lib

def run_summary(data):
    summary = lib.summary(data)
    print(summary)

def run_missing_summary(data):
    missing_summary = lib.missing_summary(data)
    print(missing_summary)

def run_histogram(data, column):
    lib.histogram(data, column)


def run_scatterplot(data, x, y):
    lib.scatterplot(data, x, y)


if __name__ == "__main__":
    df = lib.read_file('assets/datasets/credit/train.csv')
    summary = run_summary(data=df)
    missing_summary = run_missing_summary(data=df)
    run_histogram(df, column='Age')
    run_scatterplot(df, x='Age', y='LoanAmount')


    str1 = f"{summary.to_markdown()}"
    str2 = f"{missing_summary.to_markdown()}"

    file_path = "./report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str1 + str2)