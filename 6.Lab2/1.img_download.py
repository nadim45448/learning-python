""" 
download and change the wallpaper automatically
 """

 
import requests
import json
# import PyWallpaper
api_url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response=requests.get(api_url)
# content=response.content 
content=response.content.decode('UTF-8')
# print(type(content))

# convert string to json
dict_content=json.loads(content)

# get the image url
image_url=dict_content['url']

# download the image
res=requests.get(image_url)

# save img
with open('apod.png','wb') as image:
    image.write(res.content)

# set as wallpaper
# PyWallpaper.change_wallpaper('D:\coding\Python\apod.png')

"""  
import requests

api_key = "DEMO_KEY"
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the JSON data
response = requests.get(api_url)
data = response.json()

# Get the image URL
image_url = data['url']

# Download the image
image_response = requests.get(image_url)

# Save the image
with open('apod.jpg', 'wb') as image_file:
    image_file.write(image_response.content)

print("Image downloaded successfully!")
"""

