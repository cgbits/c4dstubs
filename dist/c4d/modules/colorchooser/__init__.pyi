from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import Vector
from c4d.documents import BaseDocument


class ColorSwatchGroup(object):
    def __init__(self, name: str, selected: bool, colors: Any) -> None:
        """    
        Creates a new swatch group.
        
        .. versionchanged:: R20
        
        *colors* changed to a maxon.BaseArray of maxon.ColorA.
        
        :type name: str
        :param name: The name of the group.
        :type selected: bool
        :param selected: The selection state of the group.
        :type colors: maxon.BaseArray[maxon.ColorA]
        :param colors: The colors to fill the group with.
        :rtype: c4d.modules.colorchooser.ColorSwatchGroup
        :return: A new swatch group.
        
        
        """
        ...
    
    def Merge(self, group: ColorSwatchGroup) -> bool:
        """    
        Merges colors from *group*.
        
        :type group: c4d.modules.colorchooser.ColorSwatchGroup
        :param group: The group to merge colors from.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def CopyFrom(self, group: ColorSwatchGroup) -> bool:
        """    
        Copies a group.
        
        :type group: c4d.modules.colorchooser.ColorSwatchGroup
        :param group: The group to copy colors from.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetName(self) -> str:
        """    
        Retrieves the group name.
        
        :rtype: str
        :return: The group name.
        
        
        """
        ...
    
    def SetName(self, name: str) -> None:
        """    
        Sets the group name.
        
        :type name: str
        :param name: The new group name.
        
        
        """
        ...
    
    def GetColorCount(self) -> int:
        """    
        Retrieves the number of colors stored in the group.
        
        :rtype: int
        :return: The number of colors stored in the group.
        
        
        """
        ...
    
    def GetColor(self, index: int) -> Any:
        """    
        Retrieves the color at the given *index*.
        
        .. versionchanged:: R20
        
        The function returns a maxon.ColorA in the tuple.
        
        :type index: int
        :param index: The index of the color. Must be 0 <= *index* < :meth:`GetColorCount()`.
        :rtype: tuple(maxon.ColorA, bool)
        :return: The color value and its selection status.
        
        
        """
        ...
    
    def GetColors(self, selectedOnly: bool) -> Any:
        """    
        Retrieves the colors stored in the group.
        
        .. versionchanged:: R20
        
        The function returns a maxon.BaseArray of maxon.ColorA.
        
        :type selectedOnly: bool
        :param selectedOnly: Set to **True** to get only the selected colors, set to **False** to get all colors (default).
        :rtype: maxon.BaseArray[maxon.ColorA]
        :return: The list of colors.
        
        
        """
        ...
    
    def SetColor(self, index: int, color: Any, selected: int) -> bool:
        """    
        Edits the color at the given *index*.
        
        .. versionchanged:: R20
        
        *color* changed to maxon.ColorA type.
        
        :type index: int
        :param index: The index of the color. Must be 0 <= *index* < :meth:`GetColorCount()`.
        :type color: maxon.ColorA
        :param color: The new color value.
        :type selected: int
        :param selected: The new selection status. Possible values are: `-1` = keep current selection status unchanged, 0 = `unselect`, 1 = `select`.
        :rtype: bool
        :return: **True** if the color could be changed, otherwise **False**.
        
        
        """
        ...
    
    def AddColor(self, color: Any, selected: Vector, insertAt: Vector) -> int:
        """    
        Adds a new *color* to the group.
        
        .. versionchanged:: R20
        
        *color* changed to maxon.ColorA type.
        
        :type color: maxon.ColorA
        :param color: The color value.
        :type selected: c4d.Vector
        :param selected: The initial selection state of the color.
        :type insertAt: c4d.Vector
        :param insertAt: The index of the new color (the list size will increase and the existing elements are moved) or `-1` to add it to the end of the list.
        :rtype: int
        :return: The index of the new color or `-1` if an error occurred.
        
        
        """
        ...
    
    def AddColors(self, colors: Any, selected: bool, merge: bool, insertAt: int) -> int:
        """    
        Adds colors to the group.
        
        .. versionchanged:: R20
        
        *colors* changed to a maxon.BaseArray of maxon.ColorA.
        
        :type colors: maxon.BaseArray[maxon.ColorA]
        :param colors: The colors to add.
        :type selected: bool
        :param selected: The initial selection state of added colors.
        :type merge: bool
        :param merge: Set to **True** to merge the colors with current group colors. Set to **False** to replace the content of the group.
        :type insertAt: int
        :param insertAt: If *merge* is set to **True**, this is the index to insert the new colors.
        :rtype: int
        :return: The index of the new colors or `-1` if an error occurred.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Removes all colors from the group.
        
        
        """
        ...
    
    def RemoveColor(self, index: int, removeCount: int) -> bool:
        """    
        Removes the color at the given *index*.
        
        :type index: int
        :param index: The index of the color. Must be 0 <= *index* < :meth:`GetColorCount()`.
        :type removeCount: int
        :param removeCount: Number of colors to be removed. If *removeCnt* is higher than what is available only the number of remaining colors will be removed.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def RemoveSelectedColors(self) -> None:
        """    
        Removes all selected colors from the group.
        
        
        """
        ...
    
    def HasDuplicatedColors(self) -> bool:
        """    
        Checks if the group has duplicated colors.
        
        :rtype: bool
        :return: **True** if duplicated colors were found, otherwise **False**.
        
        
        """
        ...
    
    def RemoveDuplicatedColors(self) -> None:
        """    
        Removes duplicated colors in the group.
        
        
        """
        ...
    
    def InvertSelection(self) -> None:
        """    
        Inverts the selection state of all colors, so the currently selected colors will be unselected and vice-versa.
        
        
        """
        ...
    
    def SelectColor(self, index: int, selected: bool) -> bool:
        """    
        Selects/unselects the color at the given *index*.
        
        :type index: int
        :param index: The index of the color. Must be 0 <= *index* < :meth:`GetColorCount()`.
        :type selected: bool
        :param selected: The new selection status.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def IsColorSelected(self, index: int) -> bool:
        """    
        Checks if the color at the given *index* is selected.
        
        :type index: int
        :param index: The index of the color. Must be 0 <= *index* < :meth:`GetColorCount()`.
        :rtype: bool
        :return: **True** if the color is selected, **False** if it is unselected or *index* is invalid.
        
        
        """
        ...
    
    def SelectGroup(self, select: bool) -> None:
        """    
        Selects the group. This will select/unselect the group icon and all colors in the group.
        
        :type select: bool
        :param select: The new selection status.
        
        
        """
        ...
    
    def IsGroupSelected(self) -> bool:
        """    
        Checks if the group is selected.
        
        :rtype: bool
        :return: **True** if the group is selected, otherwise **False**.
        
        
        """
        ...
    
    def SortColors(self) -> None:
        """    
        Sorts colors in the group based on their HSV values.
        
        
        """
        ...
    

