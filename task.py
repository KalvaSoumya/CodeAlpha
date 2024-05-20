import pandas as pd

def clean_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Handle missing values: fill with median for numeric columns, mode for categorical columns
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize column names: convert to lowercase and replace spaces with underscores
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

# Example usage
input_file = 'raw_data.csv'
output_file = 'cleaned_data.csv'
clean_data(input_file, output_file)