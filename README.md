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

### UMich Newspaper Scraper

- Files:
  - `UMich.ipynb`
- Purpose:
    - Read through all subpages of UMich *The Michigan Daily* publications from 2009 onward by using Selenium's Chrome Web Driver. Then get all days with publications and the associated links to zipped text files of the publications, found in `umich_article_pages.json`. Then, iterate through these links, and for each one download the ZIP file and extract the contents to a temporary location, and read all text files to generate `journal_data/txt/UMich`. This data can then be processed and queried for information generating figures such as what's in `figures/UMich`.

### UCSD Newspaper Scraper

- Files:
  - `UCSD.ipynb`
- Purpose:
    - Read through all subpages of UCSD *The Guardian* publications from 2009 onward, getting all months with publications, and then for each month getting all days with publications and the associated links to publications, which can be found in `ucsd_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/UCSD`. This data can then be processed and queried for information generating figures such as what's in `figures/UCSD`.

### York Newspaper Scraper

- Files:
  - `York.ipynb`
- Purpose:
    - Read through all subpages of York *Excalibur* publications from 2010 onward, getting all months with publications, and then for each month getting all days with publications and the associated links to publications, which can be found in `york_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/York`. This data can then be processed and queried for information generating figures such as what's in `figures/York`.

### McGill Newspaper Scraper

- Files:
  - `McGill.ipynb`
- Purpose:
    - Read through all subpages of *The McGIll Daily* publications from 2009 onward, getting all months with publications, and then for each month getting all days with publications and the associated links to publications, which can be found in `mcgill_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/McGill`. This data can then be processed and queried for information generating figures such as what's in `figures/McGill`.

### UCF Newspaper Scraper

- Files:
  - `UCF.ipynb`
- Purpose:
    - Read through all subpages of *Knight News* website publications from 2009 onward by proceduring getting the link for each subpage, and then for each month getting all days with publications and the associated links to publications, which can be found in `ucf_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/UCF`. This data can then be processed and queried for information generating figures such as what's in `figures/UCF`.

### USF Newspaper Scraper

- Files:
  - `USF.ipynb`
- Purpose:
    - Read through all subpages of *The Oracle* website publications from 2009 onward by retrieving the link for each subpage. Then, for each month, get all days with publications and the associated links to publications, which can be found in `usf_article_pages.json`. Iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/USF`. This data can then be processed and queried for information, generating figures such as what's in `figures/USF`. Additionally, it includes code to graph mentions of a specific string (e.g., "Palestine") over time, allowing customization of hyperparameters like the time slice and saving the resulting figure.

### GW Newspaper Scraper

- Files:
  - `GW.ipynb`
- Purpose:
    - Read through all subpages of *The Hatchet* website archives to retrieve the URLs of subpages that contain publications. Filter the subpages based on their publication dates (from 2009 onward). Then, retrieve the article links and dates from these subpages and store them in `gw_article_pages.json`. Next, process the articles by fetching their content and combining it into text format. The resulting text is saved in `journal_data/txt/GW` files. This data can be further processed and queried for information, like generating figures such as what's in `figures/GW`. Additionally, the code includes functionality to graph mentions of a specific string (e.g., "Palestine") over time, allowing customization of hyperparameters like the time slice and saving the resulting figure.

### CMU Newspaper Scraper

- Files:
  - `CMU.ipynb`
- Purpose:
    - The code retrieves subpage URLs from *The Tartan* archives for each year from 2009 to the current year. It then extracts the article links and dates from these subpages, filtering out unwanted links such as PDFs or specific sections. The resulting article links and dates are stored in `cmu_article_pages.json`. The code also includes functionality to process the articles for each date, fetching their content and saving it in text format, which is saved in `journal_data/txt/CMU`. Finally, the code graphs mentions of a specific string (e.g., "Israel") over time, allowing customization of hyperparameters such as the time slice and saving the resulting figures in `figures/CMU`.

### AU Newspaper Scraper

- Files:
  - `AU.ipynb`
- Purpose:
    - The code retrieves article links and dates from The Eagle Online search results page. It iterates over a range of dates, constructs the appropriate URL, sends a request, and parses the response to extract the article links and dates. The resulting data is stored in `au_article_pages.json`. The code also includes functionality to process the articles for each date, fetching their content and saving it as text files in the directory `journal_data/txt/AU`. Finally, the code graphs mentions of a specific string (e.g., "Israel") over time, allowing customization of hyperparameters such as the time slice. The resulting figures are saved in `figures/AU`.

### Georgetown Newspaper Scraper

- Files:
  - `Georgetown.ipynb`
- Purpose:
    - The Georgetown code scrapes article links from *The Hoya* and retrieves their publication dates. It saves the data in a JSON file named `georgetown_article_pages.json`. The code then processes the saved data, converting the articles into text format. The text data is organized and stored in the directory `journal_data/txt/Georgetown` with separate text files for each publication date. Additionally, the code includes functionality to generate a graph depicting the mentions of a specific keyword over time for Georgetown. The generated graph is saved in the `figures/Georgetown` directory, providing visual representation of the keyword mentions.

### Harvard Newspaper Scraper

- Files:
  - `Harvard.ipynb`
- Purpose:
    - Read through all subpages of *The Harvard Crimson* website publications from 2009 onward by proceduring getting the link for each subpage, and then for each month getting all days with publications and the associated links to publications, which can be found in `harvard_article_pages.json`. Then, iterate through these links, use BeautifulSoup to fetch the content from the HTML, and append all content together as text to generate `journal_data/txt/Harvard`. This data can then be processed and queried for information generating figures such as what's in `figures/Harvard`.

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