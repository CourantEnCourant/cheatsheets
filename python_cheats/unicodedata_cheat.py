import unicodedata

def remove_diacritics(text: str) -> str:
    normalized_text = unicodedata.normalize('NFD', text)  # NFD: Normalization Form Decomposition
    stripped_str = ''.join(c for c in normalized_text if unicodedata.category(c) != 'Mn')  # Mn: Mark, Non-spacing
    return stripped_str
