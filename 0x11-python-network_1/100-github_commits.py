#!/usr/bin/python3
"""
Fetches and prints 10 most recent commits of a repository
from a specified owner using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name
    )

    response = requests.get(url)
    commits = response.json()

    for i, commit in enumerate(commits[:10]):
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")
        ))