class ColorSwatchData(object):
    def __init__(self, doc: Optional[BaseDocument] = ..., global_: Optional[bool] = ...) -> None:
        """    
        Creates a new swatch data.
        
        :type doc: Optional[c4d.documents.BaseDocument]
        :param doc: Optional document to load swatches from.
        :type global_: Optional[bool]
        :param global_: If **True** the Global Swatch Group will be loaded.
        :rtype: c4d.modules.colorchooser.ColorSwatchData
        :return: A new swatch data.
        
        
        """
        ...
    
    def Load(self, doc: BaseDocument, merge: Optional[bool] = ..., globalColors: Optional[bool] = ...) -> bool:
        """    
        Loads color groups.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to load the color groups from.
        :type merge: Optional[bool]
        :param merge:
        
        | If **True** the colors of the given document are merged with the stored colors.
        | Otherwise the existing colors are discarded (default).
        
        :type globalColors: Optional[bool]
        :param globalColors:
        
        .. versionadded:: R20
        
        If **True** the global colors are loaded.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Save(self, doc: BaseDocument, globalColors: Optional[bool] = ...) -> bool:
        """    
        Saves the document-based color groups into the given document.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document to store the color groups into.
        :type globalColors: Optional[bool]
        :param globalColors:
        
        .. versionadded:: R20
        
        If **True** the global colors are saved.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def LoadPresetByName(self, name: str, merge: Optional[bool] = ...) -> bool:
        """    
        Loads the document-based swatch groups of the first preset with the given *name* found in the user's Color Swatch Preset directory, including subdirectories.
        
        .. seealso::
        
        :func:`GetColorSwatchPresetDirectory() <c4d.modules.colorchooser.GetColorSwatchPresetDirectory>`
        
        :type name: str
        :param name: The preset name to load.
        :type merge: Optional[bool]
        :param merge: If **True** the colors of the preset are merged with the stored colors. Otherwise the existing colors are discarded (default).
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def LoadPresetByURL(self, url: str, merge: BaseDocument) -> bool:
        """    
        Loads the document-based swatch groups of the given preset.
        
        :type url: str
        :param url: The preset url.
        :type merge: c4d.documents.BaseDocument
        :param merge: If **True** the colors of the preset are merged with the stored colors. Otherwise the existing colors are discarded (default).
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SavePresetByName(self, name: str, author: Optional[str] = ..., info: Optional[str] = ..., forceOverwrite: Optional[bool] = ...) -> bool:
        """    
        Saves the document-based groups as a Color Swatch preset.
        
        :type name: str
        :param name: The preset name.
        :type author: Optional[str]
        :param author: The preset author.
        :type info: Optional[str]
        :param info: Preset additional info.
        :type forceOverwrite: Optional[bool]
        :param forceOverwrite: Set to **True** to force overwriting the preset in case it already exists.
        :rtype: bool
        :return: **True** if the preset was saved successfully, otherwise **False**.
        
        
        """
        ...
    
    def SavePresetByURL(self, url: str, author: Optional[str] = ..., info: Optional[str] = ..., forceOverwrite: Optional[bool] = ...) -> bool:
        """    
        Saves the document-based groups as a Color Swatch preset.
        
        :type url: str
        :param url:
        
        | The url to save the preset to. Must include the preset name and must point to an existing library.
        | Example: `presetToSaveURL = c4d.modules.colorchooser.GetColorSwatchPresetDirectory() + "MyPreset"`
        
        :type author: Optional[str]
        :param author: The preset author.
        :type info: Optional[str]
        :param info: The preset additional info.
        :type forceOverwrite: Optional[bool]
        :param forceOverwrite: Set to **True** to force overwriting the preset in case it already exists.
        :rtype: bool
        :return: **True** if the preset was saved successfully, otherwise **False**.
        
        
        """
        ...
    
    def Merge(self, data: ColorSwatchData) -> bool:
        """    
        Merges groups from *data*.
        
        :type data: c4d.modules.colorchooser.ColorSwatchData
        :param data: The data to merge groups from.
        :rtype: bool
        :return: **True** if the groups were successfully merged, otherwise **False**.
        
        
        """
        ...
    
    def CopyFrom(self, data: ColorSwatchData) -> bool:
        """    
        Copies color swatch data.
        
        :type data: c4d.modules.colorchooser.ColorSwatchData
        :param data: The data to copy groups from.
        :rtype: bool
        :return: **True** if the color swatch data was successfully copied, otherwise **False**.
        
        
        """
        ...
    
    def GetGroupCount(self, category: int) -> int:
        """    
        Returns the number of groups stored in *category*.
        
        :type category: int
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :rtype: int
        :return: The number of color groups.
        
        
        """
        ...
    
    def GetGroupAtIndex(self, index: int, category: Optional[int] = ...) -> ColorSwatchGroup:
        """    
        Retrieves the  group at the given *index*.
        
        :type index: int
        :param index: The index of the color group. Must be 0 <= *index* < :meth:`GetGroupCount()`.
        :type category: Optional[int]
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :rtype: c4d.modules.colorchooser.ColorSwatchGroup
        :return: The swatch group or **None**.
        
        
        """
        ...
    
    def SetGroupAtIndex(self, index: int, group: ColorSwatchGroup, category: Optional[int] = ...) -> bool:
        """    
        Replaces the group at the given *index*.
        
        :type index: int
        :param index: The index of the color group. Must be 0 <= *index* < :meth:`GetGroupCount()`.
        :type group: c4d.modules.colorchooser.ColorSwatchGroup
        :param group: The group to set.
        :type category: Optional[int]
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the group was successfully set, otherwise **False**.
        
        
        """
        ...
    
    def AddGroup(self, category: Optional[int] = ..., name: Optional[str] = ..., selected: Optional[bool] = ..., insertAt: Optional[int] = ..., colors: Optional[Any] = ...) -> ColorSwatchGroup:
        """    
        Adds a new group.
        
        :type category: Optional[int]
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :type name: Optional[str]
        :param name: The name of the new group. If empty the default string "Untitled" will be used.
        :type selected: Optional[bool]
        :param selected: The initial selection state of the new group.
        :type insertAt: Optional[int]
        :param insertAt: The index of the new group (the list size will increase and the existing elements will be moved) or `-1` to add it to the end of the list (default).
        :type colors: List[maxon.ColorA]
        :param colors: The colors to fill the group with.
        :rtype: c4d.modules.colorchooser.ColorSwatchGroup
        :return: The new swatch group or **None**.
        
        
        """
        ...
    
    def InsertGroup(self, group: ColorSwatchGroup, insertAt: Optional[int] = ..., category: Optional[int] = ...) -> bool:
        """    
        Inserts an existing group.
        
        :type group: c4d.modules.colorchooser.ColorSwatchGroup
        :param group: The group to insert.
        :type insertAt: Optional[int]
        :param insertAt: The index of the new group (the list size will increase and the existing elements will be moved) or `-1` to add it to the end of the list (default).
        :type category: Optional[int]
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the group was successfully inserted, otherwise **False**.
        
        
        """
        ...
    
    def RemoveGroup(self, index: int, category: Optional[int] = ...) -> bool:
        """    
        Removes the document-based group at the given *index*.
        
        :type index: int
        :param index: The index of the color group to remove. Must be 0 <= *index* < :meth:`GetGroupCount()`.
        :type category: Optional[int]
        :param category:
        
        .. versionadded:: R20
        
        The group category:
        
        .. include:: /consts/SWATCH_CATEGORY.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the group was successfully removed, otherwise **False**.
        
        
        """
        ...
    
    def RemoveSelectedItems(self) -> None:
        """    
        Removes all selected groups and colors, including selected global colors.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Removes all groups and colors, including globals.
        
        
        """
        ...
    


