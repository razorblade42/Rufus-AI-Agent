from rufus.agent import RufusAgent

if __name__ == "__main__":
    # Path to the ChromeDriver executable
    SELENIUM_DRIVER_PATH = 'C:/Users/araj0/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe';
    # Initialize the Rufus Agent
    rufus = RufusAgent(2,1,SELENIUM_DRIVER_PATH)

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
    result = rufus.scrape(url="https://www.amazon.in/s?k=amazon+shoes&adgrpid=64475670368&ext_vrnc=hi&hvadid=590593835457&hvdev=c&hvlocphy=9299565&hvnetw=g&hvqmt=e&hvrand=3246560036712660643&hvtargid=kwd-694970439&hydadcr=22282_2255478&tag=googinhydr1-21&ref=pd_sl_7zivw3v566_e", instructions=instructions)

    # Print the structured output
    print("Scraped and Structured Content: \n", result)

    # Save the result to a JSON file
    # rufus.save_to_json(result, filename="output.json")

