def get_wikipedia_page(url):
    import requests

    print("Getting Wikipedia page...", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # check if the request is successful

        return response
    except requests.RequestException as e:
        print(f"An error occurred:", {e})
        return None