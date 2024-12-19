import requests
import re
from dataclasses import dataclass
from utils import download

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7,application/vnd.github+json",
    "authorization": "Bearer ${GH_TOKEN}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

@dataclass
class Asset:
    browser_download_url: str
    name: str

@dataclass
class GithubRelease:
    tag_name: str
    html_url: str
    body: str
    assets: list[Asset]

def count_releases(repo_url: str) -> int | None:
    url = f"https://api.github.com/repos/{repo_url}/releases"
    response = requests.get(url, headers=HEADERS)

    print("Get count releases of " + repo_url + ": " + str(response.status_code))
    if response.status_code == 200:
        release = response.json()
        
        count = len(release)
        return count
    elif response.status_code == 404:
        return

def get_last_build_version(repo_url: str, prerelease: bool = False) -> GithubRelease | None:
    url = f"https://api.github.com/repos/{repo_url}/releases"

    if prerelease is False:
        url += "/latest"

    response = requests.get(url, headers=HEADERS)

    print("Get latest releases of " + repo_url + ": " + str(response.status_code))
    if response.status_code == 200:

        if prerelease is True:
            release = response.json()[0]
        else:
            release = response.json()

        assets = [
            Asset(
                browser_download_url=asset["browser_download_url"], name=asset["name"]
            )
            for asset in release["assets"]
        ]

        return GithubRelease(
            tag_name=release["tag_name"], html_url=release["html_url"], body=release["body"], assets=assets
        )
    elif response.status_code == 404:
        return

def download_release_asset(repo: str, regex: str, prerelease: bool, out_dir: str, filename=None, version=None):
    url = f"https://api.github.com/repos/{repo}/releases"

    if prerelease is False and not version:
        url += "/latest"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch github")

    if version:
        response = [i for i in response.json() if prerelease is False]
        release = [i for i in response if i["tag_name"] == version][0]
        
        if len(release) == 0:
            raise Exception(f"No release found for version {version} on {repo}")
    elif prerelease is True:
        release = response.json()[0]
    else:
        release = response.json()
        
    if not release:
        raise Exception(f"No release found for {repo}")

    link = None
    for i in release["assets"]:
        if re.search(regex, i["name"]):
            link = i["browser_download_url"]
            if filename is None:
                filename = i["name"]
            break

    download(link, f"{out_dir.lstrip("/")}/{filename}")