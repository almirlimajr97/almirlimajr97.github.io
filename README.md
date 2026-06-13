# almirlimajr97.github.io

Personal website of Almir Lima Jr.

Live at: [almirlimajr97.github.io](https://almirlimajr97.github.io)

## Built with Claude

This site was built with the help of [Claude](https://claude.ai), Anthropic's AI assistant — from the initial design and layout to the automation workflows for posts and SEO.

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
├── files/                  # PDFs and other static files
├── sitemap.xml             # Auto-generated (do not edit manually)
├── robots.txt
├── post-template.html      # Starting point for new posts (manual workflow)
└── .github/
    ├── scripts/
    │   ├── generate_post.py    # Generates post HTML from form inputs
    │   ├── update_posts.py     # Updates posts.json and sitemap.xml
    │   └── post_template.html  # HTML template used by new-post workflow
    └── workflows/
        ├── deploy.yml          # Deploys the site on push
        ├── update-posts.yml    # Auto-updates posts.json and sitemap.xml when a new post is added
        └── new-post.yml        # Creates a new post via GitHub Actions form
```

## Adding a new post

### Option 1 — GitHub Actions form (recommended)

1. Go to **Actions → New post → Run workflow**
2. Fill in the fields:
   - **Title** — full post title
   - **Date** — e.g. `Jun 2026`
   - **Content** — Markdown (`##` for sections, `**bold**`, `[text](url)`)
   - **Acknowledgements** — optional, supports Markdown links
   - **PDF filename** — optional, e.g. `myfile.pdf` (must be in `/files/`)
   - **Slug** — optional file name (auto-generated from title if blank)
3. Click **Run workflow** — the post is created, `posts.json` and `sitemap.xml` are updated, and the site is deployed automatically.

### Option 2 — Manual

1. Duplicate `post-template.html` and rename it (e.g. `my-new-post.html`)
2. Fill in the required fields:
   - `<meta name="post-title">` and `<meta name="post-date">` — auto-set the browser tab title
   - The visible `<h1>` and date in the body
   - The post content inside `<article>`
3. Move the file to the `posts/` folder
4. Push to master:

```bash
git add posts/my-new-post.html
git commit -m "New post: title"
git push origin master
```

The `update-posts.yml` workflow automatically updates `posts.json` and `sitemap.xml`, and `deploy.yml` republishes the site.

## SEO

- `sitemap.xml` and `robots.txt` are in place for search engine crawling
- The site is verified on [Google Search Console](https://search.google.com/search-console)
- The sitemap is auto-updated whenever a new post is added

## Tech stack

Plain HTML, CSS, and JavaScript — no frameworks, no build step. Hosted on GitHub Pages via GitHub Actions.
