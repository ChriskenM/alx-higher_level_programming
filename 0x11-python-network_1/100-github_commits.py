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
            owner_name, repo_name)

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))

    except requests.exceptions.HTTPError as errh:
        print("Error code: {}".format(response.status_code))
    except ValueError:
        print("Not a valid JSON")
    except Exception as err:
        print("Error: {}".format(err))
