from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseContainer, Vector, BaseTime, C4DAtom, SplineData, BaseList2D, Gradient, BaseObject, DateTimeData, IconData, DescID
from c4d.plugins import GeResource
from c4d.documents import BaseDocument
from c4d.bitmaps import BaseBitmap
from c4d.storage import MemoryFileStruct


class C4DGadget(object):
    ...

class EditorWindow(object):
    def DrawXORLine(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Draws an XOR line in the editor view.
        
        :type x1: int
        :param x1: Start X coordinate of the line.
        :type y1: int
        :param y1: Start Y coordinate of the line.
        :type x2: int
        :param x2: End X coordinate of the line.
        :type y2: int
        :param y2: End Y coordinate of the line.
        
        
        """
        ...
    
    def MouseDragStart(self, button: int, mx: float, my: float, flags: int) -> None:
        """    
        Initializes a mouse dragging loop.
        
        For instance in a :meth:`ToolData.MouseInput`.
        
        .. code-block:: python
        
        mousex = msg[c4d.BFM_INPUT_X]
        mousey = msg[c4d.BFM_INPUT_Y]
        
        win.MouseDragStart(c4d.KEY_MLEFT, mousex, mousey, c4d.MOUSEDRAGFLAGS_DONTHIDEMOUSE|c4d.MOUSEDRAGFLAGS_NOMOVE)
        
        mx = mousex
        my = mousey
        while True:
        result, dx, dy, channels = win.MouseDrag()
        if result !=c4d.MOUSEDRAGRESULT_CONTINUE:
        break
        
        mx += dx
        my += dy
        print "Mouse Dragging at position [%f,%f]" % (mx, my)
        
        print "Mouse Dragging Ended: ", win.MouseDragEnd()
        
        :type button: int
        :param button: State of the mouse buttons.
        :type mx: float
        :param mx: The mouse X coordinate.
        :type my: float
        :param my: The mouse Y coordinate.
        :type flags: int
        :param flags: The mouse drag flags:
        
        .. include:: /consts/MOUSEDRAGFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def MouseDrag(self) -> Tuple[int, float, float, BaseContainer]:
        """    
        Checks for the mouse drag status.
        
        .. code-block:: python
        
        result, dx, dy, channels = win.MouseDrag()
        
        :rtype: Tuple[int, float, float, c4d.BaseContainer]
        :return: A tuple.
        
        
        """
        ...
    
    def MouseDragEnd(self) -> int:
        """    
        Checks why the mouse drag ended. Allows to perform any undo operations needed if the user canceled the drag.
        
        :rtype: int
        :return: The mouse drag result:
        
        .. include:: /consts/MOUSEDRAGRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def BfGetInputEvent(self, askdevice: int, res: BaseContainer) -> bool:
        """    
        Gets the next input event for a certain device from the event queue.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the event could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def BfGetInputState(self, askdevice: int, askchannel: int, res: BaseContainer) -> bool:
        """    
        Polls a certain channel of a device for the current input state.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type askchannel: int
        :param askchannel: The channel to ask.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the state could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def Screen2Local(self) -> Tuple[int, int]:
        """    
        Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the user area).
        
        .. code-block:: python
        
        x, y = win.Screen2Local()
        
        :rtype: Tuple[int, int]
        :return: The local x and y coordinate.
        :raise RuntimeError: If the coordinates cannot be transformed.
        
        
        """
        ...
    
    def Local2Screen(self) -> Tuple[int, int]:
        """    
        Transforms local coordinates (relative to the top left corner of the user area) to screen coordinates (relative to the top left corner of the system screen).
        
        .. code-block:: python
        
        x, y = win.Local2Screen()
        
        :rtype: Tuple[int, int]
        :return: The screen x and y coordinate.
        :raise RuntimeError: If the coordinates cannot be transformed.
        
        
        """
        ...
    
    def Global2Local(self) -> Tuple[int, int]:
        """    
        Transforms global window coordinates (relative to the top left corner of the application window) to local coordinates (relative to the top left corner of the user area).
        
        .. code-block:: python
        
        x, y = win.Global2Local()
        
        :rtype: Tuple[int, int]
        :return: The local x and y coordinate.
        :raise RuntimeError: If the coordinates cannot be transformed.
        
        
        """
        ...
    
    def Local2Global(self) -> Tuple[int, int]:
        """    
        Transforms local coordinates (relative to the top left corner of the user area) to global window coordinates (relative to the top left corner of the application window).
        
        .. code-block:: python
        
        x, y = win.Local2Global()
        
        :rtype: Tuple[int, int]
        :return: The global x and y coordinate.
        :raise RuntimeError: If the coordinates cannot be transformed.
        
        
        """
        ...
    

class GeDialog(object):
    def __init__(self) -> None:
        """    
        Init a GeDialog.
        
        
        """
        ...
    
    def CreateLayout(self) -> bool:
        """    
        Override - Called when Cinema 4D is about to display the dialog.
        
        :rtype: bool
        :return: **True** if successful, or **False** to signalize an error.
        
        
        """
        ...
    
    def Message(self, msg: BaseContainer, result: BaseContainer) -> int:
        """    
        | Override this function to react to more messages than covered by the other functions.
        | Normally this is not necessary.
        
        .. note::
        
        If overridden, include a call to the base version of this function, :meth:`GeDialog.Message`:
        
        .. code-block:: python
        
        def Message(self, msg, result):
        return c4d.gui.GeDialog.Message(self, msg, result)
        
        :type msg: BaseContainer
        :param msg: The message container.
        :type result: BaseContainer
        :param result: A container to store results in.
        :rtype: int
        :return: The return value depends on the message.
        
        
        """
        ...
    
    def InitValues(self) -> bool:
        """    
        Called when the dialog is initialized by the GUI.
        
        :rtype: bool
        :return: **True** if successful, or **False** to signalize an error.
        
        
        """
        ...
    
    def CoreMessage(self, id: int, msg: BaseContainer) -> bool:
        """    
        | Override this function if you want to react to Cinema 4D core messages.
        | The original message is stored in msg.
        
        :type id: int
        :param id: The message ID:
        
        .. include:: /consts/EVMSG.rst
        :start-line: 3
        
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        :rtype: bool
        :return: Currently not used - but you have to return a bool value.
        
        
        """
        ...
    
    def Command(self, id: int, msg: BaseContainer) -> bool:
        """    
        | Override this function if you want to react to user clicks.
        | Whenever the user clicks on a gadget and/or changes its value this function will be called.
        | It is also called when a string menu item is selected. Override it to handle such events.
        
        .. note::
        
        Remember that you need to call :func:`StopAllThreads() <c4d.StopAllThreads>` before making modifications to the scene.
        
        :type id: int
        :param id: The ID of the gadget that triggered the event.
        :type msg: c4d.BaseContainer
        :param msg: The original message container. Contains the following values:
        
        .. include:: /consts/BFM_ACTION.rst
        :start-line: 3
        
        :rtype: bool
        :return: **False** if there was an error, otherwise **True**.
        
        
        """
        ...
    
    def AskClose(self) -> bool:
        """    
        | Override it to avoid closing the dialog if an error situation has occurred.
        | If the user wants to close the dialog with the OK button this function will be called.
        
        .. note::
        
        If you return **False** everything will be as usual, but if you return **True** the dialog won't close.
        
        .. warning::
        
        | Please pay attention to the result value.
        | **True** means, it will **not** close.
        
        :rtype: bool
        :return: **True** if the dialog shouldn't be closed, **False** if it should.
        
        
        """
        ...
    
    def Timer(self, msg: BaseContainer) -> None:
        """    
        If you subscribe to timer events using :meth:`SetTimer` (x), this function is called every x'th millisecond.
        
        :type msg: BaseContainer
        :param msg: The raw timer message.
        
        
        """
        ...
    
    def DestroyWindow(self) -> None:
        """    
        Override this method - this function is called when the dialog is about to be closed temporarily, for example for layout switching.
        
        
        """
        ...
    
    def Open(self, dlgtype: int, pluginid: int, xpos: int, ypos: int, defaultw: int, defaulth: int, subid: int) -> bool:
        """    
        Opens the dialog at the specified position.
        
        .. note::
        
        | If *xpos* = `-1` and *ypos* = `-1` the dialog will be opened at the current mouse position.
        | If *xpos* = `-2` and *ypos* = `-2` the dialog will be opened at the center of the screen.
        
        :type dlgtype: int
        :param dlgtype: The dialog type:
        
        .. include:: /consts/DLG_TYPE.rst
        :start-line: 3
        
        :type pluginid: int
        :param pluginid: The plugin ID of :class:`CommandData <c4d.plugins.CommandData>`.
        :type xpos: int
        :param xpos: The X position of the dialog. See note above.
        :type ypos: int
        :param ypos: The Y position of the dialog. See note above.
        :type defaultw: int
        :param defaultw: The default width in pixels.
        :type defaulth: int
        :param defaulth: The default height in pixels.
        :type subid: int
        :param subid: The dialog sub-ID. This can be used to open several dialogs with a single command plugin for :meth:`CommandData.ExecuteSubID`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Restore(self, pluginid: int, secret: Any) -> bool:
        """    
        Used to restore an asynchronous dialog that has been placed in the users layout.
        
        .. note::
        
        Just use this method in :meth:`CommandData.RestoreLayout`.
        
        :type pluginid: int
        :param pluginid: The plugin ID of the menu plugin.
        :type secret: PyCObject
        :param secret: The `secret` argument of :meth:`CommandData.RestoreLayout`.
        :rtype: bool
        :return: **True** if successfully restored, otherwise **False**.
        
        
        """
        ...
    
    def GetInputState(self, askdevice: int, askchannel: int, res: BaseContainer) -> bool:
        """    
        Polls a certain channel of a device for the current input state.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type askchannel: int
        :param askchannel: The channel to ask.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the state could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def GetInputEvent(self, askdevice: int, res: BaseContainer) -> bool:
        """    
        Gets the next input event for a certain device from the event queue.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the event could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def KillEvents(self) -> None:
        """    
        Flushes all events from the window message queue. For example if you loop while the mouse is down (polling) you can call this command to flush all keydowns/mouseclicks that are made during the loop.
        
        
        """
        ...
    
    def Local2Global(self) -> None:
        """    
        Transforms local coordinates (relative to the top left corner of the dialog) to global coordinates (relative to the top left corner of the physical window). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Global2Local(self) -> None:
        """    
        Transforms global coordinates (relative to the top left corner of the physical window) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Local2Screen(self) -> None:
        """    
        Transforms local coordinates (relative to the top left corner of the dialog) to screen coordinates (relative to the top left corner of the system screen). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Screen2Local(self) -> None:
        """    
        Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def SetDefaultColor(self, id: Union[C4DGadget, int], colorid: int, color: Vector) -> None:
        """    
        Set the default color for GUI elements.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID.
        :type colorid: int
        :param colorid: The color ID. See :doc:`COLOR constants</consts/COLOR>`.
        :type color: c4d.Vector
        :param color: The color.
        
        
        """
        ...
    
    def GetColorRGB(self, colorid: int) -> None:
        """    
        Gets the RGB values associated with a color ID.
        
        :type colorid: int
        :param colorid: The color ID. See :doc:`COLOR constants</consts/COLOR>`.
        :rtype: dict{**r**: int, **g**: int, **b**: int}
        :return: The color in the dict with the keys *r*, *g* and *b*.
        
        
        """
        ...
    
    def CheckValueRanges(self) -> bool:
        """    
        Checks if the value for all input fields are within the allowed range.
        
        :rtype: bool
        :return: **True** if everything is alright, or **False** if any field is wrong.
        
        
        """
        ...
    
    def AddGadget(self, type: int, gadget: int) -> bool:
        """    
        Add a gadget to the dialog.
        
        Several one can be useful:
        
        - c4d.DIALOG_NOMENUBAR to disables the menu bar.
        - c4d. DIALOG_PIN to add the ability to dock the GeDialog.
        
        :param type: The gadget type ID.
        :type type: int
        :param gadget: The gadget ID.
        :type gadget: int
        :return: Success of the addition of the Gadget.
        :rtype: bool
        
        
        """
        ...
    
    def AddCheckbox(self, id: int, flags: int, initw: int, inith: int, name: str) -> C4DGadget:
        """    
        Add a checkbox to the dialog.
        
        .. image:: /_imgs/modules/gui/gedialog_checkbox.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type name: str
        :param name: Name of the checkbox option.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddButton(self, id: int, flags: int, initw: int, inith: int, name: str) -> C4DGadget:
        """    
        Add a button to the dialog.
        
        .. image:: /_imgs/modules/gui/gedialog_button.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type name: str
        :param name: Name of the button.
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddStaticText(self, id: int, flags: int, initw: int, inith: int, name: str, borderstyle: int) -> C4DGadget:
        """    
        Adds a static text field to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_statictext1.png
        
        .. image:: /_imgs/modules/gui/gedialog_statictext2.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type name: str
        :param name: Name of the button.
        :type borderstyle: int
        :param borderstyle: Border style:
        
        .. include:: /consts/BORDER.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddEditText(self, id: int, flags: int, initw: int, inith: int, editflags: int) -> C4DGadget:
        """    
        Adds an editable text field to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_edittextbox.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type editflags: int
        :param editflags: Edit flags:
        
        .. include:: /consts/EDITTEXT.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddMultiLineEditText(self, id: int, flags: int, initw: int, inith: int, style: int) -> C4DGadget:
        """    
        Adds an editable text field with multiple lines to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_multilineedit.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type style: int
        :param style: A combination of the following flags:
        
        .. include:: /consts/DR_MULTILINE.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddEditNumber(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds an editable number field to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_editnumber.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddEditNumberArrows(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds an editable number field with up/down arrows to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_editnumberarrows.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddSlider(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds a slider with an editable number field to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_slider.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddEditSlider(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds a slider with an editable number field to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_editslider.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddColorField(self, id: int, flags: int, initw: int, inith: int, colorflags: int) -> C4DGadget:
        """    
        Adds a simple color field without sliders to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_colorfield.png
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type colorflags: int
        :param colorflags: .. versionadded:: R14.014 Color flags:
        
        .. include:: /consts/DR_COLORFIELD.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddComboBox(self, id: int, flags: int, initw: int, inith: int, specialalign: bool, allowfiltering: bool) -> C4DGadget:
        """    
        Adds a combo box to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_combobox.png
        
        .. note::
        
        To add items to the combo box menu use the :meth:`AddChild` method.
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type specialalign: bool
        :param specialalign:
        
        | Used to quantize the width of the combo box.
        | If this is **True** then the width of the combo box will be a multiple of `initw`.
        | For example if `initw` is 60px and `specialalign` is **True** the width will be 60, 120, 180px and so on.
        
        :type allowfiltering: bool
        :param allowfiltering:
        
        .. versionadded:: R21
        
        **True** to allow keyboard filtering of the combobox list.
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddColorChooser(self, id: int, flags: int, initw: int, inith: int, layoutflags: int, settings: BaseContainer) -> C4DGadget:
        """    
        Adds a color field with sliders to the layout.
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type layoutflags: int
        :param layoutflags: Flags:
        
        .. include:: /consts/DR_COLORFIELD.rst
        :start-line: 3
        
        :type settings: c4d.BaseContainer
        :param settings:
        
        .. versionadded:: R17.048
        
        The color chooser settings.
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddRadioGroup(self, id: int, flags: int, columns: int, rows: int) -> bool:
        """    
        Adds a radio group to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_radiogroup.png
        
        .. note::
        
        To add items to the radio button group use the :meth:`AddChild` function.
        
        :type id: int
        :param id: The control ID.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type columns: int
        :param columns: Number of columns, or 0 if rows is used.
        :type rows: int
        :param rows: Number of rows, or 0 if columns is used.
        :rtype: bool
        :return: **True** if the radio group was added, otherwise **False**.
        
        
        """
        ...
    
    def AddRadioButton(self, id: int, flags: int, initw: int, inith: int, name: str) -> C4DGadget:
        """    
        Adds a radio button to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_radiobutton.png
        
        .. note::
        
        Used with radio groups created with :meth:`AddRadioGroup`.
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type name: str
        :param name: Name of the radio button.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddRadioText(self, id: int, flags: int, initw: int, inith: int, name: str) -> C4DGadget:
        """    
        Adds a text radio button to the layout (like the ones to the left in the Cinema 4D material editor).
        
        .. note::
        
        Used with radio groups created with :meth:`AddRadioGroup`.
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :type name: str
        :param name: Name of the text radio button.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddPopupButton(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds a popup button to the layout.
        
        .. note::
        
        To add items to the popup menu use :meth:`AddChild` or :meth:`SetPopup`.
        
        .. versionadded:: R19
        
        :type id: int
        :param id: The unique ID of the dialog.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddSeparatorH(self, inith: Any, flags: int) -> C4DGadget:
        """    
        Adds a horizontal separator to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_separator1.png
        
        :type initw: int
        :param initw: Initial width.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddSeparatorV(self, initv: int, flags: int) -> C4DGadget:
        """    
        Adds a vertical separator to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_separator1.png
        
        :type initv: int
        :param initv: Initial width.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddCustomGui(self, id: int, pluginid: int, name: str, flags: int, minw: int, minh: int, customdata: BaseContainer) -> None:
        """    
        Adds a custom GUI to the dialog.
        
        :type id: int
        :param id: The ID of the custom GUI to add.
        :type pluginid: int
        :param pluginid: The plugin ID.
        :type name: str
        :param name: The name of the added custom GUI. (Not necessarily used.)
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type minw: int
        :param minw: Minimum width.
        :type minh: int
        :param minh: Minimum height.
        :type customdata: c4d.BaseContainer
        :param customdata: Container with settings for the custom GUI element.
        :rtype: Any :class:`custom GUI <c4d.gui.BaseCustomGui>` class
        :return: The custom GUI that was added, or **None** if an error occured.
        
        .. versionchanged:: R18.057
        
        | The method returns a :class:`BaseCustomGui <c4d.gui.BaseCustomGui>` when there is no class available for the custom GUI.
        | This allows to interact with any custom GUI, calling for instance :meth:`BaseCustomGui.GetData`/:meth:`SetData() <BaseCustomGui.SetData>`.
        
        
        """
        ...
    
    def FindCustomGui(self, id: int, pluginid: int) -> None:
        """    
        Get the custom GUI for a certain ID.
        
        .. note::
        
        The GUI object must have been previously added with :meth:`AddCustomGui`.
        
        :type id: int
        :param id: The ID of the custom GUI.
        :type pluginid: int
        :param pluginid: The plugin ID of the custom GUI.
        :rtype: Any :class:`custom GUI <c4d.gui.BaseCustomGui>` class
        :return: The found custom GUI, or **None** if it could not be retrieved.
        
        .. versionchanged:: R18.057
        
        | The method returns a :class:`BaseCustomGui <c4d.gui.BaseCustomGui>` when there is no class available for the custom GUI.
        | This allows to interact with any custom GUI, calling for instance :meth:`BaseCustomGui.GetData`/:meth:`SetData() <BaseCustomGui.SetData>`.
        
        
        """
        ...
    
    def AddChild(self, id: Union[C4DGadget, int], subid: int, child: str) -> bool:
        """    
        Adds items to combo boxes or popup buttons. The resource equivalent is *CHILDS*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type subid: int
        :param subid: ID of the item to add.
        :type child: str
        :param child: Name of the item to add.
        :rtype: bool
        :return: **True** if the child was added.
        
        
        """
        ...
    
    def FreeChildren(self, id: Union[C4DGadget, int]) -> bool:
        """    
        Clears the item list of combo boxes and popup buttons.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: bool
        :return: **True** if the children were removed.
        
        
        """
        ...
    
    def SetPopup(self, id: Union[C4DGadget, int], bc: BaseContainer) -> bool:
        """    
        Sets the item list of a popup button using a popup menu container.
        
        .. versionadded:: R19
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type bc: c4d.BaseContainer
        :param bc: A container with the items to set.
        :rtype: bool
        :return: **True** if the popup menu was set, otherwise **False**.
        
        
        """
        ...
    
    def AddChildren(self, id: Union[C4DGadget, int], bc: BaseContainer) -> bool:
        """    
        Adds children to a dialog element using a container.
        
        .. versionadded:: R19
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type bc: c4d.BaseContainer
        :param bc: A container with the children to set.
        :rtype: bool
        :return: **True** if  the children were added, otherwise **False**.
        
        
        """
        ...
    
    def AttachUserArea(self, ua: GeUserArea, id: Union[C4DGadget, int], userareaflags: int) -> bool:
        """    
        | Assigns a :class:`GeUserArea <c4d.gui.GeUserArea>` object to a user area control in the dialog.
        | The object will handle all messages to the user area and is responsible for painting the user area.
        |
        | A good practice is to place the :class:`GeUserArea <c4d.gui.GeUserArea>` derived object as a member of
        the :class:`GeDialog <c4d.gui.GeDialog>` derived class.
        
        :type ua: c4d.gui.GeUserArea
        :param ua: A user area object to attach.
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID.
        :type userareaflags: int
        :param userareaflags: Flags for the user area:
        
        .. include:: /consts/USERAREAFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the children were removed.
        
        
        """
        ...
    
    def AddUserArea(self, id: int, flags: int, initw: int, inith: int) -> C4DGadget:
        """    
        Adds a user area to the layout.
        
        .. note::
        
        Use :meth:`AttachUserArea` to assign a :class:`GeUserArea <c4d.gui.GeUserArea>` object to the user area control.
        
        :type id: int
        :param id: The user area ID.
        :type flags: int
        :param flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        
        :rtype: c4d.gui.C4DGadget
        :return: The added gadget.
        
        
        """
        ...
    
    def AddSubDialog(self, id: int, flags: int, initw: int, inith: int) -> bool:
        """    
        Adds a sub-dialog to the layout.
        
        .. note::
        
        Use :meth:`AttachSubDialog` to assign a :class:`c4d.gui.SubDialog` object to the sub-dialog control.
        
        .. versionadded:: R19
        
        :type id: int
        :param id: The sub-dialog ID.
        :type flags: int
        :param flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type initw: int
        :param initw: Initial width.
        :type inith: int
        :param inith: Initial height.
        :rtype: bool
        :return: **True** if the sub-dialog was added, otherwise **False**.
        
        
        """
        ...
    
    def AttachSubDialog(self, userdlg: SubDialog, id: int) -> bool:
        """    
        | Attaches a :class:`c4d.gui.SubDialog` derived object to a sub-dialog control, added with :meth:`AddSubDialog`.
        | To replace the sub-dialog with another one, just call this function again.
        
        .. versionadded:: R19
        
        :type userdlg: c4d.gui.SubDialog
        :param userdlg: The sub-dialog to attach.
        :type id: int
        :param id: The sub-dialog ID.
        :rtype: bool
        :return: **True** if the sub-dialog was attached, otherwise **False**.
        
        
        """
        ...
    
    def AddDlgGroup(self, type: int) -> bool:
        """    
        Adds a dialog group with standard buttons to the layout.
        
        .. image:: /_imgs/modules/gui/gedialog_dlggroup.png
        
        .. note::
        
        | The dialog group contains the standard buttons of a modal dialog (OK and Cancel).
        | By having these grouped together in a single element, Cinema 4D can change the ordering and alignment of the buttons to suit the operation system used.
        
        :type type: int
        :param type: Specifies what standard buttons to include. Can be a combination of:
        
        .. include:: /consts/DLG.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the dialog group was added, otherwise **False**.
        
        
        """
        ...
    
    def GetItemDim(self, id: Union[C4DGadget, int]) -> None:
        """    
        Queries a dialog control for its current position and size in pixels.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID.
        :rtype: dict('x': int, 'y': int, 'w': int, 'h': int)
        :return: A dictionary with the X/Y coordinates of the upper left corner and the width/height of the control.
        
        
        """
        ...
    
    def GetDragPosition(self, msg: BaseContainer) -> None:
        """    
        Extracts local drag coordinates from a drag and drop event.
        
        :type msg: c4d.BaseContainer
        :param msg: The original message.
        :rtype: dict{'x': int, 'y': int}
        :return: The local X and Y position.
        
        
        """
        ...
    
    def GetDragObject(self, msg: BaseContainer) -> None:
        """    
        Extracts the object from a drag and drop message.
        
        :type msg: c4d.BaseContainer
        :param msg: The original message.
        :rtype: dict{'type': int, 'object': any}
        :return: The type of drag and the object itself. The types are:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetDragDestination(self, cursor: int, gadgetid: int) -> bool:
        """    
        Sets the correct cursor during drag and drop handling.
        
        :type cursor: int
        :param cursor: A mouse cursor:
        
        .. include:: /consts/MOUSE.rst
        :start-line: 3
        
        :type gadgetid: int
        :param gadgetid: The dialog element that this cursor is for, or `0`.
        :rtype: bool
        :return: **True** if the cursor could be set, otherwise **False**.
        
        
        """
        ...
    
    def CheckDropArea(self, id: int, msg: BaseContainer, horiz: bool, vert: bool) -> bool:
        """    
        Checks the drag position in a drag event message against a certain dialog element's position in the layout.
        
        .. note::
        
        The check can be limited to only X or Y coordinates.
        
        :type id: int
        :param id: The dialog element that this cursor is for, or `0`.
        :type msg: c4d.BaseContainer
        :param msg: The drag message.
        :type horiz: bool
        :param horiz: If **True** the drag position is checked against the horizontal bounds of the region.
        :type vert: bool
        :param vert: If **True** the drag position is checked against the vertical bounds of the region.
        :rtype: bool
        :return: **True** if the drag message is within the bounds specified, otherwise **False**.
        
        
        """
        ...
    
    def GroupBeginInMenuLine(self) -> None:
        """    
        Begins a group in the menu bar of the dialog.
        
        .. note::
        
        End the group with :meth:`GroupEnd`
        
        
        """
        ...
    
    def GroupWeightsSave(self, id: Union[C4DGadget, int]) -> BaseContainer:
        """    
        Retrieves group weights for group *id*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: c4d.BaseContainer
        :return: A new container with the weights or **None**.
        
        .. include:: /consts/GROUPWEIGHTS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GroupWeightsLoad(self, id: Union[C4DGadget, int], weights: BaseContainer) -> bool:
        """    
        Sets group weights for group *id*.
        
        The group weights are usually absolute values.
        
        .. note::
        
        | If an element has a bigger minimum size the given weight will be ignored.
        | The sum of the weights do not need to be `100`.
        
        .. note::
        
        | A weight value can be negative.
        | In this case the group keeps its size absolute and it is not resized proportionally.
        
        .. code-block:: python
        
        def CreateLayout():
        self.GroupBegin(GRP_SUB,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,2,0,"",c4d.BFV_GRIDGROUP_ALLOW_WEIGHTS)
        
        self.AddStaticText(1000,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        self.AddStaticText(1001,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        
        self.AddStaticText(1002,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        self.AddStaticText(1003,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        
        self.AddStaticText(1004,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        self.AddStaticText(1005,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,0,0,"SubDialog2",c4d.BORDER_THIN_IN)
        
        self.AddEditNumberArrows(1006, c4d.BFH_SCALEFIT)
        
        if not self.weights_saved:
        #initialization code
        
        self.weights.SetInt32(c4d.GROUPWEIGHTS_PERCENT_W_CNT, 2)      # number of columns - has to be equal to the given layout
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL+0,25.0)  # weight for col 1
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL+1,75.0)  # weight for col 2
        
        #set the rows
        self.weights.SetInt32(c4d.GROUPWEIGHTS_PERCENT_H_CNT,4)       # number of rows - has to be equal to the given layout
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL+0,10.0)  # weight for row 1
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL+1,30.0)  # weight for row 2
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL+2,60.0)  # weight for row 3
        self.weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL+3,0.0)   # weight for row 4
        self.weights_saved = True
        
        self.GroupWeightsLoad(GRP_SUB, self.weights)
        self.GroupEnd()
        return True
        
        def Message(self, msg, result):
        if msg.GetId()==c4d.BFM_WEIGHTS_CHANGED:
        #if the weights change because of user interaction you will get notified
        if msg.GetInt32(c4d.BFM_WEIGHTS_CHANGED)==GRP_SUB:
        self.weights = self.GroupWeightsSave(GRP_SUB)
        return GeDialog.Message(self, msg, result)
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type weights: c4d.BaseContainer
        :param weights: The weights to store:
        
        .. include:: /consts/GROUPWEIGHTS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the group weights could be set, otherwise **False**.
        
        
        """
        ...
    
    def ScrollGroupBegin(self, id: int, flags: int, scrollflags: int, initw: int, inith: int) -> bool:
        """    
        Begins a scrollgroup.
        
        :type id: int
        :param id: The scroll group ID.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type scrollflags: int
        :param scrollflags: Additional settings for the scroll group. Can be a combination of the following flags:
        
        .. include:: /consts/SCROLLGROUP.rst
        :start-line: 3
        
        :type initw: int
        :param initw: The initial width of the scroll area.
        :type inith: int
        :param inith: The initial height of the scroll area.
        :rtype: bool
        :return: **True** if scrollgroup was added.
        
        
        """
        ...
    
    def LayoutChanged(self, id: int) -> bool:
        """    
        | Notifies Cinema 4D that the layout of a dynamic group in the dialog has changed.
        | This is usually done by first calling :meth:`LayoutFlushGroup` and then adding new controls.
        
        :type id: int
        :param id: The ID of the changed group.
        :rtype: bool
        :return: **True** if the layout was updated, otherwise **False**.
        
        
        """
        ...
    
    def LayoutChangedNoRedraw(self, id: Union[C4DGadget, int]) -> bool:
        """    
        | Notifies Cinema 4D that the layout of a dynamic group in the dialog has changed.
        | This is usually done by first calling :meth:`LayoutFlushGroup` and then adding new controls.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The ID of the changed group.
        :rtype: bool
        :return: **True** if the layout was updated, otherwise **False**.
        
        
        """
        ...
    
    def Activate(self, id: int) -> bool:
        """    
        Sets the focus to a specific control within the dialog.
        
        :type id: int
        :param id: The control ID.
        :rtype: bool
        :return: **True** if the control was activated.
        
        
        """
        ...
    
    def IsActive(self, id: int) -> bool:
        """    
        Checks if the given gadget has the focus.
        
        :type id: int
        :param id: The control ID.
        :rtype: bool
        :return: **True** if the control is active, otherwise **False**.
        
        
        """
        ...
    
    def LayoutFlushGroup(self, id: int) -> bool:
        """    
        | Removes all controls from a group and places the control insertion point within the group.
        | This makes it possible to have dynamic groups.
        
        .. note::
        
        After all components are added call :meth:`LayoutChanged` with the group ID.
        
        :type id: int
        :param id: The control ID.
        :rtype: bool
        :return: **True** if the group was flushed.
        
        
        """
        ...
    
    def RemoveElement(self, id: int) -> bool:
        """    
        Removes an element from the dialog.
        
        :type id: int
        :param id: The control ID.
        :rtype: bool
        :return: **True** if the element was removed.
        
        
        """
        ...
    
    def HideElement(self, id: int, hide: bool) -> bool:
        """    
        Hides/unhides an element from the dialog.
        
        :type id: int
        :param id: The control ID.
        :type hide: bool
        :param hide: **True** to hide and **False** to unhide.
        :rtype: bool
        :return: **True** if the element was hidden/unhidden.
        
        
        """
        ...
    
    def MenuFlushAll(self) -> bool:
        """    
        | Flushes the menu bar of the dialog, removing all menus.
        |
        | Add menus with :meth:`MenuSubBegin`.
        
        .. note::
        
        Call :meth:`MenuFinished` when all menus and items have been added.
        
        :rtype: bool
        :return: **True** if the menu bar was flushed.
        
        
        """
        ...
    
    def MenuSubBegin(self, string: str) -> bool:
        """    
        | Creates a new menu group.
        | At the top level this means a menu, at lower levels a sub-menu.
        |
        | Add items with :meth:`MenuAddCommand`, :meth:`MenuAddString` or :meth:`MenuAddSeparator`.
        
        .. note::
        
        Call :meth:`MenuSubEnd` when the menu is finished.
        
        :type string: str
        :param string: Name of the sub menu.
        :rtype: bool
        :return: **True** if a menu group could be begun.
        
        
        """
        ...
    
    def MenuSubEnd(self) -> bool:
        """    
        Closes the current menu group, opened with :meth:`MenuSubBegin`.
        
        :rtype: bool
        :return: **True** if the menu group was ended, otherwise **False**.
        
        
        """
        ...
    
    def MenuAddCommand(self, cmdid: int) -> bool:
        """    
        | Adds a command item to the current menu.
        | This can either be a Cinema 4D command or a plugin command.
        
        .. note::
        
        Particularly useful is *IDM_CM_CLOSEWINDOW* to add a close item for dialogs.
        
        :type cmdid: int
        :param cmdid: A Cinema 4D command id or a plugin ID.
        :rtype: bool
        :return: **True** if the command was added.
        
        
        """
        ...
    
    def MenuAddString(self, id: int, string: str) -> bool:
        """    
        Adds a string item to the current menu.
        
        .. note::
        
        :meth:`Command` will be called when the menu item is selected.
        
        :type id: int
        :param id: The item ID.
        :type string: str
        :param string: The item text. Use a *&d&* suffix for disabled and a *c* suffix for checked items.
        :rtype: bool
        :return: **True** if the menu item was added, otherwise **False**.
        
        
        """
        ...
    
    def MenuAddSeparator(self) -> bool:
        """    
        Adds a separator to the current menu.
        
        :rtype: bool
        :return: **True** if a separator was added.
        
        
        """
        ...
    
    def MenuFinished(self) -> bool:
        """    
        Call this function when all menus and all items have been added.
        
        :rtype: bool
        :return: **True** if a separator was added.
        
        
        """
        ...
    
    def MenuInitString(self, id: int, enabled: bool, value: bool) -> bool:
        """    
        | Used to change the enabled/disabled and checked/unchecked state of menu items.
        | Can be called after :meth:`MenuFinished` to update the menu item dynamically.
        
        :type id: int
        :param id: The menu item ID.
        :type enabled: bool
        :param enabled: **True** if the item is enabled, otherwise **False**.
        :type value: bool
        :param value: **True** if the menu item should be checked.
        :rtype: bool
        :return: **True** if the item was set.
        
        
        """
        ...
    
    def TabGroupBegin(self, id: int, flags: int, tabtype: int) -> bool:
        """    
        Begins a tab group.
        
        .. image:: /_imgs/modules/gui/gedialog_tabgroups.png
        
        :type id: int
        :param id: The ID of the group.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type tabtype: int
        :param tabtype: Specifies what kind of tabs to use:
        
        .. include:: /consts/TAB.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if a tab group could be begun, otherwise **False**.
        
        
        """
        ...
    
    def GroupBegin(self, id: int, flags: int, cols: int, rows: int, title: str, groupflags: int, initw: int, inith: int) -> bool:
        """    
        Begins a group.
        
        :type id: int
        :param id: The ID of the group.
        :type flags: int
        :param flags: Layout flags:
        
        .. include:: /consts/BF_Layout.rst
        :start-line: 3
        
        :type cols: int
        :param cols: Columns.
        :type rows: int
        :param rows: Rows
        :type title: str
        :param title: The title.
        :type groupflags: int
        :param groupflags:
        
        Settings for the group. Can be a combination of the following:
        
        .. include:: /consts/BF_GroupLayout.rst
        :start-line: 3
        
        :type initw: int
        :param initw:
        
        .. versionadded:: R14.014
        
        Initial width.
        
        :type inith: int
        :param inith:
        
        .. versionadded:: R14.014
        
        Initial height.
        
        :rtype: bool
        :return: **True** if a group could be begun, otherwise **False**.
        
        
        """
        ...
    
    def GroupEnd(self) -> bool:
        """    
        Ends groups.
        
        :rtype: bool
        :return: **True** if the group was ended, otherwise **False**.
        
        
        """
        ...
    
    def GroupSpace(self, spacex: int, spacey: int) -> bool:
        """    
        | Sets the space in pixels between two elements in the current group.
        | Equivalent to `SPACE` in dialog resources.
        
        :type spacex: int
        :param spacex: The X distance.
        :type spacey: int
        :param spacey: The Y distance.
        :rtype: bool
        :return: **True** if the spacing could be set.
        
        
        """
        ...
    
    def GroupBorder(self, borderstyle: int) -> None:
        """    
        Sets the border type of the current group, and displays the title in the border if possible.
        
        .. note::
        
        | Use :meth:`GroupBorderNoTitle` if you do not have a title.
        | Otherwise there'll be a small gap in the border where the title would be.
        
        :type borderstyle: int
        :param borderstyle: The style:
        
        .. include:: /consts/BORDER.rst
        :start-line: 3
        
        
        """
        ...
    
    def GroupBorderNoTitle(self, borderstyle: int) -> None:
        """    
        Sets the border type of the current group, and displays the title in the border if possible.
        
        :type borderstyle: int
        :param borderstyle: The style:
        
        .. include:: /consts/BORDER.rst
        :start-line: 3
        
        
        """
        ...
    
    def GroupBorderSpace(self, left: int, top: int, right: int, bottom: int) -> bool:
        """    
        Sets the border size around the current group in pixels.
        
        :type left: int
        :param left: The distance to the left of the group.
        :type top: int
        :param top: The distance above the group.
        :type right: int
        :param right: The distance to the right of the group.
        :type bottom: int
        :param bottom: The distance below the group.
        :rtype: bool
        :return: **True** if the border space was set.
        
        
        """
        ...
    
    def Close(self) -> bool:
        """    
        Close the dialog.
        
        :rtype: bool
        :return: **True** if successfully closed, otherwise **False**.
        
        
        """
        ...
    
    def SendMessage(self, gadget: Any, value: BaseContainer) -> object:
        """    
        Sends a message to a dialog gadget.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: c4d.BaseContainer
        :param value: The message container.
        :rtype: object
        :return: Depends on the message.
        
        
        """
        ...
    
    def SendParentMessage(self, msg: BaseContainer) -> bool:
        """    
        Sends a message to the parent dialog.
        
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        :rtype: bool
        :return: **True** if the message was sent.
        
        
        """
        ...
    
    def GetId(self) -> int:
        """    
        Gets the dialog ID.
        
        :rtype: int
        :return: The id.
        
        
        """
        ...
    
    def GetType(self, id: int) -> int:
        """    
        Return the type of a gadget.
        
        :param id: The gadget id.
        :type id: int
        :rtype: int
        :return: The gadget id type.
        
        
        """
        ...
    
    def IsVisible(self) -> bool:
        """    
        Checks if the dialog is visible.
        
        :rtype: bool
        :return: **True** if it is visible, otherwise **False**.
        
        
        """
        ...
    
    def IsOpen(self) -> bool:
        """    
        Checks if the dialog is open.
        
        :rtype: bool
        :return: **True** if it is open, otherwise **False**.
        
        
        """
        ...
    
    def SetTimer(self, value: int) -> None:
        """    
        Initializes the timer clock, so that :meth:`Timer` is called every timer milliseconds. Use :meth:`SetTimer` (0) to stop the clock.
        
        .. note::
        
        | Depending on the speed of the computer, the operating system, the complexity of the dialog and the threads running in the background, there is no guarantee that event messages will occur on a regular basis.
        | Using a value of 500 ms should be no problem but if using a value of 1 ms one might get events with the following time spaces: 3 ms, 76 ms, 15 ms, 19 ms, 67 ms...
        
        .. note::
        
        The timer will be paused while a synchronous dialog is opened in Cinema 4D.
        
        .. warning::
        
        Keep in mind that using small timer values results in heavy message traffic in the application which may slow down Cinema 4D.
        
        :type value: int
        :param value: The timer interval in milliseconds.
        
        
        """
        ...
    
    def SetTitle(self, title: str) -> None:
        """    
        Sets the title of the dialog window.
        
        :type title: str
        :param title: The title.
        
        
        """
        ...
    
    def Enable(self, gadget: Any, enable: Any) -> None:
        """    
        Enables or disables the dialog gadget, depending on the value of *enable*.
        
        :type gadget:  :class:`C4DGadget <c4d.gui.C4DGadget>`
        :param gadget: The dialog gadget
        :type enabled: bool
        :param enabled: **True** means enabled, otherwise **False**.
        
        
        """
        ...
    
    def LoadDialogResource(self, id: int, lr: GeResource, flags: int) -> bool:
        """    
        | Loads an external resource file.
        | This is the preferred method for dialog layout since it gives maximum flexibility and easy multi language support.
        
        .. note::
        
        The dialog loaded is automatically surrounded by an additional outer group, so *flags* means the same as with dialog groups (e.g. *BFV_CENTER*).
        
        :type id: int
        :param id: The dialog ID.
        :type lr: c4d.plugins.GeResource
        :param lr: A loaded resource or **None**. If this is **None** then the global resource singleton is used.
        :type flags: int
        :param flags: Additional layout flags.
        :rtype: bool
        :return: **true** if the dialog was successfully loaded, otherwise **false**.
        
        
        """
        ...
    
    def SetBool(self, id: Union[C4DGadget, int], value: bool) -> bool:
        """    
        Sets the value of checkbox controls.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: bool
        :param value: The new value.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetLong(self, id: Union[C4DGadget, int], value: int, min: int, max: int, step: bool, tristate: Any, min2: int, max2: int) -> bool:
        """    
        .. deprecated:: R15
        Use :meth:`SetInt32` instead.
        
        Sets the value and limits of integer fields.
        
        .. note::
        
        Also used for tab groups, radio buttons and combo boxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: int
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted.
        :type max: int
        :param max: The maximum value accepted.
        :type step: int
        :param step: The step used for arrow buttons.
        :type step: bool
        :param step: If this is **True** the control is tinted blue to indicate tristate mode.
        :type min2: int
        :param min2: The minimum value allowed outside the range used for sliders. Overrides *min* for the acceptance check.
        :type max2: int
        :param max2: The minimum value allowed outside the range used for sliders. Overrides *max* for the acceptance check.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetInt32(self, id: Union[C4DGadget, int], value: int, min: int, max: int, step: bool, tristate: Any, min2: int, max2: int) -> bool:
        """    
        Sets the value and limits of integer fields.
        
        .. versionadded:: R15.037
        
        .. note::
        
        Also used for tab groups, radio buttons and combo boxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: int
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted.
        :type max: int
        :param max: The maximum value accepted.
        :type step: int
        :param step: The step used for arrow buttons.
        :type step: bool
        :param step: If this is **True** the control is tinted blue to indicate tristate mode.
        :type min2: int
        :param min2: The minimum value allowed outside the range used for sliders. Overrides *min* for the acceptance check.
        :type max2: int
        :param max2: The minimum value allowed outside the range used for sliders. Overrides *max* for the acceptance check.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetReal(self, id: Union[C4DGadget, int], value: float, min: int, max: int, step: float, format: int, min2: int, max2: int, quadscale: bool, tristate: bool) -> bool:
        """    
        .. deprecated:: R15
        
        Use :meth:`SetFloat` instead.
        
        Sets the value, unit and limits of float fields.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: float
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted.
        :type max: int
        :param max: The maximum value accepted.
        :type step: float
        :param step: The step used for arrow buttons.
        :type format: int
        :param format: The unit and format of the field. Valid formats are:
        
        .. include:: /consts/FORMAT.rst
        :start-line: 3
        
        :type min2: int
        :param min2: The minimum value allowed outside the range used for sliders. Overrides *min* for the acceptance check.
        :type max2: int
        :param max2: The maximum value allowed outside the range used for sliders. Overrides *max* for the acceptance check.
        :type quadscale: bool
        :param quadscale: If this is **True** a quadratic scale is used for the slider, so that more precision is available for lower values.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetFloat(self, id: Union[C4DGadget, int], value: float, min: int, max: int, step: float, format: int, min2: int, max2: int, quadscale: bool, tristate: bool) -> bool:
        """    
        Sets the value, unit and limits of float fields.
        
        .. versionadded:: R15.037
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: float
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted.
        :type max: int
        :param max: The maximum value accepted.
        :type step: float
        :param step: The step used for arrow buttons.
        :type format: int
        :param format: The unit and format of the field. Valid formats are:
        
        .. include:: /consts/FORMAT.rst
        :start-line: 3
        
        :type min2: int
        :param min2: The minimum value allowed outside the range used for sliders. Overrides *min* for the acceptance check.
        :type max2: int
        :param max2: The maximum value allowed outside the range used for sliders. Overrides *max* for the acceptance check.
        :type quadscale: bool
        :param quadscale: If this is **True** a quadratic scale is used for the slider, so that more precision is available for lower values.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetMeter(self, id: Union[C4DGadget, int], value: float, min: int, max: int, step: float, tristate: bool) -> bool:
        """    
        Sets the value and limits of a meter field.
        
        .. note::
        
        Same as :meth:`SetFloat` with *FORMAT_METER*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: float
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted.
        :type max: int
        :param max: The maximum value accepted.
        :type step: float
        :param step: The step used for arrow buttons.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetDegree(self, id: Union[C4DGadget, int], value: float, min: int, max: int, step: float, tristate: bool) -> bool:
        """    
        Sets the value and limits of an angle field.
        
        .. note::
        
        Same as :meth:`SetFloat` with *FORMAT_DEGREE*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: float
        :param value: The new value.
        :type min: int
        :param min: The minimum angle accepted in degrees.
        :type max: int
        :param max: The maximum angle accepted in degrees.
        :type step: float
        :param step: The step used for arrow buttons in degrees.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetPercent(self, id: Union[C4DGadget, int], value: float, min: int, max: int, step: float, tristate: bool) -> bool:
        """    
        Sets the value and limits of a percent field.
        
        .. note::
        
        Same as :meth:`SetFloat` with *FORMAT_PERCENT*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: float
        :param value: The new value.
        :type min: int
        :param min: The minimum value accepted (percentage units).
        :type max: int
        :param max: The maximum value accepted (percentage units).
        :type step: float
        :param step: The step used for arrow buttons (percentage units).
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetTime(self, id: Union[C4DGadget, int], doc: Any, value: BaseTime, min: BaseTime, max: BaseTime, stepframes: int, tristate: bool) -> bool:
        """    
        Sets the value and limits of a time field.
        
        .. note::
        
        Same as :meth:`SetFloat` with *FORMAT_FRAMES*.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: c4d.BaseTime
        :param value: The new time.
        :type min: c4d.BaseTime
        :param min: The minimum time accepted.
        :type max: c4d.BaseTime
        :param max: The maximum time accepted.
        :type stepframes: int
        :param stepframes: The frame step used for arrow buttons.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetString(self, id: Union[C4DGadget, int], value: str, tristate: bool, flags: int) -> bool:
        """    
        | Sets the text of string controls.
        | Used for all controls that have a text, for example static text fields, edit fields, buttons and checkboxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type value: str
        :param value: The new string.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/EDITTEXT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetColorField(self, id: Union[C4DGadget, int], color: Vector, brightness: float, maxbrightness: float, flags: int) -> bool:
        """    
        Sets the color, brightness and limits of color fields and color choosers.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type color: c4d.Vector
        :param color: The color.
        :type brightness: float
        :param brightness: The new brightness value.
        :type maxbrightness: float
        :param  maxbrightness: The maximum brightness allowed.
        :type flags: int
        :param flags: Controls what parts of a color chooser that are available. Possible values are:
        
        .. include:: /consts/DR_COLORFIELD.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetFilename(self, id: Union[C4DGadget, int], fn: str, tristate: bool) -> bool:
        """    
        Sets the text of string controls, taking the new value from a filename.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type fn: str
        :param fn: The new filename.
        :type tristate: bool
        :param tristate: If this is **True** the control is tinted blue to indicate tristate mode.
        :rtype: bool
        :return: **True** if the value was set.
        
        
        """
        ...
    
    def SetMultiLinePos(self, id: Union[C4DGadget, int], line: int, pos: int) -> bool:
        """    
        Set the cursor position within a dialog multi-line string item.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type line: int
        :param line: The line number.
        :type pos: int
        :param pos: The position within the line.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetMultiLineMode(self, id: Union[C4DGadget, int], mode: int) -> bool:
        """    
        Sets the edit mode for multi-line edit fields.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type mode: int
        :param mode: The multi-line edit mode:
        
        .. include:: /consts/SCRIPTMODE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the multi-line mode was set, otherwise **False**.
        
        
        """
        ...
    
    def GetBool(self, id: Union[C4DGadget, int]) -> bool:
        """    
        Retrieves the value of checkbox controls.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: bool
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetLong(self, id: Union[C4DGadget, int]) -> int:
        """    
        .. deprecated:: R15
        
        Use :meth:`GetInt32` instead.
        
        Retrieves the value of integer fields.
        
        .. note::
        
        Also used for tab groups, radio buttons and combo boxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: int
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetInt32(self, id: Union[C4DGadget, int]) -> int:
        """    
        Retrieves the value of integer fields.
        
        .. versionadded:: R15.037
        
        .. note::
        
        Also used for tab groups, radio buttons and combo boxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: int
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetReal(self, id: Union[C4DGadget, int]) -> float:
        """    
        .. deprecated:: R15
        
        Use :meth:`GetFloat` instead.
        
        Retrieves the value of float fields.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: float
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetFloat(self, id: Union[C4DGadget, int]) -> float:
        """    
        Retrieves the value of float fields.
        
        .. versionadded:: R15.037
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: float
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetVector(self, id_x: Union[C4DGadget, int], id_y: Union[C4DGadget, int], id_z: Union[C4DGadget, int]) -> Vector:
        """    
        Retrieves the value of three float fields at the same time as a vector.
        
        :type id_x: Union[c4d.gui.C4DGadget, int]
        :param id_x: The control ID of the X field.
        :type id_y: Union[c4d.gui.C4DGadget, int]
        :param id_y: The control ID of the Y field.
        :type id_z: Union[c4d.gui.C4DGadget, int]
        :param id_z: The control ID of the Z field.
        :rtype: c4d.Vector
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetString(self, id: Union[C4DGadget, int]) -> str:
        """    
        | Retrieves the text from string controls.
        | Used for all controls that have a text, for example static text fields, edit fields, buttons and checkboxes.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: str
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetColorField(self, id: Union[C4DGadget, int]) -> None:
        """    
        Retrieves the color and brightness of color controls.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: dict{**brightness**: float, **color**: :class:`Vector <c4d.Vector>`}
        :return: The value or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetTime(self, id: Union[C4DGadget, int], doc: BaseDocument) -> BaseTime:
        """    
        Retrieves the time of time fields.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :rtype: c4d.BaseTime
        :return: The time or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def GetFilename(self, id: Union[C4DGadget, int]) -> str:
        """    
        Retrieves the text from string controls as a filename.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: str
        :return: The time or **None** if the value was not retrieved.
        
        
        """
        ...
    
    def CheckTristateChange(self, id: Union[C4DGadget, int]) -> bool:
        """    
        Indicates whatever a control's content has been changed since the last time its value was set manually with.
        
        :type id: Union[c4d.gui.C4DGadget, int]
        :param id: The control ID or int.
        :rtype: bool
        :return: **True** if the control has been changed, otherwise **False**.
        
        
        """
        ...
    
    def GetVisibleArea(self, scrollgroup: int) -> None:
        """    
        | Queries a scroll group for its currently visible region, a rectangle between (**x1,y1**) and (**x2,y2**).
        | The coordinates are in pixels.
        
        :type scrollgroup: int
        :param scrollgroup: The scroll group ID.
        :rtype: dict{**x1**: int, **y1**: int , **x2**: int , **y2**: int }
        :return: The visible area in coordinates, in keys **x1**, **y1**, **x2**, **y2**.
        
        
        """
        ...
    
    def SetVisibleArea(self, scrollgroupid: Any, x1: int, y1: int, x2: int, y2: int) -> bool:
        """    
        | Scrolls a scroll group so that the rectangle between (*x1,y1*) and (*x2,y2*) is visible.
        | The coordinates are in pixels.
        
        .. note::
        
        | If the area is smaller than the scroll group then it is moved only as much as necessary.
        | If the area is bigger than the scroll group then the top left corners are aligned.
        
        :type scrollgroup: int
        :param scrollgroup: The scroll group ID.
        :type x1: int
        :param x1: The X coordinate of the top left corner of the rectangle.
        :type y1: int
        :param y1: The Y coordinate of the top left corner of the rectangle.
        :type x2: int
        :param x2: The X coordinate of the bottom right corner of the rectangle.
        :type y2: int
        :param y2: The Y coordinate of the bottom right corner of the rectangle.
        :rtype: bool
        :return: **True** if the group was scrolled or already had the right view.
        
        
        """
        ...
    

class SubDialog(GeDialog):
    ...

class GeUserArea(object):
    def __init__(self) -> None:
        """    
        Creates a user area that is not attached to any dialog.
        
        .. note::
        
        The user area must be attached to a dialog with :meth:`GeDialog.AttachUserArea` before it can be used.
        
        :rtype: c4d.gui.GeUserArea
        :return: A new user area.
        
        
        """
        ...
    
    def Init(self) -> bool:
        """    
        | Called once when the user area is initialized by the GUI, before the layout is calculated.
        | Override this function if you need to initialize anything.
        
        .. note::
        
        Return **True** if successful, or **False** to signalize an error.
        
        :rtype: bool
        :return: **True** if successful, or **False** to signalize an error.
        
        
        """
        ...
    
    def InitValues(self) -> bool:
        """    
        | Called after the layout is calculated, before the user area is drawn.
        | Override this function if you need to initialize anything.
        
        .. note::
        
        Return **True** if successful, or **False** to signalize an error.
        
        :rtype: bool
        :return: **True** if successful, or **False** to signalize an error.
        
        
        """
        ...
    
    def GetMinSize(self) -> Tuple[int, int]:
        """    
        Override this function to specify a minimum size for the user area.
        
        .. code-block:: python
        
        def GetMinSize(self):
        #do a calculation here
        return self.width, self.height
        
        :rtype: tuple(int, int)
        :return: A tuple with two elements just like this.
        
        
        """
        ...
    
    def DrawMsg(self, x1: int, y1: int, x2: int, y2: int, msg: BaseContainer) -> None:
        """    
        | Called when Cinema 4D wants you to draw your userarea.
        | Use the drawing functions to update your user area in the region specified by the rectangle from (x1,y1) to (x2,y2).
        
        :type x1: int
        :param x1: The upper left x coordinate.
        :type y1: int
        :param y1:  The upper left y coordinate.
        :type x2: int
        :param x2: The lower right x coordinate.
        :type y2: int
        :param y2: The lower right y coordinate.
        :type msg: c4d.BaseContainer
        :param msg: A mesage container.
        
        
        """
        ...
    
    def InputEvent(self, msg: BaseContainer) -> bool:
        """    
        | Called when an input event is received.
        | The information about the input event is stored in the *msg* container.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type msg: c4d.BaseContainer
        :param msg: The event container.
        :rtype: bool
        :return: **True** if the event was handled, otherwise **False**.
        
        
        """
        ...
    
    def CoreMessage(self, id: int, msg: BaseContainer) -> bool:
        """    
        | Called when a Cinema 4D core messages is received.
        | The message type is given by *id* and the message information is stored in *msg*.
        
        :type id: int
        :param id: The message ID:
        
        .. include:: /consts/EVMSG.rst
        :start-line: 3
        
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        :rtype: bool
        :return: Currently not used - but you have to return a bool value.
        
        
        """
        ...
    
    def Sized(self, w: int, h: int) -> None:
        """    
        Called when the user area is resized.
        
        .. note::
        
        Override if you need to update anything.
        
        :type w: int
        :param w: The new width in pixels.
        :type h: int
        :param h: The new height in pixels.
        
        
        """
        ...
    
    def Timer(self, msg: BaseContainer) -> None:
        """    
        | If you subscribe to timer events using :meth:`SetTimer` (x), this function is called every *x* th millisecond.
        | The raw timer message is stored in *msg*.
        
        :type msg: c4d.BaseContainer
        :param msg: The timer message container.
        
        
        """
        ...
    
    def Message(self, msg: BaseContainer, result: BaseContainer) -> int:
        """    
        Override this function to react to more messages than covered by the other functions. Normally this is not necessary.
        
        .. note::
        
        If overridden, include a call to the base version of this function, :meth:`GeUserArea.Message`:
        
        .. code-block:: python
        
        def Message(self, msg, result):
        if msg.GetId():
        #Do something
        return True
        
        return c4d.gui.GeUserArea.Message(self, msg, result)
        
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        :type result: c4d.BaseContainer
        :param result: A container to store results in.
        :rtype: int
        :return: The return value depends on the message.
        
        
        """
        ...
    
    def Redraw(self, thread: bool) -> None:
        """    
        Forces the user area to redraw itself.
        
        :type thread: bool
        :param thread: Must be set to **True** if the function is called from another thread than the main Cinema 4D thread.
        
        
        """
        ...
    
    def SendParentMessage(self, msg: BaseContainer) -> None:
        """    
        Use this function to send a custom message to the parent dialog.
        
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        
        
        """
        ...
    
    def GetId(self) -> int:
        """    
        Returns the ID of the user area.
        
        :rtype: int
        :return: The ID.
        
        
        """
        ...
    
    def GetWidth(self) -> int:
        """    
        Returns the width of the user area.
        
        :rtype: int
        :return: Width in pixels.
        
        
        """
        ...
    
    def GetHeight(self) -> int:
        """    
        Returns the height of the user area.
        
        :rtype: int
        :return: Height in pixels.
        
        
        """
        ...
    
    def IsEnabled(self) -> bool:
        """    
        Indicates the enabled state.
        
        :rtype: bool
        :return: **True** if the user area is enabled in the dialog, otherwise **False**.
        
        
        """
        ...
    
    def HasFocus(self) -> bool:
        """    
        Indicates the focus state.
        
        :rtype: bool
        :return: **True** if the user area has the focus in the dialog, otherwise **False**.
        
        
        """
        ...
    
    def SetTimer(self, x: int) -> None:
        """    
        Initializes the timer clock, so that :meth:`Timer` is called every timer milliseconds.
        
        .. note::
        
        | Depending on the speed of the computer, the operating system, the complexity of the dialog and the threads running in the background, there is no guarantuee that event messages will occur on a regular basis.
        | Using a value of 500 ms should be no problem but if using a value of 1 ms one might get events with the following time spaces: 3 ms, 76 ms, 15 ms, 19 ms, 67 ms...
        
        .. note::
        
        | Keep in mind that using small timer values results in heavy message traffic in the application which may slow down Cinema 4D (and all other applications running on the computer) to a point where nothing is working any longer besides your dialog.
        
        :type x: int
        :param x: The timer interval in milliseconds.
        
        
        """
        ...
    
    def GetInputState(self, askdevice: int, askchannel: int, res: BaseContainer) -> bool:
        """    
        Polls a certain channel of a device for the current input state.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type askchannel: int
        :param askchannel: The channel to ask.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the state could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def GetInputEvent(self, askdevice: int, res: BaseContainer) -> bool:
        """    
        Gets the next input event for a certain device from the event queue.
        
        .. seealso::
        
        :doc:`Input Events </misc/inputevents>`.
        
        :type askdevice: int
        :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
        :type res: c4d.BaseContainer
        :param res: The result container.
        :rtype: bool
        :return: **True** if the event could be retrieved in *res*, otherwise **False**.
        
        
        """
        ...
    
    def KillEvents(self) -> None:
        """    
        Flushes all events from the window message queue.
        
        .. note::
        
        For example if you loop while the mouse is down (polling) you can call this command to flush all keydowns/mouseclicks that are made during the loop.
        
        
        """
        ...
    
    def IsHotkeyDown(self, id: int) -> int:
        """    
        Checks the standard navigation hotkeys.
        
        :type id: int
        :param id: The hotkey to check:
        
        .. include:: /consts/HOTKEY.rst
        :start-line: 3
        
        :rtype: int
        :return: A value != 0 if the hotkey is pressed.
        
        .. include:: /consts/HOTKEYFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetColorRGB(self, colorid: int) -> None:
        """    
        Gets the RGB values associated with a color ID.
        
        :type colorid: int
        :param colorid: The color ID. See :doc:`COLOR constants</consts/COLOR>`.
        :rtype: dict{**r**: int, **g**: int, **b**: int}
        :return: The color from 0 to 255 in the dict with the keys *r*, *g* and *b*.
        
        
        """
        ...
    
    def DrawSetPen(self, color: Vector) -> None:
        """    
        Sets the draw color.
        
        :type color: c4d.Vector
        :param color: The color to set from 0.0 to 1.0.
        
        
        """
        ...
    
    def DrawSetTextCol(self, fg: Vector, bg: Vector) -> None:
        """    
        Sets the draw color.
        
        :type fg: c4d.Vector
        :param fg: A color vector from 0.0 to 1.0.
        :type bg: c4d.Vector
        :param bg: A color vector from 0.0 to 1.0.
        
        
        """
        ...
    
    def DrawLine(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Draws a line with the current pen color between (*x1,y1*) and (*x2,y2*).
        
        :type x1: int
        :param x1: The X start coordinate.
        :type y1: int
        :param y1: The Y start coordinate.
        :type x2: int
        :param x2: The X end coordinate.
        :type y2: int
        :param y2: The Y end coordinate.
        
        
        """
        ...
    
    def DrawRectangle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).
        
        :type x1: int
        :param x1: The X coordinate of the first corner.
        :type y1: int
        :param y1: The Y coordinate of the first corner.
        :type x2: int
        :param x2: The X coordinate of the opposite corner.
        :type y2: int
        :param y2: The Y coordinate of the opposite corner.
        
        
        """
        ...
    
    def DrawBitmap(self, bmp: BaseBitmap, wx: int, wy: int, ww: int, wh: int, x: int, y: int, w: int, h: int, mode: int) -> None:
        """    
        | Draws a bitmap into the user area.
        | The region *(x,y)* to *(x+w,y+h)* from the bitmap will be scaled and transformed into the region *(wx,wy)* to *(wx+ww,wy+wh)* of the destination area.
        
        .. note::
        
        *BMP_ALLOWALPHA* can be combined with the other modes.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The bitmap to draw.
        :type wx: int
        :param wx: X coordinate of the upper left corner of the destination area.
        :type wy: int
        :param wy: Y coordinate of the upper left corner of the destination area.
        :type ww: int
        :param ww: Width of the destination area.
        :type wh: int
        :param wh: Height of the destination area.
        :type x: int
        :param x: X coordinate of the upper left corner of the bitmap area.
        :type y: int
        :param y: Y coordinate of the upper left corner of the bitmap area.
        :type w: int
        :param w: Width of the bitmap area.
        :type h: int
        :param h: Height of the bitmap area.
        :type mode: int
        :param mode: Can be a combination of the following flags:
        
        .. include:: /consts/BMP.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawBorder(self, type: int, x1: int, y1: int, x2: int, y2: int) -> None:
        """    
        Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).
        
        :type type: int
        :param type: The border type. Possible values:
        
        .. include:: /consts/BORDER.rst
        :start-line: 3
        
        :type x1: int
        :param x1: The X coordinate of the first corner.
        :type y1: int
        :param y1: The Y coordinate of the first corner.
        :type x2: int
        :param x2: The X coordinate of the opposite corner.
        :type y2: int
        :param y2: The Y coordinate of the opposite corner.
        
        
        """
        ...
    
    def DrawText(self, text: str, x: int, y: int, flags: int) -> None:
        """    
        Draws the string *txt* with the upper left corner at the position (*x*, *y*).
        
        .. note::
        
        Use :meth:`DrawGetTextWidth` and :meth:`DrawGetFontHeight` to find out where to place the text.
        
        :type text: str
        :param text: The string to draw.
        :type x: int
        :param x: X coordinate of the upper left corner of the drawn text.
        :type y: int
        :param y: Y coordinate of the upper left corner of the drawn text.
        :type flags: int
        :param flags: Flags.
        
        
        """
        ...
    
    def DrawBezier(self, sx: float, sy: float, p: List[float], closed: bool, filled: bool) -> None:
        """    
        Draws concatenated bezier curves.
        
        .. versionadded:: R14.014
        
        .. note::
        
        Due to improve speed performance, the elements of *p* will be modified and might be invalid and all values must be set again if :meth:`DrawBezier` will be called again with the same array.
        
        :type sx: float
        :param sx: X coordinate of the upper left corner of the drawn curve. This is the X coordinate of the starting point.
        :type sy: float
        :param sy: Y coordinate of the upper left corner of the drawn curve. This is the Y coordinate of the starting point.
        :type p: array of float
        :param p: An array with the bezier curves points.
        
        Here is an example of initializing the curve points array.
        
        .. code-block:: python
        
        points = array.array('f', xrange(6))
        
        points[0] = 35  # The X coordinate of the control point for the starting point.
        points[1] = 200 # The Y coordinate of the control point for the starting point.
        points[2] = 220 # The X coordinate of the control point for the ending point.
        points[3] = 260 # The Y coordinate of the control point for the ending point.
        points[4] = 220 # The X coordinate of the ending point.
        points[5] = 40 # The Y coordinate of the ending point.
        
        self.DrawBezier(120, 160, points, False, False)
        
        :type closed: bool
        :param closed: If **True**, the last point of the last segment connects back to the starting point ( *sx* , *sy*).
        :type filled: bool
        :param filled: If **True**, fills the drawn bezier curves, only if it is also *closed*.
        
        
        """
        ...
    
    def FillBitmapBackground(self, bmp: BaseBitmap, offsetx: int, offsety: int) -> None:
        """    
        | Fills the bitmap *bmp* with the current pen color.
        | The *offsetx* and *offsety* parameters are used when the background is a pattern and are given in local coordinates of the user area.
        
        .. note::
        
        This can be used to make semi-transparent bitmap blits.
        
        :type bmp: c4d.bitmaps.BaseBitmap
        :param bmp: The bitmap to fill.
        :type offsetx: int
        :param offsetx: The X offset in pixels.
        :type offsety: int
        :param offsety: The X offset in pixels.
        
        
        """
        ...
    
    def DrawSetFont(self, fontid: int) -> None:
        """    
        Sets the text font.
        
        :type fontid: int
        :param fontid: The font to use:
        
        .. include:: /consts/FONT.rst
        :start-line: 3
        
        
        """
        ...
    
    def DrawGetTextWidth(self, text: str) -> int:
        """    
        Returns the width in pixels of the string *text*, if it were drawn in the current font.
        
        :type text: str
        :param text: The string to measure.
        :rtype: int
        :return: The width in pixels.
        
        
        """
        ...
    
    def DrawGetFontHeight(self) -> int:
        """    
        Returns the height in pixels of a line of text in the current font.
        
        :rtype: int
        :return: Height in pixels.
        
        
        """
        ...
    
    def DrawGetFontBaseLine(self) -> int:
        """    
        Returns the base line of the set font.
        
        :rtype: int
        :return: The base line of the set font.
        
        
        """
        ...
    
    def DrawSetTextRotation(self, textrotation: float) -> None:
        """    
        Rotates the font for drawing.
        
        .. note::
        
        Rotation is clockwise and must be set to 0 after drawing.
        
        :type textrotation: float
        :param textrotation: The text rotation in degree.
        
        
        """
        ...
    
    def SetClippingRegion(self, x: int, y: int, w: int, h: int) -> None:
        """    
        | Should be used at the top of the :meth:`DrawMsg` function to specify the clipping region.
        | Without specifying a dedicated clipping region everything will be painted, even if it is outside the user area!
        
        .. note::
        
        The method :meth:`OffScreenOn` automatically sets the clipping region to the whole user area, so normally this function is not necessary.
        
        :type x: int
        :param x: X coordinate of the upper left corner of the clipping region.
        :type y: int
        :param y: Y coordinate of the upper left corner of the clipping region.
        :type w: int
        :param w: Width of the clipping region.
        :type h: int
        :param h: Height of the clipping region.
        
        
        """
        ...
    
    def ClearClippingRegion(self) -> None:
        """    
        Clears any clipping region set with :meth:`SetClippingRegion`.
        
        
        """
        ...
    
    def OffScreenOn(self, x: int, y: int, w: int, h: int) -> bool:
        """    
        | Enables double buffering to avoid blinking and flickering effects.
        | Sets the clipping area to the rectangular area determined by *x*, *y*, *w* and *h*.
        | If x == c4d.NOTOK the size will be calculated automatically.
        
        .. note::
        
        The GUI will automatically switch planes.
        
        .. note::
        
        Just call this function before drawing things.
        
        :type x: int
        :param x: X-coordinate of the clipping area.
        :type y: int
        :param y: Y-coordinate of the clipping area.
        :type w: int
        :param w: Width of the clipping area.
        :type h: int
        :param h: Height of the clipping area.
        :rtype: bool
        :return: **True** if double buffering could be enabled, otherwise **False**.
        
        
        """
        ...
    
    def ScrollArea(self, xdiff: int, ydiff: int, x: int, y: int, w: int, h: int) -> None:
        """    
        Scrolls the area from *(x,y)* to *(x+w,y+h)* in the direction specified by *xdiff* and *ydiff*.
        
        :type xdiff: int
        :param xdiff: X distance to scroll.
        :type ydiff: int
        :param ydiff: Y distance to scroll.
        :type x: int
        :param x: X coordinate of the upper left corner of the area to scroll.
        :type y: int
        :param y: Y coordinate of the upper left corner of the area to scroll.
        :type w: int
        :param w: Width of the area to scroll.
        :type h: int
        :param h: Height of the area to scroll.
        
        
        """
        ...
    
    def ActivateFading(self, milliseconds: int) -> None:
        """    
        Activates the fading.
        
        .. versionadded:: R14.014
        
        :type milliseconds: int
        :param milliseconds: Time for the fading.
        
        
        """
        ...
    
    def AdjustColor(self, colorid: int, highlightid: int, percent: float) -> None:
        """    
        Sets the blend colors for user area fading.
        
        .. versionadded:: R14.014
        
        :type colorid: int
        :param colorid: A color ID to fade from. See :doc:`COLOR constants</consts/COLOR>`.
        :type highlightid: int
        :param highlightid: A color ID to fade to. See :doc:`COLOR constants</consts/COLOR>`.
        :type percent: float
        :param percent: Fading percentage.
        
        
        """
        ...
    
    def Local2Global(self) -> None:
        """    
        Transforms local coordinates (relative to the top left corner of the dialog) to global coordinates (relative to the top left corner of the physical window). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Global2Local(self) -> None:
        """    
        Transforms global coordinates (relative to the top left corner of the physical window) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Local2Screen(self) -> None:
        """    
        Transforms local coordinates (relative to the top left corner of the dialog) to screen coordinates (relative to the top left corner of the system screen). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def Screen2Local(self) -> None:
        """    
        Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.
        
        :rtype: dict{**x**: int, **y**: int}
        :return: The converted coordinates or **None**.
        
        
        """
        ...
    
    def LayoutChanged(self) -> None:
        """    
        Tells Cinema 4D that the user area now has new dimensions. That causes c4d to call:
        
        1. :meth:`GetMinSize`
        2. :meth:`Sized`
        3. :meth:`InitValues`
        4. :meth:`DrawMsg`
        
        
        """
        ...
    
    def GetDragPosition(self, msg: BaseContainer) -> None:
        """    
        Extracts local drag coordinates from a drag and drop event.
        
        :type msg: c4d.BaseContainer
        :param msg: The original message.
        :rtype: dict{'x': int, 'y': int}
        :return: The local X and Y position.
        
        
        """
        ...
    
    def GetDragObject(self, msg: BaseContainer) -> None:
        """    
        Extracts the object from a drag and drop message.
        
        :type msg: c4d.BaseContainer
        :param msg: The original message.
        :rtype: dict{'type': int, 'object': any}
        :return: The type of drag and the object itself. The types are:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def HandleMouseDrag(self, msg: BaseContainer, type: int, data: Any, dragflags: int) -> bool:
        """    
        Starts a drag and drop operation.
        
        .. versionadded:: R19.024
        
        :type msg: c4d.BaseContainer
        :param msg: The mouse event message that triggered the drag and drop.
        :type type: int
        :param type: The type of *data*:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        :type data: any
        :param data: Depends on *type*.
        :type dragflags: int
        :param dragflags: The drag flags. Private.
        :rtype: bool
        :return:
        
        | **True** if the user moved the mouse and a drag and drop operation was initiated.
        | **False** if the user did not move the mouse, so that the original event is a normal mouse click event.
        
        
        """
        ...
    
    def SetDragDestination(self, cursor: int) -> bool:
        """    
        Sets the correct cursor during drag and drop handling.
        
        :type cursor: int
        :param cursor: A mouse cursor:
        
        .. include:: /consts/MOUSE.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the cursor could be set, otherwise **False**.
        
        
        """
        ...
    
    def CheckDropArea(self, msg: BaseContainer, horiz: bool, vert: bool) -> bool:
        """    
        Checks the drag position in a drag event message against the user area's position in the layout.
        
        .. note::
        
        The check can be limited to only X or Y coordinates.
        
        :type msg: c4d.BaseContainer
        :param msg: The drag message.
        :type horiz: bool
        :param horiz: If **True** the drag position is checked against the horizontal bounds of the region.
        :type vert: bool
        :param vert: If **True** the drag position is checked against the vertical bounds of the region.
        :rtype: bool
        :return: **True** if the drag message is within the bounds specified, otherwise **False**.
        
        
        """
        ...
    
    def MouseDragStart(self, button: int, mx: float, my: float, flag: int) -> None:
        """    
        | Starts a mouse drag. Only call this when a mouse down message is received.
        | Then repeatedly poll with :meth:`MouseDrag` during the drag.
        
        :type button: int
        :param button: The mouse button that is pressed:
        
        .. include:: /consts/BFM_INPUT_MOUSE.rst
        :start-line: 3
        
        :type mx: float
        :param mx: The X position of the mouse.
        :type my: float
        :param my: The Y position of the mouse.
        :type flag: int
        :param flag: The mouse drag flags:
        
        .. include:: /consts/MOUSEDRAGFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def MouseDrag(self) -> None:
        """    
        Polls the mouse during a drag started with :meth:`MouseDragStart`.
        
        The best way to use this function is.
        
        .. code-block:: python
        
        while True:
        result, mx, mx, channels = ua.MouseDrag()
        if result != c4d.MOUSEDRAGRESULT_CONTINUE:
        break
        
        To check for qualifiers see the channels container.
        
        .. code-block:: python
        
        if channels[c4d.BFM_INPUT_QUALIFIER] & QSHIFT:
        ...
        if channels[c4d.BFM_INPUT_QUALIFIER] & QCTRL:
        ...
        
        :rtype: tuple(int, float, float, :class:`c4d.BaseContainer`)
        :return: A tuple with the following information:
        
        int: The mouse drag result:
        
        .. include:: /consts/MOUSEDRAGRESULT.rst
        :start-line: 3
        
        | float: The X delta-coordinate of the mouse (the amount the mouse has moved).
        | float: The Y delta-coordinate of the mouse (the amount the mouse has moved).
        | :class:`c4d.BaseContainer`: The channels values. Also contains these pen values:
        
        .. include:: /consts/PEN.rst
        :start-line: 3
        
        
        """
        ...
    
    def MouseDragEnd(self) -> int:
        """    
        Checks why the mouse drag ended. Allows to perform any undo operations needed if the user canceled the drag.
        
        :rtype: int
        :return: The mouse drag result:
        
        .. include:: /consts/MOUSEDRAGRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetBorderSize(self, type: int) -> None:
        """    
        Retrieves the space required to draw a border.
        
        :type type: int
        :param type: The border type:
        
        .. include:: /consts/BORDER.rst
        :start-line: 3
        
        :rtype: dict{**l**: int, **t**: int, **r**: int, **b**: int}
        :return: The space.
        
        
        """
        ...
    

