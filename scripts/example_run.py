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

