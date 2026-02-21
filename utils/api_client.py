import requests
from utils.config import BASE_URL


class APIClient:

    @staticmethod
    def get_posts():
        return requests.get(f"{BASE_URL}/posts")

    @staticmethod
    def get_post_by_id(post_id):
        return requests.get(f"{BASE_URL}/posts/{post_id}")

    @staticmethod
    def create_post(payload):
        return requests.post(f"{BASE_URL}/posts", json=payload)