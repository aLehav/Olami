import os
import csv
import pandas as pd

def build_csv(data_path, output_path, get_sentiment):
    # Load the csv
    df = pd.read_csv(data_path, encoding='utf8')

    granularities = ['article','paragraph','sentence']

    output_file_exists = os.path.exists(output_path)

    if output_file_exists:
        # If it exists, read the output file and create a list of existing dates
        with open(output_path, 'r', newline='\n', encoding='utf8') as existing_file:
            existing_dates = set()
            reader = csv.reader(existing_file)
            next(reader)  # Skip the header row
            for row in reader:
                existing_dates.add(row[0])  # Assuming the date is in the first column

        # Filter the DataFrame to skip rows with existing dates
        df = df[~df['date'].isin(existing_dates)]

    # Open the output CSV file for writing
    with open(output_path, 'a', newline='\n', encoding='utf8') as output_file:
        csv_writer = csv.writer(output_file)

        # Write the header row
        if not output_file_exists:
            header = list(df.columns)
            for granularity in granularities:
                header.extend([f'{granularity}_neg', f'{granularity}_pos', f'{granularity}_neu'])
            csv_writer.writerow(header)

        # Process sentiment analysis and write to the CSV file line by line
        for index, row in df.iterrows():
            article = row['article']
            keyword = row['keyword']

            output_row = [row['date'], row['school'], keyword, article]
            # Perform sentiment analysis for each granularity
            for granularity in granularities:
                neg, pos, neu = get_sentiment(article, granularity, keyword)

                # Prepare the row to write to the CSV file
                output_row.extend([neg, pos, neu])

                # Print the line with sentiment analysis results
                print(f"Article: {article[:30]}... | Keyword: {keyword} | Granularity: {granularity} | Neg: {neg} | Pos: {pos} | Neu: {neu}")

            # Write the row to the CSV file
            csv_writer.writerow(output_row)

    # The output CSV file will be automatically closed after the 'with' block