def ColorRGBToString(color: Vector) -> str:
    """    
    | Converts a RGB *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).
    | Example: The string result for the color `Vector(0.45, 0.32, 1.0)` will be "115, 82, 255" if *WPREF_COLOR_RGBRANGE* is configured to *COLORSYSTEM_RANGE_255*.
    
    :type color: c4d.Vector
    :param color: The RGB color to convert to string. Its components must be in range [0.0, 1.0].
    :rtype: str
    :return: The string representation of the color.
    
    
    """
    ...

def ColorHSVToString(color: Vector) -> str:
    """    
    | Converts a HSV *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).
    | Example: The string result for the color `Vector(0.45, 0.32, 1.0)` will be "251.471 deg , 68 %, 100 %".
    
    :type color: c4d.Vector
    :param color: The HSV color to convert to string. Its components must be in range [0.0, 1.0]. See :func:`RGBToHSV() <c4d.utils.RGBToHSV>` / :func:`HSVToRGB() <c4d.utils.HSVToRGB>`.
    :rtype: str
    :return: The string representation of the color.
    
    
    """
    ...

def ColorComponentFloatTo8Bit(colorComponentInput: float) -> int:
    """    
    Converts a RGB float color component in range [0.0, 1.0] to 8-bit (range [0, 255]).
    
    :type colorComponentInput: float
    :param colorComponentInput: The color component to be converted. Must be in range [0.0, 1.0].
    :rtype: int
    :return: The converted 8-bit color component in range [0, 255].
    
    
    """
    ...

