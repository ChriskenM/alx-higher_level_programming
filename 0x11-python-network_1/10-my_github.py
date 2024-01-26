#!/usr/bin/python3
"""
Uses GitHub API to display user id using Basic Authentication
with a personal access token.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()

        json_data = response.json()
        print("{}".format(json_data['id']))
    except requests.exceptions.HTTPError as errh:
        print("Error code: {}".format(response.status_code))
    except ValueError:
        print("Not a valid JSON")
    except Exception as err:
        print("Error: {}".format(err))
