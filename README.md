# Olami Data Project Work

## Article Project

### USC Newspaper Scraper

- Files:
  - `USC.ipynb`
- Purpose:
    - Read through all years of USC *Daily Trojan* publications, get all months with publications, and then for each month get all days with publications and the associated links to publications, found in `usc_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/USC`. This data can then be processed taking out redundant text such as `usc_text.txt` and queried for information generating figures such as what's in `figures/USC`.

### UF Newspaper Scraper

- Files:
  - `UF.ipynb`
- Purpose:
    - Read through all years of UF *Independent Florida Gator* publications, get all months with publications, and then for each month get all days with publications and the associated links to publications. Then, iterate through these links, use the Django API attached to the downloads tab to get a list of pdf links, found in `uf_article_pages.json`. Then, iterate through these links, use PyPDF2 to get the PDF's text object to generate `journal_data/txt/UF`. This data can then be processed and queried for information generating figures such as what's in `figures/UF`.

## Past Work

Twitter Scraping:
  - Files: 
    - `past_work/Tweet_Sentiment.ipynb`
  - Conclusions:
    - Project paused as Twitter API went from $0 to $20K+ a month.
    - Redundant compared to projects such as [ADL OHI Index](https://www.adl.org/online-hate-index-0).

Named Entity Recognition
  - Files:
    - `Article_Sentiment.ipynb`
  - Conclusions:
    - Redundant compared to projects such as [ADL OHI Index](https://www.adl.org/online-hate-index-0).
    - Would be difficult to get sinificant results both because of disagreements in the definitons for antisemitism and antizionism, and issues with the significant overlap of the two.

Topic Recognition
  - Files:
    - `past_work/Article_Topic_Recognition.ipynb`
    - `past_work/gensim_evaluation_ex.py`
    - `past_work/gensim_evaluation_ex.ipynb`
    - `past_work/data`
  - Conclusions:
    - May be usable in domain-specific texts, but inefficient for recognizing antisemitism or positive Jewish mention from a large pool of data because of unsupervised approach and sparsity of Jewish mention.

\<p> Tag Scraper

- Files:
    - `past_work/passover_text.csv`
    - `past_work/willm_scraper_passover.ipynb`
- Purpose:
    - Scrapes the HTML content of a specific website, extracts the text from all the <p> tags, store the text in a pandas dataframe, and then saves the dataframe as a CSV file.

Example Scraper

- Files: 
    - `past_work/Example_Scraper.ipynb`
    - `past_work/example_scraper.py`
    - `past_work/example_scraper_output.csv`
- Purpose:
    - Generate a list of scraped links from an example site.