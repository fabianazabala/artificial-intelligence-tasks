import pandas as pd

data = {'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female']
        }

df = pd.DataFrame(data, columns=['total_bill', 'tip', 'sex'])

print(df)

print("___________________________________________________________________")
df.to_csv('file.csv', index=False)

mean = df['total_bill'].mean()
print('\nMean\n------')
print(mean)

df.loc[:, "total_bill"].mean()

print("___________________________________________________________________")
print(df['tip'].max())

print("___________________________________________________________________")
