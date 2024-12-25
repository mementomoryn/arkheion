# Arkheion (WIP)

_**Ever feel annoyed of missing songs you once liked because it's removed from music streaming services?**_

Rest assured, **Arkheion** support downloading from various music streaming services.

**Arkheion** collects multiple python scripts to download songs, albums, and even playlists in the best quality.

With **Arkheion**, you can easily download favorite songs you wanted to archive.

Why use **Arkheion** instead of running the scripts directly in your device:
- Entirely ran with GitHub-hosted runners through Actions, so it's really fast.
- Provide a simple input GUI, so it's much easier to use.
- Downloads is uploaded as GitHub Artifacts, allowing you to share previously downloaded songs with just a link.
- Works in practically every devices, as long as it could invoke GitHub Actions workflows 

## Usage

1. [Star](../../stargazers) this repository 🌟
2. Open the repository [Actions page](../../actions).
3. Pick one of the [_module_](#modules) workflows you want to use (e.g. Streamrip).
4. Press the `run workflow` button and input the info.
5. Done!

> [!IMPORTANT]
> To request downloads, you must have collaborator access.

## Modules

### Streamrip

[![GitHub Repo stars](https://img.shields.io/github/stars/nathom/streamrip?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/nathom/streamrip)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/streamrip.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/streamrip.yml)

| Services | Sources      |
| :------- | :----------- |
| Qobuz    | Direct[^1]   |
| Deezer   | Direct[^1]   |
| Tidal    | Direct[^1]   |
| Last.fm  | Fallback[^2] |

### SpotDL

[![GitHub Repo stars](https://img.shields.io/github/stars/spotDL/spotify-downloader?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/spotDL/spotify-downloader)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/spotdl.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/spotdl.yml)

| Services      | Sources       |
| :------------ | :------------ |
| Spotify       | Fallback [^2] |
| YouTube Music | Direct[^1]    |

[^1]: Downloads directly from respective services.
[^2]: Downloads duplicate from other services.