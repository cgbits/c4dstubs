from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import GeListNode, BaseDraw, BaseTag, Matrix, BaseContainer, Vector, DescID, HandleInfo, Description, BaseObject, AliasTrans, SplineObject, BaseList2D, BaseShader
from c4d.documents import BaseDocument
from c4d.bitmaps import BaseBitmap
from c4d.modules.mograph import FalloffDataData
from c4d.threading import BaseThread
from c4d.gui import EditorWindow, SubDialog
from c4d.modules.sculpting import BrushDabData, SculptBrushParams
from c4d.modules.render import InitRenderStruct, ChannelData
from c4d.storage import ByteSeq


class PriorityList(object):
    def Add(self, node: GeListNode, priority: int, flags: int) -> None:
        """    
        Adds an execution point for *node* and the time specified by *priority*.
        
        :type node: c4d.GeListNode
        :param node: The node to execute.
        :type priority: int
        :param priority: The priority in the pipeline. Standard values are:
        
        .. include:: /consts/EXECUTIONPRIORITY.rst
        :start-line: 3
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/EXECUTIONFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    

class GeResource(object):
    def __init__(self) -> None:
        """    
        Creates a new resource object.
        
        :rtype: c4d.plugins.GeResource
        :return: The new resource object.
        
        
        """
        ...
    
    def Init(self, path: str) -> bool:
        """    
        Initializes the resources from their files in the 'res' folder.
        
        :type path: str
        :param path: The root directory of the plugin's folder to find the 'res' folder.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitAsGlobal(self) -> bool:
        """    
        Lets access the `Cinema 4D` main application string resource.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def LoadString(self, id: int) -> str:
        """    
        Loads a string from the string resource file.
        
        .. seealso::
        
        :func:`GeLoadString() <c4d.plugins.GeLoadString>`
        
        :type id: int
        :param id: The ID for the string in the resource file.
        :rtype: str
        :return: The string from the resource file for the passed *id*.
        
        
        """
        ...
    

class BasePlugin(BaseList2D):
    def GetFilename(self) -> str:
        """    
        Returns the filename of the plugin.
        
        :rtype: str
        :return: The filename of the plugin.
        
        
        """
        ...
    
    def GetInfo(self) -> int:
        """    
        Flags for the plugin.
        
        :rtype: int
        :return: The flags:
        
        .. include:: /consts/PLUGINFLAG.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetID(self) -> int:
        """    
        Gets the plugin ID.
        
        :rtype: int
        :return: The plugin ID.
        
        
        """
        ...
    

class BaseDrawHelp(object):
    def __init__(self, bd: BaseDraw, doc: BaseDocument) -> None:
        """    
        Create a new help object for base draw *bd*.
        
        :type bd: c4d.BaseDraw
        :param bd: The base draw the :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` is assigned to.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document of the base draw *bd*.
        :rtype: c4d.plugins.BaseDrawHelp
        :return: The new base draw help object.
        
        
        """
        ...
    
    def GetDocument(self) -> BaseDocument:
        """    
        Returns the relevant document for the current draw operation, i.e. the currently active document. Never returns **None**.
        
        :rtype: c4d.documents.BaseDocument
        :return: The relevant document.
        
        
        """
        ...
    
    def GetActiveTag(self) -> BaseTag:
        """    
        Returns the currently active tag, or **None** if no tag is active (similar to :meth:`BaseDocument.GetActiveTag` but more efficient since the active tag is cached).
        
        :rtype: c4d.BaseTag
        :return: The active tag.
        
        
        """
        ...
    
    def GetMg(self) -> Matrix:
        """    
        Returns the global matrix of the object to be drawn (similar to :meth:`BaseObject.GetMg` but more efficient since the matrix is cached).
        
        :rtype: c4d.Matrix
        :return: The global matrix.
        
        
        """
        ...
    
    def SetMg(self, mg: Matrix) -> None:
        """    
        Sets the matrix returned by :meth:`GetMg`.
        
        :type mg: c4d.Matrix
        :param mg: New matrix.
        
        
        """
        ...
    
    def GetDisplay(self) -> BaseContainer:
        """    
        Retrieves a container with the display mode for the object to be drawn. See `Tdisplay.h` for values.
        
        :rtype: c4d.BaseContainer
        :return: The display mode container.
        
        
        """
        ...
    
    def SetDisplay(self, bc: BaseContainer) -> None:
        """    
        Sets the display mode for the object to be drawn. See `Tdisplay.h` for values.
        
        .. versionadded:: R19
        
        :type bc: c4d.BaseContainer
        :param bc: The new display mode container.
        
        
        """
        ...
    
    def GetViewSchedulerFlags(self) -> int:
        """    
        Returns the flags which have been passed to :func:`DrawViews() <c4d.DrawViews>`.
        
        :rtype: int
        :return: Flags:
        
        .. include:: /consts/DRAWFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsActive(self) -> bool:
        """    
        Checks if the current object is active.
        
        .. versionadded:: R14.014
        
        :rtype: bool
        :return: **True** if the current object is active.
        
        
        """
        ...
    
    def IsHighlight(self) -> bool:
        """    
        Checks if the current object is highlighted (i.e. when the user has moved the mouse over it).
        
        .. versionadded:: R14.014
        
        :rtype: bool
        :return: **True** if the current object is highlighted.
        
        
        """
        ...
    

class BaseData(object):
    ...

class BitmapLoaderData(BaseData):
    def Identify(self, name: str, probe: Any, size: int) -> bool:
        """    
        Override - Identify the file type as one that can be loaded using this plugin. If possible, the file should not be identified through the suffix, but through the *probe* data.
        
        :type name: str
        :param name: The name of the file.
        :type probe: buffer
        :param probe: The start of a small chunk of data from the start of the file for testing this file type. Usually the *probe* size is 1024 bytes. The buffer is just accessible in this method.
        :type size: int
        :param size: The size of the chunk for testing this file type.
        :rtype: bool
        :return: **True** if your plugin recognises this file.
        
        
        """
        ...
    
    def Load(self, name: str, bm: BaseBitmap, frame: int) -> int:
        """    
        Override - Load the image file into the bitmap.
        
        .. warning:: **Never** call any GUI commands in this method. Use the return value to inform the user about the state of the rendering.
        
        :type name: str
        :param name: The filename of the file.
        :type bm: c4d.bitmaps.BaseBitmap
        :param bm: The bitmap. Please call :meth:`BaseBitmap.Init` or :meth:`BaseBitmap.InitWith` before, to initialize the size.
        :type frame: int
        :param frame: The frame number for formats containing multiple images in a file such as Quicktime or AVI.
        :rtype: int
        :return: The return values:
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetSaver(self) -> int:
        """    
        Return the ID of the corresponding bitmap saver, if there is one.
        
        :rtype: int
        :return: The plugin ID of the corresponding :class:`BitmapSaverData <c4d.plugins.BitmapSaverData>`, or **None** if there is not one.
        
        
        """
        ...
    
    def GetInformation(self, name: str) -> Tuple[int, int]:
        """    
        Implement this function if you want to support loading movies.
        
        :type name: str
        :param name: The name of the file to check.
        :rtype: tuple(int, int)
        :return: The `number of frames` and `fps` information for *name*.
        
        
        """
        ...
    

