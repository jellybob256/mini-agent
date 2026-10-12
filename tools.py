# tools.py

def calculator(prompt: str) -> str:
    """
    Extract a simple math expression and compute it.
    Example: "calculate 23*45" -> "1035"
    """
    import re

    match = re.search(r'(\d+[\+\-\*/]\d+)', prompt)
    if match:
        expr = match.group(1)
        return str(eval(expr))
    return "No calculation found."

def weather_api(prompt: str) -> str:
    """
    Simple fake weather API for now.
    """
    if "New York" in prompt:
        return "New York: 22°C, sunny"
    elif "London" in prompt:
        return "London: 15°C, cloudy"
    return "Weather info not available."

def joke(prompt: str) -> str:
    """
    Return a simple joke.
    """
    return "Why did the AI cross the road? To optimize its path!"