class TreeViewFunctions(object):
    def GetFirst(self, root: Any, userdata: Any) -> Any:
        """    
        Called to retrieve the first object of the tree.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :rtype: Any
        :return: The first object.
        
        
        """
        ...
    
    def GetDown(self, root: Any, userdata: Any, obj: Any) -> Any:
        """    
        Called to retrieve the first child of *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: Any
        :return: The first child of *obj*.
        
        
        """
        ...
    
    def GetNext(self, root: Any, userdata: Any, obj: Any) -> Any:
        """    
        Called to retrieve the object after *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: Any
        :return: The object after *obj*.
        
        
        """
        ...
    
    def GetPred(self, root: Any, userdata: Any, obj: Any) -> Any:
        """    
        Called to retrieve the object before *obj*.
        
        .. note::
        
        This is only used for drag and drop checks.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: Any
        :return: The object before *obj*.
        
        
        """
        ...
    
    def GetColumnWidth(self, root: Any, userdata: Any, obj: Any, col: int, area: GeUserArea) -> int:
        """    
        Called to retrieve the column width of object *obj* in column *col*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type col: int
        :param col: The column index.
        :type area: c4d.gui.GeUserArea
        :param area: The user area used to determine the text width with :meth:`GeUserArea.DrawGetTextWidth`.
        :rtype: int
        :return: The column width.
        
        
        """
        ...
    
    def GetHeaderColumnWidth(self, root: Any, userdata: Any, col: int, area: GeUserArea) -> int:
        """    
        Called to retrieve the width of the header for column *col*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type col: int
        :param col: The column index.
        :type area: c4d.gui.GeUserArea
        :param area: The user area used to determine the text width with :meth:`GeUserArea.DrawGetTextWidth`.
        :rtype: int
        :return: The header column width, or a negative number for auto header width.
        
        
        """
        ...
    
    def GetMinHeaderHeight(self, root: Any, userdata: Any, area: GeUserArea) -> int:
        """    
        Called to retrieve the minimum header height.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type area: c4d.gui.GeUserArea
        :param area: The user area used to determine the text height with :meth:`GeUserArea.DrawGetFontHeight`.
        :rtype: int
        :return: The minimum header height, or a negative value for auto header height.
        
        
        """
        ...
    
    def GetLineHeight(self, root: Any, userdata: Any, obj: Any, col: int, area: GeUserArea) -> int:
        """    
        Called to retrieve the line height of object *obj* in column *col*.
        
        .. note::
        
        Always return a positive value.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type col: int
        :param col: The column index.
        :type area: c4d.gui.GeUserArea
        :param area: The user area used to determine the text height with :meth:`GeUserArea.DrawGetFontHeight`.
        :rtype: int
        :return: The line height.
        
        
        """
        ...
    
    def GetColors(self, root: Any, userdata: Any, obj: Any) -> None:
        """    
        Called to specify the text colors of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: tuple(int or :class:`c4d.Vector`, int or :class:`c4d.Vector`) or list(int or :class:`c4d.Vector`, int or :class:`c4d.Vector`)
        :return: The normal and selected text color as color ID or vector.
        
        
        """
        ...
    
    def GetBackgroundColor(self, root: Any, userdata: Any, obj: Any, line: int) -> None:
        """    
        Called to specify the background color of *line*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type line: int
        :param line: The line index.
        :rtype: int or :class:`c4d.Vector`
        :return: The background color for *line* as color ID or vector.
        
        
        """
        ...
    
    def DrawCell(self, root: Any, userdata: Any, obj: Any, col: int, drawinfo: Dict[str, Any]) -> None:
        """    
        Called to draw the cell for object *obj* in column *col* into the user *area* in *drawinfo['frame']*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type col: int
        :param col: The column index.
        :type drawinfo: dict
        :param drawinfo: The draw information. See :ref:`drawInfo_dict`.
        :rtype: int or :class:`c4d.Vector`
        :return: The background color as color ID or vector.
        
        
        """
        ...
    
    def DrawHeaderCell(self, root: Any, userdata: Any, col: int, drawinfo: Dict[str, Any]) -> bool:
        """    
        Called to draw the header for column *col* into the user *area* in *drawinfo['frame']*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type col: int
        :param col: The column index.
        :type drawinfo: dict
        :param drawinfo: The draw information. See :ref:`drawInfo_dict`.
        :rtype: bool
        :return: **True** if the header has been drawn or **False** if the header should be drawn by the tree view.
        
        
        """
        ...
    
    def IsSelected(self, root: Any, userdata: Any, obj: Any) -> bool:
        """    
        Called to retrieve the selection status of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: bool
        :return: **True** if the object is selected, otherwise **False**.
        
        
        """
        ...
    
    def Select(self, root: Any, userdata: Any, obj: Any, mode: int) -> None:
        """    
        Called to select object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type mode: int
        :param mode: The selection mode:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsOpened(self, root: Any, userdata: Any, obj: Any) -> bool:
        """    
        Called to retrieve the folding status of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: bool
        :return: **True** if the object is opened, otherwise **False**.
        
        
        """
        ...
    
    def Open(self, root: Any, userdata: Any, obj: Any, onoff: bool) -> None:
        """    
        Called to open or close object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type onoff: bool
        :param onoff: **True** if *obj* should be opened, otherwise **False**.
        
        
        """
        ...
    
    def GetName(self, root: Any, userdata: Any, obj: Any) -> str:
        """    
        Called to retrieve the name of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: str
        :return: The object name.
        
        
        """
        ...
    
    def SetName(self, root: Any, userdata: Any, obj: Any, str: str) -> None:
        """    
        Called to set the name of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type str: str
        :param str: The new object name.
        
        
        """
        ...
    
    def GetID(self, root: Any, userdata: Any, obj: Any) -> int:
        """    
        Called to retrieve the ID of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: int
        :return: The object ID.
        
        
        """
        ...
    
    def IsChecked(self, root: Any, userdata: Any, obj: Any, lColumn: int) -> int:
        """    
        Called to retrieve the checkbox status of object *obj* for column *lColumn*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type lColumn: int
        :param lColumn: The column index.
        :rtype: int
        :return: A combination of the following flags or **c4d.NOTOK** to show no checkbox:
        
        .. include:: /consts/LV_CHECKBOX.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetCheck(self, root: Any, userdata: Any, obj: Any, lColumn: int, bCheck: bool, bcMsg: BaseContainer) -> None:
        """    
        Called to set the checkbox status of object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type lColumn: int
        :param lColumn: The column index.
        :type bCheck: bool
        :param bCheck: **True** if the checkbox should be checked, otherwise **False**.
        :type bcMsg: c4d.BaseContainer
        :param bcMsg: The container originally sent to the :meth:`GeUserArea.InputEvent` of the tree view's user area.
        
        
        """
        ...
    
    def IsTristate(self, root: Any, userdata: Any) -> bool:
        """    
        Called to retrieve the tristate flag of the tree.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :rtype: bool
        :return: **True** if the tristate flag is set, otherwise **False**.
        
        
        """
        ...
    
    def GetDragType(self, root: Any, userdata: Any, obj: Any) -> int:
        """    
        Called to retrieve the drag type of object *obj*, i.e. the type that the user would get if he started a drag in that cell.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: int
        :return: The object drag type, or **c4d.NOTOK** to disable drag-and-drop:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        
        """
        ...
    
    def AcceptDragObject(self, root: Any, userdata: Any, obj: Any, dragtype: int, dragobject: Any) -> Tuple[int, bool]:
        """    
        Called to check if object *obj* can accept the specified drag-and-drop action, and in that case what the result would be.
        
        .. note::
        
        If *obj* is **None** then *dragobject* should be inserted as a child of the root.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type dragtype: int
        :param dragtype:
        
        The drag type:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        :type dragobject: any
        :param dragobject: The drag object.
        :rtype: tuple(int, bool)
        :return: A tuple with the following information:
        
        - int: The insert mode:
        
        .. include:: /consts/INSERT.rst
        :start-line: 3
        
        .. note::
        
        The **ACCEPT_DRAG_OBJECT_FORCE_COPY** bit flag can be used together with the **INSERT** constants.
        
        - bool: **True** if copying is allowed to this position, otherwise **False**.
        
        
        """
        ...
    
    def GenerateDragArray(self, root: Any, userdata: Any, obj: Any) -> List[C4DAtom]:
        """    
        Called to generate a drag array for object *obj*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: List[c4d.C4DAtom]
        :return: The drag objects for *obj*.
        
        
        """
        ...
    
    def DragStart(self, root: Any, userdata: Any, obj: Any) -> int:
        """    
        Called to determine if object *obj* can be dragged or not and if dragged objects will be selected or not.
        
        .. versionadded:: R19.024
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :rtype: int
        :return: A combination of the following flags:
        
        .. include:: /consts/TREEVIEW_DRAGSTART.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetDragObject(self, root: Any, userdata: Any, obj: Any) -> None:
        """    
        Called to set the drag object to *obj*.
        
        .. versionadded:: R19.024
        
        .. note::
        
        | Helps to determine if dragging happens internally (rearranged items) or externally (dragged items from another treeview for instance).
        | To check this, store the drag object data and compare it with *dragobject* in :meth:`InsertObject`.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: The drag object on drag start.
        
        
        """
        ...
    
    def InsertObject(self, root: Any, userdata: Any, obj: Any, dragtype: int, dragobject: Any, insertmode: int, bCopy: bool) -> None:
        """    
        Called to insert *dragobject* as specified.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type dragtype: int
        :param dragtype:
        
        The drag type:
        
        .. include:: /consts/DRAGTYPE.rst
        :start-line: 3
        
        :type dragobject: any
        :param dragobject: The drag object on drag receive.
        :type insertmode: int
        :param insertmode:
        
        The insert mode:
        
        .. include:: /consts/INSERT.rst
        :start-line: 3
        
        :type bCopy: bool
        :param bCopy: **True** if the object should be copied, otherwise **False**.
        
        
        """
        ...
    
    def CreateContextMenu(self, root: Any, userdata: Any, obj: Any, lColumn: int, bc: BaseContainer) -> None:
        """    
        Called to build a context menu for object *obj* and column *lColumn*.
        
        .. seealso:: :func:`c4d.gui.ShowPopupDialog` for the format.
        
        .. note::
        
        | *bc* container already contains 2 default items: **c4d.ID_TREEVIEW_CONTEXT_REMOVE** and **c4d.ID_TREEVIEW_CONTEXT_RESET**. These may be removed.
        | The added menu entry IDs must be larger than **c4d.ID_TREEVIEW_FIRST_NEW_ID**.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type lColumn: int
        :param lColumn: The column index.
        :type bc: c4d.BaseContainer
        :param bc: Add context menu entries to this container.
        
        
        """
        ...
    
    def ContextMenuCall(self, root: Any, userdata: Any, obj: Any, lColumn: int, lCommand: int) -> bool:
        """    
        Called by a command in the context menu setup in :meth:`CreateContextMenu`.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type lColumn: int
        :param lColumn: The column index.
        :type lCommand: int
        :param lCommand: The menu command ID.
        :rtype: bool
        :return: **True** if the command has been processed and the data needs to be updated, otherwise **False**.
        
        
        """
        ...
    
    def GetHeaderSortArrow(self, root: Any, userdata: Any, lColID: int) -> int:
        """    
        Called to retrieve the sort mode of column *lColID*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type lColID: int
        :param lColID: The column index.
        :rtype: int
        :return: The sort direction.
        
        
        """
        ...
    
    def IsResizeColAllowed(self, root: Any, userdata: Any, lColID: int) -> bool:
        """    
        Called to check if column *lColID* can be resized or not.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type lColID: int
        :param lColID: The column index.
        :rtype: bool
        :return: **True** if the column can be resized, otherwise **False**.
        
        
        """
        ...
    
    def IsMoveColAllowed(self, root: Any, userdata: Any, lColID: int) -> bool:
        """    
        Called to check if column *lColID* can be moved or not.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type lColID: int
        :param lColID: The column index.
        :rtype: bool
        :return: **True** if the column can be moved, otherwise **False**.
        
        
        """
        ...
    
    def InputEvent(self, root: Any, userdata: Any, pArea: GeUserArea, msg: BaseContainer) -> bool:
        """    
        Called when an input event is received.
        
        .. note::
        
        All information about the input event is stored in the *msg* container.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type pArea: c4d.gui.GeUserArea
        :param pArea: The user area of the tree view.
        :type msg: c4d.BaseContainer
        :param msg: The event container.
        :rtype: bool
        :return: **True** if the event was handled, otherwise **False**.
        
        
        """
        ...
    
    def MouseDown(self, root: Any, userdata: Any, obj: Any, col: int, mouseinfo: Dict[str, Any], rightButton: bool) -> bool:
        """    
        Called when a mouse down event is received.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type col: int
        :param col: The column index.
        :type mouseinfo: dict
        :param mouseinfo: The mouse information. See :ref:`mouseInfo_dict`.
        :type rightButton: bool
        :param rightButton: **True** if the right mouse button was used, otherwise **False**.
        :rtype: bool
        :return: **True** if the event was handled, otherwise **False**.
        
        
        """
        ...
    
    def DoubleClick(self, root: Any, userdata: Any, obj: Any, col: int, mouseinfo: Dict[str, Any]) -> bool:
        """    
        Called when a mouse double click event is received.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type obj: any
        :param obj: An object in the tree.
        :type col: int
        :param col: The column index.
        :type mouseinfo: dict
        :param mouseinfo: The mouse information. See :ref:`mouseInfo_dict`.
        :rtype: bool
        :return: **True** if the event was handled, otherwise **False**.
        
        
        """
        ...
    
    def DeletePressed(self, root: Any, userdata: Any) -> None:
        """    
        Called when a delete event is received.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        
        
        """
        ...
    
    def HeaderClick(self, root: Any, userdata: Any, lColID: int, lChannel: int, bDblClk: int, mouseX: int, mouseY: int, ua: GeUserArea) -> bool:
        """    
        Called when a header has been clicked.
        
        .. versionchanged:: R20
        
        Added parameters *mouseX*, *mouseY* and *ua*.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type lColID: int
        :param lColID: The column index.
        :type lChannel: int
        :param lChannel:
        
        The mouse channel:
        
        .. include:: /consts/BFM_INPUT_MOUSE.rst
        :start-line: 3
        
        :type bDblClk: int
        :param bDblClk: **True** for double-click event, otherwise **False**.
        :type mouseX: int
        :param mouseX:
        
        .. versionadded:: R20
        
        The mouse horizontal position local to the left hand edge of the column, or `NOTOK` if dragging a column.
        
        :type mouseY: int
        :param mouseY:
        
        .. versionadded:: R20
        
        The mouse vertical position local to the header top, or `NOTOK` if dragging a column.
        
        :type ua: c4d.gui.GeUserArea
        :param ua:
        
        .. versionadded:: R20
        
        The header's user area, or **None** if dragging a column.
        
        :rtype: bool
        :return: **True** if the tree view needs to be updated, otherwise **False**.
        
        
        """
        ...
    
    def Scrolled(self, root: Any, userdata: Any, h: int, v: int, x: int, y: int) -> None:
        """    
        Called when the tree view has been scrolled.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type h: int
        :param h: The horizontal scroll steps.
        :type v: int
        :param v: The vertical scroll steps.
        :type x: int
        :param x: The X offset.
        :type y: int
        :param y: The Y offset.
        
        
        """
        ...
    
    def PaintFinished(self, root: Any, userdata: Any) -> None:
        """    
        Called when a paint selection has been performed in the tree view.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        
        
        """
        ...
    
    def SelectionChanged(self, root: Any, userdata: Any) -> None:
        """    
        Called when selection has changed.
        
        :type root: any
        :param root: The tree root passed to :meth:`TreeViewCustomGui.SetRoot`.
        :type userdata: any
        :param userdata: The user data passed to :meth:`TreeViewCustomGui.SetRoot`.
        
        
        """
        ...
    

class BaseCustomGui(object):
    def GetWidth(self) -> int:
        """    
        Retrieves the width of the custom GUI in pixels.
        
        .. versionadded:: R18.011
        
        :rtype: int
        :return: The width of the custom GUI.
        
        
        """
        ...
    
    def GetHeight(self) -> int:
        """    
        Retrieves the height of the custom GUI in pixels.
        
        .. versionadded:: R18.011
        
        :rtype: int
        :return: The height of the custom GUI.
        
        
        """
        ...
    
    def Redraw(self) -> None:
        """    
        Redraws the custom GUI.
        
        .. versionadded:: R18.011
        
        
        """
        ...
    
    def LayoutChanged(self) -> bool:
        """    
        Tells the custom GUI that the layout has changed.
        
        .. versionadded:: R18.011
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Activate(self) -> bool:
        """    
        Activates the custom GUI.
        
        .. versionadded:: R18.011
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetDefaultForResEdit(self) -> bool:
        """    
        Sets the custom GUI to the resource editor defaults.
        
        .. versionadded:: R18.011
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetData(self, data: Any) -> bool:
        """    
        Sets the custom GUI data.
        
        .. versionadded:: R18.011
        
        :type data: any
        :param data: The new data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetData(self) -> Any:
        """    
        Retrieves the custom GUI data.
        
        .. versionadded:: R18.011
        
        :rtype: Any
        :return: The current data.
        
        
        """
        ...
    
    def SetLayoutMode(self, mode: int) -> None:
        """    
        Sets the layout mode.
        
        .. versionadded:: R18.011
        
        :type mode: int
        :param mode: The new layout mode:
        
        .. include:: /consts/LAYOUTMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetLayoutMode(self) -> int:
        """    
        Retrieves the layout mode.
        
        .. versionadded:: R18.011
        
        :rtype: int
        :return: The current layout mode:
        
        .. include:: /consts/LAYOUTMODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SupportLayoutSwitch(self) -> bool:
        """    
        Checks if the custom GUI supports layout switching.
        
        .. versionadded:: R18.011
        
        :rtype: bool
        :return: **True** if the layout switch is supported, otherwise **False**.
        
        
        """
        ...
    

class TreeViewCustomGui(BaseCustomGui):
    def SetRoot(self, root: Any, functions: TreeViewFunctions, userdata: Any) -> bool:
        """    
        Initializes the tree.
        
        :type root: any
        :param root: Root object.
        :type functions: c4d.gui.TreeViewFunctions
        :param functions: Tree view functions.
        :type userdata: any
        :param userdata: User data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetLayout(self, columns: int, data: BaseContainer) -> bool:
        """    
        Sets the layout for the tree view.
        
        :type columns: int
        :param columns: Number of columns.
        :type data: c4d.BaseContainer
        :param data: Column data container, with one column type entry for each column:
        
        .. include:: /consts/LV.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Refresh(self) -> None:
        """    
        Refreshes the tree view.
        
        
        """
        ...
    
    def SetHeaderText(self, lColumnID: int, str: str) -> bool:
        """    
        Set the header text for a column.
        
        :type lColumnID: int
        :param lColumnID: Column index.
        :type str: str
        :param str: Header text.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MakeVisible(self, pObj: Any) -> bool:
        """    
        Scrolls to *pObj* and expands the tree if necessary.
        
        :type pObj: any
        :param pObj: The object to scroll to.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ShowObject(self, pObj: Any) -> bool:
        """    
        Expands the tree to *pObj*.
        
        :type pObj: any
        :param pObj: The object to expand to.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetVisibleScrollArea(self) -> Tuple[int, int, int, int]:
        """    
        Queries the internal scroll group for its currently visible region.
        
        .. versionadded:: R17.048
        
        :rtype: tuple(int,int,int,int)
        :return: The X and Y coordinates of the top/bottom left/right visible corner: tuple(x1,y1,x2,y2).
        
        
        
        """
        ...
    
    def SetVisibleScrollArea(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """    
        Sets the internal scroll group currently visible region, a rectangle between (*x1*, *y1*) and (*x2*, *y2*).
        
        .. versionadded:: R18.020
        
        :type x1: int
        :param x1: The left X value.
        :type y1: int
        :param y1: The top Y value.
        :type x2: int
        :param x2: The right X value.
        :type y2: int
        :param y2: The bottom Y value.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetVisibleLineCount(self) -> int:
        """    
        Gets the number of currently visible lines related to folded and unfolded items of the tree.
        
        .. versionadded:: R17.048
        
        :rtype: int
        :return: The number of visible lines.
        
        
        """
        ...
    
    def SetFocusItem(self, pItem: Any) -> None:
        """    
        Sets the focus item.
        
        :type pItem: any
        :param pItem: The new focus item.
        
        
        """
        ...
    
    def IsFocusItem(self, pItem: Any) -> bool:
        """    
        Checks if *pItem* is the focus item.
        
        :type pItem: any
        :param pItem: The item to check.
        :rtype: bool
        :return: **True** if *pItem* is the focus item, otherwise **False**.
        
        
        """
        ...
    

class SplineCustomGui(BaseCustomGui):
    def SetSpline(self, data: SplineData) -> bool:
        """    
        Sets the data.
        
        :type data: c4d.SplineData
        :param data: The new spline data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetSplineData(self) -> SplineData:
        """    
        Gets the data.
        
        :rtype: c4d.SplineData
        :return: The spline data.
        
        
        """
        ...
    
    def SetGridLineCountH(self, l: int) -> None:
        """    
        Set the horizontal grid line count.
        
        :type l: int
        :param l: The new count.
        
        
        """
        ...
    
    def SetGridLineCountV(self, l: int) -> None:
        """    
        Set the vertical grid line count.
        
        :type l: int
        :param l: The new count.
        
        
        """
        ...
    
    def GetGridLineCountH(self) -> int:
        """    
        Get the horizontal grid line count.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetGridLineCountV(self) -> int:
        """    
        Get the vertical grid line count.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetScreenPosition(self, v: Vector) -> Tuple[float, float]:
        """    
        Get the screen position for a spline value.
        
        :type v: c4d.Vector
        :param v: The spline value.
        :rtype: tuple(float, float)
        :return: The screen X and Y positions.
        
        
        """
        ...
    
    def GetValue(self, x: int, y: int) -> Vector:
        """    
        Get the spline value for a screen position.
        
        .. versionadded:: R14.014
        
        :type x: int
        :param x: The screen X position.
        :type y: int
        :param y: The screen Y position.
        :rtype: c4d.Vector
        :return: The spline value.
        
        
        """
        ...
    
    def SetCustomColor(self, bSet: bool, col: Vector) -> None:
        """    
        Set a custom color for the curve.
        
        .. versionadded:: R14.014
        
        :type bSet: bool
        :param bSet: True if a custom color should be used.
        :type col: c4d.Vector
        :param col: The custom color.
        
        """
        ...
    

class SoundEffectorCustomGui(BaseCustomGui):
    def SetGUIOwnerOverride(self, bl: BaseList2D) -> bool:
        """    
        Sets the GUI owner that receives the sound track.
        
        :type bl: c4d.BaseList2D
        :param bl: The GUI owner.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetGUIOwnerOverride(self, doc: BaseDocument) -> BaseList2D:
        """    
        Retrieves the GUI owner.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :rtype: c4d.BaseList2D
        :return: The GUI owner, or **None** if the function fails.
        
        
        """
        ...
    

class RangeCustomGui(BaseCustomGui):
    ...

class QuickTabCustomGui(BaseCustomGui):
    def ClearStrings(self) -> None:
        """    
        Removes all strings.
        
        
        """
        ...
    
    def AppendString(self, id: int, str: str, checked: bool) -> None:
        """    
        Appends a string.
        
        :type id: int
        :param id: String ID.
        :type str: str
        :param str: String to append.
        :type checked: bool
        :param checked: Initial selection state.
        
        
        """
        ...
    
    def DoLayoutChange(self) -> None:
        """    
        Call this after appending strings to show the results.
        
        
        """
        ...
    
    def IsSelected(self, id: int) -> bool:
        """    
        Checks if a string is selected.
        
        :type id: int
        :param id: String ID.
        :rtype: bool
        :return: **True** if string *id* is selected, otherwise **False**.
        
        
        """
        ...
    
    def SetTextColor(self, id: int, col: int) -> None:
        """    
        Set the text color of item *id* to *col*.
        
        :type id: int
        :param id: String ID.
        :type col: int
        :param col: Text color, e.g. *COLOR_MATERIALMANAGER_TEXT_SELECTED*. See :doc:`/consts/COLOR`.
        
        
        """
        ...
    
    def Select(self, id: int, b: bool) -> bool:
        """    
        Change the selection state of item *id* to *b*.
        
        :type id: int
        :param id: String ID.
        :type b: bool
        :param b: New selection state.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetLayerColor(self, id: int, show: bool, col: Vector) -> None:
        """    
        Sets the layer color of string id.
        
        :param id: The string ID.
        :type id: int
        :param show: **True** to show the layer color.
        :type show: bool
        :param col: The color.
        :type col: c4d.Vector
        
        
        """
        ...
    

class LinkBoxGui(BaseCustomGui):
    def SetLink(self, obj: BaseList2D) -> bool:
        """    
        Sets the link.
        
        :type obj: c4d.BaseList2D
        :param obj: The object to set.
        :rtype: bool
        :return: **True** if the object was set, otherwise **False**.
        
        
        """
        ...
    
    def GetLink(self, doc: BaseDocument, instance: int) -> None:
        """    
        Evaluates the link in *doc*, returning **None** if the linked object is not an instance of *instance*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: Document to evaluate the link in.
        :type instance: int
        :param instance: The type to check.
        
        
        """
        ...
    

class InExcludeCustomGui(BaseCustomGui):
    ...

class HtmlViewerCustomGui(BaseCustomGui):
    def SetText(self, url: str) -> None:
        """    
        Set the HTML viewer text.
        
        :type url: str
        :param url: New text.
        
        
        """
        ...
    
    def SetUrl(self, url: str, encoding: int) -> None:
        """    
        Set the HTML viewer URL.
        
        :type url: str
        :param url: New URL.
        :type encoding: int
        :param encoding: Encoding:
        
        .. include:: /consts/URL_ENCODING.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetURLCallback(self, callback: Any, user_data: Any) -> None:
        """    
        Set the URL callback.
        
        :type callback: function(*user_data*, *url*, *encoding*) : *user_data*: not used, always **None** - *url*: str - *encoding*: int
        :param callback: New callback, or **None** to disable callback.
        :type user_data: any
        :param user_data: User data. - Not used currently, limitation of the implementation.
        
        
        """
        ...
    
    def DoAction(self, action: int) -> None:
        """    
        Do an action in the HTML viewer.
        
        :type action: int
        :param action: Action:
        
        .. include:: /consts/WEBPAGE.rst
        :start-line: 3
        
        
        """
        ...
    

class HyperLinkCustomGui(BaseCustomGui):
    def SetLinkString(self, strLink: str, strText: str) -> None:
        """    
        Sets the strings.
        
        :type strLink: str
        :param strLink: The new link string or **None**.
        :type strText: str
        :param strText: The new text string or **None**.
        
        
        """
        ...
    
    def GetLinkString(self) -> Tuple[str, str]:
        """    
        Gets the strings.
        
        :rtype: tuple(str, str)
        :return: The link and text strings.
        
        
        """
        ...
    

class GradientCustomGui(BaseCustomGui):
    def SetGradient(self, data: Gradient) -> bool:
        """    
        Sets the data.
        
        :type data: c4d.Gradient
        :param data: The new Gradient data.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetGradient(self) -> Gradient:
        """    
        Get the data.
        
        :rtype: c4d.Gradient
        :return: The new gradient data object.
        
        
        """
        ...
    

class FontChooserCustomGui(BaseCustomGui):
    def GetFont(self) -> BaseContainer:
        """    
        Retrieves the font container.
        
        :rtype: c4d.BaseContainer
        :return: The font container.
        
        
        """
        ...
    
    def SetFont(self, bc: BaseContainer) -> None:
        """    
        Sets the font container.
        
        .. note::
        
        Use :meth:`GeClipMap.GetFontDescription` or :meth:`GeClipMap.EnumerateFonts` to get a font description container.
        
        :type bc: c4d.BaseContainer
        :param bc: The font container.
        
        
        """
        ...
    

class DescriptionCustomGui(BaseCustomGui):
    def SetObject(self, op: BaseObject) -> None:
        """    
        Sets a single object to show.
        
        :type op: c4d.BaseObject
        :param op: The object to show. Must not be **None**.
        
        
        """
        ...
    

class DateTimeControl(BaseCustomGui):
    def SetDateTime(self, d: DateTimeData, bSetData: bool, bSetTime: bool) -> None:
        """    
        Sets the time.
        
        :type d: c4d.DateTimeData
        :param d: The new time.
        :type bSetData: bool
        :param bSetData: If this is **False** the date part of *d* is disregarded.
        :type bSetTime: bool
        :param bSetTime: If this is **False** the time part of *d* is disregarded.
        
        
        """
        ...
    
    def GetDateTime(self) -> DateTimeData:
        """    
        Get the time.
        
        :rtype: c4d.DateTimeData
        :return: The new spline data object.
        
        
        """
        ...
    

class BitmapButtonCustomGui(BaseCustomGui):
    def SetImage(self, obj: Union[str, BaseBitmap, Dict[str, Any], IconData], copybmp: bool, secondstate: bool) -> bool:
        """    
        Sets the image.
        
        :type obj: Union[str, c4d.bitmaps.BaseBitmap, dict, c4d.IconData]
        :param obj: The filename, bitmap or icon to load the image from.
        
        .. versionchanged:: 21
        
        :class:`c4d.IconData` is now supported.
        
        :type copybmp: bool
        :param copybmp: If this is **True** the bitmap is copied.
        :type secondstate: bool
        :param secondstate: If this is **True** the function stores a second state for toggle and clickable buttons.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetToggleState(self, set: bool) -> None:
        """    
        Sets the toggle state of the button.
        
        :type set: bool
        :param set: New toggle state.
        
        
        """
        ...
    
    def SetCommandDragId(self, cmdid: int) -> None:
        """    
        | Sets a command ID for the bitmap button.
        | This enables drag and drop of the command into tool bars and menu manager. Used e.g. in the script manager.
        
        :type cmdid: int
        :param cmdid: The ID of the command.
        
        
        """
        ...
    


def GetInputState(askdevice: int, askchannel: int, res: BaseContainer) -> bool:
    """    
    Polls a certain channel of a device for the current input state.
    
    .. seealso::
    
    :doc:`Input Events </misc/inputevents>`
    
    :type askdevice: int
    :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
    :type askchannel: int
    :param askchannel: The channel to ask.
    :type res: c4d.BaseContainer
    :param res: The result container.
    :rtype: bool
    :return: **True** if the state could be retrieved in *res*, otherwise **False**.
    
    
    """
    ...

def GetInputEvent(askdevice: int, res: BaseContainer) -> bool:
    """    
    Gets the next input event for a certain device from the event queue.
    
    .. seealso::
    
    :doc:`Input Events </misc/inputevents>`.
    
    :type askdevice: int
    :param askdevice: The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
    :type res: c4d.BaseContainer
    :param res: The result container.
    :rtype: bool
    :return: **True** if the event could be retrieved in *res*, otherwise **False**.
    
    
    """
    ...

def MessageDialog(text: str, type: int) -> int:
    """    
    Display a message dialog with the string as the message.
    
    .. code-block:: python
    
    import c4d
    
    c4d.gui.MessageDialog("Why do you take baths in milk? 'I can't find a cow tall enough for a shower.")
    
    .. image:: /_imgs/modules/gui/gui_messagedialog.png
    :align: center
    
    :type text: str
    :param text: The string to print out.
    :type type: int.
    :param type: The values are:
    
    .. include:: /consts/GEMB.rst
    :start-line: 3
    
    :rtype: int
    :return: Result from the message box. The value for this are:
    
    .. include:: /consts/GEMB_R.rst
    :start-line: 3
    
    
    """
    ...

def QuestionDialog(text: str) -> bool:
    """    
    | Opens a standard question dialog with a question mark icon and Yes/No buttons.
    | The text is specified as a string.
    
    .. code-block:: python
    
    rvalue = c4d.gui.QuestionDialog("Do you think I am a dialog?")
    
    .. image:: /_imgs/modules/gui/gui_questiondialog.png
    :align: center
    
    :type text: str
    :param text: The string to show.
    :rtype: bool
    :return: **True** if the user answered Yes, otherwise **False**.
    
    
    """
    ...

def RenameDialog(text: str) -> str:
    """    
    Opens a standard rename dialog
    
    .. code-block:: python
    
    name = op.GetName()             # Get the name of the active object
    rvalue = c4d.gui.RenameDialog(name) # Pass it for rename
    print rvalue                    # Returns None if the user aborts the dialog
    
    .. image:: /_imgs/modules/gui/gui_renamedialog.png
    :align: center
    
    :type text: str
    :param text: The string with the name to change.
    :rtype: str
    :return: The changed string on success, otherwise **None** if the user canceled the dialog.
    
    
    """
    ...

def InputDialog(text: str, preset: str) -> str:
    """    
    Opens an input dialog which returns the input string.
    
    :type text: str
    :return text: The label string.
    :type preset: str
    :return preset: The default value which will be written on popup.
    :rtype: str
    :return: The input as string.
    
    
    """
    ...

def ColorDialog(flags: int, col: Vector) -> Vector:
    """    
    Opens a color chooser dialog for the user to select a color. The look of this dialog depends on the operating system.
    
    .. image:: /_imgs/modules/gui/gui_choose_color.png
    :align: center
    
    :type flags: int
    :param flags: Flags.
    :type col: c4d.Vector
    :param col:
    
    .. versionadded:: R19.024
    
    The default color.
    
    :rtype: c4d.Vector
    :return: A :class:`Vector <c4d.Vector>` on success, otherwise **None** if the user canceled the dialog.
    
    
    """
    ...

def FontDialog() -> BaseContainer:
    """    
    | Opens a font chooser dialog for the user to select a font.
    | The look of this dialog depends on the operating system.
    
    .. image:: /_imgs/modules/gui/gui_choose_font.png
    :align: center
    
    :rtype: c4d.BaseContainer
    :return: A :class:`BaseContainer <c4d.BaseContainer>` with the font settings, otherwise **None**
    
    
    """
    ...

def SelectionListDialog(arr: Any, doc: BaseDocument, x: int, y: int) -> int:
    """    
    Shows a popup menu with of the given object tuple and lets the user choose an object at the position of the mouse.
    
    :type arr: list of type :class:`BaseObject <c4d.BaseObject>`
    :param arr: A list of BaseObjects.
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type x: int
    :param x: X-Coordinate
    :type y: int
    :param y: Y-Coordinate
    :rtype: int
    :return: The user choice, or *NOTOK* if nothing was selected.
    
    
    """
    ...

def ShowPopupDialog(cd: Union[None, GeDialog], bc: Optional[BaseContainer] = ..., x: Optional[int] = ..., y: Optional[int] = ..., flags: Optional[int] = ...) -> int:
    """    
    | Displays a popup menu dialog. The menu is defined by adding string items sequentially to a :class:`BaseContainer <c4d.BaseContainer>`. (i.e. the order the items are set in the container determines their order in the menu.) The ID of the string item determines its function.
    |
    | Here is a complete example of the features:
    
    .. code-block:: python
    
    import c4d
    
    # Declare menu items ID
    
    IDM_MENU1 = c4d.FIRST_POPUP_ID
    IDM_MENU2 = c4d.FIRST_POPUP_ID+1
    IDM_MENU3 = c4d.FIRST_POPUP_ID+2
    IDM_MENU4 = c4d.FIRST_POPUP_ID+3
    
    IDM_SUBMENU1 = c4d.FIRST_POPUP_ID+10
    IDM_SUBMENU2 = c4d.FIRST_POPUP_ID+11
    
    # Main menu
    
    menu = c4d.BaseContainer()
    menu.InsData(IDM_MENU1, 'Item 1')
    menu.InsData(IDM_MENU2, 'Item 2')
    menu.InsData(0, '') # Append separator
    
    # Sub menu
    
    submenu = c4d.BaseContainer()
    submenu.InsData(1, 'Item 3') # Set submenu title
    submenu.InsData(IDM_SUBMENU1, 'SubItem 1')
    submenu.InsData(IDM_SUBMENU2, 'SubItem 2&c&') # Check this subitem
    
    menu.SetContainer(IDM_MENU3, submenu) # Set submenu as subcontainer
    menu.InsData(0, '') # Append separator
    
    # Add another item to the menu
    
    menu.InsData(IDM_MENU4, 'Item 4&d&')  # Disable this item
    
    # Finally show popup dialog
    
    result = c4d.gui.ShowPopupDialog(cd=None, bc=menu, x=300, y=300)
    print result
    
    .. image:: /_imgs/modules/gui/gui_popudialogexample.png
    :align: center
    
    - A string with ID=0 gives a separator.
    
    .. code-block:: python
    
    menu.InsData(0, '')
    
    - A string with ID=1 sets the name of the menu (used for submenus).
    
    .. code-block:: python
    
    submenu.SetString(1, 'Text')
    
    - IDs in the range 1000 to 899999 inserts a Cinema 4D command.
    
    .. code-block:: python
    
    menu.InsData(c4d.IDM_COPY, 'Copy')
    menu.InsData(c4d.IDM_PASTE, 'Paste')
    
    To add 'Cube' command to a menu.
    
    .. code-block:: python
    
    menu.InsData(c4d.Ocube, "CMD")
    
    For a list of IDs, see the `c4d_symbols.h` file. A special case is the *c4d.IDM_CM_CLOSEWINDOW* ID that will close the current dialog.
    
    - The same applies to plugin IDs of plugins that have a menu entry (everything above 1000000).
    
    .. code-block:: python
    
    menu.SetString(pluginid, 'Text')
    
    - The IDs that are left, between 900000 (*c4d.FIRST_POPUP_ID*) and 999999, can be used for your own menu items.
    
    .. code-block:: python
    
    ID_MENU1 = c4d.FIRST_POPUP_ID
    ID_MENU2 = c4d.FIRST_POPUP_ID+1
    ID_MENU3 = c4d.FIRST_POPUP_ID+2
    
    :type cd: Union[None, c4d.gui.GeDialog]
    :param cd: The parent dialog.
    :type bc: c4d.BaseContainer
    :param bc: The container with the elements. The elements have to be strings. You can optionally set a title with the ID `0` or just start with the first element with the ID *c4d.FIRST_POPUP_ID*. If you set a title, we recommend to add the string '&d&' to the name of the title (see example) to grey it out. The title cannot be selected, even if its not greyed out.
    :type x: int
    :param x: Popup X position in screen pixels, or *c4d.MOUSEPOS* to popup where the cursor is.
    :type y: int
    :param y: Popup Y position in screen pixels, or *c4d.MOUSEPOS* to popup where the cursor is.
    :type flags: int
    :param flags: One of the following flags:
    
    .. include:: /consts/POPUP.rst
    :start-line: 3
    
    :rtype: int
    :return: The ID of the selected item, or *0* if nothing was selected.
    
    
    """
    ...

def GeUpdateUI() -> None:
    """    
    Forces a redraw of the GUI, for example after a change of the preferences or Linear Workflow settings.
    
    
    """
    ...

def SetMousePointer(l: int) -> None:
    """    
    Sets the type of mouse pointer.
    
    :type l: int
    :param l: Values for the mouse pointer image:
    
    .. include:: /consts/MOUSE.rst
    :start-line: 3
    
    
    """
    ...

def GetCursorBitmap(type: Any, hotspotx: Any, hotspoty: Any) -> None:
    """    
    Private.
    
    
    """
    ...

def GetShortcutCount() -> int:
    """    
    Gets the global shortcut count.
    
    :rtype: int
    :return: Number of shortcuts.
    
    
    """
    ...

def Shortcut2String(shortqual: int, shortkey: int) -> str:
    """    
    Converts a shortcut to a readable string.
    
    :type shortqual: int
    :param shortqual: Qualifier.
    :type shortkey: int
    :param shortkey: Key.
    :rtype: str
    :return: Shortcut string.
    
    
    """
    ...

def AddShortcut(bc: BaseContainer) -> bool:
    """    
    Adds the shortcut in *bc* to the shortcut list.
    
    :type bc: c4d.BaseContainer
    :param bc: Shortcut to add. These are the IDs:
    
    .. include:: /consts/SHORTCUT.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def RemoveShortcut(index: int) -> bool:
    """    
    Removes the shortcut at *index*.
    
    :type index: int
    :param index: Shortcut index, *0<=index<* :func:`GetShortcutCount`
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def LoadShortcutSet(fn: Union[str, MemoryFileStruct], add: bool) -> bool:
    """    
    Loads shortcuts from *fn*.
    
    :type fn: Union[str, c4d.storage.MemoryFileStruct]
    :param fn: File with shortcuts to load.
    :type add: bool
    :param add: Add the shortcuts, instead of replacing.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def SaveShortcutSet(fn: Union[str, MemoryFileStruct]) -> bool:
    """    
    Saves shortcuts to *fn*.
    
    :type fn: Union[str, c4d.storage.MemoryFileStruct]
    :param fn: File to save the shortcuts to.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def GetMenuResource(menuname: str) -> BaseContainer:
    """    
    Gets the menu container of a main menu.
    
    :type menuname: str
    :param menuname: Main menu name, e.g. **"M_EDITOR"** (the same name as on disk or that you can see in the menu editor).
    :rtype: c4d.BaseContainer
    :return: The menu container:
    
    .. include:: /consts/MENURESOURCE.rst
    :start-line: 3
    
    
    """
    ...

def SearchMenuResource(bc: BaseContainer, searchstr: str) -> bool:
    """    
    Searches a menu container for a certain plugin command (which is a string identifier, for example **"PLUGIN_CMD_1000472"**).
    
    :type bc: c4d.BaseContainer
    :param bc: Menu container to search.
    :type searchstr: str
    :param searchstr: Search string.
    :rtype: bool
    :return: **True** if the command was found, otherwise **False**.
    
    
    """
    ...

def SearchPluginMenuResource(identifier: str) -> Any:
    """    
    Searches for the 'Plugins' main category in 'M_EDITOR'.
    
    :type identifier: str
    :param identifier: The resource identifier.
    :rtype: ptr
    :return: The found menu container, or **None**.
    
    .. note:: To get the actual menu container use :func:`c4d.Cast`:
    
    .. code-block:: python
    
    res = gui.SearchPluginMenuResource()
    bc = c4d.Cast(None, res)
    
    
    """
    ...

def SearchPluginSubMenuResource(identifier: str, bc: BaseContainer) -> Any:
    """    
    Searches for the "Plugins" main category in "M_EDITOR" or optionally a submenu specified by *bc*.
    
    :type identifier: str
    :param identifier: The resource identifier.
    :type bc: c4d.BaseContainer
    :param bc: Submenu container.
    :rtype: ptr
    :return: The found menu container, or **None**.
    
    .. note:: To get the actual menu container use :func:`c4d.Cast`:
    
    .. code-block:: python
    
    res = gui.SearchPluginMenuResource()
    bc = c4d.Cast(None, res)
    
    
    """
    ...

def UpdateMenus() -> None:
    """    
    Forces a menu update.
    
    
    """
    ...

def GetGuiWorldColor(cid: int) -> Vector:
    """    
    Gets a GUI color from its constant ID.
    
    :type cid: int
    :param cid: The color ID. See :doc:`COLOR constants</consts/COLOR>`.
    :rtype: c4d.Vector
    :return: The GUI color.
    
    
    """
    ...

def GetInterfaceIcon(type: int, id_x: int, id_y: int, id_w: int, id_h: int) -> None:
    """    
    Returns the icon for an interface element.
    
    .. versionadded:: R14.014
    
    :type type: int
    :param type: Flags:
    
    .. include:: /consts/INTERFACE_ICON_TYPE.rst
    :start-line: 3
    
    :type id_x: int
    :param id_x: The X position ID of the icon.
    :type id_y: int
    :param id_y: The Y position ID of the icon.
    :type id_w: int
    :param id_w: The width ID of the icon.
    :type id_h: int
    :param id_h: The height ID of the icon.
    :rtype: dict{**bmp**: :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>`, **flags**: int, **w**: int, **h**: int, **x**: int, **y**: int}
    :return: The icon resource data, or **None** if an error occurred.
    
    
    """
    ...

def GetInterfaceIconEx(type: int, id_x: int, id_y: int, id_w: int, id_h: int) -> None:
    """    
    Returns the icon for an interface element.
    
    .. versionadded:: R21
    
    .. note::
    
    It's similar to :func:`c4d.gui.GetInterfaceIcon`, the only difference it's the return type, since :func:`c4d.gui.GetInterfaceIconEx` return an :class:`c4d.IconData`.
    
    :type type: int
    :param type: Flags:
    
    .. include:: /consts/INTERFACE_ICON_TYPE.rst
    :start-line: 3
    
    :type id_x: int
    :param id_x: The X position ID of the icon.
    :type id_y: int
    :param id_y: The Y position ID of the icon.
    :type id_w: int
    :param id_w: The width ID of the icon.
    :type id_h: int
    :param id_h: The height ID of the icon.
    :rtype: :class:`IconData`
    :return: The icon resource data, or **None** if an error occurred.
    
    
    """
    ...

def RegisterIcon(lIconID: int, pBmp: BaseBitmap, x: Optional[int] = ..., y: Optional[int] = ..., w: Optional[int] = ..., h: Optional[int] = ...) -> bool:
    """    
    Registers an icon from a bitmap. Optionally a sub-icon can be specified within an larger image by giving a rectangle from (*x*, *y*) to (*x+w*, *y+h*). If no rectangle is specified the whole bitmap is used. The bitmap is internally copied.
    
    :type lIconID: int
    :param lIconID: A unique plugin ID. You **must** obtain this from `PluginCafe.com <http://plugincafe.com/>`_
    :type pBmp: c4d.bitmaps.BaseBitmap
    :param pBmp: The bitmap to use for the icon. Is internally copied.
    :type x: int
    :param x: Optional X coordinate of the top left corner of the sub-icon rectangle.
    :type y: int
    :param y: Optioanl Y coordinate of the top left corner of the sub-icon rectangle.
    :type w: int
    :param w: Optional width of the sub-icon rectangle.
    :type h: int
    :param h: Optional height of the sub-icon rectangle.
    :rtype: bool
    :return: **True** if the icon was registered, otherwise **False**.
    
    
    """
    ...

def GetIcon(lIconID: int) -> None:
    """    
    Gets an icon registered with :func:`RegisterIcon`. Similar to :func:`InitResourceBitmap() <c4d.bitmaps.InitResourceBitmap>`.
    
    .. code-block:: python
    
    import c4d
    
    icon = c4d.gui.GetIcon(c4d.RESOURCEIMAGE_MOVE)
    bmp = icon["bmp"]
    x, y = icon["x"], icon["y"]
    
    :type lIconID: int
    :param lIconID: The ID of the icon. For a list of possible IDs check out :func:`InitResourceBitmap() <c4d.bitmaps.InitResourceBitmap>`
    :rtype: dict{**bmp**: :class:`BaseBitmap <c4d.bitmaps.BaseBitmap>`, **x**: int, **y**: int, **w**: int, **h**: int}
    :return: The information about the icon data.
    
    
    """
    ...

def UnregisterIcon(lIconID: int) -> bool:
    """    
    Unregisters the icon with ID *lIconID*. Only unregister your own registered icons.
    
    :type lIconID: int
    :param lIconID: The ID of the icon.
    :rtype: bool
    :return: **True** if the icon was unregistered, otherwise **False**.
    
    
    """
    ...

def GetShortcut(index: int) -> BaseContainer:
    """    
    Gets the shortcut at *index*.
    
    :type index: int
    :param index: Shortcut index, *0<=index<* :func:`GetShortcutCount <c4d.gui.GetShortcutCount>`
    :rtype: c4d.BaseContainer
    :return: The retrieved shortcut.
    
    
    """
    ...

def SizePixChr(pixels: int, chars: int) -> int:
    """    
    Combines the :func:`SizePix` and :func:`SizeChr` functions. The returned value is interpreted as a number of characters/lines plus a number of pixels.
    
    :type pixels: int
    :param pixels: The pixel dimension.
    :type chars: int
    :param chars: The number of characters.
    :rtype: int
    :param: The size value.
    
    
    """
    ...

def SizePix(pixels: int) -> int:
    """    
    Bakes a pixel size so that it can be used to specify dialog control dimension.
    
    :type pixels: int
    :param pixels: The pixel dimension.
    :rtype: int
    :param: The size value.
    
    
    """
    ...

def SizeChr(chars: int) -> int:
    """    
    Bakes a character count so that it can be used to specify dialog control dimension. (How many characters that will fit in a control for widths, and how many standard lines that will fit for heights.)
    
    :type chars: int
    :param chars: The number of characters.
    :rtype: int
    :return: The size value.
    
    
    """
    ...

def GeGetScreenDimensions(x: int, y: int, whole_screen: bool) -> None:
    """    
    Returns the screen dimensions in pixels.
    
    :type x: int
    :param x: Screen X coordinates to identify which display information is read (for multi-display setups).
    :type y: int
    :param y: Screen Y coordinates to identify which display information is read (for multi-display setups).
    :type whole_screen: bool
    :param whole_screen: **True** if dimensions of the whole screen (including taskbar etc.) are returned, otherwise **False**.
    :rtype: dict{**sx1**: int, **sy1**: int, **sx2**: int, **sy2**: int}
    :return: A dictionary with the screen dimensions:
    
    :type sx1: int
    :key sx1: The minimum X coordinate (left).
    :type sy1: int
    :key sy1: The minimum Y coordinate (top).
    :type sx2: int
    :key sx2: The maximum X coordinate (right).
    :type sy2: int
    :key sy2: The maximum Y coordinate (bottom).
    
    
    """
    ...

def ActiveObjectManager_SetObject(id: int, op: C4DAtom, flags: int, activepage: DescID) -> None:
    """    
    Sets the currently shown object *op* in the specified mode.
    
    .. note::
    
    | Use this only if a mode has been registered without a hook.
    | Otherwise the managers will ask for new objects themselves, and listen for events when new objects are selected.
    
    :type id: int
    :param id: The mode ID:
    
    .. include:: /consts/ACTIVEOBJECTMODE.rst
    :start-line: 3
    
    :type op: c4d.C4DAtom
    :param op: The object to show.
    :type flags: int
    :param flags: The flags:
    
    .. include:: /consts/ACTIVEOBJECTMANAGER.rst
    :start-line: 3
    
    :type activepage: c4d.DescID
    :param activepage: The description ID of the object's tab to be shown.
    
    
    """
    ...

def ActiveObjectManager_SetObjects(id: int, objects: List[C4DAtom], flags: int, activepage: DescID) -> None:
    """    
    Sets the currently shown *objects* in the specified mode.
    
    .. versionadded:: R19.053
    
    .. note::
    
    | Use this only if a mode has been registered without a hook.
    | Otherwise the managers will ask for new objects themselves, and listen for events when new objects are selected.
    
    :type id: int
    :param id: The mode ID:
    
    .. include:: /consts/ACTIVEOBJECTMODE.rst
    :start-line: 3
    
    :type objects: list of atoms
    :param objects: The objects to show.
    :type flags: int
    :param flags: The flags:
    
    .. include:: /consts/ACTIVEOBJECTMANAGER.rst
    :start-line: 3
    
    :type activepage: c4d.DescID
    :param activepage: The descripion ID of the objects' tab to be shown.
    
    
    """
    ...

