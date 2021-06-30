from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import Vector, Matrix, BaseTime, BaseContainer, GeListNode
from c4d.bitmaps import BaseBitmap
from c4d.documents import BaseDocument


class ByteSeq(object):
    def __init__(self, buf: Any, len: int, readonly: bool) -> None:
        """    
        Allocates a byte sequence.
        
        :type buf: PyCObject or None
        :param buf: PyCObject address or **None** to allocate a new pool of memory.
        :type len: int
        :param len: The length of the new byte sequence.
        :type readonly: bool
        :param readonly: Set to **True** if the byte sequence should be flagged as read-only, otherwise **False**.
        :rtype: c4d.storage.ByteSeq
        :return: The byte sequence object.
        
        
        """
        ...
    
    def __str__(self) -> str:
        """    
        Creates a string object from the byte sequence.
        
        :rtype: str
        :return: The byte-sequence returned as a string.
        
        
        """
        ...
    
    def __add__(self, other: int) -> ByteSeq:
        """    
        :type other: int
        :param other: The offset value.
        :rtype: c4d.storage.ByteSeq
        :returns: New :class:`ByteSeq <c4d.storage.ByteSeq>` object.
        
        
        """
        ...
    
    def __compare__(self, other: ByteSeq) -> bool:
        """    
        Compares two byte sequences.
        
        :type other: c4d.storage.ByteSeq
        :param other:  The other byte sequence.
        :rtype: bool
        :return: **True** if the byte sequences are equal, otherwise **False**.
        
        
        """
        ...
    
    def __iter__(self) -> Iterable[str]:
        """    
        Iterates over the bytes of the object, interpreted as one-element string.
        
        .. literalinclude:: /../../doc.python.code/c4d/storage/byteseq/iter.py
        :language: python
        
        :rtype: iter for str
        :return: The iterator.
        
        
        """
        ...
    
    def __hash__(self) -> int:
        """    
        | Returns a hash of the byte sequence.
        | The hash value is cached if the object owns the byte sequence and it is flagged as read-only.
        
        print hash(bs)
        
        :rtype: int
        :return: The hash.
        
        
        """
        ...
    
    def __len__(self) -> int:
        """    
        Returns the length of the byte sequence.
        
        :rtype: int
        :return: The length.
        
        
        """
        ...
    
    def __setitem__(self, key: Union[int, List[Any]], value: int) -> None:
        """    
        Replaces a byte at position *key* with the new *value*:
        
        .. literalinclude:: /../../doc.python.code/c4d/storage/byteseq/getitem.py
        :language: python
        
        :raise TypeError: If byte sequence is flagged as read-only.
        :type key: Union[int, Slice[Any]]
        :param key: The index.
        :type value: int
        :param value: The new value, must be between `0-255`.
        
        
        """
        ...
    
    def __getitem__(self, key: Union[int, List[Any]]) -> str:
        """    
        Gets the bytes at position key:
        
        .. literalinclude:: /../../doc.python.code/c4d/storage/byteseq/getitem.py
        :language: python
        
        :type key: Union[int, Slice[Any]]
        :param key: The index
        :rtype: str
        :return: The bytes at the requested position.
        
        
        """
        ...
    
    def GetClone(self) -> ByteSeq:
        """    
        Clones a byte sequence.
        
        :rtype: c4d.storage.ByteSeq
        :return: The clone.
        
        
        """
        ...
    
    def GetOffset(self, o: int) -> None:
        """    
        Returns buffer at offset *o* in this byte sequence.
        
        :type o: int
        :param o: The offset.
        :return: The buffer object.
        
        
        """
        ...
    

