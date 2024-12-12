class Path:
    def __init__(self, path: str=None):
        self.name = "File/folder name"
        self.stem = "File/folder stem"
        self.suffix = "File suffix. Empty string if folder"
        self.parent = "Parent folder"

    # General methods

    def cwd(self) -> str:
        return "Current working directory"

    def exists(self) -> bool:
        return "Whether the file/folder exists"

    def absolute(self) -> str:
        return "Absolute path"

    def rename(self, path_with_new_name: Path) -> None:
        return "Rename file/folder in directory"

    # Folder management methods

    def create_child_folder(self, parent_folder, child_folder) -> Path:
        """Syntaxe: child_folder = parent_folder / child_folder"""
        return "A new child/grandchild Path"

    def is_dir(self) -> bool:
        return "Whether the Path is a folder"

    def mkdir(self) -> None:
        """Create folder"""
        return None
        
    def rmdir(self) -> None:
        """Delete folder in file system"""
        return None

    # File management methods

    def is_file(self) -> bool:
        return "Whether the Path is a file"

    def touch(self) -> None:
        """Create new file"""
        return None

    def unlink(self) -> None:
        """"Delete file"""
        return None

    # Reading directoies

    def glob(self, pattern: str, case_sensitive: bool=False) -> List[Path]:
        """Patterns include wilcards. Examples: `*.py`, `**/*`"""
        return "List of files/folders who match pattern"


