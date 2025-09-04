from typing import Callable

class Model:
    def __init__(self):
        pass

    def from_pretrain(self, checkpoint, cache_dir):
        """
        :param checkpoint: load from a checkpoint
        :param cache_dir: specify a store location
        :return: Model
        """
        return


class Dataset:
    features: dict
    """
    Example: {'id': Value(dtype='string', id=None), 
              'title': Value(dtype='string', id=None), 
              'context': Value(dtype='string', id=None)}
    """

    def __init__(self, dataset, split):
        pass

    @staticmethod
    def load_dataset(self, checkpoint, streaming, cache_dir):
        """
        :param checkpoint:
        :param streaming: use streaming to avoid download
        :param cache_dir:
        :return:
        """
        pass

    def save_to_disk(self, path: Path | str):
        """Save current pa"""
        return

    def filter(self, func: Callable):
        """Filter from a boolian lambda expression"""
        return

    def shuffle(self, seed: int):
        """Shuffle"""
        return

    def map(self, func: Callable, num_proc: int, desc: str):
        """
        :param func: transformation lambda expression
        :param num_proc: transform 4 examples at a time
        :param desc: description
        :return:
        """
        """
        Example of a func:
        def tokenize_question(example):
            example['tokenized_question_context'] = tokenizer.tokenize(example['question'],  
                                                                       example['context'],
                                                                       truncation=True,
                                                                       padding="max_length",
                                                                       max_length=512)
            return example
        """
        return

    def add_column(self, column_name: str, column: list):
        return

    def set_format(self, type: str):
        """
        :param type: valid options are [None, 'numpy', 'torch', 'tensorflow', 'jax', 'arrow', 'pandas', 'polars']
        :return:
        """
        return
