#!/usr/bin/python3
"""Function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit: subreddit name

    Returns:
        Number of subscribers to the subreddit,
        or 0 if the subreddit requested is invalid
    """
    # Set the User-Agent header to avoid issues with Too Many Requests
    headers = {'User-Agent': 'xica369'}

    # Construct the URL for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        return response.json().get("data").get("subscribers")
    else:
        # Return 0 if the subreddit is invalid or if there's an issue with the request
        return 0


if __name__ == "__main__":
    import sys

    # Check if the script is executed with the required command-line argument
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the function and print the result
        subscribers_count = number_of_subscribers(sys.argv[1])
        print(subscribers_count)
