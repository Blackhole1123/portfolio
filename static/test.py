import json
import os

def post_api(post):
    o = open("/Users/rishaandesai/Websites/portfolio/posts.json", "r")
    posts = o.readlines()
    o.close()
    posts = [json.loads(i) for i in posts]
    for p in posts:
        if p["name"] == post:
            return p

print(post_api("cryosleep"))