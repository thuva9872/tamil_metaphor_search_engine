from elasticsearch import Elasticsearch

from query import *


INDEX = 'sample3'
client = Elasticsearch(['http://localhost:9200'])


def process_query(query):
    # Keyword-based differentiation
    if ":" in query:
        keywords = query.split(':')
        if keywords[0] == "பாடல்":
            query_body = search_with_field(keywords[1], "பாடல்")
        elif keywords[0] == "படம்":
            query_body = search_with_field(keywords[1], "படம்")
        elif keywords[0] == "வருடம்":
            if "-" in keywords[1]:
                lte, gte = keywords[1].strip().split("-")
                query_body = search_range(gte, lte)
            else:
                query_body = search_with_field(keywords[1].strip(), "வருடம்")
        elif keywords[0] == "இசைமைப்பாளர்":
            query_body = search_with_field(keywords[1], "இசைமைப்பாளர்")
        elif keywords[0] == "பாடகர்":
            query_body = search_with_field(keywords[1], "பாடகர்")
        elif keywords[0] == "பாடல்வரிகள்":
            query_body = search_with_field(keywords[1], "பாடல்வரிகள்")
    # Exact match search query
    elif '''”''' in query or '''"''' in query:
        query_body = exact_search(query)
    # Wild card match search query
    elif '*' in query:
        query_body = wild_card_search(query)
    # Basic search query
    else:
        query_body = basic_search(query)
    return query_body


def search(query):
    query_body = process_query(query)
    print('Searching...')
    resp = client.search(index=INDEX, body=query_body)
    return resp
