import sqlite3
import pandas as pd

# Load card data from CSV file (replace 'cards.csv' with your file name)
card_data = pd.read_csv('csvs/treasure.csv')

# Create a new DataFrame with selected columns
card_data = card_data.iloc[:, [i for i in range(card_data.shape[1]) if i not in [1,2,5]]]

# Drop null rows
card_data = card_data.dropna()

card_data['id'] = range(1, len(card_data) + 1)
card_data['used'] = 0

# Connect to SQLite database
conn = sqlite3.connect('cards.db')

# Insert card data into the cards table
card_data.to_sql('treasure', conn, if_exists='replace', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()