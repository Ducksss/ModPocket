"""API endpoint definitions."""


class APIEndpoint:
    """Base class for API endpoints."""
    
    def __init__(self, path: str, method: str = "GET"):
        """Initialize an API endpoint.
        
        Args:
            path: The endpoint path
            method: HTTP method (GET, POST, etc.)
        """
        self.path = path
        self.method = method
    
    def url(self, base_url: str = "") -> str:
        """Get the full URL for this endpoint.
        
        Args:
            base_url: Base URL to prepend
            
        Returns:
            Full endpoint URL
        """
        return f"{base_url}{self.path}"


def create_endpoint(path: str, method: str = "GET") -> APIEndpoint:
    """Factory function to create an API endpoint.
    
    Args:
        path: The endpoint path
        method: HTTP method
        
    Returns:
        APIEndpoint instance
    """
    return APIEndpoint(path, method)
