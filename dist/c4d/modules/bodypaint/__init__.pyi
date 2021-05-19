from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseSelect, BaseContainer, Vector, CPolygon, BaseObject, BaseList2D
from c4d.bitmaps import ColorProfile, BaseBitmap
from c4d.documents import BaseDocument
from c4d.storage import ByteSeq


class TempUVHandle(object):
    def GetMode(self) -> int:
        """    
        Retrieves the current UV editor mode.
        
        :rtype: int
        :return: The UV editor mode:
        
        .. include:: /consts/MEditorModes.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetPoints(self) -> None:
        """    
        Retrieves the read-only points array.
        
        :rtype: list of :class:`c4d.Vector`
        :return: The points.
        
        
        """
        ...
    
    def GetPolys(self) -> None:
        """    
        Retrieves the read-only polygons array.
        
        :rtype: list of :class:`c4d.CPolygon`
        :return: The polygons.
        
        
        """
        ...
    
    def GetPolySel(self) -> None:
        """    
        Retrieves the selected polygons.
        
        :rtype: :class:`c4d.BaseSelect`
        :return: The polygons selection.
        
        
        """
        ...
    
    def GetPolyHid(self) -> None:
        """    
        Retrieves the hidden polygons.
        
        :rtype: :class:`c4d.BaseSelect`
        :return: The hidden polygons selection.
        
        
        """
        ...
    
    def GetUVPointSel(self) -> None:
        """    
        Retrieves the selected UV points.
        
        .. note::
        
        The points are indexed by `4` * `polygon` + `point` where `polygon` is the polygon index and `point` is the point index between `0` and `3`.
        
        :rtype: :class:`c4d.BaseSelect`
        :return: The hidden polygons selection.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Retrieves the point count.
        
        :rtype: int
        :return: The point count.
        
        
        """
        ...
    
    def GetPolyCount(self) -> int:
        """    
        Retrieves the polygon count.
        
        :rtype: int
        :return: The polygon count.
        
        
        """
        ...
    
    def GetBaseObject(self) -> None:
        """    
        Retrieves the object of the UV set.
        
        :rtype: :class:`c4d.BaseObject`
        :return: The object of the UV set.
        
        
        """
        ...
    
    def IsEditable(self) -> None:
        """    
        | Checks if UVs are editable or not.
        | Polygon objects have editable UVs, object generators usually not.
        
        :rtype: :class:`c4d.BaseObject`
        :return: The object of the UV set.
        
        
        """
        ...
    
    def GetUVW(self) -> List[Dict[str, Any]]:
        """    
        Retrieves the UV list.
        
        :rtype: list of dict('a','b','c','d')
        :return: The UV list.
        
        
        """
        ...
    
    def SetUVW(self, uvw: List[Dict[str, Any]]) -> bool:
        """    
        Applies changes of the UV set to the object.
        
        :type uvw: list of dict('a','b','c','d')
        :param uvw: The UV list to set.
        :rtype: bool
        :returns: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetUVWFromTextureView(self, uvw: List[Dict[str, Any]], ignoreHidden: bool, ignoreUnselected: bool, autoSelectAll: bool, registerUndo: bool) -> bool:
        """    
        Applies changes of the UV set to the object.
        
        :type uvw: list of dict('a','b','c','d')
        :param uvw: The UV list to set.
        :type ignoreHidden: bool
        :param ignoreHidden: If **True**, do not affect the UV coordinates of UV Polygons or UV Points of hidden polygons.
        :type ignoreUnselected: bool
        :param ignoreUnselected: If **True**, do not affect the UV coordinates of UV Polygons, or UV Points (depending on the current mode) that are unselected in the Texture View.
        :type autoSelectAll: bool
        :param autoSelectAll: If **True**, automatically selects all UV Polygons, or UV Points (depending on the current mode).
        :type registerUndo: bool
        :param registerUndo: If **True**, an undo is added for the operation.
        :rtype: bool
        :returns: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetUVPointSelectionFromTextureView(self, uvPointSelection: BaseSelect, bleedSelection: bool) -> bool:
        """    
        | Sets the UV Point selection.
        | The points have to be indexed as follows: <tt>4 * polygon + point</tt> where **c** polygon is the polygon index and **c** point is the point index between **0 and 3** (a, b, c, d).
        
        .. versionadded:: S22
        
        :param uvPointSelection: The Point BaseSelect that will be defined from the UV Point selection.
        :type uvPointSelection: c4d.BaseSelect
        :param bleedSelection:
        
        | If **True,** ensures that if one UV point is selected, all UV points having the same coordinates are selected as well.
        | If false it doesn't check, which is faster.
        
        :type bleedSelection: bool
        :return: **True** if successful, otherwise **False**.
        :rtype: bool
        
        
        """
        ...
    

class PaintBitmap(BaseList2D):
    def GetBw(self) -> int:
        """    
        Get the width of the paint bitmap.
        
        :rtype: int
        :return: The width of the paint bitmap.
        
        
        """
        ...
    
    def GetBh(self) -> int:
        """    
        Get the height of the paint bitmap.
        
        :rtype: int
        :return: The height of the paint bitmap.
        
        
        """
        ...
    
    def GetPaintTexture(self) -> PaintTexture:
        """    
        Get the paint texture if possible.
        
        :rtype: c4d.modules.bodypaint.PaintTexture
        :return: The paint texture if possible, otherwise **None**.
        
        
        """
        ...
    
    def GetParent(self) -> PaintBitmap:
        """    
        Get the parent.
        
        .. note::
        
        This can be a layer or a texture for instance.
        
        :rtype: c4d.modules.bodypaint.PaintBitmap
        :return: The paint texture if possible, otherwise **None**.
        
        
        """
        ...
    
    def GetLayerDownFirst(self) -> PaintLayer:
        """    
        Get the first alpha channel layer.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The first alpha channel layer, or **None** if there is none.
        
        
        """
        ...
    
    def GetLayerDownLast(self) -> PaintLayer:
        """    
        Get the last child layer.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The last child layer, or **None** if there is none.
        
        
        """
        ...
    
    def GetAlphaFirst(self) -> PaintLayer:
        """    
        Get the first alpha channel layer.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The first alpha channel layer, or **None** if there is none.
        
        
        """
        ...
    
    def GetAlphaLast(self) -> PaintLayer:
        """    
        Get the last alpha channel layer.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The last alpha channel layer, or **None** if there is none.
        
        
        """
        ...
    
    def AddAlphaChannel(self, bitdepth: int, prev: Optional[PaintLayer] = ..., undo: Optional[bool] = ..., activate: Optional[bool] = ...) -> PaintLayerBmp:
        """    
        Add an alpha channel to the layer.
        
        :type bitdepth: int
        :param bitdepth: The bit depth of the alpha channel:
        
        .. include:: /consts/BITDEPTH.rst
        :start-line: 3
        
        :type prev: c4d.modules.bodypaint.PaintLayer
        :param prev: Optional point to insert the alpha channel.
        :type undo: bool
        :param undo: **True** to create an undo on the undo stack, otherwise **False**.
        :type activate: bool
        :param activate: If **True** alpha channel will be activated.
        
        :rtype: c4d.modules.bodypaint.PaintLayerBmp
        :return: The added alpha channel, or **None** if it failed.
        
        
        """
        ...
    
    def AskApplyAlphaMask(self) -> bool:
        """    
        Check if an alpha mask can be applied.
        
        :rtype: bool
        :return: **True** if an alpha mask can be applied, otherwise **False**.
        
        
        """
        ...
    
    def UpdateRefresh(self, xmin: int, ymin: int, xmax: int, ymax: int, flags: int) -> None:
        """    
        Refresh an area of the paint bitmap.
        
        .. note::
        
        Must be done after modifying the paint bitmap.
        
        :type xmin: int
        :param xmin: Left coordinate of the refreshed area.
        :type ymin: int
        :param ymin: Top coordinate of the refreshed area.
        :type xmax: int
        :param xmax: Right coordinate of the refreshed area.
        :type ymax: int
        :param ymax: Bottom coordinate of the refreshed area.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/UPDATE.rst
        :start-line: 3
        
        
        """
        ...
    
    def UpdateRefreshAll(self, flags: int, reallyall: bool) -> None:
        """    
        Refresh the complete paint bitmap. Has to be done after modifying the paint bitmap.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/UPDATE.rst
        :start-line: 3
        
        :type reallyall: bool
        :param reallyall:
        
        | If **True** an infinite bounding box is used for the refresh.
        | If **False** the bounding box of the layer is used, this is much faster.
        
        
        """
        ...
    
    def GetColorMode(self) -> int:
        """    
        Get the color mode of the paint bitmap.
        
        :rtype: int
        :return: The color mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetDirty(self, flags: int) -> int:
        """    
        Get dirty count.
        
        :type flags: int
        :param flags: Reserved, must be 0.
        :rtype: int
        :return: Dirty count, incremented when the paint bitmap changes.
        
        
        """
        ...
    

