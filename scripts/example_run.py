from rufus.agent import RufusAgent

if __name__ == "__main__":
    # Initialize the Rufus Agent
    rufus = RufusAgent(base_url="https://www.sf.gov/")

    # Provide custom user instructions
    instructions = "We're making a chatbot for the HR in San Francisco."

    # Scrape the site using the agent
    result = rufus.scrape(url="", instructions=instructions)

    # Print the structured output
    print("Scraped and Structured Content: \n", result)

    # Save the result to a JSON file
    rufus.save_to_json(result, filename="output.json")
