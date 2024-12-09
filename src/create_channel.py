#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from datetime import datetime
import os
import argparse

def create_channel(output_dir):
    # check if output directory already exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"New folder created: {output_dir}")
    print("Welcome to the RSS Channel Creator!")
    
    # prompt user for channel info
    name = input("Enter your Name (for the channel): ").strip() 
    bio = input("Enter your Bio: ").strip()
    picture_url = input("Enter your Channel Picture URL: ").strip()
    contact = input("Enter your Contact Info (optional): ").strip() or None
    
    # create root RSS element
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    # add channel metadata
    ET.SubElement(channel, "title").text = name
    ET.SubElement(channel, "description").text = bio
    if contact:
        ET.SubElement(channel, "link").text = contact
    
    # ass channel image
    if picture_url:
        image = ET.SubElement(channel, "image")
        ET.SubElement(image, "url").text = picture_url
        ET.SubElement(image, "title").text = name
        if contact:
            ET.SubElement(image, "link").text = contact

    # add date
    ET.SubElement(channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    # generate rss.xml
    output_file = os.path.join(output_dir, "rss.xml")
    tree = ET.ElementTree(rss)
    with open(output_file, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print(f"RSS Channel created successfully! File saved as {output_file}.")

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description="Create an RSS Channel")
    parser.add_argument(
        "output_dir",
        nargs="?", # makes arg optional
        default=".", # defaults to current directory
        help="The directory where the RSS file will be created. If not specified, it will default to the current directory."
    )
    args = parser.parse_args()
    create_channel(args.output_dir)
