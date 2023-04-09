import os

def make_txt_entry(school_name=None,
                     publication_date=None,
                     text=None):
    if school_name is None or publication_date is None or text is None:
        return RuntimeError("Function make_txt_entry has invalid arguments.")
    
    file_path = "journal_data/txt/"+school_name.replace(" ","_")+"/"+publication_date+".txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)