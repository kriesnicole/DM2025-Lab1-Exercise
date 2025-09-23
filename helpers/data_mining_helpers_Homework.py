import nltk

def format_rows(docs):
    """Format a list of text documents and strip special characters"""
    D = []
    for d in docs:  # docs ist jetzt eine Liste von Texten
        temp_d = " ".join(str(d).split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, label_map=None):
    """Format numeric labels into human-readable labels"""
    if label_map is not None:
        return label_map.get(target, "Unknown")
    return target  # falls keine Mapping-Dictionary übergeben wird, return original

def check_missing_values(row):
    """Check and count missing values in a row"""
    counter = 0
    for element in row:
        if element is True:
            counter += 1
    return ("The amount of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            tokens.append(word)
    return tokens
