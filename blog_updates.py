#!/usr/bin/env python3

import argparse
from get_blogs import get_blog_posts, get_top_blog_posts, BLOG_URL

def main(number_of_posts):
    top_blog_posts = get_top_blog_posts(BLOG_URL, number_of_posts=number_of_posts)
    if top_blog_posts:
        for title, url, date in top_blog_posts:
            print(f"Title: {title}")
            print(f"Date: {date}")
            print(f"URL: {url}\n")
    else:
        print("No blog posts found.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch the latest blog posts from OpenAI.')
    parser.add_argument('-n', '--blogs', type=int, default=2, help='Number of blog posts to fetch')
    args = parser.parse_args()

    main(args.blogs)
