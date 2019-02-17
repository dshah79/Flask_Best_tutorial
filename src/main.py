import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/train_LoanPredDataset.csv") ## Load the data

shape =  (df.shape) ## Shape of the Dataframe  614 * 12

#print (df.describe()) ## Gives an Idea


print (df['Property_Area'].value_counts())

a = df['ApplicantIncome'].hist(bins=50)

df.boxplot (column='ApplicantIncome', by= 'Education')

plt.show()

#print df['Credit_History'].value_counts(ascending=True)


print df.pivot_table(values='Loan_Status', index=['Credit_History'], aggfunc=lambda  x : x.map({'Y':1, 'N': 0}).mean())

