from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseObject, BaseContainer
from c4d.documents import BaseDocument


class VolumeObject(BaseObject):
    def __init__(self) -> None:
        """    
        Creates a :class:`VolumeObject <c4d.modules.volume.VolumeObject>`.
        
        :rtype: c4d.modules.volume.VolumeObject
        :return: A :class:`VolumeObject <c4d.modules.volume.VolumeObject>`.
        
        
        """
        ...
    
    def GetGridType(self) -> int:
        """    
        Returns the grid type.
        
        :rtype: int
        :return: The grid type:
        
        .. include:: /consts/GRIDTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetGridClass(self) -> int:
        """    
        Returns the grid class.
        
        :rtype: int
        :return: The grid class:
        
        .. include:: /consts/GRIDCLASS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetVolume(self) -> None:
        """    
        Returns the core volume object.
        
        :rtype: :class:`maxon.frameworks.volume.VolumeRef`
        :return: The core volume object.
        
        
        """
        ...
    
    def SetVolume(self, volume: Any) -> None:
        """    
        Sets the core volume object.
        
        :type volume: :class:`maxon.frameworks.volume.VolumeRef`
        :param volume: The core volume object to set.
        
        
        """
        ...
    

class VolumeBuilder(BaseObject):
    def __init__(self) -> None:
        """    
        Creates a :class:`VolumeBuilder <c4d.modules.volume.VolumeBuilder>`.
        
        :rtype: c4d.modules.volume.VolumeBuilder
        :return: A :class:`VolumeBuilder <c4d.modules.volume.VolumeBuilder>`.
        
        
        """
        ...
    
    def InputObjectIsChild(self, index: int) -> bool:
        """    
        Checks if object at *index* in the object list is a child of the generator.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the list object to check.
        :rtype: bool
        :return: **True** if the input object is a child, otherwise **False**.
        
        
        """
        ...
    
    def GetInputObjectCount(self, countDouble: bool) -> int:
        """    
        Returns the number of objects in the list.
        
        .. note::
        
        The function does not count folders.
        
        :type countDouble: bool
        :param countDouble: If **True** the objects that are present multiple times in the list are counted multiple times.
        :rtype: int
        :return: The number of objects in the object list.
        
        
        """
        ...
    
    def GetInputObject(self, index: int) -> BaseObject:
        """    
        Retrieves the input object referenced at the given *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object to access.
        :rtype: c4d.BaseObject
        :return: The input object at *index*. **None** if it is a folder or if the function failed.
        
        
        """
        ...
    
    def GetInputObjectByType(self, type: int, startIndex: int) -> Tuple[BaseObject, int]:
        """    
        Retrieves the input object with the given *type*.
        
        :type type: int
        :param type: The type of object to access.
        :type startIndex: int
        :param startIndex: The index to start the search.
        :rtype: Tuple[c4d.BaseObject, int]
        :return: The input object and its index. **None** if the function failed.
        
        
        """
        ...
    
    def GetListEntryCount(self) -> int:
        """    
        Returns the number of elements in the objects list containing folders.
        
        :rtype: int
        :return: The number of elements in the object list.
        
        
        """
        ...
    
    def AddSceneObject(self, object: BaseObject, index: int) -> bool:
        """    
        Adds a valid object from the document to the objects list.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type object: c4d.BaseObject
        :param object: The object that should be added to the objects list.
        :type index: int
        :param index: The index the object should be added to.
        :rtype: bool
        :return: **True** if the object was added successfully, otherwise **False**.
        
        
        """
        ...
    
    def RemoveObject(self, index: int) -> bool:
        """    
        Removes the object in the list at the given *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        |
        | If the object is a child of the :class:`VolumeBuilder <c4d.modules.volume.VolumeBuilder>`, it will be automatically readded to the list.
        | Removing the object from the hierarchy would prevent that.
        
        :type index: int
        :param index: The index of the object to remove.
        :rtype: bool
        :return: **True** if the object was removed successfully, otherwise **False**.
        
        
        """
        ...
    
    def ClearInputObjects(self) -> None:
        """    
        Clears the objects list.
        
        
        """
        ...
    
    def GetSettingsContainerForIndex(self, index: int) -> BaseContainer:
        """    
        Returns the internal container for the settings of an input object at the given *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        |
        | Allows to change the settings that control the specific conversion of an input object.
        
        :type index: int
        :param index: The index of the object in the list.
        :rtype: c4d.BaseContainer
        :return: The settings container for the object. **None** if it is a folder/filter or if the function failed.
        
        
        """
        ...
    
    def GetSettingsContainerForObject(self, object: BaseObject) -> BaseContainer:
        """    
        Returns the internal container for the settings of an input object.
        
        .. note::
        
        Allows to change the settings that control the specific conversion of an input object.
        
        :type object: c4d.BaseObject
        :param object: The input object in the objects list.
        :rtype: c4d.BaseContainer
        :return: The settings container for the object. **None** if it is a folder/filter or if the function failed.
        
        
        """
        ...
    
    def SetBoolMode(self, index: int, boolmode: int) -> None:
        """    
        Sets the bool mode for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :type boolmode: int
        :param boolmode: The bool mode to set:
        
        .. include:: /consts/BOOLTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetBoolMode(self, index: int) -> int:
        """    
        Gets the bool mode for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :rtype: int
        :return: The bool mode:
        
        .. include:: /consts/BOOLTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetMixMode(self, index: int, mixmode: int) -> None:
        """    
        Sets the mix mode for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :type mixmode: int
        :param mixmode: The mix mode to set:
        
        .. include:: /consts/MIXTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMixMode(self, index: int) -> int:
        """    
        Gets the mix mode for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :rtype: int
        :return: The mix mode:
        
        .. include:: /consts/MIXTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetEnable(self, index: int, enable: bool) -> None:
        """    
        Sets the enabled state for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :type enable: bool
        :param enable: The enabled state to set.
        
        
        """
        ...
    
    def GetEnable(self, index: int) -> bool:
        """    
        Gets the enabled state for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :rtype: bool
        :return: **True** if the object is enabled, otherwise **False**.
        
        
        """
        ...
    
    def SetSelected(self, index: int, select: bool) -> None:
        """    
        Sets the selection state for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :type select: bool
        :param select: The The selection state to set.
        
        
        """
        ...
    
    def GetSelected(self, index: int) -> bool:
        """    
        Gets the selection state for the input object at *index*.
        
        .. note::
        
        | Because the list is a tree, *index* depends on the position shown in the UI.
        | This means children are iterated first.
        
        :type index: int
        :param index: The index of the object in the list.
        :rtype: bool
        :return: **True** if the object is selected, otherwise **False**.
        
        
        """
        ...
    
    def SetMixVectorMode(self, index: int, mixmode: int) -> None:
        """    
        Sets the mix vector mode for the index.
        
        :param index: The index of the object to set the mix vector mode for.
        :type index: int
        :param mixmode: The mix vector mode to set.
        
        .. include:: /consts/MIXVECTORTYPE.rst
        :start-line: 3
        
        :type mixmode: int
        
        
        """
        ...
    
    def GetMixVectorMode(self, index: int) -> int:
        """    
        Gets the mix vector mode for the index.
        
        :param index: The index of the object to get the mix vector mode for.
        :type index: int
        :rtype: int
        :return: The mix vector mode for the object at the given index.
        
        .. include:: /consts/MIXVECTORTYPE.rst
        :start-line: 3
        
        
        
        """
        ...
    


def SendVolumeCommand(command: int, list: Any, bc: BaseContainer, doc: BaseDocument) -> Union[bool, List[BaseObject]]:
    """    
    Sends a volume command.
    
    :type command: int
    :param command: The volume command ID:
    
    .. include:: /consts/VOLUMECOMMANDTYPE.rst
    :start-line: 3
    
    :type list: List[:class:`c4d.BaseObject`]
    :param list: The objects to apply the volume command to.
    :type bc: c4d.BaseContainer
    :param bc: The settings container. See :doc:`/consts/VOLUMECOMMANDSETTINGS`.
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: bool or List[c4d.BaseObject)
    :return:
    
    | **True** if the volume command succeeded, otherwise **False**.
    | If the volume command succeeds the resulting objects are returned, if any, instead of **True**.
    
    
    """
    ...