class BitmapSaverData(BaseData):
    def Edit(self, data: BaseContainer) -> bool:
        """    
        Override - Open the settings dialog for this import/export filter.
        
        :type data: c4d.BaseContainer
        :param data: The settings for your plugin.
        :rtype: bool
        :return: **True** if the dialog opened successfully.
        
        
        """
        ...
    
    def Save(self, fn: str, bmp: BaseBitmap, data: BaseContainer, savebits: int) -> int:
        """    
        Override - Save the bitmap to a file.
        
        .. warning::
        
        **Never** call any GUI commands in this method. Use the return value to inform the user about the state of the rendering.
        
        :type fn: str
        :param fn: The filename of the file to save.
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The bitmap to save the image from.
        :type data: c4d.BaseContainer
        :param data: The settings for your plugin. These settings are stored with the general preferences.
        :type savebits: int
        :param savebits: Flags for the save:
        
        .. include:: /consts/SAVEBIT.rst
        :start-line: 3
        
        :rtype: int
        :return: The return values:
        
        .. include:: /consts/IMAGERESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMaxAlphas(self, data: BaseContainer) -> int:
        """    
        Get the maximum number of alpha channels this format supports with the current settings.
        
        :type data: c4d.BaseContainer
        :param data: The settings for your plugin. These settings are stored with the general preferences.
        :rtype: int
        :return: The number of alpha channels.
        
        
        """
        ...
    
    def GetMaxResolution(self, layers: bool) -> int:
        """    
        Overload this to return the maximum resolution of the image format.
        
        :type layers: bool
        :param layers: **True** if layers are to be saved, otherwise **False**.
        :rtype: int
        :return: The maximum resolution supported by the image format.
        
        
        """
        ...
    

class CommandData(BaseData):
    def Execute(self, doc: BaseDocument) -> bool:
        """    
        Override - Called when the plugin is selected by the user.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document when the command was selected.
        :rtype: bool
        :return: **True** if the command was executed successfully, otherwise **False**.
        
        
        """
        ...
    
    def RestoreLayout(self, secret: Any) -> bool:
        """    
        | Override - Called by Cinema 4D when loading a layout and restoring async dialogs.
        | If this function is not implemented Cinema 4D will create an empty "???" dialog.
        
        :type secret: PyCObject
        :param secret: An internal hook. Pass it to :meth:`GeDialog.Restore`
        :rtype: bool
        :return: **True** if the dialog was restored, otherwise **False**.
        
        
        """
        ...
    
    def Message(self, type: int, data: Any) -> bool:
        """    
        Override - Called when the command receives messages.
        
        .. seealso:: :doc:`MSG </consts/MSG_PLUGINS>` for the information on the messages type, data and input/output.
        
        :type type: int
        :param type: The message type.
        :type data: any
        :param data: The message data.
        :rtype: bool
        :return: Depends on the message *type*.
        
        
        """
        ...
    
    def GetSubContainer(self, doc: BaseDocument, submenu: BaseContainer) -> bool:
        """    
        | Override - Create dynamic subcontainer entries for a menu.
        | The menu entries on the top level will all be placed at the point where the command plugin was placed.
        | To create a submenu, place the entries as subcontainers in the returned container with ID 0. In the subcontainer, place a string with ID 1 to name it.
        
        .. code-block:: python
        
        bc = BaseContainer()
        bc.SetString(1, "Submenu Test")
        bc.SetString(1000, "First Entry")
        submenu.InsData(0, bc)
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document when the command was selected.
        :type submenu: c4d.BaseContainer
        :param submenu: Fill this with the submenu structure.
        :rtype: bool
        :return: **True** if you put anything in the container, otherwise **False**.
        
        
        """
        ...
    
    def GetScriptName(self) -> str:
        """    
        Override - Return the script name of the command data. If this function is implemented, the command is stored by name rather than by ID in layouts, shortcuts and menus.
        
        :rtype: str
        :return: Script name.
        
        
        """
        ...
    
    def ExecuteSubID(self, doc: BaseDocument, subid: int) -> bool:
        """    
        Override - Execute the command plugin with the *subid* that was given by :meth:`GetSubContainer`.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document when the command was selected.
        :type subid: int
        :param subid: Sub command ID.
        :rtype: bool
        :return: **True** if the message was processed.
        
        
        """
        ...
    
    def ExecuteOptionID(self, doc: BaseDocument, plugid: int, subid: int) -> bool:
        """    
        Override - Execute the command plugin when the user calls it through its options dialog.
        
        .. image:: /_imgs/modules/plugins/commanddata_commandoptions.png
        
        .. note::
        
        Plugins must be :func:`registered <c4d.plugins.RegisterCommandPlugin>` with *PLUGINFLAG_COMMAND_OPTION_DIALOG* set.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document when the command was selected.
        :type plugid: int
        :param plugid: The command's plugin ID.
        :type subid: int
        :param subid: Only available for plugins that have sub-IDs (which normally are called using :meth:`ExecuteSubID`).
        :rtype: bool
        :return: **True** if the command was executed successfully, otherwise **False**.
        
        
        """
        ...
    
    def GetState(self, doc: BaseDocument) -> int:
        """    
        | Override - Called to get the state of the command.
        | This affects how it is displayed in menus or toolbars.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document that is currently active in the editor.
        :rtype: int
        :return: A combination of the state flags:
        
        .. include:: /consts/CMD.rst
        :start-line: 3
        
        
        """
        ...
    

class FalloffData(BaseData):
    def Init(self, falldata: FalloffDataData, bc: BaseContainer) -> bool:
        """    
        Called when the falloff is first created.
        
        :type falldata: c4d.modules.mograph.FalloffDataData
        :param falldata: Falloff data information.
        :type bc: c4d.BaseContainer
        :param bc: Falloff's basecontainer; normally this is the owning object's basecontainer.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitFalloff(self, bc: BaseContainer, falldata: FalloffDataData) -> bool:
        """    
        Called just before sampling. Allows you to set up any necessary data in *falldata* or *bc*.
        
        :type bc: c4d.BaseContainer
        :param bc: Falloff's basecontainer; normally this is the owning object's basecontainer.
        :type falldata: c4d.modules.mograph.FalloffDataData
        :param falldata: Falloff data information.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Sample(self, p: Vector, data: FalloffDataData) -> float:
        """    
        Called to sample any point.
        
        .. note::
        
        To get *p* in world coordinates multiply it by :attr:`data.mat <FalloffDataData.mat>`.
        
        :type p: c4d.Vector
        :param p: The position of the point to sample in falloff space.
        :type data: c4d.modules.mograph.FalloffDataData
        :param data: Falloff data information.
        :rtype: float
        :return: The falloff value.
        
        
        """
        ...
    
    def FreeFalloff(self, falldata: FalloffDataData) -> None:
        """    
        Called when the falloff object is freed.
        
        :type falldata: c4d.modules.mograph.FalloffDataData
        :param falldata: Falloff data information.
        
        
        """
        ...
    
    def CheckDirty(self, bc: BaseContainer) -> bool:
        """    
        :type bc: c4d.BaseContainer
        :param bc: Falloff's basecontainer; normally this is the owning object's basecontainer.
        :rtype: bool
        :return: Dirty state.
        
        
        """
        ...
    
    def GetDVisible(self, id: DescID, bc: BaseContainer, desc_bc: BaseContainer) -> bool:
        """    
        Called to change the visibility of any element in the description; just return **True** or **False** for the *id*.
        
        :type id: c4d.DescID
        :param id: The ID being evaluated.
        :type bc: c4d.BaseContainer
        :param bc: Falloff's basecontainer; normally this is the owning object's basecontainer.
        :type desc_bc: c4d.BaseContainer
        :param desc_bc: The description element's container.
        :rtype: bool
        :return: Visibility of *id*.
        
        
        """
        ...
    
    def GetHandleCount(self, bc: BaseContainer, data: Any) -> int:
        """    
        Called to get the number of handles the falloff has. Part of the automated handle interface.
        
        :type bc: c4d.BaseContainer
        :param bc: Falloff's container; normally this is the owning falloff's basecontainer.
        :type falldata: c4d.modules.mograph.FalloffDataData
        :param falldata: Falloff data information.
        :rtype: int
        :return: The number of handles.
        
        
        """
        ...
    
    def GetHandle(self, bc: BaseContainer, i: int, info: HandleInfo, data: FalloffDataData) -> Vector:
        """    
        Called to get the information for handle at index *i*. Part of the automated handle interface.
        
        :type bc: c4d.BaseContainer
        :param bc: Falloff's container; normally this is the owning falloff's basecontainer.
        :type i: int
        :param i: The handle index.
        :type info: c4d.HandleInfo
        :param info: The handle info.
        :type data: c4d.modules.mograph.FalloffDataData
        :param data: Falloff data information.
        :rtype: c4d.Vector
        :return: The current local position of the handle with index *i*.
        
        
        """
        ...
    
    def SetHandle(self, bc: BaseContainer, i: int, p: Vector, data: FalloffDataData) -> None:
        """    
        | Called to set the information for handle at index *i*. Part of the automated handle interface.
        | Called when the user has moved handle *i* to position *p*. Update the falloff's internal data accordingly (e.g. parameter values etc).
        
        :type bc: c4d.BaseContainer
        :param bc: Falloff's container; normally this is the owning falloff's basecontainer.
        :type i: int
        :param i: The handle index.
        :type p: c4d.Vector
        :param p: The new position for handle *i*.
        :type data: c4d.modules.mograph.FalloffDataData
        :param data: Falloff data information.
        
        
        """
        ...
    
    def Draw(self, data: FalloffDataData, drawpass: int, bd: BaseDraw, bh: BaseDrawHelp) -> int:
        """    
        For allowing you to draw the falloff in the viewport. You should use these predefined color constants:
        
        .. include:: /consts/FALLOFF.rst
        :start-line: 3
        
        .. note::
        
        This function is called in a thread context. Please see the :ref:`important information <threading-information>` about threading.
        
        :type data: c4d.modules.mograph.FalloffDataData
        :param data: Falloff data information.
        :type drawpass: int
        :param drawpass: One of the following:
        
        .. include:: /consts/DRAWPASS.rst
        :start-line: 3
        
        .. warning::
        
        Only draw in *DRAWPASS_HIGHLIGHTS* if you **really** know what you are doing. Otherwise **always** check the *drawpass* and then **do not** draw if it is *DRAWPASS_HIGHLIGHTS*.
        
        Here is an example.
        
        .. code-block:: python
        
        def Draw(self, data, drawpass, bd, bh):
        
        if drawpass==c4d.DRAWPASS_HIGHLIGHTS:
        return False
        
        # Put here your drawing operations
        
        return True
        
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` editor's view.
        :rtype: int
        :return: Success of drawing into the editor view:
        
        .. include:: /consts/DRAWRESULT.rst
        :start-line: 3
        
        .. versionchanged:: R18.011 Changed to *DRAWRESULT*. Returning a bool is still supported for backward compatibility.
        
        
        """
        ...
    
    def Message(self, type: int, bc: BaseContainer, m_data: Any) -> bool:
        """    
        Called when the falloff receives messages.
        
        .. seealso:: :doc:`MSG </consts/MSG_PLUGINS>` for the information on the messages type, data and input/output.
        
        :type type: int
        :param type: The message type:
        :type bc: c4d.BaseContainer
        :param bc: Falloff's basecontainer; normally this is the owning object's basecontainer.
        :type m_data: any
        :param m_data: The message data.
        :rtype: bool
        :return: Depends on the message type.
        
        
        """
        ...
    

class MessageData(BaseData):
    def GetTimer(self) -> int:
        """    
        | Override - Called to return a time in milliseconds to receive timer messages (*MSG_TIMER*) with that interval in :meth:`CoreMessage()`.
        | This method is queried again after each message.
        
        :rtype: int
        :return: The timer interval in milliseconds, or `0` for no timer messages.
        
        
        """
        ...
    
    def CoreMessage(self, id: int, bc: BaseContainer) -> bool:
        """    
        Override - Called to receive core messages.
        
        :type id: int
        :param id: The core message ID:
        
        .. include:: /consts/EVMSG.rst
        :start-line: 3
        
        :type bc: c4d.BaseContainer
        :param bc: The core message container.
        :rtype: bool
        :return: Currently not used but a bool has to be returned.
        
        
        """
        ...
    

class SculptBrushToolData(BaseData):
    def InitTool(self, doc: BaseDocument, data: BaseContainer, bt: BaseThread) -> bool:
        """    
        Called each time the tool is selected.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The original tool settings container.
        :type bt: c4d.threading.BaseThread
        :param bt: The thread this method is being called from.
        :rtype: bool
        :return: **True** if there was no error, otherwise **False**.
        
        
        """
        ...
    
    def FreeTool(self, doc: BaseDocument, data: BaseContainer) -> bool:
        """    
        Called each time the user chooses another tool.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The original tool settings container.
        :rtype: bool
        :return: **True** if there was no error, otherwise **False**.
        
        
        """
        ...
    
    def DoCommand(self, mode: int, arr: Any, bc: BaseContainer, doc: BaseDocument, flags: int) -> None:
        """    
        Called by :func:`SendModelingCommand() <c4d.utils.SendModelingCommand>` to perform a command.
        
        :type mode: int
        :param mode: The modeling mode:
        
        .. include:: /consts/MODELINGCOMMANDMODE.rst
        :start-line: 3
        
        :type arr: list of :class:`BaseList2D <c4d.BaseList2D>`
        :param arr: The input objects.
        :type bc: c4d.BaseContainer
        :param bc: The modeling command settings container.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the operation.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/MODELINGCOMMANDFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitDefaultSettings(self, doc: BaseDocument, data: BaseContainer) -> None:
        """    
        Called to let initialize the default tool settings in *data*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        
        
        """
        ...
    
    def KeyboardInput(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, win: EditorWindow, msg: BaseContainer) -> bool:
        """    
        Called when the user types something in any of the editor views.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type win: c4d.gui.EditorWindow
        :param win: The :class:`EditorWindow <c4d.gui.EditorWindow>` object for the active editor view.
        :type msg: c4d.BaseContainer
        :param msg: The original message container.
        :rtype: bool
        :return: **False** if a problem occured.
        
        
        """
        ...
    
    def MouseInput(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, win: EditorWindow, msg: BaseContainer) -> bool:
        """    
        Called when the user clicks with the mouse in any of the editor views.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type win: c4d.gui.EditorWindow
        :param win: The :class:`EditorWindow <c4d.gui.EditorWindow>` object for the active editor view.
        :type msg: c4d.BaseContainer
        :param msg: The original message container.
        :rtype: bool
        :return: **False** if a problem occured.
        
        
        """
        ...
    
    def GetState(self, doc: BaseDocument) -> int:
        """    
        Called to check if the tool should be enabled, checked or not.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document the tool is being used in.
        :rtype: int
        :return: The return flags:
        
        .. include:: /consts/CMD.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetCursorInfo(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, x: float, y: float, bc: BaseContainer) -> bool:
        """    
        Called when the cursor is over the editor window to get the state of the mouse pointer.
        
        The bubble help and cursor can be set using.
        
        .. code-block:: python
        
        bc.SetString(c4d.RESULT_BUBBLEHELP, "My Tools Help")
        bc.SetLong(c4d.RESULT_CURSOR, c4d.MOUSE_POINT_HAND)
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type x: float
        :param x: The x coordinate of the mouse cursor relative to the top-left of the currently active editor view.
        :type y: float
        :param y: The y coordinate of the mouse cursor relative to the top-left of the currently active editor view.
        :type bc: c4d.BaseContainer
        :param bc: The container to store the result in. Use the following container IDs:
        
        .. include:: /consts/RESULT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **False** if a problem occured.
        
        
        """
        ...
    
    def Draw(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, bh: BaseDrawHelp, bt: BaseThread, flags: int) -> int:
        """    
        Called when the editor view is updated so you can display graphics for your tool in the view.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd:  The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` object for the active editor view.
        :type bt: c4d.threading.BaseThread
        :param bt: The thread this method is being called from.
        :type flags: int
        :param flags: The flags are:
        
        .. include:: /consts/TOOLDRAWFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: The values for this are:
        
        .. include:: /consts/TOOLDRAW.rst
        :start-line: 3
        
        
        """
        ...
    
    def AllocSubDialog(self, bc: BaseContainer) -> SubDialog:
        """    
        Called to get a GUI for the Active Tool window. Return an instance of your tool's dialog.
        
        :type bc: c4d.BaseContainer
        :param bc: Currently not used.
        :rtype: c4d.gui.SubDialog
        :return: The allocated subdialog.
        
        
        """
        ...
    
    def Message(self, doc: BaseDocument, data: BaseContainer, type: int, t_data: Any) -> bool:
        """    
        Called when the tool receives messages.
        
        .. seealso:: :doc:`MSG </consts/MSG_PLUGINS>` for the information on the messages type, data and input/output.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The current tool data.
        :type type: int
        :param type: The message type.
        :type t_data: any
        :param t_data: Depends on *type*.
        :rtype: bool
        :return: Depends on the message type.
        
        
        """
        ...
    
    def GetToolPluginId(self) -> int:
        """    
        Return the unique id for the tool plugin as obtained from www.plugincafe.com.
        
        :rtype: int
        :return: The tool plugin ID.
        
        
        """
        ...
    
    def GetResourceSymbol(self) -> str:
        """    
        Return the name of the resource file for this brush.
        
        :rtype: str
        :return: The name of the resource file for this brush.
        
        
        """
        ...
    
    def StartStroke(self, strokeCount: int, data: BaseContainer) -> None:
        """    
        | :meth:`StartStroke` is called once at the start of the stroke. It passes the total number of instances of the brush that will be drawn.
        | The number of instances will change depending on the symmetry mirroring and radial settings.
        |
        | Use this method to setup any data on your brush that you might want to access from within your :meth:`ApplyDab` override via :meth:`BrushDabData.GetBrush`.
        |
        | Calling order for brush stroke methods:
        
        - :meth:`StartStroke`: Called once at the start of the stroke.
        - :meth:`StartStrokeInstance`: Call for each instance of a stroke that will be used. Use this to initialize any data you might need for the duration of the entire brush stroke.
        - :meth:`StartSymmetry`: Called once before all the instances are about to be drawn for a small mouse movement. This will be called MANY times during a stroke as the mouse moves over the model.
        - :meth:`StartStrokeInstanceDabs`: Called once before a bunch of consecutive dabs will be draw for a single instance (mirrored brush).
        - :meth:`StartDab`: Called for each dab that needs to be drawn between 2 mouse locations on the object for a single brush stroke instance.
        - :meth:`ApplyDab` gets called to process the dab.
        - :meth:`EndDab`
        - :meth:`EndStrokeInstanceDabs`
        - :meth:`EndSymmetry`: Called once when all symmetrical strokes have finished.
        - :meth:`EndStrokeInstance`: Called for each instance of a stroke that was used.
        - :meth:`EndStroke`
        
        .. note::
        
        **StartStroke()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeCount: int
        :param strokeCount: The number of instances of the brush that will be drawn.
        :type data: c4d.BaseContainer
        :param data: The data for the brush.
        
        
        """
        ...
    
    def StartStrokeInstance(self, strokeInstanceID: int) -> None:
        """    
        | Called after :meth:`StartStroke`. Called once for each brush instance at the start of a stroke.
        | The number of instances will change depending on the symmetry mirroring and radial settings.
        |
        | Use this method to allocate any data you may want to access during a brush stroke, that may be specific for each individual instance.
        | Setup here any data on your brush that you might want to access from within your :meth:`ApplyDab` override via :meth:`BrushDabData.GetBrush`.
        
        .. note::
        
        **StartStrokeInstance()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def StartSymmetry(self) -> None:
        """    
        | Called directly before each individual brush instance is about to be handled.
        | Between this method and :meth:`EndSymmetry` all the dabs for each instance will be drawn from one mouse location on the surface of the model to another.
        | This method will be called every time the user moves its mouse over the object on the screen to indicate that a new batch of dabs is going to be drawn.
        |
        | Use this method to setup any data on your brush that you might want to access from within your :meth:`ApplyDab` override via :meth:`BrushDabData.GetBrush`.
        
        .. note::
        
        **StartSymmetry()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        
        """
        ...
    
    def StartStrokeInstanceDabs(self, strokeInstanceID: int) -> None:
        """    
        | Called before all the dabs for a single instance are about to be drawn.
        | After this call all the dabs for just one instance of the brush on the surface will interpolate between the 2 mouse locations on the object then draw all the dabs for that instance.
        |
        | Use this method to setup any data on your brush that you might want to access from within your :meth:`ApplyDab` override via :meth:`BrushDabData.GetBrush`.
        
        .. note::
        
        **StartStrokeInstanceDabs()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def StartDab(self, strokeInstanceID: int) -> None:
        """    
        | Called before the :meth:`ApplyDab` override is called which will then process the dab.
        |
        | Use this method to setup any data on your brush that you might want to access from within your :meth:`ApplyDab` override via :meth:`BrushDabData.GetBrush`.
        
        .. note::
        
        **StartDab()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def EndDab(self, strokeInstanceID: int) -> None:
        """    
        Called after :meth:`ApplyDab` function.
        
        .. note::
        
        **EndDab()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def EndStrokeInstanceDabs(self, strokeInstanceID: int) -> None:
        """    
        Called after all the dabs have been drawn for a single instance of the brush.
        
        .. note::
        
        **EndStrokeInstanceDabs()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def EndSymmetry(self) -> None:
        """    
        Called after all the dabs for all the instances have been drawn for a single mouse movement on screen.
        
        .. note::
        
        **EndSymmetry()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        
        """
        ...
    
    def EndStrokeInstance(self, strokeInstanceID: int) -> None:
        """    
        | Called on mouse up after a brush stroke. This method is called once for each instance.
        | Use this method to delete any temporary data you may have allocated in your :meth:`StartStrokeInstance` override.
        
        .. note::
        
        **EndStrokeInstance()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        
        
        """
        ...
    
    def EndStroke(self) -> None:
        """    
        Called on mouse up after :meth:`EndStrokeInstance` has been called for each instance.
        
        .. note::
        
        **EndStroke()** will only be called if :meth:`SculptBrushParams.EnableBrushAccess` has been set to **True**.
        
        
        """
        ...
    
    def MouseData(self, strokeInstanceID: int, brushData: BaseContainer, md: Dict[str, Any]) -> None:
        """    
        Constantly receives data about the object underneath the mouse. This method will get called when you move the cursor over an object on screen and happens when the mouse button is up or down.
        
        .. versionadded:: R17.048
        
        .. note::
        
        **MouseData()** will only be called if :meth:`SculptBrushParams.EnableMouseData` has been set to **True**.
        
        :type strokeInstanceID: int
        :param strokeInstanceID: The ID of the brush instance being drawn.
        :type brushData: c4d.BaseContainer
        :param brushData: The BaseContainer data for the brush.
        :type md: dict
        :param md: The mouse data information for the current position of the mouse on the surface of the object:
        
        - "pObject": :class:`SculptObject <c4d.modules.sculpting.SculptObject>` The selected Object underneath the mouse.
        - "mouseCoord": :class:`Vector <c4d.Vector>` The screen coordinates for the mouse location in the current viewport.
        - "hitPoint": :class:`Vector <c4d.Vector>` The hitpoint on the surface of the model at the center of the brush dab.
        - "normal": :class:`Vector <c4d.Vector>` The normal on the surface of the model at the center of the brush dab.
        - "barryCoord": :class:`Vector <c4d.Vector>` The barycentric coordinates within the triangle for the hit polygon.
        - "polygon": int The Index of the hit polygon.
        - "mouseDrag": **True** if the mouse button is held down and being dragged in the viewport.
        - "distance": The distance from the mouse in local space to the surface of the object.
        - "isBackface": **True** if the polygon under the mouse is backfacing.
        
        
        """
        ...
    
    def OverwriteLoadedPresetSettings(self, data: BaseContainer) -> None:
        """    
        After a preset has been loaded this method will get called to allow the brush to disable or change any of the loaded settings if required.
        
        :type data: c4d.BaseContainer
        :param data: The settings for the loaded brush.
        
        
        """
        ...
    
    def PostInitDefaultSettings(self, doc: BaseDocument, data: BaseContainer) -> None:
        """    
        | When a brush is reset by the user, in the UI, then it sets it back to its defaults.
        | Afterwards this method is called so you can overwrite any of the standard brush settings with your own for this brush.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :type data: c4d.BaseContainer
        :param data: The settings for the loaded brush.
        
        
        """
        ...
    
    def GetEnabling(self, id: int) -> bool:
        """    
        Called internally by the sculpting system to check if an UI element is enabled or not.
        
        If this method is overridden then make sure to also check the return value of this method directly by calling `SculptBrushToolData.GetEnabling(id)` at the end.
        
        :type id: int
        :param id: The id of the UI element from the `.res` file.
        :rtype: bool
        :return: **True** if the element should be enabled, otherwise **False**.
        
        
        """
        ...
    
    def HandleFillTool(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, win: EditorWindow, msg: BaseContainer) -> bool:
        """    
        Private.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :type data: c4d.BaseContainer
        :param data: The brush data.
        :type bd: c4d.BaseDraw
        :param bd: The editor view the tool is being used in.
        :type win: c4d.gui.EditorWindow
        :param win: The editor window the tool is being used in.
        :type msg: c4d.BaseContainer
        :param msg: The mouse/tablet message data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def HandleNonModelPickMode(self) -> bool:
        """    
        Private. Do something special when the first mouse click is not on the model.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :type data: c4d.BaseContainer
        :param data: The brush data.
        :type bd: c4d.BaseDraw
        :param bd: The editor view the tool is being used in.
        :type win: c4d.gui.EditorWindow
        :param win: The editor window the tool is being used in.
        :type msg: c4d.BaseContainer
        :param msg: The mouse/tablet message data.
        :rtype: bool
        :return: **True** if handled, otherwise **False**. In the case where you wish to only handle the mouse click and not the mouse drag it can return **False**.
        
        
        """
        ...
    
    def DrawNonModelPickMode(self) -> bool:
        """    
        Private.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :type data: c4d.BaseContainer
        :param data: The brush data.
        :type bd: c4d.BaseDraw
        :param bd: The editor view the tool is being used in.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` object for the active editor view.
        :type bt: c4d.threading.BaseThread
        :param bt: The thread this method is being called from.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/TOOLDRAWFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def HasDrawMode(self, mode: int) -> bool:
        """    
        | Override to let the system know what draw modes the brush supports.
        | The system will call this method to check if a draw mode is supported by this brush. If the brush supports all the draw modes then it can just return **True**.
        | Otherwise you can specify which draw modes should be enabled by checking each of them.
        
        :type mode: int
        :param mode: The ID for the DrawMode. For example *MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LINE*.
        :rtype: bool
        :return: **True** if the draw *mode* is supported, otherwise **False**.
        
        
        """
        ...
    
    def ApplyDab(self, dab: BrushDabData) -> None:
        """    
        Called to modify the sculpt object. Implement the functionality of your brush here!
        
        :type dab: c4d.modules.sculpting.BrushDabData
        :param dab: The brush dab data.
        
        
        """
        ...
    

class ToolData(BaseData):
    def InitTool(self, doc: BaseDocument, data: BaseContainer, bt: BaseThread) -> bool:
        """    
        Override - Called each time the tool is selected.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The original tool settings container.
        :type bt: c4d.threading.BaseThread
        :param bt: The calling thread.
        :rtype: bool
        :return: **True** if there was no error, otherwise **False**.
        
        
        """
        ...
    
    def FreeTool(self, doc: BaseDocument, data: BaseContainer) -> None:
        """    
        Override - Called each time the user chooses another tool.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The original tool settings container.
        
        
        """
        ...
    
    def InitDefaultSettings(self, doc: BaseDocument, data: BaseContainer) -> None:
        """    
        Called to let you initialize the default tool settings in *data*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        
        
        """
        ...
    
    def MouseInput(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, win: EditorWindow, msg: BaseContainer) -> bool:
        """    
        Override - Called when the user clicks with the mouse in any of the editors views.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type win: c4d.gui.EditorWindow
        :param win: The :class:`EditorWindow <c4d.gui.EditorWindow>` object for the active editor view.
        :type msg: c4d.BaseContainer
        :param msg: The original message container.
        :rtype: bool
        :return: **False** if a problem occured during this function.
        
        
        """
        ...
    
    def KeyboardInput(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, win: EditorWindow, msg: BaseContainer) -> bool:
        """    
        Override - Called when the user types something in any of the editors views.
        
        .. note::
        
        Make sure that you only use this function when the user is somehow working with your plugin, so that other plugins can also use this hook when it is their turn.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type win: c4d.gui.EditorWindow
        :param win: The :class:`EditorWindow <c4d.gui.EditorWindow>` object for the active editor view.
        :type msg: c4d.BaseContainer
        :param msg: The original message container.
        :rtype: bool
        :return: **False** if a problem occured during this function.
        
        
        """
        ...
    
    def GetState(self, doc: BaseDocument) -> int:
        """    
        Called to check if the tool should be enabled, checked or not.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document the tool is being used in.
        :rtype: int
        :return: The return flags:
        
        .. include:: /consts/CMD.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetCursorInfo(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, x: float, y: float, bc: BaseContainer) -> bool:
        """    
        Called when the cursor is over editor window to get the state of the mouse pointer.
        
        .. seealso:: :maxongithub:`Py-LiquidPainter <plugins/py-liquid_painter_r12/py-liquid_painter_r12.pyp#L232>` change the cursor and the bubble help string.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The currently active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd: The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type x: float
        :param x: The x coordinate of the mouse cursor relative to the top-left of the currently active editor view.
        :type y: float
        :param y: The y coordinate of the mouse cursor relative to the top-left of the currently active editor view.
        :type bc: c4d.BaseContainer
        :param bc: The container to store the result in. Use the following container IDs:
        
        .. include:: /consts/RESULT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **False** if a problem occured during this function.
        
        
        """
        ...
    
    def Draw(self, doc: BaseDocument, data: BaseContainer, bd: BaseDraw, bh: BaseDrawHelp, bt: BaseThread, flags: int) -> int:
        """    
        Called when the editor view is updated so you can display graphics for your tool in the view.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type bd: c4d.BaseDraw
        :param bd:  The :class:`BaseDraw <c4d.BaseDraw>` object for the active editor view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The helper for the editor's view. The caller owns the pointed base draw helper.
        :type flags: int
        :param flags: The flags are:
        
        .. include:: /consts/TOOLDRAWFLAGS.rst
        :start-line: 3
        
        :type bt: c4d.threading.BaseThread
        :param bt: The calling thread.
        :rtype: int
        :return: The values for this are:
        
        .. include:: /consts/TOOLDRAW.rst
        :start-line: 3
        
        
        """
        ...
    
    def AllocSubDialog(self, bc: BaseContainer) -> SubDialog:
        """    
        Called to get a GUI for the Active Tool window. Return an instance of your tool's dialog.
        
        :type bc: c4d.BaseContainer
        :param bc: Currently not used.
        :rtype: c4d.gui.SubDialog
        :return: The allocated sub dialog.
        
        
        """
        ...
    
    def Message(self, doc: BaseDocument, data: BaseContainer, type: int, t_data: Any) -> bool:
        """    
        Called when the tool receives messages.
        
        .. seealso:: :doc:`MSG </consts/MSG_PLUGINS>` for the information on the messages type, data and input/output.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The current document.
        :type data: c4d.BaseContainer
        :param data: The current tool data.
        :type type: int
        :param type: The message type.
        :type t_data: any
        :param t_data: Depends on *type*.
        :rtype: bool
        :return: Depends on the message *type*.
        
        
        """
        ...
    
    def GetDDescription(self, doc: BaseDocument, data: BaseContainer, description: Description, flags: int) -> Union[bool, Tuple[bool, int]]:
        """    
        Called to add parameters to the description for the tool. Modify the passed description as needed and return the appropriate flags.
        
        .. versionadded:: R18.011
        
        .. note::
        
        If only a description resource is used it is not needed to overload :meth:`GetDDescription() <ToolData.GetDDescription>`.
        
        .. seealso:: :meth:`NodeData.GetDDescription`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type description: c4d.Description
        :param description: The description to add the parameters to.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_DESC.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, int): The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def GetDParameter(self, doc: BaseDocument, data: BaseContainer, id: DescID, flags: int) -> Union[bool, Tuple[bool, Any, int]]:
        """    
        | Called to override the reading of description parameters. Necessary for parameters that are not simply stored in the tool's container e.g. class members.
        | Return the parameter data and the appropriate flags if the right *id* is provided.
        
        .. versionadded:: R18.011
        
        .. note::
        
        If only a description resource is used it is not needed to overload :meth:`GetDParameter() <ToolData.GetDParameter>`.
        
        .. seealso:: :meth:`NodeData.GetDParameter`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_GET.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, any, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, any, int): The status (**True** if successful, otherwise **False**), parameter data and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def SetDParameter(self, doc: BaseDocument, data: BaseContainer, id: DescID, t_data: Any, flags: int) -> Union[bool, Tuple[bool, int]]:
        """    
        Called to override the writing of parameters. Read the passed *t_data* if the right *id* is provided, store the data and return the appropriate flags.
        
        .. versionadded:: R18.011
        
        .. note::
        
        If only a description resource is used it is not needed to overload :meth:`SetDParameter() <ToolData.SetDParameter>`.
        
        .. seealso:: :meth:`NodeData.SetDParameter`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type t_data: any
        :param t_data: The parameter data to set.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_SET.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, int): The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def GetDEnabling(self, doc: BaseDocument, data: BaseContainer, id: DescID, t_data: Any, flags: int, itemdesc: BaseContainer) -> bool:
        """    
        | Called to let decide which parameters should be enabled or disabled (ghosted).
        | This can be used both for parameters that are stored in the tool's container and for custom parameters.
        |
        | Just read the passed *t_data* if the right *id* was provided, and return **True** to enable the parameter or **False** to disable it depending on the value.
        |
        | And if the passed *id* element is not processed, include a call to the base class method as last return.
        
        .. code-block:: python
        
        return ToolData.GetDEnabling(self, doc, data, id, t_data, flags, itemdesc)
        
        .. versionadded:: R18.011
        
        .. seealso:: :meth:`NodeData.GetDEnabling`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type t_data: any
        :param t_data: The current data for the parameter.
        :type flags: int
        :param flags: Not used.
        :type itemdesc: c4d.BaseContainer
        :param itemdesc: The description, encoded to a container as described in :class:`c4d.Description`.
        :rtype: bool
        :return: **True** if the parameter should be enabled, otherwise **False**.
        
        .. note::
        
        It is recommended to include a call to the base class method as last return.
        
        
        """
        ...
    
    def TranslateDescID(self, doc: BaseDocument, data: BaseContainer, id: DescID) -> None:
        """    
        | Called by the Attribute Manager for every tool and every description ID.
        | Gives the opportunity to route a description ID in the description of a tool to another one.
        
        .. versionadded:: R18.011
        
        .. seealso:: :meth:`NodeData.TranslateDescID`
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type data: c4d.BaseContainer
        :param data: The tool settings container.
        :type id: c4d.DescID
        :param id: The source description ID.
        :rtype: bool or tuple(bool, :class:`DescID <c4d.DescID>`, :class:`C4DAtom <c4d.C4DAtom>`)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, :class:`DescID <c4d.DescID>`, :class:`C4DAtom <c4d.C4DAtom>`): The status (**True** if successful, otherwise **False**), target description ID and tool.
        
        
        """
        ...
    