class PaintTexture(PaintBitmap):
    def GetFirstLayer(self) -> PaintLayer:
        """    
        Get the first layer of the paint texture.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The first layer of the paint texture, or **None** if there is none.
        
        
        """
        ...
    
    def GetLastLayer(self) -> PaintLayer:
        """    
        Get the last layer of the paint texture.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The last layer of the paint texture, or **None** if there is none.
        
        
        """
        ...
    
    def AddLayerBmp(self, insertafter: PaintLayer, layerset: PaintLayer, mode: int, useundo: bool, activate: bool) -> PaintLayerBmp:
        """    
        Add a bitmap layer.
        
        :type insertafter: c4d.modules.bodypaint.PaintLayer
        :param insertafter: The layer insertion point.
        :type layerset: c4d.modules.bodypaint.PaintLayer
        :param layerset: The parent layer folder.
        :type mode: int
        :param mode: Mode (should be the same as the paint texture):
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type useundo: bool
        :param useundo: **True** to create an undo on the undo stack, otherwise **False**.
        :type activate: bool
        :param activate: **True** to select the layer.
        :rtype: c4d.modules.bodypaint.PaintLayerBmp
        :return: The added bitmap layer.
        
        
        """
        ...
    
    def AddLayerFolder(self, insertafter: PaintLayer, insertunder: PaintLayer, useundo: bool, activate: bool) -> PaintLayerBmp:
        """    
        Add a layer folder.
        
        :type insertafter: c4d.modules.bodypaint.PaintLayer
        :param insertafter: The layer insertion point.
        :type insertunder: c4d.modules.bodypaint.PaintLayer
        :param insertunder: Parent layer folder.
        :type useundo: bool
        :param useundo: **True** to create an undo on the undo stack, otherwise **False**.
        :type activate: bool
        :param activate: **True** to select the layer.
        :rtype: c4d.modules.bodypaint.PaintLayerBmp
        :return: The added layer folder.
        
        
        """
        ...
    
    def SetActiveLayer(self, layer: PaintLayer, activatetexture: bool, show: bool) -> None:
        """    
        Select a layer.
        
        :type layer: c4d.modules.bodypaint.PaintLayer
        :param layer: The layer to select.
        :type activatetexture: bool
        :param activatetexture: Select the texture.
        :type show: True
        :param show: Show the texture.
        
        
        """
        ...
    
    def GetActive(self) -> PaintLayer:
        """    
        Get the selected layer, or **None** if there is none.
        
        :rtype: c4d.modules.bodypaint.PaintLayer
        :return: The selected layer.
        
        
        """
        ...
    
    def GetLinkLayers(self, addfolders: bool) -> None:
        """    
        Get linked layers.
        
        :type addfolders: bool
        :param addfolders: If **True** the layer hierarchy is taken into account (see layer folders), otherwise **False**.
        :rtype: list of :class:`PaintLayer <c4d.modules.bodypaint.PaintLayer>`
        :return: The list containing the linked layers.
        
        
        """
        ...
    
    def SetColorMode(self, newcolormode: int, doundo: bool) -> None:
        """    
        Change the color mode of the paint texture.
        
        :type newcolormode: int
        :param newcolormode: The new color mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type doundo: bool
        :param doundo: **True** to create an undo for changing the color mode, otherwise **False**.
        
        
        """
        ...
    
    def GetFilename(self) -> str:
        """    
        Get the filename of the paint texture.
        
        :rtype: str
        :return: The filename of the paint texture.
        
        
        """
        ...
    
    def GetLayerCount(self) -> int:
        """    
        Get the number of layers of the paint texture.
        
        :rtype: int
        :return: The number of layers.
        
        
        """
        ...
    
    def GetAlphaCount(self) -> int:
        """    
        Get the number of alpha channels of the paint texture.
        
        :rtype: int
        :return: The number of alpha channels.
        
        
        """
        ...
    
    def SetColorProfile(self, profile: ColorProfile) -> bool:
        """    
        Sets the color profile for the paint texture.
        
        .. versionadded:: R17.048
        
        :type profile: c4d.bitmaps.ColorProfile
        :param profile: The color profile to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetColorProfile(self) -> ColorProfile:
        """    
        Gets the color profile for the paint texture.
        
        .. versionadded:: R17.048
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The color profile.
        
        
        """
        ...
    
    @staticmethod
    def CreateNewTexture(path: str, settings: BaseContainer) -> PaintTexture:
        """    
        Creates a new paint texture.
        
        :type path: str
        :param path: The filename for the paint texture.
        :type settings: c4d.BaseContainer
        :param settings: The settings for the texture creation:
        
        .. include:: /consts/TEXTURE.rst
        :start-line: 3
        
        :rtype: c4d.modules.bodypaint.PaintTexture
        :return: The created paint texture if successful, otherwise **None**.
        
        
        """
        ...
    
    @staticmethod
    def GetTextureDefaults(channel: Any) -> BaseContainer:
        """    
        Gets the default texture settings for the passed material *channel* ID.
        
        :type path: int
        :param path: The material channel ID:
        
        .. include:: /consts/CHANNEL.rst
        :start-line: 3
        
        :rtype: c4d.BaseContainer
        :return: The default texture settings:
        
        .. include:: /consts/TEXTURE.rst
        :start-line: 3
        
        
        """
        ...
    
    @staticmethod
    def SetSelected_Texture(bmp: PaintBitmap, preferred: PaintMaterial) -> bool:
        """    
        Selects a paint texture.
        
        :type bmp: c4d.modules.bodypaint.PaintBitmap
        :param bmp: The paint texture to select.
        :type preferred: c4d.modules.bodypaint.PaintMaterial
        :param preferred: The prefered paint material, usually **None**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def GetSelectedTexture() -> PaintTexture:
        """    
        Gets the selected paint texture.
        
        :rtype: c4d.modules.bodypaint.PaintTexture
        :return: The selected paint texture or **None** if no paint is selected.
        
        
        """
        ...
    

