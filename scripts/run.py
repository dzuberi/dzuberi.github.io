import json
import yaml  # Add this import
import os
from scholarly import scholarly
import time
import random
from scholarly import ProxyGenerator
import urllib.parse
from pprint import pprint
import re

# Set up a ProxyGenerator object to use free proxies
if False:
    pg = ProxyGenerator()
    if not pg.FreeProxies(repeat=True):
        print("Error: No free proxies available. Exiting.")
        exit(1)
    scholarly.use_proxy(pg)

def fetch_author(author_id):
    retries = 5
    for _ in range(retries):
        try:
            author = scholarly.search_author_id(author_id)
            return scholarly.fill(author)
        except Exception as e:  
            print(f"Error: {e}. Retrying...")
            time.sleep(random.uniform(5, 10))  
    print("Failed to fetch author after retries.")
    return None

# def extract_authors(citation):
#     # This assumes the citation is in the form: "Author1, Author2, Author3, ..., Title"
#     match = re.match(r"(.+?),\s*(.+?),\s*(.*)", citation) 
#     if match:
#         return match.group(1) 
#     return "Unknown Authors"


author_id = "_hr4TpEAAAAJ"
author = fetch_author(author_id)
if author:
    publications = []

    if not author.get('publications'):
        print("Warning: No publications found for this author.")
    
    for pub in author.get('publications', []):  
        bib = pub.get('bib', {})
        title = bib.get("title", "Unknown Title")
        
        author_pub_id = pub.get('author_pub_id', "")
        
        authors = ""
        title = ""
        year = ""
        venue = ""
        url = ""
        abstract = ""

        try:
            publication = scholarly.fill(pub)
        except Exception as e:
            print(f"Error fetching publication details for {title}: {e}")
            
        if publication:
            authors = publication.get("bib", {}).get("author", "")
            title = publication.get("bib", {}).get("title", "")
            year = publication.get("bib", {}).get("pub_year", "")
            venue = publication.get("bib", {}).get("citation", "")
            url = publication.get("pub_url", f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={urllib.parse.quote_plus(title)}+Danial+Zuberi")
            abstract = publication.get("bib", {}).get("abstract", "")
        else:
            continue

        publications.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "url": url,
            "abstract": abstract,
        })



    with open("../_data/publications.yaml", "w") as f:
        yaml.dump(publications, f, allow_unicode=True, sort_keys=False, width=float("inf"))

    print("Publications saved successfully.")
else:
    print("Failed to retrieve author data.")

