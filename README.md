# Priyanka Rauniyar | Analytics Portfolio

A responsive Streamlit portfolio for business analytics, BI, data science, and healthcare analytics work.

## Run locally

Use Python 3.9 or newer (Python 3.12 is recommended for a fresh environment).

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, normally `http://localhost:8501`. The app requires no API keys or backend form service. The portrait and resume are loaded from the existing local files `image.jpg` and `PriyankaRauniyar_Resume.pdf`.

## Project content

Project cards and dedicated case studies are driven by [`data/portfolio.json`](data/portfolio.json). The Projects page shows all projects directly, without filters. To add work, add an object to the `projects` list using the existing fields: `id`, `title`, `category`, `areas`, `problem`, `contribution`, `methods`, `outcome`, `links`, `context`, `data`, `approach`, `validation`, `interpretation`, `limitations`, and `source`. `visual` is optional and supports repository images, verified confusion-matrix data, or factual workflow steps; do not use invented data to fill a chart. The `featured` field selects the overview project. Readmission-only fields (`test_encounters`, `historical_predictions`, and `metrics`) keep the held-out evaluation distinct from historical exploration.

Only include facts supported by a public artifact or approved for publication. The summer bank employee-expertise case study presents the completed institution-matching phase: the broader 69.8M+ employment source, a final accepted bridge of 5,156 unique RCIDs, 12 professor-approved additions to the preceding version, and zero duplicate RCIDs. Employee-level merging and lending analysis were not completed in this phase. It includes no employment records, mappings, unpublished lending findings, or restricted code; review aggregate metrics and methodology with the supervising professor before publishing. PantryPulse links to the user-provided dashboard URL and source repository; its documented operational visit history and capacity are simulated. Check the live URL before sharing publicly. Do not put raw datasets, unpublished research, identifiers, credentials, or private API keys in this repository. Local Streamlit secrets belong in `.streamlit/secrets.toml`, which is ignored by Git.

## Deploy on Streamlit Community Cloud

1. Push this repository to a GitHub repository that you control. Keep `app.py`, `portfolio.py`, the `pages/` directory, `data/portfolio.json`, `requirements.txt`, `image.jpg`, `PriyankaRauniyar_Resume.pdf`, and the `static/` certificate PDFs, and `.streamlit/config.toml` together in the repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub and choose **Create app**.
3. Select the repository and branch, set the main file path to `app.py`, and deploy. Python 3.12 is recommended; the app does not need secrets.
4. After deployment, open Home, Projects, Experience, and Contact; test navigation, project case-study links, the resume download, certificates opening in a browser tab, contact links, and both live dashboard links. Confirm that the live dashboard is accessible to intended visitors.

## Files

- `app.py`: Streamlit app setup and navigation.
- `pages/`: Home, Projects, Experience, Education, Achievements, Skills, and Contact.
- `portfolio.py`: shared content loading, scoped theme styles and reusable project cards.
- `data/portfolio.json`: structured project content.
The PDFs in `static/` are intentionally public. Streamlit serves them through `/app/static/` with inline PDF content type so the browser can open them.
