def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q


def search_with_field(query, field):
    q = {
        "query": {
            "match": {
                field: query
            }
        }
    }
    return q


def exact_search(query):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase"
            }
        }
    }
    return q


def wild_card_search(query):
    q = {
        "query": {
            "wildcard": {
                "பாடல்வரிகள்": {
                    "value": query
                }
            }
        },
    }
    return q


def search_range(lte, gte):
    q = {
        "query": {
            "range": {
                "வருடம்": {
                    "gte": gte,
                    "lte": lte
                }
            }
        },
        "sort": [
            {
                "வருடம்": {
                    "order": "asc"
                }
            }
        ]
    }
    return q
