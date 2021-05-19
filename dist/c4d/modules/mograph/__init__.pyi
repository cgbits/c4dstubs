from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.storage import HyperFile
from c4d import DescID, BaseContainer, BaseList2D, Vector, GeListHead, Matrix, BaseObject, Description, HandleInfo, BaseDraw, BaseTime, BaseSelect
from c4d.documents import BaseDocument
from c4d.threading import BaseThread
from c4d.plugins import BaseDrawHelp


_attributes: int = ...


class MoData(object):
    def GetDirty(self, mask: int) -> int:
        """    
        Get dirty count. Can be used to check if something has changed.
        
        :type mask: int
        :param mask: Flags:
        
        .. include:: /consts/MDDIRTY.rst
        :start-line: 3
        
        :rtype: int
        :return: Dirty count.
        
        
        """
        ...
    
    def SetDirty(self, mask: int) -> None:
        """    
        Mark the data as dirty.
        
        :type mask: int
        :param mask: Flags:
        
        .. include:: /consts/MDDIRTY.rst
        :start-line: 3
        
        
        """
        ...
    
    def Clear(self, reset: bool) -> None:
        """    
        Clear the data in the arrays.
        
        :type reset: bool
        :param reset: **True** will fill the arrays with their default values.
        
        
        """
        ...
    
    def Read(self, hf: HyperFile) -> bool:
        """    
        Read the data from a hyper file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyper file to read from.
        :rtype: bool
        :return: **True** if the data was read, otherwise **False**.
        
        
        """
        ...
    
    def Write(self, hf: HyperFile) -> bool:
        """    
        Write the data to a hyper file.
        
        :type hf: c4d.storage.HyperFile
        :param hf: The hyper file to write to.
        :rtype: bool
        :return: **True** if the data was written, otherwise **False**.
        
        
        """
        ...
    
    def GetMemorySize(self) -> int:
        """    
        Get the size of the data in bytes.
        
        :rtype: int
        :return: Size of the data.
        
        
        """
        ...
    
    def SetCount(self, cnt: int) -> bool:
        """    
        Set the length of the arrays.
        
        :type cnt: int
        :param cnt: The new length of the arrays.
        :rtype: bool
        :return: **True** if the length was set, otherwise **False**.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Get the length of the arrays.
        
        :rtype: int
        :return: The length of the arrays.
        
        
        """
        ...
    
    def GetArrayCount(self) -> int:
        """    
        Get the number of arrays.
        
        :rtype: int
        :return: The number of arrays.
        
        
        """
        ...
    
    def GetArrayDescID(self, index: int) -> DescID:
        """    
        Get the description ID for the specified array index.
        
        :type index: int
        :param index: The index of the array.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :rtype: c4d.DescID
        :return: The description ID.
        
        
        """
        ...
    
    def GetArrayID(self, index: int) -> int:
        """    
        Get the ID for the specified array index.
        
        :type index: int
        :param index: The index of the array.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :rtype: int
        :return: The retrieved ID:
        
        .. include:: /consts/MODATA.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetArrayIndexType(self, index: int) -> int:
        """    
        Get the data type of the specified array.
        
        :type index: int
        :param index: The index of the array.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :rtype: int
        :return: Type:
        
        .. include:: /consts/DTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetArrayType(self, id: int) -> None:
        """    
        Get the data type of the specified array.
        
        :type id: int
        :param id: The ID of the array:
        
        .. include:: /consts/MODATA.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetArrayIndex(self, id: DescID) -> int:
        """    
        Get the array index for the specified description ID.
        
        :type id: c4d.DescID
        :param id: The description ID.
        :rtype: long
        :return: The retrieved array index.
        
        
        """
        ...
    
    def GetDataInstance(self, id: DescID) -> BaseContainer:
        """    
        Get a pointer to the container for the specified array.
        
        :type id: c4d.DescID
        :param id: The description ID of the array.
        :rtype: c4d.BaseContainer
        :return: The internal container.
        
        
        """
        ...
    
    def GetDataIndexInstance(self, index: int) -> BaseContainer:
        """    
        Get a pointer to the container for the specified array.
        
        :type index: int
        :param index: The index of the array.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :rtype: c4d.BaseContainer
        :return: The internal container.
        
        
        """
        ...
    
    def GetData(self, id: int) -> BaseContainer:
        """    
        Get a copy of the array's container.
        
        :type id: int
        :param id: The ID of the array:
        
        .. include:: /consts/MODATA.rst
        :start-line: 3
        
        :rtype: c4d.BaseContainer
        :return: The array's container.
        
        
        """
        ...
    
    def AddArray(self, id: DescID, name: str, default_flags: int) -> int:
        """    
        Add the specified array.
        
        :type id: c4d.DescID
        :param id: The description ID of the array.
        :type name: str
        :param name: The name of the array.
        :type default_flags: int
        :param default_flags: Default flags:
        
        .. include:: /consts/MOGENFLAG.rst
        :start-line: 3
        
        :rtype: int
        :return: The index of the added array or *NOTOK* if it failed.
        
        
        """
        ...
    
    def RemoveArray(self, id: DescID) -> bool:
        """    
        Remove the specified array.
        
        :type id: c4d.DescID
        :param id: The description ID of the array.
        :rtype: bool
        :return: **True** if the array has been removed, otherwise **False**.
        
        
        """
        ...
    
    def SetName(self, id: DescID, name: str) -> None:
        """    
        Set the name for the specified array.
        
        :type id: c4d.DescID
        :param id: The description ID of the array.
        :type name: str
        :param name: The new name of the array.
        
        
        """
        ...
    
    def GetName(self, id: DescID) -> str:
        """    
        Get the name of the specified array.
        
        :type id: c4d.DescID
        :param id: The description ID of the array.
        :rtype: str
        :return: The name of the array.
        
        
        """
        ...
    
    def SetIndexName(self, index: int, name: str) -> None:
        """    
        Set the name for the specified array.
        
        :type index: int
        :param index: The index of the array.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :type name: str
        :param name: The new name of the array.
        
        
        """
        ...
    
    def GetIndexName(self, index: int) -> str:
        """    
        Get the name of the specified array.
        
        :type index: int
        :param index: Array index.
        :raise IndexError: If the array *index* is out of range : *0<=index<*:meth:`GetArrayCount`.
        :rtype: str
        :return: The name of the array.
        
        
        """
        ...
    
    def GetArray(self, id: int) -> List[Any]:
        """    
        Get an array.
        
        :type id: int
        :param id: The ID of the array:
        
        .. include:: /consts/MODATA.rst
        :start-line: 3
        
        :rtype: list
        :return: The array.
        
        
        """
        ...
    
    def SetArray(self, id: int, arr: List[Any], apply_strength: bool) -> None:
        """    
        Set an array.
        
        :type id: int
        :param id: The ID of the array:
        
        .. include:: /consts/MODATA.rst
        :start-line: 3
        
        :type arr: list
        :param arr: The array.
        :type apply_strength: bool
        :param apply_strength: If **True**, a falloff must be present in the :class:`MoData <c4d.modules.mograph.MoData>` instance
        
        
        """
        ...
    
    def Flush(self) -> None:
        """    
        | Flushes the data.
        | All data is cleared, the arrays are freed.
        
        
        """
        ...
    
    def SetOffset(self, offset: int) -> None:
        """    
        Set an offset from the beginning of the arrays, for example array[0] becomes array[offset].
        
        :type offset: int
        :param offset: The array offset, 0 <= *offset* < :meth:`GetCount`.
        
        
        """
        ...
    
    def SetLimit(self, limit: int) -> None:
        """    
        | Limits the array. All data are kept internally.
        | Can be useful for certain cases for instance merging.
        
        :type limit: int
        :param limit: The array limit, 0 <= *limit* < :meth:`GetCount`.
        
        
        """
        ...
    
    def GetGenerator(self) -> BaseList2D:
        """    
        Returns the generator.
        
        .. versionadded:: R14.014
        
        .. note::
        
        In a Python Effector the variable `gen` is the generator.
        
        :rtype: c4d.BaseList2D
        :return: The generator.
        
        
        """
        ...
    
    def GetFalloffs(self) -> List[float]:
        """    
        Returns the established falloffs.
        
        .. note::
        
        Before R20, the falloffs was returned in reverse order.
        
        :rtype: list of float
        :return: The falloff samples.
        
        
        """
        ...
    
    def GetCurrentIndex(self) -> int:
        """    
        Returns the current index.
        
        :rtype: int
        :return: The current index.
        
        
        """
        ...
    
    def GetBlendID(self) -> int:
        """    
        Returns the current blend ID.
        
        :rtype: int
        :return: The current blend ID.
        
        
        """
        ...
    

class FieldOutputBlock(object):
    def __init__(self) -> None:
        """    
        Creates a :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance.
        
        :rtype: c4d.modules.mograph.FieldOutputBlock
        :return: The created :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance.
        
        
        """
        ...
    
    def GetSubBlock(self) -> FieldOutputBlock:
        """    
        Gets a sub-section of the sampling arrays.
        
        :type offset: int
        :param offset: The offset index to retrieve a sub-block starting at.
        :type size: int
        :param size: The suggested size of the block. Note the function clamps the size against the maximum number of entries.
        :rtype: c4d.modules.mograph.FieldOutputBlock
        :return: The requested sub-block.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Resets the :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance to an empty state. All memory is deallocated.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Returns the number of elements in the sub-block.
        
        :rtype: int
        :return: The number of elements.
        
        
        """
        ...
    
    def GetFullCount(self) -> int:
        """    
        Returns the number of elements in the parent :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        
        :rtype: int
        :return: The full number of elements.
        
        
        """
        ...
    
    def GetOffset(self) -> int:
        """    
        Returns the offset of the sub-block in the parent :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        
        :rtype: int
        :return: The offset.
        
        
        """
        ...
    
    def GetOwner(self) -> FieldOutput:
        """    
        Returns the parent or owner :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        
        :rtype: c4d.modules.mograph.FieldOutput
        :return: The owner.
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if the :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance allocations and sizes are valid.
        
        .. note::
        
        An empty :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance is considered valid.
        
        :rtype: bool
        :return: **True** if the :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance is valid, otherwise **False**.
        
        
        """
        ...
    
    def IsPopulated(self) -> bool:
        """    
        Checks if the :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` is valid and non-empty.
        
        :rtype: bool
        :return: **True** if the :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` instance is populated, otherwise **False**.
        
        
        """
        ...
    
    def CopyFrom(self, src: FieldOutputBlock) -> bool:
        """    
        Copies from :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` *src*.
        
        :type src: c4d.modules.mograph.FieldOutputBlock
        :param src: The source :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def CopyArrayContentFrom(self, src: FieldOutputBlock) -> bool:
        """    
        Copies from *src* array content.
        
        .. note::
        
        | Size and flags are not affected by :meth:`CopyArrayContentFrom`.
        | The destination :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` must be big enough to accept the full content of *src*.
        
        :type src: c4d.modules.mograph.FieldOutputBlock
        :param src: The source :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ClearMemory(self, startIdx: int, count: int, deactivatedOnly: bool, deactivatedState: bool) -> None:
        """    
        Resets the sampling data to default values.
        
        .. note::
        
        Values are reset to `0`, colors to `1.0`, direction to `0`, deactivated to `0`.
        
        :type startIdx: int
        :param startIdx: The index to start at.
        :type count: int
        :param count: The number of array elements to reset to default value.
        :type deactivatedOnly: bool
        :param deactivatedOnly: **True** to clear deactivated only, otherwise **False**.
        :type deactivatedState: bool
        :param deactivatedState: The state the deactivated array should be cleared to.
        
        
        """
        ...
    
    def ClearDeactivated(self, state: bool) -> None:
        """    
        Clears the deactivated array.
        
        :type state: bool
        :param state: The state the deactivated array should be cleared to.
        
        
        """
        ...
    
    def CalculateCrc(self) -> int:
        """    
        Calculates a Crc on all internal data.
        
        .. note::
        
        Crc is not kept internally and is calculated from scratch on each :meth:`CalculateCrc` call.
        
        :rtype: int
        :return: The calculated Crc.
        
        
        """
        ...
    
    def GetValue(self, index: int) -> float:
        """    
        Reads value at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def SetValue(self, index: int, value: float) -> None:
        """    
        Writes value at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type value: float
        :param value: The value to set.
        
        
        """
        ...
    
    def GetAlpha(self, index: int) -> float:
        """    
        Reads alpha at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: float
        :return: The alpha.
        
        
        """
        ...
    
    def SetAlpha(self, index: int, alpha: float) -> None:
        """    
        Writes alpha at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type alpha: float
        :param alpha: The alpha to set.
        
        
        """
        ...
    
    def GetColor(self, index: int) -> Vector:
        """    
        Reads color at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The color.
        
        
        """
        ...
    
    def SetColor(self, index: int, color: Vector) -> None:
        """    
        Writes color at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type color: c4d.Vector
        :param color: The color to set.
        
        
        """
        ...
    
    def GetDirection(self, index: int) -> Vector:
        """    
        Reads direction at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The direction.
        
        
        """
        ...
    
    def SetDirection(self, index: int, direction: Vector) -> None:
        """    
        Writes direction at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type direction: c4d.Vector
        :param direction: The direction to set.
        
        
        """
        ...
    
    def GetRotation(self, index: int) -> Vector:
        """    
        Reads rotation at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The rotation.
        
        
        """
        ...
    
    def SetRotation(self, index: int, rotation: Vector, pivot: Vector) -> None:
        """    
        Writes rotation at specified *index*.
        
        .. versionchanged:: R21
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type rotation: c4d.Vector
        :param rotation: The rotation to set.
        :type pivot: c4d.Vector
        :param pivot: The rotational velocity.
        
        
        """
        ...
    
    def GetPivot(self, index: int) -> Vector:
        """    
        Retrieve the rotational velocity (axe + magnitude) at specified *index*.
        
        .. versionadded:: R21
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The rotational velocity (axe + magnitude).
        
        
        """
        ...
    
    def GetDeactivated(self, index: int) -> bool:
        """    
        Reads deactivated state at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: bool
        :return: The deactivated state.
        
        
        """
        ...
    
    def SetDeactivated(self, index: int, deact: bool) -> None:
        """    
        Writes deactivated state at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type deact: bool
        :param deact: The deactivated state to set.
        
        
        """
        ...
    

class FieldOutput(object):
    def __init__(self) -> None:
        """    
        Creates a :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance.
        
        :rtype: c4d.modules.mograph.FieldOutput
        :return: The created :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance.
        
        
        """
        ...
    
    @staticmethod
    def Create(size: int, flags: int, src: FieldOutputBlock) -> FieldOutput:
        """    
        Creates a :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` with the specified sampling arrays.
        
        :type size: int
        :param size: The size.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/FIELDSAMPLE_FLAG.rst
        :start-line: 3
        
        :type src: c4d.modules.mograph.FieldOutputBlock
        :param src: Alternatively pass only a source :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>` to copy its size and arrays.
        :rtype: c4d.modules.mograph.FieldOutput
        :return: The created :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance.
        
        
        """
        ...
    
    def GetBlock(self) -> FieldOutputBlock:
        """    
        Retrieves all arrays in a :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>`.
        
        :rtype: c4d.modules.mograph.FieldOutputBlock
        :return: A sub-block for the whole :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        
        
        """
        ...
    
    def GetSubBlock(self, offset: int, size: int) -> FieldOutputBlock:
        """    
        Gets a sub-section of the sampling arrays.
        
        :type offset: int
        :param offset: The offset index to retrieve a sub-block starting at.
        :type size: int
        :param size: The suggested size of the block. Note the function clamps the size against the maximum number of entries.
        :rtype: c4d.modules.mograph.FieldOutputBlock
        :return: The requested sub-block.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Resets the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance to an empty state.
        
        .. note::
        
        All memory is deallocated.
        
        
        """
        ...
    
    def Flush(self) -> None:
        """    
        Flushes the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance, keeping the arrays allocated for future resize.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Returns the number of elements in the sample arrays.
        
        :rtype: int
        :return: The number of elements.
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance allocations and sizes are valid.
        
        .. note::
        
        An empty :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance is considered valid.
        
        :rtype: bool
        :return: **True** if the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance is valid, otherwise **False**.
        
        
        """
        ...
    
    def IsPopulated(self) -> bool:
        """    
        Checks if the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` is valid and non-empty.
        
        :rtype: bool
        :return: **True** if the :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` instance is populated, otherwise **False**.
        
        
        """
        ...
    
    def CopyFrom(self, src: FieldOutput) -> bool:
        """    
        Copies from :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` *src*. Performs a deep copy.
        
        :type src: c4d.modules.mograph.FieldOutput
        :param src: The source :class:`FieldOutput <c4d.modules.mograph.FieldOutput>`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def CopyArrayContentFrom(self, src: Union[FieldOutputBlock, FieldOutputBlock]) -> bool:
        """    
        Copies from *src* array content.
        
        .. note::
        
        | Size and flags are not affected by :meth:`CopyArrayContentFrom`.
        | Source data is copied into target up to current size. If target is bigger than source, the remaining items are cleared.
        
        :type src: Union[c4d.modules.mograph.FieldOutputBlock, c4d.modules.mograph.FieldOutputBlock]
        :param src: The source :class:`FieldOutput <c4d.modules.mograph.FieldOutput>` or :class:`FieldOutputBlock <c4d.modules.mograph.FieldOutputBlock>`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Resize(self, newSize: int, sampleFlags: int, resizeFlags: int) -> bool:
        """    
        Resizes the arrays held in the FieldOutput.
        
        .. note::
        
        Unspecified channel arrays are resized to `0` length according to *resizeFlags*.
        
        :type newSize: int
        :param newSize: The new size for the arrays.
        :type sampleFlags: int
        :param sampleFlags: The channels to sample:
        
        .. include: /consts/FIELDSAMPLE_FLAG.rst
        
        :type resizeFlags: int
        :param resizeFlags: The flags for the resize.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ClearMemory(self, startIdx: int, count: int, deactivatedOnly: bool, deactivatedState: bool) -> None:
        """    
        Resets the sampling data to default values.
        
        .. note::
        
        Values are reset to `0`, colors to `1.0`, direction to `0`, deactivated to `0`.
        
        :type startIdx: int
        :param startIdx: The index to start at.
        :type count: int
        :param count: The number of array elements to reset to default value.
        :type deactivatedOnly: bool
        :param deactivatedOnly: **True** to clear deactivated only, otherwise **False**.
        :type deactivatedState: bool
        :param deactivatedState: The state the deactivated array should be cleared to.
        
        
        """
        ...
    
    def ClearDeactivated(self, state: bool) -> None:
        """    
        Clears the deactivated array.
        
        :type state: bool
        :param state: The state the deactivated array should be cleared to.
        
        
        """
        ...
    
    def CalculateCrc(self) -> int:
        """    
        Calculates a Crc on all internal data.
        
        .. note::
        
        Crc is not kept internally and is calculated from scratch on each :meth:`CalculateCrc` call.
        
        :rtype: int
        :return: The calculated Crc.
        
        
        """
        ...
    
    def GetValue(self, index: int) -> float:
        """    
        Reads value at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: float
        :return: The value.
        
        
        """
        ...
    
    def SetValue(self, index: int, value: float) -> None:
        """    
        Writes value at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type value: float
        :param value: The value to set.
        
        
        """
        ...
    
    def GetAlpha(self, index: int) -> float:
        """    
        Reads alpha at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: float
        :return: The alpha.
        
        
        """
        ...
    
    def SetAlpha(self, index: int, alpha: float) -> None:
        """    
        Writes alpha at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type alpha: float
        :param alpha: The alpha to set.
        
        
        """
        ...
    
    def GetColor(self, index: int) -> Vector:
        """    
        Reads color at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The color.
        
        
        """
        ...
    
    def SetColor(self, index: int, color: Vector) -> None:
        """    
        Writes color at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type color: c4d.Vector
        :param color: The color to set.
        
        
        """
        ...
    
    def GetDirection(self, index: int) -> Vector:
        """    
        Reads direction at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The direction.
        
        
        """
        ...
    
    def SetDirection(self, index: int, direction: Vector) -> None:
        """    
        Writes direction at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type direction: c4d.Vector
        :param direction: The direction to set.
        
        
        """
        ...
    
    def GetRotation(self, index: int) -> Vector:
        """    
        Reads rotation at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The rotation.
        
        
        """
        ...
    
    def SetRotation(self, index: int, rotation: Vector, pivot: Vector) -> None:
        """    
        Writes rotation at specified *index*.
        
        .. versionchanged:: R21
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type rotation: c4d.Vector
        :param rotation: The rotation to set.
        :type pivot: c4d.Vector
        :param pivot: The rotational velocity.
        
        
        """
        ...
    
    def GetPivot(self, index: int) -> Vector:
        """    
        Retrieve the rotational velocity (axe + magnitude) at specified *index*.
        
        .. versionadded:: R21
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: c4d.Vector
        :return: The rotational velocity (axe + magnitude).
        
        
        """
        ...
    
    def GetDeactivated(self, index: int) -> bool:
        """    
        Reads deactivated state at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :rtype: bool
        :return: The deactivated state.
        
        
        """
        ...
    
    def SetDeactivated(self, index: int, deact: bool) -> None:
        """    
        Writes deactivated state at specified *index*.
        
        :type index: int
        :param index: The index in the array.
        :raise IndexError: If the *index* is out of range : *0<=index<*:meth:`GetCount`.
        :type deact: bool
        :param deact: The deactivated state to set.
        
        
        """
        ...
    

