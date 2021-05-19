from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.storage import MemoryFileStruct, ByteSeq
from c4d import BaseContainer, Vector
from c4d.modules.bodypaint import PaintBitmap


class MovieSaver(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.bitmaps.MovieSaver
        :return: The new movie saver
        
        
        """
        ...
    
    def Open(self, name: Union[str, MemoryFileStruct], bm: BaseBitmap, fps: int, format: int, data: BaseContainer, savebits: int) -> None:
        """    
        | Opens a movie stream to the file *name*.
        | The resolution and bit depth are defined by the first frame in *bm*.
        | The framerate is specified by *fps*.
        
        :type name: Union[str, c4d.storage.MemoryFileStruct]
        :param name: A file.
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: A typical frame of the movie, used for dimensions.
        :type fps: int
        :param fps: The frame rate in frames per second
        :type format: int
        :param format: The file format. Valid values are either *FILTER_AVI* or *FILTER_MOVIE*.
        :type data: c4d.BaseContainer
        :param data: Additional settings for the file format.
        
        (Please see the documentation for the AVI and Quicktime formats for more information.)
        
        .. include:: /consts/AVISAVER.rst
        :start-line: 3
        
        .. include:: /consts/QTSAVER.rst
        :start-line: 3
        
        :type savebits: int
        :param savebits: Can be a combination of the following flags:
        
        .. include:: /consts/SAVEBIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def Close(self) -> None:
        """    
        Close the movie file.
        
        
        """
        ...
    
    def Write(self, bm: BaseBitmap) -> int:
        """    
        Adds another frame to the end of the movie stream.
        
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The frame to add
        :rtype: int
        :return: The result. Possible values are:
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def Choose(self, format: int, bc: BaseContainer) -> None:
        """    
        Opens the standard compression chooser for movie formats.
        
        .. note::
        
        The arguments might change in the future.
        
        The new settings are stored in **bc** if the user clicks ok.
        
        .. code-block:: python
        
        data = c4d.BaseContainer()
        action = ms.Choose(c4d.FILTER_AVI, data)
        if action==False: return #is True if the user canceled the dialog
        
        ms.Open(..., data, ...)
        
        :type format: int
        :param format: The file format. Valid values are either *FILTER_AVI* or *FILTER_MOVIE*.
        :type bc: c4d.BaseContainer
        :param bc: Used to pass the default settings, and to read the settings the user has chosen.
        
        
        """
        ...
    

class MovieLoader(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.bitmaps.MovieLoader
        :return: The new movie loader
        
        
        """
        ...
    
    def Open(self, fn: Union[str, MemoryFileStruct]) -> None:
        """    
        Open a movie file.
        
        :type fn: Union[str, c4d.storage.MemoryFileStruct]
        :param fn: The file.
        
        
        """
        ...
    
    def Close(self) -> None:
        """    
        Close the movie file.
        
        
        """
        ...
    
    def GetInfo(self) -> Tuple[int, float]:
        """    
        Return information about the movie.
        
        .. code-block:: python
        
        framecount, fps = ml.GetInfo()
        
        :rtype: tuple(int, float)
        :return: Frame and FPS
        
        
        """
        ...
    
    def Read(self, new_frame_idx: int) -> None:
        """    
        Read an image from the movie.
        
        .. code-block:: python
        
        framecount, fps = ml.GetInfo()
        for frame in xrange(framecount):
        result, image = ml.Read(frame)
        #when result is not IMAGERESULT_OK...
        #...image is None.
        if result != c4d.IMAGERESULT_OK:
        break
        
        pass
        
        :type new_frame_idx: int
        :param new_frame_idx: The frame number of the frame to be read.
        :rtype: tuple(:doc:`IMAGERESULT </consts/IMAGERESULT>`, :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>`)
        :return: The image result and the bitmap or **None**.
        
        
        """
        ...
    

class GeClipMap(object):
    def __init__(self) -> None:
        """    
        Creates a new instance of :class:`GeClipMap <c4d.bitmaps.GeClipMap>`.
        
        :rtype: c4d.bitmaps.GeClipMap
        :return: The new clipmap.
        
        
        """
        ...
    
    def Init(self, w: int, h: int, bits: int) -> bool:
        """    
        Initializes the clip map bitmap to the given dimensions and depth. Any previous data is lost.
        
        :type w: int
        :param w: Width
        :type h: int
        :param h: height
        :type bits: int
        :param bits: 32
        :rtype: bool
        :return: **True** if the initialization was successful.
        
        
        """
        ...
    
    def InitWith(self, name: Union[str, MemoryFileStruct], frame: int) -> Tuple[int, bool]:
        """    
        Loads the clip map bitmap from the file specified by *name*.
        
        .. note::
        
        | The file can be either a movie or a picture.
        | The file format is automatically detected.
        | Any previous data is lost.
        
        .. code-block:: python
        
        result, isMovie = clmap.InitWith(path)
        if result == c4d.IMAGERESULT_OK: #int check
        # picture loaded
        if isMovie: #bool check
        pass # file is a movie
        else:
        pass # file is no movie
        
        :type name: Union[str, c4d.storage.MemoryFileStruct]
        :param name: The path to the image.
        :type frame: int
        :param frame: The frame number to load in a movie.
        :rtype: tuple(int, bool)
        :return: The image result and a boolean value if the file is a movie.
        
        
        """
        ...
    
    def InitWithBitmap(self, bm: BaseBitmap, alpha_channel: BaseBitmap) -> bool:
        """    
        | Loads the clip map bitmap from *bm*.
        | Any previous data is lost.
        
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The bitmap to initalize the clip map with.
        :type alpha_channel: c4d.bitmaps.BaseBitmap
        :param alpha_channel: The alpha channel to use in *bm*.
        :rtype: bool
        :return: **True** if the clip map was initialized, otherwise **False**.
        
        
        """
        ...
    
    def Destroy(self) -> None:
        """    
        Resets the clip map to its initial state and frees allocated memory.
        
        .. warning::
        
        Requires a new call to :meth:`Init` before the clip map can be used again.
        
        
        """
        ...
    
    def GetBitmap(self) -> BaseBitmap:
        """    
        Returns the internal bitmap object.
        
        .. warning::
        
        The clip map alpha channel won't be encoded in this bitmap. This is a limitation.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The bitmap.
        
        
        """
        ...
    
    def BeginDraw(self) -> None:
        """    
        Must be called before any drawing commands.
        
        .. note::
        
        After you call a sequence of drawing commands you should call :meth:`GeClipMap.EndDraw`.
        
        
        """
        ...
    
    def EndDraw(self) -> None:
        """    
        Must be called after any drawing commands.
        
        .. note::
        
        Before you call a sequence of drawing commands you should call :meth:`GeClipMap.BeginDraw`.
        
        
        """
        ...
    
    def GetDim(self) -> Tuple[int, int]:
        """    
        Retrieves the pixel dimensions of the clip map.
        
        .. code-block:: python
        
        w, h = clmap.GetDim()
        
        :rtype: tuple of int
        :return: The width and height dimensions of the clip map.
        
        
        """
        ...
    
    def GetBw(self) -> int:
        """    
        Retrieves the pixel width of the clip map.
        
        :rtype: int
        :return: The width.
        
        
        """
        ...
    
    def GetBh(self) -> int:
        """    
        Retrieves the pixel height of the clip map.
        
        :rtype: int
        :return: The height.
        
        
        """
        ...
    
    def Blit(self, dx: int, dy: int, s_dp: GeClipMap, sx1: int, sy1: int, sx2: int, sy2: int, rop: int) -> None:
        """    
        Blits from *s_dp* to this clip map. The region (*sx1*, *sy1*) to (*sx2*, *sy2*) from the source will be copied into the region with the top left corner at (*dx*, *dy*) in the destination.
        
        Additionally you can specify a raster operation with *rop*.
        
        :type dx: int
        :param dx: Top left destination X coordinate.
        :type dy: int
        :param dy: Top left destination Y coordinate.
        :type s_dp: c4d.bitmaps.GeClipMap
        :param s_dp: Source.
        :type sx1: int
        :param sx1: Top left source X coordinate.
        :type sy1: int
        :param sy1: Top left source Y coordinate.
        :type sx2: int
        :param sx2: Bottom right source X coordinate.
        :type sy2: int
        :param sy2: Bottom right source Y coordinate.
        :type rop: int
        :param rop: Raster operation:
        
        .. include:: /consts/GE_CM_BLIT.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetColor(self, r: int, g: int, b: int, alpha: int) -> None:
        """    
        Sets the draw color.
        
        :type r: int
        :param r: Red. (Between 0 and 255.).
        :type g: int
        :param g: Green. (Between 0 and 255.)
        :type b: int
        :param b: Blue. (Between 0 and 255.)
        :type alpha: int
        :param alpha: Alpha value. (Between 0 and 255.)
        
        
        """
        ...
    
    def SetOffset(self, off_x: int, off_y: int) -> None:
        """    
        Offsets all the following draw commands by this amount.
        
        .. note::
        
        The clip region is not offset.
        
        :type off_x: int
        :param off_x: X distance in pixels.
        :type off_y: int
        :param off_y: Y distance in pixels.
        
        
        """
        ...
    
    def SetDrawMode(self, mode: int, par: int) -> None:
        """    
        Sets the draw mode for the following drawing operations.
        
        :type mode: int
        :param mode: Mode:
        
        .. include:: /consts/GE_CM_DRAWMODE.rst
        :start-line: 3
        
        :type par: int
        :param par: Parameter (Depends on *mode*)
        
        
        """
        ...
    
    def SetPixel(self, x: int, y: int) -> None:
        """    
        Sets the pixel at (*x,y*) to the draw color.
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        
        
        """
        ...
    
    def Line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Draws a line from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: First X coordinate.
        :type y1: int
        :param y1: First Y coordinate.
        :type x2: int
        :param x2: Second X coordinate.
        :type y2: int
        :param y2: Second Y coordinate.
        
        
        """
        ...
    
    def Rect(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Draws the outline of a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        
        
        """
        ...
    
    def FillRect(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        
        
        """
        ...
    
    def Arc(self, x1: int, y1: int, x2: int, y2: int, seg: Any) -> None:
        """    
        Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        :type seq: int
        :param seg: The arc is drawn in the direction given by:
        
        === =====================================================
        0           (*x1,y1*) -> (*x2,y1*) -> (*x2,y2*)
        1           (*x2,y1*) -> (*x2,y2*) -> (*x1,y2*)
        2           (*x2,y2*) -> (*x1,y2*) -> (*x1,y1*)
        3           (*x1,y2*) -> (*x1,y1*) -> (*x2,y1*)
        === =====================================================
        
        
        """
        ...
    
    def FillArc(self, x1: int, y1: int, x2: int, y2: int, seg: Any) -> None:
        """    
        Draws an arc within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        :type seq: int
        :param seg: The arc is drawn in the direction given by:
        
        === =====================================================
        0           (*x1,y1*) -> (*x2,y1*) -> (*x2,y2*)
        1           (*x2,y1*) -> (*x2,y2*) -> (*x1,y2*)
        2           (*x2,y2*) -> (*x1,y2*) -> (*x1,y1*)
        3           (*x1,y2*) -> (*x1,y1*) -> (*x2,y1*)
        === =====================================================
        
        
        """
        ...
    
    def Ellipse(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Draws an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        
        
        """
        ...
    
    def FillEllipse(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Fills an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        
        
        """
        ...
    
    def SetPixelRGBA(self, x: int, y: int, r: int, g: int, b: int, a: int) -> None:
        """    
        Sets the pixel at (*x,y*) to the specified color.
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :type r: int
        :param r: Red. (Between 0 and 255.)
        :type g: int
        :param g: Green. (Between 0 and 255.)
        :type b: int
        :param b: Blue. (Between 0 and 255.)
        :type a: int
        :param a: Alpha value. (Between 0 and 255.)
        
        
        """
        ...
    
    def GetPixelRGBA(self, x: int, y: int) -> List[int]:
        """    
        Retrieves the color of the pixel at (x,y).
        
        .. code-block:: python
        
        r, g, b, a = clmap.GetPixelRGBA(5, 5)
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :rtype: List[int]
        :return: The color of the pixel.
        
        
        """
        ...
    
    def TextAt(self, x: int, y: int, txt: str) -> None:
        """    
        Prints the string txt with the top left corner at (*x,y*) in the current draw color.
        
        :type x: int
        :param x: Top left X coordinate.
        :type y: int
        :param y: Top left Y coordinate.
        :type txt: str
        :param txt: Text to print.
        
        
        """
        ...
    
    def TextWidth(self, txt: str) -> int:
        """    
        Calculates the width of the string *txt* in the current font.
        
        :type txt: str
        :param txt: The string.
        :rtype: int
        :return: Calculates the maximum height of a string in the current font.
        
        
        """
        ...
    
    def TextHeight(self) -> None:
        """    
        Calculates the maximum height of a string in the current font.
        
        
        """
        ...
    
    def TextAscent(self) -> None:
        """    
        Calculates the ascent in the current font. This is the distance from the baseline to the ascended line and usually represents the height of capital letters.
        
        
        """
        ...
    
    def ClipPoint(self, x: int, y: int) -> bool:
        """    
        Checks if a point is inside the clip region.
        
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :rtype: bool
        :return: **True** if the point is inside the region, otherwise **False**.
        
        
        """
        ...
    
    def ClipArea(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """    
        Checks if a rectangle is inside the clip region.
        
        :type x1: int
        :param x1: Top left X coordinate.
        :type y1: int
        :param y1: Top left Y coordinate.
        :type x2: int
        :param x2: Bottom right X coordinate.
        :type y2: int
        :param y2: Bottom right Y coordinate.
        :rtype: int
        :return: The result.
        
        
        """
        ...
    
    def SetFont(self, font_description: BaseContainer, font_size: float) -> bool:
        """    
        Sets the current font.
        
        :type font_description: c4d.BaseContainer
        :param font_description: The font description. Can be **None** for the default font.
        :type font_size: float
        :param font_size: Font size, or 0.0 for the default height.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetFont(self, font_description: BaseContainer) -> float:
        """    
        Returns the current font description.
        
        :type font_description: c4d.BaseContainer
        :param font_description: Assigned the current font description.
        :rtype: float
        :return: The font size.
        
        
        """
        ...
    
    @staticmethod
    def GetFontName(font_description: BaseContainer, type: int) -> str:
        """    
        Retrieves the font name from a font description.
        
        .. versionadded:: R17.032
        
        :type font_description: c4d.BaseContainer
        :param font_description: The font description.
        :type type: int
        :param type: The type of font name:
        
        .. include:: /consts/GE_FONT_NAME.rst
        :start-line: 3
        
        :rtype: str
        :return: The font name.
        
        
        """
        ...
    
    @staticmethod
    def GetFontDescription(name: str, type: int) -> BaseContainer:
        """    
        Retrieves a font description.
        
        .. versionadded:: R17.032
        
        :type name: str
        :param name: The font name.
        :type type: int
        :param type: The type of font name:
        
        .. include:: /consts/GE_FONT_NAME.rst
        :start-line: 3
        
        :rtype: c4d.BaseContainer
        :return: The font description.
        
        
        """
        ...
    
    @staticmethod
    def EnumerateFonts(sort_mode: str) -> BaseContainer:
        """    
        | Enumerates all fonts and returns them in a container.
        | For each font a container (font description) will be inserted. They can be used for :meth:`SetFont` and :meth:`GetFontName`.
        
        .. versionadded:: R17.032
        
        :type sort_mode: str
        :param sort_mode: The sort mode:
        
        .. include:: /consts/GE_CM_FONTSORT.rst
        :start-line: 3
        
        :rtype: c4d.BaseContainer
        :return: The font list.
        
        
        """
        ...
    
    @staticmethod
    def GetDefaultFont(type: int) -> BaseContainer:
        """    
        Retrieves Cinema 4D's default font.
        
        .. versionadded:: R17.032
        
        :type type: int
        :param type: The default font type:
        
        .. include:: /consts/GE_FONT_DEFAULT.rst
        :start-line: 3
        
        :rtype: c4d.BaseContainer
        :return: The default font description.
        
        
        """
        ...
    
    @staticmethod
    def GetFontSize(font_description: BaseContainer, type: int) -> float:
        """    
        Retrieves the font size for a given font.
        
        .. versionadded:: R17.032
        
        :type font_description: c4d.BaseContainer
        :param font_description: The font description.
        :type type: int
        :param type: The type of font size:
        
        .. include:: /consts/GE_FONT_SIZE.rst
        :start-line: 3
        
        :rtype: float
        :return: The font size.
        
        
        """
        ...
    
    @staticmethod
    def SetFontSize(font_description: BaseContainer, type: int, size: float) -> bool:
        """    
        Sets the font size for a given font.
        
        .. versionadded:: R17.032
        
        :type font_description: c4d.BaseContainer
        :param font_description: The font description.
        :type type: int
        :param type: The type of font size:
        
        .. include:: /consts/GE_FONT_SIZE.rst
        :start-line: 3
        
        :type size: float
        :param size: The font size to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    

class ColorProfileConvert(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.bitmaps.ColorProfileConvert
        :return: The new :class:`ColorProfileConvert <c4d.bitmaps.ColorProfileConvert>`.
        
        
        """
        ...
    
    def PrepareTransform(self, srccolormode: int, srcprofile: ColorProfile, dstcolormode: ColorProfile, dstprofile: ColorProfile, bgr: bool) -> bool:
        """    
        | Prepares the color conversion i.e. checks if a conversion is needed.
        | A conversion is only necessary if **True** is returned. Two identical color spaces will return **False**.
        
        :type srccolormode: int
        :param srccolormode: The source color mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type srcprofile: c4d.bitmaps.ColorProfile
        :param srcprofile: The source color profile.
        :type dstcolormode: c4d.bitmaps.ColorProfile
        :param dstcolormode: The destination color mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type dstprofile: c4d.bitmaps.ColorProfile
        :param dstprofile: The destination color profile.
        :type bgr: bool
        :param bgr: **True** to swap the RGB channels. Only necessary when working directly with Windows bitmaps.
        :rtype: bool
        :return: **True** a conversion is necessary, otherwise **False**.
        
        
        """
        ...
    
    def Convert(self, src: ByteSeq, dst: ByteSeq, cnt: int, skipInputComponents: bool, skipOutputComponents: bool) -> None:
        """    
        Converts the color profiles of the pixel data.
        
        :type src: c4d.storage.ByteSeq
        :param src: The source pixel buffer.
        :type dst: c4d.storage.ByteSeq
        :param dst: The destination pixel buffer.
        :type cnt: int
        :param cnt: The number of pixels to convert.
        :type skipInputComponents: bool
        :param skipInputComponents:
        
        | The number of bytes to skip in the source buffer after each converted pixel. For instance a RGB pixel contains 3 bytes.
        | After conversion the number of *skipInputComponents* bytes is added to the source pointer.
        
        :type skipOutputComponents: bool
        :param skipOutputComponents:
        
        | The number of bytes to skip in the destination buffer after each converted pixel. For instance a RGB pixel contains 3 bytes.
        | After conversion the number of SkipOutputComponents bytes is added to the destination pointer.
        
        
        """
        ...
    

class ColorProfile(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.bitmaps.ColorProfile
        :return: The new render data
        
        
        """
        ...
    
    def OpenProfileFromFile(self, fn: Union[str, MemoryFileStruct]) -> None:
        """    
        Open a profile from a file.
        
        :type fn: Union[str, c4d.storage.MemoryFileStruct]
        :param fn: The file.
        
        
        """
        ...
    
    def WriteProfileToFile(self, fn: Union[str, MemoryFileStruct]) -> bool:
        """    
        Write a profile to a file
        
        :type fn: Union[str, c4d.storage.MemoryFileStruct]
        :param fn: The file.
        :rtype: bool
        :return: Is **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetInfo(self) -> str:
        """    
        Returns the profile info.
        
        :rtype: str
        :return: The profile info
        
        
        """
        ...
    
    def HasProfile(self) -> bool:
        """    
        Check if a profile is set.
        
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def IsMonitorProfileMode(self) -> bool:
        """    
        Check if the current profile is the monitor profile.
        
        :rtype: bool
        :return: **True** if the monitor profile is set, otherwise **False**.
        
        
        """
        ...
    
    def SetMonitorProfileMode(self, on: bool) -> bool:
        """    
        Link this color profile to the monitor color profile.
        
        :type on: bool
        :param on: Set **True** to link the color profile to the monitor profile.
        :rtype: bool
        :return: **True** if set, otherwise **False**.
        
        
        """
        ...
    
    def CheckColorMode(self, colormode: int) -> bool:
        """    
        Check the color mode of the color profile.
        
        :type colormode: int
        :param colormode: The mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if set, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def GetDefaultSRGB() -> ColorProfile:
        """    
        Returns the default SRGB final.
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The profile.
        
        
        """
        ...
    
    @staticmethod
    def GetDefaultLinearRGB() -> ColorProfile:
        """    
        Returns the default linear final.
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The profile.
        
        
        """
        ...
    
    @staticmethod
    def GetDefaultSGray() -> ColorProfile:
        """    
        Returns the default SGray linear color.
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The profile.
        
        
        """
        ...
    
    @staticmethod
    def GetDefaultLinearGray() -> ColorProfile:
        """    
        Returns the default gray linear color.
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The profile.
        
        
        """
        ...
    

class BaseBitmap(object):
    def __init__(self) -> None:
        """    
        :rtype:  :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>`
        :return: The new bitmap.
        
        
        """
        ...
    
    def __getitem__(self, key: int) -> Tuple[int, int, int]:
        """    
        This is similar to :meth:`GetPixel`.
        
        .. code-block:: python
        
        r, g, b = bmp[5, 5] #returns the color of a pixel at position x(5), y(5)
        
        :raise IndexError: If the pixel position is out of the bitmap boundaries. See :meth:`GetSize`, :meth:`GetBw` and :meth:`GetBh`.
        :type key: int
        :param key: The pixel position.
        :rtype: tuple(int, int, int)
        :return: The color of a pixel. Range between *0-255*.
        
        
        """
        ...
    
    def __setitem__(self, key: int, value: Tuple[int, int, int]) -> None:
        """    
        This is similar to :meth:`GetPixel`.
        
        .. code-block:: python
        
        bmp[5, 5] = (50, 255, 50) #returns the color of a pixel at position x(5), y(5)
        
        .. note::
        
        | The :class:`Vector <c4d.Vector>` objects does not support item deletion.
        | For instance by calling `del(bmp[5,5])`.
        
        :raise IndexError: If the pixel position is out of the bitmap boundaries. See :meth:`GetSize`, :meth:`GetBw` and :meth:`GetBh`.
        :type key: int
        :param key: The pixel position.
        :type value: tuple(int, int, int)
        :param value: The color of the pixel. Range between *0-255*.
        
        
        """
        ...
    
    def __eq__(self, other: Any) -> None:
        """    
        
        """
        ...
    
    def __ne__(self, other: Any) -> None:
        """    
        Check if two references point to the same bitmap.
        
        .. note::
        
        Does not compare if two references are equal.
        
        
        """
        ...
    
    def SetPixel(self, x: int, y: int, r: int, g: int, b: int) -> bool:
        """    
        | Sets the pixel at *(x, y)* to the color specified by *(r,g,b) (0 <= r/g/b <= 255)*.
        | Similar to the :meth:`__setitem__`.
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type x: int
        :param x: The X coordinate.
        :type y: int
        :param y: The Y coordinate.
        :type r: int
        :param r: The red component.
        :type g: int
        :param g: The green component.
        :type b: int
        :param b: The blue component.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPixel(self, x: int, y: int) -> List[int]:
        """    
        Retrieves the color at (*x,y*). Similar to the :meth:`__getitem__`.
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type x: int
        :param x: The X coordinate.
        :type y: int
        :param y: The Y coordinate.
        :rtype: List[int]
        :return: The color of the pixel. Range between *0-255*.
        
        
        """
        ...
    
    def GetPixelDirect(self, x: int, y: int) -> Vector:
        """    
        Retrieves the color at (*x,y*).
        
        .. versionadded:: S22
        
        .. note::
        
        | The range of the assigned parameters are *0.0* to *255.0*, regardless of the bit depth of the image where (255.0, 255.0, 255.0) is white.
        | The range returns float value, so 8, 16 and 32 bit precision is supported.
        
        :param x: The X coordinate.
        :type x: int
        :param y: The Y coordinate.
        :type y: int
        :return: Color as form of a 3D Vector.
        :rtype: c4d.Vector
        
        
        """
        ...
    
    def GetPixelCnt(self, x: int, y: int, cnt: int, buffer: ByteSeq, inc: int, dstmode: int, flags: int, conversion: ColorProfileConvert) -> bool:
        """    
        Reads *cnt* pixels from (*x*, *y*) in the bitmap to the buffer with mode *dstmode*, incrementing *inc* bytes for each pixel.
        
        :type x: int
        :param x: X coordinate of the first pixel to set.
        :type y: int
        :param y: Y coordinate of the first pixel to set.
        :type cnt: int
        :param cnt: Number of pixels to set.
        :type buffer: c4d.storage.ByteSeq
        :param buffer: The destination buffer.
        :type inc: int
        :param inc: The byte increment per pixel in the buffer.
        :type dstmode: int
        :param dstmode: The destination mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/PIXELCNT.rst
        :start-line: 3
        
        :type conversion: c4d.bitmaps.ColorProfileConvert
        :param conversion:
        
        .. versionadded:: R17.032
        
        | This should be normally set to **None**. Pass a color profile only if a conversion is wanted before retrieving the pixel data.
        | This only works if either the bitmap is 32-bit per component (so no 8/16-bit images) or the *dstmode* is 32-bit per component.
        | The conversion is done before color reduction (e.g. if *dstmode* is 16-bit the profile is first applied and then the data resampled to 16-bit).
        
        :rtype: bool
        :return: **True** if successful, otherwise *False*.
        
        
        """
        ...
    
    def SetPixelCnt(self, x: int, y: int, cnt: int, buffer: ByteSeq, inc: int, srcmode: int, flags: int) -> bool:
        """    
        Sets *cnt* pixels at (*x*, *y*) in the bitmap from buffer with mode *srcmode*, incrementing *inc* bytes for each pixel.
        
        The following example shows you how to read/write from/into an image.
        
        .. code-block:: python
        
        '''
        Test Example:
        BaseBitmap.SetPixelCnt()/BaseBitmap.GetPixelCnt()
        
        This example shows how to copy the internal data of a 32 bit per-channel image to a new one.
        '''
        
        import c4d, struct
        
        def main():
        path = c4d.storage.LoadDialog(type=c4d.FILESELECTTYPE_IMAGES, title="Please Choose a 32 Bit Image:")
        if not path: return
        
        # Create and initialize selected image
        orig = c4d.bitmaps.BaseBitmap()
        if orig.InitWith(path)[0] != c4d.IMAGERESULT_OK:
        c4d.gui.MessageDialog("Cannot load image "" + path + "".")
        return
        
        # Check if channel depth is really 32 bit
        if orig.GetBt()/3 != 32:
        c4d.gui.MessageDialog("The image "" + path + "" is not a 32 bit per-channel image.")
        return
        
        # Get selected image infos
        width, height = orig.GetSize()
        bits = orig.GetBt()
        
        # Create the copy and initialize it
        copy = c4d.bitmaps.BaseBitmap()
        copy.Init(width, height, bits)
        
        # Calculate the number of bytes per pixel
        inc = orig.GetBt()/8 # Each pixel has RGB bits, so we need an offset of 'inc' bytes per pixel
        # the image has 32 bits per-channel : (32*3)/8 = 12 bytes per pixel (1 byte = 8 bits)
        # the image has 3 channels per pixel (RGB) : 12/3 = 4 bytes per component = 1 float
        
        # Create a byte sequence buffer large enough to store the copied image pixels
        sq = c4d.storage.ByteSeq(None, width*height*inc)
        
        for row in xrange(height):
        offset = sq.GetOffset(row*(width*inc)) # Offset on bitmap row + offset bytes per pixel
        orig.GetPixelCnt(0, row, width, offset, inc, c4d.COLORMODE_RGBf, c4d.PIXELCNT_NONE) # Read pixels from the original bitmap to the buffer
        
        #Example: RGB value of first pixel (only for 32 bits)
        #import struct
        #r, g, b = struct.unpack("fff", sq[0:12])
        #print r, g, b
        
        for row in xrange(height):
        offset = sq.GetOffset(row*(width*inc)) # Offset on bitmap row + offset bytes per pixel
        copy.SetPixelCnt(0, row, width, offset, inc, c4d.COLORMODE_RGBf, c4d.PIXELCNT_NONE) # Set pixels in bitmap copy
        
        c4d.bitmaps.ShowBitmap(orig) # Show original
        c4d.bitmaps.ShowBitmap(copy) # Show copied image
        
        
        if __name__=='__main__':
        main()
        
        
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
    
    def GetInternalChannel(self) -> BaseBitmap:
        """    
        | Get the internal read-only alpha channel.
        | The internal alpha channel is the one that's saved together with the picture, with those formats that support this.
        
        .. note::
        
        If no internal alpha is available, None is returned.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The internal alpha channel.
        
        
        """
        ...
    
    def GetAlphaPixel(self, channel: Any, x: int, y: int) -> int:
        """    
        Get the alpha value at (*x,y*).
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The alpha channels to use. Has to be an alpha bitmap.
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :rtype: int
        :return: The alpha value. Range is *0* to *255*.
        
        
        """
        ...
    
    def SetAlphaPixel(self, channel: Any, x: int, y: int, val: int) -> None:
        """    
        Sets the alpha value at *(x,y)* to *val*. The valid range of val is *0* to *255*.
        
        .. note::
        
        | Currently this method does no range check of *x* and *y*.
        | This might be added in the future.
        | Please do the check on your own.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The alpha channels to use. Has to be an alpha bitmap.
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :type val: int
        :param val: The alpha value. Range is *0* to *255*.
        
        
        """
        ...
    
    def Init(self, x: int, y: int, depth: int, flags: int) -> int:
        """    
        Initializes the bitmap to the given dimensions and depth.
        
        .. warning::
        
        Any previous data in the bitmap object is lost.
        
        .. note::
        
        | The bitmap class only supports up to 4 channels.
        | Also, most image loaders will only load one alpha channel.
        
        :type x: int
        :param x: The requested width in pixels. (Max 16000 pixels.).
        :type y: int
        :param y: The requested width in pixels. (Max 16000 pixels.).
        :type depth: int
        :param depth:
        
        | The requested bit depth (24 default).
        | The possible values are {1,4,8,16,24,32}.
        | On some platforms 32 bits will be used even if 24 is requested, to allow for padding.
        
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/INITBITMAPFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: The result:
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitWith(self, name: Union[str, MemoryFileStruct], frame: Optional[int] = ...) -> Tuple[int, bool]:
        """    
        | Loads a file into the bitmap. The file can be either a movie or a picture.
        | The file format is automatically detected
        
        .. code-block:: python
        
        result, isMovie = bmp.InitWith(path)
        if result == c4d.IMAGERESULT_OK: #int check
        # picture loaded
        
        if isMovie: #bool check
        pass # file is a movie
        else:
        pass # file is no movie
        
        .. note::
        
        | The bitmap class only supports up to 4 channels.
        | Also, most image loaders will only load one alpha channel.
        
        :type name: Union[str, c4d.storage.MemoryFileStruct]
        :param name: The file.
        :type frame: int
        :param frame: The frame number to load in a movie.
        :rtype: tuple(int, bool)
        :return: The result for first element:
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        The second element is **True** if the loaded picture was a movie.
        
        
        """
        ...
    
    def FlushAll(self) -> None:
        """    
        Resets the bitmap to its initial state and frees allocated memory.
        
        .. warning::
        
        Requires a call to :meth:`Init` before the bitmap can be used again.
        
        
        """
        ...
    
    def SetColorProfile(self, profile: ColorProfile) -> bool:
        """    
        Copy the color profile to the bitmap.
        
        :type profile: c4d.bitmaps.ColorProfile
        :param profile: The profile.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetColorProfile(self) -> ColorProfile:
        """    
        Get a new color profile instance of the bitmap.
        
        :rtype: c4d.bitmaps.ColorProfile
        :return: The profile.
        
        
        """
        ...
    
    def CopyTo(self, dst: BaseBitmap) -> bool:
        """    
        Copies the image to *dst*.
        
        :type dst: c4d.bitmaps.BaseBitmap
        :param dst: The bitmap to copy the image to.
        :rtype: bool
        :return: Success of copying the image.
        
        
        """
        ...
    
    def CopyPartTo(self, dst: BaseBitmap, x: int, y: int, w: int, h: int) -> bool:
        """    
        Copies a part of the image to *dst*.
        
        :type dst: c4d.bitmaps.BaseBitmap
        :param dst: The bitmap to copy the image to.
        :type x: int
        :param x: The X position of the part to be copied from the source image.
        :type y: int
        :param y: The Y position of the part to be copied from the source image.
        :type w: int.
        :param w: The width of the part to be copied.
        :type h: int
        :param h: The height of the part to be copied.
        :rtype: bool
        :return: Success of copying the image.
        
        
        """
        ...
    
    def GetClone(self) -> BaseBitmap:
        """    
        Clones the Bitmap and returns a new instance.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The clone.
        
        
        """
        ...
    
    def GetClonePart(self, x: int, y: int, w: int, h: int) -> BaseBitmap:
        """    
        Clones a part of the bitmap, specified by the rectangle *(x,y)* to *(x+w,y+h)*.
        
        :type x: int
        :param x: The upper X coordinate of the rectangle.
        :type y: int
        :param y: The upper Y coordinate of the rectangle.
        :type w: int.
        :param w: The width of the rectangle.
        :type h: int
        :param h: The height of the rectangle.
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The cloned bitmap, or **None** if an error occured.
        
        
        """
        ...
    
    def Save(self, name: Union[str, MemoryFileStruct], format: int, data: BaseContainer, savebits: int) -> int:
        """    
        Saves the bitmap to a file. Valid formats are:
        
        .. include:: /consts/FILTER.rst
        :start-line: 3
        
        :type name: Union[str, c4d.storage.MemoryFileStruct]
        :param name: A file.
        :type format: int
        :param format: The image format.
        :type data: c4d.BaseContainer
        :param data: The data.
        :type savebits: int
        :param savebits: Can be a combination of the following flags:
        
        .. include:: /consts/SAVEBIT.rst
        :start-line: 3
        
        :rtype: int
        :return: **True** if :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>` is not empty, otherwise **False**.
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetChannelCount(self) -> int:
        """    
        Returns the number of alpha channels in the bitmap, including the internal channel.
        
        :rtype: int
        :return: Number of alpha channels.
        
        
        """
        ...
    
    def Within(self, x: int, y: int) -> bool:
        """    
        Checks if a position is in the bitmap.
        
        :type x: int
        :param x: The X Coordinate
        :type y: int
        :param y: The Y Coordinate
        :rtype: bool
        :return: **True** if the coordinate is in the bitmap.
        
        
        """
        ...
    
    def GetSize(self) -> List[int]:
        """    
        Returns the size of the bitmap in pixels.
        
        .. note::
        
        If the bitmap hasn't been initialized the return values are 0. (This is the only way to see if a bitmap has been initialized.)
        
        .. code-block:: python
        
        #bmp is a BaseBitmap instance
        x, y = bmp.GetSize()
        
        :rtype: List[int]
        :return: Bitmap width and height in pixels, or 0 if the bitmap is not initialized.
        
        
        """
        ...
    
    def GetBw(self) -> int:
        """    
        Returns the width of the bitmap in pixels.
        
        .. note::
        
        If the bitmap hasn't been initialized the return value is 0. (This is the only way to see if a bitmap has been initialized.)
        
        :rtype: int
        :return: Bitmap width in pixels, or 0 if the bitmap is not initialized.
        
        
        """
        ...
    
    def GetBh(self) -> int:
        """    
        Returns the height of the bitmap in pixels.
        
        :rtype: int
        :return: Bitmap height in pixels.
        
        
        """
        ...
    
    def GetBt(self) -> int:
        """    
        Returns the number of bits per pixel.
        
        :rtype: int
        :return: The number of bits.
        
        
        """
        ...
    
    def SetCMAP(self, i: int, r: int, g: int, b: int) -> None:
        """    
        | If the image in the bitmap has 8 bit indexed color, this function can be used to set the palette entries.
        | All four parameters must be between *0* and *255*.
        
        :type i: int
        :param i: The index.
        :type r: int
        :param r: The red component.
        :type g: int
        :param g: The green component.
        :type b: int
        :param b: The blue component.
        
        
        """
        ...
    
    def GetBpz(self) -> int:
        """    
        Returns the number of bytes per line.
        
        :rtype: int
        :return: Number of bytes per line.
        
        
        """
        ...
    
    def SetData(self, id: int, data: Any) -> bool:
        """    
        Sets bitmap data. Private.
        
        :type id: int
        :param id: The data ID to set.
        :type data: any
        :param data: The data to set.
        :rtype: bool
        :return: **True** if the data could be set, otherwise **False**.
        
        
        """
        ...
    
    def GetData(self, id: int, default: Any) -> Any:
        """    
        Gets bitmap data. Private.
        
        :type id: int
        :param id: The data ID to get.
        :type default: any
        :param default: Returned if data is not set.
        :rtype: Any
        :return: The retrieved data, or *default*.
        
        
        """
        ...
    
    def ScaleBicubic(self, dst: BaseBitmap, src_xmin: int, src_ymin: int, src_xmax: int, src_ymax: int, dst_xmin: int, dst_ymin: int, dst_xmax: int, dst_ymax: int) -> None:
        """    
        | Scales the bitmap rectangle (*src_xmin*, *src_ymin*, *src_xmax*, *src_ymax*) to fit in the destination bitmap rectangle (*dst_xmin*, *dst_ymin*, *dst_xmax*, *dst_ymax*) and copies it there.
        | The scaling, if necessary, is done using bicubic interpolation.
        | The destination needs to be initialized before calling this function.
        
        .. code-block:: python
        
        bmp.ScaleBicubic(dst, 0, 0, bmp.GetBw()-1, bmp.GetBh()-1, 0, 0, dst.GetBw()-1, dst.GetBh()-1)
        
        .. note::
        
        This function can currently only scale down, i.e. the destination needs to be smaller to the source in size.
        
        .. image:: /_imgs/modules/bitmaps/basebitmap_scalebicubic.jpg
        :width: 70%
        
        :type dst: c4d.bitmaps.BaseBitmap
        :param dst: The destination bitmap.
        :type src_xmin: int
        :param src_xmin: Source top left X coordinate.
        :type src_ymin: int
        :param src_ymin: Source top left Y coordinate.
        :type src_xmax: int
        :param src_xmax: Source bottom right X coordinate.
        :type src_ymax: int
        :param src_ymax: Source bottom right Y coordinate.
        :type dst_xmin: int
        :param dst_xmin: Destination top left X coordinate.
        :type dst_ymin: int
        :param dst_ymin: Destination top left Y coordinate.
        :type dst_xmax: int
        :param dst_xmax: Destination bottom right X coordinate.
        :type dst_ymax: int
        :param dst_ymax: Destination bottom right Y coordinate.
        
        
        """
        ...
    
    def Scale(self, dst: BaseBitmap, intens: int, sample: bool, nprop: bool) -> None:
        """    
        .. deprecated:: R18
        
        Use :meth:`BaseBitmap.ScaleIt` instead.
        
        Scales the bitmap to fit in the destination bitmap and copies it there.
        
        .. note::
        
        The destination needs to be initialized with the destination size before calling this function.
        
        .. image:: /_imgs/modules/bitmaps/basebitmap_scaleit.jpg
        :width: 70%
        
        :type dst: c4d.bitmaps.BaseBitmap
        :param dst: The destination image. Must be initiated already with the destination size.
        :type intens: int
        :param intens: Lets you change brightness of the image (128 = 50% brightness, 256 = unchanged).
        :type sample: bool
        :param sample: If **True** a better scaling algorithm is used, which results in a better quality but is a bit slower.
        :type nprop: bool
        :param nprop: Must be **True** if non-proportional scaling is wanted.
        
        
        """
        ...
    
    def ScaleIt(self, dst: BaseBitmap, intens: int, sample: bool, nprop: bool) -> None:
        """    
        Scales the bitmap to fit in the destination bitmap and copies it there.
        
        .. note::
        
        The destination needs to be initialized with the destination size before calling this function.
        
        .. image:: /_imgs/modules/bitmaps/basebitmap_scaleit.jpg
        :width: 70%
        
        :type dst: c4d.bitmaps.BaseBitmap
        :param dst: The destination image. Must be initiated already with the destination size.
        :type intens: int
        :param intens: Lets you change brightness of the image (128 = 50% brightness, 256 = unchanged).
        :type sample: bool
        :param sample: If **True** a better scaling algorithm is used, which results in a better quality but is a bit slower.
        :type nprop: bool
        :param nprop: Must be **True** if non-proportional scaling is wanted.
        
        
        """
        ...
    
    def AddChannel(self, internal: bool, straight: bool) -> int:
        """    
        Adds a new alpha channel to the image.
        
        :type internal: bool
        :param internal:
        
        | Should only be **True** for the first alpha.
        | The internal alpha will be stored within an image if the image format supports alphas.
        
        :type straight: bool
        :param straight:
        
        | Should be **True** if the image has to be interpreted as straight.
        | For information about straight alphas please take a look at the corresponding option in the render settings of Cinema 4D and the Cinema 4D manual.
        
        :rtype: int
        :return: The new channel.
        
        
        """
        ...
    
    def RemoveChannel(self, channel: BaseBitmap) -> None:
        """    
        Removes the specified channel from the bitmap.
        
        :type channel: c4d.bitmaps.BaseBitmap
        :param channel: The alpha channels to use.
        
        
        """
        ...
    
    def GetChannelNum(self, num: int) -> BaseBitmap:
        """    
        Returns the channel ID from the channel index.
        
        :type num: int
        :param num: A number between 0 and :meth:`GetChannelCount`.
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The requested channel.
        
        
        """
        ...
    
    def GetDirty(self) -> int:
        """    
        Private.
        
        :rtype: int
        :return: Dirty count, incremented when the bitmap changes.
        
        
        """
        ...
    
    def SetDirty(self) -> None:
        """    
        Makes the bitmap dirty.
        
        
        """
        ...
    
    def IsMultipassBitmap(self) -> bool:
        """    
        Checks if the image is a :class:`MultipassBitmap <c4d.bitmaps.MultipassBitmap>`.
        
        :rtype: bool
        :return: **True** if the image is a :class:`MultipassBitmap <c4d.bitmaps.MultipassBitmap>`, otherwise **False**
        
        
        """
        ...
    
    def GetColorMode(self) -> int:
        """    
        Returns the color mode of the bitmap.
        
        :rtype: int
        :return: Color mode
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMemoryInfo(self) -> int:
        """    
        Get the size of the memory used by the bitmap.
        
        :rtype: long
        :return: Memory size of the bitmap.
        
        
        """
        ...
    
    def GetUpdateRegionBitmap(self) -> BaseBitmap:
        """    
        Get the updated region of a bitmap.
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The updated region.
        
        
        """
        ...
    

class MultipassBitmap(object):
    def __init__(self, bx: int, by: int, mode: int) -> None:
        """    
        | Allocates a multipass bitmap of size bx/by and bit depth given by mode.
        | The first RGBA layer is also created.
        
        :type bx: int
        :param bx: Width in pixels.
        :type by: int
        :param bx: Height in pixels.
        :type mode: int
        :param mode: Main mode:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The new multipass bitmap.
        
        
        """
        ...
    
    def AllocWrapper(self, bmp: BaseBitmap) -> MultipassBitmap:
        """    
        | Allocates a multipass wrapper for bmp.
        | The returned multipass wrapper can be modified freely since the initial bmp is copied.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The bitmap to wrap. The caller owns the pointed bitmap.
        :rtype: MultipassBitmap
        :return: The allocated MultipassBitmap, or None if the allocation failed.
        
        
        """
        ...
    
    def DeleteLayer(self, layer: MultipassBitmap) -> bool:
        """    
        Deletes *layer* from the bitmap, freeing the memory.
        
        :type layer: c4d.bitmaps.MultipassBitmap
        :param layer: The layer to delete. Never access this reference afterwards.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FindUserID(self, id: int, subid: int) -> MultipassBitmap:
        """    
        Finds a layer in the bitmap by ID.
        
        :type id: int
        :param id: Main layer ID.
        :type subid: int
        :param subid: Sub ID.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The found layer or **None**.
        
        
        """
        ...
    
    def ClearImageData(self) -> None:
        """    
        Clears the image data for all layers.
        
        .. note::
        
        The layers themselves are not removed or deleted.
        
        
        """
        ...
    
    def GetPaintBitmap(self) -> PaintBitmap:
        """    
        Gets a BodyPaint 3D paint bitmap for the multipass bitmap.
        
        :rtype: c4d.modules.bodypaint.PaintBitmap
        :return: The paint bitmap.
        
        
        """
        ...
    
    def FreeHiddenLayers(self) -> None:
        """    
        Free the hidden layers.
        
        
        """
        ...
    
    def AddLayer(self, insertafter: MultipassBitmap, colormode: int, hidden: bool) -> None:
        """    
        Adds a layer after *insertafter* with mode *colormode* after *insertafter* in the bitmap.
        
        :type insertafter: c4d.bitmaps.MultipassBitmap
        :param insertafter: The layer to insert after.
        :type colormode: int
        :param colormode: Color mode of the new layer:
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :type hidden: bool
        :param hidden: If this is **True**, the layer is hidden.
        
        
        """
        ...
    
    def AddAlpha(self, insertafter: MultipassBitmap, colormode: int) -> MultipassBitmap:
        """    
        Adds an alpha layer with mode *colormode* after *insertafter* in the bitmap.
        
        :type insertafter: c4d.bitmaps.MultipassBitmap
        :param insertafter: The layer to insert after.
        :type colormode: int
        :param colormode: Color mode of the new alpha layer.
        
        .. include:: /consts/COLORMODE.rst
        :start-line: 3
        
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The added alpha layer or **None**
        
        
        """
        ...
    
    def AddFolder(self, insertafter: MultipassBitmap, hidden: bool) -> MultipassBitmap:
        """    
        Adds a folder after *insertafter* in the bitmap.
        
        :type insertafter: c4d.bitmaps.MultipassBitmap
        :param insertafter: The layer to insert after.
        :type hidden: bool
        :param hidden: If this is **True**, the layer is hidden.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The added folder or **None**.
        
        
        """
        ...
    
    def GetLayers(self, flags: int) -> List[BaseBitmap]:
        """    
        Gets all the layers specified by *flags*.
        
        .. versionadded:: R14.014
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/MPB_GETLAYERS.rst
        :start-line: 3
        
        :rtype: list[c4d.bitmaps.BaseBitmap]
        :return: The layers.
        
        
        """
        ...
    
    def GetParameter(self, id: int) -> Any:
        """    
        Gets a layer parameter.
        
        :type id: int
        :param id: The layer parameter ID:
        
        .. include:: /consts/MPBTYPE.rst
        :start-line: 3
        
        :rtype: Any
        :return: The retrieved layer parameter data. Can be **None**.
        
        
        """
        ...
    
    def SetParameter(self, id: int, t_data: Any) -> Any:
        """    
        Sets a layer parameter.
        
        :type id: int
        :param id: The layer parameter ID:
        
        .. include:: /consts/MPBTYPE.rst
        :start-line: 3
        
        :type t_data: any
        :param t_data: The new parameter data.
        :rtype: Any
        :return: **True** if the layer parameter was successfully set, otherwise **False**.
        
        
        """
        ...
    
    def GetLayerNum(self, num: int) -> MultipassBitmap:
        """    
        Gets the layer with number *num*.
        
        :type num: int
        :param num: Layer index, *0* <= *num* < :meth:`GetLayerCount`.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The retrieved layer, or **None** if the operation failed.
        
        
        """
        ...
    
    def GetAlphaLayerNum(self, num: int) -> MultipassBitmap:
        """    
        Gets the alpha layer with number *num*.
        
        :type num: int
        :param num: Alpha layer index, *0* <= *num* < :meth:`GetAlphaLayerCount`.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The retrieved layer, or **None** if the operation failed.
        
        
        """
        ...
    
    def GetHiddenLayerNum(self, num: int) -> MultipassBitmap:
        """    
        Gets the hidden layer with number *num*.
        
        :type num: int
        :param num: Hidden layer index, *0* <= *num* < :meth:`GetHiddenLayerCount`.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The retrieved layer, or **None** if the operation failed.
        
        
        """
        ...
    
    def GetHiddneLayerNum(self, num: int) -> MultipassBitmap:
        """    
        .. deprecated:: R21.204
        
        Use :meth:`MultipassBitmap.GetHiddenLayerNum` instead.
        
        Gets the hidden layer with number *num*.
        
        :type num: int
        :param num: Hidden layer index, *0* <= *num* < :meth:`GetHiddenLayerCount`.
        :rtype: c4d.bitmaps.MultipassBitmap
        :return: The retrieved layer, or **None** if the operation failed.
        
        
        """
        ...
    
    def GetLayerCount(self, num: int) -> int:
        """    
        | Retrieves the number of layers in the bitmap.
        | This is the sum of the number of layers, folders and alphas that are direct children of this bitmap.
        
        :type num: int
        :param num: Hidden layer index, *0* <= *num* < :meth:`GetHiddenLayerCount`.
        :rtype: int
        :return: Layer count.
        
        
        """
        ...
    
    def GetAlphaLayerCount(self) -> int:
        """    
        Retrieves the number of alpha layers in the bitmap.
        
        :rtype: int
        :return: Alpha layer count.
        
        
        """
        ...
    
    def GetHiddenLayerCount(self) -> int:
        """    
        Retrieves the number of hidden layers in the bitmap.
        
        :rtype: int
        :return: Hidden layer count.
        
        
        """
        ...
    


def ShowBitmap(bmp: BaseBitmap) -> None:
    """    
    Shows a bitmap in the picture viewer.
    
    :type bmp: c4d.bitmaps.BaseBitmap
    :param bmp: The bitmap. Will be copied.
    
    
    """
    ...

def InitResourceBitmap(resource_id: int) -> BaseBitmap:
    """    
    | Loads the global icon with ID *resource_id*.
    | Cinema 4D registers hundreds of its icons at program start and this way you can access them, for example *RESOURCEIMAGE_MOVE* is the move symbol.
    
    You can also resource your own icons via :func:`RegisterIcon() <c4d.gui.RegisterIcon>`.
    
    .. note::
    
    Also you can access the icons for commands.
    
    .. code-block:: python
    
    import c4d
    
    icon = c4d.bitmaps.InitResourceBitmap(c4d.RESOURCEIMAGE_MOVE) # Returns the 'move' bitmap from the list below
    
    :type resource_id: int
    :param resource_id: Resource ID to load.
    :rtype: c4d.bitmaps.BaseBitmap
    :return: The loaded bitmap or **None**. Find a list of all icons ID in :doc:`RESOURCEIMAGE`.
    
    
    """
    ...

def GetImageSettingsDictionary(data: BaseContainer, filterId: int) -> Any:
    """    
    Extracts the image format settings from *data*.
    
    .. versionadded:: R20
    
    :type data: c4d.BaseContainer
    :param data: The container to extract.
    :type filterId: int
    :param filterId: The filter Id.
    :rtype: maxon.DataDictionary
    :return: The extracted image format settings.
    
    
    """
    ...

def SetImageSettingsDictionary(settings: Any, data: BaseContainer, filterId: int) -> None:
    """    
    Replaces the image format settings in *data*.
    
    .. versionadded:: R20
    
    :type settings: maxon.DataDictionary
    :param settings: The image format settings to replace.
    :type data: c4d.BaseContainer
    :param data: The container to modify.
    :type filterId: int
    :param filterId: The filter Id.
    
    
    """
    ...