class NodeData(BaseData):
    def InitAttr(self, host: BaseObject, type: Any, id: DescID) -> bool:
        """    
        Initializes an object's description parameter at *id* with its default value for the data *type*.
        
        Just call this method in the :meth:`Init` method of any node data class.
        
        .. code-block:: python
        
        import c4d
        
        def Init(self, node):
        self.InitAttr(node, float, [c4d.PY_TUBEOBJECT_RAD])
        self.InitAttr(node, float, [c4d.PY_TUBEOBJECT_IRADX])
        
        node[c4d.PY_TUBEOBJECT_RAD] = 200.0
        node[c4d.PY_TUBEOBJECT_IRADX] = 50.0
        
        .. seealso:: The :maxongithub:`Py-RoundedTube <plugins/py-rounded_tube_r13/py-rounded_tube_r13.pyp>` example and its `Init()` method.
        
        :type host: c4d.BaseObject
        :param host: The host object.
        :type type: any
        :param type: Just pass the type like *float*, *int*, :class:`PriorityData <c4d.PriorityData>`, etc.
        :type id: c4d.DescID
        :param id: The parameter description ID to initialize.
        :rtype: bool
        :return: **True** if the parameter could be successfully initialized, otherwise **False**.
        
        
        """
        ...
    
    def Init(self, node: GeListNode) -> bool:
        """    
        Override - Called when a new instance of the node plugin has been allocated.
        
        .. note::
        
        If your class has a constructor it is called as usual before this function, but at that time there's no node link established.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        .. warning::
        
        Please note, if you return **False**, the object will **not** be created.
        
        
        """
        ...
    
    def Free(self, node: GeListNode) -> None:
        """    
        Override - If your class has a destructor it is called as usual after this function.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        
        
        """
        ...
    
    def Read(self, node: GeListNode, hf: GeListNode, level: int) -> bool:
        """    
        | Override - Called when a node is loaded from a file.
        | Use this function to read any settings for your plugin that are not stored in the :class:`BaseContainer <c4d.BaseContainer>`.
        | You must read these settings from the :class:`HyperFile <c4d.storage.HyperFile>` such as.
        
        .. code-block:: python
        
        hf.ReadInt32(offset)
        hf.ReadBool(object_access)
        
        For future extensions of your plugin you should check the *level* and only read the appropriate values.
        
        .. code-block:: python
        
        if level >= 0:
        hf.ReadInt32(offset)
        hf.ReadBool(object_access)
        if level >= 1:
        hf->ReadFloat(a_new_feature)
        
        :meth:`Init` will have already been called before this function is called.
        
        .. note::
        
        | It is recommended to store as much as possible in the :class:`BaseContainer <c4d.BaseContainer>` as Cinema 4D will handle the reading of those values automatically.
        | Only use member variables when necessary.
        
        .. important::
        
        | If you implement at least one of :meth:`Read`, :meth:`Write` and :meth:`CopyTo`, you must usually implement all three.
        | Otherwise data might be lost.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type hf: c4d.GeListNode
        :param hf: The hyper file to read the data from.
        :type level: int
        :param level:
        
        | The plugin level is similar to a version number for your settings.
        | The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.
        
        As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.
        
        .. important::
        
        For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.
        
        .. note::
        
        If you only use containers for all your values, you do not have to deal with *level*.
        
        :rtype: bool
        :return: **True** if the data was read successfully, otherwise **False**.
        
        
        """
        ...
    
    def Write(self, node: GeListNode, hf: GeListNode) -> bool:
        """    
        | Override - Called when a node is saved to a file.
        | Use this function to write any settings for your plugin that are not stored in the :class:`BaseContainer <c4d.BaseContainer>`.
        | You must read these settings from the :class:`HyperFile <c4d.storage.HyperFile>` such as.
        
        .. code-block:: python
        
        hf.WriteInt32(offset)
        hf.WriteBool(object_access)
        
        For future extensions of your plugin you should make sure to introduce a new level (See :meth:`Read`) when writing new values.
        
        .. code-block:: python
        
        // Level 0
        hf.WriteInt32(offset)
        hf.WriteBool(object_access)
        
        // Level 1
        hf.WriteFloat(a_new_feature)
        
        :meth:`Free` will be called after this function is called.
        
        .. note::
        
        | It is recommended to store as much as possible in the :class:`BaseContainer <c4d.BaseContainer>` as Cinema 4D will handle the writing of those values automatically.
        | Only use member variables when necessary.
        
        .. important::
        
        | If you implement at least one of :meth:`Read`, :meth:`Write` and :meth:`CopyTo`, you must usually implement all three.
        | Otherwise data might be lost.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type hf: c4d.GeListNode
        :param hf: The hyper file to write the data to.
        :rtype: bool
        :return: **True** if the data was written successfully, otherwise **False**.
        
        
        """
        ...
    
    def CopyTo(self, dest: NodeData, snode: GeListNode, dnode: GeListNode, flags: int, trn: AliasTrans) -> bool:
        """    
        | Override - Called when a node is duplicated. :meth:`Init` is called for the destination node before this function.
        | Use this function to copy any settings for the plugin that are not stored in the :class:`BaseContainer <c4d.BaseContainer>`.
        | Simply transfer them from the current node data to *dest* and/or *snode* to *dnode*:
        
        .. code-block:: python
        
        dest.offset = offset
        dest.object_access = object_access
        
        .. note::
        
        | It is recommended to store as much as possible in the :class:`BaseContainer <c4d.BaseContainer>` as Cinema 4D will handle the copying of those values automatically.
        | Only use member variables when necessary.
        
        .. important::
        
        If at least one of :meth:`Read`, :meth:`Write` and :meth:`CopyTo` is implemented, it is recommended to implement all three, otherwise data might be lost.
        
        :type dest: c4d.plugins.NodeData
        :param dest: The destination node data.
        :type snode: c4d.GeListNode
        :param snode: The source node data, i.e. the current node.
        :type dnode: c4d.GeListNode
        :param dnode: The destination node data.
        :type flags: int
        :param flags: The copy flags:
        
        .. include:: /consts/COPYFLAGS.rst
        :start-line: 3
        
        :type trn: c4d.AliasTrans
        :param trn:
        
        .. versionchanged:: R17.032
        
        An alias translator for the operation.
        
        :rtype: bool
        :return: **True** if the data was copied successfully, otherwise **False**.
        
        
        """
        ...
    
    def Message(self, node: GeListNode, type: int, data: Any) -> bool:
        """    
        Override - Called when a node receives messages.
        
        .. seealso:: :doc:`MSG </consts/MSG_PLUGINS>` for the information on the messages type, data and input/output.
        
        .. _MSG_DESCRIPTION_COMMAND_example:
        
        .. note:: The following code shows how to handle *MSG_DESCRIPTION_COMMAND* sent by a button in a description:
        
        .. code-block:: python
        
        def Message(self, node, type, data):
        if type==c4d.MSG_DESCRIPTION_COMMAND:
        if data['id'][0].id==THE_BUTTON_ID:
        print "Pushed button with the ID", THE_BUTTON_ID
        return True
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type type: int
        :param type: The message type.
        :type data: any
        :param data: The message data.
        :rtype: bool
        :return: Depends on the message *type*.
        
        
        """
        ...
    
    def GetDocument(self, node: GeListNode) -> BaseDocument:
        """    
        | If you create your own BaseList elements this allows you to tell Cinema 4D how to retrieve the document.
        | Any call to :meth:`GeListNode.GetDocument` ends up here.
        
        .. note::
        
        | Standard nodes like objects, tags etc. do not need to override this function.
        | Only if you create elements that are allocated with AllocListNode(), AllocSmallListNode() and AllocMultiNode() do need this function.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :rtype: c4d.documents.BaseDocument
        :return: The document.
        
        
        """
        ...
    
    def IsInstanceOf(self, node: GeListNode, type: int) -> bool:
        """    
        Called to know if the *node* is an instance of the given base *type*.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type type: int
        :param type: The type to check.
        :rtype: bool
        :return: **True** if the *node* is an instance of the given *type*, otherwise **False**.
        
        
        """
        ...
    
    def IsDocumentRelated(self, node: GeListNode) -> bool:
        """    
        Called by the Attribute Manager for correct undo handling.
        
        .. versionadded:: R18.011
        
        .. warning::
        
        | Should not be overloaded by regular plugins and should be used with extra care.
        | If **False** is returned no undo is possible.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :rtype: bool
        :return: **True** if the node is part of the document, otherwise **False**.
        
        
        """
        ...
    
    def GetBubbleHelp(self, node: GeListNode) -> str:
        """    
        Called to create a contextual bubble help and status bar information for the node.
        
        .. versionadded:: R18.011
        
        .. note::
        
        | When dealing with strings it is advised to use the string resources files and the :func:`GeLoadString() <c4d.plugins.GeLoadString>` function.
        | This keeps the plugin easy to localize for any language to support and makes full use of the language features of Cinema 4D.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :rtype: str
        :return: The bubble help string.
        
        
        """
        ...
    
    def GetDDescription(self, node: GeListNode, description: Description, flags: int) -> Union[bool, Tuple[bool, int]]:
        """    
        Called to add parameters to the description for the node. Modify the passed description as needed and return the appropriate flags.
        
        .. versionadded:: R18.011
        
        .. note::
        
        | If only a description resource is used it is not needed to overload :meth:`GetDDescription() <NodeData.GetDDescription>`.
        
        For instance, here is how :meth:`GetDDescription` can be implemented.
        
        
        .. code-block:: python
        
        def GetDDescription(self, node, description, flags):
        
        # Before adding dynamic parameters, load the parameters from the description resource
        if not description.LoadDescription(node.GetType()):
        return False
        
        # Get description single ID
        singleID = description.GetSingleDescID()
        
        # Check if dynamic parameter with ID paramID has to be added
        paramID = ...
        if singleID is None or paramID.IsPartOf(singleID)[0]:
        # Add dynamic parameter
        if not description.SetParameter(paramID, ...):
        return False
        
        ...
        
        # After parameters have been loaded and added successfully, return True and DESCFLAGS_DESC_LOADED with the input flags
        return (True, flags | c4d.DESCFLAGS_DESC_LOADED)
        
        .. seealso:: :class:`c4d.Description` and :meth:`DescID.IsPartOf`
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type description: c4d.Description
        :param description: The node's description to add the parameters to.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_DESC.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, int): The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def GetDParameter(self, node: GeListNode, id: DescID, flags: int) -> Union[bool, Tuple[bool, Any, int]]:
        """    
        | Called to override the reading of description parameters. Necessary for parameters that are not simply stored in the node's container e.g. class members.
        | Return the parameter data and the appropriate flags if the right *id* is provided.
        
        .. versionadded:: R18.011
        
        .. note::
        
        If only a description resource is used it is not needed to overload :meth:`GetDParameter() <NodeData.GetDParameter>`.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_GET.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, any, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, any, int): The status (**True** if successful, otherwise **False**), parameter data and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def SetDParameter(self, node: GeListNode, id: DescID, t_data: Any, flags: int) -> Union[bool, Tuple[bool, int]]:
        """    
        | Called to override the writing of parameters.
        | Read the passed *t_data* if the right *id* is provided, store the data and return the appropriate flags.
        
        .. versionadded:: R18.011
        
        .. note::
        
        If only a description resource is used it is not needed to overload :meth:`SetDParameter() <NodeData.SetDParameter>`.
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type t_data: any
        :param t_data: The parameter data to set.
        :type flags: int
        :param flags: The flags for the description operation:
        
        .. include:: /consts/DESCFLAGS_SET.rst
        :start-line: 3
        
        :rtype: bool or tuple(bool, int)
        :return: One of these options:
        
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, int): The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*).
        
        
        """
        ...
    
    def GetDEnabling(self, node: GeListNode, id: DescID, t_data: Any, flags: int, itemdesc: BaseContainer) -> bool:
        """    
        | Called to let decide which parameters should be enabled or disabled (ghosted).
        | This can be used both for parameters that are stored in the node's container and for custom parameters.
        |
        | Just read the passed *t_data* if the right *id* was provided, and return **True** to enable the parameter or **False** to disable it depending on the value.
        |
        | And if the passed *id* element is not processed, include a call to the base class method as last return.
        
        .. code-block:: python
        
        return NodeData.GetDEnabling(self, node, id, t_data, flags, itemdesc)
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type id: c4d.DescID
        :param id: The ID of the parameter.
        :type t_data: any
        :param t_data: The current data for the parameter.
        :type flags: int
        :param flags: Not used.
        :type itemdesc: c4d.BaseContainer
        :param itemdesc: The description, encoded to a container as described in :class:`Description <c4d.Description>`.
        :rtype: bool
        :return: **True** if the parameter should be enabled, otherwise **False**.
        
        .. note::
        
        It is recommended to include a call to the base class method as last return.
        
        
        """
        ...
    
    def TranslateDescID(self, node: GeListNode, id: DescID) -> None:
        """    
        | Called by the Attribute Manager for every object and every description ID.
        | Gives a `NodeData` plugin the opportunity to route a description ID in the description of a node to another one.
        | For example used for tags that are embedded in an object description so that the keyframer for a tag property creates the track on the tag and not on the object.
        
        .. versionadded:: R18.011
        
        :type node: c4d.GeListNode
        :param node: The list node connected with this instance.
        :type id: c4d.DescID
        :param id: The source description ID.
        :rtype: bool or tuple(bool, :class:`DescID <c4d.DescID>`, :class:`C4DAtom <c4d.C4DAtom>`)
        :return: One of these options:
        
        |
        | bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.
        | tuple(bool, :class:`DescID <c4d.DescID>`, :class:`C4DAtom <c4d.C4DAtom>`): The status (**True** if successful, otherwise **False**), target description ID and object.
        
        
        """
        ...
    

