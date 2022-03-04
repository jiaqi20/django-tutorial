from django.urls import reverse
#from django.test import Client

def test_nothing():
    """A dummy test"""
    assert True

def test_index_view(client):
    """Test that polls view works"""
    # Build the URL from the url's name
    url = reverse("index")
    # Make a GET request to the view using the test client
    response = client.get(url)
    # Verify that the response code is correct
    assert response.status_code == 200
    # Verify that the response body is correct
    assert response.content == b"Hello, world. You're at the polls index."
