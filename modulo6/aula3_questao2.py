urls = ["www.google.com", "www.github.com", "www.reddit.com"]


urls = [url.replace("www.", "").replace(".com", "") for url in urls]

print(urls)
