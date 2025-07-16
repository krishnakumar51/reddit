def generate_persona(username, characteristics):
    """Format the persona from Gemini’s raw output."""
    # If Gemini didn’t format perfectly, we’d parse here; for now, assume it follows prompt
    persona = f"{username.title()}\n\n{characteristics}"
    return persona