class ObjectData(NodeData):
    def GetDimension(self, op: BaseObject, mp: Vector, rad: Vector) -> None:
        """    
        Override - Return the boundaries of your object.
        
        .. code-block:: python
        
        def GetDimension(self, op, mp, rad):
        '''
        (i) When the method runs without a raised exception
        mp and rad will be internally copied, otherwise they
        are ignored.
        '''
        
        mp.x = self.x_size   # correct
        mp.y = self.y_size   # correct
        mp.z = self.z_size   # correct
        
        mp = c4d.Vector(x_size, y_size, z_size)    #!!! wrong !!! do not rebind mp!
        #this assign applies for 'rad' as well
        return
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type mp: c4d.Vector
        :param mp: Assign the center point of the bounding box to this vector.
        :type rad: c4d.Vector
        :param rad: Assign the XYZ bounding box radius to this vector.
        
        
        """
        ...
    
    def Draw(self, op: BaseObject, drawpass: int, bd: BaseDraw, bh: BaseDrawHelp) -> int:
        """    
        Override - Called when the display is updated for you to display some visual element of your op in the 3D view.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type drawpass: int
        :param drawpass: One of the following flags:
        
        .. include:: /consts/DRAWPASS.rst
        :start-line: 3
        
        .. warning::
        
        | Only draw in *DRAWPASS_HIGHLIGHTS* if you **really** know what you are doing.
        | Otherwise **always** check the *drawpass* and then **do not** draw if it is *DRAWPASS_HIGHLIGHTS*.
        
        Here is an example.
        
        .. code-block:: python
        
        def Draw(self, op, drawpass, bd, bh):
        
        if drawpass==c4d.DRAWPASS_HIGHLIGHTS:
        return c4d.DRAWRESULT_SKIP
        
        # Put here your drawing operations
        
        return c4d.DRAWRESULT_OK
        
        .. warning::
        
        | Only draw the object in one pass : *DRAWPASS_OBJECT*.
        | The object's appearance may change if you draw the same object in multiple passes.
        
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` editor's view.
        :rtype: int
        :return: Success of drawing into the editor view:
        
        .. include:: /consts/DRAWRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawShadow(self, op: BaseObject, bd: BaseDraw, bh: BaseDrawHelp) -> int:
        """    
        Called during the shadow pass instead of the :meth:`Draw` method.
        
        .. versionadded:: R14.014
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: The :class:`BaseDrawHelp <c4d.plugins.BaseDrawHelp>` editor's view.
        :rtype: int
        :return: Success of drawing into the editor view:
        
        .. include:: /consts/DRAWRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetVirtualObjects(self, op: BaseObject, hh: Any) -> BaseObject:
        """    
        Override - Return an object chain of a generator object (e.g. a polygonal object).
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        .. note::
        
        Please read the :ref:`Optimize Cache section <optimize-cache>` at the top of this page to get in touch with the caching options.
        
        .. warning::
        
        Must not be overridden for non-generator objects.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Pass this to virtual objects hierarchy methods :meth:`BaseObject.GetCache`, :meth:`BaseObject.CheckCache`, :meth:`BaseObject.GetAndCheckHierarchyClone`, :meth:`BaseObject.GetHierarchyClone`.
        
        :rtype: c4d.BaseObject
        :return: The newly allocated object chain, or **None** if a memory error occured.
        
        .. note::
        
        | Only return **None** in the case of a memory error.
        | If the generator does not produce any output (e.g. when the user chooses wrong settings) it must at least return an (empty) **Onull** object, otherwise Cinema 4D will try to rebuild the cache again and again.
        
        
        """
        ...
    
    def GetContour(self, op: BaseObject, doc: BaseDocument, lod: int, bt: BaseThread) -> Optional[SplineObject]:
        """    
        Override - Return a spline contour. For spline objects only.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        .. note::
        
        | Splines created through :meth:`GetContour` are cached.
        | To make this frame dependent, :meth:`CheckDirty` can be overloaded to set the object dirty if a certain condition has changed.
        
        .. warning::
        
        Must not be overridden for non-spline objects.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the plugin object.
        :type lod: int
        :param lod: The level of detail.
        :type bt: c4d.threading.BaseThread
        :param bt: The calling thread.
        :rtype: c4d.SplineObject or **None**
        :return: The newly allocated spline or **None**
        
        
        """
        ...
    
    def ModifyObject(self, mod: BaseObject, doc: BaseDocument, op: BaseObject, op_mg: Matrix, mod_mg: Matrix, lod: float, flags: int, thread: BaseThread) -> bool:
        """    
        Override - Called when an object plugin should modify the passed object.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        .. warning::
        
        Must not be overridden for non-modifier objects.
        
        :type mod: c4d.BaseObject
        :param mod: The modifier object.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the plugin object.
        :type op: c4d.BaseObject
        :param op: The object to modify.
        :type op_mg: c4d.Matrix
        :param op_mg: The object's world matrix.
        :type mod_mg: c4d.Matrix
        :param mod_mg: The modifier object's world matrix.
        :type lod: float
        :param lod: The level of detail.
        :type flags: int
        :param flags: Currently unused.
        :type thread: c4d.threading.BaseThread
        :param thread: The calling thread.
        :rtype: bool
        :return: Success of modifying the object.
        
        
        """
        ...
    
    def CheckDirty(self, op: BaseObject, doc: BaseDocument) -> None:
        """    
        | Override - You can override this function to check for a change in the object manually.
        | This example will make your object update every frame.
        
        .. code-block:: python
        
        def CheckDirty(self, op, doc):
        
        frame = doc.GetTime().GetFrame(doc.GetFps())
        if frame != lastFrame:
        lastFrame = frame
        op.SetDirty(c4d.DIRTYFLAGS_DATA)
        
        This method is useful to override in deformer and spline plugins.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the plugin object.
        
        
        """
        ...
    
    def MoveHandle(self, op: BaseObject, undo: BaseObject, mouse_pos: Vector, hit_id: int, qualifier: int, bd: BaseDraw) -> bool:
        """    
        Override - Move a handle manually.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type undo: c4d.BaseObject
        :param undo: This is a copy of the object that must not be modified during the move handle.
        :type mouse_pos: c4d.Vector
        :param mouse_pos: The current mouse position.
        :type hit_id: int
        :param hit_id: The handle ID returned from :meth:`DetectHandle`
        :type qualifier: int
        :param qualifier: Any qualifier keys that were pressed. These are defined in :mod:`c4d.gui`:
        
        .. include:: /consts/QUALIFIER.rst
        :start-line: 3
        
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :rtype: bool
        :return: Success of modifying the handle.
        
        
        """
        ...
    
    def DetectHandle(self, op: BaseObject, bd: BaseDraw, x: int, y: int, qualifier: int) -> int:
        """    
        Override - Manually detect a click on a handle.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type x: int
        :param x: The mouse X coordinate.
        :type y: int
        :param y: The mouse Y coordinate.
        :type qualifier: int
        :param qualifier: Any qualifier keys that were pressed. These are defined in :mod:`c4d.gui`:
        
        .. include:: /consts/QUALIFIER.rst
        :start-line: 3
        
        :rtype: int
        :return: The handle ID that is to be passed to :meth:`MoveHandle`
        
        
        """
        ...
    
    def AddToExecution(self, op: BaseObject, list: PriorityList) -> bool:
        """    
        | Override - By default this function returns *False*.
        | Then Cinema 4D will call :meth:`Execute` at the priority specified by the user in the *EXPRESSION_PRIORITY* parameter of the container.
        
        If you override this function and return *True*, then you can insert your own points of execution in the list by calling for example.
        
        .. code-block:: python
        
        list.Add(op, c4d.EXECUTIONPRIORITY_ANIMATION, 0)
        list.Add(op, c4d.EXECUTIONPRIORITY_GENERATOR, 0)
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type list: c4d.plugins.PriorityList
        :param list: The priority list to add your object's execution points to.
        :rtype: bool
        :return: **True** if you override this function and has added stuff to list.
        
        
        """
        ...
    
    def Execute(self, op: BaseObject, doc: BaseDocument, bt: Optional[BaseThread] = ..., priority: Optional[int] = ..., flags: Optional[int] = ...) -> int:
        """    
        Override - Called at the point in the priority pipeline specified by :meth:`AddToExecution`, or the lack thereof.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type doc: c4d.documents.BaseDocument
        :param doc: The host document of the object.
        :type bt: Optional[c4d.BaseThread]
        :param bt: Currently not used.
        :type priority: int
        :param priority: The priority of this call to :meth:`Execute` in the pipeline. Standard values are:
        
        .. include:: /consts/EXECUTIONPRIORITY.rst
        :start-line: 3
        
        :type flags: int
        :param flags: A combination of the following flags:
        
        .. include:: /consts/EXECUTIONFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: The result:
        
        .. include:: /consts/EXECUTIONRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def ModifyParticles(self, op: BaseObject, pp: Any, ss: Any, pcnt: int, diff: float) -> None:
        """    
        Override - Called for modifying particles. This is for particle modifiers only.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type pp: list of :class:`Particle <c4d.modules.particles.Particle>`
        :param pp: The initial element of the Particle list.
        
        .. note::
        
        This list is used to read the particles information only, the particles should not be modified.
        
        :type ss: list of :class:`BaseParticle <c4d.modules.particles.BaseParticle>`
        :param ss: The initial element of the :class:`BaseParticle <c4d.modules.particles.BaseParticle>` list. Modify the elements in this list to change the velocity of the particle.
        :type pcnt: int
        :param pcnt: The number of particles in the :class:`Particle <c4d.modules.particles.Particle>` and :class:`BaseParticle <c4d.modules.particles.BaseParticle>` list.
        :type diff: float
        :param diff: The time delta for the particles movement in seconds. Usually the difference in time between two frames, but this can be different for such functions as motion blur.
        
        
        """
        ...
    
    def GetHandleCount(self, op: BaseObject) -> int:
        """    
        Called to get the number of handles the object has. Part of the automated handle interface.
        
        .. versionadded:: R18.011
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :rtype: int
        :return: The number of handles for the object.
        
        
        """
        ...
    
    def GetHandle(self, op: BaseObject, i: int, info: HandleInfo) -> None:
        """    
        Called to get the information for handle at index *i*. Part of the automated handle interface.
        
        .. versionadded:: R18.011
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type i: int
        :param i: The handle index.
        :type info: c4d.HandleInfo
        :param info: Fill with the handle information.
        
        
        """
        ...
    
    def SetHandle(self, op: BaseObject, i: int, p: Vector, info: HandleInfo) -> None:
        """    
        | Called to set the information for handle at index *i*. Part of the automated handle interface.
        | Called when the user has moved handle *i* to position *p*. Update the object's internal data accordingly (e.g. parameter values etc).
        
        .. versionadded:: R18.011
        
        :type op: c4d.BaseObject
        :param op: The established base object.
        :type i: int
        :param i: The handle index.
        :type p: c4d.Vector
        :param p: The new handle position.
        :type info: c4d.HandleInfo
        :param info: The handle information.
        
        
        """
        ...
    

class PreferenceData(NodeData):
    def InitPreferenceValue(self, id: int, data: Any, desc: Description, descid: DescID, bc: BaseContainer) -> None:
        """    
        Initializes preference values in *bc*.
        
        :type id: int
        :param id: The world container ID of the preference parameter.
        :type data: any
        :param data: The value used for the initialization.
        :type desc: c4d.Description
        :param desc: The description of the preference hook. If **None**, *id* is used instead of *descid*.
        :type descid: c4d.DescID
        :param descid: The description ID of the preference parameter.
        :type bc: c4d.BaseContainer
        :param bc: The preference world container. A plugin should always store its parameters in a sub-container in the world container.
        
        
        """
        ...
    

class SceneLoaderData(NodeData):
    def Identify(self, node: BaseList2D, name: str, probe: Any, size: int) -> bool:
        """    
        | Override - Identify the file type as one that can be loaded using this plugin.
        |
        | If possible, the file should not be identified through the suffix, but through the *probe* data.
        
        :type node: c4d.BaseList2D
        :param node: The node object.
        :type name: str
        :param name: The name of the loader.
        :type probe: buffer
        :param probe: The start of a small chunk of data from the start of the file for testing this file type. Usually the probe size is 1024 bytes. Never call the buffer outside this method!
        :type size: int
        :param size: The size of the chunk for testing this file type.
        :rtype: bool
        :return: **True** if your plugin recognises this file.
        
        
        """
        ...
    
    def Load(self, node: BaseList2D, name: str, doc: BaseDocument, filterflags: int, error: None, bt: BaseThread) -> int:
        """    
        Override - Load the file into the document.
        
        :type node: c4d.BaseList2D
        :param node: The node object.
        :type name: str
        :param name: The filename of the file to load.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document that the selected objects should be loaded into.
        :type filterflags: int
        :param filterflags: Information about what can be done during this load call:
        
        .. include:: /consts/SCENEFILTER.rst
        :start-line: 3
        
        :type error: None
        :param error: Not supported.
        :type bt: c4d.threading.BaseThread
        :param bt: The calling thread.
        :rtype: int
        :return: The return values:
        
        .. include:: /consts/FILEERROR.rst
        :start-line: 3
        
        
        """
        ...
    

class SceneSaverData(NodeData):
    def Save(self, node: BaseList2D, name: str, doc: BaseDocument, filterflags: int) -> int:
        """    
        Override - Save the document.
        
        .. versionchanged:: R15.057
        
        .. warning::
        
        | Calling :meth:`BaseDocument.GetDocumentPath` from a scene saver invoked by :func:`SaveDocument() <c4d.documents.SaveDocument>` is now consistent with the GUI behavior of the export.
        | :meth:`BaseDocument.GetDocumentPath` now always returns the current path of the document instead of the target path of the file to save for all formats (except `Cinema 4D (*.c4d)` and `Cinema 4D XML (*.xml)`).
        | A new document flag **DOCUMENT_SAVEDOC_DESTINATIONPATH** (only set when saving) can be used in scene savers to get the destination path of the exported file.
        
        :type node: c4d.BaseList2D
        :param node: The node object.
        :type name: str
        :param name: The filename of the file to save.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document that the selected objects should be saved from.
        :type filterflags: int
        :param filterflags: The possible flags are:
        
        .. include:: /consts/SCENEFILTER.rst
        :start-line: 3
        
        :rtype: int
        :return: The return values:
        
        .. include:: /consts/FILEERROR.rst
        :start-line: 3
        
        
        """
        ...
    

class ShaderData(NodeData):
    def InitRender(self, sh: BaseShader, irs: InitRenderStruct) -> int:
        """    
        Override - Pre-calculate any data for rendering.
        
        :type sh: c4d.BaseShader
        :param sh: The shader node connected with this instance.
        :type irs: c4d.modules.render.InitRenderStruct
        :param irs: Information about the upcoming rendering.
        :rtype: int
        :return: Result of the initialisation:
        
        .. include:: /consts/INITRENDERRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def FreeRender(self, sh: BaseShader) -> None:
        """    
        Override -  Free any resources used for the precalculated data from :meth:`InitRender`.
        
        :type sh: c4d.BaseShader
        :param sh: The shader node connected with this instance.
        
        
        """
        ...
    
    def Output(self, sh: BaseShader, cd: ChannelData) -> Vector:
        """    
        | Override - Called for each point of the visible surface of a shaded object.
        | Here you should calculate and return the channel color for the point *cd*.p.
        
        **Important**:
        
        | No OS calls are allowed during this function.
        | Doing so could cause a crash, since it can be called in a multi-processor context.
        
        :type sh: c4d.BaseShader
        :param sh: The shader node connected with this instance.
        :type cd: c4d.modules.render.ChannelData
        :param cd: Channel data to use and/or modify.
        :rtype: c4d.Vector
        :return: The calculated color.
        
        
        """
        ...
    
    def SetExceptionColor(self, col: Vector) -> None:
        """    
        Set the exception color.
        
        :type col: c4d.Vector
        :param col: The exception color.
        
        
        """
        ...
    

