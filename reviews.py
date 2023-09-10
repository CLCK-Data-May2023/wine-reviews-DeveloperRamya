import pandas as pd

# Read the CSV data
df = pd.read_csv('data\winemag-data-130k-v2.csv.zip')

# Group the data by 'country' and calculate the number of reviews and average points
summary_df = df.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count', 'average_points': 'points'})
summary_df['points'] = summary_df['points'].round(1)
# Reset the index to make 'country' a regular column
summary_df.reset_index(inplace=True)

# Save the summary data to a new CSV file
summary_df.to_csv('data/reviews-per-country.csv', sep='\t', index=False)

print("Summary data has been saved to 'data/reviews-per-country.csv'")


