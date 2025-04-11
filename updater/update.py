import requests
import os
import zipfile
import io

REPO_URL = "https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/releases/latest"
DOWNLOAD_DIR = os.path.abspath(".")

def check_and_update():
    try:
        response = requests.get(REPO_URL)
        response.raise_for_status()
        data = response.json()
        zip_url = data["zipball_url"]
        version_tag = data["tag_name"]

        if not os.path.exists(".version") or open(".version").read().strip() != version_tag:
            print("Update available. Downloading...")
            zip_resp = requests.get(zip_url)
            z = zipfile.ZipFile(io.BytesIO(zip_resp.content))
            z.extractall(DOWNLOAD_DIR)
            with open(".version", "w") as f:
                f.write(version_tag)
            return True
        return False
    except Exception as e:
        print(f"Update check failed: {e}")
        return False
