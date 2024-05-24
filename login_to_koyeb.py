import os
import requests

def login_to_koyeb(api_token):
    url = "https://app.koyeb.com/v1/login"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Successfully logged in to Koyeb.")
    else:
        print(f"Failed to log in to Koyeb: {response.status_code} {response.text}")

if __name__ == "__main__":
    api_token = os.getenv("KOYEB_API_TOKEN")
    if not api_token:
        raise ValueError("KOYEB_API_TOKEN environment variable is not set")

    login_to_koyeb(api_token)
