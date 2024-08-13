# Portfolio Projects

Welcome to my portfolio! This repository contains two distinct projects that showcase my skills in data analysis and web scraping.

## 📊 Data Cleaning and EDA Project

###  Project Overview

This project focuses on cleaning and preparing a dataset related to layoffs. The goal is to enhance the quality of the data for further analysis by performing various data cleaning operations.


### 🛠️ Key Steps

1. **Creating Staging Tables**: In this step, the dataset was duplicated into a staging table to ensure that operations were performed on a separate dataset, thereby preserving the integrity of the original data.
2. **Removing Duplicates**: SQL queries were used to identify and delete duplicate entries, ensuring that each record remained unique.
3. **Standardizing Data**: Cleaning and normalizing data fields to ensure consistency, including trimming whitespace and standardizing values.
4. **Adressing Null Values**: Handle missing or null values by replacing them or removing the corresponding records.
5. **Exploratory Data Analysis (EDA)**: Analyzing the cleaned data to uncover valuable insights and identify trends.

### 📊 Sample SQL Queries

**1. Creating Staging Table**

Create a staging table to duplicate the original data, allowing for safe manipulation:

```sql
CREATE TABLE layoffs_staging
LIKE layoffs;
```

**2. Removing Duplicate Records**

Find and remove duplicate rows based on multiple columns to ensure unique entries:

```
-- Identify duplicates
WITH duplicate_cte AS (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, date
      ORDER BY (SELECT NULL)
    ) AS row_num
  FROM layoffs_staging
)

-- Remove duplicates
DELETE FROM layoffs_staging
WHERE row_num > 1; 
```

*The query above uses a Common Table Expression (CTE) to identify duplicates.
It assigns a row number to each row partitioned by specific columns: company, location, industry, total_laid_off, percentage_laid_off, and date.*


**3. Standardize Data**

Trim whitespace from text fields and update inconsistent values:

```
-- Trim whitespace from company names
UPDATE layoffs_staging
SET company = TRIM(company);

-- Standardize industry names
UPDATE layoffs_staging
SET industry = 'Crypto'
WHERE industry LIKE 'Crypto%';

-- Trim trailing periods from country names
UPDATE layoffs_staging
SET country = TRIM(TRAILING '.' FROM country)
WHERE country LIKE 'United States%';
```
 *These updates standardize the company, industry, and country fields by removing unnecessary whitespace and correcting inconsistent values.*

**4. Handle Missing Values**

Replace or remove records with missing or blank values:

```
-- Replace empty industry names with NULL
UPDATE layoffs_staging
SET industry = NULL
WHERE industry = '';

-- Remove records with missing values in critical columns
DELETE FROM layoffs_staging
WHERE total_laid_off IS NULL AND percentage_laid_off IS NULL;

```
*The first query updates empty industry values to NULL. The second query deletes records where both total_laid_off and percentage_laid_off are missing, which ensures that only complete records remain.*
``` ```


### 📈 Exploratory Data Analysis (EDA)

**Key Points of EDA:**

1. **Summary Statistics:**
   - Determine maximum and minimum values for key metrics such as `total_laid_off` and `percentage_laid_off` to understand the range and distribution of the data.

2. **Group and Aggregate:**
   - Summarize data by `company`, `industry`, and `country` to identify which entities have the highest total layoffs, providing insights into the most affected areas.

3. **Trend Analysis:**
   - Analyze trends over time to identify patterns. This includes:
     - **Yearly Trends**: Summarize layoffs by year to observe annual changes.
     - **Monthly Trends**: Examine monthly data to detect seasonal or periodic patterns.
     - **Rolling Totals**: Calculate cumulative totals to visualize overall trends over time.



## 🌐 Amazon Web Scraping Project

#### Project Overview

This project involves scraping product information from an Amazon product page. The aim is to collect data about product titles and ratings regularly and save this data for analysis.

#### 🛠️ Features

- **Scrape Product Data**: Extract product titles and ratings from Amazon.
- **Save Data to CSV**: Write the collected data to a CSV file.
- **Automate Data Collection**: Update the dataset with new data periodically.

#### 📦 Dependencies

- **BeautifulSoup**: For parsing HTML content.
- **Requests**: To fetch data from the web.
- **CSV**: For writing data to CSV files.
- **Pandas**: For data manipulation and analysis (optional).

#### 📝 Usage

1. **Install Dependencies**: Ensure you have the required Python libraries.
2. **Run the Script**: Execute the Python script to start scraping.
   ```bash
   python scraper.py
### 📝 Usage

- **View Data**: Check the `AmazonWebScraperDataset.csv` file for the latest data.

### 📊 Example Output

| Title         | Ratings | Date       |
|---------------|---------|------------|
| Product    | 4.5     | 2024-08-13 |

### 🧩 Code Snippets

**Scrape Product Title and Ratings**

```python
from bs4 import BeautifulSoup
import requests
import csv
import datetime

# Scrape product title and ratings
URL = 'https://www.amazon.com/...'
headers = {"User-Agent": "Mozilla/5.0 ..."}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id='productTitle').get_text().strip()
ratings = soup.find(id='acrPopover').get_text().strip()
today = datetime.date.today()

# Save data to CSV
header = ['Title', 'Ratings', 'Date']
data = [title, ratings, today]

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
```
### 🌟 Highlights

- **Automated Data Collection**: Keeps your dataset up-to-date with the latest product information.
- **Easy Data Access**: Stores data in a CSV file for convenience.


