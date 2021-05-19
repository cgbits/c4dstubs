from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.documents import BaseDocument
from c4d import BaseList2D, Material, BaseMaterial


def ImportSubstance(doc: BaseDocument, fn: str, copyFile: int, errPopup: bool, addUndo: bool, createMaterial: bool) -> None:
    """    
    Imports a Substance asset file (.sbsar) into *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to import into.
    :type fn: str
    :param fn: The Substance asset file.
    :type copyFile: int
    :param copyFile: The copy file flag:
    
    .. include:: /consts/SUBSTANCE_IMPORT_COPY.rst
    :start-line: 3
    
    | If set to *ASK*, user's choice will be returned.
    | Note: When set to *ASK*, the function obviously has to be called in a context where user interaction is allowed.
    
    :type errPopup: bool
    :param errPopup:
    
    | If set to **True**, problems will be communicated to the user with a message requester.
    | Note: When set to **True**, the function obviously has to be called in a context where user interaction is allowed.
    
    :type addUndo: bool
    :param addUndo: If set to **True**, an undo step will be added for the import. Caller has to care for the surrounding :meth:`BaseDocument.StartUndo` and :meth:`BaseDocument.EndUndo` calls.
    :type createMaterial: bool
    :param createMaterial: Set to **True**, to have a material created based on the configuration in preferences. Set to **False**, to suppress any creation of materials.
    :rtype: tuple(int, :class:`c4d.BaseList2D`, int)
    :return: A tuple with the following information:
    
    | int: The result for the import:
    
    .. include:: /consts/SUBSTANCE_IMPORT_RESULT.rst
    :start-line: 3
    
    | :class:`c4d.BaseList2D`: The imported Substance asset.
    | int: User's choice if *copyFile* was *ASK*. Otherwise same as passed to *copyFile*.
    
    
    """
    ...

def CreateMaterial(asset: BaseList2D, graphIndex: int, mode: int) -> None:
    """    
    Creates a Cinema 4D standard material from *asset*.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :type graphIndex: int
    :param graphIndex: The index of the graph to use (for multi-graph Substances).
    :type mode: int
    :param mode: The material creation mode
    
    .. include:: /consts/SUBSTANCE_MATERIAL_MODE.rst
    :start-line: 3
    
    :rtype: :class:`c4d.BaseMaterial`
    :return: The created material.
    
    
    """
    ...

def CreateSubstanceShader(asset: BaseList2D) -> None:
    """    
    Creates a Substance shader linked to *asset*.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset. Can be **None** (since R18.039).
    :rtype: :class:`c4d.BaseShader`
    :return: The created Substance shader.
    
    
    """
    ...

def AssignChannelToMaterial(asset: BaseList2D, mat: Material, channelId: int, outputUid: int, addUndo: bool) -> bool:
    """    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset. Needs to be part of the document.
    :type mat: c4d.Material
    :param mat: The material.
    :type channelId: int
    :param channelId: The channel ID:
    
    .. include:: /consts/CHANNEL.rst
    :start-line: 3
    
    :type outputUid: int
    :param outputUid: The unique ID of the Substance output to use.
    :type addUndo: bool
    :param addUndo: If set to **True**, an undo step will be added for the import. Caller has to care for the surrounding :meth:`BaseDocument.StartUndo` and :meth:`BaseDocument.EndUndo` calls.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GetFirstSubstance(doc: BaseDocument) -> None:
    """    
    Retrieves the first Substance asset in *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: :class:`c4d.BaseList2D`
    :return: The first Substance asset, or **None** if none exists.
    
    
    """
    ...

def GetSubstances(doc: BaseDocument, onlySelected: bool) -> None:
    """    
    Retrieves all (or only selected) Substance assets in *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type onlySelected: bool
    :param onlySelected: Set to **True** to get only selected Substance assets.
    :rtype: list of :class:`c4d.C4DAtom`
    :return: The retrieved Substance assets.
    
    
    """
    ...

def InsertLastSubstance(doc: BaseDocument, asset: BaseList2D) -> bool:
    """    
    Inserts *asset* into *doc* as last element.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GetSubstanceGraph(asset: BaseList2D, prevGraph: Any) -> Tuple[Any, str]:
    """    
    Retrieves the Substance graph. This function may be used to iterate over the graphs of *asset*.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :type prevGraph: PyCObject
    :param prevGraph: Pass **None** (default) to get the first graph, pass a graph object to get the following graph.
    :rtype: tuple(PyCObject, str)
    :return: The Substance graph and its name.
    
    
    """
    ...

