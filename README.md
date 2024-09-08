# Rufus - Intelligent Web Data Extraction for RAG Agents

## Overview

Rufus is an AI-powered web scraping agent designed to intelligently extract relevant content from websites based on user-defined prompts. This tool allows engineers to input brief instructions and dynamically retrieve, filter, and synthesize the most relevant data for downstream LLM applications, including Retrieval-Augmented Generation (RAG) agents.

## Features

- **Intelligent Crawling:** Crawl websites and selectively retrieve content based on user input.
- **Content Filtering:** Filter relevant content using NLP techniques and keyword matching.
- **Structured Output:** Synthesize content into structured documents ready for RAG systems.
- **Error Handling:** Handle nested pages, broken links, and dynamically-loaded content.

## Installation

1. Clone the repository:
    ```bash
    git clone 
    cd rufus
    ```

2. Install dependencies:
    ```bash
    conda activate <env_name>
    pip install -r requirements.txt
    ```

## Usage

You can use the `RufusAgent` to scrape content based on your instructions. Here's an example:

```python
from rufus.agent import RufusAgent

if __name__ == "__main__":
    # Path to the ChromeDriver executable
    SELENIUM_DRIVER_PATH = 'C:/Users/araj0/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
    # Base URL for the website to scrape
    BASE_URL = "https://www.amazon.in"
    # Maximum number of URLs to visit
    MAX_URLS_VISITED = 10
    # Maximum depth for nested page scraping
    MAX_DEPTH = 2
    # Delay to avoid hitting websites too hard
    DELAY = 1
    
    # Initialize the Rufus Agent
    rufus = RufusAgent(MAX_DEPTH, DELAY, SELENIUM_DRIVER_PATH, BASE_URL, MAX_URLS_VISITED)

    # Provide more detailed custom user instructions
    instructions = """
    Scrape the webpage and extract the following information:
    - Product names, descriptions, and features for shoes.
    - Pricing details, discounts, and offers.
    - Availability status of each product.
    - Customer reviews and ratings.
    - Brand and size details.
    - FAQs related to shoe purchases on the page.
    - Any additional details such as delivery options and return policies.
    """

    # Scrape the site using the agent
    result = rufus.scrape(
        path="/s?k=amazon+shoes&adgrpid=64475670368&ext_vrnc=hi&hvadid=590593835457&hvdev=c&hvlocphy=9299565&hvnetw=g"
             "&hvqmt=e&hvrand=3246560036712660643&hvtargid=kwd-694970439&hydadcr=22282_2255478&tag=googinhydr1-21&ref"
             "=pd_sl_7zivw3v566_e",
        instructions=instructions)

