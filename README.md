# Olami Data Project Work

## Article Project

### Example Scraper

- Running:
    -     python example_scraper.py
- Files: 
    - `Example_Scraper.ipynb`
    - `example_scraper.py`
    - `example_scraper_output.csv`
- Purpose:
    - Generate a list of scraped links from an example site.

### <p> Tag Scraper

- Running:
    - willm_scraper_passover.ipynb
- Files:
    - `passover_text.csv`
- Purpose:
    - Scrapes the HTML content of a specific website, extracts the text from all the <p> tags, store the text in a pandas dataframe, and then saves the dataframe as a CSV file.

### USC Website Scraper and Link Sorter

- Running:
    - willm_scraper_usc.ipynb (1)
    - file_sorter.ipynb (2)
- Files:
    - `file_sorter_output_gpt.csv`
    - `daily_trojan_june_2009_links.csv`
- Purpose:
    - (1) Scrapes a website for all relevant links to the 2009 editions of the Daily Trojan newspaper, stores them in a set to avoid duplicates, creates a DataFrame from the list of links, and saves it as a CSV file.
    - (2) Categorizes links generated from (1) into three lists based on their file extensions: (I) ".txt" & ".xml", (II)".pdf", (III) all other file extensions are stored in other_links.

## Past Work

- Twitter Scraping:
  - Files: 
    - `past_work/Tweet_Sentiment.ipynb`
  - Conclusions:
    - Project paused as Twitter API went from $0 to $20K+ a month.
    - Redundant compared to projects such as [ADL OHI Index](https://www.adl.org/online-hate-index-0).
- Named Entity Recognition
  - Files:
    - `Article_Sentiment.ipynb`
  - Conclusions:
    - Redundant compared to projects such as [ADL OHI Index](https://www.adl.org/online-hate-index-0).
    - Would be difficult to get sinificant results both because of disagreements in the definitons for antisemitism and antizionism, and issues with the significant overlap of the two.
- Topic Recognition
  - Files:
    - `past_work/Article_Topic_Recognition.ipynb`
    - `past_work/gensim_evaluation_ex.py`
    - `past_work/gensim_evaluation_ex.ipynb`
    - `past_work/data`
  - Conclusions:
    - May be usable in domain-specific texts, but inefficient for recognizing antisemitism or positive Jewish mention from a large pool of data because of unsupervised approach and sparsity of Jewish mention.