class PaintMaterial(PaintBitmap):
    def EnableMaterial(self, doc: BaseDocument, on: bool, suppressevent: bool, domaterialundo: bool) -> None:
        """    
        Enable material for painting.
        
        :type doc: c4d.documents.BaseDocument
        :param: The document the material belongs to.
        :type on: bool
        :param on: RUE to enable the material for painting, **False** to disable it.
        :type suppressevent: bool
        :param suppressevent: Private.
        :type domaterialundo: bool
        :param domaterialundo: If **True** an undo is created on the undo stack.
        
        
        """
        ...
    

class PaintLayer(PaintBitmap):
    def GetShowBit(self, hierarchy: bool, bit: int) -> bool:
        """    
        Get the visibility of the layer.
        
        :type hierarchy: bool
        :param hierarchy: If **True** the visiblity of the parents is taken into account (think of layer sets).
        :type bit: int
        :param bit: Must be set to 0.
        :rtype: bool
        :return: **True** if visible, otherwise **False**.
        
        
        """
        ...
    
    def SetShowBit(self, onoff: bool, bit: int) -> bool:
        """    
        Set the visibility of the layer.
        
        :type onoff: bool
        :param onoff: **True** if visible, otherwise **False**.
        :type bit: int
        :param bit: Must be set to 0.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ToPaintLayerBmp(self) -> PaintLayerBmp:
        """    
        Casts the PaintLayer to a PaintLayerBmp.
        
        .. versionadded:: R16.021
        
        :rtype: c4d.modules.bodypaint.PaintLayerBmp
        :return: The :class:`PaintLayer <c4d.modules.bodypaint.PaintLayer>` casted to a :class:`PaintLayerBmp <c4d.modules.bodypaint.PaintLayerBmp>`.
        
        
        """
        ...
    

class PaintLayerMask(PaintLayer):
    ...

class PaintLayerFolder(PaintLayer):
    ...

class PaintLayerBmp(PaintLayer):
    def ImportFromBaseBitmap(self, bmp: Any, usealpha: bool) -> bool:
        """    
        Fill the layer bitmap with an imported bitmap.
        
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The bitmap to import.
        :type usealpha: bool
        :param usealpha: If **True** the alpha channel of the bitmap is used, otherwise **False**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ImportFromBaseBitmapAlpha(self, bmp: Any, channel: BaseBitmap) -> bool:
        """    
        Fill the layer bitmap with an imported bitmap.
        
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The bitmap to import.
        :type channel: c4d.bitmaps.BaseBitmap
        :param channel: The separate alpha channel bitmap to import.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetBoundingBox(self) -> Dict[str, Any]:
        """    
        Get the bounding box of the bitmap layer.
        
        .. code-block:: python
        
        d = layer_bmp.GetBoundingBox()
        d["x1"], d["y1"], d["y1"], d["y2"]
        
        :rtype: dict
        :return: The coordinates.
        
        
        """
        ...
    
    def GetPixelCnt(self, x: int, y: int, cnt: int, buffer: ByteSeq, dstmode: int, flags: int) -> bool:
        """    
        Reads *cnt* pixels from (*x*, *y*) in the bitmap to the *buffer* with mode *dstmode*.
        
        .. versionadded:: R16.021
        
        :type x: int
        :param x: The starting X coordinate.
        :type y: int
        :param y: The starting Y coordinate.
        :type cnt: int
        :param cnt: The number of pixels to get.
        :type buffer: c4d.storage.ByteSeq
        :param buffer: The destination buffer.
        :type dstmode: int
        :param dstmode: The destination color mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/PIXELCNT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetPixelCnt(self, x: int, y: int, cnt: int, buffer: ByteSeq, inc: int, srcmode: int, flags: int) -> bool:
        """    
        Sets *cnt* pixels at (*x*, *y*) in the bitmap from *buffer* with mode *srcmode*, incrementing *inc* bytes for each pixel.
        
        .. versionadded:: R16.021
        
        :type x: int
        :param x: X coordinate of the first pixel to set.
        :type y: int
        :param y: Y coordinate of the first pixel to set.
        :type cnt: int
        :param cnt: Number of pixels to set.
        :type buffer: c4d.storage.ByteSeq
        :param buffer: The source buffer.
        :type inc: int
        :param inc: The byte increment per pixel in the buffer.
        :type srcmode: int
        :param srcmode: The source mode.
        
        .. note::
        
        None of the alpha modes are supported.
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/PIXELCNT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    


def IdentifyImage(texpath: str) -> int:
    """    
    Identifies the image's file format.
    
    :type texpath: str
    :param texpath: The path to the image.
    :rtype: int
    :return: The image's file format:
    
    .. include:: /consts/FILTER.rst
    :start-line: 3
    
    
    """
    ...

def PainterActivateChannel(channel: int, multi: bool, enable: bool) -> None:
    """    
    Activation/deactivation of paint channels.
    
    :type channel: int
    :param channel: The paint channel:
    
    .. include:: /consts/CHANNEL.rst
    :start-line: 3
    
    :type multi: bool
    :param multi: **True** for multi channel painting, **False** for single channel painting.
    :type enable: bool
    :param enable: **True** to activate the paint channel, **False** to deactivate the paint channel.
    
    
    """
    ...

def BPSetupWizardWithParameters(doc: BaseDocument, settings: Any, objects: Any, material: Any) -> bool:
    """    
    .. image:: /_imgs/modules/modules/bodypaint/bodypaint_bnsetupwizard.png
    
    Run the BodyPaint 3D paint wizard.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document
    :type settings:  :class:`BaseContainer <c4d.BaseContainer>`
    :param settings: The container with the settings for the paint wizard:
    
    .. include:: /consts/AMSI.rst
    :start-line: 3
    
    :type objects: any
    :param objects: Any iteratable object, e.g: list, tuple.
    :type material: any
    :param material: Any iteratable object, e.g: list, tuple.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def SendPainterCommand(command: int, doc: Optional[BaseDocument] = ..., tex: Optional[PaintTexture] = ..., bc: Optional[BaseContainer] = ...) -> bool:
    """    
    Sends commands to Bodypaint 3D.
    
    :type command: int
    :param command: Commands:
    
    .. include:: /consts/PAINTER.rst
    :start-line: 3
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The optional document for the operation.
    :type tex: c4d.modules.bodypaint.PaintTexture
    :param tex: The optional paint texture for the operation.
    :type bc: c4d.BaseContainer
    :param bc: The optional container for the operation.
    :rtype: bool
    :return: **True** if the command was successfully sent, otherwise **False**.
    
    If *command* was **PAINTER_LOADTEXTURE** and the texture successfully loaded, it then returns the :class:`PaintTexture <c4d.modules.bodypaint.PaintTexture>`
    
    .. code-block:: python
    
    import c4d
    
    texturename = r'path/to/texture'
    settings = c4d.BaseContainer()
    settings.SetFilename(c4d.LOADTEXTURE_FILENAME, texturename)
    
    tex = c4d.modules.bodypaint.SendPainterCommand(c4d.PAINTER_LOADTEXTURE, doc, None, settings)
    if not tex:
    print tex
    
    
    """
    ...

