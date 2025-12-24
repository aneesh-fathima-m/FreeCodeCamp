import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

# Column names for adult.data
columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

# Load the data file
df = pd.read_csv('adult.data', names=columns, sep=',\s*', engine='python')

# Run analysis
result = calculate_demographic_data(df)

# Print results
for key, value in result.items():
    print(f"{key}: {value}")
