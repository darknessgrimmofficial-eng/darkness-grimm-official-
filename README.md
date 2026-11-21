# Darkness Grimm — GitHub-only control

This version works on GitHub Pages without Firebase or any paid service.

## What it does

Only GitHub users with **write access** to this repository can run the content forms. Everyone else can only view the public website.

- **Actions → Manage videos → Run workflow**: add, edit, hide, show, delete, re-order, or mark a featured video.
- **Actions → Manage website settings → Run workflow**: edit About text, title, tagline, announcement, colours, channel/social/email links, and footer wording.
- **Actions → Manage genres → Run workflow**: add, rename, describe, or delete genres.
- The workflow commits the change automatically. GitHub Pages then publishes it, normally within a few minutes.

## Uploading this update

Keep the existing `assets` folder in the repository. Upload all the files and folders in this package to the **root** of `darkness-grimm-official`, replacing the existing `index.html` when GitHub asks.

The `.github` folder is important: it enables the Actions forms. GitHub may hide this folder after upload because its name begins with a dot; that is normal.

## Limits of GitHub-only publishing

GitHub Pages is a static website. It cannot provide a secure login/dashboard inside the public website or store direct video uploads. Use YouTube links for videos and image URLs for custom thumbnails. A real in-site admin dashboard needs Firebase or another backend.
