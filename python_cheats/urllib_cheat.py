from typing import Tuple

# urllib.reequest module

def urlretrieve(url: str, filename=None) -> Tuple[str, HttpMessage]:
    """
    Download the url html page, or the file associated with it.
    If "filename" parameter not specified, file will be stored in a temp directory in /var/...
    Example: downloadpath, http_message = urlretrieve(file_url, file_local_path)
    """
    return ("str passed to filename parameter", "http response as HttpMessage object")


def urlopen():
    NotImplemented