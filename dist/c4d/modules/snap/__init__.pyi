from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.documents import BaseDocument
from c4d import BaseContainer, BaseDraw, BaseObject, Matrix


def IsSnapEnabled(doc: BaseDocument, snapmode: int) -> bool:
    """    
    Check if snap is enabled for the document *doc* or for a specific *snapmode*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to test for.
    :type snapmode: int
    :param snapmode: Optionnally set a snap mode instead of checking snap for the document. One of the following:
    
    .. include:: /consts/SNAPMODE.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if snap is enabled, otherwise **False**.
    
    
    """
    ...

def EnableSnap(state: bool, doc: BaseDocument, snapmode: int) -> None:
    """    
    Set the snap enabled status for the document *doc* or a particular *snapmode*.
    
    :type state: bool
    :param state: The state to set: **True** to enable, **False** to disable.
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to set the snap mode state for.
    :type snapmode: int
    :param snapmode: Optionnally set a snap mode instead of enabling snap for the document. One of the following:
    
    .. include:: /consts/SNAPMODE.rst
    :start-line: 3
    
    
    """
    ...

def GetSnapSettings(doc: BaseDocument, snapmode: int) -> BaseContainer:
    """    
    Get the snap settings for the document *doc* or a specific *snapmode*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document related snap settings to retrieve.
    :type snapmode: int
    :param snapmode: Specify a snap mode to get or modify its specific settings instead of the global settings (pass **NOTOK**). One of the following:
    
    .. include:: /consts/SNAPMODE.rst
    :start-line: 3
    
    :rtype: c4d.BaseContainer
    :return: A copy of the settings in a :class:`BaseContainer <c4d.BaseContainer>`. The snap settings IDs are:
    
    .. include:: /consts/SNAP_SETTINGS.rst
    :start-line: 3
    
    .. include:: /consts/QUANTIZE.rst
    :start-line: 3
    
    
    """
    ...

def SetSnapSettings(doc: BaseDocument, bc: BaseContainer, snapmode: Optional[int] = ...) -> None:
    """    
    Set the snap settings for the document *doc* or a specific *snapmode*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to set the snap settings for.
    :type bc: c4d.BaseContainer
    :param bc: The :class:`BaseContainer <c4d.BaseContainer>` with the settings for the document *doc* and/or *snapmode*. The snap settings IDs are:
    
    .. include:: /consts/SNAP_SETTINGS.rst
    :start-line: 3
    
    .. include:: /consts/QUANTIZE.rst
    :start-line: 3
    
    :type snapmode: int
    :param snapmode: Optionally specify the snap mode to set the settings for instead of the global settings. One of the following:
    
    .. include:: /consts/SNAPMODE.rst
    :start-line: 3
    
    
    """
    ...

def IsQuantizeEnabled(doc: BaseDocument) -> bool:
    """    
    Check if quantizing is enabled for the document *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to test for.
    :rtype: bool
    :return: **True** if quantizing is enabled, otherwise **False**.
    
    
    """
    ...

def GetQuantizeStep(doc: BaseDocument, bd: BaseDraw, quantize_mode: int) -> None:
    """    
    Gets a quantize step value.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type bd: c4d.BaseDraw
    :param bd: Currently not used. Pass **None**.
    :type quantize_mode: int
    :param quantize_mode: The mode to retrieve the value for:
    
    .. include:: /consts/QUANTIZE.rst
    :start-line: 5
    
    
    """
    ...

def SetQuantizeStep(doc: BaseDocument, bd: BaseDraw, quantize_mode: int, val: float) -> None:
    """    
    Sets a quantize step value.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type bd: c4d.BaseDraw
    :param bd: Currently not used. Pass **None**.
    :type quantize_mode: int
    :param quantize_mode: The mode to set the value for:
    
    .. include:: /consts/QUANTIZE.rst
    :start-line: 5
    
    :type val: float
    :param val: The quantize step value to set.
    
    
    """
    ...

def GetWorkplaneObject(doc: BaseDocument) -> BaseObject:
    """    
    Retrieve the workplane object for document *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: c4d.BaseObject
    :return: The workplane object.
    
    
    """
    ...

def IsWorkplaneLock(doc: BaseDocument) -> bool:
    """    
    Get the workplane locked status for document *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: bool
    :return: **True** if the workplane is locked.
    
    
    """
    ...

def SetWorkplaneLock(bd: BaseDraw, locked: bool) -> None:
    """    
    Set the workplane locked status.
    
    :type bd: c4d.BaseDraw
    :param bd: The viewport to lock the workplane.
    :type locked: bool
    :param locked: **True** to lock the workplane.
    
    
    """
    ...

def GetWorkplaneMatrix(doc: BaseDocument, bd: BaseDraw) -> Matrix:
    """    
    Get the workplane matrix.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type bd: c4d.BaseDraw
    :param bd: The viewport you want to get the workplane's matrix from. If **None** the locked matrix is returned independently from view.
    :rtype: c4d.Matrix
    :return: The workplane matrix.
    
    
    """
    ...

