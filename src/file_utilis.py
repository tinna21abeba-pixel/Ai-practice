def save_text(filename, text):
    """Save text to a file."""
    with open(filename, "w") as file:
        file.write(text)