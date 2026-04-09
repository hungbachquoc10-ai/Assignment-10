import requests as req
def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        res = req.get(url)
        res.raise_for_status()
        data = res.json()
        print(data['value'])
    except req.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
if __name__ == "__main__":
    get_chuck_norris_joke()