def GetActiveUVSet(doc: BaseDocument, flags: int) -> TempUVHandle:
    """    
    Retrieves the document's active UV set.
    
    .. versionadded:: R18.011
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document returning the active UV set.
    :type flags: int
    :param flags: The flags:
    
    .. include:: /consts/GETACTIVEUVSET.rst
    :start-line: 3
    
    :rtype: c4d.modules.bodypaint.TempUVHandle
    :return: A temporary handle to the active UV set, or **None** if there is no active UV set. Has to be freed with :func:`FreeActiveUVSet`.
    
    
    """
    ...

def FreeActiveUVSet(handle: TempUVHandle) -> None:
    """    
    Frees the active UV set.
    
    .. versionadded:: R18.011
    
    :type handle: c4d.modules.bodypaint.TempUVHandle
    :param handle: The temporary handle of the UV set to be freed.
    
    
    """
    ...

def UpdateMeshUv(fullUpdate: bool) -> None:
    """    
    Updates the mesh based on the UVW result of interactive unwrapping.
    
    .. versionadded:: S22
    
    :param fullUpdate: **True** to perform a slow full update or **False** for a quicker one which updates only the UV coordinates of the UV Mesh.
    :type fullUpdate: bool
    :return: **True** if successful otherwise **False**.
    
    
    """
    ...

