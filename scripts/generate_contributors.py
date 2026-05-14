#!/usr/bin/env python3
"""
Fetch contributors from all Vyrox public repos,
deduplicate, and write a markdown list with avatars & usernames.
"""
import os, requests, sys
from collections import OrderedDict

REPOS = [
    "vyrox-proxy",
    "vyrox-docs",
    "vyrox-simulator",
    "vyrox-landing",
]

ORG = "vyrox-security"
TOKEN = os.environ["GH_TOKEN"]  # GitHub PAT with 'public_repo' scope

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

def get_contributors(repo):
    """Return list of (login, avatar_url, contributions) for a repo."""
    url = f"https://api.github.com/repos/{ORG}/{repo}/contributors?per_page=100"
    contributors = []
    while url:
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print(f"Error fetching {repo}: {r.status_code}", file=sys.stderr)
            break
        data = r.json()
        for c in data:
            contributors.append((c["login"], c["avatar_url"], c["contributions"]))
        # Pagination
        url = r.links.get("next", {}).get("url") if "next" in r.links else None
    return contributors

def main():
    all_contribs = OrderedDict()  # login -> (avatar_url, total_contributions)

    for repo in REPOS:
        for login, avatar, count in get_contributors(repo):
            if login in all_contribs:
                prev_avatar, prev_count = all_contribs[login]
                all_contribs[login] = (prev_avatar, prev_count + count)
            else:
                all_contribs[login] = (avatar, count)

    # Sort by total contributions descending
    sorted_contribs = sorted(all_contribs.items(), key=lambda x: x[1][1], reverse=True)

    # Generate markdown
    md_lines = ["## Contributors\n"]
    md_lines.append("<!-- auto-generated; do not edit -->\n")
    md_lines.append('<table><tr>\n')
    for login, (avatar_url, total) in sorted_contribs:
        md_lines.append(
            f'  <td align="center"><a href="https://github.com/{login}">'
            f'<img src="{avatar_url}&s=80" width="80px;" alt="{login}"/><br />'
            f'<sub><b>{login}</b></sub></a></td>\n'
        )
    md_lines.append('</tr></table>\n')
    md_lines.append(f"\n<sub>Total unique contributors: {len(sorted_contribs)}</sub>\n")

    # Write to a file that will be inserted into the README
    with open("contributors.md", "w") as f:
        f.writelines(md_lines)

if __name__ == "__main__":
    main()