# download_file.py
import sys
import urllib.request

def download_file(url, file_name):
    try:
        urllib.request.urlretrieve(url, file_name)
        print("Download complete")
    except Exception as e:
        print("Error during download:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_file.py <url> <file_name>")
        sys.exit(1)

    url = sys.argv[1]
    file_name = sys.argv[2]
    download_file(url, file_name)

#python3 download_file.py https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip source.zip