def CallUVCommand(points: List[Vector], pointCount: int, polys: List[CPolygon], polyCount: int, uvw: Dict[str, Any], polySelection: BaseSelect, pointSelection: BaseSelect, op: BaseObject, mode: int, cmdid: int, settings: Optional[BaseContainer] = ...) -> bool:
    """    
    Calls UV commands.
    
    .. versionadded:: R18.011
    
    :type points: List[c4d.Vector]
    :param points: The points array.
    :type pointCount: int
    :param pointCount: The number of points in the *points* array.
    :type polys: List[c4d.CPolygon]
    :param polys: The polygons array.
    :type polyCount: int
    :param polyCount: The number of polygons in the *polys* array.
    :type uvw: Dict[c4d.Vector, c4d.Vector, c4d.Vector, c4d.Vector]
    :param uvw: The UVWs array.
    :type polySelection: c4d.BaseSelect
    :param polySelection: The polygon selection.
    :type pointSelection: c4d.BaseSelect
    :param pointSelection: The UV point selection. The points are indexed by `4` * `polygon` + `point` where `polygon` is the polygon index and `point` is the point index between `0` and `3`.
    :type op: c4d.BaseObject
    :param op: The object of the UV set.
    :type mode: int
    :param mode: The UV editing mode:
    
    .. include:: /consts/MEditorModes.rst
    :start-line: 3
    
    :type cmdid: int
    :param cmdid: The UV command:
    
    .. include:: /consts/UVCOMMAND.rst
    :start-line: 3
    
    :type settings: c4d.BaseContainer
    :param settings: The optional settings for the UV command.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

