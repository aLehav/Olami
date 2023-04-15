def no_query(text):
    return text

def count_query(count_string):
    return lambda text: text.count(count_string)

def one_query(text):
    return 1

def hillel_counter(text):
    return count_query("Hillel")(text)

def mention_tracker(text, pipeline, query):
    processed_text = text
    for step in pipeline:
        processed_text = step(text=processed_text)
    query_result = query(processed_text)
    return query_result