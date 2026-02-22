import pytest
from utils.api_client import APIClient


class TestPostsAPI:

    def test_get_all_posts(self):
        response = APIClient.get_posts()

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list)
        assert len(data) > 0

        required_keys = {"userId", "id", "title", "body"}
        for key in required_keys:
            assert key in data[0]

    def test_get_post_by_id(self):
        
        response = APIClient.get_post_by_id(4)

        # Validate status code
        assert response.status_code == 200

        # Convert response to JSON
        data = response.json()

        expected_response = {
            "userId": 1,
            "id": 4,
            "title": "eum et est occaecati",
            "body": "ullam et saepe reiciendis voluptatem adipisci\n"
                    "sit amet autem assumenda provident rerum culpa\n"
                    "quis hic commodi nesciunt rem tenetur doloremque ipsam iure\n"
                    "quis sunt voluptatem rerum illo velit"
        }
        assert data == expected_response

    def test_create_post(self):
        payload = {
            "title": "Test Title",
            "body": "Test Body",
            "userId": 1
        }

        response = APIClient.create_post(payload)

        assert response.status_code == 201
        data = response.json()

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]

    def test_get_invalid_post(self):
        response = APIClient.get_post_by_id(999999)

        assert response.status_code == 404
