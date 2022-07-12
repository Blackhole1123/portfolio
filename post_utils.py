import json

def add_post(name, url, date, summary, categories):
    post = {
        "name": name,
        "url": url,
        "date": date,
        "summary": summary,
        "categories" : categories
    }
    post = json.dumps(post)
    with open("posts.json", "a") as f:
        f.write(post)
        f.write("\n")
    print("Post added")