def GetSubstanceInput(asset: BaseList2D, graph: Any, prevInput: Any) -> Tuple[Any, int, int, int, int, str]:
    """    
    Retrieves the Substance input of an asset. This function may be used to iterate over the inputs of *graph* for *asset*.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :type graph: PyCObject
    :param graph: The graph.
    :type prevInput: PyCObject
    :param prevInput: Pass **None** (default) to get the first input, pass an input object to get the following input.
    :rtype: tuple(PyCObject, int, int, int, int, str)
    :return: A tuple with the following information:
    
    |
    | The Substance input, or **None** if input is not available.
    | The unique ID of the input. Only valid if the function does not return **None**.
    | The ID of the first component of the input parameter in Cinema 4D. This ID can be used to create a :class:`c4d.DescID` for :meth:`C4DAtom.SetParameter`. Only valid if the function does not return **None**.
    | The number of description elements used in Cinema 4D to represent the Substance input parameter. Only valid if the function does not return **None**.
    | The data type of the input. Only valid if the function does not return **None**.
    
    .. include:: /consts/SUBSTANCE_INPUT_TYPE.rst
    :start-line: 3
    
    | Name of the returned input. Only valid if the function does not return **None** as Substance input.
    
    
    """
    ...

def GetSubstanceOutput(asset: BaseList2D, graph: Any, getBitmap: bool, prevOutput: Any) -> None:
    """    
    Retrieves the Substance output of an asset. This function may be used to iterate over the outputs of *graph* for *asset*.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :type graph: PyCObject
    :param graph: The graph.
    :type getBitmap: bool
    :param getBitmap: Set to **True**, to get a clone of the output channel bitmap.
    :type prevOutput: PyCObject
    :param prevOutput: Pass **None** (default) to get the first output, pass an output object to get the following output.
    :rtype: tuple(PyCObject, int, int, str, :class:`c4d.bitmaps.BaseBitmap`)
    :return: A tuple with the following information:
    
    |
    | The Substance output, or **None** if output is not available.
    | The unique ID of the output. Only valid if the function does not return **None**.
    | The output type ID. Only valid if the function does not return **None** as Substance output.
    
    .. include:: /consts/SUBSTANCE_OUTPUT_TYPE.rst
    :start-line: 3
    
    | The name of the returned output. Only valid if the function does not return **None**.
    | The clone of the output channel bitmap. Only valid if the function does not return **None** and *getBitmap* was passed **True**.
    
    
    """
    ...

def PrefsGetMaterialModeSetting() -> int:
    """    
    Convenience function to get the material creation mode set in Substance preferences.
    
    :rtype: int
    :return: The material creation mode:
    
    .. include:: /consts/SUBSTANCE_MATERIAL_MODE.rst
    :start-line: 3
    
    
    """
    ...

def PrefsGetPreviewSetting() -> int:
    """    
    Convenience function to get the preview mode for Content Browser set in Substance preferences.
    
    :rtype: int
    :return: `0` for mosaic preview, otherwise rendered preview scene.
    
    
    """
    ...

def MaterialUsesSubstance(mat: BaseMaterial) -> bool:
    """    
    Checks if *mat* contains any Substance shaders.
    
    :type mat: c4d.BaseMaterial
    :param mat: The material to check for Substance shaders.
    :rtype: bool
    :return: **True** if the material uses a Substance shader, otherwise **False**.
    
    
    """
    ...

def GetSubstanceMosaicPreview(asset: BaseList2D, w: int, h: int) -> None:
    """    
    Returns an image with previews of the output channels of *asset*.
    
    .. note::
    
    While the Substance asset won't have to be re-rendered, this operation still involves downscaling of all Substance outputs.
    
    :type asset: c4d.BaseList2D
    :param asset: The Substance asset.
    :type w: int
    :param w: The width of the preview image.
    :type h: int
    :param h: The height of the preview image.
    :rtype: :class:`c4d.bitmaps.BaseBitmap`
    :return: The resulting preview bitmap.
    
    
    """
    ...

