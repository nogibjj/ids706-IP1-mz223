import pandas as pd
import matplotlib.pyplot as plt

def read_file(file_path):
    df = pd.read_csv(file_path)
    return df

def summary(df):
    summary_stats = df.describe()
    return summary_stats

# def missing_summary(file_path):
def missing_summary(df):
    # df = pd.read_csv(file_path)
    missing_counts = df.isnull().sum()
    return missing_counts

def histogram(df, column):
    df[column].hist()
    plt.show()


def scatterplot(df, x, y):
    df.plot.scatter(x, y)
    plt.show()