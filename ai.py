from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def extract_client_names(note_content):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Extract all client names from this note. Return ONLY the names as a comma-separated list, nothing else.

Note: {note_content}"""
            }
        ]
    )
    
    response_text = message.content[0].text.strip()
    
    if response_text:
        names = [name.strip() for name in response_text.split(',')]
        return names
    return []