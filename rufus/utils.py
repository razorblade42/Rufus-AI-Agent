from transformers import pipeline
import re


def filter_relevant_content(soup, instructions):
    """Filter and retrieve content from the soup based on the user's instructions."""
    instructions_keywords = instructions.split()  # Extract keywords from the instructions
    relevant_content = []

    # Check relevant tags for content
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'a']):
        tag_text = tag.get_text(strip=True)

        # Match content based on the keywords in instructions
        for keyword in instructions_keywords:
            if re.search(rf"\b{keyword.lower()}\b", tag_text.lower()):
                relevant_content.append(tag_text)
                break  # Stop checking after a match to avoid duplications

    return " ".join(relevant_content)


def summarize_content(content):
    """Summarize the filtered content into a concise, structured format."""
    summarizer = pipeline("summarization")
    summarized = summarizer(content, max_length=150, min_length=50, do_sample=False)
    return summarized[0]['summary_text']