class HyperFile(object):
    def __init__(self) -> None:
        """    
        Allocates a hyper file.
        
        :rtype: c4d.storage.HyperFile
        :return: The hyper file.
        
        
        """
        ...
    
    def Open(self, ident: int, filename: Union[str, MemoryFileStruct], mode: int, error_dialog: int) -> bool:
        """    
        Opens the hyper file.
        
        :type ident: int
        :param ident: File identification.
        :type filename: Union[str, c4d.storage.MemoryFileStruct]
        :param filename: File to open.
        :type mode: int
        :param mode: File mode:
        
        .. include:: /consts/FILEOPEN.rst
        :start-line: 3
        
        :type error_dialog: int
        :param error_dialog: File error dialog:
        
        .. include:: /consts/FILEDIALOG.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the hyper file could be opened, otherwise **False**.
        
        
        """
        ...
    
    def Close(self) -> bool:
        """    
        Closes the hyper file.
        
        :rtype: bool
        :return: **True** on success.
        
        
        """
        ...
    
    def WriteChar(self, v: int) -> bool:
        """    
        Write a character to the hyperfile.
        
        :type v: int
        :param v: A char to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteUChar(self, v: int) -> bool:
        """    
        Write a very short int to the hyperfile.
        
        :type v: int
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteInt16(self, v: int) -> bool:
        """    
        Write a signed short int to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteUInt16(self, v: int) -> bool:
        """    
        Write an unsigned short int to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteInt32(self, v: int) -> bool:
        """    
        Write an int to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteUInt32(self, v: int) -> bool:
        """    
        Write an unsigned int to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteInt64(self, v: int) -> bool:
        """    
        Write a double precision int value to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The integer to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteUInt64(self, v: int) -> bool:
        """    
        Write a double precision unsigned int value to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: int
        :param v: The integer to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteFloat32(self, v: float) -> bool:
        """    
        Write a float value to the hyperfile.
        
        .. versionadded:: R16.021
        
        :type v: float
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteFloat64(self, v: float) -> bool:
        """    
        Write a double precision float value to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: float
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteVector(self, v: Vector) -> bool:
        """    
        Write a :class:`Vector <c4d.Vector>` to the hyperfile.
        
        :type v: c4d.Vector
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteVector32(self, v: Vector) -> bool:
        """    
        Write a :class:`Vector <c4d.Vector>` to the hyperfile.
        
        .. versionadded:: R16.021
        
        :type v: c4d.Vector
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteVector64(self, v: Vector) -> bool:
        """    
        Write a double precision :class:`Vector <c4d.Vector>` to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: c4d.Vector
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteMatrix(self, v: Matrix) -> bool:
        """    
        Write a :class:`Matrix <c4d.Matrix>` to the hyperfile.
        
        :type v: c4d.Matrix
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteMatrix32(self, v: Matrix) -> bool:
        """    
        Write a :class:`Matrix <c4d.Matrix>` to the hyperfile.
        
        .. versionadded:: R16.021
        
        :type v: c4d.Matrix
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteMatrix64(self, v: Matrix) -> bool:
        """    
        Write a double precision :class:`Matrix <c4d.Matrix>` to the hyperfile.
        
        .. versionadded:: R15.037
        
        :type v: c4d.Matrix
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteBool(self, v: bool) -> bool:
        """    
        Write a bool to the hyperfile.
        
        :type v: bool
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteTime(self, v: BaseTime) -> bool:
        """    
        Write a :class:`BaseTime <c4d.BaseTime>` to the hyperfile.
        
        :type v: c4d.BaseTime
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteString(self, v: str) -> bool:
        """    
        Write a string to the hyperfile.
        
        :type v: str
        :param v: The value to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteFilename(self, v: str) -> bool:
        """    
        Write a path to the hyperfile.
        
        :type v: str
        :param v: The path to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteImage(self, v: BaseBitmap, format: int, data: BaseContainer, savebits: int) -> bool:
        """    
        Write an image to the hyperfile.
        
        :type v: c4d.bitmaps.BaseBitmap
        :param v: The bitmap to write to the hyperfile.
        :type format: int
        :param format: The image format:
        
        .. include:: /consts/FILTER.rst
        :start-line: 3
        
        :type data: c4d.BaseContainer
        :param data: A container with additional format settings, or **None**.
        
        .. include:: /consts/SAVEBIT.rst
        :start-line: 3
        
        :type savebits: int
        :param savebits: The save bits:
        
        .. include:: /consts/SAVEBIT.rst
        :start-line: 3
        
        :rtype: bool
        :return: Success of writing the image.
        
        
        """
        ...
    
    def WriteContainer(self, v: BaseContainer) -> bool:
        """    
        Write the settings in a :class:`BaseContainer <c4d.BaseContainer>` to the hyperfile.
        
        :type v: c4d.BaseContainer
        :param v: The container to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def WriteMemory(self, data: ByteSeq) -> bool:
        """    
        Write a block of memory to the hyperfile.
        
        .. note::
        
        Only use this when you need to, be aware that the byte sequences will not be platform independent.
        
        :type data: c4d.storage.ByteSeq
        :param data: The data to write to the hyperfile.
        :rtype: bool
        :return: Success of writing the data.
        
        
        """
        ...
    
    def WriteData(self, v: Any) -> bool:
        """    
        Write data to the container.
        
        .. note::
        
        Please check the constructor of **GeData** in the C++ SDK to see what type this method accepts.
        
        :type v: any
        :param v: The data.
        :rtype: bool
        :return: Success of writing the value.
        
        
        """
        ...
    
    def ReadChar(self) -> int:
        """    
        Read a character from the hyperfile.
        
        :rtype: int
        :return: The character or **None** if reading failed.
        
        
        """
        ...
    
    def ReadUChar(self) -> int:
        """    
        Read an unsigned character from the hyperfile.
        
        :rtype: int
        :return: The unsigned character or **None** if reading failed.
        
        
        """
        ...
    
    def ReadInt16(self) -> int:
        """    
        Read a signed word from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The unsigned word or **None** if reading failed.
        
        
        """
        ...
    
    def ReadUInt16(self) -> int:
        """    
        Read an unsigned word from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The unsigned word or **None** if reading failed.
        
        
        """
        ...
    
    def ReadInt32(self) -> int:
        """    
        Read an int from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The unsigned int or **None** if reading failed.
        
        
        """
        ...
    
    def ReadUInt32(self) -> int:
        """    
        Read an unsigned int from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The unsigned int or **None** if reading failed.
        
        
        """
        ...
    
    def ReadInt64(self) -> int:
        """    
        Read a double precision int from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: int
        :return: The value or **None** if reading failed.
        
        
        """
        ...
    
    def ReadUInt64(self) -> int:
        """    
        Read a double precision unsigned int from the hyperfile.
        
        .. versionadded:: R16.021
        
        :rtype: int
        :return: The value or **None** if reading failed.
        
        
        """
        ...
    
    def ReadFloat(self) -> float:
        """    
        Read a float from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: float
        :return: The float or **None** if reading failed.
        
        
        """
        ...
    
    def ReadFloat32(self) -> float:
        """    
        Read a float from the hyperfile.
        
        .. versionadded:: R16.021
        
        :rtype: float
        :return: The float or **None** if reading failed.
        
        
        """
        ...
    
    def ReadFloat64(self) -> float:
        """    
        Read a double precision float from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: float
        :return: The float or **None** if reading failed.
        
        
        """
        ...
    
    def ReadVector(self) -> Vector:
        """    
        Read a :class:`Vector <c4d.Vector>` from the hyperfile.
        
        :rtype: c4d.Vector
        :return: The vector or **None** if reading failed.
        
        
        """
        ...
    
    def ReadVector32(self) -> Vector:
        """    
        Read a :class:`Vector <c4d.Vector>` from the hyperfile.
        
        .. versionadded:: R16.021
        
        :rtype: c4d.Vector
        :return: The vector or **None** if reading failed.
        
        
        """
        ...
    
    def ReadVector64(self) -> Vector:
        """    
        Read a double precision :class:`Vector <c4d.Vector>` from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: c4d.Vector
        :return: The vector or **None** if reading failed.
        
        
        """
        ...
    
    def ReadMatrix(self) -> Matrix:
        """    
        Read a :class:`Matrix <c4d.Matrix>` from the hyperfile.
        
        :rtype: c4d.Matrix
        :return: The matrix or **None** if reading failed.
        
        
        """
        ...
    
    def ReadMatrix32(self) -> Matrix:
        """    
        Read a :class:`Matrix <c4d.Matrix>` from the hyperfile.
        
        .. versionadded:: R16.021
        
        :rtype: c4d.Matrix
        :return: The matrix or **None** if reading failed.
        
        
        """
        ...
    
    def ReadMatrix64(self) -> Matrix:
        """    
        Read a double precision :class:`Matrix <c4d.Matrix>` from the hyperfile.
        
        .. versionadded:: R15.037
        
        :rtype: c4d.Matrix
        :return: The matrix or **None** if reading failed.
        
        
        """
        ...
    
    def ReadBool(self) -> bool:
        """    
        Read a bool from the hyperfile.
        
        :rtype: bool
        :return: The bool or **None** if reading failed.
        
        
        """
        ...
    
    def ReadTime(self) -> BaseTime:
        """    
        Read a :class:`BaseTime <c4d.BaseTime>` from the hyperfile.
        
        :rtype: c4d.BaseTime
        :return: The time or **None** if reading failed.
        
        
        """
        ...
    
    def ReadString(self) -> str:
        """    
        Read a string from the hyperfile.
        
        :rtype: str
        :return: The string or **None** if reading failed.
        
        
        """
        ...
    
    def ReadFilename(self) -> str:
        """    
        Read a path from the hyperfile.
        
        :rtype: str
        :return: The path or **None** if reading failed.
        
        
        """
        ...
    
    def ReadImage(self) -> BaseBitmap:
        """    
        Read a bitmap from the hyperfile.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The bitmap or **None** if reading failed.
        
        
        """
        ...
    
    def ReadContainer(self) -> BaseBitmap:
        """    
        Read a container from the hyperfile.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The container or **None** if reading failed.
        
        
        """
        ...
    
    def ReadMemory(self) -> ByteSeq:
        """    
        Read a block of memory from the hyperfile.
        
        .. note::
        
        Only use this when you need to, be aware that the byte sequences will not be platform independent.
        
        :rtype: c4d.storage.ByteSeq
        :return: The value or **None** if reading failed.
        
        
        """
        ...
    
    def ReadData(self) -> Any:
        """    
        Read a data from the hyperfile.
        
        .. note::
        
        Please check the constructor of **GeData** in the C++ SDK to see what type this method accepts.
        
        :rtype: Any
        :return: The value or **None** if reading failed.
        
        
        """
        ...
    
    def GetError(self) -> int:
        """    
        Get the error from the last hyperfile operation.
        
        :rtype: int
        :return: The error number.
        
        
        """
        ...
    
    def SetError(self, err: int) -> None:
        """    
        Set the error value for this hyperfile.
        
        :type err: int
        :param err: The error number.
        
        
        """
        ...
    
    def ReadValueHeader(self) -> int:
        """    
        Read the value header from the file. This is only necessary in combination with loops.
        
        Example:
        
        .. literalinclude:: /../../doc.python.code/c4d/storage/hyperfile/readvalueheader.py
        :language: python
        
        :rtype: int
        :return: The header value or **None**:
        
        .. include:: /consts/HYPERFILEVALUE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SkipValue(self, h: int) -> bool:
        """    
        Skip a given type of value.
        
        :type h: int
        :param h: The hyper file value to skip:
        
        .. include:: /consts/HYPERFILEVALUE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the value was of the given header type and it was skipped, otherwise **False**.
        
        
        """
        ...
    
    def WriteChunkStart(self, id: int, level: int) -> bool:
        """    
        Write a chunk marker into the file indicating the beginning of a new chunk of data.
        
        .. note::
        
        | Chunks should only be used if absolutely necessary.
        | If a plugin uses chunks badly then the file structure can become corrupted.
        
        :type id: int
        :param id: The ID for the chunk.
        :type level: int
        :param level: If you want to write additional information you can increase the level this allows you to easily save/read new values.
        :rtype: bool
        :return: Success of writing the chunk identification.
        
        
        """
        ...
    
    def WriteChunkEnd(self) -> bool:
        """    
        Write a chunk ending marker into the file.
        
        :rtype: bool
        :return: Success of writing the chunk end.
        
        
        """
        ...
    
    def ReadChunkStart(self) -> None:
        """    
        Read a chunks identification from the file.
        
        .. literalinclude:: /../../doc.python.code/c4d/storage/hyperfile/readchunkstart.py
        :language: python
        
        :rtype: dict{**id**: int, **level**: int}
        :return: The identification or **None** on failure.
        
        
        """
        ...
    
    def ReadChunkEnd(self) -> bool:
        """    
        Read a chunks end marker from the file.
        
        :rtype: bool
        :return: Success of reading the chunk end.
        
        
        """
        ...
    
    def SkipToEndChunk(self) -> bool:
        """    
        Move the file pointer to the end of the chunk.
        
        .. note::
        
        This should always be called after finishing reading your values from this chunk.
        
        :rtype: bool
        :return: Success of finding the end of the chunk.
        
        
        """
        ...
    
    def GetDocument(self) -> BaseDocument:
        """    
        Gets the active document for the hyper file operation.
        
        .. note::
        
        Can be **None**, for example when saving layouts.
        
        :rtype: c4d.documents.BaseDocument
        :return: The document or **None**.
        
        
        """
        ...
    
    def GetFileVersion(self) -> int:
        """    
        Get the version of Cinema 4D that wrote the file.
        
        .. note::
        
        Only valid during reading a Cinema 4D scene, object, material etc.
        
        :rtype: int
        :return: The file version.
        
        
        """
        ...
    
    def GetFilterFlags(self) -> int:
        """    
        Gets the filter flags, the value is valid only during a Load or a Merge.
        
        .. versionadded:: R21.108
        
        :rtype: int
        :return: The filter flags:
        
        .. include:: /consts/SCENEFILTER.rst
        :start-line: 3
        
        
        """
        ...
    