class TagData(NodeData):
    def Draw(self, tag: BaseTag, op: BaseObject, bd: BaseDraw, bh: BaseDrawHelp) -> bool:
        """    
        Override - Called when the display is updated for you to display some visual element of your tag in the 3D view.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type tag: c4d.BaseTag
        :param tag: The object which is established with this instance.
        :type op: c4d.BaseObject
        :param op: The host object of the tag.
        :type bd: c4d.BaseDraw
        :param bd: The editor's view.
        :type bh: c4d.plugins.BaseDrawHelp
        :param bh: An helper class.
        :rtype: bool
        :return: Success of drawing into the editor view.
        
        
        """
        ...
    
    def Execute(self, tag: BaseTag, doc: BaseDocument, op: BaseObject, bt: BaseThread, priority: int, flags: int) -> int:
        """    
        Override - Called at the point when the tag is executed.
        
        .. note::
        
        | This function is called in a thread context.
        | Please see the :ref:`important information <threading-information>` about threading.
        
        :type tag: c4d.BaseTag
        :param tag: The established :class:`BaseTag <c4d.BaseTag>`.
        :type doc: c4d.documents.BaseDocument
        :param doc: The host document of the tag's object.
        :type op: c4d.BaseObject
        :param op: The host object of the tag.
        :type bt: c4d.threading.BaseThread
        :param bt: The calling thread.
        :type priority: int
        :param priority: One of the following flags:
        
        .. include:: /consts/EXECUTIONPRIORITY.rst
        :start-line: 3
        
        :type flags: int
        :param flags: A combination of the following flags:
        
        .. include:: /consts/EXECUTIONFLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: One of the following results:
        
        .. include:: /consts/EXECUTIONRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def AddToExecution(self, tag: BaseTag, list: PriorityList) -> bool:
        """    
        | Override - By default this function returns **False**.
        | Then Cinema 4D will call :meth:`Execute` at the priority specified by the user in the *EXPRESSION_PRIORITY* parameter of the container.
        
        If you override this function and return **True**, then you can insert your own points of execution in the list by calling for example.
        
        .. code-block:: python
        
        list.Add(tag, EXECUTIONPRIORITY_ANIMATION, 0)
        list.Add(tag, EXECUTIONPRIORITY_GENERATOR, 0)
        
        Cinema 4D will then call :meth:`Execute` two times.
        
        :type tag: c4d.BaseTag
        :param tag: The established :class:`BaseTag <c4d.BaseTag>`.
        :type list: c4d.plugins.PriorityList
        :param list: The priority list to add your tag's execution points to.
        :rtype: bool
        :return: **True** if you override this function and have added stuff to list.
        
        
        """
        ...
    
    def Message(self, node: BaseTag, type: int, data: Any) -> bool:
        ...
    


def GeLoadString(id: int, p1: str, p2: str, p3: str, p4: str) -> str:
    """    
    Load a string and replace the first '#' with the placeholder string.
    
    In Cinema 4D there is a convention that in strings '#' is a placeholder for dynamic parts (this allows you to translate a whole sentence as sentence structure and word placement may be reverted in other language).
    
    .. warning::
    
    To use this function, *__res__* must be defined in your global scope.
    
    For example:
    
    If the string is named: "loading of file '#' failed" then you can pass the actual filename (as string) as *p1* and you'll get the desired result.
    
    :type id: int
    :param id: The ID of the string to get.
    :type p1: str
    :param p1: The string to insert into the first placeholder.
    :type p2: str
    :param p2: The string to insert into the second placeholder.
    :type p3: str
    :param p3: The string to insert into the third placeholder.
    :type p4: str
    :param p4: The string to insert into the fourth placeholder.
    :rtype: str
    :return: The completed string.
    
    
    """
    ...

def GetToolData(doc: BaseDocument, plugind: Any) -> BaseContainer:
    """    
    Gets the tool data container for the tool with ID *pluginid*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to get the settings for.
    :type pluginid: int
    :param pluginid: The plugin ID of the tool.
    :rtype: c4d.BaseContainer
    :return: Tool data container.
    
    
    """
    ...

def RegisterPluginHelpCallback(pluginid: int, callback: Callable[..., Any]) -> bool:
    """    
    Registers a callback for plugin help support.
    
    .. versionadded:: R19
    
    :type pluginid: int
    :param pluginid: The plugin id. Please obtain a serial from `PluginCafe.com <http://plugincafe.com/>`_
    :type callback: function(*opType*, *baseType*, *group*, *property*)
    :param callback:
    
    | The help callback for the plugin. Useful to display context sensitive help when the user selects "Show Help" for a node or attribute.
    | The passed arguments are:
    
    | *opType*: `str`: The node type name, for example "OATOM".
    | *baseType*: `str`: The name of the base object type that *opType* is derived from, usually the same as *opType*.
    | *group*: `str`: The name of the group in the attribute manager, for example "ID_OBJECTPROPERTIES".
    | *property*: `str`: The name of the property, for example "ATOMOBJECT_SINGLE".
    
    | The callback function returns **True** if help has been provided, otherwise **False**.
    
    .. warning::
    
    Only return **True** for the registered plugin types.
    
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GetWorldPluginData(id: int) -> BaseContainer:
    """    
    Retrieves a container stored with :func:`SetWorldPluginData` from the Cinema 4D preferences. This can be used by any plugin to store preferences.
    
    .. seealso:: This :maxongithub:`script <scripts/03_application_development/files_media/export_alembic_r14.py>` that shows how to effectively access and change the settings of an importer/exporter.
    
    :type id: int
    :param id: The plugin ID that the container should be associated with.
    :rtype: c4d.BaseContainer
    :return: The retrieved container
    
    
    """
    ...