def ColorComponent8BitToFloat(colorComponentInput: int) -> float:
    """    
    Converts a RGB 8-bit color component (range [0, 255]) to float in range [0.0, 1.0].
    
    :type colorComponentInput: int
    :param colorComponentInput: The 8-bit color component to be converted. Must be in range [0, 255].
    :rtype: float
    :return: The converted color component in range [0.0, 1.0].
    
    
    """
    ...

def ColorFloatTo8Bit(floatColor: Vector) -> List[Any]:
    """    
    Converts a RGB float color in range [0.0, 1.0] to 8-bit color (range [0, 255]).
    
    :type floatColor: c4d.Vector
    :param floatColor: The color to be converted. Must be in range [0.0, 1.0].
    :rtype: list(int, int, int)
    :return: The converted 8-bit red, green and blue color components.
    
    
    """
    ...

def Color8BitToFloat(red: int, green: int, blue: int) -> None:
    """    
    Converts a RGB 8-bit color (range [0, 255]) to float color in range [0.0, 1.0].
    
    :type red: int
    :param red: The 8-bit color component to be converted. Must be in range [0, 255].
    :type green: int
    :param green: The 8-bit color component to be converted. Must be in range [0, 255].
    :type blue: int
    :param blue: The 8-bit color component to be converted. Must be in range [0, 255].
    :rtype: :class:`c4d.Vector`
    :return: The converted float color in range [0.0, 1.0].
    
    
    """
    ...

