import url_scanner as reader
import time, datetime
import flask_app, flask_wrapper

"""html = reader.get_html('https://all.me')
print("html found")
urls = reader.find_github_urls(html)
print("urls found")
url = reader.choose_url(urls)
print("url chosen")

print(url)"""

flask_wrapper.update_row(3)