import os
import requests

def login_to_koyeb(api_token):
    url = "https://app.koyeb.com/v1/account"
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
    api_tokens = os.getenv("KOYEB_API_TOKENS")
    if not api_tokens:
        raise ValueError("KOYEB_API_TOKENS environment variable is not set")

    for token in api_tokens.split(','):
        token = token.strip()
        if token:
            login_to_koyeb(token)
