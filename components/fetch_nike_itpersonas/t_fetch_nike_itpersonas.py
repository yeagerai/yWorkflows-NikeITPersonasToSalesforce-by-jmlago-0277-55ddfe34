
# test_fetch_nike_it_personas.py
import pytest
from pydantic import BaseModel
from typing import Dict, List
from fastapi.testclient import TestClient
from your_module_path import FetchNikeITPersonas, FetchNikeITPersonasInputDict, FetchNikeITPersonasOutputDict, fetch_nike_it_personas_app

client = TestClient(fetch_nike_it_personas_app)

test_cases = [
    (
        FetchNikeITPersonasInputDict(AccessToken="valid_access_token"),
        FetchNikeITPersonasOutputDict(
            PersonasData=[
                {
                    "id": "123",
                    "name": "John Doe",
                    "title": "Software Engineer",
                },
                {
                    "id": "456",
                    "name": "Jane Doe",
                    "title": "Project Manager",
                },
            ]
        ),
    ),
    (
        FetchNikeITPersonasInputDict(AccessToken="expired_access_token"),
        FetchNikeITPersonasOutputDict(PersonasData=[]),
    ),
    (
        FetchNikeITPersonasInputDict(AccessToken="invalid_access_token"),
        FetchNikeITPersonasOutputDict(PersonasData=[]),
    ),
]

@pytest.mark.parametrize("mocked_input, expected_output", test_cases)
def test_fetch_nike_it_personas(monkeypatch, mocked_input, expected_output):
    # Mock the requests.get function
    def mock_requests_get(url, headers):
        if headers["Authorization"] == f"Bearer {mocked_input.AccessToken}":
            if mocked_input.AccessToken == "valid_access_token":
                return MockResponse(
                    data=[
                        {
                            "id": "123",
                            "name": "John Doe",
                            "title": "Software Engineer",
                        },
                        {
                            "id": "456",
                            "name": "Jane Doe",
                            "title": "Project Manager",
                        },
                    ]
                )
            else:
                return MockResponse(data=[])
        else:
            return MockResponse(data=[], status_code=403)

    # Patch the requests.get method
    monkeypatch.setattr(requests, "get", mock_requests_get)

    # Call the transform() method with mocked input
    fetch_nike_it_personas = FetchNikeITPersonas()
    result = fetch_nike_it_personas.transform(mocked_input)

    # Assert that the output matches the expected output
    assert result == expected_output

@pytest.mark.parametrize("mocked_input, expected_output", test_cases)
def test_fetch_nike_it_personas_endpoint(mocked_input, expected_output):
    with TestClient(fetch_nike_it_personas_app) as client:
        response = client.post("/transform/", json=mocked_input.dict())
        assert response.status_code == 200
        assert response.json() == expected_output.dict()

# MockResponse class for requests.get function
class MockResponse:
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def json(self):
        return {"elements": self.data}

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"Error: {self.status_code}")
