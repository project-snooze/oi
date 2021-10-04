import requests
import base64
import asyncio
import ast
import json

async def post_photo(image):
    print("Started into the post image method")
    url = "https://api.imgbb.com/1/upload"
    key = "0f6acb0d66647a379e2766ac4592d0c7"
    headers = {"key": key}
    porc = {"image": image}
    response = requests.request("POST", url, params=headers, data=porc)
    return str(response.content)

images=[]

with open("oile/3.png", "rb") as file:
    hopa=asyncio.run(post_photo(base64.b64encode(file.read())))
    m=ast.literal_eval(hopa)
    n=m.decode("utf-8")
    p=json.loads(n)
    images.append(p['data']['url'])

for i in range(10):
    i+=1
    poza="oile/"+str(i)+".png"
    with open(poza, "rb") as file:
        hopa=asyncio.run(post_photo(base64.b64encode(file.read())))
        m=ast.literal_eval(hopa)
        n=m.decode("utf-8")
        p=json.loads(n)
        url=p['data']['url']
        images.append(url)
        print(images)
        with open("images.txt", "a+") as f:
            f.write("\n"+url)

print(images)