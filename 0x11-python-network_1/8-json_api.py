#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
Displays id & name if the response is properly JSON formatted and not empty.
Otherwise, prints appropriate messages.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except requests.exceptions.HTTPError as errh:
        print("Error code: {}".format(response.status_code))
    except ValueError:
        print("Not a valid JSON")
    except Exception as err:
        print("Error: {}".format(err))
