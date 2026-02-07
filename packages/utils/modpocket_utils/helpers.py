"""Utility helper functions."""


def format_text(text: str, uppercase: bool = False) -> str:
    """Format text with optional uppercase conversion.
    
    Args:
        text: The text to format
        uppercase: Whether to convert to uppercase
        
    Returns:
        Formatted text
    """
    formatted = text.strip()
    if uppercase:
        formatted = formatted.upper()
    return formatted


def chunk_list(lst: list, size: int) -> list:
    """Split a list into chunks of specified size.
    
    Args:
        lst: The list to chunk
        size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]
