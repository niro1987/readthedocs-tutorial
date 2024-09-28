"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.


    Parameters:
        kind (list[str] | None, Optional): "kind" of ingredients. 
    
    Raises:
        lumache.InvalidKindError: If the kind is invalid.

    Returns:
        list[str]: The ingredients list.

    """
    return ["shells", "gorgonzola", "parsley"]
