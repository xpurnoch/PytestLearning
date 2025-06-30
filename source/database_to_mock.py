import requests
database: dict[int, str] = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user(user_id: int) -> str:
    return database.get(user_id, "None")

def fetch_users() -> list[dict]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError(f"Failed to fetch users: {response.status_code}")