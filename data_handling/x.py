import re

def validate_input(text):
    # Define regex patterns
    url_pattern = re.compile(r'\b(https?://)?(www\.)?((?!mawad\.ae).)*\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    
    # Define allowed email and URL pattern
    allowed_email = "hello@mawadonline.com"
    allowed_url_pattern = re.compile(r'\b(https?://)?(www\.)?mawad\.ae\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

    # Find all URLs and emails in the text
    urls = url_pattern.findall(text)
    emails = email_pattern.findall(text)

    # Validate URLs
    for url in urls:
        if not allowed_url_pattern.match(url[0]):
            print(f"Invalid URL found: {url[0]}")
            return False
    
    # Validate Emails
    for email in emails:
        if email != allowed_email:
            print(f"Invalid email found: {email}")
            return False

    return True

# Get user input
user_input = input("Enter your text: ")

# Validate user input
if validate_input(user_input):
    print("Text is valid.")
else:
    print("Text contains invalid URLs or emails.")
