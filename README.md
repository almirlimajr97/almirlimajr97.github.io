# almirlimajr97.github.io

Personal website of Almir Lima Jr. — Economist & Data Scientist.

Live at: [almirlimajr97.github.io](https://almirlimajr97.github.io)

## Structure

```
almirlimajr97.github.io/
├── index.html              # Home
├── cv/
│   └── index.html          # CV (embedded PDF)
├── research/
│   └── index.html          # Papers & Writings
├── posts/
│   ├── posts.json          # Auto-generated index (do not edit manually)
│   └── *.html              # Individual posts
├── assets/
│   └── files/              # PDFs and other files
├── favicon.svg
├── headshot.jpeg
└── .github/
    └── workflows/
        ├── deploy.yml          # Deploys the site on push
        └── update-posts.yml    # Auto-updates posts.json when a new post is added
```

## Adding a new post

1. Duplicate `post-template.html` and rename it (e.g. `my-new-post.html`)
2. Fill in the required fields:
   - `<title>` in `<head>`
   - `<meta name="post-title">` and `<meta name="post-date">` tags
   - The visible `<h1>` and date in the body
   - The post content inside `<article>`
3. Move the file to the `posts/` folder
4. Push to master:

```bash
git add posts/my-new-post.html
git commit -m "New post: title"
git push origin master
```

The `update-posts.yml` workflow will automatically update `posts.json`, and the `deploy.yml` workflow will republish the site. The post will appear on the Research page sorted by date.

## Tech stack

Plain HTML, CSS, and JavaScript — no frameworks, no build step. Hosted on GitHub Pages via GitHub Actions.