def SetWorldPluginData(id: int, bc: BaseContainer, add: bool) -> bool:
    """    
    Stores a container in the Cinema 4D preferences. Can be used by any plugin to store preferences.
    
    .. seealso:: This :maxongithub:`script <scripts/03_application_development/files_media/export_alembic_r14.py>` that shows how to effectively access and change the settings of an importer/exporter.
    
    :type id: int
    :param id: The plugin ID that the container should be associated with. Please use a unique ID from `PluginCafe <http://www.plugincafe.com>`_.
    :type bc: c4d.BaseContainer
    :param bc: The container to store.
    :type add: bool
    :param add: If this is **True** the container values are merged with the ones currently stored for this ID. Otherwise the previous values are lost.
    :rtype: bool
    :return: **True** if the container was stored, otherwise **False**.
    
    
    """
    ...

def ReadRegInfo(pluginid: int, size: int) -> ByteSeq:
    """    
    Reads user-specific data (e.g. login data for a user account).
    
    .. note::
    
    Use this method instead of :func:`WritePluginInfo` in a license server environment.
    
    :type pluginid: int
    :param pluginid: The plugin ID the data is associated with.
    :type size: int
    :param size: The buffer size
    :rtype: c4d.storage.ByteSeq
    :return: The data buffer.
    
    
    """
    ...

