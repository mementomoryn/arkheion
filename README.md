# Arkheion

**ENGLISH** | [INDONESIAN](IDN_README.md)

_**Ever feel annoyed of missing songs you once liked because it's removed from music streaming platforms?**_

Rest assured, **Arkheion** support archiving from various music streaming platforms.

**Arkheion** collects multiple python scripts to archive tracks, albums, playlists, etc in the best quality.

With **Arkheion**, you can easily archive your favorite songs.

Why use **Arkheion** instead of running the scripts directly in your device:

- Entirely ran with GitHub-hosted runners through Actions, so it's really fast.
- Provide a simple input GUI, so it's much easier to use.
- Uploaded as GitHub Artifacts, allowing you to share previously downloaded songs with just a link.
- Works in practically every devices, as long as it could invoke GitHub Actions workflows

## Usage

1. [Star](../../stargazers) this repository 🌟
2. Open the repository [Actions page](../../actions).
3. Pick one of the [_module_](#modules) workflows you wanted to use (e.g. Streamrip).
4. Press the `run workflow` button and fill out the inputs info.
5. Open _workflow run_ that you just ran, and wait until the _run_ is completed.
6. Download the _artifacts_.
7. Done!

> [!IMPORTANT]
> To request and download, you must have collaborator access.

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

> [!TIP]
> To download multiple at the same time, you should use '&&' (without the quotes) between the queries.

### SpotDL

[![GitHub Repo stars](https://img.shields.io/github/stars/spotDL/spotify-downloader?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/spotDL/spotify-downloader)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/spotdl.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/spotdl.yml)

| Services      | Sources       |
| :------------ | :------------ |
| Spotify       | Fallback [^2] |
| YouTube Music | Direct[^1]    |

> [!TIP]
> To download multiple at the same time, you should use '&&' (without the quotes) between the queries.

### gYTMdl

[![GitHub Repo stars](https://img.shields.io/github/stars/glomatico/gytmdl?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/glomatico/gytmdl)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/gytmdl.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/gytmdl.yml)

| Services      | Sources    |
| :------------ | :--------- |
| YouTube Music | Direct[^1] |

> [!TIP]
> To download multiple at the same time, you should use '&&' (without the quotes) between the queries.

### Votify

[![GitHub Repo stars](https://img.shields.io/github/stars/glomatico/votify?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/glomatico/votify)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/votify.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/votify.yml)

| Services | Sources    |
| :------- | :--------- |
| Spotify  | Direct[^1] |

> [!TIP]
> To download multiple at the same time, you should use '&&' (without the quotes) between the queries.

### TidalDLNG

> Broken, no support for custom paths

[![GitHub Repo stars](https://img.shields.io/github/stars/exislow/tidal-dl-ng?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/exislow/tidal-dl-ng)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/tidal-dl-ng.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/tidal-dl-ng.yml)

| Services | Sources     |
| :------- | :---------- |
| Tidal    | Direct [^1] |

[^1]: Archive directly from respective sources.
[^2]: Archive matching duplicate from other sources.
