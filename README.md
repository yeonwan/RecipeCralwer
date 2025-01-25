# RecipeCrawler

**RecipeCrawler** is a Python-based web scraping project designed to collect recipes from the "Maangchi" recipe website. It includes modules for crawling recipe data, storing the collected information, and editing or processing the data.

---

## Table of Contents
1. [Introduction](#introduction)
2. [File Overview](#file-overview)
3. [Installation](#installation)
4. [How to Run](#how-to-run)
---

## Introduction
**RecipeCrawler** automates the process of extracting recipe data from "Maangchi" and storing it in a structured format for further use. This project is useful for collecting data for recipe analysis, food blogs, or building datasets for cooking-related applications.

---

## File Overview

- **editjson.py**
  - Provides functionality to edit or process the JSON data extracted from the recipe website. Useful for cleaning, updating, or reformatting the stored recipes.

- **recipeCrawler.py**
  - The core web scraping script that extracts recipe data from "Maangchi." This script handles crawling, parsing, and extracting the relevant information from the website's pages.

- **storeRecipe.py**
  - Manages the storage of crawled recipe data into structured formats, such as JSON or a database. Ensures data integrity and easy retrieval for further processing or analysis.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/RecipeCrawler.git
   cd RecipeCrawler
   ```

2. **Set Up Python Environment**
   - Ensure you have **Python 3.6+** installed.
   - Create and activate a virtual environment (recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Linux/Mac
     venv\Scripts\activate     # On Windows
     ```

3. **Install Dependencies**
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```
   - If `requirements.txt` is unavailable, ensure you have libraries like `requests`, `BeautifulSoup4`, and `json` installed.

---

## How to Run

1. **Run the Crawler**
   - Execute the main crawler script to start scraping recipes:
     ```bash
     python recipeCrawler.py
     ```

2. **Store the Data**
   - After crawling, use `storeRecipe.py` to save the extracted recipes:
     ```bash
     python storeRecipe.py
     ```

3. **Edit the Stored Data**
   - Use `editjson.py` to modify or clean the stored recipe data:
     ```bash
     python editjson.py
     ```

---

## Usage

- **Customizing the Scraper**
  - Modify `recipeCrawler.py` to specify the number of recipes or specific categories to scrape.

- **Data Cleaning**
  - Use `editjson.py` to clean and preprocess the stored data.

- **Integration**
  - Integrate the stored recipe data into other applications, such as recipe search engines or food recommendation systems.


