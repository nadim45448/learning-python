import requests
api_url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_response(url):
    return requests.get(url)

if __name__=="_main_":
    
    # print(__name__)

    res=get_response(api_url)
    print(res)