def ColorComponentFloatTo16Bit(colorComponentInput: float) -> int:
    """    
    Converts a RGB float color component in range [0.0, 1.0] to 16-bit (range [0, 65535]).
    
    :type colorComponentInput: float
    :param colorComponentInput: The color component to be converted. Must be in range [0.0, 1.0].
    :rtype: int
    :return: The converted 16-bit color component in range [0, 65535].
    
    
    """
    ...

def ColorComponent16BitToFloat(colorComponentInput: int) -> float:
    """    
    Converts a RGB 16-bit color component (range [0, 65535]) to float in range [0.0, 1.0].
    
    :type colorComponentInput: int
    :param colorComponentInput: The 16-bit color component to be converted. Must be in range [0, 65535].
    :rtype: float
    :return: The converted color component in range [0.0, 1.0].
    
    
    """
    ...

def ColorFloatTo16Bit(floatColor: Vector) -> List[Any]:
    """    
    Converts a RGB float color in range [0.0, 1.0] to 16-bit color (range [0, 65535]).
    
    :type floatColor: c4d.Vector
    :param floatColor: The color to be converted. Must be in range [0.0, 1.0].
    :rtype: list(int, int, int)
    :return: The converted 16-bit red, green and blue color components.
    
    
    """
    ...

def Color16BitToFloat(red: int, green: int, blue: int) -> None:
    """    
    Converts a RGB 16-bit color (range [0, 65535]) to float color in range [0.0, 1.0].
    
    :type red: int
    :param red: The 16-bit color component to be converted. Must be in range [0, 65535].
    :type green: int
    :param green: The 16-bit color component to be converted. Must be in range [0, 65535].
    :type blue: int
    :param blue: The 16-bit color component to be converted. Must be in range [0, 65535].
    :rtype: :class:`c4d.Vector`
    :return: The converted float color in range [0.0, 1.0].
    
    
    """
    ...

def ColorKelvinTemperatureToRGB(kelvinDegree: float, tint: float) -> None:
    """    
    Converts color Kelvin temperature to RGB value.
    
    :type kelvinDegree: float
    :param kelvinDegree: The Kelvin temperature value in Kelvin degrees. Useful range: [1000.0, 10000.0] deg K
    :type tint: float
    :param tint: Offsets the color temperature from green (negative value) to magenta (positive value). Set to 0.0 to disable tinting. Value will be clamped to range [-1.0, 1.0].
    :rtype: :class:`c4d.Vector`
    :return: The converted RGB color value.
    
    
    """
    ...

