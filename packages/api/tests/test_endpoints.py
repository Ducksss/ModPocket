"""Tests for endpoints module."""

from modpocket_api.endpoints import APIEndpoint, create_endpoint


def test_api_endpoint_init():
    """Test APIEndpoint initialization."""
    endpoint = APIEndpoint("/users", "GET")
    assert endpoint.path == "/users"
    assert endpoint.method == "GET"


def test_api_endpoint_url():
    """Test APIEndpoint url method."""
    endpoint = APIEndpoint("/users")
    assert endpoint.url() == "/users"
    assert endpoint.url("https://api.example.com") == "https://api.example.com/users"


def test_create_endpoint():
    """Test create_endpoint factory function."""
    endpoint = create_endpoint("/posts", "POST")
    assert isinstance(endpoint, APIEndpoint)
    assert endpoint.path == "/posts"
    assert endpoint.method == "POST"
