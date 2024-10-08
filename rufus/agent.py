from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from rufus.utils import filter_relevant_content_and_save


class RufusAgent:
    def __init__(self, max_depth=2, delay=1, selenium_driver_path="", base_url="", max_urls_visited=10):
        """Initialize Rufus agent with base URL and other settings"""
        self.max_depth = max_depth  # Maximum depth for nested page scraping
        self.delay = delay  # Delay to avoid hitting websites too hard
        self.visited_urls = set()  # Track visited URLs to avoid scraping the same page
        self.selenium_driver_path = selenium_driver_path  # Path to the Selenium WebDriver
        self.base_url = base_url  # Base URL for the website
        self.max_urls_visited = max_urls_visited  # Maximum number of URLs to visit
        self.cur_url_visited = 0

    def scrape(self, path, instructions, depth=0):
        self.cur_url_visited += 1
        full_url = self.base_url + path
        print("Scraping with parameters: ", full_url, instructions, depth)
        """Main scraping function that handles links, nested pages, and dynamically-loaded content."""
        if depth > self.max_depth:
            return {}  # Stop further recursion when max depth is reached
        #
        # full_url = url.startswith('http') and url or "https://" + url  # Handle relative URLs

        # Avoid revisiting the same URLs
        if full_url in self.visited_urls:
            return {}
        self.visited_urls.add(full_url)

        # Use Selenium to handle dynamic content loading
        try:
            # Initialize Selenium WebDriver
            service = Service(
            )  # Update path to chromedriver
            driver = webdriver.Chrome(service=service)
            driver.get(full_url)
            time.sleep(self.delay)  # Wait for dynamic content to load

            # Get the page source and parse it with BeautifulSoup
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Close the WebDriver after loading the page
            driver.quit()

            # Filter content based on user instructions
            filter_relevant_content_and_save(soup, instructions)

            if self.cur_url_visited >= self.max_urls_visited:
                print(f"Maximum number of URLs visited ({self.max_urls_visited}) reached.")
                return

            # Recursively scrape nested pages by following links
            self.scrape_nested_links(soup, instructions, depth + 1)

        except Exception as e:
            print(f"Failed to scrape {full_url}: {e}")

    def scrape_nested_links(self, soup, instructions, depth):
        """Scrape nested links from the current page."""

        for link in soup.find_all('a', href=True):
            next_url = link['href']

            # Only follow relative links or same-domain absolute links
            if next_url.startswith('/') or next_url.startswith(self.base_url):
                # if next_url starts with self.base_url, we need to remove the base_url from the next_url, and it
                # should start with '/'
                if next_url.startswith(self.base_url):
                    next_url = next_url[len(self.base_url):]

                self.scrape(next_url, instructions, depth)

                if self.cur_url_visited >= self.max_urls_visited:
                    print(f"Maximum number of URLs visited ({self.max_urls_visited}) reached.")
                    return

