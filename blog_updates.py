# main.py
from get_blogs import get_blog_posts, get_top_blog_posts, BLOG_URL


top_blog_posts = get_top_blog_posts(BLOG_URL, number_of_posts=2)
if top_blog_posts:
    for title, url, date in top_blog_posts:
        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"URL: {url}\n")
else:
    print("No blog posts found.")
