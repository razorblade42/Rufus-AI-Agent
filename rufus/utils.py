import re
import json


def filter_relevant_content_and_save(soup, instructions):
    """Filter and retrieve content from the soup based on the user's instructions, and return the content as
    structured JSON."""
    instructions_keywords = instructions.lower().split()  # Extract keywords from the instructions
    relevant_content = []  # Store relevant sections of content

    # Check relevant tags for content (e.g., headings, paragraphs, links)
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'a']):
        tag_text = tag.get_text(strip=True)

        # Match content based on keywords in instructions
        for keyword in instructions_keywords:
            if re.search(rf"\b{keyword.lower()}\b", tag_text.lower()):
                relevant_content.append({
                    "tag": tag.name,
                    "content": tag_text,
                    "url": tag.get('href') if tag.name == 'a' else None, # Include URL if it's a link
                #     also add the keyword that matched
                    "matched_keyword": keyword
                })
                break  # Stop checking after a match to avoid duplications

    # Prepare the content in a JSON-compatible format
    json_output = {
        "instructions": instructions,
        "results": relevant_content
    }

    # return json_output
#     instead of returning the json_output, we will save it to a json file
    save_to_json(json_output, "output.json")


def save_to_json(data, filename):
    """Save the extracted data to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data has been saved to {filename}")