class MemoryFileStruct(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.storage.MemoryFileStruct
        :return: The memory file object.
        
        
        """
        ...
    
    def SetMemoryReadMode(self, adr: Union[ByteSeq, str], size: int) -> None:
        """    
        Sets the buffer read from a memory block instead of from a file.
        
        :type adr: Union[c4d.storage.ByteSeq, str]
        :param adr: The memory address to read from.
        :type size: int
        :param size: The size of the memory block, or -1 if the buffer is "big enough".
        
        
        """
        ...
    
    def SetMemoryWriteMode(self) -> None:
        """    
        Sets the buffer ready to be written to.
        
        
        """
        ...
    
    def GetData(self) -> None:
        """    
        Retrieves all data written to the memory file.
        
        :rtype: tuple(:class:`ByteSeq <c4d.storage.ByteSeq>`, int)
        :return: A tuple with the buffer data and size.
        
        
        """
        ...
    


def LoadDialog(type: int, title: str, flags: int, force_suffix: str, def_path: str, def_file: str) -> str:
    """    
    Open a load dialog. The look of this dialog depends on the operating system.
    
    .. image:: /_imgs/modules/storage/storage_load.png
    :align: center
    
    .. warning::
    
    If the filename returned by :func:`LoadDialog` will be passed to a non-Cinema 4D function it must be decoded to an utf-8 object.
    
    .. literalinclude:: /../../doc.python.code/c4d/storage/loaddialog.py
    :language: python
    
    :type type: int
    :param type: One of the following flags:
    
    .. include:: /consts/FILESELECTTYPE.rst
    :start-line: 3
    
    :type title: str
    :param title: The title.
    :type flags: int
    :param flags: The flags:
    
    .. include:: /consts/FILESELECT.rst
    :start-line: 3
    
    :type force_suffix: str
    :param force_suffix: Currently not used.
    :type def_path: str
    :param def_path: The default path on popup.
    :type def_file: str
    :param def_file:
    
    .. versionadded:: R18.057
    
    The default file on popup.
    
    :rtype: str
    :return: The selected path.
    
    
    """
    ...

def SaveDialog(type: int, title: str = ..., force_suffix: str = ..., def_path: str = ..., def_file: str = ...) -> str:
    """    
    Open a save dialog. The look of this dialog depends on the operating system.
    
    .. image:: /_imgs/modules/storage/storage_save.png
    :align: center
    
    :type type: int
    :param type: One of the following flags:
    
    .. include:: /consts/FILESELECTTYPE.rst
    :start-line: 3
    
    :type title: str
    :param title: The title.
    :type force_suffix: str
    :param force_suffix: The suffix.
    :type def_path: str
    :param def_path: The default path on popup.
    :type def_file: str
    :param def_file:
    
    .. versionadded:: R18.057
    
    The default file on popup.
    
    :rtype: str
    :return: The selected path.
    
    
    """
    ...

def ShowInFinder(path: str, open: bool) -> bool:
    """    
    Show the file/path in the Finder (OSX) or Explorer (Windows).
    
    :type path: str
    :param path: The file/path to show.
    :type open: bool
    :param open: If True the file will be opened by the assigned application.
    :rtype: bool
    :return: **True** if the path/file exists, otherwise **False**.
    
    
    """
    ...

def GeGetPluginPath() -> str:
    """    
    Retrieve the path of the current module.
    
    .. warning::
    
    The Python implementation is different from the C++.
    In the Python SDK, this function returns the path of the Python SDK module. To get the path of your Python plugin use **__file__**.
    
    .. seealso::
    
    :ref:`directory-structure`
    
    :rtype: str
    :return: The path of the Python SDK module.
    
    
    """
    ...

def GeGetC4DPath(whichpath: int) -> str:
    """    
    Gets one of the Cinema 4D paths.
    
    :type whichpath: int
    :param whichpath: The path to get:
    
    .. include:: /consts/C4D_PATH.rst
    :start-line: 3
    
    :rtype: str
    :return: The retrieved path.
    
    
    """
    ...

def GeGetStartupApplication() -> str:
    """    
    Returns the complete path of the host application (Cinema 4D, BODYPAINT 3D, NET) of the plugin:
    
    (Mac) e.g: '/Applications/MAXON/Cinema 4D R21_022/Cinema 4D.app'
    (Windows) e.g: 'C:/Program Files/MAXON/Cinema 4D R21_022/Cinema 4D.exe'
    
    :rtype: str
    :return: The complete path to the host application.
    
    
    """
    ...

def GeGetStartupWritePath() -> str:
    """    
    Returns the **writeable** startup directory. This is the directory where all user data (preferences, libraries etc.) are stored:
    
    (Mac) e.g: '/Users/UserName/Library/Preferences/MAXON/Cinema 4D R12_C333CB6C'
    (Windows) e.g: 'C:/Users/UserName/AppData/Roaming/Maxon/Cinema 4D R21_022_95E9A228'
    
    .. note::
    
    For example to store plugin preferences since modern OS do not allow to write files into the application folder.
    
    :rtype: str
    :return: The **writeable** startup directory.
    
    
    """
    ...

def GeGetMemoryStat() -> BaseContainer:
    """    
    Gets Cinema 4D memory statistics.
    
    :rtype: c4d.BaseContainer
    :return: Can be **None** if receiving memory container failed. Assigned statistics:
    
    .. include:: /consts/C4D_MEMORY_STAT.rst
    :start-line: 3
    
    
    """
    ...

def GeMemGetFreePhysicalMemoryEstimate() -> int:
    """    
    Get the estimated free physical memory.
    
    :rtype: long
    :return: The estiumated free physical memory.
    
    
    """
    ...

def WriteHyperFile(doc: BaseDocument, node: GeListNode, filename: Union[str, MemoryFileStruct], ident: int) -> int:
    """    
    Writes a single list node to disk as a hyper file.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document of the node.
    :type node: c4d.GeListNode
    :param node: The node to write.
    :type filename: Union[str, c4d.storage.MemoryFileStruct]
    :param filename: A file to write to.
    :type ident: long
    :param ident: A unique file identification, to make sure that you only read your own files.
    :rtype: int
    :return: The result:
    
    .. include:: /consts/FILEERROR.rst
    :start-line: 3
    
    
    """
    ...

def ReadHyperFile(doc: BaseDocument, node: GeListNode, filename: Union[str, MemoryFileStruct], ident: int) -> int:
    """    
    Reads a single list node from a hyper file on disk. The read data replaces the data in *node*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document of the node.
    :type node: c4d.GeListNode
    :param node: The node to read to.
    :type filename: Union[str, c4d.storage.MemoryFileStruct]
    :param filename: A file to read from.
    :type ident: long
    :param ident: A unique file identification, to make sure that you only read your own files.
    :rtype: int
    :return: The result:
    
    .. include:: /consts/FILEERROR.rst
    :start-line: 3
    
    
    """
    ...

def GeGetStartupPath() -> str:
    """    
    Get the path for the main folder Cinema 4D:
    
    (Mac) e.g: '/Applications/MAXON/Cinema 4D R12'
    (Windows) e.g: 'C:/Program Files/MAXON/Cinema 4D R21_022'
    
    :rtype: str
    :return: The main path for the Cinema 4D application.
    
    
    """
    ...

def GetUserSiteSpecificPath() -> str:
    """    
    Get the path to the site folder in the user folder.
    
    (Windows 64-bits) e.g: 'C:/Users/$UserName/AppData/Roaming/MAXON/R15/library/python/packages/win64'
    
    .. versionadded:: R15.037
    
    .. note::
    
    This folder exists so that 3rd party packages can be installed in it.
    
    :rtype: str
    :return: The path to the site folder in the user folder.
    
    
    """
    ...

def GetFreeVolumeSpace(drive: str) -> Tuple[int, int]:
    """    
    Calculate the free space on a volume.
    
    .. versionadded:: R16.021
    
    :type drive: str
    :param drive: Can point to a volume or directory.
    :rtype: tuple(long, long)
    :return: The number of available bytes on the volume and the total size of the volume in bytes.
    
    
    """
    ...

def GeExecuteProgram(app: str, path: str) -> bool:
    """    
    Executes an application.
    
    .. note:: The application is started asynchronously.
    
    :type app: str
    :param app: The name of the application to execute.
    :type path: str
    :param path: The name of a file to open using the application.
    :rtype: bool
    :return: **True** if the application was executed, otherwise **False**.
    
    
    """
    ...

def GeExecuteFile(path: str) -> bool:
    """    
    Executes a file.
    
    .. note::
    
    Opens a file as if the user double-clicked it: the default application for this file will open.
    
    :type path: str
    :param path: The name of the application to execute.
    :rtype: bool
    :return: **True** if the application was executed, otherwise **False**.
    
    
    """
    ...

def GeGetMovieInfo(path: Union[str, MemoryFileStruct]) -> None:
    """    
    Get information from a movie file.
    
    :type path: Union[str, c4d.storage.MemoryFileStruct]
    :param path: The path of the movie file.
    :rtype: dict{**frames**: int, **fps**: float}
    :return: The number of frames and frames per second.
    
    
    """
    ...

def GeIdentifyFile(name: Union[str, MemoryFileStruct], probe: Any, recognition: int) -> None:
    """    
    Identify the file in name.
    
    :type name: Union[str, c4d.storage.MemoryFileStruct]
    :param name: The file to check.
    :type probe: buffer
    :param probe: The start of a small chunk of data from the start of the file for testing this file type. Usually the probe size is 1024 bytes.
    :type recognition: int
    :param recognition: Identification flags:
    
    .. include:: /consts/IDENTIFYFILE.rst
    :start-line: 3
    
    :rtype: tuple(int, :class:`BasePlugin <c4d.plugins.BasePlugin>`)
    :return: The result and, for image formats, the image loader that was identified.
    
    .. include:: /consts/IDENTIFYFILE.rst
    :start-line: 3
    
    
    """
    ...

