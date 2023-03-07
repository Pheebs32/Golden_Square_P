def grammar(text: str):
    front = text[0]
    end = text[-1]
    punctuation = ['!', '?', '.']
    if (front == front.upper()) and (end in punctuation):
        return True
    return False
