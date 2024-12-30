# Arkheion

[ENGLISH](README.md) | **INDONESIAN**

_**Pernah kesal karena lagu favorit kamu hilang dari platform streaming musik?**_

Tenang aja, **Arkheion** bisa download dari berbagai platform streaming musik.

**Arkheion** mengumpulkan beberapa aplikasi python sehingga bisa download track, album, playlist, dll dengan kualitas terbaik.

Dengan **Arkheion**, kamu bisa dengan mudah download lagu favoritmu.

Kenapa pilih **Arkheion** dibanding menjalankan aplikasi langsung di perangkatmu:

- Dijalankan dengan runner GitHub Actions, jadi prosesnya cepat banget.
- Ada interface input yang sederhana, buat ini lebih mudah dipakai.
- Diunggah sebagai GitHub Artifacts, jadi kamu bisa share apa yang sudah didownload hanya dengan link.
- Bisa dipakai untuk hampir semua perangkat, selama bisa menjalankan alur kerja GitHub Actions.

## Cara Pakai

1. [Star](../../stargazers) repositori ini 🌟
2. Buka halaman [Actions](../../actions).
3. Pilih salah satu alur kerja [_modul_](#modules) yang kamu mau pakai (misalnya Streamrip).
4. Tekan tombol `run workflow` dan isi informasi.
5. Buka _workflow run_ yang udah kamu jalankan, dan tunggu sampai prosesnya selesai.
6. Unduh _artifacts_.
7. Selesai!

> [!IMPORTANT]
> Untuk request dan download, kamu perlu punya akses collaborator.

## Modul

### Streamrip

[![GitHub Repo stars](https://img.shields.io/github/stars/nathom/streamrip?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/nathom/streamrip)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/streamrip.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/streamrip.yml)

| Platform | Sumber       |
| :------- | :----------- |
| Qobuz    | Direct[^1]   |
| Deezer   | Direct[^1]   |
| Tidal    | Direct[^1]   |
| Last.fm  | Fallback[^2] |

> [!TIP]
> Untuk download lebih dari satu, kamu bisa pake '&&' (tanda petiknya gausah) di antara query.

### SpotDL

[![GitHub Repo stars](https://img.shields.io/github/stars/spotDL/spotify-downloader?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/spotDL/spotify-downloader)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/spotdl.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/spotdl.yml)

| Platform      | Sumber        |
| :------------ | :------------ |
| Spotify       | Fallback [^2] |
| YouTube Music | Direct[^1]    |

> [!TIP]
> Untuk download lebih dari satu, kamu bisa pake '&&' (tanda petiknya gausah) di antara query.

### TidalDLNG

> Rusak, gak ada support buat custom path

[![GitHub Repo stars](https://img.shields.io/github/stars/exislow/tidal-dl-ng?style=for-the-badge&logo=github&logoColor=FFFFFF&label=Stars&labelColor=444444&color=222333)](https://github.com/exislow/tidal-dl-ng)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mementomoryn/arkheion/tidal-dl-ng.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=FFFFFF&label=workflows&labelColor=444444)](../../actions/workflows/tidal-dl-ng.yml)

| Platform | Sumber      |
| :------- | :---------- |
| Tidal    | Direct [^1] |

[^1]: Arsip langsung dari platform yang kamu pilih.
[^2]: Arsip duplikat yang cocok dari platform yang lain.
