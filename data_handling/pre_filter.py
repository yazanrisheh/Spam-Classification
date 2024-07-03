import re


def validate_input_pre_model(text):
    url_pattern = re.compile(
        r"\bhttps?://(?:www\.)?[\w.-]+\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*"
    )
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

    allowed_email = "hello@mawadonline.com"
    allowed_url_pattern = re.compile(r"https?://(?:www\.)?mawadonline\.com/.*")

    urls = url_pattern.findall(text)
    emails = email_pattern.findall(text)

    for url in urls:
        if not allowed_url_pattern.match(url):
            print(f"Invalid URL found: {url}")  # Log invalid URL for internal tracking
            return False  # Only returning the boolean status

    for email in emails:
        if email != allowed_email:
            print(
                f"Invalid email found: {email}"
            )  # Log invalid email for internal tracking
            return False  # Only returning the boolean status

    return True
