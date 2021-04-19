class dotdict(dict):
    """
      dot.notation access to dictionary attributes
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def dot_notation(func):
    def wraper(*args, **kwargs):
        try:
            return dotdict(func(*args, **kwargs))
        except TypeError:
            return None

    return wraper
