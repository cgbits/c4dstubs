from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.documents import BaseDocument, LayerObject, RenderData
from c4d.storage import HyperFile, ByteSeq
from c4d.bitmaps import BaseBitmap, GeClipMap
from c4d.utils import Neighbor
from c4d.modules.render import ChannelData, InitRenderStruct
from c4d.plugins import BaseDrawHelp
from c4d.gui import EditorWindow
from c4d.modules.mograph import FieldInfo, FieldInput, FieldOutput, FieldLayer
from c4d.modules.net import NetRenderService
from c4d.threading import BaseThread
from c4d.symbols import *
from c4d import bitmaps, plugins, utils, storage, gui, documents, threading, modules


class AliasTrans(object):
    def Init(self, doc: BaseDocument) -> bool:
        """    
        Initializes the alias translator in the specified document *doc*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :rtype: bool
        :return: **True** if the alias translator was initialized, otherwise **False**.
        
        
        """
        ...
    
    def Translate(self, connect_oldgoals: bool) -> None:
        """    
        Translates the links in all objects that the translator has come across.
        
        :type connect_oldgoals: bool
        :param connect_oldgoals:
        
        | **True** to connect old goals.
        | For example: Take a cube with an instance linked to this cube, select both and duplicate them in one action.
        | The new cube is linked to the new instance if *connect_oldgoals* is **True**.
        | If it is **False** the new instance is linked to the old cube.
        
        
        """
        ...
    

class BaseSelect(object):
    def __init__(self) -> None:
        """    
        Initializes a new base selection.
        
        :rtype: c4d.BaseSelect
        :return: The new base selection.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Get the number of selected elements.
        
        :rtype: int
        :return: The number of selected elements.
        
        
        """
        ...
    
    def GetSegments(self) -> int:
        """    
        | Get the number of segments that contain elements.
        | For example: the selections 0..4, 6..7, 9..12 would be three segments.
        | This method would return 3 and :meth:`GetCount` would return 11.
        
        :rtype: int
        :return: The number of selected segments.
        
        
        """
        ...
    
    def IsSelected(self, num: int) -> bool:
        """    
        Get the selection state of an element.
        
        To efficiently go through selections use the following code.
        
        .. code-block:: python
        
        bs = op.GetPointS()
        sel = bs.GetAll(op.GetPointCount())
        for index, selected in enumerate(sel):
        if not selected: continue
        print "Index", index, "is selected"
        
        This is faster than.
        
        .. code-block:: python
        
        bs = op.GetPointS()
        for index in xrange(op.GetPointCount()):
        if bs.IsSelected(index):
        print "Index", index, "is selected"
        
        :type num: int
        :param num: The element index to select.
        :rtype: bool
        :return: **True** if the element was already selected.
        
        
        """
        ...
    
    def Select(self, num: int) -> bool:
        """    
        Selects an element.
        
        :type num: int
        :param num: The element index to select.
        :rtype: bool
        :return: **True** if the element was already selected.
        
        
        """
        ...
    
    def SelectAll(self, max: int, min: int, deselectAll: bool) -> bool:
        """    
        Selects all elements within the given range.
        
        .. note::
        
        All previous selections are cleared.
        
        .. warning::
        
        *min* and *max* parameters are swapped compared to the C++ API version and *min* gets a default value of `0`.
        
        Here is an example showing how to select all the edges of a :class:`PolygonObject <c4d.PolygonObject>`.
        
        .. code-block:: python
        
        import c4d
        
        def main():
        nbr = c4d.utils.Neighbor()
        nbr.Init(op) # Initialize neighbor with a polygon object
        
        edges = c4d.BaseSelect()
        edges.SelectAll(nbr.GetEdgeCount()-1) # Select all edges in the range [0, nbr.GetEdgeCount()]
        
        op.SetSelectedEdges(nbr, edges, c4d.EDGESELECTIONTYPE_SELECTION) # Select edges from our edges selection
        c4d.EventAdd() # Update Cinema 4D
        
        if __name__ == '__main__':
        main()
        
        :type max: int
        :param max: The last element in the range to select.
        :type min: int
        :param min: The first element in the range to select. Default to `0`.
        :type deselectAll: bool
        :param deselectAll:
        
        .. versionadded:: R17.048
        
        Deselects all previously selected elements before creating the new selection (equivalent to **SELECTION_NEW**).
        
        :rtype: bool
        :return: Success of selecting the elements.
        
        
        """
        ...
    
    def Deselect(self, num: int) -> bool:
        """    
        Deselects an element.
        
        :type num: int
        :param num: The element index to deselect.
        :rtype: bool
        :return: **True** if the element was already deselected.
        
        
        """
        ...
    
    def DeselectAll(self) -> bool:
        """    
        Deselect all elements.
        
        :rtype: bool
        :return: Success of deselecting all elements.
        
        
        """
        ...
    
    def Toggle(self, num: int) -> bool:
        """    
        Toggles the selection state of an element.
        
        :type num: int
        :param num: The index of the element to toggle.
        :rtype: bool
        :return: Success of changing the selection state of the element.
        
        
        """
        ...
    
    def ToggleAll(self, min: int, max: int) -> bool:
        """    
        Toggle the selection state of all elements in the given range.
        
        :type min: int
        :param min: The first element to toggle.
        :type max: int
        :param max: The last element to toggle in the range.
        :rtype: bool
        :return: Success of changing the selection state.
        
        
        """
        ...
    
    def GetRange(self, seg: int, max: int) -> Tuple[int, int]:
        """    
        | Returns the selected elements contained in a segment.
        | See :meth:`BaseSelect.GetSegments`.
        
        .. versionadded:: R19
        
        :type seg: int
        :param seg: The segment to get the elements for: 0 <= *seg* < :meth:`GetSegments`
        :type max: int
        :param max:
        
        | The maximum value for the returned elements numbers.
        | Usually pass :meth:`PolygonObject.GetPolygonCount` or :meth:`PointObject.GetPointCount` or the edge count of the object.
        | The method makes sure they are < *max*.
        
        :rtype: tuple(int,int)
        :return:
        
        | The index of the first and last selected elements in the given segment.
        | If the segment has a length of one, the same if will be set for the first and last entry in the tuple.
        | **None** if the function failed.
        
        
        """
        ...
    
    def Merge(self, src: BaseSelect) -> bool:
        """    
        Selects all elements that are selected in *src*.
        
        :type src: c4d.BaseSelect
        :param src: The source selection object.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DeselectFrom(self, src: BaseSelect) -> bool:
        """    
        Deselects all elements that are selected in *src*.
        
        .. note::
        
        For C++ developers: This function is redirected to **Bool Deselect(const BaseSelect *src)**
        
        :type src: c4d.BaseSelect
        :param src: The source selection object.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Cross(self, src: BaseSelect) -> bool:
        """    
        Intersects all elements in *src*.
        
        .. versionadded:: R19
        
        :type src: c4d.BaseSelect
        :param src: The source selection object.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetClone(self) -> BaseSelect:
        """    
        Make a duplicate of this selection object with its elements.
        
        :rtype: c4d.BaseSelect
        :return: The clone object.
        
        
        """
        ...
    
    def GetDirty(self) -> int:
        """    
        | Returns the dirty counter of the selection.
        | This counter is increased every time a function is called that changes the selection.
        
        :rtype: int
        :return: Dirty counter.
        
        
        """
        ...
    
    def CopyTo(self, dest: BaseSelect) -> bool:
        """    
        Copy the selection elements in this selection object to another BaseSelect.
        
        :type dest: c4d.BaseSelect
        :param dest: The destination selections object.
        :rtype: bool
        :return: Success of copying the selection elements.
        
        
        """
        ...
    
    def SetAll(self, states: List[int]) -> bool:
        """    
        | Set all selected elements from a list.
        | The elements in the list are interpreted as boolean: `0` means the element is `unselected`, and `1` means it is `selected`.
        
        .. note::
        
        The old selection will be completely overridden.
        
        :type states: List[int]
        :param states: A list of elements to select.
        :rtype: bool
        :return: Success of selecting the elements.
        
        
        """
        ...
    
    def GetAll(self, max: int) -> List[int]:
        """    
        Returns all selected elements in a list.
        
        :type max: int
        :param max: The maximum number of elements to place into the array.
        :rtype: List[int]
        :return: The list
        
        
        """
        ...
    
    def HostAlive(self) -> int:
        """    
        Returns if the host object is still alive.
        
        :rtype: int
        :return:
        
        * **2** if the instance has no host object.
        * **1** if the host object is alive if set.
        * **0** if the object is not alive.
        
        
        """
        ...
    
    def Write(self, hf: HyperFile) -> None:
        """    
        Saves the selection to a file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to write to.
        
        
        """
        ...
    
    def Read(self, hf: HyperFile) -> bool:
        """    
        Reads a selection from a file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to read from.
        :rtype: bool
        :return: True if successful, otherwise False.
        
        
        """
        ...
    
    def FindSegment(self, num: int) -> int:
        """    
        Returns which segment contains the element *num*.
        
        .. versionadded:: R19
        
        :type num: int
        :param num: The index of the element.
        :rtype: int
        :return: The found segment index. `-1` if no segment was found.
        
        
        """
        ...
    
    def GetLastElement(self) -> int:
        """    
        Returns the last element.
        
        :rtype: int
        :return: Last element.
        
        
        """
        ...
    

class BaseTime(object):
    def __init__(self, z: Optional[int] = ..., n: Optional[Union[bool, int]] = ...) -> None:
        """    
        | Initializes the internal time value from a real value in seconds.
        | This will multiply the seconds by 1000.0 and store it as a fraction with the denominator at 1000.0.
        
        :type z: int
        :param z: Optional time in seconds.
        :type n: Union[bool, int]
        :param n: If *n* is **False**, disable the automatic fraction-reduction and if int, set the denominator.
        :rtype: c4d.BaseTime
        :return: A new basetime.
        
        
        """
        ...
    
    def __cmp__(self, other: BaseTime) -> None:
        """    
        Compare two times with each other.
        
        :type other: c4d.BaseTime
        :param other: The time value to compare with.
        
        
        """
        ...
    
    def __eq__(self, other: BaseTime) -> bool:
        """    
        Check if two different BaseTime represents the same time.
        
        :type other: c4d.BaseTime
        :param other: The time value to compare with.
        :rtype: bool
        :return: **True** if the BaseTime are similar, otherwise **False**.
        
        
        """
        ...
    
    def __ne__(self, other: Any) -> bool:
        """    
        Check if two different BaseTime don't represents the same time.
        
        :rtype: bool
        :return: **True** if the BaseTime don't represent the same time, otherwise **False**.
        
        
        """
        ...
    
    def __ge__(self, other: BaseTime) -> bool:
        """    
        Check if the passed BaseTime is greater or equal than self.
        
        :type other: c4d.BaseTime
        :param other: The other BaseTime.
        :rtype: bool
        :return: **True** if other BaseTime is greater or equal than self
        
        
        """
        ...
    
    def __gt__(self, other: BaseTime) -> bool:
        """    
        Check if the passed BaseTime is greater than self.
        
        :type other: c4d.BaseTime
        :param other: The other BaseTime.
        :rtype: bool
        :return: **True** if other BaseTime is greater than self
        
        
        """
        ...
    
    def __le__(self, other: BaseTime) -> bool:
        """    
        Check if the passed BaseTime is lesser or equal than self.
        
        :type other: c4d.BaseTime
        :param other: The other BaseTime.
        :rtype: bool
        :return: **True** if other BaseTime is lesser or equal than self
        
        
        """
        ...
    
    def __lt__(self, other: BaseTime) -> bool:
        """    
        Check if the passed BaseTime is lesser than self.
        
        :type other: c4d.BaseTime
        :param other: The other BaseTime.
        :rtype: bool
        :return: **True** if other BaseTime is lesser than self
        
        
        """
        ...
    
    def __add__(self, other: BaseTime) -> BaseTime:
        """    
        Add two times and return the result.
        
        :type other: c4d.BaseTime
        :param other: The other value.
        :rtype: c4d.BaseTime
        :return: The result.
        
        
        """
        ...
    
    def __sub__(self, other: BaseTime) -> BaseTime:
        """    
        Subtract two times and return the result.
        
        :type other: c4d.BaseTime
        :param other: The other value.
        :rtype: c4d.BaseTime
        :return: The result.
        
        
        """
        ...
    
    def __mul__(self, other: BaseTime) -> BaseTime:
        """    
        Multiply two times and return the result.
        
        :type other: c4d.BaseTime
        :param other: The other value.
        :rtype: c4d.BaseTime
        :return: The result.
        
        
        """
        ...
    
    def __div__(self, other: BaseTime) -> BaseTime:
        """    
        Divide two times and return the result.
        
        :type other: c4d.BaseTime
        :param other: The other value.
        :rtype: c4d.BaseTime
        :return: The result.
        
        
        """
        ...
    
    def GetFrame(self, fps: int) -> int:
        """    
        Get the number of frames equivalent to this time for the given number of frames per second.
        
        :type fps: int
        :param fps: The number of frames for this time.
        :rtype: int
        :return: The frames per second to use to calculate the frame number for this time.
        
        
        """
        ...
    
    def Quantize(self, fps: float) -> None:
        """    
        Quantize the internal value so that it is a multiple of the specified framerate.
        
        :type fps: number
        :param fps: The number of frames per second to make this time a multiple of.
        
        
        """
        ...
    
    def SetNumerator(self, r: float) -> None:
        """    
        Set the numerator part of the internally stored time.
        
        :type r: number
        :param r: The numerator.
        
        
        """
        ...
    
    def GetNumerator(self) -> float:
        """    
        Get the numerator part of the internally stored time.
        
        :rtype: float
        :return: The numerator.
        
        
        """
        ...
    
    def SetDenominator(self, r: float) -> None:
        """    
        Get the denominator part of the internally stored time.
        
        :type r: number
        :param r: The denominator.
        
        
        """
        ...
    
    def GetDenominator(self) -> float:
        """    
        Get the denominator part of the internally stored time.
        
        :rtype: float
        :return: The denominator
        
        
        """
        ...
    
    def Get(self) -> float:
        """    
        Return the time in seconds.
        
        :rtype: float
        :return: Time in seconds.
        
        
        """
        ...
    
    def TimeDif(self, t2: BaseTime) -> int:
        """    
        Check which is the largest between the time and *t2*.
        
        :type t2: c4d.BaseTime
        :param t2: The time to compare with.
        :rtype: int
        :return: `-1` if the time is < *t2*, `0` if they are equal and `1` if the time is > *t2*.
        
        
        """
        ...
    

class CPolygon(object):
    def __init__(self, t_a: int, t_b: int, t_c: int, t_d: Optional[int] = ...) -> None:
        """    
        :type t_a: int
        :param t_a: Index of first point in the polygon.
        :type t_b: int
        :param t_b: Index of second point in the polygon.
        :type t_c: int
        :param t_c: Index of third point in the polygon.
        :type t_d: int
        :param t_d: Index of optional fourth point in the polygon.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        Returns a string representation of the polygon. Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around an instance of :class:`CPolygon <c4d.CPolygon>`. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_.)
        
        :rtype: str
        :return: The string representation of the polygon.
        
        
        """
        ...
    
    def IsTriangle(self) -> bool:
        """    
        Checks if the polygon is a triangle.
        
        .. versionadded:: R16.021
        
        :rtype: bool
        :return: **True** if the polygon is a triangle, otherwise **False**.
        
        
        """
        ...
    
    def Find(self, index: int) -> int:
        """    
        Checks if one of the polygon vertex indices is equal to *index* and returns the found polygon vertex number (`0`-`3`, equals :attr:`a` - :attr:`d`).
        
        .. versionadded:: R16.021
        
        :type index: int
        :param index: The vertex index to check.
        :rtype: int
        :return: The matching polygon vertex number (`0`-`3`, equals :attr:`a` - :attr:`d`). **NOTOK** is returned if there is no match.
        
        """
        ...
    
    def FindEdge(self, index1: int, index2: int) -> int:
        """    
        Checks if the vertex indices *index1* and *index2* form an edge in this polygon. If so the polygon edge number is returned (`0`-`3`).
        
        .. versionadded:: R16.021
        
        :type index1: int
        :param index1: The vertex index of the first edge point.
        :type index2: int
        :param index2: The vertex index of the second edge point.
        :rtype: int
        :return: The found polygon edge number (`0`-`3`). **NOTOK** is returned if there is no match.
        
        
        """
        ...
    
    def EdgePoints(self, edge: int) -> Tuple[int, int]:
        """    
        Retrieves the point indices for *edge*.
        
        .. versionadded:: R16.021
        
        :type edge: int
        :param edge: The edge index (`0`-`3`).
        :rtype: tuple(int, int)
        :return: The index of the first and second edge point.
        
        
        """
        ...
    

class CustomIconSettings(object):
    @staticmethod
    def FillCustomIconSettingsFromBaseList2D(settings: CustomIconSettings, data: BaseContainer, defaultIconId: int, bcFillDefault: bool) -> None:
        """    
        Fills the passed :class:`c4d.CustomIconSettings` `settings` with the data from a BaseList2D BaseContainer.
        
        .. note::
        
        This is mostly used in plugin development. See py-custom-icon example in github.
        
        :param settings: The Custom Icon Settings to fill.
        :type settings: c4d.CustomIconSettings
        :param data: The BaseContainer of a BaseList2D (retrieved with BaseList2D.GetData()).
        :type data: c4d.BaseContainer
        :param defaultIconId: The default IconId the CustomIconSettings should use (usually node.GetType()).
        :type defaultIconId: int
        :param bcFillDefault: True if default should be filled
        :type bcFillDefault: bool
        
        
        """
        ...
    
    def GetCustomIcon(self, cid: Dict[str, Any], settings: CustomIconSettings, drawBeforeColoring: bool) -> None:
        """    
        Fill the dictionary `cid` with the passed CustomIconSettings
        
        .. note::
        
        This is mostly used in plugin development. See py-custom-icon example in github.
        
        :param cid: A dictionary with the structure of :ref:`MSG_GETCUSTOMICON <MSG_GETCUSTOMICON_C4DATOM>`.
        :type cid: dict
        :param settings: The Custom Icon Settings to fill `cid` with.
        :type settings: c4d.CustomIconSettings
        :param drawBeforeColoring: True if the icon should be drawn before color change.
        :type drawBeforeColoring: bool
        
        
        """
        ...
    

class DescID(object):
    def __init__(self, id1: DescLevel, id2: Optional[DescLevel] = ..., id3: Optional[DescLevel] = ...) -> None:
        """    
        Create a DescID instance up to three levels
        
        .. code-block:: python
        
        dId = c4d.DescID()
        dId = c4d.DescID(dId) #copy constructor
        dId = c4d.DescID(10) #first level with given ID
        dId = c4d.DescID(DescLevel(10), DescLevel(20), DescLevel(30)) #set three levels
        
        :type id1: c4d.DescLevel
        :param id1: First level.
        :type id2: c4d.DescLevel
        :param id2: Second level.
        :type id3: c4d.DescLevel
        :param id3: Third level.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        Returns the DescID as string. Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around an instance of :class:`DescID <c4d.DescID>`. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_)
        
        .. code-block:: python
        
        dId = c4d.DescID(c4d.DescLevel(30))
        print dId                # output '(30, 0, 0)'
        
        :rtype: str
        :return: The DescID as string.
        
        
        """
        ...
    
    def __lshift__(self, other: int) -> DescID:
        """    
        Returns the result of popping *shift* levels from the **bottom** of the stack
        
        .. code-block:: python
        
        dId = c4d.DescID(c4d.DescLevel(30), c4d.DescLevel(40), c4d.DescLevel(50))
        dId<<2
        
        :type other: int
        :param other: Number of levels to pop.
        :raise IndexError: If *other* is out of range : *0<=other<*:meth:`GetDepth`.
        :rtype: c4d.DescID
        :return: Result.
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> DescLevel:
        """    
        Returns the level at position *key* in the stack
        
        .. code-block:: python
        
        dId = c4d.DescID(c4d.DescLevel(30), c4d.DescLevel(40), c4d.DescLevel(50))
        diD[2]
        
        :type key: int
        :param key: The position.
        :raise IndexError: If *other* is out of range : *0<=key<*:meth:`GetDepth`.
        :rtype: c4d.DescLevel
        :return: The level at the specified position.
        
        
        """
        ...
    
    def __eq__(self, other: Any) -> None:
        """    
        Checks if all levels are equal.
        
        
        """
        ...
    
    def __ne__(self, other: Any) -> None:
        """    
        The reverse of :meth:`__eq__ <DescID.__eq__>`.
        
        
        """
        ...
    
    def SetId(self, subid: DescLevel) -> None:
        """    
        Set the highest level to *subid*.
        
        :type subid: c4d.DescLevel
        :param subid: New toplevel.
        
        
        """
        ...
    
    def PushId(self, subid: DescLevel) -> None:
        """    
        Push a new level onto the stack.
        
        :type subid: c4d.DescLevel
        :param subid: Level to push.
        
        
        """
        ...
    
    def PopId(self) -> None:
        """    
        Pops the highest level from the stack.
        
        
        """
        ...
    
    def GetDepth(self) -> int:
        """    
        Return the depth.
        
        :rtype: int
        :return: The depth.
        
        
        """
        ...
    
    def Write(self, hf: HyperFile) -> None:
        """    
        Writes the description to a file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to write to.
        
        
        """
        ...
    
    def Read(self, hf: HyperFile) -> bool:
        """    
        Reads the description from a file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to read from.
        :rtype: bool
        :return: True if successful, otherwise False.
        
        
        """
        ...
    
    def GetHashCode(self) -> int:
        """    
        Gets a hash code for the description ID.
        
        .. versionadded:: R17.048
        
        :rtype: int
        :return: The hash code.
        
        
        """
        ...
    
    def IsPartOf(self, cmp: Union[int, List[Any], DescID]) -> Tuple[bool, int]:
        """    
        Checks if the description ID is part of *cmp* and returns the length of the match.
        
        .. versionadded:: R18.020
        
        :type cmp: Union[int, list, c4d.DescID]
        :param cmp: The super description ID.
        
        .. versionchanged:: R18.057
        
        Can be a int, list or :class:`DescID <c4d.DescID>`
        
        :rtype: Tuple[bool, int]
        :return: A tuple with the following information:
        
        |
        | bool: **True** if the description ID matches a lowest part of *cmp*, otherwise **False**.
        | int: The length of the match.
        
        
        """
        ...
    

class DescLevel(object):
    def __init__(self, t_id: int, t_datatype: Optional[int] = ..., t_creator: Optional[int] = ...) -> None:
        """    
        Constructor, specifying the values.
        
        :type t_id: int
        :param t_id: Initial value for *id*.
        :type t_datatype: int
        :param t_datatype: Initial value for *dtype*.
        :type t_creator: int
        :param t_creator: Initial value for *creator*.
        
        
        """
        ...
    
    def __eq__(self, other: Any) -> None:
        """    
        Checks if all specified values are equal to the values in *other*.
        
        
        """
        ...
    
    def __ne__(self, other: Any) -> None:
        """    
        The reverse of :meth:`__eq__`.
        
        
        """
        ...
    

class Description(object):
    def __iter__(self, bc: BaseContainer, id: DescID, groupid: DescID) -> None:
        """    
        Iterate over the parameters of an object's description.
        
        :type bc: c4d.BaseContainer
        :param bc: The container that holds the information for the current description parameter.
        :type id: c4d.DescID
        :param id: The ID of the current description parameter.
        :type groupid: c4d.DescID
        :param groupid: The group ID of the current description parameter.
        
        Here is how to print the name of all the parameters of an object
        
        .. code-block:: python
        
        import c4d
        
        def main():
        if op is None:
        return
        
        description = op.GetDescription(c4d.DESCFLAGS_DESC_NONE)    # Get the description of the active object
        for bc, paramid, groupid in description:                    # Iterate over the parameters of the description
        print bc[c4d.DESC_NAME]                                 # Print the current parameter name
        
        if __name__=='__main__':
        main()
        
        
        """
        ...
    
    def LoadDescription(self, id: Union[int, str]) -> bool:
        """    
        Loads a description by name or ID.
        
        .. versionadded:: R18.011
        
        .. warning::
        
        Existing description parameters are lost.
        
        :type id: Union[int, str]
        :param id: The description name (e.g. "Obase") or ID (e.g. *c4d.Obase*).
        :rtype: bool
        :return: **True** if the description was loaded, otherwise **False**.
        
        
        """
        ...
    
    def GetParameter(self, id: DescID, ar: Any) -> BaseContainer:
        """    
        Retrieves the information container for a parameter.
        
        .. versionadded:: R18.011
        
        :type id: c4d.DescID
        :param id: The description ID.
        :type ar: list of :class:`c4d.C4DAtom`
        :param ar:
        
        .. versionadded:: R18.039
        
        Optional array for dynamic descriptions, e.g. sub-descriptions of a gradient or dynamic XPresso node, that need an array of elements the parameter is assigned to.
        
        :rtype: c4d.BaseContainer
        :return: The information container.
        
        .. versionchanged:: R18.057
        
        Returns only one information container.
        
        
        """
        ...
    
    def GetParameterI(self, id: DescID, ar: Optional[Any] = ...) -> None:
        """    
        Retrieves the information container instance for a parameter.
        
        .. versionadded:: R18.011
        
        :type id: c4d.DescID
        :param id: The description ID.
        :type ar: list of :class:`c4d.C4DAtom`
        :param ar: Optional array for dynamic descriptions, e.g. sub-descriptions of a gradient or dynamic XPresso node, that need an array of elements the parameter is assigned to.
        :rtype: :class:`c4d.BaseContainer`
        :return: The information container instance or **None**.
        
        
        """
        ...
    
    def SetParameter(self, id: DescID, param: BaseContainer, groupid: DescID) -> bool:
        """    
        Inserts a description parameter into the collection.
        
        .. versionadded:: R18.011
        
        :type id: c4d.DescID
        :param id: The description ID.
        :type param: c4d.BaseContainer
        :param param: The settings for the new parameter.
        :type groupid: c4d.DescID
        :param groupid: The ID of the parameter's group, or :data:`c4d.DESCID_ROOT`.
        :rtype: bool
        :return: **True** if the parameter was inserted, otherwise **False**.
        
        
        """
        ...
    
    def CreatePopupMenu(self) -> BaseContainer:
        """    
        Builds a popup menu for choosing a parameter in the description.
        
        .. versionadded:: R18.011
        
        :rtype: c4d.BaseContainer
        :return: The menu container.
        
        
        """
        ...
    
    def CheckDescID(self, searchid: DescID, ops: Any) -> DescID:
        """    
        Checks if a description ID *searchid* exists for the given objects *ops*.
        
        .. note::
        
        usually only one single object is passed as otherwise the smallest common nominator is returned.
        
        .. versionadded:: R18.011
        
        :type searchid: c4d.DescID
        :param searchid: The partial ID.
        :type ops: list of :class:`C4DAtom <c4d.C4DAtom>`
        :param ops: A list of atom objects for dynamic descriptions. Usually **None**.
        :rtype: c4d.DescID
        :return: The complete ID.
        
        
        """
        ...
    
    def GetSubDescriptionWithData(self, did: DescID, op: Any, bc: BaseContainer, singledescid: DescID) -> bool:
        """    
        Retrieves dynamic sub-description data (e.g. the gradient data type).
        
        .. versionadded:: R18.011
        
        :type did: c4d.DescID
        :param did: The description ID.
        :type op: list of :class:`C4DAtom <c4d.C4DAtom>`
        :param op: A list of atom objects.
        :type bc: c4d.BaseContainer
        :param bc: The existing container for the data type. Can be just :class:`c4d.BaseContainer() <c4d.BaseContainer>`.
        :type singledescid: c4d.DescID
        :param singledescid: Should be **None**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetSingleDescID(self) -> DescID:
        """    
        Retrieves the single description ID.
        
        .. versionadded:: R18.011
        
        :rtype: c4d.DescID
        :return: The single description ID.
        
        
        """
        ...
    

class HandleInfo(object):
    def __init__(self) -> None:
        """    
        Constructor.
        
        
        """
        ...
    
    def CalculateNewPosition(self, bd: BaseDraw, mg: Matrix, mouse_pos: Vector) -> Vector:
        """    
        Calculates a handle position for a given mouse position.
        
        :type bd: c4d.BaseDraw
        :param bd: The active viewport.
        :type mg: c4d.Matrix
        :param mg: The global matrix of the handle's parent object.
        :type mouse_pos: c4d.Vector
        :param mouse_pos: The mouse coordinates for which to calculate the handle position.
        :rtype: c4d.Vector
        :return: The new handle position.
        
        
        """
        ...
    

class IconData(object):
    def __init__(self) -> None:
        """    
        Initializes a new :class:`Vector <c4d.IconData>`.
        
        :rtype: c4d.IconData
        :return: A new icon data.
        
        
        """
        ...
    
    def GetClonePart(self) -> None:
        """    
        Gets a copy of the bitmap's part for the icon data.
        
        :rtype: :class:`c4d.bitmaps.BaseBitmap`
        :return: The copy of the icon part.
        
        
        """
        ...
    
    def GetGuiScalePart(self) -> None:
        """    
        Gets a copy of the scaled bitmap's part for the icon data with the size :meth:`IconData.GetGuiW`/:meth:`IconData.GetGuiH`.
        
        :rtype: :class:`c4d.bitmaps.BaseBitmap`
        :return: The copy of the scaled icon part.
        
        
        """
        ...
    
    def GetGuiW(self) -> None:
        """    
        Gets the GUI scaled width of the icon data.
        
        :type value: int
        :param value: The GUI scaled width.
        
        
        """
        ...
    
    def GetGuiH(self) -> int:
        """    
        Gets the GUI scaled height of the icon data.
        
        :rtype: int
        :return: The GUI scaled height.
        
        
        """
        ...
    

class LayerShaderLayer(object):
    def GetNext(self) -> LayerShaderLayer:
        """    
        Gets the next layer.
        
        .. note::
        
        Use this method to navigate trough the layers of a layer shader.
        
        :rtype: c4d.LayerShaderLayer
        :return: The next layer.
        
        
        """
        ...
    
    def GetType(self) -> int:
        """    
        Gets the layer type.
        
        :rtype: int
        :return: The layer type:
        
        .. include:: /consts/LayerType.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetName(self, doc: BaseDocument) -> str:
        """    
        Gets the name of the layer.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: str
        :return: The layer name.
        
        
        """
        ...
    
    def GetPreview(self) -> BaseBitmap:
        """    
        Retrieves the preview bitmap.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The preview bitmap.
        
        
        """
        ...
    
    def GetParameter(self, id: int) -> Any:
        """    
        Retrieves layer parameters.
        
        .. note::
        
        See Layer Shader Library documentation in the C++ SDK for the information on the parameter IDs and types.
        
        :type id: int
        :param id: The ID of the parameter to get.
        :rtype: Any
        :return: The parameter value.
        
        
        """
        ...
    
    def SetParameter(self, id: int, data: Any) -> bool:
        """    
        Sets layer parameters.
        
        .. note::
        
        See Layer Shader Library documentation in the C++ SDK for the information on the parameter IDs and types.
        
        :type id: int
        :param id: The ID of the parameter to set.
        :type data: any
        :param data: The new parameter value.
        :rtype: bool
        :return: **True** if the parameter could be set, otherwise **False**.
        
        
        """
        ...
    

class Quaternion(object):
    def __init__(self) -> None:
        """    
        Returns a new :class:`Quaternion <c4d.Quaternion>` instance.
        
        
        """
        ...
    
    def GetMatrix(self) -> Matrix:
        """    
        Derives a rotation matrix from the quaternion.
        
        :rtype: c4d.Matrix
        :return: The rotation matrix.
        
        
        """
        ...
    
    def SetMatrix(self, m: Matrix) -> None:
        """    
        Derives quaternion values from a rotation matrix.
        
        :type m: c4d.Matrix
        :param m: The rotation matrix to set.
        
        
        """
        ...
    
    def SetMatrixNorm(self, m: Matrix) -> None:
        """    
        Derives quaternion values from a normalized rotation matrix.
        
        :type m: c4d.Matrix
        :param m: The normalized rotation matrix to set.
        
        
        """
        ...
    
    def SetHPB(self, hpb: Vector) -> None:
        """    
        Derives quaternion values from a HPB rotation.
        
        :type hpb: c4d.Vector
        :param hpb: The HPB rotation.
        
        
        """
        ...
    
    def SetAxis(self, ax: Vector, ww: float) -> None:
        """    
        Sets the quaternion values directly.
        
        :type ax: c4d.Vector
        :param ax: The direction vector.
        :type ww: float
        :param ww: The rotation angle.
        
        
        """
        ...
    

class ReflectionLayer(object):
    def GetLayerID(self) -> int:
        """    
        Retrieves the layer ID.
        
        .. versionadded:: R18.020
        
        :rtype: int
        :return: The layer ID. Must be a value greater or equal than `3`, otherwise it failed.
        
        
        """
        ...
    
    def GetDataID(self) -> int:
        """    
        Retrieves the layer base data ID to get/set its data.
        
        :rtype: int
        :return: The layer base data ID.
        
        
        """
        ...
    
    def GetName(self) -> str:
        """    
        Retrieves the layer name.
        
        .. versionadded:: R18.020
        
        :rtype: str
        :return: The layer name.
        
        
        """
        ...
    
    def SetName(self, name: str) -> None:
        """    
        Sets the layer name.
        
        .. versionadded:: R18.020
        
        :type name: str
        :param name:
        
        | The layer name to set.
        | If not valid (e.g. empty or all chars are whitespaces) a default layer name will be used.
        
        
        """
        ...
    
    def GetFlags(self) -> int:
        """    
        Retrieves the flags for the layer.
        
        .. versionadded:: R18.020
        
        :rtype: int
        :return: The layer flags:
        
        .. include:: /consts/REFLECTION_FLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetFlags(self, flags: int) -> None:
        """    
        Sets the flags for the layer.
        
        .. versionadded:: R18.020
        
        :type flags: int
        :param flags: The layer flags to set:
        
        .. include:: /consts/REFLECTION_FLAG.rst
        :start-line: 3
        
        
        """
        ...
    

class Vector(object):
    x: float
    y: float
    z: float

    def __init__(self, x: Optional[Union[int, float, Vector]] = ..., y: Optional[Union[int, float]] = ..., z: Optional[Union[int, float]] = ...) -> None:
        """    
        | Initializes a new :class:`Vector <c4d.Vector>`.
        | All arguments are optional so it is possible to create a new vector without any arguments. All components are simply `0`.
        | Otherwise *x* can be a :class:`Vector <c4d.Vector>` so all components of the passed vector will be copied to the new vector.
        | If only a number is passed, all components will be set to this.
        
        .. code-block:: python
        
        c4d.Vector()
        # => Vector(0,0,0)
        
        c4d.Vector(100)
        # => Vector(100,100,100)
        
        v = c4d.Vector(100,100,100)
        c4d.Vector(v)
        # => Vector(100,100,100)
        
        c4d.Vector(1,2,3)
        # => Vector(1,2,3)
        
        :type x: Union[int, float, c4d.Vector]
        :param x: If *x* is a number and is the only passed argument, set this to all components. If *x* is a vector, clone it. Otherwise set the X component.
        :type y: number
        :param y: Set the Y component.
        :type z: number
        :param z: Set the Z component.
        :rtype: c4d.Vector
        :return: A new vector.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        | Returns a string representation of the vector.
        | Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around a vector object. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_)
        
        .. code-block:: python
        
        vec = Vector(30.0, 40.0, 2)
        print vec
        # => Vector(30.0, 40.0, 2.0)
        
        :rtype: str
        :return: The Vector as string.
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> float:
        """    
        Retrieves X, Y and Z components by index
        
        .. versionadded:: R14.014
        
        .. code-block:: python
        
        v = c4d.Vector(1,2,3)
        x = v[0]
        y = v[1]
        z = v[2]
        print x, y, z
        # => 1.0 2.0 3.0
        
        :type key: int
        :param key: The component index.
        :raise IndexError: If the index *key* is out of range : *0<=key<2*.
        :rtype: float
        :return: The vector component.
        
        
        """
        ...
    
    def __setitem__(self, key: int, value: float) -> None:
        """    
        Assigns X, Y and Z components by index
        
        .. versionadded:: R14.014
        
        .. code-block:: python
        
        v = c4d.Vector(1,2,3)
        v[0] = 0
        print v
        # => Vector(0, 2, 3)
        
        .. note:: The :class:`Vector <c4d.Vector>` objects does not support item deletion. For instance by calling `del(v[0])`.
        
        :type key: int
        :param key: The component index.
        :raise IndexError: If the index *key* is out of range : *0<=key<2*.
        :type value: float
        :param value: The new vector component.
        
        
        """
        ...
    
    def __add__(self, other: Union[Vector, int, float]) -> Vector:
        """    
        Adds a scalar or vector to the vector
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)+1
        # => Vector(2,3,4)
        
        c4d.Vector(1,2,3)+c4d.Vector(2,3,4)
        # => Vector(3,5,7)
        
        :type other: Union[c4d.Vector, int, float]
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def __sub__(self, other: Union[Vector, int, float]) -> Vector:
        """    
        Subtracts a scalar or vector from the vector
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)-1
        # => Vector(0,1,2)
        
        c4d.Vector(1,2,3)-c4d.Vector(2,3,4)
        # => Vector(-1,-1,-1)
        
        :type other: Union[c4d.Vector, int, float]
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def __mul__(self, other: Union[Matrix, Vector, float]) -> Union[Vector, float]:
        """    
        | If *other* is a vector, calculates the dot product of the vectors.
        | If *other* is a float, it multiplies each vector component by the scalar.
        | If *other* is a matrix, the vector is transformed by it.
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)*c4d.Vector(2,3,4)
        # => 20
        
        c4d.Vector(1,2,3)*5
        # => Vector(5,10,15)
        
        c4d.Vector(1,2,3)*c4d.Matrix(v1=c4d.Vector(2,0,0))
        # => Vector(2,2,3)
        
        :type other: c4d.Matrix
        :param other: The other argument.
        :rtype: c4d.Vector or float
        :return:  A float if *other* is of type :class:`Vector <c4d.Vector>`. A vector, if *other* is of type float or :class:`Matrix <c4d.Matrix>`.
        
        
        """
        ...
    
    def __div__(self, other: float) -> Vector:
        """    
        Divides each vector component by the scalar
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)/5
        # => Vector(0.2, 0.4, 0.6)
        
        :type other: number
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def __mod__(self, other: Vector) -> Vector:
        """    
        Calculates the cross product of vectors
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)%c4d.Vector(2,3,4)
        # => Vector(-1, 2, -1)
        
        :type other: c4d.Vector
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def __xor__(self, other: Matrix) -> Vector:
        """    
        | Multiplies vectors component-wise if *other* is a vector.
        | If *other* is a matrix then the vector is transformed by it.
        
        .. code-block:: python
        
        c4d.Vector(1,2,3)^c4d.Vector(2,3,4)
        # => Vector(2,6,12)
        
        c4d.Vector(1,2,3)^c4d.Matrix(v1=c4d.Vector(2,0,0))
        # => Vector(2,2,3)
        
        :type other: c4d.Matrix
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def __abs__(self) -> Vector:
        """    
        Returns a vector with the absolute (positive) value of each component
        
        .. code-block:: python
        
        abs(c4d.Vector(-1, -2, -3))
        # => Vector(1,2,3)
        
        :rtype: c4d.Vector
        :return: The absolute vector.
        
        
        """
        ...
    
    def __neg__(self) -> Vector:
        """    
        Returns the negative of the vector
        
        .. code-block:: python
        
        -c4d.Vector(1,2,3)
        # => Vector(-1,-2,-3)
        
        :rtype: c4d.Vector
        :return: The negative vector.
        
        
        """
        ...
    
    def __invert__(self) -> Vector:
        """    
        Returns the normalized vector
        
        .. code-block:: python
        
        ~c4d.Vector(1,2,3)
        # => Vector(0.267,0.535,0.802)
        
        :rtype: c4d.Vector
        :return: The normalized vector.
        
        
        """
        ...
    
    def __eq__(self, other: Vector) -> bool:
        """    
        Checks if two vectors are equal.
        
        :type other: c4d.Vector
        :param other: The other vector.
        :rtype: bool
        :return: **True** if both vectors are equal.
        
        
        """
        ...
    
    def __ne__(self, other: Vector) -> bool:
        """    
        Check if two vectors are not equal.
        
        :type other: c4d.Vector
        :param other: The other vector.
        :rtype: bool
        :return: **True** if both vectors are not equal.
        
        
        """
        ...
    
    def __ge__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __gt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __le__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __lt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def Dot(self, v2: Vector) -> float:
        """    
        Calculates the dot product of the vector and vector **v2**.
        
        :type v2: c4d.Vector
        :param v2: The second vector.
        :rtype: float
        :return: The dot product.
        
        
        """
        ...
    
    def Cross(self, v2: Vector) -> Vector:
        """    
        Calculates the cross product of the vector and vector **v2**.
        
        :type v2: c4d.Vector
        :param v2: The other vector.
        :rtype: c4d.Vector
        :return: The result.
        
        
        """
        ...
    
    def GetLength(self) -> float:
        """    
        Calculates the length of the vector.
        
        :rtype: float
        :return: The length.
        
        
        """
        ...
    
    def GetDistance(self, v1: Vector, v2: Vector) -> float:
        """    
        Retrieve the distance between two vectors.
        
        :param v1: The first vector.
        :type v1: c4d.Vector
        :param v2: The second vector.
        :type v2: c4d.Vector
        :return: the distance from v1 to v2.
        :rtype: float
        
        
        """
        ...
    
    def GetLengthSquared(self) -> float:
        """    
        Calculates the squared length of the vector.
        
        :rtype: float
        :return: The squared length.
        
        
        """
        ...
    
    def GetNormalized(self) -> Vector:
        """    
        Calculates the normalized vector, so that :meth:`GetLength` returns `1.0`.
        
        :rtype: c4d.Vector
        :return: The normalized vector.
        
        
        """
        ...
    
    def Normalize(self) -> None:
        """    
        Normalizes the vector, so that :meth:`GetLength` returns `1.0`.
        
        
        """
        ...
    

class Vector4d(object):
    def __init__(self, x: Union[int, float, Vector], y: float, z: float, w: float) -> None:
        """    
        | Initializes a new :class:`Vector4d <c4d.Vector4d>`.
        | All arguments are optional so it is possible to create a new vector without any arguments. X/Y/Z components are simply `0` and W `1`.
        | If only 1 argument is passed, it can be either a number or :class:`c4d.Vector`:
        - number: All components are set to this number.
        - :class:`c4d.Vector`: X/Y/Z components of the passed vector are copied to the new vector and W is set `1`.
        | If 2 arguments are passed:
        - The first argument has to be a :class:`c4d.Vector` and the second one a number. X/Y/Z components of the passed vector are copied to the new vector and W is set the number argument.
        | If 4 arguments are passed:
        - *x*, *y*, *z*, *w* have to be floats and are respectively assigned to X/Y/Z/W components.
        |
        
        .. code-block:: python
        
        c4d.Vector4d()
        # => Vector4d(0,0,0,1)
        
        c4d.Vector4d(5)
        # => Vector4d(5, 5, 5, 5)
        
        v = c4d.Vector4d(5, 5, 5)
        c4d.Vector4d(v)
        # => Vector4d(5, 5, 5, 1)
        c4d.Vector4d(v, 2)
        # => Vector4d(5, 5, 5, 2)
        
        c4d.Vector4d(1, 2, 3, 4)
        # => Vector4d(1, 2, 3, 4)
        
        :type x: Union[int, float, c4d.Vector]
        :param x: If *x* is a number and is the only passed argument, set this to X/Y/Z components. If *x* is a :class:`c4d.Vector`, its X/Y/Z components are copied to the new vector. Otherwise set the X component.
        :type y: number
        :param y: The Y component. If 2 arguments are passed, set to W component.
        :type z: number
        :param z: The Z component.
        :type w: number
        :param w: The W component.
        :rtype: :class:`c4d.Vector4d`
        :return: A new :class:`c4d.Vector4d`.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        | Returns a string representation of the :class:`c4d.Vector4d`.
        | Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around a :class:`c4d.Vector4d` object. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_)
        
        .. code-block:: python
        
        v = c4d.Vector4d(3.0, 4.0, 2.0, 5.0)
        print v
        # => Vector4d(3, 4, 2, 5)
        
        :rtype: str
        :return: The :class:`c4d.Vector4d` as string.
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> float:
        """    
        Retrieves X/Y/Z/W components by index
        
        .. code-block:: python
        
        v = c4d.Vector4d(1, 2, 3, 4)
        x = v[0]
        y = v[1]
        z = v[2]
        w = v[3]
        print x, y, z, w
        # => 1.0 2.0 3.0 4.0
        
        :type key: int
        :param key: The component index.
        :raise IndexError: If the index *key* is out of range : *0<=key<3*.
        :rtype: float
        :return: The :class:`c4d.Vector4d` component.
        
        
        """
        ...
    
    def __setitem__(self, key: int, value: float) -> None:
        """    
        Assigns X/Y/Z/W components by index
        
        .. code-block:: python
        
        v = c4d.Vector4d(1, 2, 3, 4)
        v[3] = 0
        print v
        # => Vector4d(1, 2, 3, 0)
        
        .. note::
        
        | The :class:`c4d.Vector4d` objects does not support item deletion.
        | For instance by calling `del(v[0])`.
        
        :type key: int
        :param key: The component index.
        :raise IndexError: If the index *key* is out of range : *0<=key<3*.
        :type value: float
        :param value: The new value for the :class:`c4d.Vector4d` component.
        
        
        """
        ...
    
    def __add__(self, other: Vector4d) -> None:
        """    
        Adds another :class:`c4d.Vector4d` to the :class:`c4d.Vector4d`
        
        .. code-block:: python
        
        c4d.Vector4d(1,2,3,4)+c4d.Vector4d(2,3,4,5)
        # => Vector4d(3, 5, 7, 9)
        
        :type other: c4d.Vector4d
        :param other: The other vector.
        :rtype: :class:`c4d.Vector4d`
        :return: The result vector.
        
        
        """
        ...
    
    def __sub__(self, other: Vector4d) -> None:
        """    
        Subtracts another :class:`c4d.Vector4d` from the :class:`c4d.Vector4d`
        
        .. code-block:: python
        
        c4d.Vector4d(1, 2, 3, 4)-c4d.Vector4d(2, 3, 4, 5)
        # => Vector4d(-1, -1, -1, -1)
        
        :type other: c4d.Vector4d
        :param other: The other vector.
        :rtype: :class:`c4d.Vector4d`
        :return: The result vector.
        
        
        """
        ...
    
    def __mul__(self, other: Union[int, float, Vector]) -> None:
        """    
        | If *other* is a :class:`c4d.Vector4d`, multiplies each vector component in the left-hand vector by its counterpart in the right-hand vector and returns the vector result.
        | If *other* is a number, multiplies each vector components by the scalar and returns the vector result.
        
        .. code-block:: python
        
        c4d.Vector4d(1, 2, 3, 4)*c4d.Vector4d(2, 3, 4, 5)
        # => Vector4d(2, 6, 12, 20)
        
        c4d.Vector4d(1, 2, 3, 4)*5
        # => Vector4d(5, 10, 15, 20)
        
        :type other: Union[int, float, c4d.Vector]
        :param other: The other argument.
        :rtype: :class:`c4d.Vector4d`
        :return:  The result vector.
        
        
        """
        ...
    
    def __eq__(self, other: Vector4d) -> bool:
        """    
        Checks if 2 vectors are equal.
        
        :type other: c4d.Vector4d
        :param other: The other vector.
        :rtype: bool
        :return: **True** if both vectors are equal, otherwise **False**.
        
        
        """
        ...
    
    def __ne__(self, other: Vector4d) -> bool:
        """    
        Check if 2 vectors are not equal.
        
        :type other: c4d.Vector4d
        :param other: The other vector.
        :rtype: bool
        :return: **True** if both vectors are not equal, otherwise **False**.
        
        
        """
        ...
    
    def __ge__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __gt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __le__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __lt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def SetZero(self) -> None:
        """    
        Sets all vector components to zero.
        
        
        """
        ...
    
    def Dot(self, b: Vector4d) -> float:
        """    
        Calculates the dot product of the :class:`c4d.Vector4d` and :class:`c4d.Vector4d` *b*.
        
        :type b: c4d.Vector4d
        :param b: The other vector.
        :rtype: float
        :return: The dot product.
        
        
        """
        ...
    
    def MakeVector3(self) -> None:
        """    
        Scales the vector so that :attr:`Vector4d.w` equals `1`.
        
        
        """
        ...
    
    def NormalizeW(self) -> None:
        """    
        Scales the vector so that :attr:`Vector4d.w` equals `1`.
        
        .. versionadded:: R20
        
        
        """
        ...
    
    def GetVector3(self) -> None:
        """    
        Retrieves a :class:`c4d.Vector` from the :class:`c4d.Vector4d`.
        
        :rtype: :class:`c4d.Vector`
        :return: The converted :class:`c4d.Vector`.
        
        
        """
        ...
    

class Matrix(object):
    off: Vector
    v1: Vector
    v2: Vector
    v3: Vector

    def __init__(self, off: Vector, v1: Vector, v2: Vector, v3: Vector) -> None:
        """    
        | Initializes a new :class:`Matrix <c4d.Matrix>`.
        | All arguments are optional so it is possible to create a new matrix without any arguments. All components are simply set to:
        
        - off = Vector(0)
        - v1 = Vector(1,0,0)
        - v2 = Vector(0,1,0)
        - v3 = Vector(0,0,1)
        
        .. code-block:: python
        
        mat = c4d.Matrix()
        # => Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0))
        
        mat = c4d.Matrix()
        mat.off = c4d.Vector(100,0,0)
        
        v1 = c4d.Vector(3)
        v2 = c4d.Vector(12,4,9.3)
        v3 = c4d.Vector(9,80,3)
        off = c4d.Vector(v1+v2)
        mat = c4d.Matrix(off,v1,v2,v3)
        
        :type off: c4d.Vector
        :param off: The translation vector.
        :type v1: c4d.Vector
        :param v1: The X axis of a left-handed coordinate system.
        :type v2: c4d.Vector
        :param v2: The Y axis of a left-handed coordinate system.
        :type v3: c4d.Vector
        :param v3: The Z axis of a left-handed coordinate system.
        :rtype: c4d.Matrix
        :return: A new matrix.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        Returns the Matrix as string. Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around an instance of :class:`Matrix <c4d.Matrix>`. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_)
        
        .. code-block:: python
        
        v1 = c4d.Vector(3)
        v2 = c4d.Vector(12,4,9.3)
        v3 = c4d.Vector(9,80,3)
        off = c4d.Vector(v1+v2)
        mat = c4d.Matrix(off,v1,v2,v3)
        print mat
        # => Matrix(v1: (3, 3, 3); v2: (12, 4, 9.3); v3: (12, 4, 9.3); off: (15, 7, 12.3))
        
        :rtype: str
        :return: The Vector as string.
        
        
        """
        ...
    
    def __add__(self, other: Matrix) -> Matrix:
        """    
        Adds two matrices.
        
        :type other: c4d.Matrix
        :param other: The other matrix.
        :rtype: c4d.Matrix
        :return: The result matrix.
        
        
        """
        ...
    
    def __sub__(self, other: Matrix) -> Matrix:
        """    
        Subtracts two matrices.
        
        :type other: c4d.Matrix
        :param other: The other matrix.
        :rtype: c4d.Matrix
        :return: The result matrix.
        
        
        """
        ...
    
    def __mul__(self, other: Union[Matrix, Vector, int, float]) -> Union[Matrix, Vector]:
        """    
        | Multiplies a matrix or vector by the matrix. Can also scale each vector of the matrix by a scalar.
        |
        | If both objects are of type :class:`Matrix <c4d.Matrix>`,  multiplies the left hand matrix by the right hand matrix.
        | If the left object is of type :class:`Matrix <c4d.Matrix>` and the right one of type :class:`Vector <c4d.Vector>`, multiplies the vector by the matrix including any translation in the matrix.
        | If the left object is of type :class:`Vector <c4d.Vector>` and the right one of type :class:`Matrix <c4d.Matrix>`, multiplies the vector by the matrix including any translation in the matrix.
        | If the right object is a number, multiplies each vector of the matrix by it.
        
        :type other: Union[c4d.Vector, int, float]
        :param other: The other argument.
        :rtype: c4d.Vector
        :return: The result matrix or vector.
        
        
        """
        ...
    
    def __div__(self, other: float) -> Matrix:
        """    
        Divides each element in the matrix by a scalar.
        
        :type other: float
        :param other: The scalar.
        :rtype: c4d.Matrix
        :return: The result matrix.
        
        
        """
        ...
    
    def __invert__(self) -> Matrix:
        """    
        Inverts the matrix.
        
        :rtype: c4d.Matrix
        :return: The inverted matrix.
        
        
        """
        ...
    
    def __eq__(self, other: Matrix) -> bool:
        """    
        Checks if two matrices are equal.
        
        :type other: c4d.Matrix
        :param other: The other matrix.
        :rtype: bool
        :return: **True** if matrices are equal.
        
        
        """
        ...
    
    def __ne__(self, other: Matrix) -> bool:
        """    
        Checks if two matrices are not equal.
        
        :type other: c4d.Matrix
        :param other: The other matrix.
        :rtype: bool
        :return: **True** if matrices are not equal.
        
        
        """
        ...
    
    def __ge__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __gt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __le__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def __lt__(self, other: Any) -> None:
        """    
        raise NotImplemented.
        
        
        """
        ...
    
    def Normalize(self) -> None:
        """    
        Normalizes the matrix.
        
        
        """
        ...
    
    def GetNormalized(self) -> Matrix:
        """    
        Calculates the normalized matrix.
        
        :rtype: c4d.Matrix
        :return: The normalized matrix.
        
        
        """
        ...
    
    def Mul(self, v: Vector) -> Vector:
        """    
        Multiply the vector by the matrix, this includes any translation in the matrix.
        
        :type v: c4d.Vector
        :param v: The vector to multiply.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def MulV(self, v: Vector) -> Vector:
        """    
        Multiply the vector by the matrix, this does not include any translation.
        
        :type v: c4d.Vector
        :param v: The vector to multiply.
        :rtype: c4d.Vector
        :return: The result vector.
        
        
        """
        ...
    
    def GetTensorMatrix(self) -> Matrix:
        """    
        Returns the matrix' tensor.
        
        :rtype: c4d.Matrix
        :return: The tensor matrix.
        
        
        """
        ...
    
    def Scale(self, v: Union[Vector, float]) -> None:
        """    
        Performs uniform matrix scaling (float) or non-uniform matrix scaling (vector).
        
        :type v: Union[c4d.Vector, float]
        :param v: The scaling scalar.
        
        
        """
        ...
    
    def GetScale(self) -> Vector:
        """    
        Returns the scale stored by the matrix.
        
        :return: The scale.
        :rtype: c4d.Vector
        
        
        """
        ...
    

class BaseContainer(object):
    def __init__(self, n: Optional[Union[BaseContainer, int]] = ...) -> None:
        """    
        Initializes a new container.
        
        :type n: [c4d.BaseContainer, int, None]
        :param n: Use int if you just want to set the ID of the container. Pass a container if you want to clone it, or **None** to use a standard empty container.
        :rtype: c4d.BaseContainer
        :return: The new container.
        
        
        """
        ...
    
    def __iter__(self) -> None:
        """    
        The BaseContainer is iterable so just use it like in the following example
        
        .. code-block:: python
        
        def iter_container(bc):
        for index, value in bc:
        print "Index: %i, Value: %s" % (index, str(value))
        
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> Any:
        """    
        Returns a value with the specified ID.
        
        :type key: int
        :param key: Index of the value.
        :rtype: Any
        :return: Any value.
        
        
        """
        ...
    
    def __setitem__(self, key: int, value: Any) -> None:
        """    
        | Automatically redirect the value to the corresponding Set* method.
        | Its recommended to use the original Set* method to avoid type problems.
        
        .. warning::
        
        | This method can replace types.
        | Please check the types before when a special key is associated with a special type.
        
        To delete a key, call *del(bc[i])* or :meth:`RemoveData`.
        
        :type key: int
        :param key: Index of the value.
        :type value: any
        :param value: It depends on the type which Set* method is internally called.
        
        
        """
        ...
    
    def __ne__(self, other: BaseContainer) -> None:
        """    
        Check if the compared containers don't have the same ID, don't have the same values, and all values are not equal.
        
        :type other: c4d.BaseContainer
        :param other: Returns **True** if the compared containers are equal.
        
        
        """
        ...
    
    def __eq__(self, other: BaseContainer) -> None:
        """    
        Check if the compared containers have the same ID, have the same values, and all values are equal.
        
        :type other: c4d.BaseContainer
        :param other: Returns **True** if the compared containers are equal.
        
        
        """
        ...
    
    def __len__(self) -> int:
        """    
        Calculates the number of data elements inside the container.
        
        :rtype: int
        :return: The number of data elements.
        
        
        """
        ...
    
    def GetClone(self, flags: int, trans: AliasTrans) -> BaseContainer:
        """    
        Returns a copy of the container including all values.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/COPYFLAGS_BaseContainer.rst
        :start-line: 3
        
        :type trans: c4d.AliasTrans
        :param trans:
        
        .. versionadded:: R17.032
        
        An optional alias translator for the operation.
        
        :rtype: c4d.BaseContainer
        :return: The cloned container.
        
        
        """
        ...
    
    def CopyTo(self, dst: BaseContainer, flags: int, trans: AliasTrans) -> None:
        """    
        Copies all values to *dst*.
        
        :type dst: c4d.BaseContainer
        :param dst: The destination container.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/COPYFLAGS_BaseContainer.rst
        :start-line: 3
        
        :type trans: c4d.AliasTrans
        :param trans:
        
        .. versionadded:: R17.032
        
        An optional alias translator for the operation.
        
        
        """
        ...
    
    def FlushAll(self) -> None:
        """    
        | Clears all values in the container.
        | The container ID is not changed.
        
        
        """
        ...
    
    def GetId(self) -> int:
        """    
        Returns the ID of the container.
        
        :rtype: int
        :return: The container ID.
        
        
        """
        ...
    
    def SetId(self, id: int) -> None:
        """    
        Sets the ID of the container.
        
        :type id: int
        :param id: The container ID.
        
        
        """
        ...
    
    def GetDirty(self) -> int:
        """    
        | Returns the dirty count.
        | Can be used to check if the container has changed.
        
        :rtype: int
        :return: Dirty counter. It is incremented when the container changes.
        
        
        """
        ...
    
    def RemoveData(self, id: int) -> bool:
        """    
        Removes the first data item with the specified ID.
        
        :type id: int
        :param id: The container ID.
        :rtype: bool
        :return: **True** if any value was removed, otherwise **False**.
        
        
        """
        ...
    
    def RemoveIndex(self, i: int) -> bool:
        """    
        Removes the data item at the specified index *i*.
        
        :type i: int
        :param i: The index of the value to be removed.
        :rtype: bool
        :return: **True** if any value was removed, otherwise **False**.
        
        
        """
        ...
    
    def FindIndex(self, i: Any) -> bool:
        """    
        Returns the index for the value with the specified ID, or -1 if no such value exists.
        
        :type id: int
        :param id: The ID of the value.
        :rtype: bool
        :return: The index of the value, or -1.
        
        
        """
        ...
    
    def GetIndexId(self, index: int) -> bool:
        """    
        | Returns the ID of the element at the specified index, or *NOTOK* if it doesn't exist.
        | Used to browse through the container.
        
        :type index: int
        :param index: The index of the value.
        :rtype: bool
        :return: The ID of the value, or *NOTOK*.
        
        
        """
        ...
    
    def GetType(self, id: int) -> int:
        """    
        Returns the type of a container element by ID.
        
        :type id: int
        :param id: The ID of the element.
        :rtype: int
        :return: The type:
        
        .. include:: /consts/GEDATATYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def InsData(self, id: int, n: Any) -> Any:
        """    
        Inserts an arbitrary data at the specified *id*.
        
        .. warning::
        
        This function does not check if the ID already exists in the container!
        
        :type id: int
        :param id: The ID to insert at.
        :type n: any
        :param n: The data to insert.
        :rtype: Any
        :return: The inserted data.
        
        
        """
        ...
    
    def InsDataAfter(self, id: int, n: Any, last: Any) -> Any:
        """    
        Inserts an arbitrary data at the specified *id* after *last*.
        
        .. warning::
        
        This function does not check if the ID already exists in the container!
        
        :type id: int
        :param id: The ID to insert at.
        :type n: any
        :param n: The data to insert.
        :type last: any
        :param last: The data to insert after.
        :rtype: Any
        :return: The inserted data.
        
        
        """
        ...
    
    def SetData(self, id: int, n: Any) -> None:
        """    
        | Sets an arbitrary data value at the specified ID.
        | If a value exists under the same ID, its content will be changed.
        
        :type id: int
        :param id: The ID of the element to set.
        :type n: any
        :param n: The data value to set.
        
        
        """
        ...
    
    def GetData(self, id: int) -> Any:
        """    
        Returns the data for an element by ID.
        
        :type id: int
        :param id: The ID of the element.
        :rtype: Any
        :return: The data or **None** if it wasn't found.
        
        
        """
        ...
    
    def GetDataPointer(self, id: int) -> Any:
        """    
        Retrieves a pointer to directly access the data.
        
        .. versionadded:: R17.053
        
        .. code-block:: python
        
        import c4d
        
        bc = c4d.BaseContainer()
        bc[1000] = "hello"
        bc[2000] = "world"
        
        # Print content
        print "Original:"
        for dataid, data in bc:
        print data,
        
        dataptr = bc.GetDataPointer(1000)
        bc.InsDataAfter(3000, "beautiful", dataptr)
        
        # Print content
        print "Changed:"
        for dataid, data in bc:
        print data,
        print
        
        :type id: int
        :param id: The ID of the element.
        :rtype: PyCObject
        :return: A pointer to the data.
        
        
        """
        ...
    
    def GetBool(self, id: int, preset: bool) -> bool:
        """    
        Returns a bool value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: bool
        :param preset: Returned if the value is not available.
        :rtype: bool
        :return: The value.
        
        
        """
        ...
    
    def GetLong(self, id: int, preset: int) -> int:
        """    
        .. deprecated:: R15
        
        Use :meth:`GetInt32` instead.
        
        Returns a int value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: int
        :param preset: Returned if the value is not available.
        :rtype: int
        :return: The value.
        
        
        """
        ...
    
    def GetInt32(self, id: int, preset: int) -> int:
        """    
        Returns a int value with the specified ID, or *preset* if it doesn't exist.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: int
        :param preset: Returned if the value is not available.
        :rtype: int
        :return: The value.
        
        
        """
        ...
    
    def GetLLong(self, id: int, preset: int) -> int:
        """    
        .. deprecated:: R15
        
        Use :meth:`GetInt64` instead.
        
        Returns a long value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: long
        :param preset: Returned if the value is not available.
        :rtype: long
        :return: The value.
        
        
        """
        ...
    
    def GetInt64(self, id: int, preset: int) -> int:
        """    
        Returns a long value with the specified ID, or *preset* if it doesn't exist.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: long
        :param preset: Returned if the value is not available.
        :rtype: long
        :return: The value.
        
        
        """
        ...
    
    def GetReal(self, id: int, preset: float) -> float:
        """    
        .. deprecated:: R15
        
        Use :meth:`GetFloat` instead.
        
        Returns a float value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: float
        :param preset: Returned if the value is not available.
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def GetFloat(self, id: int, preset: float) -> float:
        """    
        Returns a float value with the specified ID, or *preset* if it doesn't exist.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: float
        :param preset: Returned if the value is not available.
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def GetVector(self, id: int, preset: Vector) -> Vector:
        """    
        Returns a :class:`Vector <c4d.Vector>` value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: c4d.Vector
        :param preset: Returned if the value is not available.
        :rtype: c4d.Vector
        :return: The value.
        
        
        """
        ...
    
    def GetMatrix(self, id: int, preset: Matrix) -> Matrix:
        """    
        Returns a :class:`Matrix <c4d.Matrix>` value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: c4d.Matrix
        :param preset: Returned if the value is not available.
        :rtype: c4d.Matrix
        :return: The value.
        
        
        """
        ...
    
    def GetString(self, id: int, preset: str) -> str:
        """    
        Returns a string value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: str
        :param preset: Returned if the value is not available.
        :rtype: str
        :return: The value.
        
        
        """
        ...
    
    def GetFilename(self, id: int, preset: str) -> str:
        """    
        Returns a string value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: str
        :param preset: Returned if the value is not available.
        :rtype: str
        :return: The value.
        
        
        """
        ...
    
    def GetUuid(self, id: int, preset: Any) -> None:
        """    
        Returns a uuid value with the specified ID, or *preset* if it doesn't exist.
        
        .. versionadded:: R16.021
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param preset: Returned if the value is not available.
        :rtype: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :return: The value.
        
        
        """
        ...
    
    def GetTime(self, id: int, preset: BaseTime) -> BaseTime:
        """    
        Returns a :class:`BaseTime <c4d.BaseTime>` value with the specified ID, or *preset* if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested value.
        :type preset: c4d.BaseTime
        :param preset: Returned if the value is not available.
        :rtype: c4d.BaseTime
        :return: The value.
        
        
        """
        ...
    
    def GetContainer(self, id: int) -> BaseContainer:
        """    
        Returns a copy of the sub-container with the specified ID, or an empty container if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :rtype: c4d.BaseContainer
        :return: The Sub-container.
        
        
        """
        ...
    
    def GetContainerInstance(self, id: int) -> BaseContainer:
        """    
        | Returns the sub-container with the specified ID, or **None** if it doesn't exist.
        | Changes to the container are reflected in the stored sub-container.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :rtype: c4d.BaseContainer
        :return: The sub-container, or **None**.
        
        
        """
        ...
    
    def GetLink(self, id: int, doc: BaseDocument, isinstanceof: int) -> BaseList2D:
        """    
        Returns a linked object, evaluated in the attached document.
        
        .. note::
        
        If *instanceof* is specified, **None** is returned if the object is not of this type.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to evalulate the link in or **None**.
        :type isinstanceof: int
        :param isinstanceof: Set this to a node type to only return the link if it is of this type.
        :rtype: c4d.BaseList2D
        :return: The linked object, or **None** if the link is broken.
        
        
        """
        ...
    
    def GetObjectLink(self, id: int, doc: BaseDocument) -> BaseObject:
        """    
        Returns a linked base object, evaluated in the attached document.
        
        .. note::
        
        Returns **None** if the link doesn't point to a base object.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to evalulate the link in.
        :rtype: c4d.BaseObject
        :return: The linked base object, or **None** if the link is broken.
        
        
        """
        ...
    
    def GetMaterialLink(self, id: int, doc: BaseDocument) -> BaseMaterial:
        """    
        Returns a linked material object, evaluated in the attached document.
        
        .. note::
        
        Returns **None** if the link doesn't point to a base object.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to evalulate the link in.
        :rtype: c4d.BaseMaterial
        :return: The linked material object, or **None** if the link is broken.
        
        
        """
        ...
    
    def GetCustomDataType(self, id: int) -> None:
        """    
        Returns a copy of the custom data type or **None** if it doesn't exist.
        
        :type id: int
        :param id: The ID of the requested sub-container.
        :return: The custom data type.
        
        
        """
        ...
    
    def GetVoid(self, id: int) -> Any:
        """    
        Gets the void* value at the specified id.
        
        :type id: int
        :param id: The ID of the requested void object.
        :rtype: PyCObject
        :return: The PyCObject representing the void object.
        
        
        """
        ...
    
    def SetBool(self, id: int, b: bool) -> None:
        """    
        Sets a bool value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type b: bool
        :param b: The new value.
        
        
        """
        ...
    
    def SetLong(self, id: int, l: int) -> None:
        """    
        .. deprecated:: R15
        
        Use :meth:`SetInt32` instead.
        
        Sets an int value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: int
        :param l: The new value.
        
        
        """
        ...
    
    def SetInt32(self, id: int, l: int) -> None:
        """    
        Sets an int value and changes the data type accordingly.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: int
        :param l: The new value.
        
        
        """
        ...
    
    def SetLLong(self, id: int, l: int) -> None:
        """    
        .. deprecated:: R15
        
        Use :meth:`SetInt64` instead.
        
        Sets a long value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: long
        :param l: The new value.
        
        
        """
        ...
    
    def SetInt64(self, id: int, l: int) -> None:
        """    
        Sets a long value and changes the data type accordingly.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: long
        :param l: The new value.
        
        
        
        """
        ...
    
    def SetReal(self, id: int, v: Any) -> None:
        """    
        .. deprecated:: R15
        
        Use :meth:`SetFloat` instead.
        
        Sets a float value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: int
        :param l: The new value.
        
        
        """
        ...
    
    def SetFloat(self, id: int, v: Any) -> None:
        """    
        Sets a float value and changes the data type accordingly.
        
        .. versionadded:: R15.037
        
        :type id: int
        :param id: The ID of the value to set.
        :type l: int
        :param l: The new value.
        
        
        """
        ...
    
    def SetVector(self, id: int, v: Vector) -> None:
        """    
        Sets a :class:`Vector <c4d.Vector>` value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type v: c4d.Vector
        :param v: The new value.
        
        
        """
        ...
    
    def SetMatrix(self, id: int, m: Matrix) -> None:
        """    
        Sets a :class:`Matrix <c4d.Matrix>` value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type m: c4d.Matrix
        :param m: The new value.
        
        
        """
        ...
    
    def SetString(self, id: int, s: str) -> None:
        """    
        Sets a string value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type s: str
        :param s: The new value.
        
        
        """
        ...
    
    def SetFilename(self, id: int, f: str) -> None:
        """    
        Sets a new string value with the specified ID to *s* as a filepath, or inserts it if it didn't exist.
        
        :type id: int
        :param id: The ID of the value to set.
        :type f: str
        :param f: The new value.
        
        
        """
        ...
    
    def SetUuid(self, id: int, u: Any) -> None:
        """    
        Sets a uuid value and changes the data type accordingly.
        
        .. versionadded:: R16.021
        
        :type id: int
        :param id: The ID of the value to set.
        :type u: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param u: The new value.
        
        
        """
        ...
    
    def SetTime(self, id: int, b: BaseTime) -> None:
        """    
        Sets a :class:`BaseTime <c4d.BaseTime>` value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type b: c4d.BaseTime
        :param b: The new value.
        
        
        """
        ...
    
    def SetContainer(self, id: int, s: BaseContainer) -> None:
        """    
        Sets a :class:`BaseContainer <c4d.BaseContainer>` value and changes the data type accordingly.
        
        :type id: int
        :param id: The ID of the value to set.
        :type s: c4d.BaseContainer
        :param s: The sub-container
        
        
        """
        ...
    
    def SetLink(self, id: int, link: C4DAtom) -> None:
        """    
        Stores a link to an atom object with the specified ID.
        
        :type id: int
        :param id: The ID of the value to set.
        :type link: c4d.C4DAtom
        :param link: The link to store.
        
        
        """
        ...
    
    def SetVoid(self, id: int, v: Any) -> None:
        """    
        Stores a PyCObject to an void* object with the specified ID.
        
        :type id: int
        :param id: The ID of the requested void object.
        :type v: PyCObject
        :param v: The void* as a PyCObject to store.
        
        
        """
        ...
    
    def GetIndexData(self, index: int) -> Any:
        """    
        Retrieves the data for the element at *index*.
        
        .. versionadded:: R16.038
        
        :type index: int
        :param index: The index of the element.
        :rtype: Any
        :return: The data, or **None** if no data was found.
        
        
        """
        ...
    
    def SetIndexData(self, index: int, data: Any) -> bool:
        """    
        Sets the data for the element at *index*.
        
        .. versionadded:: R16.038
        
        :type index: int
        :param index: The index of the element.
        :type data: any
        :param data: The data for the element.
        :rtype: bool
        :return: **True** if the data was set, otherwise **False**.
        
        
        """
        ...
    
    def IsInstance(self) -> bool:
        """    
        Checks if the container is an instance.
        
        :rtype: bool
        :return: **True** if the container is an instance, otherwise **False**.
        
        
        """
        ...
    
    def MergeContainer(self, src: BaseContainer) -> None:
        """    
        Stores the values in src in this container, overwriting any elements with colliding IDs and keeping the rest.
        
        :type src: c4d.BaseContainer
        :param src: The source container.
        
        
        """
        ...
    
    def Sort(self) -> None:
        """    
        Sorts the container entries by ID.
        
        
        """
        ...
    

class C4DAtom(object):
    def __eq__(self, other: Any) -> None:
        """    
        
        """
        ...
    
    def __ne__(self, other: Any) -> bool:
        """    
        Check if two different objects point to the same object.
        
        .. note::
        
        Does not compare if two different objects are equal.
        
        :rtype: bool
        :return: **True** if the objects point to the same object, otherwise **False**.
        
        
        """
        ...
    
    def __call__(self) -> C4DAtom:
        """    
        | Returns the atom if it is alive or **None** if the atom is dead.
        | This is a convenient way to know if you can still use the object.
        
        :rtype: c4d.C4DAtom
        :return: The atom if it is still alive, otherwise **None**.
        
        
        """
        ...
    
    def SetDirty(self, flags: int) -> None:
        """    
        Sets the dirty checksum, the one returned by :meth:`GetDirty`.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DIRTYFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetDirty(self, flags: int) -> int:
        """    
        | Gets the dirty checksum for the object.
        | This can be used to check if the object has been changed.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DIRTYFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: The checksum.
        
        
        """
        ...
    
    def GetHDirty(self, mask: int) -> int:
        """    
        Returns the dirty count for the specified *mask*.
        
        .. versionadded:: R19
        
        :type mask: int
        :param mask: The dirty flags:
        
        .. include:: /consts/HDIRTYFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: The dirty count.
        
        
        """
        ...
    
    def SetHDirty(self, mask: int) -> None:
        """    
        Sets the dirty flags for the specified *mask*.
        
        .. versionadded:: R19
        
        :type mask: int
        :param mask: The dirty flags:
        
        .. include:: /consts/HDIRTYFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsAlive(self) -> bool:
        """    
        | Even though a reference to an object still exists, the object might be freed by an user interaction. Normally not needed.
        | E.g. the C++ Python Object representing a BaseList2D actually store a pointer to this BaseList2D.
        | This pointed BaseList2D could be dead for some reason, but we still have a Python object. So in this case IsAlive will return False.
        
        :rtype: bool
        :return: **True** if the object is still alive, otherwise **False**
        
        
        """
        ...
    
    def CheckType(self, id: int) -> int:
        """    
        Checks if this atom is an instance of a base type.
        
        .. note::
        
        This is only an alias to :meth:`C4DAtom.IsInstanceOf`
        
        :type id: int
        :param id: The base type ID, for example *Ocube*.
        :rtype: int
        :return: **True** if the atom is an instance of the type *id*, otherwise **False**.
        
        
        """
        ...
    
    def IsInstanceOf(self, id: int) -> int:
        """    
        Checks if this atom is an instance of a base type.
        
        .. versionadded:: R16.021
        
        :type id: int
        :param id: The base type ID, for example *Ocube*.
        :rtype: int
        :return: **True** if the atom is an instance of the type *id*, otherwise **False**.
        
        
        """
        ...
    
    def GetType(self) -> int:
        """    
        | Get the type of the atom.
        | This must be used to make sure that the derived object really is of the right type before trying to access its members.
        
        :rtype: int
        :return: The type, for example *Ocube*.
        
        
        """
        ...
    
    def GetRealType(self) -> int:
        """    
        | Get the real type of the atom.
        | This is similar to :meth:`GetType`, but for multinodes the ID of the last linked part is returned.
        | E.g. XPresso nodes have the type *ID_GV_GROUPDATA* or *ID_GV_NODEDATA*. With :meth:`GetRealType()` you will get the ID of the operator as a return value.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The real type, for example *Ocube*.
        
        
        """
        ...
    
    def GetClassification(self) -> int:
        """    
        Returns the base type of the object, e.g. for all objects *Obase*, for all materials *Mmat*, for all tags *Tbase* etc.
        
        :rtype: int
        :return: The base type.
        
        
        """
        ...
    
    def Message(self, type: int, data: Any) -> bool:
        """    
        Sends a message to the atom.
        
        .. seealso::
        
        :doc:`MSG </consts/MSG_C4DATOM>` for the information on the messages type, data and input/output.
        
        .. note::
        
        Some notification messages are automatically passed along to branches: *MSG_POINTS_CHANGED*, *MSG_POLYGONS_CHANGED* and *MSG_SEGMENTS_CHANGED*. This is for convenience and historical reasons.
        
        :type type: int
        :param type: The message type.
        :type data: any
        :param data: The message data.
        :rtype: bool
        :return: Depends on the message *type*.
        
        
        """
        ...
    
    def MultiMessage(self, flags: int, type: int, data: Any) -> bool:
        """    
        Sends a message to the atom and to its children, parents or branches, depending on *flags*.
        
        .. seealso::
        
        :doc:`MSG </consts/MSG_C4DATOM>` for the information on the messages type, data and input/output.
        
        :type flags: int
        :param flags: A combination of the following flags:
        
        .. include:: /consts/MULTIMSG_ROUTE.rst
        :start-line: 3
        
        :type type: int
        :param type: The message type.
        :type data: any
        :param data: The message data.
        :rtype: bool
        :return: Depends on the message *type*.
        
        
        """
        ...
    
    def CopyTo(self, dst: C4DAtom, flags: Optional[int] = ..., trn: Optional[AliasTrans] = ...) -> bool:
        """    
        Copies all values from *self* to *dst*. The atoms must be of the same type!
        
        :type dst: c4d.C4DAtom
        :param dst: The destination.
        :type flags: int
        :param flags: Optional flags for the copy:
        
        .. include:: /consts/COPYFLAGS.rst
        :start-line: 3
        
        :type trn: c4d.AliasTrans
        :param trn:
        
        .. versionadded:: R17.032
        
        An optional alias translator for the operation.
        
        :rtype: bool
        :return: **True** if the atom was copied.
        
        
        """
        ...
    
    def GetClone(self, flags: Optional[int] = ..., trn: Optional[AliasTrans] = ...) -> C4DAtom:
        """    
        Clones the object and returns the reference.
        
        :type flags: int
        :param flags: Optional flags for the clone:
        
        .. include:: /consts/COPYFLAGS.rst
        :start-line: 3
        
        :type trn: c4d.AliasTrans
        :param trn:
        
        .. versionadded:: R17.032
        
        An optional alias translator for the operation.
        
        :rtype: c4d.C4DAtom
        :return: Minimum of type atom.
        
        
        """
        ...
    
    def Write(self, hf: HyperFile) -> bool:
        """    
        Writes the atom to a :class:`HyperFile <c4d.storage.HyperFile>`.
        
        .. note::
        
        | This is the function to use if you have opened the hyper file yourself and are writing the object manually.
        | If writing within a plugin function where Cinema 4D has passed the hyper file you should use :meth:`WriteObject`.
        
        .. note::
        
        The methods :meth:`Read`, :meth:`Write`, :meth:`ReadObject` and :meth:`WriteObject` are generally not recommended for plugins.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to write to.
        :rtype: bool
        :return: **True** if the atom was written, otherwise **False**.
        
        
        """
        ...
    
    def Read(self, hf: HyperFile, id: int, level: int) -> bool:
        """    
        Reads to this atom from a :class:`HyperFile <c4d.storage.HyperFile>`, manually specifying ID and level.
        
        .. note::
        
        | This is the function to use if you have opened the hyper file yourself and are reading the object separately.
        | If reading within a plugin function where Cinema 4D has passed the hyper file you should use :meth:`ReadObject`.
        
        .. note::
        
        The methods :meth:`Read`, :meth:`Write`, :meth:`ReadObject` and :meth:`WriteObject` are generally not recommended for plugins.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to read from.
        :type id: int
        :param id: The ID of the atom to read.
        :type level: int
        :param level: The disklevel of the atom to read.
        :rtype: bool
        :return: **True** if the atom was read, otherwise **False**.
        
        
        """
        ...
    
    def WriteObject(self, hf: HyperFile) -> bool:
        """    
        Writes this atom to a :class:`HyperFile <c4d.storage.HyperFile>`, within another write operation.
        
        .. note::
        
        | This is the function to use where Cinema 4D has passed the hyper file you should use, for example in a plugin hook.
        | Otherwise you should use :meth:`Write`.
        
        .. note::
        
        The methods :meth:`Read`, :meth:`Write`, :meth:`ReadObject` and :meth:`WriteObject` are generally not recommended for plugins.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to write to.
        :rtype: bool
        :return: **True** if the atom was written, otherwise **False**.
        
        
        """
        ...
    
    def ReadObject(self, hf: HyperFile, readheader: bool) -> bool:
        """    
        Reads to this atom from a :class:`HyperFile <c4d.storage.HyperFile>` within another read operation.
        
        .. note::
        
        | This is the function to use where Cinema 4D has passed the hyper file you should use, for example in a plugin hook.
        | Otherwise you should use :meth:`Read`.
        
        .. note::
        
        The methods :meth:`Read`, :meth:`Write`, :meth:`ReadObject` and :meth:`WriteObject` are generally not recommended for plugins.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyperfile to read from.
        :type readheader: bool
        :param readheader: Normally **True**. Should only be **False** if you have manually read the file header yourself.
        :rtype: bool
        :return: **True** if the atom was read, otherwise **False**.
        
        
        """
        ...
    
    def GetDescription(self, flags: int) -> Description:
        """    
        Gets the description for this atom.
        
        .. versionadded:: R15.037
        
        .. warning::
        
        | Every caller of :meth:`GetDescription` gets a copy of the object's description, including the Attribute Manager.
        | The only way to customize the description is to override :meth:`NodeData.GetDDescription`.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DESCFLAGS_DESC.rst
        :start-line: 3
        
        :rtype: c4d.Description
        :return: The atom's description.
        
        
        """
        ...
    
    def GetParameter(self, id: DescID, flags: int) -> Any:
        """    
        Gets a description parameter of this atom.
        
        .. versionadded:: R16.021
        
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DESCFLAGS_GET.rst
        :start-line: 3
        
        :rtype: Any
        :return: The parameter data, or **None** if an error occured.
        
        
        """
        ...
    
    def SetParameter(self, id: DescID, data: Any, flags: int) -> bool:
        """    
        Sets a description parameter of this atom.
        
        .. versionadded:: R16.021
        
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type data: any
        :param data: The parameter data to set.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DESCFLAGS_SET.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the parameter was set, otherwise **False**.
        
        
        """
        ...
    
    def FindUniqueID(self, appid: int) -> ByteSeq:
        """    
        Checks for a specific unique application ID.
        
        .. versionadded:: R16.021
        
        :type appid: int
        :param appid: A unique application ID, has to be registered at MAXON, at least it should be obtained from http://www.plugincafe.com
        :rtype: c4d.storage.ByteSeq
        :return: The unique application ID data, or **None** if it could not be found.
        
        
        """
        ...
    
    def AddUniqueID(self, appid: int, mem: ByteSeq) -> bool:
        """    
        Adds unique application ID to the object.
        
        .. versionadded:: R16.021
        
        :type appid: int
        :param appid: A unique application ID, has to be registered at MAXON, at least it should be obtained from http://www.plugincafe.com
        :type mem: c4d.storage.ByteSeq
        :param mem: The unique application ID data. Used for instance to store the name of a software vendor.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetUniqueIDCount(self) -> int:
        """    
        Retrieves the number of unique application IDs.
        
        .. versionadded:: R16.021
        
        :rtype: int
        :return: The number of unique application IDs.
        
        
        """
        ...
    
    def GetUniqueIDIndex(self, idx: int) -> None:
        """    
        Gets the *idx*-th unique application ID data.
        
        .. versionadded:: R16.050
        
        :type idx: int
        :param idx: The unique ID index: *0<=idx<*:func:`GetUniqueIDCount`
        :rtype: tuple(int, :class:`ByteSeq <c4d.storage.ByteSeq>`)
        :return:  The unique application ID and its data. Used for instance to read the name of a software vendor.
        
        **None** if it could not be found.
        
        
        """
        ...
    

class GeListNode(C4DAtom):
    def __setitem__(self, key: Union[int, List[Any], DescID], value: Any) -> None:
        """    
        Uses a description ID as a key into the container, and stores the specified data.
        
        .. note::
        
        | Has to be used to set an object's parameters data.
        | Its corresponding function of the C++ API is `C4DAtom::SetParameter()`.
        
        .. seealso::
        
        :doc:`Symbols in Cinema 4D </misc/descriptions>`
        
        :type key: Union[int, list, c4d.DescID]
        :param key: The description ID.
        :type value: any
        :param value: The data to store:
        
        +--------------------------------------------------------+
        | Types to get and set                                   |
        +========================================================+
        | *bool*                                                 |
        +--------------------------------------------------------+
        | *int*                                                  |
        +--------------------------------------------------------+
        | *float*                                                |
        +--------------------------------------------------------+
        | *long*                                                 |
        +--------------------------------------------------------+
        | *str*                                                  |
        +--------------------------------------------------------+
        | :class:`BaseContainer <c4d.BaseContainer>`             |
        +--------------------------------------------------------+
        | :class:`Matrix <c4d.Matrix>`                           |
        +--------------------------------------------------------+
        | :class:`Vector <c4d.Vector>`                           |
        +--------------------------------------------------------+
        | :class:`BaseList2D <c4d.BaseList2D>`                   |
        +--------------------------------------------------------+
        | :class:`BaseTime <c4d.BaseTime>`                       |
        +--------------------------------------------------------+
        | :class:`MatAssignData <c4d.MatAssignData>`             |
        +--------------------------------------------------------+
        | :class:`InExcludeData <c4d.InExcludeData>`             |
        +--------------------------------------------------------+
        | :class:`SplineData <c4d.SplineData>`                   |
        +--------------------------------------------------------+
        | :class:`Gradient <c4d.Gradient>`                       |
        +--------------------------------------------------------+
        | :class:`DateTimeData <c4d.DateTimeData>`               |
        +--------------------------------------------------------+
        | :class:`PriorityData <c4d.PriorityData>`               |
        +--------------------------------------------------------+
        | :class:`LayerSet <c4d.LayerSet>`                       |
        +--------------------------------------------------------+
        | :class:`FontData <c4d.FontData>`                       |
        +--------------------------------------------------------+
        | :class:`UnitScaleData <c4d.UnitScaleData>`             |
        +--------------------------------------------------------+
        | :class:`PLAData <c4d.PLAData>`                         |
        +--------------------------------------------------------+
        
        
        """
        ...
    
    def __getitem__(self, key: Union[int, List[Any], DescID]) -> Any:
        """    
        Uses a description ID as a key into the container, and retrieves the stored data.
        
        .. note::
        
        Has to be used to get an object's parameters data. Its corresponding function of the C++ API is `C4DAtom::GetParameter()`.
        
        .. seealso::
        
        :doc:`Descriptions in Cinema 4D </misc/descriptions>`
        
        :type key: Union[int, list, c4d.DescID]
        :param key: The description ID.
        :rtype: Any
        :return: See :meth:`__setitem__`
        
        
        """
        ...
    
    def InsertBefore(self, obj: GeListNode) -> None:
        """    
        Insert self before *obj*.
        
        .. note::
        
        | Take care *obj* is a correct type.
        | For example it is not possible to insert a document before a :class:`BaseObject <c4d.BaseObject>`.
        | Check this using :meth:`C4DAtom.GetClassification` and :meth:`C4DAtom.GetType`.
        
        .. warning::
        
        | Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!
        | See :ref:`threading-information`.
        
        :type obj: c4d.GeListNode
        :param obj: The object to insert before.
        
        
        """
        ...
    
    def InsertAfter(self, obj: GeListNode) -> None:
        """    
        Insert self after *obj*.
        
        .. note::
        
        | Take care *obj* is a correct type.
        | For example it is not possible to insert a document after a :class:`BaseObject <c4d.BaseObject>`.
        | Check this using :meth:`C4DAtom.GetClassification` and :meth:`C4DAtom.GetType`.
        
        .. warning::
        
        | Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!
        | See :ref:`threading-information`.
        
        :type obj: c4d.GeListNode
        :param obj: The object to insert after.
        
        
        """
        ...
    
    def InsertUnder(self, obj: GeListNode) -> None:
        """    
        Insert self under *obj*.
        
        .. note::
        
        | Take care *obj* is a correct type.
        | For example it is not possible to insert a document under a :class:`BaseObject <c4d.BaseObject>`.
        | Check this using :meth:`C4DAtom.GetClassification` and :meth:`C4DAtom.GetType`.
        
        :type obj: c4d.GeListNode
        :param obj: The object to insert under.
        
        
        """
        ...
    
    def InsertUnderLast(self, obj: GeListNode) -> None:
        """    
        Insert self as the last child of *obj*.
        
        .. note::
        
        | Take care *obj* is a correct type.
        | For example it is not possible to insert a document under a :class:`BaseObject <c4d.BaseObject>`.
        | Check this using :meth:`C4DAtom.GetClassification` and :meth:`C4DAtom.GetType`.
        
        .. warning::
        
        | Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!
        | See :ref:`threading-information`.
        
        :type obj: c4d.GeListNode
        :param obj: The object to insert under.
        
        
        """
        ...
    
    def GetNext(self) -> Optional[GeListNode]:
        """    
        Returns the next object in the list.
        
        :rtype: c4d.GeListNode or **None**
        :return: The next object.
        
        
        """
        ...
    
    def GetPred(self) -> Optional[GeListNode]:
        """    
        Returns the previous object in the list.
        
        :rtype: c4d.GeListNode or **None**
        :return: The previous object.
        
        
        """
        ...
    
    def GetUp(self) -> Optional[GeListNode]:
        """    
        Returns the parent object.
        
        :rtype: c4d.GeListNode or **None**
        :return: The parent object.
        
        
        """
        ...
    
    def GetDown(self) -> Optional[GeListNode]:
        """    
        Returns the first child of this object in the list.
        
        :rtype: c4d.GeListNode or **None**
        :return: The first child object.
        
        
        """
        ...
    
    def GetDownLast(self) -> Optional[GeListNode]:
        """    
        Returns the last child of this object in the list.
        
        :rtype: c4d.GeListNode or **None**
        :return: The first child object.
        
        
        """
        ...
    
    def GetChildren(self) -> List[GeListNode]:
        """    
        Returns children in a list (not grandchild).
        
        :rtype: list of type :class:`GeListNode <c4d.GeListNode>`
        :return: All children in a list.
        
        
        """
        ...
    
    def Remove(self) -> None:
        """    
        Removes this node from a list.
        
        .. warning::
        
        | Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!
        | See :ref:`threading-information`.
        
        
        """
        ...
    
    def GetDocument(self) -> BaseDocument:
        """    
        Get the document for this node.
        
        :rtype: c4d.documents.BaseDocument
        :return: The document.
        
        
        """
        ...
    
    def GetListHead(self) -> GeListHead:
        """    
        Returns the list head.
        
        :rtype: c4d.GeListHead
        :return: The list head, or **None** if the node is not attached to one.
        
        .. versionchanged:: R19
        
        The function now returns a :class:`c4d.GeListHead` object.
        
        
        """
        ...
    
    def GetBranchInfo(self, flags: int) -> List[Dict[str, Any]]:
        """    
        Returns information about which other nodes the node contains. For example objects contain tags.
        
        .. versionadded:: R19
        
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/GETBRANCHINFO.rst
        :start-line: 3
        
        :rtype: list of dict{'head', 'name', 'id', 'flags'}
        :return:
        
        A list of dictionaries (**None** if the function failed) with the following information:
        
        | 'head': :class:`c4d.GeListHead`: Either a :class:`c4d.GeListNode` or a :class:`c4d.GeListHead` for the branch, depending on *flags*.
        | 'name': `str`: The human readable name of the branch.
        | 'id': `int`: The base ID of the branch. For example `VPbase`, `Mbase` or `Obase`.
        | 'flags': `int`: The flags for the branch:
        
        .. include:: /consts/BRANCHINFOFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsDocumentRelated(self) -> bool:
        """    
        Checks if the node is of a type that can be inserted into a :class:`BaseDocument <c4d.documents.BaseDocument>`
        
        :rtype: bool
        :return: **True** if the node is document related, otherwise **False**.
        
        
        """
        ...
    
    def GetNBit(self, bit: int) -> bool:
        """    
        Raw access to a 64-bit bitfield, containing information about the node state.
        
        :type bit: int
        :param bit: Bit index:
        
        .. include:: /consts/NBIT.rst
        :start-line: 3
        
        :rtype: bool
        :return: Bit state.
        
        
        """
        ...
    
    def ChangeNBit(self, bit: int, bitmode: int) -> bool:
        """    
        Sets bits in the 64-bit bitfield of the node.
        
        :type bit: int
        :param bit: Bit index:
        
        .. include:: /consts/NBIT.rst
        :start-line: 3
        
        :type bitmode: int
        :param bitmode: Bit mode:
        
        .. include:: /consts/NBITCONTROL.rst
        :start-line: 3
        
        :rtype: bool
        :return: Bit state.
        
        
        """
        ...
    
    def GetDataInstance(self) -> BaseContainer:
        ...
    

class CKey(GeListNode):
    def GetTime(self) -> BaseTime:
        """    
        Get the time of this key.
        
        :rtype: c4d.BaseTime
        :return: The time.
        
        
        """
        ...
    
    def GetTimeLeft(self) -> BaseTime:
        """    
        Get the left time of this key.
        
        :rtype: c4d.BaseTime
        :return: The left time.
        
        
        """
        ...
    
    def GetTimeRight(self) -> BaseTime:
        """    
        Get the left time of this key.
        
        :rtype: c4d.BaseTime
        :return: The right time.
        
        
        """
        ...
    
    def GetValue(self) -> float:
        """    
        Get the value of this key. Just for keys with float values.
        
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def GetValueLeft(self) -> float:
        """    
        Get the value of this key. Just for keys with float values.
        
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def GetValueRight(self) -> float:
        """    
        Get the right of this key. Just for keys with float values.
        
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def SetValue(self, seq: CCurve, v: float) -> None:
        """    
        Set the value of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type v: float
        :param v: The new value.
        
        
        """
        ...
    
    def SetValueLeft(self, seq: CCurve, v: float) -> None:
        """    
        Set the left value of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type v: float
        :param v: The new value.
        
        
        """
        ...
    
    def SetValueRight(self, seq: CCurve, v: float) -> None:
        """    
        Set the right value of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type v: float
        :param v: The new value.
        
        
        """
        ...
    
    def SetTime(self, seq: CCurve, t: BaseTime) -> None:
        """    
        Set the time of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type t: c4d.BaseTime
        :param t: The new time.
        
        
        """
        ...
    
    def SetTimeLeft(self, seq: CCurve, t: BaseTime) -> None:
        """    
        Set the left time of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type t: c4d.BaseTime
        :param t: The time.
        
        
        """
        ...
    
    def SetTimeRight(self, seq: CCurve, t: BaseTime) -> None:
        """    
        Set the right time of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type t: c4d.BaseTime
        :param t: The time.
        
        
        """
        ...
    
    def SetInterpolation(self, seq: CCurve, inter: int) -> None:
        """    
        Set the interpolation type of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type inter: int
        :param int: The new interpolation type:
        
        .. include:: /consts/CINTERPOLATION.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetInterpolation(self) -> int:
        """    
        Returns the interpolation type.
        
        :rtype: int
        :return: The interpolation type:
        
        .. include:: /consts/CINTERPOLATION.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetQuatInterpolation(self, seq: CCurve, inter: int, bUndo: bool) -> None:
        """    
        Sets the quaternion interpolation type of the key.
        
        .. versionadded:: R18.020
        
        .. note::
        
        Keys at the same time on other component curve will be modified.
        
        :type seq: c4d.CCurve
        :param seq: The curve the key belongs to.
        :type inter: int
        :param inter: The quaternion interpolation type to set:
        
        .. include:: /consts/ROTATIONINTERPOLATION.rst
        :start-line: 3
        
        :type bUndo: bool
        :param bUndo:
        
        | **True** to add the 3 rotation keys in the undo system.
        | The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        
        """
        ...
    
    def GetQuatInterpolation(self) -> int:
        """    
        Gets the quaternion interpolation type of the key.
        
        .. versionadded:: R18.020
        
        :rtype: int
        :return:  The quaternion interpolation type:
        
        .. include:: /consts/ROTATIONINTERPOLATION.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetTrack(self) -> CTrack:
        """    
        Get the track of this key.
        
        :rtype: c4d.CTrack
        :return: The track.
        
        
        """
        ...
    
    def GetCurve(self) -> CCurve:
        """    
        Get the curve of this key.
        
        :rtype: c4d.CCurve
        :return: The curve.
        
        
        """
        ...
    
    def FlushData(self) -> None:
        """    
        Flush the key data.
        
        
        """
        ...
    
    def SetGeData(self, seq: CCurve, d: Any) -> None:
        """    
        Set the data of this key.
        
        :type seq: c4d.CCurve
        :param seq: The curve.
        :type d: any
        :param d: The data.
        
        
        """
        ...
    
    def GetGeData(self) -> Any:
        """    
        Get the data of this key.
        
        :rtype: Any
        :return: The data, depends on the key.
        
        
        """
        ...
    
    def GetClone(self, trans: AliasTrans) -> CKey:
        """    
        Gets a clone of the key.
        
        :type trans: c4d.AliasTrans
        :param trans:
        
        .. versionadded:: R17.032
        
        An optional alias translator for the operation.
        
        :rtype: c4d.CKey
        :return: The cloned key.
        
        
        """
        ...
    
    def GetAutomaticTangentMode(self) -> int:
        """    
        Gets the AutoTangent mode of the key.
        
        .. versionadded:: R17.048
        
        :rtype: int
        :return: The AutoTangent mode:
        
        .. include:: /consts/CAUTOMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetAutomaticTangentMode(self, seq: CCurve, autoMode: int) -> None:
        """    
        Sets the AutoTangent mode of the key.
        
        .. versionadded:: R17.048
        
        :type seq: c4d.CCurve
        :param seq: The curve the key belongs to.
        :type autoMode: int
        :param autoMode: The AutoTangent mode to set:
        
        .. include:: /consts/CAUTOMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetTimeLeftAdjustValue(self, seq: CCurve, t: BaseTime) -> bool:
        """    
        Sets Time Left and adjusts Value so the angle stays the same.
        
        .. versionadded:: R17.048
        
        :type seq: c4d.CCurve
        :param seq: The curve the key belongs to.
        :type t: c4d.BaseTime
        :param t: The Time Left to set.
        :rtype: bool
        :return: **True** if successful. **False** if current Time Left is smaller than **FLT_MIN** and Value is not Zero (angle cannot stay the same).
        
        
        """
        ...
    
    def SetTimeRightAdjustValue(self, seq: CCurve, t: BaseTime) -> bool:
        """    
        Sets Time Right and adjusts Value so the angle stays the same.
        
        .. versionadded:: R17.048
        
        :type seq: c4d.CCurve
        :param seq: The curve the key belongs to.
        :type t: c4d.BaseTime
        :param t: The Time Right to set.
        :rtype: bool
        :return: **True** if successful. **False** if current Time Right is smaller than **FLT_MIN** and Value is not Zero (angle cannot stay the same).
        
        
        """
        ...
    

class GeListHead(GeListNode):
    def __init__(self, type: int) -> None:
        """    
        Creates a list head.
        
        :type type: int
        :param type: The id of the object, e.g: (*Ocube*). See also: :doc:`/misc/descriptions`.
        :rtype: c4d.GeListHead
        :return: A list head.
        
        
        """
        ...
    
    def InsertFirst(self, node: GeListNode) -> None:
        """    
        Inserts *node* as the first element in the list.
        
        :type node: c4d.GeListNode
        :param node: The node to insert first.
        
        
        """
        ...
    
    def InsertLast(self, node: GeListNode) -> None:
        """    
        Inserts *node* as the last element in the list.
        
        :type node: c4d.GeListNode
        :param node: The node to insert last.
        
        
        """
        ...
    
    def Insert(self, node: GeListNode, parent: GeListNode, prev: GeListNode) -> None:
        """    
        Inserts *node* as a child of *parent* or after *prev*.
        
        :type node: c4d.GeListNode
        :param node: The node to insert.
        :type parent: c4d.GeListNode
        :param parent: The node to insert *node* as child.
        :type prev: c4d.GeListNode
        :param prev: The node to insert *node* after.
        
        
        """
        ...
    
    def SetParent(self, parent: GeListNode) -> None:
        """    
        | Sets the parent of the list head.
        | Usually called directly after the list head is created.
        
        :type parent: c4d.GeListNode
        :param parent: The parent to set.
        
        
        """
        ...
    
    def GetParent(self) -> GeListNode:
        """    
        | Returns the parent of the list head.
        | For the tag list head this would be the object, for the object list head this would be the document etc.
        
        :rtype: c4d.GeListNode
        :return: The parent, or **None** if the list head has no parent.
        
        
        """
        ...
    
    def GetFirst(self) -> GeListNode:
        """    
        Returns the first node in the list.
        
        :rtype: c4d.GeListNode
        :return: The first child node in the list.
        
        
        """
        ...
    
    def GetLast(self) -> GeListNode:
        """    
        Returns the last node in the list.
        
        :rtype: c4d.GeListNode
        :return: The last child node in the list.
        
        
        """
        ...
    
    def FlushAll(self) -> None:
        """    
        Clears the list, removing all nodes.
        
        
        """
        ...
    

class BaseList2D(GeListNode):
    def __init__(self, type: int) -> None:
        """    
        :type type: int
        :param type: The id of the object, e.g: (*Ocube*). See also: :doc:`/misc/descriptions`.
        :rtype: c4d.BaseList2D
        :return: The new object.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        Returns the BaseList2D as string. Called if `str() <https://docs.python.org/2.7/library/functions.html#str>`_ is wrapped around an instance of :class:`BaseList2D <c4d.BaseList2D>`. (See `__str__ <https://docs.python.org/2.7/reference/datamodel.html?highlight=__str__#object.__str__>`_.)
        
        :rtype: str
        :return: The string representation of :class:`BaseList2D <c4d.BaseList2D>`.
        
        
        """
        ...
    
    def GetNodeData(self) -> Any:
        """    
        Returns the NodeData part of the BaseList2D.
        
        .. note::
        
        Only Python defined node.
        
        :rtype: any
        :return: The established NodeData.
        
        
        """
        ...
    
    def GetCTrackRoot(self) -> GeListHead:
        """    
        Returns the track root of the object. To get the tracks of an object use :meth:`GetCTracks` instead.
        
        :rtype: c4d.GeListHead
        :return: The track root if there is one, otherwise **None**.
        
        .. versionchanged:: R19
        
        The function now returns a :class:`c4d.GeListHead` object.
        
        
        """
        ...
    
    def GetFirstCTrack(self) -> CTrack:
        """    
        Returns the first CTrack of the object.
        
        :rtype: c4d.CTrack
        :return: The first track, or **None** if there are no tracks.
        
        
        """
        ...
    
    def GetCTracks(self) -> None:
        """    
        Returns all CTracks of an object.
        
        :rtype: list of type :class:`CTrack <c4d.CTrack>`
        :return: The CTrack.
        
        
        """
        ...
    
    def FindCTrack(self, id: DescID) -> CTrack:
        """    
        Find the track for the specified description *id*.
        
        :type id: c4d.DescID
        :param id: The description ID to check.
        :rtype: c4d.CTrack
        :return: The track found, or **None** if there was no match.
        
        
        """
        ...
    
    def InsertTrackSorted(self, track: CTrack) -> None:
        """    
        Inserts a track and automatically places it at the right place (so that Y comes after Y etc.)
        
        :type track: c4d.CTrack
        :param track: The track to insert.
        
        
        """
        ...
    
    def AddEventNotification(self, bl: Any, eventid: Any, flags: Any, data: Any) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def RemoveEventNotification(self, doc: Any, bl: Any, eventid: Any) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def FindEventNotification(self, doc: Any, bl: Any, eventid: Any) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def GetMain(self) -> BaseList2D:
        """    
        Goes up the next level, e.g. from tag to object or Xpresso node to tag, or object to document, etc.
        
        :rtype: c4d.BaseList2D
        :return: The main object of this object or **None**.
        
        
        """
        ...
    
    def SetBit(self, mask: int) -> None:
        """    
        Sets the object bits denoted by *mask*.
        
        :type mask: int
        :param mask: The bit mask of the bits:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetBit(self, mask: int) -> int:
        """    
        Gets the state of the object bits denoted by *mask*.
        
        :type mask: int
        :param mask: The bit mask of the bits:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        :rtype: int
        :return: The state of the object bits.
        
        
        """
        ...
    
    def DelBit(self, mask: int) -> None:
        """    
        Deletes the object bits denoted by *mask*, i.e. sets the corresponding bit to `0`.
        
        :type mask: int
        :param mask: The bit mask of the bits:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def ToggleBit(self, mask: int) -> None:
        """    
        Toggles the state of the object bits denoted by *mask*.
        
        :type mask: int
        :param mask: The bit mask of the bits:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetAllBits(self) -> int:
        """    
        Returns all of the object's bits.
        
        :rtype: int
        :return: The object's bits:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetAllBits(self, mask: int) -> None:
        """    
        Sets all the object's bits at once.
        
        :type mask: int
        :param mask: The object's bits to set:
        
        .. include:: /consts/BIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetIcon(self) -> None:
        """    
        Returns the original bitmap pattern.
        
        .. warning::
        
        Please, never edit the returned bitmap - read only.
        
        An example
        
        .. code-block:: python
        
        icon = obj.GetIcon()
        print icon["bmp"], icon["x"], icon["y"], icon["w"], icon["h"]
        
        :rtype: dict{**bmp**: :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>`, **x**: int, **y**: int, **w**: int, **h**: int}
        :return: The image and size information like height, width and X/Y position in the icon table.
        
        
        """
        ...
    
    def GetIconEx(self) -> None:
        """    
        Returns the original bitmap pattern.
        
        .. note::
        
        Similar to :meth:`BaseList2D.GetIcon` but instead returns a :class:`c4d.IconData`.
        
        .. warning::
        
        Please, never edit the returned bitmap - read only.
        
        :rtype: :class:`c4d.IconData`
        :return: The image and size information like height, width and X/Y position in the icon table.
        
        
        """
        ...
    
    def GetFirstShader(self) -> BaseList2D:
        """    
        Returns the first shader of the object.
        
        .. note::
        
        Normally you don't have to deal with this list. But if you want to create or modify shader trees via the API you need to read the following lines:
        
        - If you are programming shader links you need to make sure that every shader is referenced only once; it is not allowed that a shader is referenced multiple times.
        - If the referencing object is a shader the referenced shader must be a child of it, otherwise it must be inserted via :meth:`InsertShader`.
        
        
        - Example 1: A tag references a shader. The shader must be inserted into the tag using :meth:`tag.InsertShader() <InsertShader>`.
        - Example 2: A shader (A) references another shader (B): shader B must be a child of shader A.
        
        :rtype: c4d.BaseList2D
        :return: The first shader of the object, or **None** if there is no shader.
        
        
        """
        ...
    
    def InsertShader(self, shader: BaseList2D, pred: BaseList2D) -> None:
        """    
        Inserts a shader in the object's shader list.
        
        .. code-block:: python
        
        import c4d
        
        mat = doc.GetFirstMaterial()
        if mat is None: return False
        
        shd = c4d.BaseList2D(c4d.Xbitmap)
        
        mat[c4d.MATERIAL_COLOR_SHADER] = shd
        mat.InsertShader(shd)
        mat.Message(c4d.MSG_UPDATE)
        mat.Update(True, True)
        
        c4d.EventAdd()
        
        :type shader: c4d.BaseList2D
        :param shader: The shader to insert.
        :type pred: c4d.BaseList2D
        :param pred: The shader to insert the new shader after, or **None** to insert the new shader first. This shader must already be inserted into the list.
        
        
        """
        ...
    
    def GetLayerData(self, doc: BaseDocument, rawdata: bool) -> None:
        """    
        Get the layer data for this object.
        
        .. versionchanged:: R21
        
        `xref` added to the dictionary.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type rawdata: bool
        :param rawdata: Usually :meth:`GetLayerData` takes special global modes like SOLO Layer automatically into account. But if you want to see the original layer values without any additional global changes you can set *rawdata* to **True** to get them.
        :rtype: dict{**solo**: bool, **view**: bool, **render**: bool, **manager**: bool, **locked**: bool, **generators**: bool, **expressions**: bool, **animation**: bool, **color**: :class:`Vector <c4d.Vector>`, **xref**: bool}
        
        
        """
        ...
    
    def SetLayerData(self, doc: BaseDocument, data: Any) -> bool:
        """    
        Set the layer data for this object.
        
        .. versionchanged:: R21
        
        `xref` added to the dictionary.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type data: dict{**solo**: bool, **view**: bool, **render**: bool, **manager**: bool, **locked**: bool, **generators**: bool, **expressions**: bool, **animation**: bool, **color**: c4d.Vector, **xref**: bool}
        :param data: The new layer data. it is possible to leave values in the dictionary out.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetLayerObject(self, doc: BaseDocument) -> LayerObject:
        """    
        Get the layer of this object.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :rtype: c4d.documents.LayerObject
        :return: The layer.
        
        
        """
        ...
    
    def SetLayerObject(self, layer: Optional[LayerObject] = ...) -> bool:
        """    
        Set the layer of this object.
        
        :type layer: c4d.documents.LayerObject
        :param layer:
        
        The new layer.
        
        .. versionchanged:: R18.020 Can be **None**.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetInfo(self) -> int:
        """    
        Returns the information flags for the object. The interpretation depends on the object type.
        
        When a BaseList2D is registered, some behaviors have to be defined (e.g. for an object, it might be a generator, a modifier, etc...)
        
        This is done through Flags, and GetInfo returns these flags.
        
        .. code-block:: python
        
        if bl2D.GetInfo() & c4d.OBJECT_MODIFIER:
        print " This bl2D is an object modifier"
        
        :rtype: int
        :return: The flags. This is the same as the info parameter of the registration function of the registration function of the :class:`NodeData <c4d.plugins.NodeData>`.
        
        
        """
        ...
    
    def KeyframeSelectionContent(self) -> bool:
        """    
        Checks if there are any active keyframe selections.
        
        .. note::
        
        | This is not the same as **BIT_ACTIVE**, it is the possibility to restrict autokeyframing to certain description parameters.
        | See "Animation->Add Keyframe Selection" in the Attributes Manager.
        
        :rtype: bool
        :return: **True** if there is a keyframe selection, otherwise *False*.
        
        
        """
        ...
    
    def ClearKeyframeSelection(self) -> None:
        """    
        Clears the current keyframe selection.
        
        
        """
        ...
    
    def FindKeyframeSelection(self, id: DescID) -> bool:
        """    
        Checks if *id* is included in the keyframe selection.
        
        :type id: c4d.DescID
        :param id: The description ID to check.
        :rtype: bool
        :return: **True** if the given *id* is selected, otherwise **False**.
        
        
        """
        ...
    
    def SetKeyframeSelection(self, id: DescID, selection: bool) -> None:
        """    
        Sets the keyframe selection status of *id* to *selection*.
        
        :type id: c4d.DescID
        :param id: The description ID to set.
        :type selection: bool
        :return: **True** to select the key, otherwise id is selected, otherwise **False**.
        
        
        """
        ...
    
    def TransferGoal(self, dst: BaseList2D, undolink: bool) -> None:
        """    
        | Transfer goals from this object to *dst*.
        | This changes all internal links that point to this object to point to *dst* instead.
        
        :type dst: c4d.BaseList2D
        :param dst: The destination
        :type undolink: bool
        :param undolink: This has to be set to *False*. Private.
        
        
        """
        ...
    
    def GetDataInstance(self) -> BaseContainer:
        """    
        | This method returns the original container of the object.
        | The container is only alive as long as the host object is alive.
        | If you access the container even the host object is dead, Python will raise a **ReferenceError**.
        |
        | The elements of the container are type protected when you set touch them via :meth:`GeListNode.__setitem__`,
        | that means, you can just overwrite an element with a new object when its of the same type. When you want to overwrite the element with another type, you need to delete the previous element
        | with **del(bc[ELEMENT_ID])**, or use the manual **BaseContainer.Set*** methods.
        
        :raise ReferenceError: If the container is dead. The container is just alive as long as the host object is alive. Access to a dead container leads to this error.
        :raise TypeError: When you set an element of the wrong expected type.
        :rtype: c4d.BaseContainer
        :return: The original container reference.
        
        
        """
        ...
    
    def GetData(self) -> BaseContainer:
        """    
        Returns a copy of the object's container.
        
        :rtype: c4d.BaseContainer
        :return: The container reference.
        
        
        """
        ...
    
    def SetData(self, bc: BaseContainer, add: bool) -> BaseContainer:
        """    
        | Sets the object container.
        | By default the contents of *bc* are merged with the existing container.
        | You can control this behavior with *add*.
        
        .. note::
        
        Do not forget to send a :meth:`C4DAtom.Message` if you change any settings.
        
        :type bc: c4d.BaseContainer
        :param bc: The container.
        :type add: bool
        :param add: If this is **True** the values are merged, otherwise the old values are discarded.
        :rtype: c4d.BaseContainer
        :return: The container reference.
        
        
        """
        ...
    
    def GetTypeName(self) -> str:
        """    
        The name of the object category, for example *Phong*, *Spline*, *Bone*, etc.
        
        :rtype: str
        :return: The type name.
        
        
        """
        ...
    
    def SetName(self, name: str) -> None:
        """    
        Set the name of the object.
        
        :type name: str
        :param name: Set the name.
        
        
        """
        ...
    
    def GetName(self) -> str:
        """    
        Returns the name of the object.
        
        :rtype: str
        :return: The name.
        
        
        """
        ...
    
    def GetNLARoot(self) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def Scale(self, scale: float) -> None:
        """    
        Scale the object.
        
        :type scale: float
        :param scale: The size.
        
        
        """
        ...
    
    def Edit(self) -> bool:
        """    
        | Triggers the edit action for this object.
        
        .. note::
        
        | For most types this brings up the node in the attributes manager.
        | Some still show a separate dialog.
        
        :rtype: bool
        :return: **False** if an error occurred, otherwise **True**.
        
        
        """
        ...
    
    def GetBubbleHelp(self) -> str:
        """    
        Returns the bubble help of the object.
        
        :rtype: str
        :return: The bubble help.
        
        
        """
        ...
    
    def AddUserData(self, datadescription: BaseContainer) -> DescID:
        """    
        Allocates a new user data and return its ID. Use :meth:`c4d.GetCustomDataTypeDefault` to create a default container for user data.
        
        .. code-block:: python
        
        import c4d
        
        def AddLongDataType(obj):
        if obj is None: return
        
        bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_LONG) # Create default container
        bc[c4d.DESC_NAME] = "Test"                        # Rename the entry
        
        element = obj.AddUserData(bc)     # Add userdata container
        obj[element] = 30                 # Assign a value
        c4d.EventAdd()                    # Update
        
        .. image:: /_imgs/modules/c4d/baselist2d_userdata.png
        :align: center
        
        :type datadescription: c4d.BaseContainer
        :param datadescription: Settings of the new user data. See :class:`Description <c4d.Description>` for more information on the description IDs.
        :rtype: c4d.DescID
        :return: The description ID. The first level is :data:`c4d.DESCID_DYNAMICSUB`.
        
        
        """
        ...
    
    def RemoveUserData(self, id: Union[int, List[int], DescID]) -> bool:
        """    
        Removes a userdata element. There are several ways how to delete a user data.
        
        .. note:
        
        The ID for a user data entry starts with the value **1**, not **0**.
        
        This function supports several types to identify a user data entry.
        
        .. code-block:: python
        
        obj.RemoveUserData(1)  # removes the first user data
        obj.RemoveUserData([c4d.ID_USERDATA, 1])
        obj.RemoveUserData(c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA), c4d.DescLevel(1)))
        
        :type id: Union[int, List[int], c4d.DescID]
        :param id: The id of the userdata.
        :rtype: bool
        :return: **True** if the userdata is removed, otherwise **False**.
        
        
        """
        ...
    
    def GetUserDataContainer(self) -> None:
        """    
        Browse through the user data container sequence.
        
        .. code-block:: python
        
        for id, bc in op.GetUserDataContainer():
        print id, bc
        
        :rtype: list[(:class:`DescID <c4d.DescID>`, :class:`BaseContainer <c4d.BaseContainer>`),]
        :return: A list of tuples with the :class:`Description <c4d.Description>` ID and container for each user data.
        
        
        """
        ...
    
    def SetUserDataContainer(self, descid: DescID, datadescription: BaseContainer) -> bool:
        """    
        Insert a new user data with the specified ID.
        
        :type descid: c4d.DescID
        :param descid: ID of the new user data.
        :type datadescription: c4d.BaseContainer
        :param datadescription: Settings to the new user data. See :class:`Description <c4d.Description>` for more information on the description IDs.
        :rtype: **True** if the user data was inserted, otherwise *False*.
        
        
        """
        ...
    

class BaseMaterial(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Initialize a new :class:`BaseMaterial <c4d.BaseMaterial>` in memory.
        
        :type type: int
        :param type: The material type : :doc:`/types/materials`.
        :rtype: c4d.BaseMaterial
        :return: The new material.
        
        
        """
        ...
    
    def Compare(self, snd: BaseMaterial) -> bool:
        """    
        Check if the materials are identical.
        
        .. note::
        
        Only the name of the compared materials can be different.
        
        :type snd: c4d.BaseMaterial
        :param snd: The material to compare with.
        :rtype: bool
        :return: **True** if the materials contents are the same, otherwise **False**.
        
        
        """
        ...
    
    def GetPreview(self, flags: int) -> BaseBitmap:
        """    
        Retrieves the preview picture of the material.
        
        :type flags: int
        :param flags: Currently not used.
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The preview picture or **None** if it has not been calculated.
        
        
        """
        ...
    
    def GetAverageColor(self, channel: Optional[int] = ...) -> Vector:
        """    
        Returns an average color for the material, based on the material preview.
        
        :type channel: int
        :param channel: An optional specific channel to get the average for.
        
        .. include:: /consts/CHANNEL.rst
        :start-line: 3
        
        :rtype: c4d.Vector
        :return: Average color.
        
        
        """
        ...
    
    def Update(self, preview: bool, rttm: bool) -> None:
        """    
        Recalculates the material's thumbnail and updates internal values.
        
        .. note::
        
        | Recalculating the thumbnail/RTTM image is time intensive.
        | It only needs to be done if you want to let the user view the change.
        | The calculations are done asynchronously.
        
        :type preview: bool
        :param preview: If this value is **True** then the preview thumbnail is updated.
        :type rttm: bool
        :param rttm: If this value is **True** then the real time texture map of the material will be recalculated.
        
        
        """
        ...
    
    def GetRenderInfo(self) -> int:
        """    
        Retrieves information about what the material requires from the raytracer and what it will return.
        
        :rtype: int
        :return: The return values are:
        
        .. include:: /consts/VOLUMEINFO.rst
        :start-line: 3
        
        
        """
        ...
    

class Material(BaseMaterial):
    def __init__(self) -> None:
        """    
        :rtype: c4d.Material
        :return: The new material.
        
        
        """
        ...
    
    def GetChannelState(self, channel: int) -> bool:
        """    
        Get the state of a channel (if it is enabled or disabled).
        
        :type channel: int
        :param channel: The type of channel:
        
        .. include:: /consts/CHANNEL.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the channel is enabled.
        
        
        """
        ...
    
    def SetChannelState(self, channel: int, state: bool) -> None:
        """    
        Set the state of a channel (if it is enabled or disabled).
        
        :type channel: int
        :param channel: The type of channel to change:
        
        .. include:: /consts/CHANNEL.rst
        :start-line: 3
        
        :type state: bool
        :param state: **True** to enable the channel.
        
        
        """
        ...
    
    def AddReflectionLayer(self) -> ReflectionLayer:
        """    
        Adds a reflection/specular layer.
        
        .. versionadded:: R17.032
        
        :rtype: c4d.ReflectionLayer
        :return: The added reflection/specular layer.
        
        
        """
        ...
    
    def GetReflectionLayerID(self, id: int) -> ReflectionLayer:
        """    
        Retrieves a reflection/specular layer by ID.
        
        .. versionadded:: R17.032
        
        :type id: int
        :param id: The layer ID.
        :rtype: c4d.ReflectionLayer
        :return: The reflection/specular layer.
        
        
        """
        ...
    
    def GetReflectionLayerIndex(self, index: int) -> ReflectionLayer:
        """    
        Retrieves a reflection/specular layer by index.
        
        .. versionadded:: R17.032
        
        :type index: int
        :param index: The layer index.
        :rtype: c4d.ReflectionLayer
        :return: The reflection/specular layer.
        
        
        """
        ...
    
    def GetReflectionLayerTrans(self) -> ReflectionLayer:
        """    
        Retrieves the transparency layer.
        
        .. versionadded:: R17.032
        
        :rtype: c4d.ReflectionLayer
        :return: The transparency layer, or **None** if not available.
        
        
        """
        ...
    
    def GetReflectionLayerCount(self) -> int:
        """    
        Retrieves the number of reflection/specular layers.
        
        .. versionadded:: R17.032
        
        :rtype: int
        :return: The reflection/specular layers' count.
        
        
        """
        ...
    
    def RemoveReflectionLayerID(self, id: int) -> None:
        """    
        Removes a reflection/specular layer by ID.
        
        .. versionadded:: R17.032
        
        :type id: int
        :param id: The layer ID.
        
        
        """
        ...
    
    def RemoveReflectionLayerIndex(self, index: int) -> None:
        """    
        Removes a reflection/specular layer by index.
        
        .. versionadded:: R17.032
        
        :type index: int
        :param index: The layer index.
        
        
        """
        ...
    
    def RemoveReflectionAllLayers(self) -> None:
        """    
        Deletes all reflection/specular layers.
        
        .. versionadded:: R17.032
        
        
        """
        ...
    
    def GetAllReflectionShaders(self) -> None:
        """    
        Retrieves all the reflection/specular shaders.
        
        .. versionadded:: R17.032
        
        :rtype: list of :class:`BaseShader <c4d.BaseShader>`
        :return: The reflection/specular shaders.
        
        
        """
        ...
    
    def GetReflectionPrimaryLayers(self) -> Tuple[int, int]:
        """    
        Retrieves the indices to the primary reflection and specular layers (can be -1 for empty).
        
        .. versionadded:: R17.032
        
        :rtype: tuple(int, int)
        :return: The most significant reflection and specular layers.
        
        
        """
        ...
    

class BaseObject(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Initialize a new :class:`BaseObject <c4d.BaseObject>` in memory.
        
        :type type: int
        :param type: The object type : :doc:`/types/objects`.
        :rtype: c4d.BaseObject
        :return: The new base object.
        
        
        """
        ...
    
    def GetAbsPos(self) -> Vector:
        """    
        Returns the absolute position of the object. These will be absolute local coordinates within its parent object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The absolute object position.
        
        
        """
        ...
    
    def SetAbsPos(self, v: Vector) -> None:
        """    
        Sets the absolute local position of the object within its parent. If the object has no parent then these will be world coordinates.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The absolute object position.
        
        
        """
        ...
    
    def GetAbsScale(self) -> Vector:
        """    
        Returns the absolute scale of the object. These will be relative to the objects parent if it has one.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The absolute object scale.
        
        
        """
        ...
    
    def SetAbsScale(self, v: Vector) -> None:
        """    
        Sets the absolute scale of the object relative to its parent object if it has one.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The absolute object scale.
        
        
        """
        ...
    
    def GetAbsRot(self) -> Vector:
        """    
        Returns the absolute HPB rotation of the object relative to any parent object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The absolute object rotation.
        
        
        """
        ...
    
    def SetAbsRot(self, v: Vector) -> None:
        """    
        Sets the absolute HPB rotation of the object relative to any parent object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The absolute object rotation.
        
        
        """
        ...
    
    def GetFrozenPos(self) -> Vector:
        """    
        Returns the frozen position of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The frozen object position.
        
        
        """
        ...
    
    def SetFrozenPos(self, v: Vector) -> None:
        """    
        Sets the frozen position of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The frozen object position.
        
        
        """
        ...
    
    def GetFrozenScale(self) -> Vector:
        """    
        Returns the frozen scale of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The frozen object scale.
        
        
        """
        ...
    
    def SetFrozenScale(self, v: Vector) -> None:
        """    
        Sets the frozen scale of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The frozen object scale.
        
        
        """
        ...
    
    def GetFrozenRot(self) -> Vector:
        """    
        Returns the frozen HPB rotation of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The frozen object rotation.
        
        
        """
        ...
    
    def SetFrozenRot(self, v: Vector) -> None:
        """    
        Sets the frozen HPB rotation of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The frozen object rotation.
        
        
        """
        ...
    
    def GetRelPos(self) -> Vector:
        """    
        Returns the relative position of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The relative object position.
        
        
        """
        ...
    
    def SetRelPos(self, v: Vector) -> None:
        """    
        Set the relative position of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The relative object position.
        
        
        """
        ...
    
    def GetRelScale(self) -> Vector:
        """    
        Returns the relative scale of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The relative object scale.
        
        
        """
        ...
    
    def SetRelScale(self, v: Vector) -> None:
        """    
        Sets the relative scale of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The relative object scale.
        
        
        """
        ...
    
    def GetRelRot(self) -> Vector:
        """    
        Returns the relative HPB rotation of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Vector
        :return: The relative object rotation.
        
        
        """
        ...
    
    def SetRelRot(self, v: Vector) -> None:
        """    
        Sets the relative HPB rotation of the object.
        
        .. seealso::
        
        See also :ref:`freeze_transformations`.
        
        :type v: c4d.Vector
        :param v: The relative object rotation.
        
        
        """
        ...
    
    def GetMl(self) -> Matrix:
        """    
        Get the local matrix that represents the objects position, scale and rotation.
        
        :rtype: c4d.Matrix
        :return: The object's local matrix.
        
        
        """
        ...
    
    def SetMl(self, m: Matrix) -> None:
        """    
        Set the local matrix that represents the objects position, scale and rotation.
        
        :type m: c4d.Matrix
        :param m: The object's new local matrix.
        
        
        """
        ...
    
    def GetFrozenMln(self, m: Matrix) -> None:
        """    
        Returns the frozen and normalized matrix of the object. See also :ref:`freeze_transformations`.
        
        :type m: c4d.Matrix
        :param m: The object's frozen and normalized matrix.
        
        
        """
        ...
    
    def GetRelMln(self) -> Matrix:
        """    
        Returns the relative and normalized matrix of the object. See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Matrix
        :return: The object's relative and normalized matrix.
        
        
        """
        ...
    
    def GetRelMl(self) -> Matrix:
        """    
        Returns the relative matrix of the object. See also :ref:`freeze_transformations`.
        
        :rtype: c4d.Matrix
        :return: The object's relative matrix.
        
        
        """
        ...
    
    def SetRelMl(self, m: Matrix) -> None:
        """    
        Sets the relative matrix of the object. See also :ref:`freeze_transformations`.
        
        :type m: c4d.Matrix
        :param m: The object's new relative matrix.
        
        
        """
        ...
    
    def GetMg(self) -> Matrix:
        """    
        Get the world (global) matrix that represents the objects position, scale and rotation.
        
        .. note::
        
        | This will only work if the object is attached to a document.
        | Virtual objects in caches and deform caches are not attached to a document, so this function cannot be used for those objects.
        
        :rtype: c4d.Matrix
        :return: The object's world matrix.
        
        
        """
        ...
    
    def SetMg(self, m: Matrix) -> None:
        """    
        Set the world (global) matrix that represents the objects position, scale and rotation.
        
        :type m: c4d.Matrix
        :param m: The object's new world matrix.
        
        
        """
        ...
    
    def GetMln(self) -> Matrix:
        """    
        Get the local normalized matrix that represents the objects position, scale and rotation.
        
        :rtype: c4d.Matrix
        :return: The object's normalized local matrix.
        
        
        """
        ...
    
    def GetMgn(self) -> Matrix:
        """    
        Get the global normalized matrix that represents the objects position, scale and rotation.
        
        :rtype: c4d.Matrix
        :return: The object's normalized world matrix.
        
        
        """
        ...
    
    def GetUpMg(self) -> Matrix:
        """    
        | Get the global matrix of the parent object that represents the objects position, scale and rotation.
        | If the object has no parent object then this matrix will be a unit matrix.
        
        :rtype: c4d.Matrix
        :return: The parent object's world matrix.
        
        
        """
        ...
    
    def CopyMatrixTo(self, dst: BaseObject) -> None:
        """    
        Copy the matrix to another object.
        
        :type dst: c4d.BaseObject
        :param dst: The destintation object.
        
        
        """
        ...
    
    def GetMp(self) -> Vector:
        """    
        Bounding box center (vector), in local space.
        
        :rtype: c4d.Vector
        :return: The bounding box center.
        
        
        """
        ...
    
    def GetRad(self) -> Vector:
        """    
        This is the bounding box radius (x/y/z) of the object, this works for all objects and is faster than manually finding the bounds of even polygon objects, the radius is internally cached.
        
        :rtype: c4d.Vector
        :return: The bounding box width, height and depth.
        
        
        """
        ...
    
    def GetEditorMode(self) -> int:
        """    
        Returns the state of the editor dot for this object.
        
        :rtype: int
        :return: The editor mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetEditorMode(self, mode: int) -> None:
        """    
        Set the state of the editor dot for this object.
        
        :type mode: int
        :param mode: The editor mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetRenderMode(self) -> int:
        """    
        Returns the state of the render dot for this object.
        
        :rtype: int
        :return: The render mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetRenderMode(self, mode: int) -> None:
        """    
        Set the render state for this object.
        
        :type mode: int
        :param mode: The render mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetTag(self, type: int, nr: int) -> BaseTag:
        """    
        Get a tag of a certain type associated with this object.
        
        :type type: int
        :param type: The type of tag to fetch from the object. See :doc:`/types/tags`.
        :type nr: int
        :param nr: The starting tag index to find of this type.
        :rtype: c4d.BaseTag
        :return: The requested tag, or **None** if no tags of the requested type are available.
        
        .. note::
        
        If you request a specific number that is not available then **None** will be returned even if there is a tag of that type with a different index.
        
        
        """
        ...
    
    def KillTag(self, type: int, nr: int) -> None:
        """    
        Removes a tag from the object and free its resources.
        
        :type type: int
        :param type: The type of tag to fetch from the object. See :doc:`/types/tags`.
        :type nr: int
        :param nr: The starting tag index to find of this type.
        
        
        """
        ...
    
    def GetRealSpline(self) -> SplineObject:
        """    
        | Get a real spline representation of a primitive spline object.
        | This can for example be used to calculate the length of the spline.
        | If the object is a real spline it returns this. Otherwise **None**.
        
        .. note::
        
        | The matrix of the returned object must not be used.
        | Use the matrix of the original primitive spline object instead.
        
        :rtype: c4d.SplineObject
        :return: The created spline object.
        
        .. warning::
        
        | The returned object is owned by the host object and therefore should be cloned when inserted somewhere else.
        | Ignoring this would lead to a crash if the original object is deleted.
        
        Here is how to safely insert the real spline representation of a primitive spline object.
        
        .. code-block:: python
        
        import c4d
        
        def main():
        realSpline = op.GetRealSpline()               # Active object is a primitive spline object
        if realSpline is not None:
        doc.InsertObject(realSpline.GetClone())     # Insert the clone of the created spline object in the document
        c4d.EventAdd()
        
        if __name__=='__main__':
        main()
        
        
        """
        ...
    
    def GetVisibility(self, parent: float) -> float:
        """    
        The object's visibility depends upon its parent, if it has no visibility track this will return the parent's visibility which is passed.
        
        .. note::
        
        The range of values are *0.0<=visibility<=1.0*.
        
        .. note::
        
        In the editor only a visibility of *0.0* can be noticed but all other intermediate values are visualized in the renderer only.
        
        :type parent: float
        :param float: The parent objects visibility.
        :rtype: float
        :return: The visibility.
        
        
        """
        ...
    
    def SetDeformMode(self, mode: bool) -> None:
        """    
        Set the state of the deformation/generator tick.
        
        :type mode: bool
        :param mode: **True** to enable the generator/deformer object.
        
        
        """
        ...
    
    def GetDeformMode(self) -> bool:
        """    
        Returns the state of the deformation/generator tick.
        
        :rtype: bool
        :return: **True** if the generator/deformer object is enabled.
        
        
        """
        ...
    
    def GetUniqueIP(self) -> int:
        """    
        Get the ip of the object.
        
        :rtype: int
        :return: The object IP number.
        
        
        """
        ...
    
    def SetUniqueIP(self, ip: int) -> None:
        """    
        Set the ip of the object.
        
        :type ip: int
        :param ip: The object IP number.
        
        
        """
        ...
    
    def CopyTagsTo(self, dest: BaseObject, visible: bool, variable: bool, hierarchical: bool) -> None:
        """    
        Copy the tags of the object to another object.
        
        :type dest: c4d.BaseObject
        :param dest: The destination object.
        :type visible: bool
        :param visible: **True** if the tags must be visible, **False** if it must not be visible or **NOTOK** if it can be either (if this property does not need to be checked).
        :type variable: bool
        :param variable: **True** if the tags must be variable, **False** if it must not be variable or **NOTOK** if it can be either (if this property does not need to be checked).
        :type hierarchical: bool
        :param hierarchical: **True** if the tags must be hierarchical, **False** if it must not be hierarchical or **NOTOK** if it can be either (if this property does not need to be checked).
        :return: **True** if the object's tags were copied successfully, otherwise **False**.
        
        
        """
        ...
    
    def GetFirstTag(self) -> BaseTag:
        """    
        Returns the first tag of the object.
        
        :rtype: c4d.BaseTag
        :return: The first tag of the object, or **None** if the object has no tags.
        
        
        """
        ...
    
    def GetLastTag(self) -> BaseTag:
        """    
        Returns the last tag of the object.
        
        .. versionadded:: R19.024
        
        :rtype: c4d.BaseTag
        :return: The last tag of the object, or **None** if the object has no tags.
        
        
        """
        ...
    
    def GetTags(self) -> None:
        """    
        Returns all tags in a list.
        
        :rtype: list of type :class:`BaseTag <c4d.BaseTag>`
        :return: The list of all tags.
        
        
        """
        ...
    
    def MakeTag(self, x: int, pred: Optional[BaseTag] = ...) -> BaseTag:
        """    
        Create and insert a tag for this object.
        
        :type x: int
        :param x: The type of tag to create. See :doc:`/types/tags`.
        :type pred: c4d.BaseTag
        :param pred: The tag will insert after *pred*.
        :rtype: c4d.BaseTag
        :return: The new tag.
        
        
        """
        ...
    
    def MakeVariableTag(self, x: int, count: int, pred: BaseTag) -> BaseTag:
        """    
        Create a variable tag for this object.
        
        :type x: int
        :param x: The type of tag to create:
        
        .. include:: /types/tags_variable.rst
        :start-line: 3
        
        :type count: int
        :param count: The size of the variable tags data.
        :type pred: c4d.BaseTag
        :param pred: The tag will insert after *pred*.
        :rtype: c4d.BaseTag
        :return: The new tag.
        
        
        """
        ...
    
    def InsertTag(self, tp: BaseTag, pred: Optional[BaseTag] = ...) -> None:
        """    
        Attach a :class:`BaseTag <c4d.BaseTag>` to :class:`BaseObject <c4d.BaseObject>`.
        
        .. warning::
        
        | If the tag type was not registered with **TAG_MULTIPLE**, any existing old tag of same type will be implicitly removed.
        | Any previous reference to the old tag will be invalid afterwards.
        
        :type tp: c4d.BaseTag
        :param tp: The tag which will be attached.
        :type pred: c4d.BaseTag
        :param pred: *tp* will insert after *pred*.
        
        
        """
        ...
    
    def GetTagDataCount(self, type: int) -> int:
        """    
        Get the variable tag data count.
        
        :type type: int
        :param type: The type of tag:
        
        .. include:: /types/tags_variable.rst
        :start-line: 3
        
        :rtype: int
        :return: The number of elements in the variable tag.
        
        
        """
        ...
    
    def IsDirty(self, flags: int) -> bool:
        """    
        Check if the object has been changed since the last time the object was touched.
        
        :type flags: int
        :param flags: The object part to check:
        
        .. include:: /consts/DIRTYFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the object is dirty, otherwise **False**.
        
        
        """
        ...
    
    def SetDirty(self, flags: int) -> None:
        """    
        Check if the object has been changed since the last time the object was touched.
        
        :type flags: int
        :param flags: See parameters at :meth:`IsDirty`.
        
        
        """
        ...
    
    def Touch(self) -> None:
        """    
        Mark object to be used by a generator; automatically resets 'dirty'.
        
        
        """
        ...
    
    def SetPhong(self, on: bool, anglelimit: bool, angle: float) -> bool:
        """    
        Set the phong smoothing for the object.
        
        .. note::
        
        | This function will delete any existing Phong tag.
        | If *on* is set to **True** it will create a new Phong tag.
        
        :type on: bool
        :param on: **False** removes the phong tag from the object.
        :type anglelimit: bool
        :param anglelimit: **True** if *angle* should be used.
        :type angle: float
        :param angle: The phong angle.
        :rtype: bool
        :return: Success of changing the smoothing.
        
        
        """
        ...
    
    def GetIsoparm(self) -> LineObject:
        """    
        Gets the previously built isoparm representation of the object.
        
        .. note::
        
        May return None if the isoparm is not available or is not yet built.
        
        :rtype: c4d.LineObject
        :return: The LineObject representing isoparam.
        
        
        """
        ...
    
    def SetIsoparm(self, l: LineObject) -> None:
        """    
        Sets the isoparm representation of the object.
        
        .. warning::
        
        Must only be called from within :meth:`ObjectData.GetVirtualObjects()` of a generator object.
        
        :type l: c4d.LineObject
        :param l: The isoparm representation of the object to set.
        
        
        """
        ...
    
    def GetDeformCache(self) -> BaseObject:
        """    
        | Gets the previously built cache that has been deformed by an active deformer.
        | It is important to understand the concept how the deformer cache operates.
        | For each object in the hierarchy that generates a polygonal cache a deformer cache could also have been created by an active deformer object.
        
        A simple example will help to see how this works:
        
        .. image:: /_imgs/modules/c4d/baseobject_cache_arraycube1.png
        
        | Take the simple hierarchy shown above, the array generator object creates a virtual hierarchy in the cache, this can be retrieved using :meth:`GetCache`.
        | This hierarchy is:
        
        .. image:: /_imgs/modules/c4d/baseobject_cache_arraycube2.png
        
        From each of the Cube objects a further cache is generated, this time polygonal:
        
        .. image:: /_imgs/modules/c4d/baseobject_cache_arraycube3.png
        
        From these the deformer object generates a deformed polygon cache:
        
        .. image:: /_imgs/modules/c4d/baseobject_cache_arraycube4.png
        
        So the final hierarchy is:
        
        .. image:: /_imgs/modules/c4d/baseobject_cache_arraycube5.png
        
        | When a deformer becomes active every object/cache object gets a deform cache (if it was a polygonal object).
        | The deformer cache is always polygonal and is only ever a single object.
        
        .. note::
        
        | The caches are always built after all plugins and expressions have been called.
        | If the virtual objects have to be accessed to obtain a polygonal based object it is generally advised to call :func:`SendModelingCommand() <c4d.utils.SendModelingCommand>` with **MCOMMAND_CURRENTSTATETOOBJECT**.
        | This will rebuild the cache for the passed object if needed, and then clone the polygonal objects.
        
        :rtype: c4d.BaseObject
        :return: The objects previously built deformed cache. May return **None** if the cache is not available or is not yet built.
        
        
        """
        ...
    
    def GetCache(self, hh: Any) -> BaseObject:
        """    
        Get the object from the previously built cache.
        
        .. note::
        
        | Situations can be quite complex in Cinema 4D. For instance :meth:`GetCache` could return a list of objects.
        | For example the default Sweep Generator internally has some built-in caches for the sweep surface and for the caps.
        | The following helper routine can be used to make things easier. It browses through this rather complex hierarchy of objects and caches recursively
        
        .. code-block:: python
        
        def DoRecursion(op):
        tp = op.GetDeformCache()
        if tp is not None:
        DoRecursion(tp)
        else:
        tp = op.GetCache()
        if tp is not None:
        DoRecursion(tp)
        else:
        if not op.GetBit(c4d.BIT_CONTROLOBJECT):
        if op.IsInstanceOf(c4d.Opolygon):
        ...
        
        tp = op.GetDown()
        while tp is not None:
        DoRecursion(tp)
        tp = tp.GetNext()
        
        .. warning::
        
        | Use the above routine only if the caches are already built.
        | It is for instance not safe to use it in a command plugin since the user can have stopped the scene redraw and the building of caches.
        
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | An optional hierarchy helper for the operation. Only for some special cases a hierarchy help must be passed.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()`.
        
        :rtype: c4d.BaseObject
        :return: The object's previously built cache. May return **None** if the cache is not available or is not yet built.
        
        
        """
        ...
    
    def GetCacheParent(self) -> BaseObject:
        """    
        | A cache/deform object has no :meth:`GetUp <GeListNode.GetUp>` link.
        | Instead this method can be called to detect the cache building parent.
        
        :rtype: c4d.BaseObject
        :return: The cache parent or **None**.
        
        
        """
        ...
    
    def CheckCache(self, hh: Any) -> bool:
        """    
        | Check if cache is built, if it matches the requirements (polygonized/isoparm, level of detail etc.).
        | It returns the dirty status of the cache.
        
        .. note::
        
        This function must only be called from within :meth:`ObjectData.GetVirtualObjects`/`main()` of a generator object.
        
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()`.
        
        :rtype: bool
        :return: **True** if the cache is dirty, **False** if it is valid.
        
        
        """
        ...
    
    def GetHighlightHandle(self, bd: BaseDraw) -> int:
        """    
        | Checks if a highlight handle has been hit, by returning the ID previously returned by :meth:`ObjectData.DetectHandle`.
        | The handle can then be drawn in the highlight mode.
        
        :type bd: c4d.BaseDraw
        :param bd: A base draw.
        :rtype: int
        :return: The handle ID.
        
        
        """
        ...
    
    def NewDependenceList(self) -> None:
        """    
        Start a new dependence list. These enable you to keep track of changes made to any children.
        
        .. note::
        
        The object must be children of your object.
        
        
        """
        ...
    
    def CompareDependenceList(self) -> bool:
        """    
        Compares if anything in the dependence list has changed.
        
        :rtype: bool
        :return: **True** if the list has not changed (are the same).
        
        
        """
        ...
    
    def AddDependence(self, hh: Any, op: BaseObject, dirtyflags: int) -> Any:
        """    
        | Add a child object to the dependence list.
        | Usually this will be child objects that are used by a generator object.
        
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()` function.
        
        :type op: c4d.BaseObject
        :param op: The child object to add to the dependence list.
        
        :type dirtyflags: int
        :param dirtyflags:
        
        .. versionadded:: R19.024
        
        The dirty flags stored within the dependence list:
        
        .. include:: /consts/DIRTYFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def TouchDependenceList(self) -> None:
        """    
        Mark all the objects in the dependence list that they will be replaced by the generator.
        
        
        """
        ...
    
    def SearchHierarchy(self, op: BaseObject) -> bool:
        """    
        Check if the object is a child of *op*.
        
        :type op: c4d.BaseObject
        :param op: Check within this object's hierarchy.
        :rtype: bool
        :return: **True** if the object is a child of op, otherwise **False**.
        
        
        """
        ...
    
    def GetAndCheckHierarchyClone(self, hh: Any, op: BaseObject, flags: int, allchildren: bool, dirty: bool, trans: AliasTrans) -> Any:
        """    
        | Check and generate a clone of the child objects of a parent generator.
        | This is similar to :meth:`GetHierarchyClone` except that it will check if the hierarchy is dirty and if not it will not need to generate a new clone.
        
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()` function.
        
        :type op: c4d.BaseObject
        :param op: The object to start the clone from, usually the first child of the parent object.
        :type flags: int
        :param flags: The flags for the generation of the cloned chain, the values are:
        
        .. include:: /consts/HIERARCHYCLONEFLAGS.rst
        :start-line: 3
        
        :type allchildren: bool
        :param allchildren: **True** if all children should be used in the check.
        :type dirty: bool
        :param dirty:
        
        .. versionadded:: R18.057
        
        Has to be set to **None** (or left unset) for the cloning to take place. Set to **True** if some part of the child objects in the chain has changed, or **False** if nothing has changed.
        
        :type trans: c4d.AliasTrans
        :param trans:
        
        .. versionadded:: R18.057
        
        An optional alias translator for the operation.
        
        :rtype: dict{**clone**: :class:`BaseObject <c4d.BaseObject>`, **dirty**: bool}
        :return: The cloned object and a dirty flag: **True** if some part of the child objects in the chain has changed, or **False** if nothing has changed.
        
        
        """
        ...
    
    def GetHierarchyClone(self, hh: Any, op: BaseObject, flags: int, dirty: bool, trans: AliasTrans, dirtyflags: int) -> Any:
        """    
        Generate a clone of the child objects of a parent generator.
        
        | The result returned by :meth:`GetAndCheckHierarchyClone` will be a chain of objects with various types. Passing *HIERARCHYCLONEFLAGS_ASLINE* e.g. will force all splines to be converted, but not every object in the chain will be of type *Oline*.
        | Some objects like :class:`PolygonObject <c4d.PolygonObject>` cannot be converted, also there are *Onull*.
        
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()` function.
        
        :type op: c4d.BaseObject
        :param op: The object to start the clone from, usually the parent object itself.
        :type flags: int
        :param flags: The flags for the generation of the cloned chain, the values are:
        
        .. include:: /consts/HIERARCHYCLONEFLAGS.rst
        :start-line: 3
        
        :type dirty: bool
        :param dirty:
        
        .. versionadded:: R18.057
        
        Has to be set to **None** (or left unset) for the cloning to take place. Set to **True** if some part of the child objects in the chain has changed, or **False** if nothing has changed.
        
        :type trans: c4d.AliasTrans
        :param trans:
        
        .. versionadded:: R18.057
        
        An optional alias translator for the operation.
        
        :type dirtyflags: int
        :param dirtyflags:
        
        .. versionadded:: R19.024
        
        The dirty flags stored within the dependence list:
        
        .. include:: /consts/DIRTYFLAGS.rst
        :start-line: 3
        
        :rtype: dict{**clone**: :class:`BaseObject <c4d.BaseObject>`, **dirty**: bool}
        :return: The cloned object and a dirty flag: **True** if some part of the child objects in the chain has changed, or **False** if nothing has changed.
        
        
        """
        ...
    
    def SetRotationOrder(self, order: int) -> None:
        """    
        Sets the rotation order of the object.
        
        .. versionadded:: R14.014
        
        :type order: int
        :param order: The new rotation order:
        
        .. include:: /consts/ROTATIONORDER.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetRotationOrder(self) -> int:
        """    
        Gets the rotation order of the object.
        
        .. versionadded:: R14.014
        
        :rtype: int
        :return: The rotation order:
        
        .. include:: /consts/ROTATIONORDER.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetGUID(self) -> int:
        """    
        | Returns a unique ID for any object in a document.
        | This works for generated objects in a cache (e.g. clones generated by a MoGraph cloner) and also for 'real' objects in the document (this is special, because :meth:`GetUniqueIP` does not do this).
        
        .. versionadded:: R14.014
        
        .. note::
        
        The ID generation for cache objects is based on :meth:`GetUniqueIP`, so if two cache objects have the same IP, they will probably also get the same GUID (unless they are point objects or polygon objects with different point or poly count).
        
        .. note::
        
        The ID generation for 'real' objects is based on the object's marker, so if an object has no marker it will not return a GUID.
        
        :rtype: long
        :return: A checksum for the object.
        
        
        """
        ...
    
    def SetQuaternionRotationMode(self, active: bool, undo: bool) -> None:
        """    
        Sets the quaternion rotation mode of the object.
        
        .. versionadded:: R18.020
        
        :type active: bool
        :param active: Enable/Disable the quaternion rotation mode for the object.
        :type undo: bool
        :param undo:
        
        | Add undo for the change of quaternion rotation mode.
        | The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        
        """
        ...
    
    def IsQuaternionRotationMode(self) -> bool:
        """    
        Checks if object rotation is interpolated in quaternion mode.
        
        .. versionadded:: R18.020
        
        :rtype: bool
        :return: **True** if rotation interpolation is quaternion, otherwise **False**.
        
        
        """
        ...
    
    def SynchronizeVectorTrackKeys(self, vectorTrackID: int, bUndo: Any, startRange: Optional[BaseTime] = ..., endRange: Optional[BaseTime] = ...) -> bool:
        """    
        Makes sure that the track Curves components are synchronized (keys on each component).
        
        If a component track is found, the other track components will be synchronized.
        
        .. versionadded:: R18.020
        
        :type vectorTrackID: int
        :param vectorTrackID: ID of the vector track to synchronize.
        :type undo: int
        :param undo: Add undo to value changed (need to manage start and end externally).
        :type startRange: c4d.BaseTime
        :param startRange: Optionally start operation at given time.
        :type endRange: c4d.BaseTime
        :param endRange: Optionally end operation at given time.
        :rtype: bool
        :return: **True** if track synchronization was successful, otherwise **False**.
        
        
        """
        ...
    
    def FindBestEulerAngle(self, rotationTrackID: int, adjustTangent: bool, undo: int, startRange: Optional[BaseTime] = ..., endRange: Optional[BaseTime] = ...) -> bool:
        """    
        Tries to find the best Euler angle according to the previous key.
        
        .. note::
        
        The object must have keys on each component.
        
        .. versionadded:: R18.020
        
        :type rotationTrackID: int
        :param rotationTrackID: Rotation Track ID to manage (relative, global, absolute, frozen).
        :type adjustTangent: bool
        :param adjustTangent: Try to adjust the tangent with new value, if **False** auto is used.
        :type undo: int
        :param undo: Add undo to value changed (need to manage start and end externally).
        :type startRange: c4d.BaseTime
        :param startRange: Optionally start operation at given time.
        :type endRange: c4d.BaseTime
        :param endRange: Optionally end operation at given time.
        :rtype: bool
        :return: **True** if rotation synchronization was successful, otherwise **False**.
        
        
        """
        ...
    
    def EvaluateSynchronizedRotation(self, time: BaseTime, flags: BaseTime, applyRotation: bool) -> None:
        """    
        Forces an evaluation of all rotation tracks and considers quaternion interpolation.
        
        .. versionadded:: R18.020
        
        :type time: c4d.BaseTime
        :param time: The evaluation time.
        :type flags: c4d.BaseTime
        :param flags: The animate flags:
        
        .. include:: /consts/ANIMATEFLAGS.rst
        :start-line: 3
        
        :type applyRotation: bool
        :param applyRotation:
        
        .. versionadded:: R18.039
        
        Pass **False** to return rotation result instead of updating attributes.
        
        :rtype: bool or tuple(bool, :class:`c4d.Vector`)
        :return:
        
        | If *applyRotation* is **True**, a bool giving the evaluation result.
        | If *applyRotation* is **False**, a tuple with the following information:
        | bool: **True** if evaluation was a success, otherwise **False**.
        | :class:`c4d.Vector`: The rotation vector result.
        
        
        """
        ...
    
    def GetVectorTracks(self, id: DescID) -> None:
        """    
        Returns each component track for the given *id*.
        
        .. versionadded:: R18.020
        
        :type id: c4d.DescID
        :param id: ID of desired vector.
        :rtype: tuple(bool, :class:`c4d.CTrack`, :class:`c4d.CTrack`, :class:`c4d.CTrack`)
        :return: A tuple with the following information:
        
        | bool: **True** if successful, otherwise **False**.
        | :class:`c4d.CTrack`: The X track of vector, or **None** if not found.
        | :class:`c4d.CTrack`: The Y track of vector, or **None** if not found.
        | :class:`c4d.CTrack`: The Z track of vector, or **None** if not found.
        
        
        """
        ...
    
    def GetVectorCurves(self, curveToSearch: CCurve) -> None:
        """    
        Returns each component curve for the given curve.
        
        .. versionadded:: R18.020
        
        :type curveToSearch: c4d.CCurve
        :param curveToSearch: The curve component of desired vector.
        :rtype: tuple(bool, :class:`c4d.CCurve`, :class:`c4d.CCurve`, :class:`c4d.CCurve`)
        :return: A tuple with the following information:
        
        | bool: **True** if successful, otherwise **False**.
        | :class:`c4d.CCurve`: The X curve of vector, or **None** if not found.
        | :class:`c4d.CCurve`: The Y curve of vector, or **None** if not found.
        | :class:`c4d.CCurve`: The Z curve of vector, or **None** if not found.
        
        
        """
        ...
    
    def GetModelingAxis(self, doc: BaseDocument) -> Matrix:
        """    
        Gets the internal matrix for the modeling axis.
        
        .. versionadded:: R19
        
        .. note::
        
        To access the axis type, and other axis options, use the IDs defined in `toolmodelingaxis.h`.
        
        .. seealso::
        
        :meth:`BaseObject.SetModelingAxis`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: c4d.Matrix
        :return: The modeling axis.
        
        
        """
        ...
    
    def SetModelingAxis(self, m: Matrix) -> None:
        """    
        Sets the internal matrix for the modeling axis.
        
        .. versionadded:: R19
        
        .. note::
        
        | To access the axis type, and other axis options, use the IDs in `toolmodelingaxis.h`.
        | Here is a code sample:
        
        .. code-block:: python
        
        import c4d
        
        def SetToolData(doc, toolID, paramID, data):
        plug = c4d.plugins.FindPlugin(toolID, c4d.PLUGINTYPE_TOOL)
        if plug is None:
        return
        
        plug[paramID] = data
        SetToolData(doc, c4d.ID_MODELING_LIVESELECTION, c4d.MDATA_AXIS_MODE, c4d.MDATA_AXIS_MODE_FREE)
        
        :type m: c4d.Matrix
        :param m: The new modeling axis to set.
        
        
        """
        ...
    
    def GetChildren(self) -> List[BaseObject]:
        ...
    

class CameraObject(BaseObject):
    def __init__(self) -> None:
        """    
        :rtype: c4d.CameraObject
        :return: The new camera.
        
        
        """
        ...
    
    def GetProjection(self) -> int:
        """    
        Get the camera projection.
        
        :rtype: int
        :return: The projection. See :file:`Ocamera.h` for values.
        
        
        """
        ...
    
    def GetFocus(self) -> float:
        """    
        Get the focus of the camera.
        
        :rtype: float
        :return: The focus.
        
        
        """
        ...
    
    def GetZoom(self) -> float:
        """    
        Get the zoom of the camera.
        
        :rtype: float
        :return: The zoom.
        
        
        """
        ...
    
    def GetOffset(self) -> Vector:
        """    
        Return the offset.
        
        :rtype: c4d.Vector
        :return: The offset.
        
        
        """
        ...
    
    def GetAperture(self) -> float:
        """    
        Return the aperture width.
        
        :rtype: float
        :return: The camera's aperture.
        
        
        """
        ...
    
    def SetProjection(self, projection: int) -> None:
        """    
        Set the camera projection.
        
        :type projection: int
        :param projection: The projection. See :file:`Ocamera.h` for values.
        
        
        """
        ...
    
    def SetFocus(self, v: float) -> None:
        """    
        Set the focus of the camera.
        
        :type v: float
        :param v: The focus.
        
        
        """
        ...
    
    def SetZoom(self, zoom: float) -> None:
        """    
        Set the zoom of the camera.
        
        :type zoom: float
        :param zoom: The zoom.
        
        
        """
        ...
    
    def SetOffset(self, offset: Vector) -> None:
        """    
        Set the offset.
        
        :type offset: c4d.Vector
        :param offset: The offset.
        
        
        """
        ...
    
    def SetAperture(self, v: float) -> None:
        """    
        Set the aperture width.
        
        :type v: float
        :param v: The camera's aperture.
        
        
        """
        ...
    
    def StereoGetCameraCount(self, doc: BaseDocument, bd: BaseDraw, rd: RenderData, flags: Optional[int] = ...) -> int:
        """    
        Returns the number of stereoscopic cameras.
        
        .. versionadded:: R19
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :type bd: c4d.BaseDraw
        :param bd: The stereoscopic view.
        :type rd: c4d.documents.RenderData
        :param rd: The stereoscopic render settings.
        :type flags: int
        :param flags: Optional. Currently unused. Set to `0`.
        :rtype: int
        :return: The number of stereoscopic cameras.
        
        
        """
        ...
    
    def StereoGetCameraInfo(self, doc: BaseDocument, bd: BaseDraw, rd: RenderData, n: int, flags: Optional[int] = ...) -> None:
        """    
        Returns the information for a stereoscopic camera.
        
        .. versionadded:: R19
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :type bd: c4d.BaseDraw
        :param bd: The stereoscopic view.
        :type rd: c4d.documents.RenderData
        :param rd: The stereoscopic render settings.
        :type n: int
        :param n: The stereoscopic camera index: `0` <= *n* < :meth:`StereoGetCameraCount`
        :type flags: int
        :param flags: Optional. Currently unused. Set to `0`.
        :rtype: dict{'m': :class:`c4d.Matrix`, 'off_x': float, 'off_y': float, 'name': str}
        :return: A dictionary (**None** if the function failed) with the stereo camera information:
        
        | 'm': Stereoscopic camera matrix.
        | 'off_x': Stereoscopic camera film X offset.
        | 'off_y': Stereoscopic camera film Y offset.
        | 'name': Stereoscopic camera name.
        
        
        """
        ...
    

class VoronoiFracture(BaseObject):
    def __init__(self) -> None:
        """    
        :rtype: c4d.VoronoiFracture
        :return: The new Voronoi fracture object.
        
        
        """
        ...
    
    def GetSourcesCount(self) -> int:
        """    
        Returns the number of elements in the Sources list, including point generators.
        
        :rtype: int
        :return: The number of elements in the Sources list.
        
        
        """
        ...
    
    def GetSource(self, index: int) -> BaseObject:
        """    
        Retrieves the object referenced at the given *index*.
        
        .. note::
        
        If *index* references a point generator that point generator object is returned.
        
        :type index: int
        :param index: The index of the source element to access.
        :rtype: c4d.BaseObject
        :return: The object at the given *index*, or **None** if the method failed.
        
        
        """
        ...
    
    def GetSourceByType(self, type: int, startIndex: int) -> None:
        """    
        Retrieves the object referenced in the Sources list with the given type.
        
        .. note::
        
        If multiple objects with the given *type* exist the first is returned.
        
        :type type: int
        :param type: The type of object to access.
        :type startIndex: int
        :param startIndex: The index to start the search.
        :rtype: tuple(:class:`c4d.BaseObject`, int)
        :return: A tuple with the found source object and its index, or **None** if the method failed.
        
        
        """
        ...
    
    def RemoveSource(self, index: int) -> bool:
        """    
        Removes the source element in the list at the given index.
        
        .. note::
        
        If the index references a point generator it is also deleted from the internal list.
        
        :type index: int
        :param index: The index of the source element to remove.
        :rtype: bool
        :return: **True** if the element was removed successfully, otherwise **False**.
        
        
        """
        ...
    
    def AddPointGenerator(self, type: int, shaderType: int) -> None:
        """    
        Adds a new point generator.
        
        :type type: int
        :param type: The type of point generator, either **ID_POINTCREATOR_CREATORTYPE_DISTRIBUTION** or **ID_POINTCREATOR_CREATORTYPE_SHADER**.
        :type shaderType: int
        :param shaderType: If a Shader generator is created a shader of this type is automatically added to it.
        :rtype: tuple(:class:`c4d.BaseObject`, int)
        :return: A tuple with the added point generator and its index, or **None** if the method failed.
        
        
        """
        ...
    
    def AddSceneObject(self, object: BaseObject) -> Tuple[bool, int]:
        """    
        Adds a valid object from the scene to the Sources list.
        
        :type object: c4d.BaseObject
        :param object: The scene object that should be added.
        :rtype: tuple(bool, int)
        :return: A tuple with the scene object addition state and its index, or **None** if the method failed.
        
        
        """
        ...
    
    def ClearSources(self) -> None:
        """    
        Clears the Sources list and deletes all point generators.
        
        
        """
        ...
    
    def GetSourceSettingsContainerForIndex(self, index: int) -> BaseContainer:
        """    
        Returns the internal container for the settings of an external source input, like a polygon object as point source.
        
        .. versionadded:: R19
        
        .. note::
        
        Allows to change the settings that control for example the distribution of points in the object and the point count.
        
        :type index: int
        :param index: The index of the object in the Sources list.
        :rtype: c4d.BaseContainer
        :return: The container for the source settings if the index fits to an external Source input, otherwise **None**.
        
        
        """
        ...
    
    def GetSourceSettingsContainerForObject(self, object: BaseObject) -> BaseContainer:
        """    
        Returns the internal container for the settings of an external source input, like a polygon object as point source.
        
        .. versionadded:: R19
        
        .. note::
        
        Allows to change the settings that control for example the distribution of points in the object and the point count.
        
        :type object: c4d.BaseObject
        :param object: The external source object in the Sources list.
        :rtype: c4d.BaseContainer
        :return: The container for the source settings if the object is in the Sources list, otherwise **None**.
        
        
        """
        ...
    

class InstanceObject(BaseObject):
    def __init__(self) -> None:
        """    
        Creates an :class:`InstanceObject <c4d.InstanceObject>`.
        
        :rtype: c4d.InstanceObject
        :return: An :class:`InstanceObject <c4d.InstanceObject>` instance.
        
        
        """
        ...
    
    def IsMultiInstance(self) -> bool:
        """    
        Checks if the instance object is in multi-instance mode.
        
        :rtype: bool
        :return: **True** if in multi-instance mode, otherwise **False**.
        
        
        """
        ...
    
    def GetReferenceObject(self, doc: BaseDocument) -> BaseObject:
        """    
        Return the instantiated object.
        
        .. note::
        
        Same as accessing the *INSTANCEOBJECT_LINK* parameter in the object's data container.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document the instance object belongs to.
        :rtype: c4d.BaseObject
        :return: The reference object. **None** if the instance object is unassigned.
        
        
        """
        ...
    
    def SetReferenceObject(self, refObj: BaseObject) -> None:
        """    
        Sets the instantiated object used for the multiple instances.
        
        .. note::
        
        Same as assigning the *INSTANCEOBJECT_LINK* parameter in the object's data container.
        
        :type refObj: c4d.BaseObject
        :param refObj: The reference object to set.
        
        
        """
        ...
    
    def GetInstanceCount(self) -> int:
        """    
        Returns the instance count (number of instances and matrices).
        
        :rtype: int
        :return: The instance count.
        
        
        """
        ...
    
    def GetInstanceMatrix(self, index: int) -> Matrix:
        """    
        Returns the global matrix of the instance at the specified *index*.
        
        :type index: int
        :param index: The instance index.
        :rtype: c4d.Matrix
        :return: The instance matrix.
        
        
        """
        ...
    
    def GetInstanceMatrices(self) -> List[Matrix]:
        """    
        Returns the instance matrices.
        
        :rtype: List[c4d.Matrix]
        :return: The list of instance matrices.
        
        
        """
        ...
    
    def SetInstanceMatrices(self, matrices: List[Matrix]) -> bool:
        """    
        Sets the instance matrices.
        
        .. note::
        
        The size of *matrices* iterable determines the instance count.
        
        :type matrices: Union[List[c4d.Matrix], Tuple[c4d.Matrix]]
        :param matrices: The iterable (list or tuple) for the instance matrices to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetInstanceColor(self, index: int) -> Vector:
        """    
        Returns the color of the instance at the specified *index*.
        
        :type index: int
        :param index: The instance index.
        :rtype: c4d.Vector
        :return: The instance color.
        
        
        """
        ...
    
    def GetInstanceColors(self) -> List[Vector]:
        """    
        Returns the instance colors.
        
        :rtype: List[c4d.Vector]
        :return: The list of instance colors.
        
        
        """
        ...
    
    def SetInstanceColors(self, colors: List[Vector]) -> bool:
        """    
        Sets the instance colors.
        
        :type colors: Union[List[c4d.Vector], Tuple[c4d.Vector]]
        :param colors: The iterable (list or tuple) for the instance colors to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    

class LodObject(BaseObject):
    def __init__(self) -> None:
        """    
        Creates a LOD object.
        
        :rtype: c4d.LodObject
        :return: The new LOD object.
        
        
        """
        ...
    
    def GetCurrentLevel(self) -> int:
        """    
        Queries the current LOD level.
        
        :rtype: int
        :return: The current LOD level index, or **NOTOK**/**-1** in error case.
        
        
        """
        ...
    
    def GetLevelCount(self) -> int:
        """    
        Queries the current number of LOD levels.
        
        :rtype: int
        :return: The current LOD level count, or **NOTOK**/**-1** in error case.
        
        
        """
        ...
    
    def GetShowControlDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the show control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetManualModeObjectListDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the object list for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetSimplifyModeDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the simplify mode for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetDecimateStrengthDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the decimation strength for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetPerObjectControlDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the per object control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetNullDisplayDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the NullObject Display control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetNullRadiusDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the NullObject Radius control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetNullAspectRatioDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the NullObject Aspect Ratio control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetNullOrientationDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the NullObject Orientation control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetDisplayStModeDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the Display Style Mode control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetDisplayShModeDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the Display Shading Mode control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetDisplayBFCDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the Display Backface Culling control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    
    def GetDisplayTexDescID(self, level: int) -> DescID:
        """    
        Calculates the dynamic description ID of the Display Texture control for the passed LOD *level*.
        
        :type level: int
        :param level: The LOD level.
        :rtype: c4d.DescID
        :return: The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
        
        
        """
        ...
    

class PointObject(BaseObject):
    def GetPointH(self) -> BaseSelect:
        """    
        Return the hidden points.
        
        :rtype: c4d.BaseSelect
        :return: The hidden points.
        
        
        """
        ...
    
    def GetPointS(self) -> BaseSelect:
        """    
        Return the selected points.
        
        :rtype: c4d.BaseSelect
        :return: The selected points.
        
        
        """
        ...
    
    def GetPoint(self, id: int) -> Vector:
        """    
        Get the position of a point.
        
        :type id: int
        :param id: The point index.
        :raise IndexError: If the point index *id* is out of range : *0<=id<*:meth:`GetPointCount`.
        :rtype: c4d.Vector
        :return: The position of the point.
        
        
        """
        ...
    
    def SetPoint(self, id: int, pos: Vector) -> None:
        """    
        Set the position of a point.
        
        .. note::
        
        Call :meth:`obj.Message <C4DAtom.Message>` (*c4d.MSG_UPDATE*) after you set all your points to update the object.
        
        :type id: int
        :param id: The point index.
        :raise IndexError: If the point index *id* is out of range : *0<=id<*:meth:`GetPointCount`.
        :type pos: c4d.Vector
        :param pos: The position of the point.
        
        
        """
        ...
    
    def GetAllPoints(self) -> None:
        """    
        Return all point positions.
        
        :rtype: list of :class:`Vector <c4d.Vector>`
        :return: The list of positions.
        
        
        """
        ...
    
    def SetAllPoints(self, p: Any) -> None:
        """    
        | Set all points of the point object.
        | The length of the passed list object must be equal the count of points.
        
        .. note::
        
        Call :meth:`obj.Message <C4DAtom.Message>` (*c4d.MSG_UPDATE*) after you set all your points to update the object.
        
        :type p: list of :class:`Vector <c4d.Vector>`
        :param p: The list of positions.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Return the number of points.
        
        :rtype: int
        :return: The number of points.
        
        
        """
        ...
    
    def CalcVertexMap(self, modifier: BaseObject) -> List[float]:
        """    
        Get an array of vertex weights.
        
        .. versionchanged:: R19.053
        
        Previous name was `CalcVertexmap` (still works for backward compatibility).
        
        :type modifier: c4d.BaseObject
        :param modifier: The modifier object.
        :rtype: list of float
        :return: The list of weights, or **None** if failed.
        
        
        """
        ...
    
    def ResizeObject(self, pcnt: int) -> bool:
        """    
        Changes the number of points in the point object.
        
        :type pcnt: int
        :param pcnt: The new number of points.
        :rtype: bool
        :return: Success of changing the number of points.
        
        
        """
        ...
    

class LineObject(PointObject):
    def __init__(self, pcnt: int, scnt: int) -> None:
        """    
        Creates a :class:`LineObject <c4d.LineObject>`.
        
        :type pcnt: int
        :param pcnt: The point count.
        :type scnt: int
        :param scnt: The segment count.
        :rtype: c4d.LineObject
        :return: A line object.
        
        
        """
        ...
    
    def Triangulate(self, regular: float) -> PolygonObject:
        """    
        Converts the line object into polygons.
        
        :type regular: float
        :param regular: The size of polygons to fill the inside of the line object with. Pass `0.0` to connect the contour with no filling.
        :rtype: c4d.PolygonObject
        :return: The created polygon object.
        
        
        """
        ...
    
    def GetSegmentCount(self) -> int:
        """    
        Gets the number of segments.
        
        :rtype: int
        :return: The number of elements in the segments array.
        
        
        """
        ...
    

class PolygonObject(PointObject):
    def __init__(self, pcnt: int, vcnt: int) -> None:
        """    
        :type pcnt: int
        :param pcnt: Point count.
        :type vcnt: int
        :param vcnt: Polygon count.
        :rtype: c4d.PolygonObject
        :return: The object.
        
        
        """
        ...
    
    def GetPolygonS(self) -> BaseSelect:
        """    
        Return the selected polygons.
        
        :rtype: c4d.BaseSelect
        :return: A reference to the selected polygon structure.
        
        
        """
        ...
    
    def GetPolygonH(self) -> BaseSelect:
        """    
        Return the hidden polygons.
        
        :rtype: c4d.BaseSelect
        :return: A reference to the hidden polygon structure.
        
        
        """
        ...
    
    def GetEdgeS(self) -> BaseSelect:
        """    
        | Get the selected edges.
        | The edges are indexed by `4 * polygon + edge` where polygon is the polygon index and edge is the edge index between `0 and 3`.
        
        .. warning::
        
        | If you change this selection you must make sure that its still valid, so that shared edges have a well-defined selection status.
        | It is safer to use :meth:`SetSelectedEdges`.
        
        :rtype: c4d.BaseSelect
        :return: A reference to the selection of visible edges.
        
        
        """
        ...
    
    def GetEdgeH(self) -> BaseSelect:
        """    
        | Get the hidden edges.
        | The edges are indexed by `4 * polygon + edge` where polygon is the polygon index and edge is the edge index between `0 and 3`.
        
        .. note::
        
        The edges are only hidden within the editor.
        
        .. warning::
        
        | If you change this selection you must make sure that it is still valid, so that shared edges have a well-defined selection status.
        | It is safer to use :meth:`SetSelectedEdges`.
        
        :rtype: c4d.BaseSelect
        :return: A reference to the selection of hidden edges.
        
        
        """
        ...
    
    def SetPolygon(self, id: int, polygon: CPolygon) -> None:
        """    
        Set a polygon.
        
        .. note::
        
        Call :meth:`obj.Message <C4DAtom.Message>` (*c4d.MSG_UPDATE*) after you set all your polygons to update the object.
        
        :type id: int
        :param id: The index.
        :raise IndexError: If the polygon index *id* is out of range : *0<=id<*:meth:`GetPolygonCount`.
        :type polygon: c4d.CPolygon
        :param polygon: The polygon to set at index *id*.
        
        
        """
        ...
    
    def GetPolygon(self, id: int) -> CPolygon:
        """    
        Get a polygon.
        
        :type id: int
        :param id: The index.
        :raise IndexError: If the polygon index *id* is out of range : *0<=id<*:meth:`GetPolygonCount`.
        :rtype: c4d.CPolygon
        :return: The polygon at index *id*.
        
        
        """
        ...
    
    def ResizeObject(self, pcnt: int, vcnt: int) -> bool:
        """    
        | Change the number of points and polygons in the object.
        | If *vcnt* is -1 or not set, the method of :meth:`PointObject.ResizeObject` is used.
        
        :type pcnt: int
        :param pcnt: The new number of points.
        :type vcnt: int
        :param vcnt: The new number of polygons.
        :rtype: bool
        :return: Success of changing the number of points and segments.
        
        
        """
        ...
    
    def GetPhongBreak(self) -> BaseSelect:
        """    
        | Get the phong break edges.
        | The edges are indexed by `4 * polygon + edge` where polygon is the polygon index and edge is the edge index between `0 and 3`.
        
        .. warning::
        
        | If you change this selection you must make sure that its still valid, so that shared edges have a well-defined phong break status.
        | it is safer to use :meth:`SetSelectedEdges`.
        
        :rtype: c4d.BaseSelect
        :return: The phong break.
        
        
        """
        ...
    
    def GetPolygonTranslationMap(self) -> Tuple[int, List[int]]:
        """    
        Gets a translation map from polygon indices to N-gon indices.
        
        :rtype: tuple(int, List[int])
        :return: The number of N-gons (and remaining polygons) and the list of N-gon indices. (`0`, []) if the function failed.
        
        .. versionchanged:: R19.024
        
        Was only returning the list of N-gon indices.
        
        .. note::
        
        | The number of n-gon correspond to all N-gons and all remaining polygons which are not part of any N-gons.
        | The `list` has an amount of entries corresponding to the Cpolygon count of the Polygon Object.
        | Where each number of the `list` correspond to the Cpolygon id and the value to the N-gon this Cpolygon belongs to.
        | An Abstract example [0, 4] means the CPolygon 0 belongs to the N-gon 0 and the CPolygon 1 belongs to the N-gon 4.
        
        
        """
        ...
    
    def GetNGonTranslationMap(self, ngoncnt: int, polymap: List[int]) -> List[int]:
        """    
        Gets a translation map from N-gon indices to polygon indices.
        
        .. versionadded:: R19.024
        
        :type ngoncnt: int
        :param ngoncnt: The number of N-gons. Pass the length of the list returned by :meth:`GetPolygonTranslationMap`, not the value given by :meth:`GetNgonCount`.
        :type polymap: List[int]
        :param polymap: The polygon map. Pass the list returned by :meth:`GetPolygonTranslationMap`, or a similarly formatted array.
        :rtype: list of (List[int])
        :return: The polygon index map if successful, otherwise **None**.
        
        .. note::
        
        | The number of polygons in N-gon `i` is stored in `list[i][0]`.
        | Then the polygon indices are stored in `list[i][j]` where `j` goes from `1` to `list[i][0]`.
        
        
        """
        ...
    
    def GetAllPolygons(self) -> None:
        """    
        Returns all polygons.
        
        :rtype: list of :class:`CPolygon <c4d.CPolygon>`
        :return: A list of copied polygons.
        
        
        """
        ...
    
    def CreatePhongNormals(self) -> List[Vector]:
        """    
        Returns a list with the stored phong normals of the object.
        
        :rtype: list of Vectors or **None**
        :return: The list or **None** if the object has no Phong Tag.
        
        
        """
        ...
    
    def GetPolygonCount(self) -> int:
        """    
        | Returns the count of polygons.
        | Is the fastest way to get the count of polygons.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetPolygonR(self) -> Any:
        """    
        Gets the start of the read-only array of polygons.
        
        .. versionadded:: R18.011
        
        .. note::
        
        | While this function may sound trivial and cheap, internally it is not.
        | For performance reasons, it is not recommended to use this function inside a loop or inside a loop condition.
        
        :rtype: PyCObject
        :return: The start of the read-only polygon array.
        
        
        """
        ...
    
    def GetPolygonW(self) -> Any:
        """    
        Gets the start of the writable array of polygons.
        
        .. versionadded:: R18.011
        
        .. note::
        
        | While this function may sound trivial and cheap, internally it is not.
        | For performance reasons, it is not recommended to use this function inside a loop or inside a loop condition.
        
        :rtype: PyCObject
        :return: The start of the writable polygon array.
        
        
        """
        ...
    
    def GetSelectedEdges(self, e: Neighbor, ltype: int) -> BaseSelect:
        """    
        | Get the selected, hidden or phong break edges.
        | The edges are indexed uniquely by a :class:`Neighbor <c4d.utils.Neighbor>` object, so each edge has a single index.
        
        .. note::
        
        This is a convenience wrapper around :meth:`GetEdgeS`, :meth:`GetEdgeH` and :meth:`GetPhongBreak`.
        
        :type e: c4d.utils.Neighbor
        :param e: The neighbor object with information about the edge topology. Must be initialized with all polygons, i.e. with :meth:`Neighbor.Init`.
        :type ltype: int
        :param ltype: The type of selection to get:
        
        .. include:: /consts/EDGESELECTIONTYPE.rst
        :start-line: 3
        
        :rtype: c4d.BaseSelect
        :return: The selected edges.
        
        
        """
        ...
    
    def SetSelectedEdges(self, e: Neighbor, pSel: BaseSelect, ltype: int) -> bool:
        """    
        | Set the selected, hidden or phong break edges.
        | The edges are indexed uniquely by a :class:`Neighbor <c4d.utils.Neighbor>` object, so each edge has a single index.
        
        .. note::
        
        This is a convenience wrapper around :meth:`GetEdgeS`, :meth:`GetEdgeH` and :meth:`GetPhongBreak`.
        
        :type e: c4d.utils.Neighbor
        :param e: The neighbor object with information about the edge topology. Must be initialized with all polygons, i.e. with :meth:`Neighbor.Init`.
        :type pSel: c4d.BaseSelect
        :param pSel: The edge to select.
        :type ltype: int
        :param ltype: The type of selection to get:
        
        .. include:: /consts/EDGESELECTIONTYPE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the selection succeeded, otherwise **False**.
        
        
        """
        ...
    
    def GetNgonCount(self) -> int:
        """    
        Get the number of N-gons in the object, i.e. the number of polygons with more points than 4.
        
        :rtype: int
        :return: The number of N-gons for this object.
        
        
        """
        ...
    
    def GetSelectedNgons(self, sel: BaseSelect) -> None:
        """    
        Copies the current N-gon selection into sel.
        
        :type sel: c4d.BaseSelect
        :param sel: Assigned the current N-gon selection.
        
        
        """
        ...
    
    def GetHiddenNgons(self, sel: BaseSelect) -> None:
        """    
        Copies the current hidden N-gon selection into *sel*.
        
        :type sel: c4d.BaseSelect
        :param sel: Assigned the current hidden N-gon selection.
        
        
        """
        ...
    
    def ValidateEdgeSelection(self, sel: BaseSelect) -> bool:
        """    
        Deselects all selected edges in *sel* that are N-gon edges.
        
        :type sel: c4d.BaseSelect
        :param sel: The selection to check for N-gon edges.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetEdgeSelection(self, sel: BaseSelect, type: int) -> bool:
        """    
        Deselects all edges in 'sel' that are N-gon edges as specified by type.
        
        :type sel: c4d.BaseSelect
        :param sel: The selection to check for N-gon edges.
        :type type: int
        :param type: The type of selection to check:
        
        .. include:: /consts/EDGESELECTIONTYPE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetNgonEdgesCompact(self) -> List[Any]:
        """    
        | Retrieves a list that contains N-gon edges information for each polygon.
        |
        | The edge compact value is based on the mask `1 << edgeIndex` with `edgeIndex` between `0` - `3` for quads, and `0`, `1`, `3` for triangles.
        | If the value for a polygon is zero then it has no N-gon edge.
        | Otherwise check each edge of the polygon with `edges[polyIndex] & (1 << edgeIndex) == 0` (with `edges` the list of N-gon edges compact values). If the condition is **True** then the edge is a N-gon edge.
        
        :rtype: list
        :return: N-gon edges information list.
        
        
        """
        ...
    
    def GetShadingBreak(self, includeBorderEdges: bool, includeUserBreak: bool, includeUserNormals: bool, userNormalsAngle: Optional[float] = ..., autoNormalsAngle: Optional[float] = ...) -> BaseSelect:
        """    
        | Gets the shading break edges based on neighbor polygons shading edges and a specified angle limit.
        |
        | Border edges can optionally be marked as break edges.
        | Current break edges can optionally be included (merged) in the resulting break edges.
        | Finally, user normal vectors can optionally be considered using a separate angle limit for this purpose.
        
        .. versionadded:: R19
        
        .. note::
        
        The edges are indexed by `4 * polygon + edge` where `polygon` is the polygon index and `edge` is the edge index between `0` and `3`.
        
        :type includeBorderEdges: bool
        :param includeBorderEdges: **True** to mark border edges as break edges, otherwise **False**.
        :type includeUserBreak: bool
        :param includeUserBreak: **True** to include the user break edges (same as obtained with :meth:`GetPhongBreak`), otherwise **False**.
        :type includeUserNormals: bool
        :param includeUserNormals: **True** to consider user normals using the *userNormalAngle* parameter, otherwise **False**.
        :type userNormalsAngle: float
        :param userNormalsAngle: Optional angle limit, in radians, beyond which polygon vertex normals sharing edge vertices create a break edge.
        :type autoNormalsAngle: float
        :param autoNormalsAngle: Optional angle limit, in radians, beyond which polygon normals sharing an edge create a break edge.
        :rtype: c4d.BaseSelect
        :return: The shading break edges.
        
        
        """
        ...
    

class SplineObject(PointObject):
    def __init__(self, pcnt: int, type: int) -> None:
        """    
        :type pcnt: int
        :param pcnt: Point count.
        :type type: int
        :param type: Spline type. Check out :ref:`spline_type`.
        
        .. include:: /consts/SPLINETYPE.rst
        :start-line: 3
        
        :rtype: c4d.SplineObject
        :return: The new object.
        
        
        """
        ...
    
    def GetInterpolationType(self) -> int:
        """    
        Get the type of spline.
        
        :rtype: int
        :return: The type of spline. Check out :ref:`spline_type`.
        
        .. include:: /consts/SPLINETYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsClosed(self) -> bool:
        """    
        Checks if spline is closed.
        
        :rtype: bool
        :return: **True** if the spline is closed.
        
        
        """
        ...
    
    def GetSplinePoint(self, t: float, segment: int) -> Vector:
        """    
        Get the spline point at a position along the given segment.
        
        :type t: float
        :param t: The position *0.0<=t<=1.0* along the segment.
        :type segment: int
        :param segment: The segment.
        :raise IndexError: If the *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: c4d.Vector
        :return: The spline point.
        
        
        """
        ...
    
    def GetSplineTangent(self, t: float, segment: int) -> Vector:
        """    
        Get the spline tangent at a position along the given segment.
        
        :type t: float
        :param t: The position *0.0<=t<=1.0* along the segment.
        :type segment: int
        :param segment: The segment to get the point in.
        :raise IndexError: If the *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: c4d.Vector
        :return: The spline point.
        
        
        """
        ...
    
    def GetSegment(self, id: int) -> None:
        """    
        Returns information about the segment.
        
        .. code-block:: python
        
        segment = spline.GetSegment(0)
        print segment["cnt"], segment["closed"] # int, bool
        
        :type id: int
        :param id: The segment.
        :raise IndexError: If the segment index *id* is out of range : *0<=id<*:meth:`GetSegmentCount`.
        :rtype: dict{**cnt**: int, **closed**: bool}
        :return: The segment.
        
        
        """
        ...
    
    def SetSegment(self, segment: Any, cnt: int, closed: bool) -> None:
        """    
        Set properties of the segment.
        
        :type id: int
        :param id: The segment
        :raise IndexError: If the *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type cnt: int
        :param cnt: The count of points.
        :type closed: bool
        :param closed: **True** if the segment is closed.
        
        
        """
        ...
    
    def GetSegmentCount(self) -> int:
        """    
        Returns the count of segments.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def ResizeObject(self, pcnt: int, scnt: int) -> bool:
        """    
        | Change the number of segments and points for this spline.
        | If *scnt* is -1 or not set, the method :meth:`PointObject.ResizeObject` of :class:`PointObject <c4d.PointObject>` is used.
        
        :type pcnt: int
        :param pcnt: The new point count.
        :type scnt: int
        :param scnt: The new segment count.
        :rtype: bool
        :return: Success of changing the number of points and segments.
        
        
        """
        ...
    
    def SetDefaultCoeff(self) -> bool:
        """    
        Initialise the spline with default coefficients.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetTangentCount(self) -> int:
        """    
        Returns the count of tangents.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetTangent(self, id: int) -> None:
        """    
        Return a tangent.
        
        .. code-block:: python
        
        tangent = spline.GetTangent()
        print tangent["vl"], tangent["vr"]
        
        :type id: int
        :param id: The tangent index.
        :raise IndexError: If the tangent index *id* is out of range : *0<=segment<*:meth:`GetTangentCount`.
        :rtype: dict{**vl**: :class:`Vector <c4d.Vector>`, **vr**: :class:`Vector <c4d.Vector>`}
        :return: Left and right part that defines the tangent.
        
        
        """
        ...
    
    def SetTangent(self, id: int, vl: Vector, vr: Vector) -> None:
        """    
        Set a tangent.
        
        .. code-block:: python
        
        spline.SetTangent(index=12, vl=tangent["vl"], vr=tangent["vr"])
        
        :type id: int
        :param id: The tangent index.
        :raise IndexError: If the tangent index *id* is out of range.
        :type vl: c4d.Vector
        :param vl: The left tangent.
        :type vr: c4d.Vector
        :param vr: The right tangent.
        
        
        """
        ...
    

class BaseShader(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Initialize a new :class:`BaseShader <c4d.BaseShader>` in memory.
        
        :type type: int
        :param type: The shader type : :doc:`/types/shaders`.
        :rtype: c4d.BaseShader
        :return: The new shader.
        
        
        """
        ...
    
    def Sample(self, cd: ChannelData) -> Vector:
        """    
        | Calls :meth:`ShaderData.Output` for the corresponding shader plugin.
        | The channel color for the point cd.p is calculated.
        
        .. note::
        
        This has to be done within a pair of :meth:`InitRender` / :meth:`FreeRender` calls.
        
        :type cd: c4d.modules.render.ChannelData
        :param cd: The channel data to use.
        :rtype: c4d.Vector
        :return: The calculated color.
        
        
        """
        ...
    
    def SampleBump(self, cd: ChannelData, bumpflags: int) -> Vector:
        """    
        | This function allows you to calculate bump mapping for a shader (and its children) with the same algorithm as Cinema 4D does.
        | The function returns the delta vector that is added to the normal.
        | The resulting normal is calculated by:
        
        .. code-block:: python
        
        n_dst =  not (n_src + SampleBump(SAMPLEBUMP_NONE)) # normalize result
        
        where **n_src** is the original normal and **n_dst** is the bumped normal.
        
        .. note::
        
        | This has to be done within a pair of :meth:`InitRender` / :meth:`FreeRender` calls.
        | Also the :attr:`BaseVolumeData.ddu` and :attr:`BaseVolumeData.ddv` vectors have to be initialized.
        
        :type cd: c4d.modules.render.ChannelData
        :param cd: The channel data to use.
        :type bumpflags: int
        :param bumpflags: Flags:
        
        .. include:: /consts/SAMPLEBUMP.rst
        :start-line: 3
        
        :rtype: c4d.Vector
        :return: The delta normal.
        
        
        """
        ...
    
    def GetBitmap(self) -> BaseBitmap:
        """    
        Returns the bitmap of shaders of type *Xbitmap*, otherwise None.
        
        .. note::
        
        This has to be done within a pair of :meth:`InitRender` / :meth:`FreeRender` calls.
        
        Here is an example.
        
        .. code-block:: python
        
        material = doc.GetFirstMaterial()
        
        shader = material[c4d.MATERIAL_COLOR_SHADER]
        
        irs = render.InitRenderStruct()
        if shader.InitRender(irs) == c4d.INITRENDERRESULT_OK:
        bitmap = shader.GetBitmap()
        shader.FreeRender()
        if bitmap is not None:
        bitmaps.ShowBitmap(bitmap)
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The bitmap.
        
        .. note::
        
        The returned bitmap must be accessed as read-only.
        
        
        """
        ...
    
    def GetRenderInfo(self) -> int:
        """    
        | Calls `ShaderData.GetRenderInfo()` for the corresponding shader plugin.
        | This retrieves information about what the plugin requires from the raytracer and what it will return.
        
        :rtype: int
        :return: The return values are:
        
        .. include:: /consts/SHADERINFO.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitRender(self, is_: InitRenderStruct) -> int:
        """    
        | Calls :meth:`ShaderData.InitRender()` for the corresponding shader plugin.
        | You have to do this before you can use the :meth:`Sample`, :meth:`SampleBump` or :meth:`GetBitmap` functions.
        
        .. note::
        
        | Remember to call :meth:`FreeRender` afterwards.
        | You aren't allowed to call :meth:`InitRender` multiple times without calling :meth:`FreeRender` in between, even from multiple threads!
        
        :type is_: c4d.modules.render.InitRenderStruct
        :param is_:
        
        Information about the upcoming rendering.
        
        :rtype: int
        :return: Result of the initialisation:
        
        .. include:: /consts/INITRENDERRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def FreeRender(self) -> None:
        """    
        Frees all resources used by this shader, allocated by calling :meth:`InitRender`.
        
        
        """
        ...
    
    def IsColorManagementOff(self, doc: BaseDocument) -> bool:
        """    
        It checks if color management is disabled for shaders within bump, alpha, displacement or normal channels when linear workflow is enabled.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the shader to check if linear workflow is disabled in it.
        :rtype: bool
        :return: **True** if color managment is disabled, otherwise **False**.
        
        
        """
        ...
    
    def Compare(self, dst: BaseShader) -> bool:
        """    
        Checks if this shader is similar to *dst*.
        
        :type dst: c4d.BaseShader
        :param dst: The shader to compare to.
        :rtype: bool
        :return: **True** if the plugin shaders are the same, otherwise **False**.
        
        
        """
        ...
    
    def HasGPURendererSupport(self) -> bool:
        """    
        Checks if the shader is supported by the GPU Renderer.
        
        .. versionadded:: R19.024
        
        :rtype: bool
        :return: **True** if the shader is natively supported by the GPU Renderer, otherwise **False**.
        
        
        """
        ...
    

class LayerShader(BaseShader):
    def __init__(self) -> None:
        """    
        Initializes a new :class:`LayerShader <c4d.LayerShader>` in memory.
        
        :rtype: c4d.LayerShader
        :return: The new shader.
        
        
        """
        ...
    
    def GetFirstLayer(self) -> LayerShaderLayer:
        """    
        Returns the first layer of the shader.
        
        .. note::
        
        To navigate through all the layers of a layer shader, get its first layer then use :meth:`LayerShaderLayer.GetNext`.
        
        :rtype: c4d.LayerShaderLayer
        :return: The first layer in the layer shader.
        
        
        """
        ...
    

class BaseTag(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Initialize a new :class:`BaseTag <c4d.BaseTag>` in memory.
        
        :type type: int
        :param type: The type of tag. See :doc:`/types/tags`.
        :rtype: c4d.BaseTag
        :return: A new tag.
        
        
        """
        ...
    
    def GetObject(self) -> BaseObject:
        """    
        Returns the object where the object is attached.
        
        :rtype: c4d.BaseObject
        :return: The object or **None** if it is not attached.
        
        
        """
        ...
    
    def GetOrigin(self) -> BaseTag:
        """    
        Returns where the tag was cloned from.
        
        .. note::
        
        For example, if the tag is on a cache object, it tells you what the original tag was from the original document.
        
        :rtype: c4d.BaseTag
        :return: The origin tag or **None**.
        
        
        """
        ...
    

class SelectionTag(BaseTag):
    def __init__(self, type: int) -> None:
        """    
        :type type: int
        :param type: The type of selection tag:
        
        .. include:: /types/tags_selection.rst
        :start-line: 3
        
        :rtype: c4d.SelectionTag
        :return: A new selection tag.
        
        
        """
        ...
    
    def GetBaseSelect(self) -> BaseSelect:
        """    
        Gets the selection.
        
        :rtype: c4d.BaseSelect
        :return: The selection instance.
        
        
        """
        ...
    

class TextureTag(BaseTag):
    def __init__(self) -> None:
        """    
        :rtype: c4d.TextureTag
        :return: A new texture tag.
        
        
        """
        ...
    
    def GetPos(self) -> Vector:
        """    
        Get the position of the texture project.
        
        :rtype: c4d.Vector
        :return: The texture XYZ position.
        
        
        """
        ...
    
    def GetRot(self) -> Vector:
        """    
        Get the rotation of the texture project.
        
        :rtype: c4d.Vector
        :return: The rot of the texture.
        
        
        """
        ...
    
    def GetScale(self) -> Vector:
        """    
        Get the scale of the texture project.
        
        :rtype: c4d.Vector
        :return: The scale of the texture.
        
        
        """
        ...
    
    def GetMl(self) -> Vector:
        """    
        Get the texture projection's coordinate system as a matrix.
        
        :rtype: c4d.Vector
        :return: The texture projection's coordinate system.
        
        
        """
        ...
    
    def GetMaterial(self, ignoredoc: bool) -> BaseMaterial:
        """    
        Get the current material associated with this tag.
        
        :type ignoredoc: bool
        :param ignoredoc:
        
        .. versionadded:: R18.020
        
        | **True** to ignore the tag's document (default), otherwise **False**.
        | **True** by default to keep backward compatibility.
        
        .. versionchanged:: R21.204
        
        Changed default value to **False** to match C++.
        
        :rtype: c4d.BaseMaterial
        :return: The material or **None**.
        
        
        """
        ...
    
    def SetPos(self, v: Vector) -> None:
        """    
        Sets the position of the texture projection.
        
        :type v: c4d.Vector
        :param v: The position of the texture.
        
        
        """
        ...
    
    def SetRot(self, v: Vector) -> None:
        """    
        Sets the rotation of the texture projection.
        
        :type v: c4d.Vector
        :param v: The rotation of the texture.
        
        
        """
        ...
    
    def SetScale(self, v: Vector) -> None:
        """    
        Sets the scale of the texture projection.
        
        :type v: c4d.Vector
        :param v: The scale of the texture.
        
        
        """
        ...
    
    def SetMl(self, m: Any) -> None:
        """    
        Sets the texture projection's coordinate system matrix.
        
        :type v: c4d.Matrix
        :param v: The texture projection's coordinate system.
        
        
        """
        ...
    
    def SetMaterial(self, mat: BaseMaterial) -> None:
        """    
        Set the material associated with this tag.
        
        :type mat: c4d.BaseMaterial
        :param mat: The material for this tag.
        
        
        """
        ...
    

class VariableTag(BaseTag):
    def __init__(self, type: int, count: int) -> None:
        """    
        Creates a :class:`VariableTag <c4d.VariableTag>`.
        
        .. note::
        
        Use :class:`VariableTag <c4d.VariableTag>` children classes to create a :class:`UVWTag <c4d.UVWTag>`, :class:`NormalTag <c4d.NormalTag>`, :class:`PointTag <c4d.PointTag>` etc.
        
        Here is how to create a vertex map tag and add it to the current polygon object.
        
        .. code-block:: python
        
        tag = c4d.VariableTag(c4d.Tvertexmap, op.GetPointCount())
        op.InsertTag(tag)
        c4d.EventAdd()
        
        :type type: int
        :param type: The variable tag type:
        
        .. include:: /types/tags_variable.rst
        :start-line: 3
        
        :type count: int
        :param count: The number of data elements in the tag.
        :rtype: c4d.VariableTag
        :return: A variable tag.
        
        
        """
        ...
    
    def GetAllHighlevelData(self) -> Any:
        """    
        Gets the data for the variable tag.
        
        The following code prints the weights from a vertex map tag.
        
        .. code-block:: python
        
        tag = op.GetTag(c4d.Tvertexmap)
        if tag:
        print tag.GetAllHighlevelData()
        
        .. note::
        
        See warning in :meth:`GetDataCount()` for *Tnormal* / :class:`NormalTag <c4d.NormalTag>`.
        
        :rtype: Any
        :return: The data for the variable tag. See table in :doc:`/types/tags_variable`.
        
        
        """
        ...
    
    def SetAllHighlevelData(self, data: Any) -> None:
        """    
        Sets the data for the variable tag.
        
        .. note::
        
        See warning in :meth:`GetDataCount()` for **Tnormal** / :class:`NormalTag <c4d.NormalTag>`.
        
        :type data: any
        :param data: The data for the variable tag. See table in :doc:``/types/tags_variable``.
        
        
        """
        ...
    
    def GetDataCount(self) -> int:
        """    
        Gets the number of data elements in the variable tag.
        
        .. warning::
        
        The **Tnormal** / :class:`NormalTag <c4d.NormalTag>` data contains `12` times more elements than :meth:`GetDataCount()` returns.
        
        :rtype: int
        :return: The number of data elements.
        
        
        """
        ...
    
    def GetDataSize(self) -> int:
        """    
        Gets the size of one data element in bytes.
        
        :rtype: int
        :return: The byte size of a data element.
        
        
        """
        ...
    
    def GetLowlevelDataAddressW(self) -> ByteSeq:
        """    
        Gets the writable buffer object for the variable tag's data.
        
        .. warning::
        
        Use with special care.
        
        :rtype: c4d.storage.ByteSeq
        :return: The buffer object.
        
        
        """
        ...
    
    def GetLowlevelDataAddressR(self) -> ByteSeq:
        """    
        Gets the read-only buffer object for the variable tag's data.
        
        .. warning::
        
        Use with special care.
        
        :rtype: c4d.storage.ByteSeq
        :return: The buffer object.
        
        
        """
        ...
    

class NormalTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.NormalTag
        :return: A new normal tag.
        
        
        """
        ...
    

class PointTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.PointTag
        :return: A new point tag.
        
        
        """
        ...
    

class PolygonTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.PolygonTag
        :return: A new polygon tag.
        
        
        """
        ...
    

class SegmentTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.SegmentTag
        :return: A new segment tag.
        
        
        """
        ...
    

class TangentTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.TangentTag
        :return: A new tangent tag.
        
        
        """
        ...
    

class UVWTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        :type count: int
        :param count: The number of elements in the tag.
        :rtype: c4d.UVWTag
        :return: A new UVW tag.
        
        
        """
        ...
    
    def GetSlow(self, i: int) -> None:
        """    
        Get the UVW coordinate for a polygon.
        
        .. code-block:: python
        
        for i in xrange(uvwtag.GetDataCount()):
        uvwdict = uvwtag.GetSlow(i)
        print uvwdict["a"]
        print uvwdict["b"]
        print uvwdict["c"]
        print uvwdict["d"]
        
        :type i: int
        :param i: The index of the polygon to get the coordinates for.
        :raise IndexError: If *i* is out of range : *0<=i<*:meth:`VariableTag.GetDataCount`.
        :rtype: dict{**a**: :class:`Vector <c4d.Vector>`, **b**: :class:`Vector <c4d.Vector>`, **c**: :class:`Vector <c4d.Vector>`, **d**: :class:`Vector <c4d.Vector>`}
        :return: The UVW coordinates.
        
        
        """
        ...
    
    def SetSlow(self, i: int, a: Vector, b: Vector, c: Vector, d: Vector) -> None:
        """    
        Set the UVW coordinates of a polygon.
        
        :type i: int
        :param i: The index of the polygon to set the coordinates for.
        :raise IndexError: If *i* is out of range : *0<=i<*:meth:`VariableTag.GetDataCount`.
        :type a: c4d.Vector
        :param a: The coordinate of the first point.
        :type b: c4d.Vector
        :param b: The coordinate of the second point.
        :type c: c4d.Vector
        :param c: The coordinate of the third point.
        :type d: c4d.Vector
        :param d: The coordinate of the fourth point.
        
        
        """
        ...
    
    def CpySlow(self, i: int, srctag: UVWTag, src: int) -> None:
        """    
        Copy a UVW coordinate.
        
        :type i: int
        :param i: The destinate polygon index in this UVWTag.
        :raise IndexError: If *i* is out of range (*0<=i<*:meth:`VariableTag.GetDataCount`) for *self* and/or *src*.
        :type srctag: c4d.UVWTag
        :param srctag: The UVWTag for the source polygon.
        :type src: int
        :param src: The source polygon index in this UVWTag.
        
        
        """
        ...
    

class VertexColorTag(VariableTag):
    def __init__(self, count: int) -> None:
        """    
        Creates a :class:`c4d.VertexColorTag`.
        
        :type count: int
        :param count: The number of elements in the tag. Must be equal to the object's polygon count if the tag is in per polygon vertex mode, otherwise must be equal to the object's point count in per vertex mode.
        :rtype: :class:`c4d.VertexColorTag`
        :return: A new Vertex Color tag.
        
        
        """
        ...
    
    def GetDataAddressR(self) -> Any:
        """    
        | Gets the read-only data handle.
        | It automatically recognizes if the tag is in per polygon vertex or per vertex mode.
        
        :rtype: PyCObject
        :return: The handle to the read-only vertex color data.
        
        
        """
        ...
    
    def GetDataAddressW(self) -> Any:
        """    
        | Gets the writable data handle.
        | It automatically recognizes if the tag is in per polygon vertex or per vertex mode.
        
        :rtype: PyCObject
        :return: The handle to the writable vertex color data.
        
        
        """
        ...
    
    def IsPerPointColor(self) -> bool:
        """    
        Checks if the data is stored per point (vertex) or per polygon vertex.
        
        :rtype: bool
        :return: **True** if vertex colors are stored per vertex, otherwise **False**.
        
        
        """
        ...
    
    def SetPerPointMode(self, perPointColor: bool) -> bool:
        """    
        Sets whatever the data is stored per point (vertex) or per polygon vertex.
        
        .. note::
        
        The item count is automatically updated and the data converted if possible.
        
        .. warning::
        
        All handles are invalidated after the call.
        
        :type perPointColor: bool
        :param perPointColor: If **True** the data will be stored per vertex otherwise per polygon vertex.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def GetPolygon(data: Any, i: int) -> None:
        """    
        Retrieves the vertex colors for the polygon *i* in per polygon vertex mode.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressR()
        
        polyCount = op.GetPolygonCount()
        for idx in xrange(polyCount):
        poly = c4d.VertexColorTag.GetPolygon(data, idx)
        print poly
        
        :type data: PyCObject
        :param data: The data handle.
        :type i: int
        :param i: The polygon index.
        :rtype: dict("a": :class:`c4d.Vector4d`, "b": :class:`c4d.Vector4d`, "c": :class:`c4d.Vector4d`, "d": :class:`c4d.Vector4d`)
        :return: The retrieved vertex color data.
        
        
        """
        ...
    
    @staticmethod
    def SetPolygon(data: Any, i: int, polygon: Dict[str, Any]) -> None:
        """    
        Sets the vertex colors for the polygon *i* in per polygon vertex mode.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressW()
        
        white = c4d.Vector4d(1.0, 1.0, 1.0, 1.0)
        poly = {"a": white, "b": white, "c": white, "d": white}
        
        polyCount = op.GetPolygonCount()
        for idx in xrange(polyCount):
        c4d.VertexColorTag.SetPolygon(data, idx, poly)
        
        c4d.EventAdd()
        
        :type data: PyCObject
        :param data: The data handle.
        :type i: int
        :param i: The polygon index.
        :type polygon: Dict
        :param polygon: The vertex color data **a, b, c and d** to be set to the polygon
        
        
        """
        ...
    
    @staticmethod
    def GetPoint(data: Any, nb: Neighbor, vadr: Any, pIndex: int) -> None:
        """    
        Retrieves the vertex color for the vertex *pIndex*.
        
        .. note::
        
        | If the tag is in per polygon vertex mode it traverses all polygons attached to it.
        | If different values are found then the average value will be returned.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressR()
        
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        point = c4d.VertexColorTag.GetPoint(data, None, None, idx)
        print point
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonR`.
        :type pIndex: int
        :param pIndex: The point index.
        :rtype: :class:`c4d.Vector4d`
        :return: The RGBA color for the passed vertex, or the average color if multiple values were found.
        
        
        """
        ...
    
    @staticmethod
    def SetPoint(data: Any, nb: Neighbor, vadr: Any, pIndex: int, color: Vector4d) -> None:
        """    
        Sets the vertex color for the vertex *pIndex*.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressW()
        
        white = c4d.Vector4d(1.0, 1.0, 1.0, 1.0)
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        c4d.VertexColorTag.SetPoint(data, None, None, idx, white)
        
        c4d.EventAdd()
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonW`.
        :type pIndex: int
        :param pIndex: The point index.
        :type color: c4d.Vector4d
        :param color: The new RGBA color to be assigned to the vertex.
        
        
        """
        ...
    
    @staticmethod
    def GetColor(data: Any, nb: Neighbor, vadr: Any, pIndex: int) -> None:
        """    
        Retrieves the vertex color for the vertex *pIndex*.
        
        .. note::
        
        | If the tag is in per polygon vertex mode it traverses all polygons attached to it.
        | If different values are found then the average value will be returned.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressR()
        
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        color = c4d.VertexColorTag.GetColor(data, None, None, idx)
        print color
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonR`.
        :type pIndex: int
        :param pIndex: The point index.
        :rtype: :class:`c4d.Vector`
        :return:  The RGB color for the passed point index, or the average color if multiple values were found.
        
        
        """
        ...
    
    @staticmethod
    def SetColor(data: Any, nb: Neighbor, vadr: Any, pIndex: int, color: Vector) -> None:
        """    
        Sets the vertex color for the vertex *pIndex*.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressW()
        
        white = c4d.Vector(1.0, 1.0, 1.0)
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        c4d.VertexColorTag.SetColor(data, None, None, idx, white)
        
        c4d.EventAdd()
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonW`.
        :type pIndex: int
        :param pIndex: The point index.
        :type color: c4d.Vector
        :param color: The new RGB color to be assigned to the vertex.
        
        
        """
        ...
    
    @staticmethod
    def GetAlpha(data: Any, nb: Neighbor, vadr: Any, pIndex: int) -> float:
        """    
        Retrieves the vertex color alpha value for the vertex *pIndex*.
        
        .. note::
        
        | If the tag is in per polygon vertex mode it traverses all polygons attached to it.
        | If different values are found then the average value will be returned.
        
        Example.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressR()
        
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        alpha = c4d.VertexColorTag.GetAlpha(data, None, None, idx)
        print alpha
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonR`.
        :type pIndex: int
        :param pIndex: The point index.
        :rtype: float
        :return: The alpha value for the passed vertex, or the average alpha value if multiple values were found.
        
        
        """
        ...
    
    @staticmethod
    def SetAlpha(data: Any, nb: Neighbor, vadr: Any, pIndex: int, value: float) -> None:
        """    
        Sets the vertex color alpha value for the vertex *pIndex*.
        
        .. code-block:: python
        
        import c4d
        
        tag = op.GetTag(c4d.Tvertexcolor)
        data = tag.GetDataAddressW()
        
        pointCount = op.GetPointCount()
        for idx in xrange(pointCount):
        c4d.VertexColorTag.SetAlpha(data, None, None, idx, 0.5)
        
        c4d.EventAdd()
        
        :type data: PyCObject
        :param data: The data handle.
        :type nb: c4d.utils.Neighbor
        :param nb: A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
        :type vadr: PyCObject
        :param vadr: The object :class:`c4d.CPolygon` array. Pass **None** if in per vertex mode. See :meth:`PolygonObject.GetPolygonW`.
        :type pIndex: int
        :param pIndex: The point index.
        :type value: float
        :param value: The new alpha value to be assigned to the vertex.
        
        
        """
        ...
    

class BaseView(BaseList2D):
    def GetFrame(self) -> Dict[str, Any]:
        """    
        | The dimension in pixels of the view window.
        | The coordinates are relative to the upper left corner of the view, and specify visible pixels. (I.e. the border is not included.).
        
        .. code-block:: python
        
        dimension = bv.GetFrame()
        print(dimension["cl"], dimension["ct"], dimension["cr"], dimension["cb"])
        # (left, top, right, bottom)
        
        :rtype: Dict[int, int, int, int]
        
        
        """
        ...
    
    def GetSafeFrame(self) -> Dict[str, Any]:
        """    
        | The dimension in pixels of the render lines.
        | The render lines show what part of the view is included in the rendered picture.
        
        .. code-block:: python
        
        position = bv.GetSafeFrame()
        print position["cl"], position["ct"], position["cr"], position["cb"]
        # (left, top, right, bottom)
        
        :rtype: Dict[int, int, int, int]
        
        
        """
        ...
    
    def GetViewParameter(self) -> Dict[str, Any]:
        """    
        | Retrieves the parameters for the current projection. See ``Ocamera.h`` for projection types.
        | The following is the code used internally to project points.
        
        .. code-block:: python
        
        CAMDIST = 0.05
        
        def WorldToCamera(p, camera_matrix):
        return p*(~inverse_camera_matrix)
        
        
        def CameraToWorld(p, camera_matrix):
        return p*camera_matrix
        
        
        def CameraToScreen(pp):
        p = c4d.Vector(pp)
        if projection==c4d.Pperspective:
        nz = 1.0/CAMDIST if p.z<=00 else 1.0/(p.z + CAMDIST)
        p.x = p.x*scale.x*nz+off.x
        p.y = p.y*scale.y*nz+off.y
        return p
        
        p.x = (p.x*scale.x)+off.x
        p.y = (p.y*scale.y)+off.y
        
        if projection==c4d.Pmilitary or projection==c4d.Pfrog or projection==c4d.Pgentleman:
        p.x += p.z*scale.x*sclaez.x
        p.y -= p.z*scale.y*scalez.y
        return p
        
        
        def ScreenToCamera(pp):
        p = c4d.Vector(pp)
        if projection==c4d.Pmilitary or projection==c4d.Pfrog or projection==c4d.Pgentleman:
        p.x -= p.z*scale.x*scalez.x
        p.y += p.z*scale.y*scalez.y
        
        p.x = (p.x-off.x)/scale.x
        p.y = (p.y-off.y)/scale.y
        
        if projection==c4d.Pperspective:
        nz = p.z + CAMDIST
        p.x *= nz
        p.y *= nz
        return p
        
        For non-axometric projection here's the code how to calculate off/scale.
        
        .. code-block:: python
        
        def InitView(camera, xres, yres, pix_x, pix_y):
        
        opm = camera.GetMg()
        data = camera.GetDataInstance()
        project = data.GetInt(CAMERA_PROJECTION, Pperspective)
        
        if projection!=Pperspective and projection!=Pparallel:
        opm.v1 = Vector(1.0,0.0,0.0)
        opm.v2 = Vector(0.0,1.0,0.0)
        opm.v3 = Vector(0.0,0.0,1.0)
        
        off.x = xres*0.5
        off.y = yres*0.5
        
        if b_ab == Pperspective:
        ap = data.GetFloat(CAMERAOBJECT_APERTURE, 36.0)
        scale.x = data.GetFloat(CAMERA_FOCUS, 36.0) / ap * xres
        else:
        scale.x = xres/1024.0*data.GetFloat(CAMERA_ZOOM,1.0)
        
        scale.y = -scale.x*pix_x/pix_y
        # ... calculated here
        
        #example how to use GetViewParameter
        params = bv.GetViewParameter()
        #params["offset"], params["scale"], params["scale_z"]
        
        :rtype: Dict[c4d.Vector, c4d.Vector, c4d.Vector]
        :return: The dimension, is never **None**.
        
        
        """
        ...
    
    def GetMg(self) -> Matrix:
        """    
        Returns the camera matrix, i.e. the global object matrix of the current camera object.
        
        :rtype: c4d.Matrix
        :return: The camera matrix.
        
        
        """
        ...
    
    def GetMi(self) -> Matrix:
        """    
        Returns the inverse of the camera matrix.
        
        Equivalent to :meth:`GetMg`, but faster.
        
        :rtype: c4d.Matrix
        :return: The inverted camera matrix.
        
        
        """
        ...
    
    def GetBaseMatrix(self) -> Matrix:
        """    
        Gets the base matrix.
        
        .. versionadded:: R14.014
        
        .. note::
        
        The base matrix is multiplied with the camera matrix so that it is possible to have e.g. a frontal view into another direction than +Z.
        
        :rtype: c4d.Matrix
        :return: The base matrix.
        
        
        """
        ...
    
    def SetBaseMatrix(self, mg: Matrix) -> None:
        """    
        Sets the base matrix.
        
        .. versionadded:: R14.014
        
        .. note::
        
        The base matrix is multiplied with the camera matrix so that it is possible to have e.g. a frontal view into another direction than +Z.
        
        :type mg: c4d.Matrix
        :param mg: The new base matrix.
        
        
        """
        ...
    
    def GetPlanarRotation(self) -> float:
        """    
        Gets the rotation of the planar views.
        
        .. versionadded:: R14.014
        
        :rtype: float
        :return: The planar rotation.
        
        
        """
        ...
    
    def SetPlanarRotation(self, r: Any) -> None:
        """    
        Sets the rotation of the planar views.
        
        .. versionadded:: R14.014
        
        :type mg: float
        :param mg: The new planar rotation.
        
        
        """
        ...
    
    def GetProjection(self) -> int:
        """    
        Returns the projection used by the view. See ``Ocamera.h`` for values.
        
        :rtype: int
        :return: The projection type.
        
        
        """
        ...
    
    def TestPoint(self, x: int, y: int) -> bool:
        """    
        | Returns **True** if the point is within the boundary returned by :meth:`GetFrame`.
        | The point coordinates must be in screen space.
        
        :type x: int
        :param x: X coordinate
        :type y: int
        :param y: Y coordinate
        :rtype: bool
        :return: **True** if the point is inside, otherwise **False**.
        
        
        """
        ...
    
    def TestPointZ(self, p: Vector) -> bool:
        """    
        | Tests if the point is visible in the view according to the current projection.
        | The point must be in camera space.
        
        :type p: c4d.Vector
        :param p: The point to check.
        :rtype: bool
        :return: **True** if the point is visible in the view, otherwise **False**.
        
        
        """
        ...
    
    def TestClipping3D(self, mp: Vector, rad: Vector, mg: Matrix) -> Dict[str, Any]:
        """    
        Tests if a bounding box is visible in the view according to the current projection.
        
        The box is defined with passed *mp*, *rad* and *mg* by these eight corner coordinates
        
        .. code-block:: python
        
        p0 = c4d.Vector(mp.x + rad.x, mp.y + rad.y, mp.z + rad.z) * mg
        p1 = c4d.Vector(mp.x + rad.x, mp.y + rad.y, mp.z - rad.z) * mg
        p2 = c4d.Vector(mp.x + rad.x, mp.y - rad.y, mp.z + rad.z) * mg
        p3 = c4d.Vector(mp.x + rad.x, mp.y - rad.y, mp.z - rad.z) * mg
        p4 = c4d.Vector(mp.x - rad.x, mp.y + rad.y, mp.z + rad.z) * mg
        p5 = c4d.Vector(mp.x - rad.x, mp.y + rad.y, mp.z - rad.z) * mg
        p6 = c4d.Vector(mp.x - rad.x, mp.y - rad.y, mp.z + rad.z) * mg
        p7 = c4d.Vector(mp.x - rad.x, mp.y - rad.y, mp.z - rad.z) * mg
        
        :type mp: c4d.Vector
        :param mp: The center of the box.
        :type rad: c4d.Vector
        :param rad: The radius of the box.
        :type mg: c4d.Matrix
        :param mg: The transformation to world space from *mp*/*rad* space.
        :rtype: Dict[bool, bool, bool]
        :return: A dictionary with the following information:
        
        | 'visible': **True** if the box is visible, otherwise **False**.
        | 'clip2d': **True** if the box needs 2D clipping, i.e. if any part of it is outside of the view boundaries. Otherwise **False**.
        | 'clipz': **True** if the box needs Z clipping, i.e. if any part of it is too close to or behind the camera. Otherwise **False**.
        
        
        """
        ...
    
    def WS(self, p: Vector) -> Vector:
        """    
        | World to screen conversion.
        | Converts *p* from world space to screen space (pixels relative to the view), and returns the conversion.
        | The orthogonal distance to the world point is stored in world units in the Z axis of the result.
        
        :type p: c4d.Vector
        :param p: A point in world space.
        :rtype: c4d.Vector
        :return: The point in screen space.
        
        
        """
        ...
    
    def SW(self, p: Vector) -> Vector:
        """    
        | Screen to world conversion.
        | Converts *p* from screen space (pixels relative to the view) to world space.
        |
        | The X and Y coordinates of the point are given in screen space; the Z coordinate is the orthogonal distance in world units to the point from the view plane. The result of the conversion is returned.
        
        :type p: c4d.Vector
        :param p: A point in screenspace.
        :rtype: c4d.Vector
        :return: The point in worldspace.
        
        
        """
        ...
    
    def WC(self, p: Vector) -> Vector:
        """    
        | World to camera conversion.
        | Converts *p* from world space to camera space and returns the result.
        
        :type p: c4d.Vector
        :param p: A point in world space.
        :rtype: c4d.Vector
        :return: The point in camera space.
        
        
        """
        ...
    
    def CW(self, p: Vector) -> Vector:
        """    
        | Camera to world conversion.
        | Converts *p* from camera space to world space and returns the result.
        
        :type p: c4d.Vector
        :param p: A point in camera space.
        :rtype: c4d.Vector
        :return: The point in world space.
        
        
        """
        ...
    
    def SC(self, p: Vector) -> Vector:
        """    
        | Screen to camera conversion.
        | Converts *p* from screen space (pixels relative to the view) to camera space and returns the result.
        |
        | The X and Y coordinates of the point are given in screen space; the Z coordinate is the orthogonal distance in world units to the point from the view plane.
        
        
        :type p: c4d.Vector
        :param p: A point in screen space.
        :rtype: c4d.Vector
        :return: The point in camera space.
        
        
        """
        ...
    
    def CS(self, p: Vector, z_inverse: bool) -> Vector:
        """    
        | Camera to screen conversion.
        | Converts *p* from camera space to screen space (pixels relative to the view) and returns the result.
        
        
        :type p: c4d.Vector
        :param p: A point in camera space.
        :type z_inverse: bool
        :param z_inverse:
        
        | If **True** the Z coordinate of the converted point is inverted.
        | This is used by the Z-buffer.
        
        :rtype: c4d.Vector
        :return: A point in screen space.
        
        
        """
        ...
    
    def WC_V(self, v: Vector) -> Vector:
        """    
        | World to camera vector conversion.
        | Converts the world vector *v* to camera space and returns the result.
        
        :type v: c4d.Vector
        :param v: A vector in world space.
        :rtype: c4d.Vector
        :return: The vector in camera space.
        
        
        """
        ...
    
    def CW_V(self, v: Vector) -> Vector:
        """    
        | Camera to world vector conversion.
        | Converts the camera vector *v* to world space and returns the result.
        
        :type v: c4d.Vector
        :param v: A vector in camera space.
        :rtype: c4d.Vector
        :return: The vector in world space.
        
        
        """
        ...
    
    def PW_S(self, z: float, horizontal: bool) -> float:
        """    
        Returns the size in world units for a single pixel at the given Z-depth *z*.
        
        :type z: float
        :param z: The Z-depth.
        :type horizontal: bool
        :param horizontal:
        
        | **True** if the size is measured horizontally, **False** for vertical measurement.
        | This is useful for non-square pixel aspect ratios.
        
        :rtype: float
        :return: The size in world units.
        
        
        """
        ...
    
    def WP_S(self, z: float, horizontal: bool) -> float:
        """    
        Returns the size in pixels for a single world unit at the given Z-depth *z*.
        
        :type z: float
        :param z: The Z-depth.
        :type horizontal: bool
        :param horizontal:
        
        | **True** if the size is measured horizontally, **False** for vertical measurement.
        | This is useful for non-square pixel aspect ratios.
        
        :rtype: float
        :return: The size in pixels.
        
        
        """
        ...
    
    def PW_W(self, p: Vector, horizontal: bool) -> float:
        """    
        Returns the size in world units for a single pixel at screen space vector *p*.
        
        :type p: c4d.Vector
        :param p: The pixel in screen space.
        :type horizontal: bool
        :param horizontal:
        
        | **True** if the size is measured horizontally, **False** for vertical measurement.
        | This is useful for non-square pixel aspect ratios.
        
        :rtype: float
        :return: Size in world units.
        
        
        """
        ...
    
    def WP_W(self, p: Vector, horizontal: bool) -> float:
        """    
        Returns the size in screen space pixels for a single world unit at world position *p*.
        
        :type p: c4d.Vector
        :param p: The world unit in world space.
        :type horizontal: bool
        :param horizontal:
        
        | **True** if the size is measured horizontally, **False** for vertical measurement.
        | This is useful for non-square pixel aspect ratios.
        
        :rtype: float
        :return: Size in screen space pixels.
        
        
        """
        ...
    
    def BackfaceCulling(self, n: Vector, p: Vector) -> Vector:
        """    
        Tests the face with center *p* and normal *n* for backface culling.
        
        :type n: c4d.Vector
        :param n: The face normal.
        :type p: c4d.Vector
        :param p: The face center.
        :rtype: c4d.Vector
        :return: **True** if the face should be visible, otherwise **False**.
        
        
        """
        ...
    
    def ZSensitiveNear(self) -> bool:
        """    
        Indicates if the view has Z near clipping.
        
        :rtype: bool
        :return: **True** if the view has Z clipping near, otherwise **False**.
        
        
        """
        ...
    
    def ZSensitiveNearClipping(self) -> None:
        """    
        Returns the near clipping of Z sensitive view.
        
        
        """
        ...
    
    def ZSensitiveFar(self) -> bool:
        """    
        Indicates if the view has Z far clipping.
        
        :rtype: bool
        :return: **True** if the view has Z clipping far, otherwise **False**.
        
        
        """
        ...
    
    def ZSensitiveFarClipping(self) -> float:
        """    
        Returns the far clipping of Z sensitive view.
        
        :rtype: float
        :return: Far clipping distance.
        
        
        """
        ...
    
    def ProjectPointOnLine(self, p: Vector, v: Vector, mouse_x: float, mouse_y: float) -> None:
        """    
        Calculates the nearest point on the line defined by *p* and *v* for a given mouse coordinate.
        
        :type p: c4d.Vector
        :param p: Start position of the line in world space.
        :type v: c4d.Vector
        :param v: Direction of the line. The length of this vector determines the scaling of the returned offset.
        :type mouse_x: float
        :param mouse_x: Mouse X-coordinate.
        :type mouse_y: float
        :param mouse_y: Mouse Y-coordinate.
        :rtype: tuple(:class:`Vector <c4d.Vector>`, float, int)
        :return: The `nearest point` on the line, the `distance` from *p* scaled by the length of *v* (`offset` = distance to p / length of v) and an `error code`:
        
        - 1 = Failed to find nearest point correctly, lines may be beyond horizon, behind camera, or ray line and line may be parallel.
        - 2 = Point is either beyond the start or end of the described segment (but a point will still be returned for the line/ray).
        
        
        """
        ...
    
    def ProjectPointOnPlane(self, p: Vector, v: Vector, mouse_x: float, mouse_y: float) -> None:
        """    
        Calculates the nearest point on the plane defined by *p* and *v* for a given mouse coordinate.
        
        :type p: c4d.Vector
        :param p: The plane's position in world space.
        :type v: c4d.Vector
        :param v: The plane's normal in world space.
        :type mouse_x: float
        :param mouse_x: Mouse X-coordinate.
        :type mouse_y: float
        :param mouse_y: Mouse Y-coordinate.
        :rtype: tuple(:class:`Vector <c4d.Vector>`, int)
        :return: The `nearest point` on the plane and an `error code`:
        
        - 1 = Failed to find nearest point correctly, lines may be beyond horizon, behind camera, or ray line and line may be parallel.
        - 2 = Point is either beyond the start or end of the described segment (but a point will still be returned for the line/ray).
        
        
        """
        ...
    
    def SetPen(self, col: Vector, flags: Optional[int] = ...) -> None:
        ...
    

class BaseDraw(BaseView):
    def __init__(self) -> None:
        """    
        Initialize a new base draw.
        
        .. versionadded:: R17.053
        
        .. note::
        
        Useful for situations when there is no base draw available. It is used for instance in Mograph's Camera shader.
        
        :rtype: c4d.BaseDraw
        :return: A new base draw.
        
        
        """
        ...
    
    def GetParameterData(self, id: int) -> Any:
        """    
        Get a new parameter object.
        
        :type id: int
        :param id: A parameter ID. See the ``dbasedraw.h`` description file.
        :rtype: Any
        :return: The parameter data for *id*. The type depends on the *id*.
        
        
        """
        ...
    
    def GetFrameScreen(self) -> None:
        """    
        Used in the Extended GL mode. This mode is not documented. See ``c4d_gl.h`` for definitions.
        
        :rtype: dict{**cl**: int, **ct**: int, **cr**: int, **cb**: int, }
        :return: A dict or **None**.
        
        
        """
        ...
    
    def HasCameraLink(self) -> bool:
        """    
        Indicates if the camera link is enabled.
        
        :rtype: bool
        :return: **True** if a scene camera is used, and **False** if the editor camera is used.
        
        
        """
        ...
    
    def SetSceneCamera(self, op: BaseObject, animate: bool) -> None:
        """    
        Sets a new scene camera. If *op* os **None**, the editor camera is used.
        
        :type op: c4d.BaseObject
        :param op: The new camera.
        :type animate: bool
        :param animate: Private.
        
        
        """
        ...
    
    def GetSceneCamera(self, doc: BaseDocument) -> BaseObject:
        """    
        Returns the current scene camera from the passed document, or **None** if no scene camera is used.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to get the scene camera from.
        :rtype: c4d.BaseObject
        :return: The scene camera.
        
        
        """
        ...
    
    def GetEditorCamera(self) -> BaseObject:
        """    
        Returns the editor camera.
        
        :rtype: c4d.BaseObject
        :return: The editor camera. Guaranteed to never be **None**.
        
        
        """
        ...
    
    def GetDisplayFilter(self) -> int:
        """    
        | Returns the current display filter.
        | This is a bit field derived from the *DISPLAYFILTER* values.
        
        .. note::
        
        To set the display filter use the description flags with :meth:`GeListNode.__setitem__` or :meth:`C4DAtom.SetParameter`.
        
        For instance the following script switches the Filter "Subdivision Surface".
        
        .. code-block:: python
        
        bd = doc.GetActiveBaseDraw()
        displayFilter = bd.GetDisplayFilter()
        
        if displayFilter & c4d.DISPLAYFILTER_HYPERNURBS:
        bd[c4d.BASEDRAW_DISPLAYFILTER_HYPERNURBS] = False
        print "Switched Off Subdivision Surface Display Filter"
        else:
        bd[c4d.BASEDRAW_DISPLAYFILTER_HYPERNURBS] = True
        print "Switched On Subdivision Surface Display Filter"
        
        bd.Message(c4d.MSG_CHANGE)
        c4d.EventAdd()
        
        Note the difference between the filters "Subdivision Surface" and "SDS Mesh".
        
        :rtype: int
        :return: A bit field with the following flags:
        
        .. include:: /consts/DISPLAYFILTER.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetEditState(self) -> int:
        """    
        Get the edit state. This is a bit field derived from the the edit state description flags in `dbasedraw.h`.
        
        .. note::
        
        To set the display filter use the description flags with :meth:`GeListNode.__setitem__` or :meth:`C4DAtom.SetParameter`.
        
        :rtype: int
        :return: A bit field with the following flags:
        
        .. include:: /consts/DISPLAYEDITSTATE.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsViewOpen(self, doc: BaseDocument) -> bool:
        """    
        Checks if the current tool can use the curent SDS/Deformed editing state.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :rtype: bool
        :return: **True** if the view is open, otherwise **False**.
        
        
        """
        ...
    
    def InitializeView(self, doc: BaseDocument, cam: BaseObject, editorsv: bool) -> None:
        """    
        Used after rendering into a framebuffer with different resolution than the editor view.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The view's document.
        :type cam: c4d.BaseObject
        :param cam: The view's camera.
        :type editorsv: bool
        :param editorsv: Set this **True** to retain the view's ratio.
        
        
        """
        ...
    
    def InitClipbox(self, left: int, top: int, right: int, bottom: int, flags: int) -> None:
        """    
        Used to render into a framebuffer with different resolution than the editor view.
        
        :type left: int
        :param left: Left coordinate of the framebuffer.
        :type top: int
        :param top: Top coordinate of the framebuffer.
        :type right: int
        :param right: Right coordinate of the framebuffer.
        :type bottom: int
        :param bottom: Bottom coordinate of the framebuffer.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/INIT_CLIPBOX.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitView(self, camera: BaseContainer, op_m: Matrix, sv: float, pix_x: float, pix_y: float, fitview: bool) -> None:
        """    
        Used to render into a framebuffer with different resolution than the editor view.
        
        :type camera: c4d.BaseContainer
        :param camera: The camera's container.
        :type op_m: c4d.Matrix
        :param op_m: The camera's matrix.
        :type sv: float
        :param sv: The frame's ratio.
        :type pix_x: float
        :param pix_x: The frame's X size.
        :type pix_y: float
        :param pix_y: The frame's Y size.
        :type fitview: bool
        :param fitview: Set this to True to fit the view.
        
        
        """
        ...
    
    def AddToPostPass(self, op: BaseObject, bh: BaseDrawHelp) -> bool:
        """    
        Adds the object *op* to *DRAWPASS_XRAY*.
        
        .. code-block:: python
        
        def Draw(self, op, drawpass, bd, bh):
        if drawpass == c4d.DRAWPASS_OBJECT:
        bd.AddToPostPass(op, bh)
        ok = True
        elif drawpass == c4d.DRAWPASS_XRAY:
        ok = True
        
        if not ok:
        return c4d.DRAWRESULT_OK
        
        The object in this example is drawn both in regular and X-ray passes.
        
        .. note::
        
        This example is only relevant to :class:`ObjectData <c4d.plugins.ObjectData>` plugins.
        
        :type op: c4d.BaseObject
        :param op: The object to add to the X-ray pass.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The current base draw helper.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetObjectColor(self, bh: BaseDrawHelp, op: BaseObject) -> Vector:
        """    
        | Returns the wireframe color in editor for the specified object.
        | Some types of objects have certain colors.
        
        .. note::
        
        For polygon objects the main color is taken into account.
        
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The current base draw helper.
        :type op: c4d.BaseObject
        :param op: The object.
        :rtype: c4d.Vector
        :return: The object color.
        
        
        """
        ...
    
    def CheckColor(self, col: Vector) -> Vector:
        """    
        Makes sure that a color has at least 15% difference to the background color.
        
        :type col: c4d.Vector
        :param col: The original vector.
        :rtype: c4d.Vector
        :return: The new color, adjusted if needed.
        
        
        """
        ...
    
    def SetTransparency(self, trans: int) -> None:
        """    
        | Sets the transparency value for following polygons.
        | The range is 0 to 255, where 255 is 100% transparent.
        
        .. note::
        
        Use negative values for true transparencies and positive values for 'dotted' transparencies.
        
        :type trans: int
        :param trans: The transparency.
        
        
        """
        ...
    
    def GetTransparency(self) -> int:
        """    
        | Returns the current transparency value for polygons.
        | The range is 0 to 255, where 255 is 100% transparent.
        
        .. note::
        
        Negative values are true transparencies and positive values are 'dotted' transparencies.
        
        :rtype: int
        :return: The transparency.
        
        
        """
        ...
    
    def PointInRange(self, p: Vector, x: int, y: int) -> bool:
        """    
        Returns **True** if the screen point (x,y) is within a hit range of the world point p, i.e. if the screen point is close to the world points projection on the screen.
        
        :type p: c4d.Vector
        :param p: A point in world space.
        :type x: int
        :param x: Screen x coordinate.
        :type y: int
        :param y: Screen y coordinate.
        :rtype: bool
        :return: **True** if the point is within range, otherwise **True**.
        
        
        """
        ...
    
    def SetPen(self, col: Vector, flags: Optional[int] = ...) -> None:
        """    
        Sets the pen color for following drawing operations.
        
        :type col: c4d.Vector
        :param col: The new color.
        :type flags: int
        :param flags:
        
        .. include:: /consts/SET_PEN.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetPointSize(self, pointsize: float) -> None:
        """    
        Sets the drawn point size.
        
        :type pointsize: float
        :param pointsize: The new point size.
        
        
        """
        ...
    
    def SimpleShade(self, p: Vector, n: Vector) -> float:
        """    
        | A quick shading algorithm that only takes the angle to the camera and a default light into account.
        | You pass a point and a normal in world space and get back the intensity.
        
        .. note::
        
        Can be combined with :meth:`DrawPolygon` to draw simple shaded polygons.
        
        :type p: c4d.Vector
        :param p: A point in world space.
        :type n: c4d.Vector
        :param n: A normal in world space.
        :rtype: float
        :return: The intensity of the light. Between 0 and 1.
        
        
        """
        ...
    
    def ConvertColor(self, c: Vector) -> Vector:
        """    
        Converts colors from document color profile to viewport color profile.
        
        :type c: c4d.Vector
        :param c: The color to convert (document).
        :rtype: c4d.Vector
        :return: The converted color (viewport).
        
        
        """
        ...
    
    def ConvertColorReverse(self, c: Vector) -> Vector:
        """    
        Converts colors from viewport color profile to document color profile.
        
        :type c: c4d.Vector
        :param c: The color to convert (viewport).
        :rtype: c4d.Vector
        :return: The converted color (document).
        
        
        """
        ...
    
    def LineZOffset(self, offset: int) -> None:
        """    
        | Sets the current Z buffer offset.
        | Use this to for example draw lines over shaded polygons in front of the screen.
        | A higher *offset* value means a higher draw priority in the Z buffer. For example:
        
        - shaded polygon (level 0)
        - unselected edges (level 2)
        - selected edges (level 4)
        
        .. note::
        
        This function only affects the new draw functions below it, i.e. :meth:`DrawHandle`, :meth:`DrawTexture`, :meth:`DrawCircle`, :meth:`DrawBox`, and :meth:`DrawSphere`.
        
        :type offset: int
        :param offset: The new Z buffer offset.
        
        
        """
        ...
    
    def SetDepth(self, enable: bool) -> None:
        """    
        Enables/disables writing to the depth buffer.
        
        :type enable: bool
        :param enable: **True** to enable depth buffer writing, otherwise **False**.
        
        
        """
        ...
    
    def SetMatrix_Projection(self) -> None:
        """    
        For internal use only.
        
        
        """
        ...
    
    def SetMatrix_Screen(self, offset: int) -> None:
        """    
        Sets the transformation matrix to screen coordinates, i.e. from (0, 0) to (width, height).
        
        .. note::
        
        This function only affects the new draw functions below it, i.e. :meth:`DrawHandle`, :meth:`DrawTexture`, :meth:`DrawCircle`, :meth:`DrawBox`, and :meth:`DrawSphere`.
        
        :type offset: int
        :param offset:
        
        | Sets the current Z buffer offset.
        | Use this to for example draw lines over shaded polygons in front of the screen.
        | A higher zoffset value means a higher draw priority in the Z buffer. For example:
        
        - shaded polygon (level 0)
        - unselected edges (level 2)
        - selected edges (level 4)
        
        
        """
        ...
    
    def SetMatrix_Camera(self) -> None:
        """    
        Sets the transformation matrix to the camera system.
        
        .. note::
        
        This function only affects the new draw functions below it, i.e. :meth:`DrawHandle`, :meth:`DrawTexture`, :meth:`DrawCircle`, :meth:`DrawBox`, and :meth:`DrawSphere`.
        
        
        """
        ...
    
    def SetMatrix_Matrix(self, op: BaseObject, mg: Matrix, zoffset: int) -> None:
        """    
        | Sets the transformation matrix to the given matrix mg.
        | The matrix should transform coordinates passed to the draw functions into world coordinates.
        
        :type op: c4d.BaseObject
        :param op: A scene object. If passed this is used to compare if the same object is still used.
        :type mg: c4d.Matrix
        :param mg: The new transformation matrix.
        :type zoffset: int
        :param zoffset: Sets the current Z buffer offset.
        
        | Use this to for example draw lines over shaded polygons in front of the screen.
        | A higher zoffset value means a higher draw priority in the Z buffer. For example:
        
        - shaded polygon (level 0)
        - unselected edges (level 2)
        - selected edges (level 4)
        
        
        """
        ...
    
    def SetClipPlaneOffset(self, o: float) -> None:
        """    
        Offsets the OpenGL clipping planes by this offset.
        
        .. versionadded:: R14.014
        
        :type o: float
        :param o: The offset.
        
        
        """
        ...
    
    def DrawPoint2D(self, p: Vector) -> None:
        """    
        | Draws a one-pixel point in the current pen color at p.
        | The coordinates must be in screen space.
        
        .. note::
        
        Changes the matrix to screen with :meth:`SetMatrix_Screen` prior to drawing.
        
        :type p: c4d.Vector
        :param p: A point.
        
        
        """
        ...
    
    def DrawLine2D(self, p1: Vector, p2: Vector) -> None:
        """    
        | Draws a line in the current pen color between *p1* and *p2*.
        | The coordinates must be in screen space.
        
        .. note::
        
        Changes the matrix to screen with :meth:`SetMatrix_Screen` prior to drawing.
        
        :type p1: c4d.Vector
        :param p1: The start point.
        :type p2: c4d.Vector
        :param p2: The end point.
        
        
        """
        ...
    
    def DrawHandle2D(self, p: Vector, type: int) -> None:
        """    
        | Draws a standard handle (orange dot) at *p*.
        | The coordinates must be in screen space.
        
        .. note::
        
        Changes the matrix to screen with :meth:`SetMatrix_Screen` prior to drawing.
        
        :type p: c4d.Vector
        :param p: A point.
        :type type: int
        :param type: The handle type. Possible values are:
        
        .. include:: /consts/DRAWHANDLE.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawCircle2D(self, mx: int, my: int, rad: float) -> None:
        """    
        | Draws a circle in the current pen color with a radius of *rad* and the center at (*mx*, *my*).
        | The coordinates must be in screen space.
        
        .. note::
        
        Changes the matrix to screen with :meth:`SetMatrix_Screen` prior to drawing.
        
        :type mx: int
        :param mx: Center x coordinate.
        :type my: int
        :param my: Center y coordinate.
        :type rad: float
        :param rad: The radius.
        
        
        """
        ...
    
    def DrawLine(self, p1: Vector, p2: Vector, flags: int) -> None:
        """    
        | Draws a line in the current pen color between *p1* and *p2*.
        | The coordinates must be in world space.
        
        :type p1: c4d.Vector
        :param p1: The start point.
        :type p2: c4d.Vector
        :param p2: The end point.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/NOCLIP.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawHandle(self, vp: Vector, type: int, flags: int) -> None:
        """    
        | Draws a standard handle (orange dot) at *vp*.
        | The coordinates must be in world space.
        
        :type vp: c4d.Vector
        :param vp: A point.
        :type type: int
        :param type: The handle type. Valid types are:
        
        .. include:: /consts/DRAWHANDLE.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Private, set to *0*.
        
        
        """
        ...
    
    def DrawPoints(self, vp: Any, vc: Any, colcnt: int, vn: Any) -> None:
        """    
        Draws an array of points with individual colors.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type vp: any
        :param vp: An iteratable object with :class:`Vector <c4d.Vector>` as elements for the point coordinates.
        :type vc: any
        :param vc: An iteratable object with floats as elements for the points color.
        
        .. versionchanged:: R18.057
        
        Can be **None**.
        
        :type colcnt: int
        :param colcnt: The number of color elements, for example 3 for RGB.
        :type vn: any
        :param vn: Reserved for future use.
        
        .. versionchanged:: R18.057
        
        Can be **None**.
        
        
        """
        ...
    
    def DrawTexture(self, bmp: BaseBitmap, padr4: Any, cadr: Any, vnadr: Any, uvadr: Any, pntcnt: int, alphamode: int, flags: int) -> None:
        """    
        | Draws a colored and shaded texture polygon using the points in *padr4*, the colors in *cadr*, the normals in *vnadr* and the UV coordinates in *uvadr*.
        | Only a triangle or a quadrangle is accepted.
        | The colors are interpolated between the points and mutiplied with the texture color.
        | The shading is determined by :meth:`SetLightList`.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The texture to draw.
        :type padr4: list of :class:`Vector <c4d.Vector>`
        :param padr4: An iteratable object with :class:`Vector <c4d.Vector>` as elements for the points coordinates.
        :type cadr: list of :class:`Vector <c4d.Vector>`
        :param cadr: An iteratable object with :class:`Vector <c4d.Vector>` as elements for the colors. Must have `4` items regardless of *pntcnt*.
        :type vnadr: list of :class:`Vector <c4d.Vector>`
        :param vnadr: An iteratable object with :class:`Vector <c4d.Vector>` as elements for the point normals. Must have `4` items regardless of *pntcnt*.
        :type uvadr: list of :class:`Vector <c4d.Vector>`
        :param uvadr: An iteratable object with :class:`Vector <c4d.Vector>` as elements for the UV coordinates. Must have `4` items regardless of *pntcnt*.
        :type pntcnt: int
        :param pntcnt: The number of points in *padr4*. Must be either `3` (triangle) or `4` (quadrangle).
        :type alphamode: int
        :param alphamode: The alpha channel mode:
        
        .. include:: /consts/DRAW_ALPHA.rst
        :start-line: 3
        
        :type flags: int
        :param flags: A combination of these flags:
        
        .. include:: /consts/DRAW_TEXTUREFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawBox(self, m: Matrix, size: float, col: Vector, wire: bool) -> None:
        """    
        | Draws a box.
        | The eight points of the box are defined as:
        
        .. code-block:: python
        
        p = [c4d.Vector() for x in xrange(8)]
        p[0] = c4d.Vector(-size, -size, -size)
        p[1] = c4d.Vector( size, -size, -size)
        p[2] = c4d.Vector( size, -size,  size)
        p[3] = c4d.Vector(-size, -size,  size)
        p[4] = c4d.Vector(-size,  size, -size)
        p[5] = c4d.Vector( size,  size, -size)
        p[6] = c4d.Vector( size,  size,  size)
        p[7] = c4d.Vector(-size,  size,  size)
        
        To get arbitrary cubic forms, set size to 0.5 and multiply the vectors in the matrix by the length.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type m: c4d.Matrix
        :param m: A matrix describing the box.
        :type size: float
        :param size: The size of the box.
        :type col: c4d.Vector
        :param col: The color of the box.
        :type wire: bool
        :param wire: If this is **True** a wireframe is drawn.
        
        
        """
        ...
    
    def DrawCircle(self, m: Matrix) -> None:
        """    
        | Draws an ellipse in the current pen color.
        | The ellipse is specified by the matrix m, where *m.v1* and *m.v2* are the axis vectors and m.off is the center position. (*m.v3* is not used.)
        |
        | The coordinates must be in world space.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type m: c4d.Matrix
        :param m: A matrix describing the circle.
        
        
        """
        ...
    
    def DrawArc(self, pos: Vector, radius: float, angle_start: float, angle_end: float, subdiv: int, flags: int) -> None:
        """    
        | Draws an arc (section of a circle) in the current pen color at *pos*.
        | The coordinates must be in screen space.
        
        .. versionadded:: R14.014
        
        :type pos: c4d.Vector
        :param pos: Position of the rectangle that defines the arc.
        :type radius: float
        :param radius: The radius.
        :type angle_start: float
        :param angle_start: Start of the angle in radians.
        :type angle_end: float
        :param angle_end: End of the angle in radians.
        :type subdiv: int
        :param subdiv: The range between *angle_start* and *angle_end* is divided into *subdiv* line segments.
        :type flags: int
        :param flags:
        
        .. versionadded:: R16.021
        
        Flags:
        
        .. include:: /consts/NOCLIP.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawPolygon(self, p: Any, f: Any) -> None:
        """    
        | Draws a manually shaded triangle or quadrangle.
        | The corner points are given as a list of Vectors in *p*, and the corner colors as a corresponding list of Vectors in *f*.
        
        .. code-block:: python
        
        p = ( c4d.Vector(0,0,0), c4d.Vector(100,0,0), c4d.Vector(50,100,0) )
        f = ( c4d.Vector(1,0,0), c4d.Vector(0,0,1), c4d.Vector(0,1,0) )
        bd.DrawPolygon(p, f)
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type p: list of :class:`Vector <c4d.Vector>`
        :param p: A list of points.
        :type f: list of type :class:`Vector <c4d.Vector>`
        :param f: A list of points.
        
        
        """
        ...
    
    def DrawSphere(self, off: Vector, size: Vector, col: Vector, flags: int) -> None:
        """    
        Draws a sphere at position off with size specified by the size vector in each direction and color specified by col.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type off: c4d.Vector
        :param off: Position coordinate.
        :type size: c4d.Vector
        :param size: Sphere size.
        :type col: c4d.Vector
        :param col: The color.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/NOCLIP.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawArrayEnd(self) -> None:
        """    
        Each :meth:`DrawPolygon` puts the polygon into an internal array and draws the polygons when the array is full or an OpenGL state changes (e.g. the matrix). With this method you can force this operation.
        
        
        """
        ...
    
    def DrawPolygonObject(self, bh: BaseDrawHelp, op: BaseObject, flags: int, parent: BaseObject, col: Vector) -> None:
        """    
        Draws a polygon object into the view.
        
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: Needs to be passed along.
        :type op: c4d.BaseObject
        :param op: The object.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DRAWOBJECT.rst
        :start-line: 3
        
        :type parent: c4d.BaseObject
        :param parent:
        
        .. versionadded:: R21
        
        | This is used for the viewport filter.
        | Take the Floor object for example, it displays a polygon object in the viewport. If parent is set to **None** the drawn polygon is considered by the viewport filter.
        | If the Floor object has been passed to parent the Floor object is considered by the viewport filter instead.
        
        :type col: c4d.Vector
        :param col:
        
        .. versionadded:: R21
        
        The object's color.
        
        
        """
        ...
    
    def DrawObject(self, bh: BaseDrawHelp, op: BaseObject, flags: int, drawpass: int, parent: BaseObject, col: Vector) -> None:
        """    
        Draws a polygon object into the view.
        
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: Needs to be passed along.
        :type op: c4d.BaseObject
        :param op: The object.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/DRAWOBJECT.rst
        :start-line: 3
        
        :type drawpass: int
        :param drawpass: Drawpass:
        
        .. include:: /consts/DRAWPASS.rst
        :start-line: 3
        
        :type parent: c4d.BaseObject
        :param parent: The parent object, can be **None**.
        :type col: c4d.Vector
        :param col:
        
        .. versionadded:: R21
        
        The object's color.
        
        
        """
        ...
    
    def GetReductionMode(self) -> bool:
        """    
        Gets the reduction mode of the base draw.
        
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetDrawPass(self) -> int:
        """    
        Gets the current drawpass.
        
        .. versionadded:: R14.041
        
        :rtype: int
        :return: One of the following flags:
        
        .. include:: /consts/DRAWPASS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetHighlightPassColor(self, bh: BaseDrawHelp, lineObject: int) -> Vector:
        """    
        Returns the color in which the object has to be drawn in the highlight pass.
        
        .. versionadded:: R19
        
        .. note::
        
        This function should only be called in the highlight pass.
        
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The base draw help.
        :type lineObject: int
        :param lineObject: Must be set to **True** if the object is a line object.
        :rtype: c4d.Vector
        :return: The highlight color, or **None** if drawing the object can be skipped.
        
        
        """
        ...
    
    def SetLightList(self, mode: int) -> bool:
        """    
        Sets the lighting used by the draw functions.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        .. note::
        
        This method only affects the new 3D drawing methods, i.e. :meth:`DrawLine`, :meth:`DrawHandle`, :meth:`DrawTexture`, :meth:`DrawCircle`, :meth:`DrawBox`, :meth:`DrawPolygon` and :meth:`DrawSphere`.
        
        :type mode: int
        :param mode: The lighting mode:
        
        .. include:: /consts/BDRAW_SETLIGHTLIST.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def InitUndo(self, doc: BaseDocument) -> None:
        """    
        Called before a change is made to the view to add the old setting to the undo buffer for the view.
        
        .. note::
        
        This undo buffer is separate from the normal undo buffer.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The view's document.
        
        
        """
        ...
    
    def DoUndo(self, doc: BaseDocument) -> None:
        """    
        Performs an undo operation in the view.
        
        .. note::
        
        This is the same as the user selecting Undo View from within Cinema 4D.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The view's document.
        
        
        """
        ...
    
    def SetDrawParam(self, id: int, data: Any) -> None:
        """    
        Sets draw parameters.
        
        .. note::
        
        The coordinates must be in the space defined by :meth:`SetMatrix_Screen`, :meth:`SetMatrix_Camera` or :meth:`SetMatrix_Matrix`.
        
        :type id: int
        :param id: Parameter ID.
        :type data: any
        :param data: Depends on the parameter ID.
        
        
        """
        ...
    
    def GetDrawParam(self, id: int) -> Any:
        """    
        Gets draw parameters.
        
        :type id: int
        :param id: Parameter ID.
        :rtype: Any
        :return: Depends on the parameter ID.
        
        
        """
        ...
    
    def TestBreak(self) -> bool:
        """    
        Checks for thread breaks in the draw.
        
        :rtype: bool
        :return: **True** if a stopping condition has occurred, otherwise *False*.
        
        
        """
        ...
    
    def GetEditorWindow(self) -> EditorWindow:
        """    
        Get the editor window of the BaseDraw.
        
        :rtype: c4d.gui.EditorWindow
        :return: The editor window of the base draw.
        
        
        """
        ...
    
    def SetTexture(self, bm: BaseBitmap, tile: bool, alphamode: int, flags: int) -> None:
        """    
        Set a texture used by the vertex buffer.
        
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The texture's bitmap.
        :type tile: bool
        :param tile: Enable tiling.
        :type alphamode: int
        :param alphamode: Alpha channel mode:
        
        .. include:: /consts/DRAW_ALPHA.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Private, set to *0*.
        
        
        """
        ...
    
    def GetGridStep(self) -> Tuple[float, float]:
        """    
        Gets the grid spacing and the transparency value of the minor grid that fade when the user zoom in or out with dynamic grid.
        
        .. versionadded:: R14.014
        
        :rtype: tuple(float, float)
        :return: The workplane grid spacing and the transparency value of the minor grid.
        
        
        """
        ...
    
    def GetViewMatrix(self, n: int) -> Tuple[float]:
        """    
        Gets the view matrix.
        
        .. versionadded:: R14.014
        
        :type n: int
        :param n: View matrix to get:
        
        .. include:: /consts/DRAW_GET_VIEWMATRIX.rst
        :start-line: 3
        
        :rtype: tuple(16*float)
        :return: The view matrix (4x4 matrix).
        
        
        """
        ...
    
    def DrawHUDText(self, x: int, y: int, txt: str) -> None:
        """    
        Draws 2D text into the viewport in the style of the HUD.
        
        .. versionadded:: R18.020
        
        :type x: int
        :param x: The left X coordinate to draw the text at.
        :type y: int
        :param y: The upper Y coordinate to draw the text at.
        :type txt: str
        :param txt: The text to draw.
        
        
        """
        ...
    
    def DrawMultipleHUDText(self, texts: Any) -> None:
        """    
        Draws many 2D text into the viewport at once.
        
        .. versionadded:: R18.020
        
        :type texts: list of dict{'_txt': str, '_position': c4d.Vector}
        :param texts: The list of text entries and their screen space positions to draw to the HUD.
        
        
        """
        ...
    
    def IsMarkedAsGPURenderer(self) -> bool:
        """    
        Checks if the view is marked as GPU Renderer.
        
        .. versionadded:: R19.024
        
        :rtype: bool
        :return: **True** if the view is marked to run the GPU Renderer, otherwise **False**.
        
        
        """
        ...
    
    def IsGPURenderer(self) -> bool:
        """    
        Checks if the view is running the GPU Renderer.
        
        .. versionadded:: R19.024
        
        :rtype: bool
        :return: **True** if the view is running the GPU renderer, otherwise **False**.
        
        
        """
        ...
    

class CCurve(BaseList2D):
    def GetKeyCount(self) -> int:
        """    
        Returns the count of :class:`CKey <c4d.CKey>`
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetKey(self, index: int) -> CKey:
        """    
        Get a writeable key by index.
        
        :type index: int
        :param index: Key index.
        :raise IndexError: If key *index* is out of range : *0<=index<*:meth:`GetKeyCount`.
        :rtype: c4d.CKey
        :return: The key found, or **None**.
        
        
        """
        ...
    
    def FindKey(self, time: BaseTime, match: int) -> None:
        """    
        Find a writable key by time.
        
        .. code-block:: python
        
        found = curve.FindKey(time)
        if found==None: return
        
        key = found["key"] #The found key
        index = found["idx"] #The index of the found key
        
        :type time: c4d.BaseTime
        :param time: A time.
        :type match: int
        :param match: Search method:
        
        .. include:: /consts/FINDANIM.rst
        :start-line: 3
        
        :rtype: dict{**key**: :class:`CKey <c4d.CKey>`, **int**: int}
        :return: Dict with the found key and index, or **None**.
        
        
        """
        ...
    
    def AddKey(self, time: BaseTime, bUndo: bool, SynchronizeKeys: bool) -> None:
        """    
        Find a writable key by time.
        
        .. code-block:: python
        
        added = curve.AddKey(time)
        if added==None: return
        
        key = found["key"] #The found key
        index = found["nidx"] #The index of the found key
        
        :type time: c4d.BaseTime
        :param time: The time to add the key at.
        :type bUndo: bool
        :param bUndo:
        
        .. versionadded:: R18.020
        
        If **True** this action will be undoable.
        
        .. note::
        
        The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        :type SynchronizeKeys: bool
        :param SynchronizeKeys:
        
        .. versionadded:: R18.020
        
        If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        
        :rtype: dict{'nidx': int, 'key': :class:`c4d.CKey`}
        :return: The added key index and object (**None** if it failed).
        
        
        """
        ...
    
    def AddKeyAdaptTangent(self, time: BaseTime, bUndo: bool, SynchronizeKeys: bool) -> None:
        """    
        Add a key to the curve but retain the curve's current curvature.
        
        .. versionadded:: R18.020
        
        :type time: c4d.BaseTime
        :param time: The time to add the key at.
        :type bUndo: bool
        :param bUndo: If **True** this action will be undoable. The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        :type SynchronizeKeys: bool
        :param SynchronizeKeys: If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        :rtype: dict{'nidx': int, 'key': :class:`c4d.CKey`}
        :return: The added key index and object (**None** if it failed).
        
        
        """
        ...
    
    def InsertKey(self, ckey: CKey, bUndo: bool, SynchronizeKeys: bool) -> bool:
        """    
        Insert a key into this curve.
        
        :type ckey: c4d.CKey
        :param ckey: The key to insert.
        :type bUndo: bool
        :param bUndo:
        
        .. versionadded:: R18.020
        
        If **True** this action will be undoable.
        
        .. note::
        
        The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        :type SynchronizeKeys: bool
        :param SynchronizeKeys:
        
        .. versionadded:: R18.020
        
        If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DelKey(self, index: int, bUndo: bool, SynchronizeKeys: bool) -> bool:
        """    
        Delete a key from this curve.
        
        :type index: int
        :param index: The index of the key to delete.
        :raise IndexError: If key *index* is out of range : *0<=index<*:meth:`GetKeyCount`.
        :type bUndo: bool
        :param bUndo:
        
        .. versionadded:: R18.020
        
        If **True** this action will be undoable.
        
        .. note::
        
        The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        :type SynchronizeKeys: bool
        :param SynchronizeKeys:
        
        .. versionadded:: R18.020
        
        If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MoveKey(self, time: BaseTime, idx: int, seq: Optional[CCurve] = ..., bUndo: Optional[bool] = ..., SynchronizeKeys: Optional[bool] = ...) -> int:
        """    
        Move a key in the curve.
        
        :type time: c4d.BaseTime
        :param time: The new time.
        :type idx: int
        :param idx: The index of the key to move.
        :raise IndexError: If key *idx* is out of range : *0<=idx<*:meth:`GetKeyCount`.
        :type seq: c4d.CCurve
        :param seq: Optional destination curve.
        :type bUndo: bool
        :param bUndo:
        
        .. versionadded:: R18.020
        
        If **True** this action will be undoable.
        
        .. note::
        
        The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        :type SynchronizeKeys: bool
        :param SynchronizeKeys:
        
        .. versionadded:: R18.020
        
        If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        
        :rtype: int
        :return: The new index.
        
        
        """
        ...
    
    def FlushKeys(self, bUndo: bool, SynchronizeKeys: bool) -> None:
        """    
        Remove all keys from this curve.
        
        :type bUndo: bool
        :param bUndo:
        
        .. versionadded:: R18.020
        
        If **True** this action will be undoable.
        
        .. note::
        
        The caller has to to manage start/end of undo actions with :meth:`BaseDocument.StartUndo`/:meth:`EndUndo() <BaseDocument.EndUndo>`.
        
        :type SynchronizeKeys: bool
        :param SynchronizeKeys:
        
        .. versionadded:: R18.020
        
        If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.
        
        
        """
        ...
    
    def SortKeysByTime(self) -> None:
        """    
        Private. Should not be used.
        
        
        """
        ...
    
    def SetKeyDirty(self) -> None:
        """    
        Set keys to dirty. Equivalent to *SetDirty(DIRTY_CHILDREN)*.
        
        
        """
        ...
    
    def GetTrack(self) -> CTrack:
        """    
        Get the track of this curve.
        
        :rtype: c4d.CTrack
        :return: The track of this curve.
        
        
        """
        ...
    
    def GetValue(self, time: BaseTime, fps: int) -> float:
        """    
        Get the value calculated at *time*, taking into account things like timecurves.
        
        :type time: c4d.BaseTime
        :param time: The time to calculate the value at.
        :type fps: int
        :param fps:
        
        .. deprecated:: R17.048
        
        The number of frames per second.
        
        :rtype: float
        :return: The calculated value.
        
        
        """
        ...
    
    def GetTangents(self, kidx: int) -> Tuple[float, float, float, float]:
        """    
        Computes the tangents of a key, taking into account all options like zero slope, link slope etc.
        
        :type kidx: int
        :param kidx: The key index. 0 <= kidx < :meth:`CCurve.GetKeyCount()`.
        :rtype: tuple(float, float, float, float)
        :return: A tuple in the following order:
        
        - The left value.
        - The right value.
        - The left time.
        - The right time.
        
        :raise OutOfRange: if kidx < 0 or kidx > :meth:`CCurve.GetKeyCount()`.
        
        
        """
        ...
    
    def SetKeyDefault(self, doc: BaseDocument, kidx: int) -> None:
        """    
        Set the defaults for key *kidx* for the curve.
        
        .. note::
        
        | This includes lock, mute, clamp, break, auto properties, interpolation and tangents.
        | This way you can set up a value and complete the missing properties with the defaults.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The curve's document.
        :type kidx: int
        :param kidx: The key index.
        
        
        """
        ...
    
    def GetStartTime(self) -> BaseTime:
        """    
        Returns the start time of the curve.
        
        .. versionadded:: R19
        
        :rtype: c4d.BaseTime
        :return: The start time of the curve.
        
        
        """
        ...
    
    def GetEndTime(self) -> BaseTime:
        """    
        Returns the end time of the curve.
        
        .. versionadded:: R19
        
        :rtype: c4d.BaseTime
        :return: The end time of the curve.
        
        
        """
        ...
    
    def FindNextUnmuted(self, index: int) -> None:
        """    
        Returns the next unmuted key.
        
        .. versionadded:: R19
        
        :type index: intcl
        :param index: The key index to start the search from: `0` <= *idx* < :meth:`GetKeyCount`
        :rtype: tuple(:class:`c4d.CKey`, int)
        :return: The next unmuted key and its index, or **None** if there is no next unmuted key.
        
        
        """
        ...
    
    def FindPrevUnmuted(self, index: int) -> None:
        """    
        Returns the previous unmuted key.
        
        .. versionadded:: R19
        
        :type index: int
        :param index: The key index to start the search from: `0` <= *idx* < :meth:`GetKeyCount`
        :rtype: tuple(:class:`c4d.CKey`, int)
        :return: The previous unmuted key and its index, or **None** if there is no previous unmuted key.
        
        
        """
        ...
    

class CTrack(BaseList2D):
    def __init__(self, bl: BaseList2D, id: DescID) -> None:
        """    
        Allocates a track object.
        
        :type bl: c4d.BaseList2D
        :param bl: Object to allocate the track for.
        :type id: c4d.DescID
        :param id: Description ID to allocate the track for.
        
        For instance a position track will be allocated like this.
        
        .. code-block:: python
        
        tr=c4d.CTrack(op, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))
        
        A track of type **int** will be allocated like this.
        
        .. code-block:: python
        
        tr=c4d.CTrack(op, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_VISIBILITY_EDITOR, c4d.DTYPE_LONG, 0, )))
        
        For a plugin and special tracks you pass the ID.
        
        .. code-block:: python
        
        tr=c4d.CTrack(op,c4d.DescLevel(ID, ID, 0))
        
        IDs for Cinema 4D's special tracks are:
        
        .. include:: /types/tracks.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetDescriptionID(self) -> DescID:
        """    
        Retrieve the description ID of this track.
        
        :rtype: c4d.DescID
        :return: The description ID.
        
        
        """
        ...
    
    def SetDescriptionID(self, object: BaseList2D, id: DescID) -> bool:
        """    
        Set the description ID of this track.
        
        :type object: c4d.BaseList2D
        :param object: Object for the new description ID.
        :type id: c4d.DescID
        :param id: New description ID.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetCurve(self, type: BaseList2D, bCreate: bool) -> CCurve:
        """    
        Get a curve of this track.
        
        :type type: c4d.BaseList2D
        :param type: The curve type:
        
        .. include:: /consts/CCURVE.rst
        :start-line: 3
        
        :type bCreate: bool
        :param bCreate: If True a curve is created if none exists.
        :rtype: c4d.CCurve
        :return: The curve of this track.
        
        
        """
        ...
    
    def GetTrackCategory(self) -> int:
        """    
        Get a curve of this track.
        
        :rtype: int
        :return: Track category:
        
        .. include:: /consts/CTRACK_CATEGORY.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetObject(self) -> BaseList2D:
        """    
        Get the host object of this track.
        
        :rtype: c4d.BaseList2D
        :return: The host object or **None**.
        
        
        """
        ...
    
    def GetBefore(self) -> int:
        """    
        Get the pre track loop type of this track.
        
        :rtype: int
        :return: Loop type:
        
        .. include:: /consts/CLOOP.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetAfter(self) -> int:
        """    
        Get the pre track loop type of this track.
        
        :rtype: int
        :return: Loop type:
        
        .. include:: /consts/CLOOP.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetBefore(self, type: int) -> None:
        """    
        Set the pre track loop type of this track.
        
        :type type: int
        :param type: Loop type:
        
        .. include:: /consts/CLOOP.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetAfter(self, type: int) -> None:
        """    
        Set the post track loop type of this track.
        
        :type type: int
        :param type: Loop type:
        
        .. include:: /consts/CLOOP.rst
        :start-line: 3
        
        
        """
        ...
    
    def FlushData(self) -> None:
        """    
        Clears the data of the track itself, for example removes time curves, pre/post loop type, etc.
        
        
        """
        ...
    
    def GetValue(self, doc: BaseDocument, time: BaseTime, fps: int) -> float:
        """    
        Retrieve the value of this track at *time*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type time: c4d.BaseTime
        :param time: The time.
        :type fps: int
        :param fps:
        
        .. deprecated:: R17.048
        
        The number of frames per second.
        
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def Remap(self, time: float) -> None:
        """    
        Remaps *time*.
        
        :type time: float
        :param time: The input time.
        :rtype: dict{'ret_time': float, 'ret_cycle' int}
        :return: The output time and cycle, or **None** if *time* could not be remapped.
        
        
        """
        ...
    
    def FillKey(self, doc: BaseDocument, bl: BaseList2D, key: CKey) -> bool:
        """    
        Fills *key* with default values.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type bl: c4d.BaseList2D
        :param bl: The object of the key to fill.
        :type key: c4d.CKey
        :param key: The key to fill.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetHeight(self) -> int:
        """    
        Get the height of the track.
        
        :rtype: int
        :return: The height in pixels.
        
        
        """
        ...
    
    def GetUnit(self) -> Tuple[int, float]:
        """    
        Get the unit and step of the track.
        
        :rtype: tuple(int, float)
        :return: The unit and the step. The units:
        
        .. include:: /consts/UNIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetTLHeight(self, id: int) -> int:
        """    
        Get the height of the mini f-curves in the timeline.
        
        :type id: int
        :param id: 0-3 for one of the four timelines.
        :rtype: int
        :return: The height of the mini f-curve in pixels.
        
        
        """
        ...
    
    def SetTLHeight(self, id: int, size: int) -> None:
        """    
        Get the height of the track.
        
        :type id: int
        :param id: 0-3 for one of the four timelines.
        :type size: int
        :param size: The new size of the mini f-curve in pixels.
        
        
        """
        ...
    
    def IsSynchronized(self) -> bool:
        """    
        Checks if keys are synchronized with other Component tracks (Vector Track only).
        
        .. versionadded:: R18.020
        
        :rtype: bool
        :return: **True** if track is synchronized, otherwise **False**.
        
        
        """
        ...
    
    def SetSynchronized(self, synch: bool) -> None:
        """    
        Sets synchronization between component Track (Vector Track only).
        
        .. versionadded:: R18.020
        
        :type synch: bool
        :param synch: **True** if Track needs to be synchronized, otherwise **False**.
        
        
        """
        ...
    
    def GetTimeTrack(self, doc: BaseDocument) -> CTrack:
        """    
        Returns the time track.
        
        .. versionadded:: R19
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: c4d.CTrack
        :return: The time track.
        
        
        """
        ...
    
    def SetTimeTrack(self, track: CTrack) -> None:
        """    
        Sets the time track.
        
        .. versionadded:: R19
        
        :type track: c4d.CTrack
        :param track: The time track to set.
        
        
        """
        ...
    
    def Draw(self, map: GeClipMap, clip_left: BaseTime, clip_right: BaseTime) -> bool:
        """    
        Draws the track into a clip map bitmap, if drawing is supported.
        
        .. versionadded:: R19
        
        :type map: c4d.bitmaps.GeClipMap
        :param map: The clip map to draw into.
        :type clip_left: c4d.BaseTime
        :param clip_left: The left time clipping.
        :type clip_right: c4d.BaseTime
        :param clip_right: The right time clipping.
        :rtype: bool
        :return: **True** if the track was drawn, otherwise **False**.
        
        
        """
        ...
    
    def GetTrackInformation(self, doc: BaseDocument, key: CKey) -> str:
        """    
        Returns the track information at the current time in *doc*, or at *key* if specified.
        
        .. versionadded:: R19
        
        .. note::
        
        The track information string is displayed in tooltips inside the Timeline for instance.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :type key: c4d.CKey
        :param key: Pass a key to retrieve the track information at, otherwise **None** to retrieve it at the current time.
        :rtype: str
        :return: The information string.
        
        
        """
        ...
    
    def SetTrackInformation(self, doc: BaseDocument, key: CKey, info: str) -> bool:
        """    
        Sets the track information at the current time in *doc*, or at *key* if specified.
        
        .. versionadded:: R19
        
        .. note::
        
        The track information string is displayed in tooltips inside the Timeline for instance.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :type key: c4d.CKey
        :param key: Pass a key to set the track information at, otherwise **None** to set it at the current time.
        :type info: str
        :param info: The information string to set.
        :rtype: bool
        :return: **True** if the track information was set, otherwise **False**.
        
        
        """
        ...
    

class CustomDataType(object):
    ...

class UnitScaleData(CustomDataType):
    def __init__(self, v: UnitScaleData) -> None:
        """    
        :type v: c4d.UnitScaleData
        :param v: Copy constructor.
        :rtype: c4d.UnitScaleData
        :return: The new unit scale data.
        
        
        """
        ...
    
    def SetUnitScale(self, scale: float, unit: int) -> bool:
        """    
        Sets the values for the unit scale data type.
        
        :type scale: float
        :param scale: The unit scale.
        :type unit: int
        :param unit: One of the following unit:
        
        .. include:: /consts/DOCUMENT_UNIT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**
        
        
        """
        ...
    
    def GetUnitScale(self) -> Tuple[float, int]:
        """    
        Retrieves the values of the unit scale data type.
        
        .. code-block:: python
        
        scale, unit = data.GetUnitScale()
        
        :rtype: tuple(float, int)
        :return: The scale and unit data
        
        
        """
        ...
    

class SplineData(CustomDataType):
    def __init__(self, v: Optional[SplineData] = ...) -> None:
        """    
        Creates a default 2 points spline.
        
        :type v: c4d.SplineData
        :param v: Source spline data for copy constructor.
        :rtype: c4d.SplineData
        :return: The spline data instance.
        
        
        """
        ...
    
    def SelectAll(self) -> None:
        """    
        Selects all points.
        
        
        """
        ...
    
    def Flip(self) -> None:
        """    
        Flips the spline.
        
        
        """
        ...
    
    def Mirror(self) -> None:
        """    
        Mirrors the spline.
        
        
        """
        ...
    
    def SetRound(self, r: float) -> None:
        """    
        Set the tension.
        
        :type r: float
        :param r: The tension
        
        
        """
        ...
    
    def GetRound(self) -> float:
        """    
        .. deprecated:: Since R13
        
        This method is only available in R12 and always returns 0.0 in R13.
        
        Gets the tension.
        
        :rtype: float
        :return: Tension.
        
        
        """
        ...
    
    def Maximum(self) -> None:
        """    
        Makes all Y coordinates less than or equal to 1.
        
        
        """
        ...
    
    def Minimum(self) -> None:
        """    
        Makes all Y coordinates greater than or equal to 0.
        
        
        """
        ...
    
    def SetType(self, id: int, bAll: bool) -> bool:
        """    
        Sets the interpolation type of the selected knots.
        
        :param id: The interpolation type.
        :type id: int
        
        .. include:: /consts/SPLINETYPE.rst
        :start-line: 3
        
        :param bAll: Pass **True** to set all knots, **False** to set selected knots only.
        :type bAll: bool
        :return: **True** if successful, otherwise **False**.
        :rtype: bool
        
        
        """
        ...
    
    def SetZero(self, bY: bool, bAll: bool) -> bool:
        """    
        Sets the tangents of selected knots to zero.
        
        :type bY: bool
        :param bY: **True** to set the tangets' Y coordinate to zero, **False** to set the X coordinate.
        :type bAll: bool
        :param bAll: **True** to set all tangents, **False** to set the tangents of selected knots only.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitDefaultFlag(self, flag: int) -> bool:
        """    
        Sets the knot flag for selected knots.
        
        :type flag: int
        :param flag: A combination of these flags:
        
        .. include:: /consts/FLAG_KNOT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DeleteAllPoints(self) -> None:
        """    
        Deletes all points.
        
        
        """
        ...
    
    def MakePointBuffer(self, lPoints: int) -> bool:
        """    
        Makes an uninitialized spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeLinearSplineLinear(self, lPoints: int) -> bool:
        """    
        Makes a linear spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeLinearSplineBezier(self, lPoints: int) -> bool:
        """    
        Makes a linear bezier spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeSquareSpline(self, lPoints: int) -> bool:
        """    
        Makes a square spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeCubicSpline(self, lPoints: int) -> bool:
        """    
        Makes a cubic spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeRootSpline(self, lPoints: int) -> bool:
        """    
        Makes a root spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeInversSpline(self, lPoints: int) -> bool:
        """    
        Makes an inverse spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeSinSpline(self, lPoints: int) -> bool:
        """    
        Makes a sinus spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeAbsCosSpline(self, lPoints: int) -> bool:
        """    
        Makes an absolute cosinus spline with *lPoints* number of points.
        
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeUserSpline(self, str: str, lPoints: int) -> bool:
        """    
        Makes a user spline from *str* with *lPoints* number of points.
        
        :type str: str
        :param str: User spline string. Any valid formula can be used.
        :type lPoints: int
        :param lPoints: Number of points, or -1 to get the default value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DeleteKnot(self, a: int) -> bool:
        """    
        Deletes a knot.
        
        :type a: int
        :param a: The knot index to delete.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InsertKnot(self, x: float, y: float, flags: int) -> int:
        """    
        Inserts a knot.
        
        :type x: float
        :param x: X coordinate
        :type y: float
        :param y: Y coordinate
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/FLAG_KNOT.rst
        :start-line: 3
        
        :rtype: int
        :return: Knot index.
        
        
        """
        ...
    
    def GetKnots(self) -> None:
        """    
        Returns all knots.
        
        :rtype: list of dict{**vPos**: :class:`Vector <c4d.Vector>`, **lFlagsSettings**: int, **bSelect**: bool, **vTangentLeft**: :class:`Vector <c4d.Vector>`, **vTangentRight**: :class:`Vector <c4d.Vector>`, **interpol**: int}
        :return: A list of dictionaries with information about the knot.
        
        
        """
        ...
    
    def SetKnot(self, index: int, vPos: Vector, lFlagsSettings: int, bSelect: bool, vTangentLeft: Vector, vTangentRight: Vector, interpol: int) -> None:
        """    
        Sets knot properties.
        
        :type index: int
        :param index: The knot index.
        :raise RangeError: If the knot *index* is out of range : *0<=index<*:meth:`GetKnotCount`.
        :type vPos: c4d.Vector
        :param vPos: Knot position.
        :type lFlagsSettings: int
        :param lFlagsSettings: Contains knot flags:
        
        .. include:: /consts/FLAG_KNOT.rst
        :start-line: 3
        
        .. note::
        
        Also contains the point index ID. The ID can be accessed using these functions:
        
        .. code-block:: python
        
        def SplineKnotGetID(flags):
        return ((flags >> 16) & 0x0000ffff)
        
        def SplineKnotSetID(flags, flag_id):
        flags = (flags & 65535) | ((flag_id & 0x0000ffff) << 16)
        
        .. important::
        
        This means that the flags must only be accessed using **'|='** and **'&='** (a good advice for any set of flags, for maximum forward compatibility).
        
        :type bSelect: bool
        :param bSelect: Internal select state. Do not change this.
        :type vTangentLeft: c4d.Vector
        :param vTangentLeft: The left tangent.
        :type vTangentRight: c4d.Vector
        :param vTangentRight: The right tangent.
        :type interpol: int
        :param interpol: Spline knot's interpolation:
        
        .. include:: /consts/CustomSplineKnotInterpolation.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetPoint(self, r: float) -> Vector:
        """    
        Gets a point from its X coordinate.
        
        :type r: float
        :param r: The x position
        :rtype: c4d.Vector
        :return: The position
        
        
        """
        ...
    
    def GetSelectCount(self) -> int:
        """    
        Returns the count of knots which are selected.
        
        :rtype: int
        :return: The count
        
        
        """
        ...
    
    def GetKnotCount(self) -> int:
        """    
        Gets the knot count.
        
        :rtype: int
        :return: Knot count.
        
        
        """
        ...
    
    def GetRange(self) -> None:
        """    
        Gets the range of the spline.
        
        .. code-block:: python
        
        def PrintRange(sd):
        sdrange = sd.GetRange()
        if not range: return
        
        print sdrange["xmin"], sdrange["xmax"], sdrange["xstep"], sdrange["ymin"], sdrange["ymax"], sdrange["ystep"]
        
        :rtype: dict{**xmin**: float, **xmax**: float, **xstep**: float, **ymin**: float, **ymax**: float, **ystep**: float}
        :return: The range dictionary or **None**.
        
        
        """
        ...
    
    def SortKnots(self) -> int:
        """    
        Sort the knots.
        
        :rtype: int
        :return: The new index of the active knot.
        
        
        """
        ...
    
    def SetRange(self, xmin: float, xmax: float, xsteps: float, ymin: float, ymax: float, ysteps: float) -> None:
        """    
        Set the range of the spline.
        
        :type xmin: float
        :param xmin: The X min range.
        :type xmax: float
        :param xmax: The X max range.
        :type xsteps: float
        :param xsteps: The X steps.
        :type ymin: float
        :param ymin: The Y min range.
        :type ymax: float
        :param ymax: The Y max range.
        :type ysteps: float
        :param ysteps: The Y steps.
        
        
        """
        ...
    
    def AdaptRange(self, xmin: float, xmax: float, xsteps: float, ymin: float, ymax: float, ysteps: float) -> None:
        """    
        Adapts the internal 0-1 range of the old spline GUI to the range set by *xmin*, *xmax*, *ymin* and *ymax*.
        
        :type xmin: float
        :param xmin: The new X minimum.
        :type xmax: float
        :param xmax: The new X maximum.
        :type xsteps: float
        :param xsteps: The new X step size.
        :type ymin: float
        :param ymin: The new Y minimum.
        :type ymax: float
        :param ymax: The new Y maximum.
        :type ysteps: float
        :param ysteps: The new Y step size.
        
        
        """
        ...
    
    def CopyTo(self, pDest: SplineData) -> bool:
        """    
        Copies this spline data values into the destination spline data.
        
        .. versionadded:: R14.014
        
        :type pDest: c4d.SplineData
        :param pDest: The destination spline data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**
        
        
        """
        ...
    

class SoundEffectorData(CustomDataType):
    def __init__(self, v: SoundEffectorData) -> None:
        """    
        Creates a :class:`c4d.SoundEffectorData`.
        
        :type v: c4d.SoundEffectorData
        :param v: An optional :class:`c4d.SoundEffectorData` to copy.
        :rtype: c4d.SoundEffectorData
        :return: The new :class:`SoundEffectorData <c4d.SoundEffectorData>`.
        
        
        """
        ...
    
    def CreateProbe(self, left: float, right: float, top: float, bottom: float, selected: bool) -> int:
        """    
        Creates a probe.
        
        :type left: float
        :param left: The left side of the probe in Hertz `[1,22050]`.
        :type right: float
        :param right: The right side of the probe in Hertz `[1,22050]`.
        :type top: float
        :param top: The top edge of the probe in the range `[0,1]`.
        :type bottom: float
        :param bottom: The bottom edge of the probe in the range `[0,1]`.
        :type selected: bool
        :param selected: **True** to select the created probe. Other probes are not deselected in the operation.
        :rtype: int
        :return: The created probe's index.
        
        
        """
        ...
    
    def GetProbeCount(self) -> int:
        """    
        Retrieves the number of probes owned by the sound effector data.
        
        :rtype: int
        :return: The probe count.
        
        
        """
        ...
    
    def GetProbe(self, index: int) -> Dict[str, Any]:
        """    
        Retrieves the probe at the specified *index*.
        
        :type index: int
        :param index: The probe index.
        :rtype: dict
        :return: The probe, or **None** if the function fails. The dictionary contains the following data:
        
        ============== ===================== =======================================================================================================================================================
        `left`         float                 The left value of probe in Hertz.
        `right`        float                 The right value of probe in Hertz.
        `top`          float                 The top value of probe in Hertz.
        `bottom`       float                 The bottom value of probe in Hertz.
        `strength`     float                 The overall strength multiplier for the probe.
        `clamp`        bool                  **True** limits the output of the probe from `0.0` to `1.0` and ignores values outside of the range.
        `samplingMode` int                   The probe mode.
        `colorMode`    int                   The color mode.
        `color`        :class:`c4d.Vector`   The color of the probe used when `colorMode` is Custom Color.
        `gradient`     :class:`c4d.Gradient` The gradient of the probe used when `colorMode` is Custom Gradient.
        ============== ===================== =======================================================================================================================================================
        
        
        """
        ...
    
    def SetProbe(self, index: int, probe: Dict[str, Any]) -> None:
        """    
        Sets the probe at the specified *index*.
        
        :type index: int
        :param index: The index of the probe to set.
        :type probe: dict
        :param probe: The probe data to set:
        
        ============== ===================== ======================================================================================================================================================================
        `left`         float                 The left value of probe in Hertz.
        `right`        float                 The right value of probe in Hertz.
        `top`          float                 The top value of probe in Hertz.
        `bottom`       float                 The bottom value of probe in Hertz.
        `strength`     float                 The overall strength multiplier for the probe.
        `clamp`        bool                  Set to **True** to limit the output of the probe from `0.0` to `1.0` and to ignore values outside of the range.
        `samplingMode` int                   The probe mode.
        `colorMode`    int                   The color mode.
        `color`        :class:`c4d.Vector`   The color of the probe used when `colorMode` is Custom Color.
        `gradient`     :class:`c4d.Gradient` The gradient of the probe used when `colorMode` is Custom Gradient.
        ============== ===================== ======================================================================================================================================================================
        
        
        """
        ...
    
    def DeleteProbe(self, index: int) -> bool:
        """    
        Deletes the probe at the specified *index*.
        
        :type index: int
        :param index: The index of the probe to delete.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def UpdateProbeOrder(self) -> None:
        """    
        Updates the probes.
        
        .. note::
        
        Must be called after adjusting any probes left or right values to update the order that the probes are calculated in.
        
        
        """
        ...
    
    def GetRange(self) -> Tuple[float, float, float, float]:
        """    
        Retrieves the range of the sound effector data.
        
        .. warning::
        
        Only valid if the data is shown in the sound sound effector GUI.
        
        :rtype: tuple(float, float, float, float)
        :return: A tuple with the left, right, top and bottom values.
        
        
        """
        ...
    
    def SetRange(self, left: float, right: float, top: float, bottom: float) -> None:
        """    
        Sets the range of the sound effector data.
        
        .. warning::
        
        Only valid if the data is shown in the sound effector GUI.
        
        :type left: float
        :param left: The left value to set.
        :type right: float
        :param right: The right value to set.
        :type top: float
        :param top: The top value to set.
        :type bottom: float
        :param bottom: The bottom value to set.
        
        
        """
        ...
    
    def GetLinLog(self) -> float:
        """    
        Retrieves the blend value for the linear/logarithmic slider.
        
        :rtype: float
        :return: The blend percentage: `0%` = linear, `100%` = log10.
        
        
        """
        ...
    
    def SetLinLog(self, value: float) -> None:
        """    
        Sets the the blend value for the linear/logarithmic slider.
        
        :type value: float
        :param value: The blend percentage to set: `0%` = linear, `100%` = log10.
        
        
        """
        ...
    
    def GetFreeze(self) -> bool:
        """    
        Retrieves the freeze state.
        
        :rtype: bool
        :return: **True** if freeze is enabled, otherwise **False**.
        
        
        """
        ...
    
    def SetFreeze(self, freeze: bool) -> None:
        """    
        Sets the freeze state.
        
        :type freeze: bool
        :param freeze: **True** to enable freeze, otherwise **False**.
        
        
        """
        ...
    
    def GetGradient(self) -> Gradient:
        """    
        Retrieves the global gradient.
        
        :rtype: c4d.Gradient
        :return: The global gradient, or **None** if the function fails.
        
        
        """
        ...
    
    def GetGradientDirection(self) -> int:
        """    
        Retrieves the global gradient direction.
        
        :rtype: int
        :return: The global gradient direction: `0` for vertical (volume), `1` for horizontal (frequency).
        
        
        """
        ...
    
    def SetGradientDirection(self, direction: int) -> None:
        """    
        Sets the global gradient direction.
        
        :type direction: int
        :param direction: The global gradient direction to set: `0` for vertical (volume), `1` for horizontal (frequency).
        
        
        """
        ...
    
    def InitSampling(self, doc: BaseDocument) -> bool:
        """    
        Initializes the sampling functionality of the sound effector data.
        
        .. note::
        
        Must be called before :meth:`Sample`. :meth:`FreeSampling` must be invoked afterwards.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FreeSampling(self) -> bool:
        """    
        Frees the memory used for sampling.
        
        .. note::
        
        Must be invoked after :meth:`InitSampling` has been called.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Sample(self, index: int, count: int) -> None:
        """    
        Samples the sound file using the probes.
        
        :type index: int
        :param index: The index of the element to sample.
        :type count: int
        :param count: The number of elements in the array being sampled.
        :rtype: tuple(float, :class:`c4d.Vector`)
        :return: A tuple with the output value and color (both **None** if the function failed).
        
        
        """
        ...
    
    def SetActiveSoundTrack(self, track: CTrack, doc: BaseDocument) -> bool:
        """    
        Sets the active sound track.
        
        :type track: c4d.CTrack
        :param track: The sound track to set.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetActiveSoundTrack(self, doc: BaseDocument) -> CTrack:
        """    
        Retrieves the active sound track.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :rtype: c4d.CTrack
        :return: The active sound track, or **None** if the function fails.
        
        
        """
        ...
    
    def CopyTo(self, dest: SoundEffectorData) -> bool:
        """    
        Copies the sound effector data.
        
        :type dest: c4d.SoundEffectorData
        :param dest: The destination sound effector data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**
        
        
        """
        ...
    

class RangeData(CustomDataType):
    def __init__(self, v: RangeData) -> None:
        """    
        Creates a :class:`c4d.RangeData`.
        
        :type v: c4d.RangeData
        :param v: An optional :class:`c4d.RangeData` to copy.
        :rtype: c4d.RangeData
        :return: The new :class:`RangeData <c4d.RangeData>`.
        
        
        """
        ...
    
    def Init(self, rangeNumber: int) -> None:
        """    
        Initializes the range data with the passed range number.
        
        .. note::
        
        The interval in between ranges will be the same.
        
        :type rangeNumber: int
        :param rangeNumber: The number of ranges.
        
        
        """
        ...
    
    def Reset(self, invalidateObject: bool) -> None:
        """    
        Resets the range data to the initial state.
        
        :type invalidateObject: bool
        :param invalidateObject: **True** to initialize the ranges after reset operation, otherwise the object will be initialized but functions with one single range.
        
        
        """
        ...
    
    def CopyTo(self, dest: RangeData) -> None:
        """    
        Copies the range data.
        
        :type dest: c4d.RangeData
        :param dest: The destination range data.
        
        
        """
        ...
    
    def AddValue(self, value: float) -> bool:
        """    
        Adds a value and splits existing range.
        
        :type value: float
        :param value: The value to add.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetCurrentValue(self) -> float:
        """    
        Retrieves the current value.
        
        :rtype: float
        :return: the current value.
        
        
        """
        ...
    
    def SetCurrentValue(self, value: float) -> None:
        """    
        Sets the current value.
        
        :type value: float
        :param value: The value, must be in the range `[0.0, 1.0]`.
        
        
        """
        ...
    
    def GetRangesCount(self) -> int:
        """    
        Retrieves the number of ranges.
        
        :rtype: int
        :return: The ranges count.
        
        
        """
        ...
    
    def GetKnotsCount(self) -> int:
        """    
        Retrieves the numbers of knots.
        
        :rtype: int
        :return: The knots count.
        
        
        """
        ...
    
    def SetKnotValue(self, knotIndex: int, value: float) -> bool:
        """    
        Sets the value for a knot.
        
        :type knotIndex: int
        :param knotIndex: The knot index to set the value.
        :type value: float
        :param value: The value to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetKnotValue(self, knotIndex: int) -> float:
        """    
        Retrieves the value for a knot.
        
        :type knotIndex: int
        :param knotIndex: The knot index to get the value.
        :rtype: float
        :return: The knot value.
        
        
        """
        ...
    
    def GetKnotIndexByValue(self, value: float) -> int:
        """    
        Searches for a knot with the specified *value*.
        
        :type value: float
        :param value: The value used to search for.
        :rtype: int
        :return: The knot index, or **NOTOK**/**-1** if not found.
        
        
        """
        ...
    
    def DeleteKnot(self, knotIndex: int) -> None:
        """    
        Deletes a knot.
        
        :type knotIndex: int
        :param knotIndex: The index of the knot to delete.
        
        
        """
        ...
    
    def GetRange(self, index: int) -> Tuple[float, float]:
        """    
        Retrieves the range at the specified *index*.
        
        :type index: int
        :param index: The range index.
        :rtype: tuple(float, float)
        :return: The range minimum and maximum values. `(0, 0)` if the function failed.
        
        
        """
        ...
    
    def GetRangeIndex(self, value: float) -> int:
        """    
        Returns the range index for the specified *value*.
        
        :type value: float
        :param value: The value, must be in the range `[0.0, 1.0]`.
        :rtype: int
        :return: The range index. `0` if the function failed
        
        
        """
        ...
    
    def GetSelectedRange(self) -> int:
        """    
        Retrieves the selected range.
        
        :rtype: int
        :return: The selected range index, or **NOTOK**/**-1** if not found.
        
        
        """
        ...
    
    def GetSelectedKnot(self) -> int:
        """    
        Retrieves the selected knot.
        
        :rtype: int
        :return: The selected knot index, or **NOTOK**/**-1** if not found.
        
        
        """
        ...
    
    def SetSelectedKnot(self, knotIndex: int) -> None:
        """    
        Sets the selected knot.
        
        :type knotIndex: int
        :param knotIndex: The index to select, or **NOTOK**/**-1** to deselect all.
        
        
        """
        ...
    
    def SetSelectedRange(self, rangeIndex: int) -> None:
        """    
        Sets the selected range.
        
        :type rangeIndex: int
        :param rangeIndex: The range index to select, or **NOTOK**/**-1** to deselect all.
        
        
        """
        ...
    
    def IsPerRangeColorMode(self) -> bool:
        """    
        Checks if the color mode is stored per range, or just as single color.
        
        :rtype: bool
        :return: **True** if the color is stored is stored per range, otherwise **False**.
        
        
        """
        ...
    
    def SetColorMode(self, perRange: bool) -> None:
        """    
        Sets the mode indicating if the color need to be stored per range, or just as single color.
        
        :type perRange: bool
        :param perRange: **True** to store the color per range, **False** to store it just as single color.
        
        
        """
        ...
    
    def GetRangeColor(self, index: int) -> Vector:
        """    
        Retrieves the range color for the specified range *index*.
        
        :type index: int
        :param index: The index of the range to get the color.
        :rtype: c4d.Vector
        :return: The range color, or a default :class:`c4d.Vector() <c4d.Vector>` if the function failed.
        
        
        """
        ...
    
    def SetRangeColor(self, index: int, color: Vector) -> None:
        """    
        Sets the range color at the specified range *index*.
        
        .. note::
        
        If :meth:`IsPerRangeColorMode` returns **False**, the range *index* is not evaluated and the color is stored at the first index.
        
        :type index: int
        :param index: The index of the range to set the color.
        :type color: c4d.Vector
        :param color: The color to be assigned to the range.
        
        
        """
        ...
    
    def IsRandomColorMode(self) -> bool:
        """    
        Checks if the colors are randomized or user defined.
        
        :rtype: bool
        :return: **True** if the colors are randomized, otherwise **False**.
        
        
        """
        ...
    
    def SetRandomColorMode(self, random: bool) -> None:
        """    
        Sets the random color mode.
        
        :type random: bool
        :param random: **True** to randomize colors, otherwise **False**.
        
        
        """
        ...
    

class PriorityData(CustomDataType):
    def __init__(self, v: Optional[PriorityData] = ...) -> None:
        """    
        :type v: c4d.PriorityData
        :param v: Copy constructor.
        :rtype: c4d.PriorityData
        :return: The new priority data.
        
        
        """
        ...
    
    def SetPriorityValue(self, lValueID: int, data: Any) -> bool:
        """    
        Sets a priority values.
        
        :type lValueID: int
        :param lValueID: The priority value ID to set:
        
        .. include:: /consts/PRIORITYVALUE.rst
        :start-line: 3
        
        :type data: any
        :param data: The priority value to set.
        :rtype: bool
        :return: **True** if successful, otherwise *False*
        
        
        """
        ...
    
    def GetPriorityValue(self, lValueID: int) -> Any:
        """    
        Retrieves the priority values.
        
        :type lValueID: int
        :param lValueID: The priority value ID to get:
        
        .. include:: /consts/PRIORITYVALUE.rst
        :start-line: 3
        
        :rtype: Any
        :return: The priority value.
        
        
        """
        ...
    

class PLAData(CustomDataType):
    def __init__(self, v: PLAData) -> None:
        """    
        :type v: c4d.PLAData
        :param v: Copy constructor.
        :rtype: c4d.PLAData
        :return: A new PLA data.
        
        
        """
        ...
    
    def GetVariableTags(self) -> None:
        """    
        Retrieve the data of a PLA key.
        
        :rtype: tuple(:class:`PointTag <c4d.PointTag>`, :class:`TangentTag <c4d.TangentTag>`) or **None**
        :return:
        
        A :class:`PointTag <c4d.PointTag>` containing the points of the PLA key and a :class:`TangentTag <c4d.TangentTag>` with the hermite tangents of each point. Returns **None** in case of an error.
        
        .. note::
        
        The point tag contains the same number of points as the object, though you should always test for this.
        
        .. note::
        
        The tangent tag contains the same number of tangents as the object, though you should always test for this.
        
        
        """
        ...
    

class MatAssignData(CustomDataType):
    def __init__(self, v: MatAssignData) -> None:
        """    
        :type v: c4d.MatAssignData
        :param v: Copy constructor.
        :rtype: c4d.MatAssignData
        :return: The new :class:`MatAssignData <c4d.MatAssignData>`.
        
        
        """
        ...
    
    def InsertObject(self, pObject: BaseList2D, lFlags: int) -> bool:
        """    
        Inserts an object into the list.
        
        :type pObject: c4d.BaseList2D
        :param pObject: Object to insert.
        :type lFlags: int
        :param lFlags: A bit field for the initial selection state of *pObject*.
        :rtype: bool
        :return: **True** if successful, otherwise **False**
        
        
        """
        ...
    
    def DeleteObject(self, lIndex: int) -> int:
        """    
        Deletes an object from the list.
        
        :type lIndex: int
        :param lIndex: Object index. (0 <= *lIndex* < :meth:`GetObjectCount`)
        :rtype: int
        :return: **True** if the object was deleted, otherwise **False**
        
        
        """
        ...
    
    def ObjectFromIndex(self, doc: BaseDocument, lIndex: int) -> BaseList2D:
        """    
        Gets an object by index.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: Object document.
        :type lIndex: int
        :param lIndex: Object index.  (0 <= *lIndex* < :meth:`GetObjectCount`)
        :rtype: c4d.BaseList2D
        :return: The object or **None**.
        
        
        """
        ...
    
    def GetObjectCount(self) -> int:
        """    
        Gets the object count.
        
        :rtype: int
        :return: Number of objects in the list.
        
        
        """
        ...
    

class LensGlowStruct(CustomDataType):
    def __init__(self, v: LensGlowStruct) -> None:
        """    
        :type v: c4d.LensGlowStruct
        :param v: Copy constructor.
        :rtype: c4d.LensGlowStruct
        :return: The new lens glow data.
        
        
        """
        ...
    

class LayerSet(CustomDataType):
    def __init__(self, v: LayerSet) -> None:
        """    
        :type v: c4d.LayerSet
        :param v: Source layer set for copy constructor.
        :rtype: c4d.LayerSet
        :return: The layer set instance.
        
        
        """
        ...
    
    def Content(self) -> bool:
        """    
        Check if the set is empty.
        
        :rtype: bool
        :return: **True** if the set contains any layer, otherwise **False**.
        
        
        """
        ...
    
    def IsLayerEnabled(self, name: str) -> bool:
        """    
        Check if a layer is enabled.
        
        :type name: str
        :param name: The layer name to check for.
        :rtype: bool
        :return: **True** if the layer is enabled, otherwise **False**.
        
        
        """
        ...
    
    def FindLayerSet(self, name: str) -> bool:
        """    
        Check if a layer is in the set.
        
        :type name: str
        :param name: The layer name to check for.
        :rtype: bool
        :return: **True** if the layer is in the set, otherwise **False**.
        
        
        """
        ...
    
    def GetName(self) -> str:
        """    
        Get the set's name.
        
        :rtype: str
        :return: The name of the set.
        
        
        """
        ...
    
    def GetMode(self) -> int:
        """    
        Returns the layer set mode.
        
        :rtype: int
        :return: The mode:
        
        .. include:: /consts/LAYERSETMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetMode(self, mode: int) -> None:
        """    
        Assign a new layer set mode.
        
        :type mode: int
        :param mode: The mode:
        
        .. include:: /consts/LAYERSETMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def RemoveLayer(self, layer: str) -> None:
        """    
        Remove a layer.
        
        :type layer: str
        :param layer: The layer to remove.
        
        
        """
        ...
    
    def AddLayer(self, layer: str) -> None:
        """    
        Add a layer.
        
        :type layer: str
        :param layer: The layer to add.
        
        
        """
        ...
    
    def FlushLayers(self) -> None:
        """    
        Flush all layers.
        
        
        """
        ...
    
    def GetPreviewMode(self) -> int:
        """    
        Return the preview mode.
        
        :rtype: int
        :return: The preview mode.
        
        
        """
        ...
    
    def SetPreviewMode(self, s: int) -> None:
        """    
        Set the preview mode.
        
        :type s: int
        :param s: The new preview mode.
        
        
        """
        ...
    
    def CopyTo(self, dst: LayerSet) -> None:
        """    
        Copies the content from *self* to *dst*.
        
        :type dst: c4d.LayerSet
        :param dst: The destination layer set.
        
        
        """
        ...
    

class InExcludeData(CustomDataType):
    def __init__(self, v: InExcludeData) -> None:
        """    
        :type v: c4d.InExcludeData
        :param v: Copy constructor.
        :rtype: c4d.InExcludeData
        :return: The new inexclude data.
        
        
        """
        ...
    
    def InsertObject(self, pObject: BaseList2D, lFlags: int) -> bool:
        """    
        Inserts an object into the list.
        
        :type pObject: c4d.BaseList2D
        :param pObject: Object to insert.
        :type lFlags: int
        :param lFlags: A bit field for the initial selection state of *pObject*. Pass **1** to activate the inserted object.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DeleteObject(self, index: int) -> bool:
        """    
        Removes the object at *index* from the list.
        
        :type index: int
        :param index: Object index. (0 <= *index* < :meth:`GetObjectCount`)
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetObjectIndex(self, doc: BaseDocument, pObject: BaseList2D) -> int:
        """    
        Gets the index of *pObject* in the list.
        
        .. versionadded:: R18.020
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to evaluate the links in.
        :type pObject: c4d.BaseList2D
        :param pObject: The object to search for.
        :rtype: int
        :return: The object index, or **c4d.NOTOK** if it was not found.
        
        
        """
        ...
    
    def ObjectFromIndex(self, doc: BaseDocument, index: int) -> BaseList2D:
        """    
        Gets the object at *index* in the list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to evaluate the links in.
        :type index: int
        :param index: Object index. (0 <= *index* < :meth:`GetObjectCount`)
        :rtype: c4d.BaseList2D
        :return: The found object, or **None**.
        
        
        """
        ...
    
    def GetObjectCount(self) -> int:
        """    
        Gets the object count.
        
        :rtype: int
        :return: Number of objects in the list.
        
        
        """
        ...
    
    def GetFlags(self, index: int) -> int:
        """    
        Gets the flags for the object at *index* in the list.
        
        :type index: int
        :param index: Object index. (0 <= *index* < :meth:`GetObjectCount`)
        :rtype: int
        :return: A bit field for the selection state of the object.
        
        
        """
        ...
    
    def SetFlags(self, index: int, flags: int) -> None:
        """    
        Sets the flags for the object at *index* in the list.
        
        .. versionadded:: R18.020
        
        :type index: int
        :param index: Object index. (0 <= *index* < :meth:`GetObjectCount`)
        :type flags: int
        :param flags: A bit field for the selection state of the object.
        
        
        """
        ...
    
    def GetFlagCount(self) -> int:
        """    
        Gets the number of flags for each object.
        
        .. versionadded:: R18.020
        
        :rtype: int
        :return: The number of flags for each object.
        
        
        """
        ...
    
    def SetFlagCount(self, flagCount: int) -> None:
        """    
        Sets the number of flags for each object.
        
        .. versionadded:: R18.020
        
        :type flagCount: int
        :param flagCount: The number of flags for each object.
        
        
        """
        ...
    
    def GetDefaultFlag(self) -> int:
        """    
        Gets the default flag for new items in the list.
        
        .. versionadded:: R18.020
        
        :rtype: int
        :return: The default flag for new items in the list.
        
        
        """
        ...
    
    def SetDefaultFlag(self, defaultFlag: int) -> None:
        """    
        Sets the default flag for new items in the list.
        
        .. versionadded:: R18.020
        
        :type defaultFlag: int
        :param defaultFlag: The default flag for new items in the list.
        
        
        """
        ...
    

class HyperLinkData(CustomDataType):
    def __init__(self, v: HyperLinkData) -> None:
        """    
        :type v: c4d.HyperLinkData
        :param v: Copy constructor.
        :rtype: c4d.HyperLinkData
        :return: The new hyper link data.
        
        
        """
        ...
    
    def SetStrings(self, strLink: str, strText: str) -> None:
        """    
        Sets the strings.
        
        :type strLink: str
        :param strLink: The new link string or **None**.
        :type strText: str
        :param strText: The new text string or **None**.
        
        
        """
        ...
    
    def GetStrings(self) -> Tuple[str, str]:
        """    
        Gets the strings.
        
        :rtype: tuple(str, str)
        :return: The link and text strings.
        
        
        """
        ...
    

class Gradient(CustomDataType):
    def __init__(self, v: Gradient) -> None:
        """    
        :type v: c4d.Gradient
        :param v: Copy constructor.
        :rtype: c4d.Gradient
        :return: The new gradient.
        
        
        """
        ...
    
    def __hash__(self) -> int:
        """    
        Returns a hash of the whole gradient state, including the needles, colors and interpolation type.
        
        .. code-block:: python
        
        print hash(obj) #hash calls obj.__hash__()
        
        :rtype: int
        :return: Hash value
        
        
        """
        ...
    
    def InvertKnots(self) -> bool:
        """    
        Inverts the knots.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DoubleKnots(self) -> bool:
        """    
        Doubles the knots.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DistributeKnots(self) -> bool:
        """    
        Distributes the knots evenly.
        
        .. versionadded:: R20
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FlushKnots(self) -> None:
        """    
        Flushes all knots.
        
        
        """
        ...
    
    def InitRender(self, irs: InitRenderStruct) -> bool:
        """    
        Initializes the renderer.
        
        .. note::
        
        Call before :meth:`CalcGradientPixel`.
        
        :type irs: c4d.modules.render.InitRenderStruct
        :param irs: Information about the upcoming rendering.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FreeRender(self) -> None:
        """    
        Free the render.
        
        .. note::
        
        Call after gradient calculation is finished.
        
        
        """
        ...
    
    def CalcGradientPixel(self, pos: float) -> Vector:
        """    
        Calculates a gradient pixel.
        
        .. note::
        
        This has to be done within a pair of :meth:`InitRender` / :meth:`FreeRender` calls.
        
        Here is an example.
        
        .. code-block:: python
        
        gradient = op[c4d.LIGHT_VISIBILITY_GRADIENT]
        irs = render.InitRenderStruct()
        
        if gradient.InitRender(irs):
        print gradient.CalcGradientPixel(0.5)
        gradient.FreeRender()
        
        :type pos: float
        :param pos: X position.
        :rtype: c4d.Vector
        :return: Calculated pixel.
        
        
        """
        ...
    
    def InsertKnot(self, col: Vector, brightness: float, pos: float, bias: float, index: int) -> int:
        """    
        Insert a knot. Not passed arguments will be set with default values.
        
        :type col: c4d.Vector
        :param col: The color.
        :type brightness: float
        :param brightness: The brightness.
        :type pos: float
        :param pos: The position.
        :type bias: float
        :param bias: The bias.
        :type index: int
        :param index: The index.
        :rtype: int
        :return: The new knot
        
        .. note::
        
        The new knot index is :meth:`GetKnotCount` - 1
        
        
        """
        ...
    
    def RemoveKnot(self, index: int) -> None:
        """    
        Delete a knot.
        
        :type index: int
        :param index: index knot.
        
        .. note::
        
        0 <= index < :meth:`GetKnotCount`
        
        
        """
        ...
    
    def GetKnot(self, index: int) -> Dict[str, Any]:
        """    
        Returns the information about a knot.
        
        :type index: int
        :param index: The index.
        
        .. note::
        
        The new knot index has to be 0 <= index < :meth:`Gradient.GetKnotCount`
        
        Check out this small example.
        
        .. code-block:: python
        
        col, brightness, pos, bias, index = gradient.GetKnot(index)
        
        :rtype: Dict[int, c4d.Vector, float, float, float]
        :return: A dictionary with the knot information.
        
        
        """
        ...
    
    def SetKnot(self, index: int, col: Vector, brightness: float, pos: float, bias: float) -> None:
        """    
        Set the values of a knot.
        
        .. note::
        
        Just the passed arguments will be set, the other will be discarded.
        
        :type index: int
        :param index: The knot index.
        
        .. note::
        
        The new knot index has to be 0 <= index < :meth:`Gradient.GetKnotCount`
        
        :type col: c4d.Vector
        :param col: The color.
        :type brightness: float
        :param brightness: The brightness.
        :type pos: float
        :param pos: The position.
        :type bias: float
        :param bias: The bias.
        
        
        """
        ...
    
    def GetData(self, id: int) -> Any:
        """    
        Gets a data item from the gradient container.
        
        :type id: int
        :param id: Data ID:
        
        .. include:: /consts/GRADIENT.rst
        :start-line: 3
        
        :rtype: Depends on *id*.
        :return: The data.
        
        
        """
        ...
    
    def SetData(self, id: int, data: Any) -> Any:
        """    
        Sets a data item from the gradient container.
        
        :type id: int
        :param id: Data ID:
        
        .. include:: /consts/GRADIENT.rst
        :start-line: 3
        
        :type data: Depends on *id*.
        :param data: The data.
        
        
        """
        ...
    
    def GetKnotCount(self) -> int:
        """    
        Gets the knot count.
        
        :rtype: int
        :return: Knot count.
        
        
        """
        ...
    
    def GetAlphaGradient(self) -> Gradient:
        """    
        Gets a copy of the alpha gradient.
        
        .. note::
        
        | It is just a copy of the original gradient.
        | Can be changed, but has no effect to the original alpha-gradient.
        
        :rtype: c4d.Gradient
        :return: Alpha gradient.
        
        
        """
        ...
    
    def AllocAlphaGradient(self) -> Gradient:
        """    
        Create a alpha of the gradient. Similar to :meth:`Gradient.GetAlphaGradient`.
        
        .. note::
        
        | It is a copy of the original gradient.
        | Can be changed, but has no effect to the original alpha-gradient.
        
        :rtype: c4d.Gradient
        :return: Alpha gradient.
        
        
        """
        ...
    
    def ConvertToAlphaGradient(self) -> None:
        """    
        Convert the current gradient to an alpha gradient.
        
        
        """
        ...
    

class FontData(CustomDataType):
    def __init__(self, v: FontData) -> None:
        """    
        :type v: c4d.FontData
        :param v: Copy constructor.
        :rtype: c4d.FontData
        :return: The new font data.
        
        
        """
        ...
    
    def SetFont(self, bc: BaseContainer) -> None:
        """    
        Sets the font container.
        
        :type bc: c4d.BaseContainer
        :param bc: The font container.
        
        
        """
        ...
    
    def GetFont(self) -> BaseContainer:
        """    
        Gets the font container.
        
        :rtype: c4d.BaseContainer
        :return: Font container.
        
        
        """
        ...
    

class FieldList(CustomDataType):
    def __init__(self) -> None:
        """    
        Creates a :class:`FieldList <c4d.FieldList>` instance.
        
        :rtype: c4d.FieldList
        :return: The created :class:`FieldList <c4d.FieldList>` instance.
        
        
        """
        ...
    
    def SampleList(self, info: FieldInfo, inputs: FieldInput, outputs: FieldOutput) -> None:
        """    
        Samples the list with full parameter control.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to sample with.
        :type inputs: c4d.modules.mograph.FieldInput
        :param inputs: The inputs to sample. A :class:`FieldInput <c4d.modules.mograph.FieldInput>` with a single position can be passed to sample just one point.
        :type outputs: c4d.modules.mograph.FieldOutput
        :param outputs: The sample data result.
        
        
        """
        ...
    
    def SampleListSimple(self, caller: BaseList2D, inputs: FieldInput, flags: int) -> FieldOutput:
        """    
        Samples the list.
        
        .. note::
        
        Use :meth:`SampleListSimple` to avoid pre-creating :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` and :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        
        :type caller: c4d.BaseList2D
        :param caller: The caller object. Pass the :class:`BaseList2D <c4d.BaseList2D>` to invoke the sampling from.
        :type inputs: c4d.modules.mograph.FieldInput
        :param inputs: The inputs to sample from.
        :type flags: int
        :param flags: The channels to sample:
        
        .. include:: /consts/FIELDSAMPLE_FLAG.rst
        :start-line: 3
        
        :rtype: c4d.modules.mograph.FieldOutput
        :return: The sampling result.
        
        
        """
        ...
    
    def DirectInitSampling(self, info: FieldInfo) -> bool:
        """    
        Initializes sampling in direct mode.
        
        .. warning::
        
        Must be called before :meth:`DirectSample` is invoked.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to initialize sampling with.
        :rtype: bool
        :return: **True** if successful otherwise **False**.
        
        
        """
        ...
    
    def DirectSample(self, inputs: FieldInput, outputs: FieldOutput, info: FieldInfo) -> bool:
        """    
        Samples in direct mode.
        
        :type inputs: c4d.modules.mograph.FieldInput
        :param inputs: The inputs to sample from.
        :type outputs: c4d.modules.mograph.FieldOutput
        :param outputs: The sample data result.
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to sample with.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DirectFreeSampling(self, info: FieldInfo) -> None:
        """    
        Frees any data allocated in :meth:`DirectInitSampling`.
        
        .. warning::
        
        Must be called after direct sampling is finished.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` used for sampling.
        
        
        """
        ...
    
    def GetDirty(self, doc: BaseDocument) -> int:
        """    
        Checks the dirtiness of the field list and its objects.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document. Can be **None**.
        :rtype: int
        :return: The dirty count.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Retrieves the total number of fields and groups in the list.
        
        :rtype: int
        :return: The number of elements in the list.
        
        
        """
        ...
    
    def Flush(self) -> None:
        """    
        Empties the list of all entries, frees any used memory and resets the :class:`FieldList <c4d.FieldList>` instance back to its default state.
        
        
        """
        ...
    
    def InsertLayer(self, layer: FieldLayer, parent: Optional[FieldLayer] = ..., prev: Optional[FieldLayer] = ...) -> bool:
        """    
        Inserts a pre-existing layer into the list.
        
        :type layer: c4d.modules.mograph.FieldLayer
        :param layer: The layer to insert. Must not be already inserted in any other list or in the current list in another location.
        :type parent: Optional[c4d.modules.mograph.FieldLayer]
        :param parent: The parent layer to insert the layer as a child of.
        :type prev: Optional[c4d.modules.mograph.FieldLayer]
        :param prev: The previous layer to the one being inserted.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetLayersRoot(self) -> GeListHead:
        """    
        Retrieves the root :class:`GeListHead <c4d.GeListHead>` that owns the layers.
        
        :rtype: c4d.GeListHead
        :return: The layers root, or **None** if the function failed.
        
        
        """
        ...
    
    def GetSelected(self, selected: List[FieldLayer], includeChildren: Optional[bool] = ...) -> None:
        """    
        Retrieves a list of all the selected layers in the list.
        
        .. note::
        
        This may include the background layer.
        
        :type selected: List[c4d.modules.mograph.FieldLayer]
        :param selected: The selected layers in the list.
        :type includeChildren: Optional[bool]
        :param includeChildren: **True** to include children layers, **False** to exclude.
        
        
        """
        ...
    
    def SetFlags(self, flag: int, state: bool) -> None:
        """    
        Sets the flags for the list.
        
        :type flag: int
        :param flag: The flags to set:
        
        .. include:: /consts/FIELDLIST_FLAGS.rst
        :start-line: 3
        
        :type state: bool
        :param state: **True** to set the flag, **False** to clear it.
        
        
        """
        ...
    
    def GetFlags(self) -> int:
        """    
        Gets the flags for the list.
        
        :rtype: int
        :return: The flags:
        
        .. include:: /consts/FIELDLIST_FLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def CheckFlag(self, flag: int) -> bool:
        """    
        Checks a specific *flag* or combination to see if set.
        
        :type flag: int
        :param flag: The flag to check:
        
        .. include:: /consts/FIELDLIST_FLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if *flag* is set, otherwise **False**.
        
        
        """
        ...
    
    def HasContent(self) -> bool:
        """    
        Checks if the list has content.
        
        :rtype: bool
        :return: **True** if there is any field layer in the list, otherwise **False**.
        
        
        """
        ...
    

class DateTimeData(object):
    def __init__(self, v: DateTimeData) -> None:
        """    
        :type v: c4d.DateTimeData
        :param v: Copy constructor.
        :rtype: c4d.DateTimeData
        :return: The new DateTime data.
        
        
        """
        ...
    
    def GetDateTime(self) -> None:
        """    
        Return the time.
        
        :rtype: `time.struct_time <https://docs.python.org/2.7/library/time.html#time.struct_time>`_
        :return: The time.
        
        
        """
        ...
    
    def SetDateTime(self, d: Any, bSetData: bool, bSetTime: bool) -> None:
        """    
        Set the time.
        
        :type d: `time.struct_time <https://docs.python.org/2.7/library/time.html#time.struct_time>`_
        :param d: The new time.
        :type bSetData: bool
        :param bSetData: If this is **False** the date part of *d* is disregarded.
        :type bSetTime: bool
        :param bSetTime: If this is **False** the time part of *d* is disregarded.
        
        Here is a sample code that shows how to parse a string into a :class:`DateTimeData <c4d.DateTimeData>` object.
        
        .. code-block:: python
        
        import c4d
        from datetime import datetime
        
        # Parse the time string
        dt = datetime.strptime('16.07.2011 03:37:12',"%d.%m.%Y %H:%M:%S")
        dtd = c4d.DateTimeData()
        # Fills the Data object with the DateTime object
        dtd.SetDateTime(dt)
        
        t = dtd.GetDateTime()
        print t.day
        print t.month
        print t.year
        
        
        """
        ...
    

class BitmapButtonStruct(object):
    def __init__(self, op: BaseList2D, id: DescID, dirty: int) -> None:
        """    
        Constructor.
        
        :type op: c4d.BaseList2D
        :param op: The object to send *MSG_DESCRIPTION_GETBITMAP* to.
        :type id: c4d.DescID
        :param id: The ID of the bitmap button.
        :type dirty: int
        :param dirty: The dirty flag. Internally used to detect changes. If this flag changes on parameter set, a new *MSG_DESCRIPTION_GETBITMAP* will be emitted.
        :rtype: c4d.BitmapButtonStruct
        :return: The new bitmap button data.
        
        
        """
        ...
    


def GeGetSerialInfo() -> None:
    """    
    Returns user registration information.
    
    .. versionchanged:: R21
    
    .. warning::
    
    | This function is there only for internal reason, don't use it instead use :func:`c4d.ExportLicenses` or :func:`c4d.GetGeneralLicensingInformation`.
    | organization, street, city and country are always empty string.
    
    :rtype: dict{**licenseId**: str, **organization**: str, **name**: str, **street**: str, **city**: str, **country**: str}
    :return: A dictionary with the serial information for Cinema 4D.
    
    
    """
    ...

def ExportLicenses() -> str:
    """    
    | Returns a json string representation of the licensing information as shown in the ExportLicenses menu command including productId, systemId, userId etc.
    
    .. versionadded:: R21
    
    .. code-block:: python
    
    import c4d
    import json
    
    data = json.loads(c4d.ExportLicenses())
    print data["username"]
    
    :rtype: str
    :return: A json string representation of the license information.
    
    
    """
    ...

def GetGeneralLicensingInformation() -> Tuple[str, str, str]:
    """    
    Returns information about the currently used license and system.
    
    .. versionadded:: R21
    
    :rtype: tuple(str, str, str)
    :return: In this order:
    
    - product ID, the product id of the active license.
    - system ID, a unique system identifier.
    - User ID, the user id that the active license is assigned with.
    
    
    """
    ...

def IsTrial() -> bool:
    """    
    Checks if the current license is a Trial version.
    
    .. versionadded:: R21
    
    :rtype: bool
    :return: **True** if it's a Trial version.
    
    
    """
    ...

def IsLiteVersion() -> bool:
    """    
    Checks if the current license is a Lite version.
    
    .. versionadded:: R21
    
    :rtype: bool
    :return: **True** if it's a Lite version.
    
    
    """
    ...

def IsEducation() -> bool:
    """    
    Checks if the current license is an Education version
    
    .. versionadded:: R21
    
    :rtype: bool
    :return: **True** if it's an Education version.
    
    
    """
    ...

def IsNFR() -> bool:
    """    
    Checks if the current license is an NFR (Not For Resell) version.
    
    .. versionadded:: R21
    
    :rtype: bool
    :return: **True** if it's an NFR version.
    
    
    """
    ...

def GeGetCinemaInfo(info: Any) -> int:
    """    
    Checks if the current license is an NFR (Not For Resell) version.
    
    .. versionadded:: R21
    
    :param info: Retrieves information about Cinema 4D's application runtime.
    :type info: The information type:
    
    .. include:: /consts/CINEMAINFO.rst
    :start-line: 3
    
    :rtype: int
    :return: The Cinema 4D's information.
    
    
    """
    ...

def GeGetVersionType() -> int:
    """    
    Get the type of Cinema 4D application that is running.
    
    .. versionchanged:: R21
    
    :rtype: int
    :return: The version type:
    
    .. include:: /consts/VERSIONTYPE.rst
    :start-line: 3
    
    
    """
    ...

def GeGetTimer() -> int:
    """    
    Get the current timer count in milliseconds.
    
    :rtype: int
    :return: The current timer count in milliseconds.
    
    
    """
    ...

def GeGetMilliSeconds() -> float:
    """    
    Get the current timer count in milliseconds.
    
    :rtype: float
    :return: The current timer count in milliseconds.
    
    
    """
    ...

def GetDefaultFPS() -> int:
    """    
    Get the default frames per second value.
    
    :rtype: int
    :return: The default FPS value.
    
    
    """
    ...

def GeGetCurrentOS() -> int:
    """    
    Get the type of OS that is running Cinema 4D.
    
    :rtype: int
    :return: The OS running Cinema 4D:
    
    .. include:: /consts/OPERATINGSYSTEM.rst
    :start-line: 3
    
    
    """
    ...

def GeGetByteOrder() -> int:
    """    
    Get the type of OS that is running Cinema 4D.
    
    :rtype: int
    :return: The byte order:
    
    .. include:: /consts/BYTEORDER.rst
    :start-line: 3
    
    
    """
    ...

def GeGetGray() -> Vector:
    """    
    Get the color values for the default Cinema 4D gray.
    
    :rtype: c4d.Vector
    :return: All color components in this vector.
    
    
    """
    ...

def GetC4DVersion() -> int:
    """    
    Get the version of Cinema 4D that is running, for instance **12016**.
    
    :rtype: int
    :return: The version of Cinema 4D.
    
    
    """
    ...

def GetAPIVersion() -> List[int]:
    """    
    Get the API version of the Python SDK, for instance **(1, 0, 1001)**
    
    :rtype: List[int]
    :return: The version of the Cinema 4D Python SDK.
    
    
    """
    ...

def StopAllThreads() -> None:
    """    
    Stop all running threads.
    
    
    """
    ...

def StatusClear() -> None:
    """    
    Clear the status bar text.
    
    
    """
    ...

def StatusSetText(str: str) -> None:
    """    
    Set the status bar text.
    
    .. code-block:: python
    
    import c4d
    c4d.StatusSetText("Hello World!")
    
    .. image:: /_imgs/modules/c4d/c4d_statussettext.png
    
    :type str: str
    :param str: The text to display.
    
    
    """
    ...

def StatusSetSpin() -> None:
    """    
    | Set the status bar progress bar spinning.
    | Use this to indicate that your plugin is still processing even if the progress bar is not increasing.
    
    .. code-block:: python
    
    import c4d
    c4d.StatusSetSpin()
    
    .. image:: /_imgs/modules/c4d/c4d_statussetspin.png
    
    
    """
    ...

def StatusSetBar(p: float) -> None:
    """    
    Set the status bar text.
    
    .. code-block:: python
    
    import c4d
    c4d.StatusSetBar(50)
    
    .. image:: /_imgs/modules/c4d/c4d_statussetbar.png
    
    :type p: float
    :param p: The percentage of the bar (*0-100*).
    
    
    """
    ...

def StatusNetClear() -> None:
    """    
    Clears the NET status bar text.
    
    .. versionadded:: R16.050
    
    
    """
    ...

def StatusSetNetBar(p: float, dat: Any) -> None:
    """    
    Sets the NET status bar progress and custom color.
    
    .. versionadded:: R16.050
    
    :type p: float
    :param p: The percentage of the progress (0-100).
    :type dat: any
    :param dat: The color for the NET status bar. Can be a color constant *COLOR_BG*, *COLOR_TEXT*, etc. or a color :class:`Vector <c4d.Vector>`.
    
    
    """
    ...

def StatusSetNetLoad(status: int) -> None:
    """    
    Sets the NET status bar to *status* state.
    
    .. versionadded:: R16.050
    
    :type status: int
    :param status: The NET status state:
    
    .. include:: /consts/STATUSNETSTATE.rst
    :start-line: 3
    
    
    """
    ...

def StatusSetNetText(str: str) -> None:
    """    
    Sets the NET status bar text.
    
    .. versionadded:: R16.050
    
    :type str: str
    :param str: The text to display.
    
    
    """
    ...

def IsNet() -> bool:
    """    
    Checks if either a NET server or client application is running.
    
    .. versionadded:: R15.037
    
    :rtype: bool
    :return: **True** if NET is running, otherwise **False**.
    
    
    """
    ...

def IsServer() -> bool:
    """    
    Checks if a NET server application is running.
    
    .. versionadded:: R15.037
    
    :rtype: bool
    :return: **True** if a NET server application is running, otherwise **False**.
    
    
    """
    ...

def IsClient() -> bool:
    """    
    Checks if a NET client application is running.
    
    .. versionadded:: R15.037
    
    :rtype: bool
    :return: **True** if a NET client application is running, otherwise **False**.
    
    
    """
    ...

def EventAdd(flags: int) -> None:
    """    
    Adds a global event to Cinema 4D's event queue. Results in a **CoreMessage()** message.
    
    .. note::
    
    | Useless to call from an expression, for instance from a Python generator or tag.
    | Since R19 if :func:`c4d.EventAdd` is called from within the code of an expression, then it is simply skipped.
    
    :type flags: int
    :param flags: One of the following flags:
    
    .. include:: /consts/EVENT.rst
    :start-line: 3
    
    
    """
    ...

def GeSyncMessage(messageid: int) -> bool:
    """    
    Sends a synchronous event message. (For example to make the timeline, timeslider etc. do an instant redraw.)
    
    :type messageid: int
    :param messageid: The message ID:
    
    .. include:: /consts/EVMSG.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def SendCoreMessage(coreid: int, msg: BaseContainer, eventid: int) -> Any:
    """    
    Sends a core message. For example
    
    .. code-block:: python
    
    machine = c4d.SendCoreMessage(c4d.COREMSG_CINEMA, c4d.BaseContainer(c4d.COREMSG_CINEMA_GETMACHINEFEATURES))
    
    :type coreid: int
    :param coreid: The core ID. *COREMSG_CINEMA* for Cinema 4D core.
    :type msg: c4d.BaseContainer
    :param msg: The message container:
    
    .. include:: /consts/COREMSG.rst
    :start-line: 3
    
    :type eventid: int
    :param eventid: The event ID.
    :rtype: Any
    :return: The returned data. Depends on the message, see table above.
    
    
    """
    ...

def GePluginMessage(id: int, data: Any) -> bool:
    """    
    Sends a plugin message to other plugins.
    
    :type id: int
    :param id: The ID of the message.
    :type data: any
    :param data: The message data.
    :rtype: bool
    :return: **True** if the message could be sent, otherwise **False**.
    
    
    """
    ...

def DrawViews(flags: int, bd: BaseDraw) -> bool:
    """    
    Redraws the editor views. Must be called from the main thread!
    
    :type flags: int
    :param flags: Which part of the editors view should be updated:
    
    .. include:: /consts/DRAWFLAGS.rst
    :start-line: 3
    
    :type bd: c4d.BaseDraw
    :param bd: The basedraw to draw when *DRAWFLAGS_ONLY_BASEDRAW* is set in flags.
    :rtype: bool
    :return: Success of updating the editor views.
    
    
    """
    ...

def SpecialEventAdd(messageid: int, p1: int, p2: int) -> None:
    """    
    Adds a custom event to the internal message queue.
    
    .. note::
    
    | There are areas in Cinema 4D, especially the GUI, which can only be handled by the main thread.
    | For instance, if you want to update the GUI from another thread, you can use SpecialEventAdd.
    | This function adds a custom event to the internal message queue which is handled by the main thread. See example below.
    
    | Use a plugin ID for *messageid* to make sure that there's no collision.
    | Results in a :meth:`GeDialog.CoreMessage` message.
    
    .. code-block:: python
    
    c4d.SpecialEventAdd(MY_PLUGIN_ID) #e.g: called in Thread 1509
    
    #[...]
    
    def CoreMessage(self, id, msg):
    if id==MY_PLUGIN_ID:
    #Fired by the main thread...
    self.dlg.LayoutChanged(GROUP_ID)
    return True
    
    return gui.GeDialog.CoreMessage(self, id, msg)
    
    :type messageid: int
    :param messageid: The message ID. Use a unique ID, for example your plugin ID.
    :type p1: int
    :param p1: Private data for the sent message.
    :type p2: int
    :param p2: Private data for the sent message.
    
    
    """
    ...

def GetGlobalTexturePath(i: int) -> str:
    """    
    .. deprecated:: R20
    Use :func:`GetGlobalTexturePaths` instead.
    
    Get the global texture path.
    
    :type i: int
    :param i: The index of the texture path (0-9).
    :rtype: str
    :return: The texture path for Cinema 4D.
    
    
    """
    ...

def SetGlobalTexturePath(i: int, fn: str) -> None:
    """    
    .. deprecated:: R20
    Use :func:`SetGlobalTexturePaths` instead.
    
    Set the global texture path.
    
    :type i: int
    :param i: The index of the texture path (0-9).
    :type fn: str
    :param fn: The texture path.
    
    
    """
    ...

def GetGlobalTexturePaths(docPath: str) -> List[Tuple[str, bool]]:
    """    
    Retrieves the global texture paths.
    
    .. versionadded:: R20
    
    :param docPath:
    
    | The path of the document. This will be used to complete relative texture paths.
    | Pass an empty string if you want to get the unmodified paths only.
    
    .. versionadded:: S22
    
    :type docPath: str
    :rtype: List[Tuple(str,bool)]
    :return: The global texture paths in a list of tuples with the path name and its enabled state.
    
    
    """
    ...

def SetGlobalTexturePaths(texturePaths: List[Tuple[str, bool]]) -> None:
    """    
    Sets the global texture paths.
    
    .. versionadded:: R20
    
    :type texturePaths: List[Tuple(str,bool)]
    :param texturePaths: The global texture paths to set in a list of tuples with the path name and its enabled state.
    
    
    """
    ...

def GenerateTexturePath(docpath: str, srcname: str, suggestedfolder: str, service: Optional[NetRenderService] = ..., bt: Optional[BaseThread] = ...) -> str:
    """    
    Generates the texture filename for a given texture image.
    
    .. versionadded:: R16.050
    
    :type docpath: str
    :param docpath: The filename of the document for the texture.
    :type srcname: str
    :param srcname: The filename of the image.
    :type suggestedfolder: str
    :param suggestedfolder: A suggested folder path for the image. Can be an empty string.
    :type service: c4d.modules.net.NetRenderService
    :param service: An optional NET render service for the operation.
    :type bt: c4d.threading.BaseThread
    :param bt: An optional thread for the operation.
    :rtype: str
    :return: The generated texture path.
    
    
    """
    ...

def IsInSearchPath(texfilename: str, docpath: str) -> bool:
    """    
    Checks if the texture *texfilename* is in the search path for files located in *docpath*.
    
    .. versionadded:: R16.050
    
    :type texfilename: str
    :param texfilename: The filename of the texture.
    :type docpath: str
    :param docpath: The document path.
    :rtype: bool
    :return: **True** if the texture file is in the search path, otherwise **False**.
    
    
    """
    ...

def FlushUnusedTextures() -> None:
    """    
    Flush all unused textures.
    
    
    """
    ...

def SetWorldContainer(bc: BaseContainer) -> None:
    """    
    Set the main Cinema 4D settings container. See `WPREF` in the C++ doc.
    
    :type bc: c4d.BaseContainer
    :param bc: The new settings.
    
    
    """
    ...

def GetWorldContainer() -> BaseContainer:
    """    
    Returns a copy of the settings container of Cinema 4D.
    
    :rtype: c4d.BaseContainer
    :return: The main Cinema 4D settings.
    
    
    """
    ...

def GetWorldContainerInstance() -> BaseContainer:
    """    
    Return a reference to the main Cinema 4D settings container that can be changed directly.
    
    .. note::
    
    | There are a few settings that are transferred to the world container within the call :func:`GetWorldContainer`, for example *WPREF_UNITS_BASIC* to *WPREF_COLOR_XXX*.
    | These settings cannot be set using :func:`GetWorldContainerInstance`.
    
    :rtype: c4d.BaseContainer
    :return: The main Cinema 4D settings.
    
    
    """
    ...

def GetViewColor(colid: int) -> Vector:
    """    
    Returns a viewport color.
    
    :type colid: int
    :param colid: Type of color to get:
    
    .. include:: /consts/VIEWCOLOR.rst
    :start-line: 3
    
    :rtype: c4d.Vector
    :return: The color value.
    
    
    """
    ...

def SetViewColor(colid: int, col: Vector) -> None:
    """    
    Set a viewport color.
    
    :type colid: int
    :param colid: Type of color to set:
    
    .. include:: /consts/VIEWCOLOR.rst
    :start-line: 3
    
    :type col: c4d.Vector
    :param col: The new color.
    
    
    """
    ...

def GeIsActiveToolEnabled() -> bool:
    """    
    Checks if the active tool is ghosted.
    
    :rtype: bool
    :param: **True** if the active tool is ghosted, otherwise **False**.
    
    
    """
    ...

def GeGetLanguage(index: int) -> None:
    """    
    | Can be used to enumerate information about the available languages.
    | Start with index==0 and then iterate until the function returns **None**.
    
    .. code-block:: python
    
    lang = GeGetLanguage(index)
    if lang==None: return
    
    index+=1
    # str, str, bool
    print lang["extensions"], lang["name"], lang["default_language"]
    
    :type index: int
    :param index: The language index.
    :rtype: dict{**extensions**: str, **name**: str, **default_language**: bool}
    :return: Information about the language
    
    
    """
    ...

def GetObjectName(type: int) -> str:
    """    
    | Gets a user presentable name from an object type ID.
    | For example, :func:`GetObjectName <GetObjectName>` (*Ocube*) returns **"Cube"**.
    
    :type type: int
    :param type: An object type ID.
    :rtype: str
    :return: The object name for type.
    
    
    """
    ...

def GetObjectType(name: str) -> int:
    """    
    | The inverse of :func:`GetObjectName`.
    | Returns an object type from an object name.
    
    :type name: str
    :param name: An object name.
    :rtype: int
    :return: The object type for *name*.
    
    
    """
    ...

def GetTagName(type: int) -> str:
    """    
    | Gets a user presentable name from a tag type ID.
    | For example, :func:`GetTagName <GetTagName>` (*Tphong*) returns **"Phong"**.
    
    :type type: int
    :param type: A tag type ID.
    :rtype: str
    :return: The tag name for type.
    
    
    """
    ...

def FindInManager(bl: BaseList2D) -> None:
    """    
    Finds and makes *bl* visible in its manager.
    
    :type bl: c4d.BaseList2D
    :param bl: The object to find.
    
    
    """
    ...

def CallCommand(cmdid: int, subid: int) -> None:
    """    
    Executes a command.
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type cmdid: int
    :param cmdid: The ID of the command.
    :type subid: int
    :param subid: The sub-command ID.
    
    
    """
    ...

def GetCommandName(id: int) -> str:
    """    
    Gets the name of a command.
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type id: int
    :param id: The ID of the command.
    :rtype: str
    :return: The command name.
    
    
    """
    ...

def GetCommandHelp(id: int) -> str:
    """    
    Gets the help string of a command.
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type id: int
    :param id: The ID of the command.
    :rtype: str
    :return: The help string.
    
    
    """
    ...

def IsCommandEnabled(id: int) -> bool:
    """    
    Checks if a command is enabled.
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type id: int
    :param id: The ID of the command.
    :rtype: bool
    :return: **True** if the command is enabled, otherwise **False**.
    
    
    """
    ...

def IsCommandChecked(id: int) -> bool:
    """    
    Checks if a command is checked.
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type id: int
    :param id: The ID of the command.
    :rtype: bool
    :return: **True** if the command is checked, otherwise **False**
    
    
    """
    ...

def PrefsLib_OpenDialog(page: int) -> bool:
    """    
    Used to open the preference dialog of Cinema 4D on a specific **page**.
    
    .. code-block:: python
    
    import c4d
    c4d.PrefsLib_OpenDialog(c4d.PREFS_MEMORY)
    
    :type page: int
    :param page: The page to open:
    
    Preferences main categories:
    
    .. include:: /consts/PREFS.rst
    :start-line: 3
    
    Preferences format:
    
    .. include:: /consts/FORMAT_Export.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** on success otherwise **False**.
    
    
    """
    ...

def CopyStringToClipboard(text: str) -> None:
    """    
    Copy a text to the clipboard.
    
    :type text: str
    :param text: The text to copy.
    
    
    """
    ...

def CopyBitmapToClipboard(map: BaseBitmap, ownerid: int) -> None:
    """    
    Copy a bitmap to the clipboard.
    
    :type map: c4d.bitmaps.BaseBitmap
    :param map: The bitmap to copy.
    :type ownerid: int
    :param ownerid: The owner id.
    
    
    """
    ...

def GetStringFromClipboard() -> str:
    """    
    Returns a string from the clipboard.
    
    :rtype: str
    :return: The string or **None**.
    
    
    """
    ...

def GetBitmapFromClipboard() -> BaseBitmap:
    """    
    Returns a bitmap from the clipboard.
    
    :rtype: c4d.bitmaps.BaseBitmap
    :return: The bitmap or **None**.
    
    
    """
    ...

def GetClipboardType() -> int:
    """    
    Get the type of the clipboard.
    
    :rtype: int
    :return: The type of the clipboard:
    
    .. include:: /consts/CLIPBOARDTYPE.rst
    :start-line: 3
    
    
    """
    ...

def GetC4DClipboardOwner() -> int:
    """    
    Get the owner ID of the clipboard.
    
    :rtype: int
    :return: The owner ID:
    
    .. include:: /consts/CLIPBOARDOWNER.rst
    :start-line: 3
    
    
    """
    ...

def RestartMe(param: int, exitcode: int) -> bool:
    """    
    Restarts Cinema 4D.
    
    :type param: int
    :param param: The parameter.
    :type exitcode: int
    :param exitcode: The exit code.
    :rtype: bool
    :return: Always **True**.
    
    
    """
    ...

def GeGetSystemInfo() -> None:
    """    
    Retrieves system information flags.
    
    :return: The system information.
    
    .. include:: /consts/SYSTEMINFO.rst
    :start-line: 3
    
    
    """
    ...

def GePrint(str: str) -> None:
    """    
    Outputs a string to the Cinema 4D console window.
    
    :param str: the string to write in the Python Console.
    :type str: str
    
    
    """
    ...

def CallButton(op: BaseList2D, id: int) -> None:
    """    
    Simulates a click of a button.
    
    For example, here is how to call the 'Apply' button of a Tool.
    
    .. code-block:: python
    
    import c4d
    
    c4d.CallCommand(c4d.ID_MODELING_TRANSFER_TOOL) # Set Transfer as current Tool
    
    tool = plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL) # Search Transfer Tool instance
    if tool is not None:
    c4d.CallButton(tool, c4d.MDATA_APPLY)
    c4d.EventAdd()
    
    .. _CallButton-warning:
    
    .. warning::
    
    | Must be called from the main thread only.
    | Forbidden to call in expressions (Python generator, tag, XPresso node, etc.). See :ref:`threading-information`.
    
    :type op: c4d.BaseList2D
    :param op:  The object.
    :type id: int
    :param id: The ID of the button.
    
    
    """
    ...

def GetCustomDataTypeDefault(type: int) -> BaseContainer:
    """    
    | Retrieve the default settings for a data type.
    | Used to create a default datatype container which can be set with :meth:`BaseList2D.AddUserData`.
    
    :type type: int
    :param type: Data type ID.
    
    .. include:: /consts/DTYPE.rst
    :start-line: 3
    
    :rtype: c4d.BaseContainer
    :return: Default settings container.
    
    
    """
    ...

def CheckIsRunning(type: int) -> bool:
    """    
    Check if a task is running.
    
    :type type: int
    :param type: The task:
    
    .. include:: /consts/CHECKISRUNNING.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if the task running, otherwise **False**.
    
    
    """
    ...

def GetMachineFeatures(type: int) -> BaseContainer:
    """    
    Retrieves the features of the computer
    
    .. code-block:: python
    
    import c4d
    bc = c4d.GetMachineFeatures()
    print bc[c4d.OPENGL_RENDERER_NAME] #Output e.g: NVIDIA GeForce 9600 Engine
    
    :type type: int
    :param type:
    
    .. versionadded:: R18.020
    
    The machine features type:
    
    .. include:: /consts/MachineFeaturesType.rst
    :start-line: 3
    
    :rtype: c4d.BaseContainer
    :return: The container with the machine features. Returned container IDs see :doc:`MACHINEINFO </consts/MACHINEINFO>` and :doc:`OPENGL </consts/OPENGL>`.
    
    
    """
    ...

def StartEditorRender(active_only: bool, raybrush: bool, x1: int, y1: int, x2: int, y2: int, bt: BaseThread, bd: BaseDraw, newthread: bool) -> None:
    """    
    Starts the editor renderer.
    
    .. code-block:: python
    
    import c4d
    def RenderEditor(doc):
    bd = doc.GetActiveBaseDraw()
    c4d.StartEditorRender(active_only=False, raybrush=False, x1=0, y1=0, x2=500, y2=500, bt=None, bd=bd, newthread=False) #render a view
    
    
    :type active_only: bool
    :param active_only: Active object only.
    :type raybrush: bool
    :param raybrush: Ray brush mode.
    :type x1: int
    :param x1: X coordinate of the first corner of the render rectangle.
    :type y1: int
    :param y1: Y coordinate of the first corner of the render rectangle.
    :type x2: int
    :param x2: X coordinate of the second corner of the render rectangle.
    :type y2: int
    :param y2: Y coordinate of the second corner of the render rectangle.
    :type bt: c4d.threading.BaseThread
    :param bt: Must be **None**. Private.
    :type bd: c4d.BaseDraw
    :param bd: Base draw to draw to.
    :type newthread: bool
    :param newthread: If this is **True** then the editor render is done asynchronously.
    
    
    """
    ...

def Cast(type: Any, obj: object) -> Any:
    """    
    Casts *obj* to the given *type*.
    
    .. versionadded:: R16.021
    
    .. note::
    
    Useful in a NET/Team render context when catching *C4DPL_JOBFINISHED_POST* message in :meth:`PluginMessage`:
    
    .. code-block:: python
    
    if id == c4d.C4DPL_JOBFINISHED_POST:
    jobUuid = c4d.Cast(c4d.modules.uuid.UUID, data)
    
    .. versionchanged:: R17.048
    
    If *type* is **None** the function casts it to a data (`GeData` in Cinema 4D API).
    
    :type type: Type
    :param type: The type to cast to. Supported types are str, c4d.BaseContainer, c4d.Matrix and uui.Uuid.
    :type obj: Object
    :param obj: The object to cast.
    :rtype: Any
    :return: The result of the cast operation.
    
    
    """
    ...

def CallFunction(op: BaseList2D, function: str, arg1: Optional[Any] = ..., arg2: Optional[Any] = ..., arg3: Optional[Any] = ...) -> Any:
    """    
    | Calls a function defined within a scripting expression.
    | This works for all parts of Cinema 4D where Python is embedded. See :ref:`c4d-python-in-c4d-Embedded`.
    
    .. versionadded:: R16.021
    
    .. note::
    
    | The arguments and returned value have to be of any Cinema 4D data type i.e. anytype or `GeData` in the C++ API.
    | Anything else will be converted to a `void*` before being sent to the other object.
    | As the maximum number of arguments is `3`, to send more make one of the arguments a :class:`BaseContainer <c4d.BaseContainer>` which can store more information.
    
    .. warning::
    
    | Bear in mind that just as with any function call it is possible to accidentally set up a cyclical dependency of one function calling another which might call the original function (either directly or indirectly by e.g. invoking an :func:`EventAdd() <c4d.EventAdd>` which might cause the original function to be re-called) and so on and which would crash Cinema 4D.
    | This risk is the same as with directly calling a function from within your own script.
    
    :type op: BaseList2D
    :param op: The object to search the function within its script.
    :type function: str
    :param function: The name of the function to call.
    :type arg1: any
    :param arg1: The first optional argument.
    :type arg2: any
    :param arg2: The second optional argument.
    :type arg3: any
    :param arg3: The third optional argument.
    :rtype: Any
    :return: The value returned by the called function.
    
    
    """
    ...

def AllocListHead() -> GeListHead:
    """    
    Allocates a list head.
    
    .. versionadded:: R16.050
    
    :rtype: c4d.GeListHead
    :return: The allocated list head node.
    :raise AllocationError: If a list head could not be allocated.
    
    .. versionchanged:: R19
    
    The function now returns a :class:`c4d.GeListHead` object.
    
    
    """
    ...

def CopyData(op1: BaseList2D, descid1: DescID, op2: BaseList2D, descid2: DescID, aliastrans: AliasTrans) -> None:
    """    
    Copies a parameter data to another.
    
    .. versionadded:: R17.032
    
    :type op1: c4d.BaseList2D
    :param op1: The source base list.
    :type descid1: c4d.DescID
    :param descid1: The parameter description ID to copy the data from.
    :type op2: c4d.BaseList2D
    :param op2: The destination base list.
    :type descid2: c4d.DescID
    :param descid2: The parameter description ID to copy the data to.
    :type aliastrans: c4d.AliasTrans
    :param aliastrans:
    
    .. versionadded:: R17.053
    
    An alias translator for the operation.
    
    
    """
    ...

def WriteConsole(str: str) -> None:
    """    
    Writes *str* to the Python console.
    
    .. versionadded:: R20
    
    :type str: str
    :param str: The string to print.
    
    
    """
    ...

def IsUVToolMode(document: BaseDocument) -> bool:
    """    
    Check if the current context is UV, if UV mode is selected or the UV Texture Editor is the last one used.
    
    .. versionadded:: S22
    
    :type document: c4d.documents.BaseDocument
    :param document: The currently active document.
    :rtype: bool
    :return: **True** if is UV mode, **False** otherwise.
    
    
    """
    ...

