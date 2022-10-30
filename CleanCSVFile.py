# isntall and import the needed python libraries
from operator import index
import pandas as pd
import langdetect as detect

# Read the csv file
df = pd.read_csv('Datasets/test.csv',
                 sep=';', header=1, on_bad_lines='skip')

# Drop the columns that are not needed
to_drop = ['Unwanted Column 1',
           'Unwanted Column 2',
           'Unwanted Column 3',
           'Unwanted Column 4',
           'Unwanted Column 5']

df.drop(to_drop, inplace=True, axis=1)

# Remove all non-alphabetic characters
df.replace(r'http\S+', ' ', regex=True, inplace=True)
df.replace(r'www\S+', ' ', regex=True, inplace=True)
df.replace(r'https\S+', ' ', regex=True, inplace=True)
df.replace(r'\W\s+', ' ', regex=True, inplace=True)
df.replace(r'\d+', ' ', regex=True, inplace=True)
df.replace(r'\t+', ' ', regex=True, inplace=True)
df.replace(r'\d+', ' ', regex=True, inplace=True)
df.replace(r'\-+', ' ', regex=True, inplace=True)
df.replace(r'\\+', ' ', regex=True, inplace=True)
df.replace(r'\/+', ' ', regex=True, inplace=True)
df.replace(r'\"+', ' ', regex=True, inplace=True)
df.replace(r'\#+', ' ', regex=True, inplace=True)
df.replace(r'\++', ' ', regex=True, inplace=True)
df.replace(r'\@+', ' ', regex=True, inplace=True)
df.replace(r'\$+', ' ', regex=True, inplace=True)
df.replace(r'\%+', ' ', regex=True, inplace=True)
df.replace(r'\^+', ' ', regex=True, inplace=True)
df.replace(r'\&+', ' ', regex=True, inplace=True)
df.replace(r'\*+', ' ', regex=True, inplace=True)
df.replace(r'\(+', ' ', regex=True, inplace=True)
df.replace(r'\)+', ' ', regex=True, inplace=True)
df.replace(r'\[+', ' ', regex=True, inplace=True)
df.replace(r'\]+', ' ', regex=True, inplace=True)
df.replace(r'\{+', ' ', regex=True, inplace=True)
df.replace(r'\}+', ' ', regex=True, inplace=True)
df.replace(r'\|+', ' ', regex=True, inplace=True)
df.replace(r'\;+', ' ', regex=True, inplace=True)
df.replace(r'\:+', ' ', regex=True, inplace=True)
df.replace(r'\<+', ' ', regex=True, inplace=True)
df.replace(r'\>+', ' ', regex=True, inplace=True)
df.replace(r'\?+', ' ', regex=True, inplace=True)
df.replace(r'\,+', ' ', regex=True, inplace=True)
df.replace(r'\.+', ' ', regex=True, inplace=True)
df.replace(r'\=+', ' ', regex=True, inplace=True)
df.replace(r'\_+', ' ', regex=True, inplace=True)
df.replace(r'\~+', ' ', regex=True, inplace=True)
df.replace(r'\`+', ' ', regex=True, inplace=True)
df.replace(r'\s+', ' ', regex=True, inplace=True)

# Remove all duplicate rows
df.drop_duplicates(inplace=True)

# Remove all rows that are NaN 
df.dropna(inplace=True)

# remove all rows that are not ASCII chacaters
df = df[df['SMS text'].map(lambda x: x.isascii())]

# remove all rows that are not English
for i in range(len(df)):
    try:
        ['SMS text'][i] = detect.detect(df['SMS text'][i])
        if df['SMS text'][i] != 'en':
            df.drop(i, inplace=True, index=False)
    except:
        pass
# Save the new csv file
df.to_csv('Datasets/test_clean.csv', index=False)
