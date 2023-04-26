import os
from datetime import datetime
import pandas as pd
from helpers.queries import mention_tracker

# Remove specific parts of text from a string
def text_removal_processing(removable_string): 
    return lambda text: text.replace(removable_string, "\n")

def schools_pipeline_query_to_csv(school_names, pipeline, query, csv_file=None):
    if os.path.exists(csv_file):
        print(f"{csv_file} already exists.")
        df = pd.read_csv(csv_file)
        return df
    data = []
    dates = []
    for school_name in school_names:
        directory = f"journal_data/txt/{school_name}"
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                date_obj = datetime.strptime(filename[:-4], '%Y_%m_%d')
                dates.append(date_obj)

                with open(filepath, 'r', encoding="utf8") as file:
                    contents = file.read()
                count = mention_tracker(contents, pipeline, query)
                data.append({'school': school_name, 'date': date_obj, 'count': 1 if count > 0 else 0, 'school_year': get_school_year(date_obj)})

    df = pd.DataFrame(data)
    df['month'] = df['date'].dt.to_period('M')
    if csv_file is not None:
        df.to_csv(csv_file, index=False)
        print(f"{csv_file} created.")
    return df

def get_school_year(date_obj):
    if date_obj.month < 8:
        return f"{date_obj.year-1}-{date_obj.year}"
    else:
        return f"{date_obj.year}-{date_obj.year+1}"