class FieldObject(BaseObject):
    def __init__(self, type: int) -> None:
        """    
        Creates a :class:`FieldObject <c4d.modules.mograph.FieldObject>` instance.
        
        :type type: int
        :param type: The field type.
        :rtype: c4d.modules.mograph.FieldObject
        :return: The created :class:`FieldObject <c4d.modules.mograph.FieldObject>` instance.
        
        
        """
        ...
    
    def InitSampling(self, info: FieldInfo) -> None:
        """    
        Initializes field sampling.
        
        .. warning::
        
        Must be called before :meth:`Sample` is invoked.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to initialize sampling with.
        
        
        """
        ...
    
    def FreeSampling(self, info: FieldInfo) -> None:
        """    
        Frees any data allocated in :meth:`InitSampling`.
        
        .. warning::
        
        Must be called after sampling is finished.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` used for sampling.
        
        
        """
        ...
    
    def Sample(self, input: FieldInput, output: FieldOutputBlock, info: FieldInfo, flags: int) -> None:
        """    
        Samples points within the field.
        
        .. warning::
        
        :meth:`InitSampling` must be called before. :meth:`FreeSampling` must be called once sampling is complete.
        
        :type input: c4d.modules.mograph.FieldInput
        :param input: The points to sample in global space.
        :type output: c4d.modules.mograph.FieldOutputBlock
        :param output: The output result values, should be allocated prior to usage.
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to sample with. It should match the info used with :meth:`InitSampling`.
        :type flags: int
        :param flags: The field object sample flags:
        
        .. include:: /consts/FIELDOBJECTSAMPLE_FLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetFieldFlags(self, doc: BaseDocument) -> int:
        """    
        Returns the field flags.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :rtype: int
        :return: The field flags:
        
        .. include:: /consts/FIELDOBJECT_FLAG.rst
        :start-line: 3
        
        
        """
        ...
    

class FieldLayer(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Creates a :class:`FieldLayer <c4d.modules.mograph.FieldLayer>` instance.
        
        :type type: int
        :param type: The layer type.
        :rtype: c4d.modules.mograph.FieldLayer
        :return: The created :class:`FieldLayer <c4d.modules.mograph.FieldLayer>` instance.
        
        
        """
        ...
    
    def GetStrength(self) -> float:
        """    
        Gets the field layer's strength in percent.
        
        :rtype: float
        :return: The strength.
        
        
        """
        ...
    
    def SetStrength(self, strength: float) -> None:
        """    
        Sets the field layer's strength in percent.
        
        :type strength: float
        :param strength: The strength to set.
        
        
        """
        ...
    
    def GetBlendingMode(self) -> int:
        """    
        Gets the field layer's blending mode.
        
        :rtype: int
        :return: The blending mode. See `flbase.h/res` for values.
        
        
        """
        ...
    
    def SetBlendingMode(self, blendingMode: int) -> None:
        """    
        Sets field layer's blending mode.
        
        :type blendingMode: int
        :param blendingMode: The blending mode to set. See `flbase.h/res` for values.
        
        
        """
        ...
    
    def GetUniqueID(self) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def SetUniqueID(self, id: Any) -> None:
        """    
        Private.
        
        
        """
        ...
    
    def GetChannelFlags(self) -> int:
        """    
        Gets the enabled flags for the layer.
        
        :rtype: int
        :return: The channel flags:
        
        .. include:: /consts/FIELDLAYER_CHANNELFLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetChannelFlags(self, flags: int) -> None:
        """    
        Sets the enabled flags for the layer.
        
        :type flags: int
        :param flags: The channel flags to set:
        
        .. include:: /consts/FIELDLAYER_CHANNELFLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetChannelFlag(self, flag: int) -> bool:
        """    
        Checks a specific channel *flag* enabled state.
        
        :type flag: int
        :param flag: The flag to check:
        
        .. include:: /consts/FIELDLAYER_CHANNELFLAG.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if channel *flag* is set, otherwise **False**.
        
        
        """
        ...
    
    def SetChannelFlag(self, flag: Any, state: bool) -> None:
        """    
        Sets a specific channel *flag* enabled *state*.
        
        :type flags: int
        :param flags: The flag to set:
        
        .. include:: /consts/FIELDLAYER_CHANNELFLAG.rst
        :start-line: 3
        
        :type state: bool
        :param state: **True** to enable the flag, **False** to disable.
        
        
        """
        ...
    
    def InitSampling(self, info: FieldInfo) -> None:
        """    
        Initializes field sampling.
        
        .. warning:: Must be called before :meth:`Sample` is invoked.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to initialize sampling with.
        
        
        """
        ...
    
    def FreeSampling(self, info: FieldInfo) -> None:
        """    
        Frees any data allocated in :meth:`InitSampling`.
        
        .. warning::
        
        Must be called after sampling is finished.
        
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` instance used for sampling.
        
        
        """
        ...
    
    def Sample(self, input: FieldInput, output: FieldOutputBlock, info: FieldInfo) -> None:
        """    
        Samples the field layer.
        
        .. warning::
        
        :meth:`InitSampling` must be called before. :meth:`FreeSampling` must be called once sampling is complete.
        
        :type input: c4d.modules.mograph.FieldInput
        :param input: The points to sample in global space.
        :type output: c4d..modules.mograph.FieldOutputBlock
        :param output: The output result values, should be allocated prior to usage.
        :type info: c4d.modules.mograph.FieldInfo
        :param info: The :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` to sample with. It should match the info used with :meth:`InitSampling`.
        
        
        """
        ...
    
    def Aggregate(self, input: Any, output: Any, info: Any) -> None:
        """    
        Private
        
        
        """
        ...
    
    def GetLayerFlags(self) -> int:
        """    
        Gets the layer's execution and display *flags*.
        
        :rtype: int
        :return: The layer flags:
        
        .. include:: /consts/FIELDLAYER_FLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetLayerFlags(self, flags: int, state: bool) -> None:
        """    
        Sets the layer's execution and display *flags*.
        
        :type flags: int
        :param flags: The layer flag to set:
        
        .. include:: /consts/FIELDLAYER_FLAG.rst
        :start-line: 3
        
        :type state: bool
        :param state: **True** to set, **False** to clear.
        
        
        """
        ...
    
    def GetLinkedObject(self, doc: BaseDocument) -> BaseList2D:
        """    
        Gets the linked object.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document the :class:`FieldLayer <c4d.modules.mograph.FieldLayer>` belongs to.
        :rtype: c4d.BaseList2D
        :return: The linked object.
        
        
        """
        ...
    
    def SetLinkedObject(self, link: BaseList2D) -> None:
        """    
        Sets the linked object.
        
        :type link: c4d.BaseList2D
        :param link: The object to link.
        
        
        """
        ...
    
    def GetMaskHead(self) -> GeListHead:
        """    
        If the :class:`c4d.FieldLayer` has a mask then this retrieve the list head containing the mask layers.
        
        :rtype: c4d.GeListHead
        :return: The GeListHead containing the mask layers, **None** if masks aren't active on this layer.
        
        
        """
        ...
    
    def AddMask(self) -> bool:
        """    
        Adds a mask to the :class:`c4d.FieldLayer`, if a mask already exists then this will do nothing.
        
        :rtype: bool
        :return: **True** on success.
        
        
        """
        ...
    
    def RemoveMask(self, link: bool) -> None:
        """    
        Removes the mask on the :class:`c4d.FieldLayer`, if no mask exists then this will do nothing.
        
        .. note::
        
        In c++ the parameter `link` is named `deleteLayers`, it's probable that it will change as well in Python.
        
        :param link: **True** to delete the layers in the mask, **False** to retain them so that when enabled again via :meth:`c4d.AddMask` the layers will reappear.
        :type link: bool
        
        
        """
        ...
    

class FieldInput(object):
    def __init__(self, position: List[Vector], allocatedCount: int, transform: Matrix, fullCount: int, direction: List[Vector], uvw: List[Vector]) -> None:
        """    
        Creates a :class:`FieldInput <c4d.modules.mograph.FieldInput>` instance.
        
        :type position: List[c4d.Vector]
        :param position: The position list to sample.
        :type allocatedCount: int
        :param allocatedCount: The length of the *position* list.
        :type transform: c4d.Matrix
        :param transform: The transform matrix required to convert the position and direction inputs to global space.
        :type fullCount: int
        :param fullCount: The full position count if *allocatedCount* is too big to allocate *position* list. If not set *allocatedCount* is used instead.
        :type direction: List[c4d.Vector]
        :param direction: The direction list to sample.
        :type uvw: List[c4d.Vector]
        :param uvw: The uvw list to sample.
        :rtype: c4d.modules.mograph.FieldInput
        :return: The created :class:`FieldInput <c4d.modules.mograph.FieldInput>` instance.
        
        
        """
        ...
    
    def GetSubBlock(self, offset: int, blockSize: int) -> FieldInput:
        """    
        Retrieves a :class:`FieldInput <c4d.modules.mograph.FieldInput>` for a subset of the original block.
        
        .. note::
        
        Useful to pass smaller blocks to the field processing threads.
        
        :type offset: int
        :param offset: The sub-block start offset.
        :type blockSize: int
        :param blockSize: The size of the desired sub-block. `400` is the recommended size.
        :rtype: c4d.modules.mograph.FieldInput
        :return: The sub-block :class:`FieldInput <c4d.modules.mograph.FieldInput>`.
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if the :class:`FieldInput <c4d.modules.mograph.FieldInput>` allocations and sizes are valid.
        
        .. note::
        
        Default empty :class:`FieldInput <c4d.modules.mograph.FieldInput>` is considered valid.
        
        :rtype: bool
        :return: **True** if the :class:`FieldInput <c4d.modules.mograph.FieldInput>` is valid, otherwise **False**.
        
        
        """
        ...
    
    def IsPopulated(self) -> bool:
        """    
        Checks if the :class:`FieldInput <c4d.modules.mograph.FieldInput>` is valid and non-empty.
        
        :rtype: bool
        :return: **True** if the :class:`FieldInput <c4d.modules.mograph.FieldInput>` is populated, otherwise **False**.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Returns the number of elements in the :class:`FieldInput <c4d.modules.mograph.FieldInput>`.
        
        :rtype: int
        :return: The number of elements.
        
        
        """
        ...
    
    def GetOffset(self) -> int:
        """    
        Returns the offset of the first element in full arrays.
        
        :rtype: int
        :return: The offset.
        
        
        """
        ...
    

class FieldInfo(object):
    def __init__(self) -> None:
        """    
        Creates a :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` instance.
        
        :rtype: c4d.modules.mograph.FieldInfo
        :return: The created :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` instance.
        
        
        """
        ...
    
    def Create(self, flags: int, thread: BaseThread, doc: BaseDocument, currentThreadIndex: int, threadCount: int, inputs: Optional[FieldInput] = ..., callers: Optional[List[BaseList2D]] = ...) -> FieldInfo:
        """    
        Creates a :class:`c4d.modules.mograph.FieldInfo` while relaying potential allocation errors.
        
        :type flags: int
        :param flags: The channels to sample.
        
        .. include:: /consts/FIELDSAMPLE_FLAG.rst
        :start-line: 3
        
        :type thread: c4d.threading.BaseThread
        :param thread: The caller thread.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to sample.
        :type currentThreadIndex: int
        :param currentThreadIndex: The thread index that will sample those points.
        :type threadCount: int
        :param threadCount: The total thread count.
        :type inputs: Optional[c4d.modules.mograph.FieldInput]
        :param inputs: The full point list.
        :type callers: Optional[list(c4d.BaseList2D)]
        :param callers: An initializer list to build the stack, first item is base of stack.
        :rtype: `c4d.modules.mograph.FieldInfo`
        :return: The created FieldInfo
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if the :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` data is valid.
        
        .. note::
        
        Default empty :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` is considered valid.
        
        :rtype: bool
        :return: **True** if the :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` is valid, otherwise **False**.
        
        
        """
        ...
    
    def IsPopulated(self) -> bool:
        """    
        Checks if the :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` data is valid and non-empty.
        
        .. note::
        
        Required :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` content should be set and ready for sampling.
        
        :rtype: bool
        :return: **True** if the :class:`FieldInfo <c4d.modules.mograph.FieldInfo>` is populated, otherwise **False**.
        
        
        """
        ...
    

class FieldCallerStack(object):
    def __init__(self) -> None:
        """    
        Creates a :class:`c4d.modules.mograph.FieldCallerStack` instance.
        
        :rtype: c4d.modules.mograph.FieldCallerStack
        :return: The created :class:`c4d.modules.mograph.FieldCallerStack` instance.
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> BaseList2D:
        """    
        Retrieves a caller from the stack by index.
        
        :type key: int
        :param key: The caller index.
        :raise IndexError: If the index *key* is out of range : *0<=key<*:meth:`GetCount`.
        :rtype: c4d.BaseList2D
        :return: The caller.
        
        
        """
        ...
    
    def CopyFrom(self, src: FieldCallerStack) -> bool:
        """    
        Copies from the supplied :class:`FieldCallerStack <c4d.modules.mograph.FieldCallerStack>` *src*.
        
        :type src: c4d.modules.mograph.FieldCallerStack
        :param src: The source.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def RecalcValue(self) -> int:
        """    
        Calculates the ID of the caller stack from scratch. Does not update stored ID value.
        
        :rtype: int
        :return: The new caller stack ID.
        
        
        """
        ...
    
    def UpdateValue(self) -> None:
        """    
        Recalculates the ID of the caller stack from scratch and updates the internal stack ID value.
        
        
        """
        ...
    
    def Add(self, caller: BaseList2D) -> bool:
        """    
        Adds a caller to the stack and updates the stack ID.
        
        :type caller: c4d.BaseList2D
        :param caller: The caller object to add to the stack.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Returns the number of callers involved in the stack.
        
        :rtype: int
        :return: The number of callers.
        
        
        """
        ...
    
    def GetValue(self) -> int:
        """    
        Returns the caller stack ID.
        
        :rtype: int
        :return: The caller stack ID.
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if the caller stack is valid.
        
        .. note::
        
        | An empty stack is valid.
        | A stack with broken links to callers is not valid.
        
        .. warning::
        
        A non empty stack with no stack ID value is not valid.
        
        :rtype: bool
        :return: **True** if the caller stack is valid, otherwise **False**.
        
        
        """
        ...
    

class FalloffDataData(object):
    ...

class C4D_Falloff(object):
    def __init__(self) -> None:
        """    
        Creates a new :class:`C4D_Falloff <c4d.modules.mograph.C4D_Falloff>`.
        
        :rtype: c4d.modules.mograph.C4D_Falloff
        :return: A new falloff.
        
        
        """
        ...
    
    def InitFalloff(self, bc: BaseContainer, doc: Optional[BaseDocument] = ..., op: Optional[BaseObject] = ...) -> bool:
        """    
        Initializes the falloff.
        
        .. warning::
        
        Always call before the sample routines.
        
        .. note::
        
        It is recommended to pass at least one of the parameters, however not compulsory.
        
        :type bc: c4d.BaseContainer
        :param bc: Optional container of the object owning the falloff. If given the :class:`FalloffDataData <c4d.modules.mograph.FalloffDataData>` is extracted from this container.
        :type doc: c4d.documents.BaseDocument
        :param doc: Optional document used to retrieve the current time for the animation of the Spline GUI offset.
        :type op: c4d.BaseObject
        :param op: Optional object used to set the matrix. If no container is given for *bc*, this object's container will be used instead.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Sample(self, point: Vector, usespline: bool, weight: Optional[float] = ...) -> float:
        """    
        Samples the falloff for any point in space.
        
        :type point: c4d.Vector
        :param point: The point to sample in world space.
        :type usespline: bool
        :param usespline: Use the Spline GUI if it exists. Defaults to **True**.
        :type weight: float
        :param weight: An optional weight offset. Equivalent of adding this value to the falloff result before clamping.
        :rtype: float
        :return: The sampled value.
        
        
        """
        ...
    
    def MultiSample(self, points: List[Vector], usespline: bool, weight: Optional[float] = ...) -> List[float]:
        """    
        Samples the falloff for an array of points in space.
        
        :type points: list of c4d.Vector
        :param points: The array of points to sample in world space.
        :type usespline: bool
        :param usespline: Use the Spline GUI if it exists. Defaults to **True**.
        :type weight: float
        :param weight: An optional weight offset. Equivalent of adding this value to the falloff result before clamping.
        :rtype: list of float
        :return: The sampled values.
        
        
        """
        ...
    
    def AddFalloffToDescription(self, description: Description, bc: Optional[BaseContainer] = ...) -> bool:
        """    
        Adds the falloff to a description.
        
        .. note::
        
        Use this function within the implementation of :meth:`NodeData.GetDDescription`.
        
        :type description: c4d.Description
        :param description: The description to add the falloff GUI to.
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Message(self, id: int, bc: Optional[BaseContainer] = ..., data: Optional[Any] = ...) -> bool:
        """    
        Sends messages to the falloff.
        
        .. note::
        
        Use this function from within the implementation of :meth:`NodeData.Message` to pass all messages to the falloff.
        
        .. seealso::
        
        :doc:`MSG </consts/MSG_C4DATOM>` for the information on the messages type, data and input/output.
        
        :type id: int
        :param id: The message type.
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :type data: any
        :param data: The message data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetHandleCount(self, bc: Optional[BaseContainer] = ...) -> int:
        """    
        Returns the number of handles for the falloff.
        
        .. note::
        
        Use this function from within the implementation of :meth:`ObjectData.GetHandleCount`.
        
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :rtype: int
        :return: The handle count.
        
        
        """
        ...
    
    def GetHandle(self, index: int, bc: BaseContainer, info: HandleInfo) -> None:
        """    
        Returns a handle for the falloff.
        
        .. note::
        
        Use this function from within the implementation of :meth:`ObjectData.GetHandle`.
        
        :type index: int
        :param index: The handle index.
        :type bc: c4d.BaseContainer
        :param bc: The falloff's container. Normally this is the owning object's container.
        :type info: c4d.HandleInfo
        :param info: The information for the requested handle.
        
        
        """
        ...
    
    def SetHandle(self, index: int, point: Vector, bc: BaseContainer, info: HandleInfo) -> None:
        """    
        Set a handle for the falloff.
        
        .. note::
        
        Use this function from within the implementation of :meth:`ObjectData.SetHandle`.
        
        :type index: int
        :param index: The handle index.
        :type point: c4d.Vector
        :param point: The new position for the handle.
        :type bc: c4d.BaseContainer
        :param bc: The falloff's container. Normally this is the owning object's container.
        :type info: c4d.HandleInfo
        :param info: The information for the handle.
        
        
        """
        ...
    
    def Draw(self, bd: BaseDraw, bh: BaseDrawHelp, drawpass: int, bc: Optional[BaseContainer] = ...) -> bool:
        """    
        Draws the falloff into a view.
        
        .. note::
        
        Use this function from within the implementation of :meth:`ObjectData.Draw` or :meth:`ToolData.Draw`.
        
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The editor's view help.
        :type drawpass: int
        :param drawpass: The draw pass:
        
        .. include:: /consts/DRAWPASS.rst
        :start-line: 3
        
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def CopyTo(self, dest: C4D_Falloff) -> bool:
        """    
        Copies the falloff to another falloff.
        
        .. note::
        
        Use this function from within the implementation of :meth:`NodeData.CopyTo`. Necessary for handles to work correctly with the undo system.
        
        :type dest: c4d.modules.mograph.C4D_Falloff
        :param dest: The destination falloff.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetDirty(self) -> None:
        """    
        Sets the falloff dirty.
        
        
        """
        ...
    
    def GetDirty(self, bc: Optional[BaseContainer] = ..., doc: Optional[BaseDocument] = ...) -> int:
        """    
        Returns the falloff dirty value.
        
        .. note::
        
        Useful to check if the falloff needs to be resampled.
        
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :type doc: c4d.documents.BaseDocument
        :param doc:
        
        .. versionadded:: R20
        
        The document.
        
        :rtype: int
        :return: The dirty value.
        
        
        """
        ...
    
    def SetMg(self, mg: Matrix) -> None:
        """    
        Sets the falloff's matrix.
        
        :type mg: c4d.Matrix
        :param mg: The new falloff's matrix.
        
        
        """
        ...
    
    def GetMg(self) -> Matrix:
        """    
        Returns the falloff's matrix.
        
        :rtype: c4d.Matrix
        :return: The matrix.
        
        
        """
        ...
    
    def SetData(self, data: FalloffDataData) -> None:
        """    
        Sets the falloff's data directly.
        
        :type data: c4d.modules.mograph.FalloffDataData
        :param data: The new falloff's data.
        
        
        """
        ...
    
    def GetData(self) -> FalloffDataData:
        """    
        Returns the falloff's data.
        
        :rtype: c4d.modules.mograph.FalloffDataData
        :return: The falloff's data.
        
        
        """
        ...
    
    def GetContainerInstance(self) -> BaseContainer:
        """    
        Returns the last container the falloff should try to use.
        
        .. note::
        
        If the falloff has not been given a container at any point it will generate one internally.
        
        :rtype: c4d.BaseContainer
        :return: The falloff's container instance. Guaranteed to be always valid.
        
        
        """
        ...
    
    def SetMode(self, type: int, bc: Optional[BaseContainer] = ...) -> bool:
        """    
        Sets the falloff mode.
        
        :type type: int
        :param type: The new falloff mode. See `ofalloff_panel.h`.
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetMode(self) -> int:
        """    
        Returns the falloff mode.
        
        :rtype: int
        :return: The falloff's mode. See `ofalloff_panel.h`.
        
        
        """
        ...
    
    def SetTime(self, time: BaseTime, bc: Optional[BaseContainer] = ...) -> None:
        """    
        Sets the current falloff time.
        
        .. note::
        
        Used only for the animated Spline GUI offset, not for any other values currently.
        
        :type time: c4d.BaseTime
        :param time: The new falloff time.
        :type bc: c4d.BaseContainer
        :param bc: Optionally pass the container of the object owning the falloff.
        
        
        """
        ...
    


def GeGetMoData(op: BaseObject) -> None:
    """    
    Returns the MoGraph data of an object.
    
    :type op: c4d.BaseObject
    :param op: The object.
    :rtype: :class:`MoData`
    :return: The MoGraph data.
    
    
    """
    ...

def GeGetMoDataSelection(op: BaseList2D) -> None:
    """    
    Retrieves the MoGraph clones selection.
    
    .. versionadded:: R18.020
    
    :type op: c4d.BaseList2D
    :param op: Can be either a MoGraph Selection tag `BaseTag(c4d.Tmgselection)` or an object with a MoGraph Selection tag.
    :rtype: :class:`c4d.BaseSelect`
    :return: The clones selection.
    
    
    """
    ...

def GeSetMoDataSelection(op: BaseList2D, selection: BaseSelect) -> bool:
    """    
    Sets the MoGraph clones selection.
    
    .. versionadded:: R18.039
    
    .. warning::
    
    | Before R21, makes sure to call :meth:`C4DAtom.SetDirty` after any usage of this method to properly updates the mograph object.
    | In R21 this bug was fixed so the next code is no more needed.
    
    .. code-block:: python
    
    # mographObject is the host mograph object of the MoGraph Selection tag: BaseTag(c4d.Tmgselection).
    mographObject.SetDirty(c4d.DIRTYFLAGS_DATA)
    mographObject.Message(c4d.MSG_UPDATE)
    
    :type op: c4d.BaseList2D
    :param op: Can be either a MoGraph Selection tag `BaseTag(c4d.Tmgselection)` or an object with a MoGraph Selection tag.
    :type selection: c4d.BaseSelect
    :param selection: The clones selection to set.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GeGetMoDataWeights(op: BaseList2D) -> List[float]:
    """    
    Retrieves the MoGraph clones weights.
    
    .. versionadded:: R18.020
    
    :type op: c4d.BaseList2D
    :param op: Can be either a MoGraph Weightmap tag `BaseTag(c4d.Tmgweight)` or an object with a MoGraph Weightmap tag.
    :rtype: list of float
    :return: The clones weights.
    
    
    """
    ...

def GeSetMoDataWeights(op: BaseList2D, weights: List[float]) -> bool:
    """    
    Sets the MoGraph clones weights.
    
    .. versionadded:: R18.039
    
    .. warning::
    
    Before R21, makes sure to call :meth:`C4DAtom.SetDirty` after any usage of this method to properly updates the mograph object.
    In R21 this bug was fixed so the next code is no more needed.
    
    .. code-block:: python
    
    # mographObject is the host mograph object of the MoGraph Weight tag: BaseTag(c4d.Tmgweight).
    # moSelTag is a BaseTag(c4d.Tmgweight)
    moSelTag.SetDirty(c4d.DIRTYFLAGS_DATA)
    mographObject.SetDirty(c4d.DIRTYFLAGS_DATA)
    mographObject.Message(c4d.MSG_UPDATE)
    
    :type op: c4d.BaseList2D
    :param op: Can be either a MoGraph Weight tag `BaseTag(c4d.Tmgweight)` or an object with a MoGraph Weight tag.
    :type weights: list of float
    :param weights: The clones weights to set.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GetMoDataDefault(id: int) -> Any:
    """    
    Get the default value for the specified :class:`MoData` ID.
    
    :type id: int
    :param id: The :class:`MoData` ID:
    
    .. include:: /consts/MODATA.rst
    :start-line: 3
    
    :rtype: Any
    :return: The default value.
    
    
    """
    ...

def GetMoDataDefaultType(id: int) -> int:
    """    
    Get the default value for the specified :class:`MoData` ID.
    
    :type id: int
    :param id: The :class:`MoData` ID:
    
    .. include:: /consts/MODATA.rst
    :start-line: 3
    
    :rtype: int
    :return: The default type:
    
    .. include:: /consts/MD.rst
    :start-line: 3
    
    
    """
    ...

