"""Shared data and presentation helpers for the Streamlit portfolio."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path
from typing import Any

import streamlit as st


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "portfolio.json"


def load_portfolio() -> dict[str, Any]:
    """Load the editable portfolio content from its structured JSON file."""
    with DATA_PATH.open(encoding="utf-8") as portfolio_file:
        return json.load(portfolio_file)


def project_by_id(project_id: str) -> dict[str, Any]:
    content = load_portfolio()
    return next(
        project for project in content["projects"] + content.get("research_internships", [])
        if project["id"] == project_id
    )


def filter_projects(
    projects: list[dict[str, Any]],
    query: str = "",
    selected_areas: list[str] | None = None,
    selected_tools: list[str] | None = None,
    status_filter: str = "All projects",
) -> list[dict[str, Any]]:
    """Filter projects by text, any selected area, all selected tools, and status."""
    normalized_query = query.strip().casefold()
    areas = set(selected_areas or [])
    tools = set(selected_tools or [])
    results = []

    for project in projects:
        project_areas = project.get("areas", [])
        project_methods = project.get("methods", [])
        searchable = " ".join([
            project["title"], project["category"], project["problem"],
            project["contribution"], project["outcome"], *project_methods, *project_areas,
        ]).casefold()
        if normalized_query and normalized_query not in searchable:
            continue
        if areas and not areas.intersection(project_areas):
            continue
        if tools and not tools.issubset(project_methods):
            continue
        is_ongoing = project.get("status") == "Ongoing"
        if status_filter == "Published projects" and is_ongoing:
            continue
        if status_filter == "Ongoing research" and not is_ongoing:
            continue
        results.append(project)

    return sorted(results, key=lambda item: (not item.get("featured", False), item["title"].casefold()))


def add_global_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');
        :root {
            --page: #101a16;
            --surface: #192720;
            --surface-quiet: #23372d;
            --ink: #f2f5ef;
            --muted: #c1d1c7;
            --line: #40594b;
            --accent: #8bd3ad;
            --accent-ink: #102219;
            --warm: #f0a18b;
            --hero: #203f34;
            --hero-text: #f7f7f0;
        }
        html[data-theme="dark"], [data-theme="dark"] {
            --page: #101a16;
            --surface: #192720;
            --surface-quiet: #23372d;
            --ink: #f2f5ef;
            --muted: #c1d1c7;
            --line: #40594b;
            --accent: #8bd3ad;
            --accent-ink: #102219;
            --warm: #f0a18b;
            --hero: #203f34;
            --hero-text: #f7f7f0;
        }
        .stApp {
            background: radial-gradient(ellipse at 78% 0%, rgba(62,97,72,.16), transparent 32rem), var(--page);
            color: var(--ink);
            font-family: 'DM Sans', sans-serif;
        }
        [data-testid="stHeader"] {
            background: color-mix(in srgb, var(--page) 90%, transparent) !important;
            -webkit-backdrop-filter: blur(18px);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--line);
            z-index: 1000;
        }
        [data-testid="stHeader"] a, [data-testid="stHeader"] button,
        [data-testid="stHeader"] span { color: var(--ink) !important; }
        [data-testid="stHeader"] a:hover, [data-testid="stHeader"] button:hover { color: var(--accent) !important; }
        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 1180px;
            padding: 2.8rem 2rem 4rem;
        }
        h1, h2, h3 { color: var(--ink); font-family: 'DM Serif Display', Georgia, serif !important; letter-spacing: 0 !important; }
        h1 { font-size: clamp(3.8rem, 6vw, 5.6rem) !important; line-height: 1.05 !important; }
        h2 { font-size: clamp(2.35rem, 3.5vw, 3rem) !important; }
        h3 { font-size: clamp(1.5rem, 2vw, 1.85rem) !important; }
        .eyebrow { color: var(--accent); font-size: .76rem; font-weight: 700; text-transform: uppercase; letter-spacing: .13em; }
        .quiet-copy { color: var(--muted); line-height: 1.62; }
        .st-key-top_nav {
            position: fixed;
            top: .55rem;
            left: 50%;
            transform: translateX(-50%);
            width: min(95vw, 1550px);
            box-sizing: border-box;
            z-index: 9999;
            margin: 0;
            padding: .55rem .7rem;
            border: 1px solid var(--line);
            border-radius: 12px;
            background: color-mix(in srgb, var(--page) 88%, transparent);
            -webkit-backdrop-filter: blur(18px);
            backdrop-filter: blur(18px);
            box-shadow: 0 10px 28px rgba(0, 23, 17, .17);
        }
        .st-key-top_nav [data-testid="stHorizontalBlock"] { display: grid !important; grid-template-columns: 1.4fr repeat(7, minmax(0, 1fr)) 1.25fr; gap: .4rem; align-items: center; }
        .st-key-top_nav [data-testid="stColumn"] { width: 100% !important; min-width: 0 !important; max-width: 100% !important; flex: none !important; }
        .st-key-top_nav [data-testid="stPageLink-NavLink"] {
            display: flex;
            width: 100%;
            box-sizing: border-box;
            white-space: nowrap;
            justify-content: center;
            min-height: 2.7rem;
            border: 1px solid var(--line);
            border-radius: 6px;
            background: var(--surface) !important;
            color: var(--ink) !important;
            font-weight: 700;
        }
        .nav-brand {
            display: flex;
            align-items: center;
            gap: .55rem;
            color: var(--ink);
            font-weight: 800;
            line-height: 1.1;
        }
        .nav-mark {
            display: grid;
            place-items: center;
            flex: 0 0 2rem;
            width: 2rem;
            height: 2rem;
            border-radius: 6px;
            background: var(--hero);
            color: var(--hero-text);
            font-size: .72rem;
        }
        .nav-name { font-size: .8rem; }
        .st-key-top_nav [data-testid="stPageLink-NavLink"] p,
        .st-key-top_nav [data-testid="stPageLink-NavLink"] span {
            color: var(--ink) !important;
            white-space: nowrap;
        }
        .st-key-top_nav .stButton button { width: 100%; white-space: nowrap; }
        .st-key-top_nav .stDownloadButton button { width: 100%; min-height: 2.7rem; white-space: nowrap; background: var(--hero) !important; border-color: var(--hero) !important; color: var(--hero-text) !important; font-weight: 700; }
        .st-key-top_nav .stDownloadButton button * { color: var(--hero-text) !important; }
        .st-key-top_nav [data-testid="stPageLink-NavLink"],
        .st-key-top_nav button { transition: transform .2s ease, box-shadow .2s ease, background-color .2s ease; }
        .st-key-top_nav [data-testid="stPageLink-NavLink"]:hover,
        .st-key-top_nav button:hover { transform: translateY(-2px); box-shadow: 0 5px 12px rgba(0, 23, 17, .18); }
        [class*="st-key-nav_active_"].stVerticalBlock [data-testid="stPageLink-NavLink"] {
            background: var(--hero) !important;
            border-color: var(--hero) !important;
            box-shadow: inset 0 -3px 0 var(--warm);
        }
        [class*="st-key-nav_active_"].stVerticalBlock [data-testid="stPageLink-NavLink"] p,
        [class*="st-key-nav_active_"].stVerticalBlock [data-testid="stPageLink-NavLink"] span {
            color: var(--hero-text) !important;
        }
        .st-key-top_nav_home_active button {
            background: var(--hero) !important;
            color: var(--hero-text) !important;
            border-color: var(--hero) !important;
            box-shadow: inset 0 -3px 0 var(--warm);
        }
        .stApp [data-testid="stWidgetLabel"],
        .stApp [data-testid="stWidgetLabel"] * {
            color: var(--ink) !important;
            font-weight: 600;
        }
        .stApp [data-testid="stTextInput"] input,
        .stApp [data-testid="stNumberInput"] input,
        .stApp [data-testid="stDateInput"] input {
            color: var(--ink) !important;
            background: var(--surface) !important;
            border-color: var(--line) !important;
        }
        .stApp [data-baseweb="input"],
        .stApp [data-baseweb="select"] > div {
            color: var(--ink) !important;
            background: var(--surface) !important;
            border-color: var(--line) !important;
        }
        .stApp [data-baseweb="select"] input,
        .stApp [data-baseweb="select"] div,
        .stApp [data-baseweb="popover"] div,
        .stApp [role="option"] {
            color: var(--ink);
        }
        .stApp [data-baseweb="popover"] [role="option"]:hover,
        .stApp [data-baseweb="popover"] [aria-selected="true"] {
            background: var(--surface-quiet) !important;
        }
        .st-key-home_hero { background: var(--hero); color: var(--hero-text); border-radius: 12px; padding: clamp(1.25rem, 4vw, 3rem); border: 1px solid rgba(255,255,255,.14); box-shadow: 0 18px 40px rgba(19,43,34,.13); }
        .st-key-home_hero h1, .st-key-home_hero h2, .st-key-home_hero h3, .st-key-home_hero p, .st-key-home_hero strong { color: var(--hero-text) !important; }
        .st-key-home_hero .eyebrow { color: #a9dfbd !important; }
        .st-key-home_hero .stDownloadButton button { background: #f6f6ef !important; color: #173d32 !important; border-color: #f6f6ef !important; }
        .st-key-home_hero .stDownloadButton button * { color: #173d32 !important; }
        .portrait { display: block; width: min(100%, 270px); aspect-ratio: 4 / 5; object-fit: cover; object-position: center 34%; border-radius: 8px; border: 3px solid rgba(255,255,255,.76); margin: 0 auto; }
        .portrait-note { color: #dce8dd !important; text-align: center; font-size: .8rem; }
        [class*="st-key-project_"].stVerticalBlock { border: 1px solid var(--line); border-radius: 8px; background: var(--surface); padding: 1.15rem 1.25rem .75rem; margin: .4rem 0 1rem; }
        [class*="st-key-project_readmission"].stVerticalBlock { border-top: 4px solid var(--accent); }
        [class*="st-key-project_bank-research"].stVerticalBlock { border-top: 4px solid var(--warm); }
        [class*="st-key-visual_"].stVerticalBlock { border: 1px solid var(--line); border-radius: 6px; background: var(--surface-quiet); padding: .7rem; }
        [class*="st-key-visual_"].stVerticalBlock img { max-height: 340px; object-fit: contain; }
        .project-type { color: var(--accent); font-size: .76rem; font-weight: 700; text-transform: uppercase; }
        .education-number { color: var(--warm); font-family: 'DM Serif Display', Georgia, serif; font-size: 1.8rem; margin: .5rem 0; }
        .project-summary { color: var(--muted); line-height: 1.58; }
        .small-label { color: var(--muted); font-size: .78rem; font-weight: 700; }
        .tool-chip { display: inline-block; margin: .15rem .25rem .15rem 0; padding: .25rem .5rem; border: 1px solid var(--line); border-radius: 999px; color: var(--muted); background: var(--page); font-size: .73rem; font-weight: 600; }
        .visual-step { padding: .55rem .65rem; margin: .35rem 0; border-left: 3px solid var(--accent); border-radius: 2px; background: var(--surface); color: var(--ink); font-size: .82rem; font-weight: 600; }
        .result-band { border-left: 3px solid var(--warm); padding: .65rem .8rem; margin: .7rem 0; background: var(--page); color: var(--ink); }
        .matrix-wrap { max-width: 100%; overflow-x: auto; }
        .confusion-matrix { width: 100%; border-collapse: separate; border-spacing: 4px; font-size: .76rem; }
        .confusion-matrix caption { text-align: left; color: var(--muted); padding: .25rem 0 .6rem; font-weight: 700; }
        .confusion-matrix th { color: var(--muted); padding: .35rem; text-align: center; }
        .confusion-matrix th[scope="row"] { text-align: left; min-width: 5.3rem; }
        .confusion-matrix td { border: 1px solid var(--line); border-radius: 4px; padding: .45rem .3rem; text-align: center; color: var(--ink); background: var(--surface); min-width: 3.8rem; }
        .confusion-matrix td.matrix-cell { background: var(--cell-bg) !important; color: var(--cell-ink) !important; border-color: rgba(255,255,255,.24); }
        .confusion-matrix td.matrix-cell strong,
        .confusion-matrix td.matrix-cell small { color: inherit !important; }
        .confusion-matrix small { display: block; font-size: .68rem; }
        .result-metrics { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: .45rem; margin-top: .7rem; }
        .result-metric { border: 1px solid var(--line); border-radius: 5px; padding: .5rem; background: var(--surface); }
        .result-metric strong { display: block; color: var(--accent); font-size: 1.05rem; }
        .result-metric span { color: var(--muted); font-size: .68rem; line-height: 1.25; }
        .accuracy-row { margin: .65rem 0; }
        .accuracy-label { display: flex; justify-content: space-between; gap: .7rem; color: var(--ink); font-size: .8rem; font-weight: 700; }
        .accuracy-track { height: .65rem; margin-top: .3rem; border-radius: 999px; background: var(--surface-quiet); overflow: hidden; }
        .accuracy-fill { height: 100%; border-radius: inherit; background: var(--accent); }
        .accuracy-row:last-of-type .accuracy-fill { background: var(--warm); }
        .project-actions { display: flex; gap: .55rem; flex-wrap: wrap; align-items: center; }
        .stButton button, .stLinkButton a, .stDownloadButton button { min-height: 2.65rem; border-radius: 5px; font-weight: 700; }
        .stLinkButton a { background: var(--surface) !important; color: var(--accent) !important; border: 1px solid var(--accent) !important; }
        .stLinkButton a:hover { background: var(--accent) !important; color: var(--accent-ink) !important; }
        .stLinkButton a:hover * { color: var(--accent-ink) !important; }
        .stDownloadButton button { background: var(--accent) !important; color: #ffffff !important; border: 1px solid var(--accent) !important; }
        [data-testid="stMetric"] { background: var(--surface-quiet); border: 1px solid var(--line); border-radius: 6px; padding: .7rem .85rem; }
        [data-testid="stMetricLabel"], [data-testid="stMetricDelta"] { color: var(--muted) !important; }
        [data-testid="stMetricValue"] { color: var(--ink) !important; }
        [data-testid="stExpander"] { border-color: var(--line); border-radius: 6px; background: var(--surface); }
        [data-testid="stSidebar"] { border-right: 1px solid var(--line); }
        a:focus-visible, button:focus-visible, input:focus-visible, [tabindex="0"]:focus-visible { outline: 3px solid var(--warm) !important; outline-offset: 2px !important; }
        hr { border-color: var(--line); }
        @media (max-width: 900px) {
            [data-testid="stAppViewContainer"] > .main .block-container { padding: .9rem 1.1rem 3rem; }
            [data-testid="stHorizontalBlock"] { flex-wrap: wrap; gap: .65rem; }
            [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] { flex: 1 1 100% !important; min-width: 100% !important; }
            .st-key-top_nav [data-testid="stHorizontalBlock"] { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            h2 { font-size: 1.7rem !important; }
            .st-key-home_hero { padding: 1.1rem; border-radius: 8px; }
            .st-key-top_nav [data-testid="stHorizontalBlock"] { grid-template-columns: repeat(4, minmax(0, 1fr)); }
            .st-key-top_nav [data-testid="stColumn"] { width: 100% !important; min-width: 0 !important; max-width: 100% !important; flex: none !important; }
            .st-key-home_primary_actions [data-testid="stHorizontalBlock"],
            .st-key-home_profile_actions [data-testid="stHorizontalBlock"] {
                display: grid !important;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: .55rem;
            }
            .st-key-home_primary_actions [data-testid="stColumn"],
            .st-key-home_profile_actions [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                max-width: 100% !important;
                flex: none !important;
            }
            h1 { font-size: 3rem !important; }
        }
        @media (max-width: 600px) {
            .st-key-top_nav [data-testid="stHorizontalBlock"] { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .st-key-top_nav { padding: .45rem .2rem; }
            .nav-brand { justify-content: center; min-height: 2.5rem; }
            .nav-name { font-size: .78rem; }
            [data-testid="stAppViewContainer"] > .main .block-container { padding: .6rem .75rem 2rem; }
            h1 { font-size: 2.45rem !important; }
            h2 { font-size: 1.7rem !important; }
            .portrait { width: min(100%, 190px); }
            .st-key-home_hero { padding: 1.1rem; border-radius: 8px; }
            [class*="st-key-project_"].stVerticalBlock { padding: .9rem; }
        }
        @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; transition-duration: .01ms !important; } }
        @media (prefers-color-scheme: dark) {
            :root {
                --page: #101a16;
                --surface: #192720;
                --surface-quiet: #23372d;
                --ink: #f2f5ef;
                --muted: #c1d1c7;
                --line: #40594b;
                --accent: #8bd3ad;
                --accent-ink: #102219;
                --warm: #f0a18b;
                --hero: #203f34;
                --hero-text: #f7f7f0;
            }
        }
        /* Home page contrast fixes only; retain the established layout and scale. */
        .st-key-home_featured_project,
        [class*="st-key-home_preview_"].stVerticalBlock {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
        }
        [class*="st-key-home_experience_"].stVerticalBlock,
        [class*="st-key-home_education_"].stVerticalBlock,
        [class*="st-key-home_certificate_"].stVerticalBlock,
        [class*="st-key-home_skill_"].stVerticalBlock {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 10px;
        }
        [class*="st-key-home_section_link_"].stVerticalBlock [data-testid="stPageLink-NavLink"],
        .st-key-home_featured_project [data-testid="stPageLink-NavLink"],
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink-NavLink"] {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.65rem;
            padding: .5rem .9rem;
            background: var(--surface-quiet) !important;
            color: var(--ink) !important;
            border: 1px solid var(--accent) !important;
            border-radius: 6px;
            font-weight: 700;
        }
        [class*="st-key-home_section_link_"].stVerticalBlock [data-testid="stPageLink-NavLink"] *,
        .st-key-home_featured_project [data-testid="stPageLink-NavLink"] *,
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink-NavLink"] * {
            color: var(--ink) !important;
        }
        [class*="st-key-home_section_link_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:hover,
        .st-key-home_featured_project [data-testid="stPageLink-NavLink"]:hover,
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:hover {
            background: var(--accent) !important;
            color: var(--accent-ink) !important;
        }
        [class*="st-key-home_section_link_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:hover *,
        .st-key-home_featured_project [data-testid="stPageLink-NavLink"]:hover *,
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:hover * {
            color: var(--accent-ink) !important;
        }
        [class*="st-key-home_section_link_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:focus-visible,
        .st-key-home_featured_project [data-testid="stPageLink-NavLink"]:focus-visible,
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink-NavLink"]:focus-visible {
            outline: 3px solid var(--warm) !important;
            outline-offset: 2px !important;
        }
        [class*="st-key-home_experience_"].stVerticalBlock [data-testid="stCaptionContainer"] p,
        [class*="st-key-home_education_"].stVerticalBlock [data-testid="stCaptionContainer"] p,
        [class*="st-key-home_certificate_"].stVerticalBlock [data-testid="stCaptionContainer"] p,
        [class*="st-key-home_skill_"].stVerticalBlock [data-testid="stCaptionContainer"] p,
        .st-key-home_featured_project [data-testid="stCaptionContainer"] p {
            color: var(--muted) !important;
            font-size: .9rem;
        }
        .st-key-home_featured_project .confusion-matrix { font-size: .82rem; }
        .st-key-home_featured_project .confusion-matrix small { font-size: .72rem; }
        .st-key-home_featured_project .result-metric span { font-size: .78rem; }
        .bank-metrics { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: .7rem; }
        .bank-metric { background: var(--surface); border: 1px solid var(--line); border-radius: 9px; padding: .9rem 1rem; }
        .bank-metric strong { display: block; color: var(--accent); font-size: clamp(1.45rem,2.4vw,2rem); line-height: 1.15; }
        .bank-metric span { display: block; color: var(--muted); font-size: .95rem; line-height: 1.4; margin-top: .25rem; }
        .bank-flow { display: flex; flex-wrap: wrap; gap: .45rem; align-items: center; margin-top: 1.1rem; }
        .bank-flow-step { border: 1px solid var(--line); border-radius: 7px; background: var(--surface); color: var(--ink); padding: .55rem .75rem; font-size: .96rem; font-weight: 700; }
        .bank-flow-arrow { color: var(--accent); font-weight: 800; }
        .bank-home-metrics { color: var(--accent); font-size: 1.05rem; font-weight: 700; line-height: 1.6; margin: .6rem 0; }
        @media (max-width: 600px) { .bank-metrics { grid-template-columns: 1fr 1fr; } .bank-flow-arrow { display: none; } }
        .st-key-top_nav { display: block !important; visibility: visible !important; }
        /* Home typography is scoped so project detail pages and navigation retain their layout. */
        .st-key-home_content { font-size: 1.03rem; line-height: 1.58; }
        .st-key-home_content [data-testid="stMarkdownContainer"] p,
        .st-key-home_content [data-testid="stMarkdownContainer"] li {
            font-size: 1.03rem;
            line-height: 1.62;
        }
        .st-key-home_content h2 { font-size: clamp(2rem, 3vw, 2.55rem) !important; line-height: 1.16 !important; }
        .st-key-home_content h3 { font-size: clamp(1.45rem, 2vw, 1.75rem) !important; line-height: 1.26 !important; }
        .st-key-home_hero h1 { font-size: clamp(2.4rem, 3.6vw, 3.4rem) !important; line-height: 1.08 !important; margin: .15rem 0 .45rem; }
        .st-key-home_hero.stVerticalBlock { min-height: 34rem; }
        .st-key-home_hero:not(:has(.st-key-home_profile_actions a[href^="mailto:"])) {
            visibility: hidden;
        }
        .st-key-home_hero .portrait { height: auto; }
        @media (max-width: 640px) {
            .st-key-home_hero.stVerticalBlock { min-height: 58rem; }
        }
        .st-key-home_hero h3 { font-size: clamp(1.4rem, 1.8vw, 1.7rem) !important; line-height: 1.28 !important; margin: .15rem 0 1rem; }
        .st-key-home_hero .hero-intro { max-width: 68ch; margin: 0 auto 1rem; }
        .st-key-home_hero .hero-intro p { margin: 0 0 .8rem; line-height: 1.55; text-align: justify; text-justify: inter-word; text-align-last: left; hyphens: auto; }
        .st-key-home_profile_actions { max-width: 68ch; margin-inline: auto; }
        .st-key-home_content .home-section-label { color: var(--accent); font-size: 1.18rem !important; font-weight: 800; text-transform: uppercase; letter-spacing: .1em; margin: 4.7rem 0 .55rem; padding-top: .8rem; border-top: 1px solid var(--line); }
        .pantry-metrics { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .55rem; margin: .9rem 0; }
        .pantry-metrics div { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: .65rem .8rem; }
        .pantry-metrics strong { display: block; font-size: 1.45rem; color: var(--accent); line-height: 1.2; }
        .pantry-metrics span { display: block; font-size: .91rem; color: var(--muted); line-height: 1.35; }
        [class*="st-key-home_preview_"].stVerticalBlock, [class*="st-key-home_experience_"].stVerticalBlock, [class*="st-key-home_education_"].stVerticalBlock, [class*="st-key-home_certificate_"].stVerticalBlock, [class*="st-key-home_skill_"].stVerticalBlock { transition: transform .23s ease, box-shadow .23s ease; }
        [class*="st-key-home_preview_"].stVerticalBlock:hover, [class*="st-key-home_experience_"].stVerticalBlock:hover, [class*="st-key-home_education_"].stVerticalBlock:hover, [class*="st-key-home_certificate_"].stVerticalBlock:hover, [class*="st-key-home_skill_"].stVerticalBlock:hover { transform: translateY(-3px); box-shadow: 0 12px 24px rgba(0, 23, 17, .12); }
        .st-key-home_content .eyebrow,
        .st-key-home_content .project-type { font-size: .96rem !important; }
        .st-key-home_content .tool-chip { font-size: .94rem; padding: .36rem .65rem; }
        .st-key-home_content .result-band { font-size: 1.06rem; line-height: 1.55; }
        .st-key-home_content .confusion-matrix { font-size: 1rem; }
        .st-key-home_content .confusion-matrix small { font-size: .88rem; }
        .st-key-home_content .confusion-matrix th,
        .st-key-home_content .confusion-matrix td { padding: .5rem .4rem; }
        .st-key-home_content .result-metric strong { font-size: 1.4rem; }
        .st-key-home_content .result-metric span { font-size: .95rem; }
        .st-key-home_content [data-testid="stCaptionContainer"] p,
        .st-key-home_content .portrait-note { font-size: 1rem !important; line-height: 1.5; }
        .st-key-home_content [data-testid="stPageLink-NavLink"],
        .st-key-home_content .stLinkButton a,
        .st-key-home_content .stDownloadButton button { font-size: 1.03rem; }
        .st-key-home_hero [data-testid="stPageLink-NavLink"] {
            display: flex; justify-content: center; align-items: center;
            min-height: 2.65rem; padding: .5rem .8rem;
            background: #f6f6ef !important; border: 1px solid #f6f6ef !important;
            border-radius: 6px; color: #173d32 !important;
        }
        .st-key-home_hero [data-testid="stPageLink-NavLink"] * { color: #173d32 !important; }
        .st-key-home_hero [data-testid="stPageLink-NavLink"]:hover { background: #d8eee0 !important; }
        @media (max-width: 600px) {
            .st-key-home_content h2 { font-size: 2rem !important; }
            .st-key-home_content h3 { font-size: 1.5rem !important; }
            .st-key-home_hero h1 { font-size: clamp(2.15rem, 8vw, 2.65rem) !important; }
            [data-testid="stAppViewContainer"] > .main .block-container { padding-top: 2rem; }
            .st-key-top_nav { max-height: 7.5rem; overflow-y: auto; }
            .pantry-metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .st-key-home_content .confusion-matrix { font-size: .9rem; }
        }
        @media (min-width: 601px) and (max-width: 900px) {
            [data-testid="stAppViewContainer"] > .main .block-container { padding-top: 2rem; }
        }
        @media (prefers-reduced-motion: reduce) {
            .st-key-top_nav [data-testid="stPageLink-NavLink"], .st-key-top_nav button,
            [class*="st-key-home_preview_"].stVerticalBlock, [class*="st-key-home_experience_"].stVerticalBlock, [class*="st-key-home_education_"].stVerticalBlock, [class*="st-key-home_certificate_"].stVerticalBlock, [class*="st-key-home_skill_"].stVerticalBlock { transition: none; }
        }
        [class*="st-key-home_preview_"].stVerticalBlock {
            height: 100%; padding: 1.5rem; box-sizing: border-box;
        }
        [class*="st-key-home_preview_"].stVerticalBlock [data-testid="stPageLink"] {
            margin-top: auto;
        }
        /* One padded surface per card; native border wrappers remain transparent. */
        [class*="st-key-home_experience_"].stVerticalBlock,
        [class*="st-key-home_education_"].stVerticalBlock,
        [class*="st-key-home_certificate_"].stVerticalBlock,
        [class*="st-key-home_skill_"].stVerticalBlock {
            padding: 1.4rem;
            height: 100%;
            gap: .85rem;
            box-sizing: border-box;
        }
        [data-testid="stVerticalBlockBorderWrapper"]:has(> [class*="st-key-home_"]) {
            border: 0 !important; padding: 0 !important;
        }
        [class*="st-key-home_experience_"].stVerticalBlock [data-testid="stMarkdownContainer"]:has(strong),
        [class*="st-key-home_education_"].stVerticalBlock [data-testid="stMarkdownContainer"]:has(strong),
        [class*="st-key-home_skill_"].stVerticalBlock [data-testid="stMarkdownContainer"]:has(strong),
        [class*="st-key-home_certificate_"].stVerticalBlock h3,
        [class*="st-key-project_"].stVerticalBlock h3,
        .st-key-home_featured_project h3 { text-align: center; }
        [class*="st-key-home_"].stVerticalBlock [data-testid="stMarkdownContainer"] p {
            overflow-wrap: anywhere;
        }
        [class*="st-key-home_certificate_"].stVerticalBlock .stLinkButton { margin-top: auto; }
        .st-key-header_menu.stVerticalBlock {
            position: fixed; top: .65rem; left: 3.5rem; right: 9rem;
            width: auto !important; max-width: calc(100vw - 12.5rem);
            z-index: 1001; background: var(--page); padding: .3rem .6rem;
            height: 3.5rem; box-sizing: border-box;
            overflow-x: auto; overflow-y: hidden;
        }
        .st-key-header_menu [data-testid="stHorizontalBlock"] {
            display: grid !important;
            grid-template-columns: repeat(11, max-content);
            justify-content: start; align-items: center; gap: .65rem;
            width: max-content !important; min-width: 0;
        }
        .st-key-header_menu [data-testid="stColumn"] {
            width: auto !important; min-width: 0 !important; max-width: none !important;
        }
        .st-key-header_menu [data-testid="stPageLink-NavLink"],
        .st-key-header_menu [data-testid="stPopoverButton"] {
            display: flex; align-items: center; justify-content: center;
            width: 100%; height: 2.5rem; min-height: 2.5rem; box-sizing: border-box;
            padding: .3rem .7rem; border: 1px solid transparent !important;
            border-radius: 999px; background: transparent !important;
            color: var(--ink) !important;
            transition: color .18s ease;
        }
        .st-key-header_menu [data-testid="stPageLink-NavLink"]:hover,
        .st-key-header_menu [data-testid="stPopoverButton"]:hover {
            color: var(--accent) !important; box-shadow: none;
        }
        .st-key-header_menu [data-testid="stPageLink-NavLink"]:focus-visible,
        .st-key-header_menu [data-testid="stPopoverButton"]:focus-visible {
            outline: 2px solid var(--accent); outline-offset: 2px;
        }
        .st-key-header_menu [class*="st-key-menu_selected_"] [data-testid="stPageLink-NavLink"],
        .st-key-header_menu [class*="st-key-menu_selected_"] [data-testid="stPopoverButton"] {
            background: #35463d !important;
            color: var(--ink) !important;
        }
        .st-key-header_menu p {
            font-weight: 700 !important;
            font-size: clamp(.75rem, .95vw, .88rem) !important; white-space: nowrap !important;
            overflow-wrap: normal !important; word-break: normal !important;
            text-align: center; line-height: 1.2; margin: 0;
        }
        .st-key-header_menu [data-testid="stMarkdownContainer"] {
            width: 100%; text-align: center;
        }
        .st-key-header_menu [data-testid="stPageLink-NavLink"] > div,
        .st-key-header_menu [data-testid="stPopoverButton"] > div {
            justify-content: center; align-items: center;
        }
        .st-key-home_hero h1, .st-key-home_hero h3,
        .st-key-home_hero .eyebrow { text-align: center; }
        .st-key-home_hero_copy.stVerticalBlock {
            max-width: 68ch; margin-inline: auto; width: 100%;
        }
        .st-key-home_hero .hero-intro p {
            text-align: justify; text-align-last: center;
            overflow-wrap: normal; word-break: normal;
        }
        .st-key-header_menu [data-testid="stPageLink-NavLink"] [data-testid="stIconMaterial"] {
            display: none;
        }
        [data-testid="stSidebar"] { z-index: 1003 !important; }
        [data-testid="stSidebarHeader"] { position: relative; z-index: 1004; }
        [data-testid="stSidebarCollapseButton"] {
            visibility: visible !important; opacity: 1 !important; display: flex !important;
        }
        [data-testid="stSidebarCollapseButton"] button {
            border: 1px solid var(--accent); border-radius: 8px;
            background: var(--surface-quiet); color: var(--ink) !important;
        }
        [data-testid="stSidebarCollapsedControl"] { z-index: 1004 !important; }
        [data-testid="stHeader"] { height: 4.5rem; }
        [data-testid="stMainBlockContainer"], .main .block-container { padding-top: 5rem !important; }
        @media (max-width: 1500px) {
            .st-key-header_menu.stVerticalBlock {
                left: 3rem; right: 5rem; max-width: calc(100vw - 8rem); padding: .3rem;
            }
        }
        .st-key-mobile_menu { display: none; }
        @media (max-width: 768px) {
            .st-key-header_menu.stVerticalBlock { display: none !important; }
            .st-key-mobile_menu { display: flex; }
            .st-key-mobile_menu [data-testid="stPageLink-NavLink"] {
                min-height: 2.75rem;
            }
            [data-testid="stHeader"] { height: 3.5rem; }
            [data-testid="stMainBlockContainer"], .main .block-container { padding-top: 4rem !important; }
        }
        @media (prefers-reduced-motion: reduce) {
            .st-key-header_menu a, .st-key-header_menu button { transition: none !important; }
        }
        :is(
            .st-key-home_hero, .st-key-home_featured_project, .st-key-contact_card,
            [class*="st-key-home_preview_"], [class*="st-key-home_experience_"],
            [class*="st-key-home_education_"], [class*="st-key-home_certificate_"],
            [class*="st-key-home_skill_"], [class*="st-key-project_"],
            [class*="st-key-visual_"], [class*="st-key-experience_"],
            [class*="st-key-education_"], [class*="st-key-certificate_"],
            [class*="st-key-skills_"], [class*="st-key-leadership_"]
        ).stVerticalBlock {
            border: 1px solid #77ae91;
            border-radius: 10px;
            transition: border-color .18s ease, box-shadow .18s ease;
        }
        :is(
            .st-key-home_hero, .st-key-home_featured_project, .st-key-contact_card,
            [class*="st-key-home_preview_"], [class*="st-key-home_experience_"],
            [class*="st-key-home_education_"], [class*="st-key-home_certificate_"],
            [class*="st-key-home_skill_"], [class*="st-key-project_"],
            [class*="st-key-visual_"], [class*="st-key-experience_"],
            [class*="st-key-education_"], [class*="st-key-certificate_"],
            [class*="st-key-skills_"], [class*="st-key-leadership_"]
        ).stVerticalBlock:hover,
        :is(
            .st-key-home_hero, .st-key-home_featured_project, .st-key-contact_card,
            [class*="st-key-home_preview_"], [class*="st-key-home_experience_"],
            [class*="st-key-home_education_"], [class*="st-key-home_certificate_"],
            [class*="st-key-home_skill_"], [class*="st-key-project_"],
            [class*="st-key-visual_"], [class*="st-key-experience_"],
            [class*="st-key-education_"], [class*="st-key-certificate_"],
            [class*="st-key-skills_"], [class*="st-key-leadership_"]
        ).stVerticalBlock:focus-within {
            border-color: var(--accent);
            box-shadow: 0 0 0 1px var(--accent);
        }
        :is([class*="st-key-experience_"], [class*="st-key-education_"],
            [class*="st-key-certificate_"], [class*="st-key-skills_"],
            [class*="st-key-leadership_"], .st-key-contact_card).stVerticalBlock {
            background: var(--surface); padding: 1.4rem;
            margin-bottom: 1rem; box-sizing: border-box;
        }
        :is(.result-metric, .bank-metric, .pantry-metrics div,
            .preview-metrics div, [data-testid="stMetric"]) { border-color: #77ae91; }
        @media (prefers-reduced-motion: reduce) {
        :is(
            .st-key-home_hero, .st-key-home_featured_project, .st-key-contact_card,
            [class*="st-key-home_preview_"], [class*="st-key-home_experience_"],
            [class*="st-key-home_education_"], [class*="st-key-home_certificate_"],
            [class*="st-key-home_skill_"], [class*="st-key-project_"],
            [class*="st-key-visual_"], [class*="st-key-experience_"],
            [class*="st-key-education_"], [class*="st-key-certificate_"],
            [class*="st-key-skills_"], [class*="st-key-leadership_"]
        ).stVerticalBlock { transition: none; }
        }
        /* Use the same borderless visual panels across these projects. */
        .st-key-visual_bank-research.stVerticalBlock,
        .st-key-visual_bank-research.stVerticalBlock:hover,
        .st-key-visual_bank-research.stVerticalBlock:focus-within,
        .st-key-visual_pantrypulse.stVerticalBlock,
        .st-key-visual_pantrypulse.stVerticalBlock:hover,
        .st-key-visual_pantrypulse.stVerticalBlock:focus-within,
        .st-key-visual_readmission.stVerticalBlock,
        .st-key-visual_readmission.stVerticalBlock:hover,
        .st-key-visual_readmission.stVerticalBlock:focus-within {
            border: none;
            box-shadow: none;
        }
        .st-key-visual_bank-research .bank-metric,
        .st-key-visual_bank-research .bank-flow-step,
        .st-key-visual_pantrypulse .pantry-metrics div {
            border: none;
            box-shadow: none;
        }
        .st-key-visual_readmission [data-baseweb="select"] > div,
        .st-key-visual_readmission [data-baseweb="select"] > div:focus-within {
            border: none !important;
            box-shadow: none !important;
            outline: none;
        }
        .st-key-home_research_internship.stVerticalBlock {
            background: var(--surface); border: 1px solid #77ae91;
            border-radius: 10px; padding: 1.5rem; box-sizing: border-box;
        }
        .st-key-home_research_internship.stVerticalBlock:hover,
        .st-key-home_research_internship.stVerticalBlock:focus-within {
            border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent);
        }
        .st-key-home_research_internship h3 { text-align: center; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_links(links: list[dict[str, str]]) -> None:
    columns = st.columns(min(len(links), 3))
    for index, link in enumerate(links):
        columns[index % len(columns)].link_button(link["label"], link["url"], use_container_width=True)


def render_project_visual(project: dict[str, Any], show_all_plots: bool = False) -> None:
    visual = project.get("visual", {})
    with st.container(key=f"visual_{project['id']}"):
        if visual.get("type") == "image":
            if visual.get("local_file"):
                st.image(str(ROOT / visual["local_file"]), caption=visual["caption"], use_container_width=True)
                st.link_button("Open visual full size", "/app/" + visual["local_file"], use_container_width=True)
            else:
                st.image(visual["url"], caption=visual["caption"], use_container_width=True)
                st.link_button("Open visual full size", visual["url"], use_container_width=True)
        elif visual.get("type") == "accuracy_comparison":
            st.markdown(f"**{escape(visual['title'])}**")
            for metric in visual["metrics"]:
                ratio = max(0, min(1, float(metric["ratio"])))
                st.markdown(
                    f'<div class="accuracy-row"><div class="accuracy-label"><span>{escape(metric["label"])}</span><span>{escape(metric["value"])}</span></div>'
                    f'<div class="accuracy-track" role="img" aria-label="{escape(metric["label"])} test accuracy {escape(metric["value"])}"><div class="accuracy-fill" style="width:{ratio:.1%}"></div></div></div>',
                    unsafe_allow_html=True,
                )
            plots = visual.get("plots", [])
            if plots and show_all_plots:
                by_file = {plot["file"]: plot for plot in plots}
                st.subheader("Held-out model performance")
                st.dataframe([
                    {"Model": "Logistic regression", "Test accuracy (reported)": "87.4%", "High-risk recall (from counts)": "96.23%", "Low-risk recall (from counts)": "66.50%"},
                    {"Model": "Decision tree", "Test accuracy (reported)": "97.4%", "High-risk recall (from counts)": "97.79%", "Low-risk recall (from counts)": "95.11%"},
                ], hide_index=True, use_container_width=True)
                st.caption("Accuracy is reported by the source; class recall is calculated from the actual/predicted axes in its test confusion matrices. The decision-tree counts imply 97.0% accuracy, which differs from the reported 97.4%. External validation is not established.")
                st.markdown("[Logistic evaluation source](https://github.com/PriyankaRauniyar/Predictive-Modeling-For-Health-risk-classification/blob/main/figures/Model_Accuracy.png) · [Decision-tree evaluation source](https://github.com/PriyankaRauniyar/Predictive-Modeling-For-Health-risk-classification/blob/main/figures/Model_Acc.png)")
                groups = [
                    ("Model interpretation", ["decision_tree.png", "scurve_bmi.png"]),
                ]
                for group_title, filenames in groups:
                    st.subheader(group_title)
                    for offset in range(0, len(filenames), 2):
                        columns = st.columns(2, gap="large")
                        for column, filename in zip(columns, filenames[offset:offset + 2]):
                            plot = by_file[filename]
                            with column:
                                st.markdown(f"**{plot['title']}**")
                                st.image(str(ROOT / "static" / "health-risk" / filename), caption=plot["caption"], use_container_width=True)
                                st.link_button("Open plot full size", f"/app/static/health-risk/{filename}", use_container_width=True)
                st.caption("Original figures from the public Health Risk Classification repository.")
            elif plots:
                titles = [plot["title"] for plot in plots]
                selected = st.selectbox("Explore project plots", titles, key=f"plot_picker_{project['id']}")
                plot = plots[titles.index(selected)]
                local_path = ROOT / "static" / "health-risk" / plot["file"]
                st.image(str(local_path), caption=plot["caption"], use_container_width=True)
                st.link_button("Open plot full size", f"/app/static/health-risk/{plot['file']}", use_container_width=True)
                st.caption("Original project figures; use the selector to explore risk curves, model evaluation, and class distributions.")
            else:
                st.image(visual["url"], caption=visual["caption"], use_container_width=True)
                st.link_button("Open decision tree full size", visual["url"], use_container_width=True)
        elif visual.get("type") == "confusion":
            classes = visual["classes"]
            matrix = visual["matrix"]
            total = sum(sum(row) for row in matrix)
            mode = st.selectbox(
                "Matrix view", ["Share of actual outcome (%)", "Encounter counts"],
                key=f"matrix_mode_{project['id']}",
            )
            records = []
            for row_index, (actual, counts) in enumerate(zip(classes, matrix)):
                row_total = sum(counts)
                for column_index, (predicted, count) in enumerate(zip(classes, counts)):
                    share = 100 * count / row_total if row_total else 0
                    records.append({
                        "Actual": actual, "Predicted": predicted,
                        "Encounters": count, "Row share": round(share, 2),
                        "Value": share if mode.startswith("Share") else count,
                        "Label": f"{share:.1f}%" if mode.startswith("Share") else f"{count:,}",
                        "Result": "Correct prediction" if row_index == column_index else "Misclassified",
                    })
            st.markdown(f"**Actual vs predicted · {total:,} held-out encounters**")
            st.vega_lite_chart({
                "data": {"values": records},
                "height": 260,
                "encoding": {
                    "x": {"field": "Predicted", "type": "nominal", "sort": classes,
                          "axis": {"title": "Predicted outcome", "labelAngle": 0}},
                    "y": {"field": "Actual", "type": "nominal", "sort": classes,
                          "axis": {"title": "Actual outcome"}},
                    "tooltip": [
                        {"field": "Actual"}, {"field": "Predicted"},
                        {"field": "Encounters", "format": ","},
                        {"field": "Row share", "title": "Share of actual outcome (%)", "format": ".1f"},
                        {"field": "Result"},
                    ],
                },
                "layer": [
                    {"mark": {"type": "rect", "stroke": "#101a16", "strokeWidth": 4, "cornerRadius": 8},
                     "encoding": {"color": {"field": "Value", "type": "quantitative",
                         "scale": {"range": ["#23372d", "#8bd3ad"]}, "legend": None}}},
                    {"mark": {"type": "text", "fontSize": 18, "fontWeight": "bold"},
                     "encoding": {"text": {"field": "Label"}, "color": {
                         "condition": {"test": "datum.Value > " + str(max(r["Value"] for r in records) * .55),
                                       "value": "#102219"}, "value": "#f2f5ef"}}},
                ],
                "config": {"view": {"stroke": None}, "axis": {"labelLimit": 160}},
            }, use_container_width=True)
            st.caption(visual["caption"] + " Hover over a cell for counts and row percentages. Diagonal cells are correct predictions; other cells are errors.")
            metric_html = "".join(
                f'<div class="result-metric"><strong>{escape(metric["value"])}</strong><span>{escape(metric["label"])}</span></div>'
                for metric in project.get("metrics", [])
            )
            st.markdown(f'<div class="result-metrics" aria-label="Frozen held-out test metrics">{metric_html}</div>', unsafe_allow_html=True)
        elif visual.get("type") == "demand_forecast":
            from datetime import date, timedelta

            start = date.fromisoformat(visual.get("history_start", "2025-10-06"))
            history = [{"Week": (start + timedelta(weeks=i)).isoformat(),
                        "Households": value, "Series": "Simulated history"}
                       for i, value in enumerate(visual["history"])]
            forecast = []
            for i, value in enumerate(visual["forecast"]):
                upper = visual["upper"][i]
                forecast.append({
                    "Week": (start + timedelta(weeks=len(history) + i)).isoformat(),
                    "Households": value, "Lower": visual["lower"][i], "Upper": upper,
                    "Status": "RED" if value > visual["capacity"] else "YELLOW" if upper > visual["capacity"] else "GREEN",
                })
            x = {"field": "Week", "type": "temporal", "axis": {"title": None, "format": "%b %Y", "tickCount": 5}}
            y = {"field": "Households", "type": "quantitative",
                 "scale": {"domain": [0, 6500]}, "axis": {"title": "Households per week", "format": ","}}
            st.markdown("**Weekly demand & capacity outlook**")
            st.vega_lite_chart({
                "height": 260,
                "layer": [
                    {"data": {"values": history}, "mark": {"type": "line", "color": "#a3ada7", "strokeWidth": 2},
                     "encoding": {"x": x, "y": y, "tooltip": [{"field": "Week", "type": "temporal"}, {"field": "Households", "format": ","}, {"field": "Series"}]}},
                    {"data": {"values": forecast}, "mark": {"type": "area", "color": "#459bd5", "opacity": .2},
                     "encoding": {"x": x, "y": {"field": "Lower", "type": "quantitative"}, "y2": {"field": "Upper"}}},
                    {"data": {"values": forecast}, "mark": {"type": "line", "color": "#459bd5", "strokeWidth": 3}, "encoding": {"x": x, "y": y}},
                    {"data": {"values": [{"Capacity": visual["capacity"]}]},
                     "mark": {"type": "rule", "color": "#ef6b60", "strokeDash": [7, 5], "strokeWidth": 2},
                     "encoding": {"y": {"field": "Capacity", "type": "quantitative"}, "tooltip": [{"field": "Capacity", "title": "Weekly capacity", "format": ","}]}},
                    {"data": {"values": forecast}, "mark": {"type": "point", "filled": True, "size": 75},
                     "encoding": {"x": x, "y": y,
                         "color": {"field": "Status", "type": "nominal", "scale": {"domain": ["GREEN", "YELLOW", "RED"], "range": ["#8bd3ad", "#e9bd57", "#ef6b60"]}, "legend": {"title": "Week status", "orient": "bottom"}},
                         "tooltip": [{"field": "Week", "type": "temporal"}, {"field": "Households", "title": "Forecast", "format": ","}, {"field": "Lower", "format": ","}, {"field": "Upper", "format": ","}, {"field": "Status"}]}},
                ],
                "config": {"view": {"stroke": None}},
            }, use_container_width=True)
            st.caption(visual["caption"])
        elif visual.get("type") == "metrics":
            for metric in project.get("metrics", []):
                st.metric(metric["label"], metric["value"], help=metric.get("help"))
            st.caption(visual.get("caption", ""))
        elif visual.get("type") == "steps":
            for step in visual.get("steps", []):
                st.markdown(f'<div class="visual-step">{escape(step)}</div>', unsafe_allow_html=True)
            if visual.get("caption"):
                st.caption(visual["caption"])
        elif visual.get("type") == "bank_summary":
            metrics = [
                ("69.8M+", "Records in broader employment source"),
                ("5,156", "Accepted RCID mappings"),
                ("12", "Professor-approved additions to V7"),
                ("0", "Duplicate RCIDs in final bridge"),
            ]
            cards = "".join(
                f'<div class="bank-metric"><strong>{escape(value)}</strong><span>{escape(label)}</span></div>'
                for value, label in metrics
            )
            st.markdown(f'<div class="bank-metrics" aria-label="Research integration outputs">{cards}</div>', unsafe_allow_html=True)
            steps = ["Normalize", "Match", "Validate", "Review", "Finalize"]
            flow = '<span class="bank-flow-arrow" aria-hidden="true">→</span>'.join(
                f'<span class="bank-flow-step">{escape(step)}</span>' for step in steps
            )
            st.markdown(f'<div class="bank-flow" aria-label="Institution matching workflow">{flow}</div>', unsafe_allow_html=True)
            st.caption(visual["caption"])


def render_project_card(project: dict[str, Any], featured: bool = False) -> None:
    with st.container(key=f"project_{project['id']}"):
        if project.get("visual"):
            content, visual = st.columns([1.35, 1])
        else:
            content, visual = st.container(), None

        with content:
            status = f" · {project['status']}" if project.get("status") else ""
            st.markdown(
                f'<div class="project-type">{escape(project["category"])}{escape(status)}</div>',
                unsafe_allow_html=True,
            )
            st.subheader(project["title"])
            st.markdown(f'<p class="project-summary">{escape(project["problem"])}</p>', unsafe_allow_html=True)
            st.markdown('<div class="small-label">Project implementation</div>', unsafe_allow_html=True)
            st.write(project["contribution"])
            st.markdown('<div class="small-label">Skills & methods</div>' if project["id"] == "bank-research" else '<div class="small-label">Methods & tools</div>', unsafe_allow_html=True)
            st.markdown(
                "".join(f'<span class="tool-chip">{escape(tool)}</span>' for tool in project["methods"]),
                unsafe_allow_html=True,
            )
            if project["id"] != "bank-research":
                st.markdown(
                    f'<div class="result-band"><strong>Evidence</strong><br>{escape(project["outcome"])}</div>',
                    unsafe_allow_html=True,
                )
            if project.get("id") == "readmission":
                st.caption(
                    f"Frozen final test: {project['test_encounters']:,} encounters. "
                    f"Separate historical export: {project['historical_predictions']:,} precomputed predictions. "
                    "Retrospective research demonstration; not clinically validated."
                )
            if project["links"]:
                link_columns = st.columns(min(len(project["links"]), 3))
                for index, link in enumerate(project["links"]):
                    link_columns[index % len(link_columns)].link_button(
                        link["label"], link["url"], use_container_width=True
                    )
            st.page_link(
                f"pages/project_{project['id']}.py",
                label="View project details",
                icon=":material/article:",
                help=f"Open the dedicated {project['title']} project details.",
                use_container_width=True,
            )

        if visual is not None:
            with visual:
                render_project_visual(project)


def render_project_detail(project_id: str) -> None:
    projects = load_portfolio()["projects"]
    project_index = next(index for index, item in enumerate(projects) if item["id"] == project_id)
    project = projects[project_index]
    previous_project = projects[(project_index - 1) % len(projects)]
    next_project = projects[(project_index + 1) % len(projects)]

    st.page_link("pages/projects.py", label="Back to Projects", icon=":material/arrow_back:")
    status = f" · {project['status']}" if project.get("status") else ""
    st.markdown(f'<p class="eyebrow">{escape(project["category"])}{escape(status)}</p>', unsafe_allow_html=True)
    st.title(project["title"])
    st.markdown(f'<p class="quiet-copy">{escape(project["problem"])}</p>', unsafe_allow_html=True)

    if project_id == "readmission":
        st.info(
            f"Frozen, untouched final test: **{project['test_encounters']:,} encounters**. "
            f"Separate historical precomputed prediction export: **{project['historical_predictions']:,} rows**. "
            "Historical rows include development data and are not used for the test metrics. "
            "Retrospective research demonstration, not a clinically validated decision tool."
        )
    elif project_id == "pantrypulse":
        st.info(
            "Operational visit history and current capacity in the documented prototype are simulated. "
            "The dashboard link is user-provided; availability can vary."
        )

    with st.container(key=f"detail_visual_{project_id}"):
        st.header("Results & outputs")
        render_project_visual(project, show_all_plots=project_id == "health-risk")
        from evidence import render_selected_evidence
        render_selected_evidence(project)

    overview, implementation = st.columns(2)
    with overview:
        st.markdown("### Question & motivation")
        st.write(project["context"])
        st.markdown("### Dataset & scope")
        st.write(project["data"])
    with implementation:
        st.markdown("### Project implementation")
        st.write(project["contribution"])
        st.markdown("### Workflow & methods")
        st.write(project["approach"])
        st.markdown("**Tools**")
        st.markdown("".join(f'<span class="tool-chip">{escape(tool)}</span>' for tool in project["methods"]), unsafe_allow_html=True)

    result, interpretation = st.columns(2)
    with result:
        st.markdown("### Verified results & validation")
        st.write(project["validation"])
        st.markdown("### Interpretation")
        st.write(project["interpretation"])
    with interpretation:
        st.markdown("### Limitations")
        st.write(project["limitations"])
        st.markdown("### Evidence source")
        st.write(project["source"])

    if project["links"]:
        st.markdown("### Project links")
        render_links(project["links"])
    st.caption(f"Evidence basis: {project['source']}.")

    previous, next_column = st.columns(2)
    previous.page_link(
        f"pages/project_{previous_project['id']}.py",
        label=f"Previous · {previous_project['title']}",
        icon=":material/arrow_back:",
        use_container_width=True,
    )
    next_column.page_link(
        f"pages/project_{next_project['id']}.py",
        label=f"Next · {next_project['title']}",
        icon=":material/arrow_forward:",
        use_container_width=True,
    )


def render_footer() -> None:
    st.divider()
    st.caption("Priyanka Rauniyar · Analytics, business intelligence, and healthcare data")
