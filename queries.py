def no_query(text):
    return text

def mention_tracker(text, pipeline, query):
    processed_text = text
    for step in pipeline:
        processed_text = step(text=processed_text)
    query_result = query(processed_text)
    return query_result