def WriteRegInfo(pluginid: int, buffer: ByteSeq) -> None:
    """    
    Writes user-specific data (e.g. login data for a user account).
    
    .. note::
    
    Use this method instead of :func:`WritePluginInfo` in a license server environment.
    
    :type pluginid: int
    :param pluginid: The plugin ID the data is associated with.
    :type buffer: c4d.storage.ByteSeq
    :param buffer: The data buffer.
    
    
    """
    ...

def ReadPluginInfo(pluginid: int, size: int) -> ByteSeq:
    """    
    Read private serial information for a plugin. Cinema 4D will store this data encrypted.
    
    :type pluginid: int
    :param pluginid: The plugin ID the data is associated with.
    :type size: int
    :param size: The buffer size
    :rtype: c4d.storage.ByteSeq
    :return: The data buffer.
    
    
    """
    ...

def WritePluginInfo(pluginid: int, buffer: ByteSeq) -> None:
    """    
    Write private serial information for a plugin. Cinema 4D will store this data encrypted.
    
    :type pluginid: int
    :param pluginid: The plugin ID the data is associated with.
    :type buffer: c4d.storage.ByteSeq
    :param buffer: The data buffer.
    
    
    """
    ...

def GetFirstPlugin() -> BasePlugin:
    """    
    Returns the first plugin of Cinema 4D.
    
    :rtype: c4d.plugins.BasePlugin
    :return: The first plugin.
    
    
    """
    ...

def FindPlugin(id: int, type: Optional[int] = ...) -> BasePlugin:
    """    
    Returns the :class:`BasePlugin <c4d.plugins.BasePlugin>` found by id.
    
    :type id: int
    :param id: The plugin id. Please obtain a serial from plugincafe.com
    :type type: int
    :param type: Optionally a plugin type filter:
    
    .. include:: /consts/PLUGINTYPE.rst
    :start-line: 3
    
    :rtype: c4d.plugins.BasePlugin
    :return: The plugin.
    
    
    """
    ...

def FilterPluginList(type: int, sortbyname: bool) -> None:
    """    
    Browses recursively through the plugin list looking for plugin of the specified *type*. For example, to find all bitmap savers you can write:
    
    .. literalinclude:: /../../doc.python.code/c4d/plugins/filterpluginlist.py
    :language: python
    
    :type type: int
    :param type: Plugin type filter:
    
    .. include:: /consts/PLUGINTYPE.rst
    :start-line: 3
    
    :type sortbyname: bool
    :param sortbyname: If this is **True** then the found plugins are sorted alphabetically by name.
    :rtype: list of :class:`BasePlugin <c4d.plugins.BasePlugin>`
    :return: The list.
    
    
    """
    ...

