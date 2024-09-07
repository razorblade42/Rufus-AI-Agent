from bs4 import BeautifulSoup
import requests
from rufus.utils import filter_relevant_content, summarize_content
import json

class RufusAgent:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape(self, url, instructions):
        """Scrape the given URL and return structured, relevant data."""
        full_url = f"{self.base_url}/{url}" if not url.startswith("http") else url
        response = requests.get(full_url)

        if response.status_code != 200:
            raise Exception(f"Failed to access {url}")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Selectively filter content based on user instructions
        relevant_content = filter_relevant_content(soup, instructions)

        # Summarize and synthesize content into a structured format
        structured_content = summarize_content(relevant_content)

        return structured_content

    def save_to_json(self, structured_content, filename="scraped_data.json"):
        """Save the structured content to a new JSON file."""
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(structured_content, json_file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")