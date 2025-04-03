# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 08:08:23 2025

@author: Hemal
"""

import streamlit as st
import feedparser
import pandas as pd

# Function to fetch and parse RSS feed

def fetch_news(rss_url):
    feed = feedparser.parse(rss_url)
    news_items = []
    for entry in feed.entries:
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        })
    return news_items

# List of categories
categories = [ "mostrecent"]

# Function to construct the URL based on user input
def construct_url(category):
    base_url = "https://timesofindia.indiatimes.com/rssfeed"
    full_url = f"{base_url}{category}.cms"
    return full_url

# Streamlit app layout
st.title("News Feed Reader")

# Dropdown to select a category
selected_category = st.selectbox("Select a category", categories)

# Construct the RSS URL based on the selected category
rss_url = construct_url(selected_category)

# Button to fetch news
if st.button("Fetch News"):
    news_items = fetch_news(rss_url)
    if news_items:
        # Convert news items to a DataFrame
        df = pd.DataFrame(news_items)
        # Display news items in a table
        st.write("Fetched News Items")
        for index, row in df.iterrows():
            st.write(f"**[{row['title']}]({row['link']})**")
            st.write(f"Published: {row['published']}")
            st.write(row['summary'])
            st.write("---")
    else:
        st.write("No news items found.")