def RegisterToolPlugin(id: int, str: str, info: int, icon: Union[None, BaseBitmap], help: str, dat: ToolData) -> bool:
    """    
    Registers a :class:`ToolData <c4d.plugins.ToolData>` plugin.
    
    .. seealso:: :maxongithub:`Py-LiquidPainter <plugins/py-liquid_painter_r12/py-liquid_painter_r12.pyp#L283>` a ToolData plugin example.
    
    :type id: int
    :param id: The plugin id. Please obtain a serial from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name.
    
    .. note::
    
    If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number. Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Tool Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_TOOL.rst
    :start-line: 3
    
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type help: str
    :param help: The tool tips and status bar help text for the command.
    
    .. note::
    
    | When using strings it is advised to use the string resources files and the :func:`GeLoadString() <c4d.plugins.GeLoadString>` function.
    | This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.
    
    :type dat: c4d.plugins.ToolData
    :param dat: A data instance for the plugin.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterSculptBrushPlugin(id: int, str: str, info: int, icon: Union[None, BaseBitmap], help: str, sculptparams: SculptBrushParams, dat: SculptBrushToolData, res: Optional[GeResource] = ...) -> bool:
    """    
    Registers a :class:`SculptBrushToolData <c4d.plugins.SculptBrushToolData>`.
    
    .. seealso::
    
    The next SculptBrushToolData plugins examples:
    
    :maxongithub:`Py-SculptGrabBrush <plugins/py-sculpt_grab_brush_r16/sculpt_grab_brush_r16.pyp>`,
    :maxongithub:`Py-SculptPaintBrush <plugins/py-sculpt_paint_brush_r16/sculpt_paint_brush_r16.pyp>`,
    :maxongithub:`Py-SculptPullBrush <plugins/py-sculpt_pull_brush_r16/sculpt_pull_brush_r16.pyp>` and
    :maxongithub:`Py-SculptTwistBrush <plugins/py-sculpt_twist_brush_r16/sculpt_twist_brush_r16.pyp>`
    
    .. versionadded:: R16.021
    
    :type id: int
    :param id: The plugin id. Please obtain a serial from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Tool Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_TOOL.rst
    :start-line: 3
    
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type help: str
    :param help: The tool tips and status bar help text for the command.
    
    .. note::
    
    | When using strings it is advised to use the string resources files and the :func:`GeLoadString() <c4d.plugins.GeLoadString>` function.
    | This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.
    
    :type sculptparams: c4d.modules.sculpting.SculptBrushParams
    :param sculptparams: The brush parameters.
    :type dat: c4d.plugins.SculptBrushToolData
    :param dat: A data instance for the plugin.
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterCommandPlugin(id: int, str: str, info: int, icon: Union[None, BaseBitmap], help: str, dat: CommandData) -> bool:
    """    
    Registers a :class:`CommandData <c4d.plugins.CommandData>` plugin.
    
    .. seealso:: :maxongithub:`Py-TextureBaker <plugins/py-texture_baker_r18/py-texture_baker_r18.pyp#L307>` a CommandData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Command Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_COMMAND.rst
    :start-line: 3
    
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type help: str
    :param help: The tool tips and status bar help text for the command.
    
    .. note::
    
    | When using strings it is advised to use the string resources files and the :func:`GeLoadString() <c4d.plugins.GeLoadString>` function.
    | This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.
    
    :type dat: c4d.plugins.CommandData
    :param dat: A data instance for the plugin.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterFalloffPlugin(id: int, str: str, info: int, g: FalloffData, description: str, res: Optional[GeResource] = ...) -> bool:
    """    
    Registers a :class:`FalloffData <c4d.plugins.FalloffData>` plugin.
    
    .. seealso:: :maxongithub:`Py-NoiseFalloff <plugins/py-noise_falloff_r14/py-noise_falloff_r14.pyp#L380>` a FalloffData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    :type g: c4d.plugins.FalloffData
    :param g: The class which inherits from :class:`FalloffData <c4d.plugins.FalloffData>`.
    :type description: str
    :param description: The name of the description resource file to use for your plugin without **.res**, for example **ofalloff_falloffname**. The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterMessagePlugin(id: int, str: str, info: int, dat: MessageData) -> bool:
    """    
    Registers a :class:`MessageData <c4d.plugins.MessageData>` plugin.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin.
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Message Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_MESSAGE.rst
    :start-line: 3
    
    :type dat: c4d.plugins.MessageData
    :param dat: A data instance for the plugin.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterBitmapSaverPlugin(id: int, str: str, info: int, dat: BitmapSaverData, suffix: str) -> bool:
    """    
    Registers a :class:`BitmapSaverData <c4d.plugins.BitmapSaverData>` plugin.
    
    .. seealso:: :maxongithub:`Py-XampleSaver <plugins/py-xample_saver_r13/py-xample_saver_r13.pyp#L122>` a BitmapSaverData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin.
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Bitmap Saver Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_BITMAPSAVER.rst
    :start-line: 3
    
    :type dat: c4d.plugins.BitmapSaverData
    :param dat: A data instance for the plugin.
    :type suffix: str
    :param suffix: The format's file suffix.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterBitmapLoaderPlugin(id: int, str: str, info: int, dat: BitmapLoaderData) -> bool:
    """    
    Registers a :class:`BitmapLoaderData <c4d.plugins.BitmapLoaderData>` plugin.
    
    .. seealso:: :maxongithub:`Py-XampleLoader <plugins/py-xample_loader_r15/py-xample_loader_r15.pyp#L104>` a BitmapLoaderData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Bitmap Loader Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_BITMAPLOADER.rst
    :start-line: 3
    
    :type dat: c4d.plugins.BitmapLoaderData
    :param dat: A data instance for the plugin.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterTagPlugin(id: int, str: str, info: int, g: Any, description: str, icon: Union[None, BaseBitmap], disklevel: Optional[int] = ..., res: Optional[GeResource] = ...) -> None:
    """    
    Registers a TagData plugin:
    
    .. note::
    
    To use this function, *__res__* must be defined in your global scope.
    
    .. seealso:: :maxongithub:`Py-LookAtCamera <plugins/py-look_at_camera_r13/py-look_at_camera_r13.pyp#L103>` a TagData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Tag Plugin Flags
    
    .. include:: /consts/TAG.rst
    :start-line: 3
    
    :type g: any
    :param g: The class which inherits from :class:`TagData <c4d.plugins.TagData>`
    :type description: str
    :param description:
    
    | The name of the description resource file to use for your plugin without **.res**, for example **Ttagname**.
    | The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.
    
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. Can be **None**. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type disklevel: int
    :param disklevel: The plugin level is similar to a version number for your settings. The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.
    
    As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.
    
    .. important::
    
    For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.
    
    .. note::
    
    If you only use containers for all your values, you do not have to deal with the disklevel.
    
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterShaderPlugin(id: int, str: str, info: int, g: Any, description: str, disklevel: int, res: Optional[GeResource] = ...) -> bool:
    """    
    Registers a :class:`ShaderData <c4d.plugins.ShaderData>` plugin.
    
    .. seealso:: :maxongithub:`Py-Fresnel <plugins/py-fresnel_r13/py-fresnel_r13.pyp#L84>` a ShaderData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: One of the following flags:
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    :type g: any
    :param g: The class which inherits from :class:`ShaderData <c4d.plugins.ShaderData>`
    :type description: str
    :param description: The name of the description resource file to use for your plugin without **.res**, for example **"Xshadername"**. The name has to be unique, i.e. **"Tdisplay"** cannot be used for two different descriptions.
    :type disklevel: int
    :param disklevel:
    
    | The plugin level is similar to a version number for your settings.
    | The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.
    
    As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.
    
    .. important::
    
    For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.
    
    .. note::
    
    If you only use containers for all your values, you do not have to deal with the disklevel.
    
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterObjectPlugin(id: int, str: str, g: Any, description: str, info: int, icon: Union[None, BaseBitmap], disklevel: int, res: Optional[GeResource] = ..., groupname: Optional[str] = ..., group: Optional[int] = ...) -> bool:
    """    
    Registers an :class:`ObjectData <c4d.plugins.ObjectData>` plugin.
    
    .. note::
    
    To use this function, *__res__* must be defined in your global scope.
    
    .. seealso:: :maxongithub:`Py-RoundedTube <plugins/py-rounded_tube_r13/py-rounded_tube_r13.pyp#L439>` an ObjectData plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type g: any
    :param g: The class which inherits from :class:`ObjectData <c4d.plugins.ObjectData>`
    :type description: str
    :param description: The name of the description resource file to use for your plugin without **.res**, for example **Oobjectname**. The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.
    :type info: int
    :param info: One of the following flags:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Object Plugin Flags
    
    .. include:: /consts/OBJECT.rst
    :start-line: 3
    
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. Can be **None**. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :type disklevel: int
    :param disklevel:
    
    | The plugin level is similar to a version number for your settings.
    | The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.
    
    As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.
    
    .. important::
    
    For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.
    
    .. note::
    
    If you only use containers for all your values, you do not have to deal with the disklevel.
    
    :type group: int
    :param group: If you will develop more plugins in the future, you can use this optional argument to group all plugins. Obtain an id from plugincafe.com and put this ID to all plugins which you want to group in your own menu.
    :type groupname: str
    :param groupname: If the argument *group* is given, you should pass a string for the groupname. If the groupname between all grouped plugins is different, the first one is used. If no groupname in the grouped plugins was found, '#naname: id' is used. do not use more than 18 chars.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterNodePlugin(id: int, str: str, info: int, g: Any, icon: Union[None, BaseBitmap], disklevel: int) -> bool:
    """    
    Registers a :class:`NodeData <c4d.plugins.NodeData>` plugin.
    
    .. note::
    
    Normally you won't use this function directly, but rather the specific registration functions for each :class:`NodeData <c4d.plugins.NodeData>` child class.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type info: int
    :param info: One of the following flags:
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    :type g: any
    :param g: The class which inherits from :class:`NodeData <c4d.plugins.NodeData>`
    :type icon: Union[None, c4d.bitmaps.BaseBitmap]
    :param icon: The icon for the command. Can be **None**. The bitmap is copied.
    
    .. note::
    
    | The icon should be of size 32x32, but will be scaled if needed.
    | It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.
    
    :type disklevel: int
    :param disklevel:
    
    | The plugin level is similar to a version number for your settings.
    | The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.
    
    As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.
    
    .. important::
    
    For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.
    
    .. note::
    
    If you only use containers for all your values, you do not have to deal with the disklevel.
    
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterPreferencePlugin(id: int, g: Any, name: str, description: str, parentid: int, sortid: int) -> None:
    """    
    Registers a new preference in the Cinema 4D preferences dialog.
    
    .. versionadded:: R19
    
    .. seealso:: :maxongithub:`Py-Preference <plugins/py-preference_r19/py-preference_r19.pyp#L221>` a Preference plugin example.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type g: any
    :param g: The class which inherits from :class:`PreferenceData <c4d.plugins.PreferenceData>`
    :type name: str
    :param name: The name of the preference.
    :type description: str
    :param description: The name of the description resource file to use for your plugin without **.res**, for example **Oobjectname**. The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.
    :type parentid: int
    :param parentid: The ID of the preference parent hook. Should be usually set to `0`.
    :type sortid: int
    :param sortid: The ID of the parent category in the preferences tree or `0` to create a top-level category. The internal categories are:
    
    .. include:: /consts/PREFS.rst
    :start-line: 3
    
    
    """
    ...

def RegisterManagerInformation(id: int, str: str, info: int) -> bool:
    """    
    Registers manager information for use when registering shortcuts with :func:`AddShortcut() <c4d.gui.AddShortcut>`.
    
    :type id: int
    :param id: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: Manager name.
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterSceneLoaderPlugin(id: int, str: str, g: Any, info: int, description: str, res: Optional[GeResource] = ...) -> bool:
    """    
    Registers a :class:`SceneLoaderData <c4d.plugins.SceneLoaderData>` plugin.
    
    .. note::
    
    To use this function, *__res__* must be defined in your global scope.
    
    :type id: int
    :param id: The plugin id. Please obtain a serial from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type g: any
    :param g: The class which inherits from :class:`SceneLoaderData <c4d.plugins.SceneLoaderData>`
    :type info: int
    :param info: The settings for the plugin. Possible flags are:
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Scene Loader Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_SCENELOADER.rst
    :start-line: 3
    
    * Scene Filter Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_SCENEFILTER.rst
    :start-line: 3
    
    :type description: str
    :param description: The name of the description resource file to use for your plugin without .res, for example *Ffiltername*. The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterSceneSaverPlugin(id: int, str: str, g: Any, info: int, description: str, suffix: str, res: Optional[GeResource] = ...) -> bool:
    """    
    Registers a :class:`SceneSaverData <c4d.plugins.SceneSaverData>` plugin.
    
    .. note::
    
    To use this function, *__res__* must be defined in your global scope.
    
    .. seealso:: :maxongithub:`Py-IesMeta <plugins/py-ies_meta_r12/py-ies_meta_r12.pyp#L206>` a SceneSaverData plugin example.
    
    :type id: int
    :param id: The plugin id. Please obtain a serial from `PluginCafe.com <http://plugincafe.com/>`_
    :type str: str
    :param str: The name of the plugin.
    
    .. note::
    
    | If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.
    | Lower numbers are displayed before higher numbers. If you make the name "--" it will show up as a menu separator.
    
    :type g: any
    :param g: The class which inherits from :class:`SceneSaverData <c4d.plugins.SceneSaverData>`
    :type info: int
    :param info: The flags are
    
    * Plugin General Flags
    
    .. include:: /consts/PLUGINFLAG.rst
    :start-line: 3
    
    * Scene Filter Plugin Flags
    
    .. include:: /consts/PLUGINFLAG_SCENEFILTER.rst
    :start-line: 3
    
    :type description: str
    :param description: The name of the description resource file to use for your plugin without .res, for example *Ffiltername*. The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.
    :type suffix: str
    :param suffix: The format's file suffix.
    :type res: c4d.plugins.GeResource
    :param res: The optional resource.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterDescription(id: int, str: str, res: GeResource) -> bool:
    """    
    Registers a description for a plugin ID.
    
    .. versionadded:: R16.021
    
    .. note::
    
    Not needed for plugin types whose Register() functions have a *description* parameter.
    
    :type id: int
    :param id: The plugin ID. If this is a standalone description, use a unique ID.
    :type str: str
    :param str:
    
    | The name of the description resource file to use for your plugin without .res extension, for example "registered".
    | The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.
    
    :type res: c4d.plugins.GeResource
    :param res: Pass to search in a specific resource class. Otherwise the default path is used.
    :rtype: bool
    :return: **True** if the registration was successful.
    
    
    """
    ...

def RegisterToken(key: str, help: str, example: str, hook: Callable[..., Any]) -> str:
    """    
    Registers a new Token that can be used in a render filename, the token is displayed in the render setting and can be selected by the user.
    
    .. versionadded:: R21
    
    .. seealso:: :maxongithub:`Py-RenderToken <plugins/py-render_token_r21/py-render_token_r21.pyp#L87>` a Token callback example.
    
    .. note::
    
    | The key is the identifier for the Token and has to be unique.
    | For this reason identify your plugin in the Token key as a prefix.
    |
    | Example: "myplug.pass" instead of just "pass" as it will collide wit the generic "pass" Token definition.
    
    :type key: str
    :param key: The key string for the Token itself without the "$".
    :type help: str
    :param help: An help string used to show the Token in the menu.
    :type example: str
    :param example: An example string for the use of the Token.
    :type hook: function(data)
    :param hook: A function used to define the string to replace the Token.
    
    The expected function signature is `functionName(data)` and parameters correspond to:
    
    - data: (:class:`c4d.BaseContainer`) A baseContainer with the next data:
    
    - data[0] (:class:`c4d.documents.BaseDocument`) The BaseDocument used for rendering, can be a clone of original document.
    - data[1] (:class:`c4d.documents.RenderData`) The RenderData used for rendering.
    - data[2] (:class:`c4d.BaseContainer`) The BaseContainer with the render settings (can be different from _rData->GetDataInstance() eg. RQ change paths).
    - data[3] (:class:`c4d.modules.takesystem.BaseTake`) The BaseTake used for rendering.
    - data[4] (int) The frame number used for rendering or NOTOK if the frame is not yet recognized.
    - data[5] (str) The pass user name if multipass is activated.
    - data[6] (str) The pass type name if multipass is activated.
    - data[7] (int) The pass ID used for rendering or NOTOK if multipass is not active or not yet recognized.
    - data[8] (bool) **True** if the pass is a separated light pass.
    - data[9] (int) The light number id.
    - data[10] (bool) **True** if the pass is a separated reflectance material pass.
    - data[11] (str) if data[9] is **True** or data[10] is **True** store here the object scene name.
    - data[12] (bool) if **True** warning strings will be used for the Tokens that cannot be resolved.
    - data[13] (:class:`c4d.BaseList2D`) An owner node for certain tokens such as MoGraph cache tokens. Can be **None**.
    
    :rtype: str
    :return: The string that will replace the Token.
    
    
    """
    ...

def RegisterHiddenToken(key: str, help: str, example: str, hook: Callable[..., Any]) -> str:
    """    
    This function registers a hidden token that is not displayed in Render Settings.
    
    .. versionadded:: R21
    
    .. seealso:: :maxongithub:`Py-RenderToken <plugins/py-render_token_r21/py-render_token_r21.pyp#L90>` a hidden Token callback example.
    
    .. note::
    
    | The key is the identifier for the Token and has to be unique.
    | For this reason identify your plugin in the Token key as a prefix.
    |
    | Example: "myplug.pass" instead of just "pass" as it will collide wit the generic "pass" Token definition.
    
    :type key: str
    :param key: The key string for the Token itself without the "$".
    :type help: str
    :param help: An help string used to show the Token in the menu.
    :type example: str
    :param example: An example string for the use of the Token.
    :type hook: function(data)
    :param hook: A function used to define the string to replace the Token.
    
    The expected function signature is `functionName(data)` and parameters correspond to:
    
    - data: (:class:`c4d.BaseContainer`) A baseContainer with the next data:
    
    - data[0] (:class:`c4d.documents.BaseDocument`) The BaseDocument used for rendering, can be a clone of original document.
    - data[1] (:class:`c4d.documents.RenderData`) The RenderData used for rendering.
    - data[2] (:class:`c4d.BaseContainer`) The BaseContainer with the render settings (can be different from _rData->GetDataInstance() eg. RQ change paths).
    - data[3] (:class:`c4d.modules.takesystem.BaseTake`) The BaseTake used for rendering.
    - data[4] (int) The frame number used for rendering or NOTOK if the frame is not yet recognized.
    - data[5] (str) The pass user name if multipass is activated.
    - data[6] (str) The pass type name if multipass is activated.
    - data[7] (int) The pass ID used for rendering or NOTOK if multipass is not active or not yet recognized.
    - data[8] (bool) **True** if the pass is a separated light pass.
    - data[9] (int) The light number id.
    - data[10] (bool) **True** if the pass is a separated reflectance material pass.
    - data[11] (str) if data[9] is **True** or data[10] is **True** store here the object scene name.
    - data[12] (bool) if **True** warning strings will be used for the Tokens that cannot be resolved.
    - data[13] (:class:`c4d.BaseList2D`) An owner node for certain tokens such as MoGraph cache tokens. Can be **None**.
    
    :rtype: str
    :return: The string that will replace the Token.
    
    
    """
    ...

