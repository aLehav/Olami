# Remove specific parts of text from a string
def text_removal_processing(removable_string): 
    return lambda text: text.replace(removable_string, "\n")