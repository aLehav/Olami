# Code Base: Unsupervised Bias Detection in College Student Newspapers

## Note on Reproducibility

All code present is the code used to generate all data and results both in this repository and in the paper. Files have been restructured for the sake of user readability. Files and folders may need to be slightly rearranged in the case of minor errors.

## Directory
```
Olami
├── archive_scrapers
│   ├── helpers
│   ├── scraper_json_files
│   └── scrapers
├── bias_processing/data
│   ├── 1
│   ├── 3
│   └── 4
├── figures
├── grouped_data
│   ├── csv
│   └── pkl
│       ├── monthly
│       └── yearly
├── journal_data/txt
└── sentiment_tools
```
## Workflow Breakdown
### Archive Scraping
To scrape an archive, a `.ipynb` file is made in `archive_scrapers/scrapers`, the dict relating days to entry links is stored in `archive_scrapers/scraper_json_files`, and associated helper functions for coding are in `archive_scrapers/helpers`.
### Keyword Querying
An example of every type of querying can be found in `AllSchools.ipynb`. Once a query is done, the results are saved to `grouped_data/csv` for the daily results and `grouped_data/pkl` for the grouped results. Visualizations from this step can be found in `figures`. Queries for each associated school can typically be found at the bottom of notebooks in `archive_scrapers/scrapers`. Helper functions used for grouping and graphing can be found at `archive_scrapers/helpers`. 
### Bias Calculation
Code for bias calculation can be found in `sentiment_tools` with results in `bias_processing/data`. `Sentiment_Dataset_Maker.ipynb` takes data from `journal_data/txt` and turns it into data in `bias_processing/data/1`. `Sentiment_Calculater_Summarizer.ipynb` takes data from `bias_processing/data/1` and turns it into data in `bias_processing/data/3`. `bias_calculater.py` takes data from `bias_processing/data/3` and turns it into data in `bias_processing/data/4`.