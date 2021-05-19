from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable


def StringConvertTokens(path: str, rpData: Dict[str, Any]) -> bool:
    """    
    Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
    
    :type path: str
    :param path: The original path string.
    :type rpData: dict
    :param rpData:
    
    The data used to extract value for Tokens. See :ref:`renderpathdata_dictionary`.
    
    :rtype: bool
    :return: The converted string, or the original path if any error.
    
    
    """
    ...

def FilenameConvertTokens(path: str, rpData: Dict[str, Any]) -> bool:
    """    
    Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
    
    :type path: str
    :param path: The original path filename.
    :type rpData: dict
    :param rpData:
    
    The data used to extract value for Tokens.  See :ref:`renderpathdata_dictionary`.
    
    :rtype: bool
    :return: The converted filename, or the original path if any error.
    
    
    """
    ...

def StringConvertTokensFilter(path: str, rpData: Dict[str, Any], exclude: List[Any]) -> bool:
    """    
    | Converts tokenized path string to standard String by replacing all Tokens with correct values if found.
    | Tokens added to *exclude* array are ignored.
    
    :type path: str
    :param path: The original path string.
    :type rpData: dict
    :param rpData:
    
    The data used to extract value for Tokens. See :ref:`renderpathdata_dictionary`.
    
    :type exclude: list
    :param exclude: A list of Tokens strings to be ignored.
    :rtype: bool
    :return: The converted string, or the original path if any error.
    
    
    """
    ...

def FilenameConvertTokensFilter(path: str, rpData: Dict[str, Any], exclude: List[str]) -> bool:
    """    
    | Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
    | Tokens added to *exclude* array are ignored.
    
    :type path: str
    :param path: The original path filename.
    :type rpData: dict
    :param rpData:
    
    The data used to extract value for Tokens. See :ref:`renderpathdata_dictionary`.
    
    :type exclude: list of str
    :param exclude: A list of Tokens strings to be ignored.
    :rtype: bool
    :return: The converted filename, or the original path if any error.
    
    
    """
    ...

def StringExtractRoot(path: str) -> bool:
    """    
    | Searches for the first Token in *path*.
    | If it is found and it is in-between "/.." returns the preceeding directory path string.
    
    :type path: str
    :param path: The original path string.
    :rtype: bool
    :return: The root string path, or the original string if no Token is found.
    
    
    """
    ...

def FilenameExtractRoot(path: str) -> bool:
    """    
    | Searches for the first Token in *path*.
    | If it is found and it is in-between "/.." returns the preceeding directory path filename.
    
    :type path: str
    :param path: The original path filename.
    :rtype: bool
    :return: The root filename path, or the original filename if no Token is found.
    
    
    """
    ...

def FilenameSlicePath(path: str) -> Tuple[str, str]:
    """    
    Splits *path* in two parts if a Token is found as sub-folders and extracts root and filename path starting at sub-folder.
    
    :type path: str
    :param path: The original path filename.
    :rtype: tuple(str, str)
    :return: The root and filename paths.
    
    
    """
    ...

def GetAllTokenEntries() -> List[Dict[str, Any]]:
    """    
    Returns a list of all available Token entries.
    
    .. versionadded:: R17.053
    
    For instance the following code prints all registered tokens
    
    .. code-block:: python
    
    import c4d
    
    tokens = c4d.modules.tokensystem.GetAllTokenEntries()
    for entry in tokens:
    print entry
    
    :rtype: list of dict
    :return: All the registered Token information, or **None** if an error occurred.
    
    
    """
    ...

