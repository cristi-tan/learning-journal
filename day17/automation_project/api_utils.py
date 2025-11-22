#Responsible only for API calls:
import requests
from config import API_BASE_URL

def get_user_details(user_id: str) -> dict:
    url = f"{API_BASE_URL}/users/{user_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "name": data.get("name", "N/A"),
            "username": data.get("username", "N/A"),
            "email": data.get("email", "N/A"),
            "city": data.get("address", {}).get("city", "N/A")
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user {user_id}: {e}")
        return {
            "name": f"User {user_id}",
            "username": "unknown",
            "email": "unknown",
            "city": "unknown"
        }

