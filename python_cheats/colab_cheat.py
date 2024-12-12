# drive module
from google.colab import drive

def mount(path: str="content/") -> None:
    """Mount your google drive. Execute os.chdir() to set desired cwd"""