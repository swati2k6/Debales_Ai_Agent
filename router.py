def route_query(query):
    query = query.lower()

    if "debales" in query:
        return "rag"
    else:
        return "serp"