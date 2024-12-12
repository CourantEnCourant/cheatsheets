

###################################

from unidecode import unidecode

def unidecode(input: str, errors='ignore') -> str:
    """
    The 'errors' parameter takes 4 arguments:
        1. 'ignore': replace non-translatable characters with empty string
        2. 'strict': raise an 'UnicodeError'
        3. 'replace': replace with '?'
        4. 'preserve': keep the original
    """
    return "A string using ASCII letters"

###################################

from langdetect import detect

def detect(input: str) -> str:
    return 'Detected language of input string'