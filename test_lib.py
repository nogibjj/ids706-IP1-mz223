import pandas as pd

from mylib.lib import read_file, summary, missing_summary, histogram, scatterplot

df = read_file('assets/datasets/credit/train.csv')

def test_read_file():
    assert isinstance(df, pd.DataFrame)

def test_summary():
    assert isinstance(summary(df), pd.DataFrame)

def test_missing_summary():

    assert isinstance(missing_summary(df), pd.Series)

def test_histogram():
    assert histogram(df, column='Age') == None

def test_scatterplot():
    assert scatterplot(df, x='Age', y='LoanAmount') == None