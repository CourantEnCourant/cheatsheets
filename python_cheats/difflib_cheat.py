import difflib

class SequenceMatcher(difflib.SequenceMatcher):

    def __init__(self, isjunk: function=None, a: str='', b: str='', autojunk: bool=True) -> :
        """
        :param isjunk:
        :param a:
        :param b:
        :param autojunk:
        """