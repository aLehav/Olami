import os
from datetime import datetime
import pandas as pd
from helpers.queries import mention_tracker
import re

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

def csv_to_positive_articles(csv_file):
    df = pd.read_csv(csv_file)
    grouped = df[['school','date']]
    # grouped = df[df['count'] > 0][['school','date']]
    grouped['txt_file'] = grouped.apply(lambda x: f"journal_data/txt/{x['school']}/{x['date'].replace('-', '_')}.txt", axis=1)
    return grouped

def positive_articles_to_sentences(df, string):
    # Define a function to search for the string in a file and return the matching sentences
    def get_sentences_with_string(file_path, string):
        # Read the contents of the file into a string
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
        # Split the contents into sentences
        sentences = re.split('[.!?]', contents)
        # Find the sentences that contain the string
        matching_sentences = [s.strip() for s in sentences if string in s]
        return matching_sentences

    # Loop through each row in the DataFrame and get the matching sentences for the 'string'
    all_matching_sentences = []
    for index, row in df.iterrows():
        file_path = row['txt_file']
        try:
            matching_sentences = get_sentences_with_string(file_path, string)
            all_matching_sentences += matching_sentences
        except UnicodeDecodeError:
            print(f"Error with encoding at file {file_path}")

    return all_matching_sentences

def preprocess_text(text):
    # Remove a starting quotation mark and whitespace if present
    text = re.sub(r'\s*^["“”]?\s*', '', text)

    # Replace abbreviations with their full form
    # text = re.sub(r'Hillel', 'The Hillel Center', text)
    # text = re.sub(r'UCSD', 'University of California San Diego', text)
    # text = re.sub(r'AS', 'Associated Students', text)
    # text = re.sub(r'UF', 'University of Florida', text)
    text = re.sub(r'Jewish', 'Jewish ', text)

    # Replace newlines and multiple spaces with a single space
    text = re.sub(r'[\n\s]+', ' ', text)

    # Add space after comma
    text = re.sub(r'([\w\d]+),([A-Za-z])', r'\1, \2', text)
    # Replace left single quote characters with right single characters
    text = re.sub(r'(\w+)’(\w+)', r"\1'\2", text) 

    # Fix mistake of column-cut words ('fol- lowed' or 'fol-lowed' to 'followed')
    text = fix_hyphens(text)

    # Add missing spaces ('TheHillel' to 'The Hillel')
    text = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)

    return text

def fix_hyphens(text):
    from nltk.corpus import wordnet

    split_regex = r"\b(\w+)[-]\s?(\w+)\b"
    words = re.split(r"(?<!-)\s", text)
    for i, word in enumerate(words):
        match = re.match(split_regex, word)
        if match:
            word1, word2 = match.group(1), match.group(2)
            joined_word = word1 + word2
            if wordnet.synsets(joined_word):
                # If the joined word is a valid word, replace the split word with the joined word
                words[i] = joined_word
            else:
                # If the joined word is not a valid word, choose the better option
                word1_score = len(wordnet.synsets(word1))
                word2_score = len(wordnet.synsets(word2))
                if word1_score > word2_score:
                    words[i] = word1
                else:
                    words[i] = word2
    return ' '.join(words)