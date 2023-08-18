"""
Given a csv from one of the Sentiment_Calculator notebooks, calculate bias by doing the following:
Group by topic, and consider that 1 series
Compute variance between series of sentiment for entire article granularity and sentence-granularity for each of the labels (Positive, Negative, Neutral) leaving you with 3 values
Average these values (add functionality to take max as well) and assume this to be 'bias'
Store the bias for a given school as a csv with the columns of School_Name, Israel_Bias, Palestine_Bias, India_Bias, China_Bias
Save a new csv with this entry, or load in a csv of past schools with these columns and add this row to the bottom
"""
method = "scaled_diff_avg"
sentiment_type = "summarizer"
sentiment_path_portion = "3" if sentiment_type == "summarizer" else "2/nltk_sia"
output_path = f"bias_processing/data/4/au_poli_bias_{method}.csv"

from statistics import mean
import numpy as np

def score_computer_generator(method=method):
    def score_computer(article_sentiment_scores, sentence_sentiment_scores):
        if len(article_sentiment_scores) == 0:
            return np.nan
        if method == "mean_avg":
            article_val = mean(article_sentiment_scores)
            sentence_val = mean(sentence_sentiment_scores)
            return (article_val + sentence_val) / 2
        elif method == "mean_diff":
            article_val = mean(article_sentiment_scores)
            sentence_val = mean(sentence_sentiment_scores)
            return article_val - sentence_val
        elif method == "diff_avg":
            differences = [a - b for a, b in zip(article_sentiment_scores, sentence_sentiment_scores)]
            return mean(differences)
        elif method == "scaled_diff_avg":
            differences = [a - b for a, b in zip(article_sentiment_scores, sentence_sentiment_scores)]
            return 100*mean(differences)
        else:
            raise(ValueError("Put in a valid method"))
    return score_computer
scorer = score_computer_generator(method=method)

"""
In this version, the bias is calculated as the average of the variances of the sentiment scores 
within each granularity (article and sentence).
"""
import pandas as pd
import os

if os.path.exists(output_path):
    os.remove(output_path)

# for SCHOOL in ["LIU","Georgetown","CMU","AU","USC","York"]:
for SCHOOL in ['AU']:

    data_path = f"bias_processing/data/{sentiment_path_portion}/{SCHOOL.lower()}_dataset_{sentiment_type}.poli.csv"

    # Read the data from the CSV file
    df = pd.read_csv(data_path)

    # Define the keywords and sentiments to be processed
    keywords = ['conservative','Democrat','liberal','Republican']
    sentiments = ['pos', 'neg', 'neu']

    # Initialize a dictionary to store the bias for each keyword and sentiment
    result_dict = {f'{keyword}_{sentiment}_Bias': [] for keyword in keywords for sentiment in sentiments}

    # Loop over each keyword and sentiment
    for keyword in keywords:
        for sentiment in sentiments:
            # Extract the sentiment scores for the keyword from the dataframe
            article_sentiment_scores = df.loc[df['keyword'] == keyword, f'article_{sentiment}']
            sentence_sentiment_scores = df.loc[df['keyword'] == keyword, f'sentence_{sentiment}']

            result_dict[f'{keyword}_{sentiment}_Bias'] = scorer(article_sentiment_scores, sentence_sentiment_scores)

    # Add the school name to the results dictionary
    result_dict['School_Name'] = SCHOOL

    # Convert the results dictionary to a DataFrame
    result_df = pd.DataFrame(result_dict, index=[0])

    # If the output file already exists, load the existing data and append the new data only if it's not duplicate
    if os.path.exists(output_path):
        existing_df = pd.read_csv(output_path)
        if not existing_df.equals(result_df):
            result_df.to_csv(output_path, mode='a', header=False, index=False)
    # If it doesn't exist, create a new file
    else:
        result_df.to_csv(output_path, index=False)