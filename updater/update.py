import requests
import zipfile
import io
import os
import sys
import subprocess

GITHUB_REPO = "https://api.github.com/repos/YOUR_USERNAME/sublime_scrapper_pro/releases/latest"

def check_for_update():
    try:
        response = requests.get(GITHUB_REPO)
        data = response.json()
        latest_version = data["tag_name"]
        asset = next((a for a in data["assets"] if a["name"].endswith(".zip")), None)
        if asset:
            return latest_version, asset["browser_download_url"]
    except Exception as e:
        print(f"Update check failed: {e}")
    return None, None

def apply_update(download_url):
    try:
        response = requests.get(download_url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall("update_tmp")

        # Overwrite files
        for root, _, files in os.walk("update_tmp"):
            for f in files:
                src = os.path.join(root, f)
                dst = os.path.join(".", os.path.relpath(src, "update_tmp"))
                os.replace(src, dst)

        # Cleanup
        os.remove("update_tmp")

        # Relaunch
        print("✅ Update applied. Restarting...")
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit(0)

    except Exception as e:
        print(f"Failed to apply update: {e}")
