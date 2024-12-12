from typing import List


class Os:
    def __init__(self):
        path = Path()

    def getcwd(self) -> str:
        return "Absolute path of cwd"

    def chdir(self) -> None:
        """Change cwd to """
        return "Change cwd"

    def listdir(self, path: str='.') -> List[str]:
        return "List of contents inside directory"

    def mkdir(self, folder: str) -> None:
        return "Create folder"

    def rmdir(self, folder: str) -> None:
        return "Delete folder"

    def makedirs(self, folder_with_children: str, exist_ok=False) -> None:
        """Set exist_ok=True prevents from crashing when creating dirs that already exist"""
        return "Create folder and all its children"


class Path:
    def __init__(self):
        pass

    def exists(self) -> bool:
        return "Whether the file/folder exists"

    def isdir(self) -> bool:
        return "Whether the Path is a folder"

    def isfile(self) -> bool:
        return "Whether the Path is a file"

