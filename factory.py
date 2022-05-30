from functools import wraps


class InstantiationError(Exception):
    """
    Raised when an object is being created without a factory method.
    """
    pass


def no_make(init_fn):
    """
    Decorator for 'hiding' the constructor. In particular the decorator ensures that the instance has been created.
    using a factory method.
    :param init_fn: The constructor (__init__) function.
    :return: The wrapped constructor.
    """

    @wraps(init_fn)
    def _no_make(self, secret, *args, **kwargs):
        stored_secret = getattr(self, "__factory_key", None)
        if not stored_secret or secret is not stored_secret:
            raise InstantiationError(f"Not allowed to instantiate {type(self).__name__} directly")
        init_fn(self, secret, *args, **kwargs)

    return _no_make


def make(fn):
    """
    Decorator for converting a class method to a factory method.
    :param fn: The class method.
    :return: The wrapped factory method.
    """

    @wraps(fn)
    def _make(cls, *args, **kwargs):
        secret = getattr(cls, "__factory_key", None)
        if not secret:
            secret = object()
            setattr(cls, "__factory_key", secret)
        return fn(cls, secret, *args, **kwargs)

    return _make


def factory(cls):
    """
    Decorator for declaring a class as factory. In particular the decroator ensures that instances of the class are
    created using a factory method.
    :param cls: The class to be declared as a factory.
    :return: The decorated class.
    """
    old_init = getattr(cls, "__init__")

    def patch_init(self, secret, *_args, **_kwargs):
        stored_secret = getattr(self, "__factory_key", None)
        if not stored_secret or secret is not stored_secret:
            raise InstantiationError(f"Not allowed to instantiate {type(self).__name__} directly")
        old_init(self, secret, *_args, **_kwargs)

    setattr(cls, "__init__", patch_init)
    return cls