def ColorHarmonyGetComplementary(color: Vector, ryb: bool) -> None:
    """    
    Generates a complementary color harmony palette from *color*. Contains the input color and its opposite color in a color wheel.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The complementary color harmony palette.
    
    
    """
    ...

def ColorHarmonyGetSplitComplementary(color: Vector, ryb: bool) -> None:
    """    
    | Generates a split complementary color harmony palette from *color*. Contains the input color and the 2 analogous colors to its complementary color.
    | The complementary color is calculated rotating 180 deg the hue of the original color in HSV space.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The split complementary color harmony palette.
    
    
    """
    ...

def ColorHarmonyGetTetradic(color: Vector, ryb: bool) -> None:
    """    
    Generates a tetradric color harmony palette. The rectangle or Tetradic color scheme uses four colors arranged into 2 complementary pairs.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The tetradric color harmony palette.
    
    
    """
    ...

def ColorHarmonyGetAnalogous(color: Vector, colorCount: int, ryb: bool) -> None:
    """    
    Generates an Analogous Color Harmony palette. Analogous color schemes use colors that are next to each other on the color wheel, i.e. 30 deg far away.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type colorCount: int
    :param colorCount: Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate and smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The analogous color harmony palette.
    
    
    """
    ...

def ColorHarmonyGetEquiangular(color: Vector, colorCount: int, ryb: bool) -> None:
    """    
    Generates an Equiangular Color Harmony palette. All colors are evenly arranged around the color wheel.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type colorCount: int
    :param colorCount: Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The equiangular color harmony palette.
    
    
    """
    ...

def ColorHarmonyRotateColor(color: Vector, colorCount: int, angle: int, ryb: bool) -> None:
    """    
    Generates a palette composed by a defined amount of colors whose hue is separated by a defined angle in HSV color space.
    
    :type color: c4d.Vector
    :param color: The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type colorCount: int
    :param colorCount: Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.
    :type angle: int
    :param angle: Rotation angle in radians. See :func:`c4d.utils.Deg`
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The palette.
    
    
    """
    ...

def ColorHarmonyInterpolateColors(color1: Vector, color2: Vector, colorCount: int, ryb: bool) -> None:
    """    
    Generates a palette composed by a defined amount of colors interpolated between *color1* and *color2* in HSV color space. All 3 HSV values will be interpolated.
    
    :type color1: c4d.Vector
    :param color1: The first generator color. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type color2: c4d.Vector
    :param color2: The second generator color. This color will be added to the resulting palette as well, and converted to RYB space if enabled.
    :type colorCount: int
    :param colorCount: Number of colors to generate. Because the 2 input colors are added as well, the resulting palette will have *colorCount* + 2 colors.
    :type ryb: bool
    :param ryb:
    
    | Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.
    | RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.
    | This means different RGB values could be converted to the same RYB value.
    
    :rtype: list of :class:`c4d.Vector`
    :return: The palette.
    
    
    """
    ...

def ColorSwatchPresetExists(name: str, urls: Optional[List[Any]] = ...) -> bool:
    """    
    Checks if any preset with the given *name* exists in user's color swatch preset directory, including subdirectories.
    
    :type name: str
    :param name: The preset name.
    :type urls: list
    :param urls: Optionally set a list that will be filled with all urls pointing to a color swatch preset with the given *name*.
    :rtype: bool
    :return: **True** if any preset with the given name was found, otherwise **False**.
    
    
    """
    ...

def ValidColorSwatchPreset(url: str) -> bool:
    """    
    Checks if the given URL points to a valid color swatch preset.
    
    :type url: str
    :param url: The url to check.
    :rtype: bool
    :return: **True** if the URL points to a valid color swatch preset, otherwise **False**.
    
    
    """
    ...

def GetColorSwatchPresetDirectory() -> str:
    """    
    Gets the user's default color swatch preset directory.
    
    :rtype: str
    :return: The preset directory.
    
    
    """
    ...

