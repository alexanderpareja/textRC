#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from datetime import datetime
import os

def add_post(feed_path):
    # check for existing feed
    if not os.path.exists(feed_path):
        print(f"Ooops. RSS feed not found at '{feed_path}'")
        return

    # load existing rss feed
    tree = ET.parse(feed_path)
    root = tree.getroot()

    # find <channel> element
    channel = root.find("channel")
    if channel is None:
        print("Oops. Channel element not found")
        return
    
    # create post 
    print("Add a new post to your feed:")
    post_body = input("Enter text: ").strip()
    post_link = input("Link (Press Enter to skip): ").strip()

    #create a new <item> element
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "description").text = post_body
    if post_link:
        ET.SubElement(item, "link").text = post_link
    ET.SubElement(item, "pubDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")

    # save updated rss feed
    tree.write(feed_path, encoding="utf-8", xml_declaration=True)
    print(f"Post added to '{feed_path}'. ")

if __name__ == "__main__":
    # default path to rss feed
    feed_path = input("Enter the path to your RSS feed file (default: './rss.xml'): ").strip() or "./rss.xml"
    add_post(feed_path)