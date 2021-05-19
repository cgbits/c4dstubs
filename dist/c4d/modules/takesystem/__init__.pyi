from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseList2D, DescID, BaseObject, BaseTag
from c4d.documents import RenderData, BaseDocument


class BaseTake(BaseList2D):
    def IsMain(self) -> bool:
        """    
        Checks if the Take is the Main Take.
        
        :rtype: bool
        :return: **True** if the Take is the Main Take, otherwise **False**.
        
        
        """
        ...
    
    def SearchHierarchy(self, op: BaseTake) -> bool:
        """    
        Checks if the Take is a child of *op*.
        
        :type op: c4d.modules.takesystem.BaseTake
        :param op: The Take to search within his hierarchy.
        :rtype: bool
        :return: **True** if the Take is child of *op*, otherwise **False**.
        
        
        """
        ...
    
    def GetOverrides(self) -> None:
        """    
        Retrieves the Override nodes owned by the Take.
        
        :rtype: list of :class:`BaseOverride <c4d.modules.takesystem.BaseOverride>`
        :return: The Override nodes.
        
        
        """
        ...
    
    def GetOverrideGroups(self) -> None:
        """    
        Retrieves the Override Groups nodes owned by the Take.
        
        :rtype: list of :class:`BaseOverrideGroup <c4d.modules.takesystem.BaseOverrideGroup>`
        :return: The Override Groups nodes.
        
        
        """
        ...
    
    def FindOrAddOverrideParam(self, takeData: TakeData, node: BaseList2D, descID: DescID, overrideValue: Any, backupValue: Optional[Any] = ..., deleteAnim: Optional[bool] = ...) -> BaseOverride:
        """    
        | Searches if parameter with *descID* is Overridden. If not adds a new Override with passed *overrideValue* for the Take.
        | If the :class:`BaseOverride <c4d.modules.takesystem.BaseOverride>` node does not exist the function automatically allocates and inserts it, plus takes care to backup data properly in parent or Main Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The scene node to override.
        :type descID: c4d.DescID
        :param descID: The parameter to override.
        :type overrideValue: any
        :param overrideValue: The initial value to set in the Overrides for the Take.
        :type backupValue: any
        :param backupValue: Optionally provide the backup value for the Main/parent Take. Mandatory to set this for parameters not from the GUI.
        :type deleteAnim: bool
        :param deleteAnim: If **True** and original parameter in the scene is animated the animation will be removed in the resulting Override.
        :rtype: c4d.modules.takesystem.BaseOverride
        :return: The found or newly created Override node.
        
        
        """
        ...
    
    def OverrideNode(self, takeData: TakeData, node: BaseList2D, deleteAnim: bool) -> BaseOverride:
        """    
        Overrides all parameters of passed *node* in the Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The scene node to override.
        :type deleteAnim: bool
        :param deleteAnim: If **True** and original parameter in the scene is animated the animation will be removed in the resulting Override.
        :rtype: c4d.modules.takesystem.BaseOverride
        :return: The newly created Override node.
        
        
        """
        ...
    
    def AutoTake(self, takeData: TakeData, node: BaseList2D, undo: BaseList2D) -> None:
        """    
        Compares nodes and automatically generates overrides for different parameters in the Take.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The scene node to override.
        :type undo: c4d.BaseList2D
        :param undo: The node to compare with.
        
        
        """
        ...
    
    def DeleteOverride(self, takeData: TakeData, node: BaseList2D, descID: DescID) -> None:
        """    
        | Deletes a single parameter Override for *node* with *descID*.
        | If the Override results empty (no more overridden parameters) then it will be deleted too.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The scene node to delete the parameter for.
        :type descID: c4d.DescID
        :param descID: The parameter Override to be deleted.
        
        
        """
        ...
    
    def FindOverride(self, takeData: TakeData, node: BaseList2D) -> BaseOverride:
        """    
        Searches if *node* is overridden in the Take.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The scene node to search the Override for.
        :rtype: c4d.modules.takesystem.BaseOverride
        :return: The Override if found, otherwise **None**.
        
        
        """
        ...
    
    def FindOverrideInHierarchy(self, takeData: TakeData, node: BaseList2D, descID: DescID) -> None:
        """    
        Searches if *node* parameter with *descID* is overridden in the Take or in a parent.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The node to search the Override for.
        :type descID: c4d.DescID
        :param descID: The parameter to search for.
        :rtype: tuple(:class:`BaseOverride <c4d.modules.takesystem.BaseOverride>`, :class:`BaseTake <c4d.modules.takesystem.BaseTake>`)
        :return: The Override if found and the Take that owns it.
        
        
        """
        ...
    
    def AddOverrideGroup(self) -> BaseOverrideGroup:
        """    
        Adds a new Override Group to the Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :rtype: c4d.modules.takesystem.BaseOverrideGroup
        :return: The added Override Group.
        
        
        """
        ...
    
    def GetFirstOverrideGroup(self) -> BaseOverrideGroup:
        """    
        Gets the first Override Group in the Take.
        
        :rtype: c4d.modules.takesystem.BaseOverrideGroup
        :return: The first Override Group, or **None** if there is none.
        
        
        """
        ...
    
    def DeleteOverrideGroup(self, takeData: TakeData, og: BaseOverrideGroup) -> None:
        """    
        Deletes an Override Group from the Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type og: c4d.modules.takesystem.BaseOverrideGroup
        :param og: The Override Group to be deleted.
        
        
        """
        ...
    
    def GetCamera(self, takeData: TakeData) -> BaseObject:
        """    
        Gets the camera for the Take.
        
        .. note::
        
        Can return the default camera.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: c4d.BaseObject
        :return: The camera assigned to the Take, or **None** if the Take uses the camera from a parent Take.
        
        
        """
        ...
    
    def GetEffectiveCamera(self, takeData: TakeData) -> None:
        """    
        Gets the camera used by the Take even if it comes from a parent Take.
        
        .. note::
        
        Can return the default camera.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: tuple(:class:`BaseObject <c4d.BaseObject>`, :class:`BaseTake <c4d.modules.takesystem.BaseTake>`)
        :return: The camera used by the Take and the Take it comes from.
        
        
        """
        ...
    
    def SetCamera(self, takeData: TakeData, camera: BaseObject) -> None:
        """    
        Sets the camera for the Take.
        
        .. note::
        
        Can be the default camera.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type camera: c4d.BaseObject
        :param camera: The camera to set, or **None** to reset and use one from a parent Take.
        
        
        """
        ...
    
    def GetRenderData(self, takeData: TakeData) -> RenderData:
        """    
        Gets the render data for the Take.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: c4d.documents.RenderData
        :return: The RenderData assigned to the Take, or **None** if the Take uses the RenderData from a parent Take.
        
        
        """
        ...
    
    def GetEffectiveRenderData(self, takeData: TakeData) -> None:
        """    
        Gets the render data used by the Take even if it comes from a parent Take.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: tuple(:class:`RenderData <c4d.documents.RenderData>`, :class:`BaseTake <c4d.modules.takesystem.BaseTake>`)
        :return: The render data used by the Take and the Take it comes from.
        
        
        """
        ...
    
    def SetRenderData(self, takeData: TakeData, rData: RenderData) -> None:
        """    
        Sets the RenderData for the Take.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type rData: c4d.documents.RenderData
        :param rData: The render data to set, or **None** to reset and use one from a parent Take.
        
        
        """
        ...
    
    def IsChecked(self) -> None:
        """    
        Gets the mark status of the Take used for rendering and export operations.
        
        :rtype: tuple(:class:`RenderData <c4d.documents.RenderData>`, :class:`BaseTake <c4d.modules.takesystem.BaseTake>`)
        :return: **True** if the Take is marked, otherwise **False**.
        
        
        """
        ...
    
    def SetChecked(self, status: bool) -> None:
        """    
        Sets the mark status of the Take used for rendering and export operations.
        
        :type status: bool
        :param status: If **True** the Take is marked, otherwise the mark is removed.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Resets all sub-structures and Overrides for the Take.
        
        .. warning::
        
        All data not in the current state of the document are deleted.
        
        
        """
        ...
    

class TakeData(object):
    def GetDocument(self) -> BaseDocument:
        """    
        Retrieves the document for the :class:`TakeData <c4d.modules.takesystem.TakeData>`.
        
        :rtype: c4d.documents.BaseDocument
        :return: The document, or **None** if the :class:`TakeData <c4d.modules.takesystem.TakeData>` is not initialized.
        
        
        """
        ...
    
    def GetMainTake(self) -> BaseTake:
        """    
        Retrieves the Main Take.
        
        .. note::
        
        Main Take is always the first under the header.
        
        :rtype: c4d.modules.takesystem.BaseTake
        :return: The Main Take.
        
        
        """
        ...
    
    def GetTakeMode(self) -> int:
        """    
        Retrieves the Take System global mode. Can be **TAKE_MODE_MANUAL** or **TAKE_MODE_AUTO**.
        
        .. note::
        
        This mode affects how the user has to interact with GUI to override parameters.
        
        :rtype: int
        :return: The Take System mode:
        
        .. include:: /consts/TAKE_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetOverrideEnabling(self) -> int:
        """    
        Retrieves the ability for the Take System to override a specific kind of node based on global switch.
        
        :rtype: int
        :return: The Take System override enabling:
        
        .. include:: /consts/OVERRIDEENABLING.rst
        :start-line: 3
        
        
        """
        ...
    
    def CheckOverrideEnabling(self, mask: int) -> bool:
        """    
        Checks for a specific **OVERRIDEENABLING**.
        
        :type mask: int
        :param mask: The Take System override enabling mask:
        
        .. include:: /consts/OVERRIDEENABLING.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the OVERRIDEENABLING is set, otherwise **False**.
        
        
        """
        ...
    
    def GetTakeSelection(self, children: Any) -> None:
        """    
        Retrieves the selected Takes.
        
        :type mask: bool
        :param mask: If **True** also selected Take children are collected.
        :rtype: list of :class:`BaseTake <c4d.modules.takesystem.BaseTake>`
        :return: The selected Takes.
        
        
        """
        ...
    
    def GetCurrentTake(self) -> BaseTake:
        """    
        Retrieves the current Take.
        
        :rtype: c4d.modules.takesystem.BaseTake
        :return: The current Take.
        
        
        """
        ...
    
    def SetCurrentTake(self, take: BaseTake) -> bool:
        """    
        Sets the current Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type take: c4d.modules.takesystem.BaseTake
        :param take: The Take to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def TakeToDocument(self, take: BaseTake) -> BaseDocument:
        """    
        Isolates a Take in a new document. The new document is allocated and filled by the function.
        
        .. note::
        
        The caller has to insert the document if necessary.
        
        :type take: c4d.modules.takesystem.BaseTake
        :param take: The Take to isolate.
        :rtype: c4d.documents.BaseDocument
        :return: The allocated document.
        
        
        """
        ...
    
    def SaveTakesWithAssets(self, selected: bool) -> bool:
        """    
        Executes a "Save Project With Assets" for Takes in the document, each saved file representing a Take.
        
        :type selected: bool
        :param selected: If **True** only selected Takes are exported, otherwise all.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def AddTake(self, name: str, parent: Optional[BaseTake] = ..., cloneFrom: Optional[BaseTake] = ...) -> BaseTake:
        """    
        Creates and inserts a new Take.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        .. warning::
        
        Selections have to be handled manually.
        
        :type name: str
        :param name: The name of the Take to add. If an empty string is passed the default Take name will be used.
        :type parent: c4d.modules.takesystem.BaseTake
        :param parent: Optionally pass a parent Take, otherwise the new Take will be added at the end of the list under the Main Take.
        :type cloneFrom: c4d.modules.takesystem.BaseTake
        :param cloneFrom: Optionally pass a Take the new Take will be cloned from.
        :rtype: c4d.modules.takesystem.BaseTake
        :return: The added Take.
        
        
        """
        ...
    
    def DeleteTake(self, take: BaseTake) -> None:
        """    
        Deletes a Take and all connected overrides. If Take is the current the Main Take will be set as current.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type take: c4d.modules.takesystem.BaseTake
        :param take: The Take to delete.
        
        
        """
        ...
    
    def InsertTake(self, takeToMove: BaseTake, destTake: BaseTake, insertMode: int) -> None:
        """    
        | Moves a Take in the hierarchy in a safe way.
        | The Take system has several hierarchy dependencies.
        | If a Take is moved while it is current or while it is a child of the Current Take then this would need to manually take care of all data sorting and handling.
        | This function do all this work.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeToMove: c4d.modules.takesystem.BaseTake
        :param takeToMove: The Take to move.
        :type destTake: c4d.modules.takesystem.BaseTake
        :param destTake: The parent destination Take. If **None** the Main Take is used. In this case c4d.NOTOK can be used as the insert mode to add the take as the last child of the main take
        :type insertMode: int
        :param insertMode: The insertion mode:
        
        .. include:: /consts/INSERT.rst
        :start-line: 3
        
        
        """
        ...
    
    def FindOverrideCounterPart(self, overrideNode: BaseOverride, descID: DescID) -> Tuple[BaseOverride, BaseTake]:
        """    
        Finds the backup node that fits with an Override (for example the backup node in the Main Take).
        
        :type overrideNode: c4d.modules.takesystem.BaseOverride
        :param overrideNode: The original Override node.
        :type descID: c4d.DescID
        :param descID: The description ID to check.
        :rtype: Tuple[c4d.modules.takesystem.BaseOverride>, c4d.modules.takesystem.BaseTake>]
        :return: The counterpart node and the Take that owns it.
        
        
        """
        ...
    
    def GetUndoState(self) -> bool:
        """    
        Gets the state of automatic Take undo.
        
        .. note::
        
        It is useful to deactivate undo when working on document clones in several situation like import/export operations where undo is not important.
        
        :rtype: bool
        :return: **True** if the automatic undo is active, otherwise **False**.
        
        
        """
        ...
    
    def SetUndoState(self, state: bool) -> None:
        """    
        Activates or deactivates the state of automatic Take undo.
        
        .. note::
        
        It is useful to deactivate undo when working on document clones in several situation like import/export operations where undo is not important.
        
        :type state: bool
        :param state: **True** if the automatic undo has to be used, otherwise **False**.
        
        
        """
        ...
    
    def ResetSystem(self) -> None:
        """    
        Resets completely the Take System. Usually not needed.
        
        .. warning::
        
        All data not in the current state of the document is deleted.
        
        
        """
        ...
    

class BaseOverrideGroup(BaseList2D):
    def GetObjectsInGroup(self) -> None:
        """    
        Retrieves all the objects in the group.
        
        :rtype: list of :class:`BaseList2D <c4d.BaseList2D>`
        :return: The objects in the group.
        
        
        """
        ...
    
    def AddToGroup(self, takeData: TakeData, node: BaseList2D) -> None:
        """    
        Adds *node* to the Override Group. If *node* is already part of another group it will be automatically removed first.
        
        .. warning::
        
        The node to add must be a real scene node. Adding BaseOverride nodes is forbidden.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The node to add.
        
        
        """
        ...
    
    def RemoveFromGroup(self, takeData: TakeData, node: BaseList2D) -> None:
        """    
        Removes *node* from the Override Group.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type node: c4d.BaseList2D
        :param node: The node to remove. If it is not part of the group the function returns.
        
        
        """
        ...
    
    def AddTag(self, takeData: TakeData, type: int, mat: Optional[TakeData] = ...) -> BaseTag:
        """    
        Adds a new tag of the given *type* to the Override Group if it is not already there.
        
        .. warning::
        
        Only tags registered with the flag **TAG_ADDTOTAKEGROUP** are accepted by the group.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type type: int
        :param type:
        
        | The tag type to be added. If the tag is already in the group the function returns.
        | If **Ttexture** the material can be assigned to *mat*.
        
        :type mat: c4d.modules.takesystem.TakeData
        :param mat: The optional material (can be **None**) if passed type is **Ttexture**.
        :rtype: c4d.BaseTag
        :return: The tag. The added one if created by the function or the one already in the group.
        
        
        """
        ...
    
    def RemoveTag(self, takeData: TakeData, type: int) -> None:
        """    
        Removes the tag of the given *type* from the Override Group.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type type: int
        :param type: The tag type to be removed. If it is not in the Group the function returns.
        
        
        """
        ...
    
    def GetEditorMode(self) -> int:
        """    
        Returns the editor visibility mode for the Override Group.
        
        :rtype: int
        :return: The editor mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetRenderMode(self) -> int:
        """    
        Returns the render visibility mode for the Override Group.
        
        :rtype: int
        :return: The render mode:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetEditorMode(self, mode: Any) -> None:
        """    
        Sets the editor visibility mode for the Override Group.
        
        :type type: int
        :param type: The editor mode to set:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetRenderMode(self, mode: Any) -> None:
        """    
        Sets the render visibility mode for the Override Group.
        
        :type type: int
        :param type: The render mode to set:
        
        .. include:: /consts/MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetTag(self, type: int) -> BaseTag:
        """    
        Searches for a tag of the given *type* attached to the Override Group.
        
        :type type: int
        :param type: The tag type to search for.
        :rtype: c4d.BaseTag
        :return: The tag if found, otherwise **None**.
        
        
        """
        ...
    
    def GetTake(self) -> BaseTake:
        """    
        Returns the Take that owns the Override Group.
        
        :rtype: c4d.modules.takesystem.BaseTake
        :return: The Take for the Override Group.
        
        
        """
        ...
    
    def Find(self, takeData: TakeData, op: BaseObject) -> bool:
        """    
        Checks if an object is included in the Override Group.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type op: c4d.BaseObject
        :param op: The object to check.
        :rtype: bool
        :return: **True** if the object is included in the Override Group, otherwise **False**.
        
        
        """
        ...
    

class BaseOverride(BaseList2D):
    def IsOverriddenParam(self, descID: DescID) -> bool:
        """    
        Checks if the parameter at *descID* is overridden.
        
        :type descID: c4d.DescID
        :param descID: The parameter to be checked.
        :rtype: bool
        :return: **True** if parameter is overridden, otherwise **False**.
        
        
        """
        ...
    
    def GetSceneNode(self) -> BaseList2D:
        """    
        Retrieves the original scene node connected to the Override node.
        
        :rtype: c4d.BaseList2D
        :return: The original scene node.
        
        
        """
        ...
    
    def GetOwnerTake(self, takeData: TakeData) -> BaseTake:
        """    
        Gets the Take that owns the Override.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: c4d.modules.takesystem.BaseTake
        :return: The Take for the Override.
        
        
        """
        ...
    
    def IsInGroup(self, takeData: TakeData) -> Tuple[bool, BaseOverrideGroup]:
        """    
        Checks if the Override is also part of an Override Group, and if yes returns the group.
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :rtype: Tuple[bool, c4d.modules.takesystem.BaseOverrideGroup]
        :return: **True** if the Override is part of an Override Group, otherwise **False**.
        
        
        """
        ...
    
    def GetAllOverrideDescID(self) -> List[DescID]:
        """    
        Retrieves the DescID of all parameters in the Override.
        
        .. note::
        
        Sub-descriptions are included if overridden.
        
        :rtype: List[c4d.DescID]
        :return: The DescID of all overridden parameters.
        
        
        """
        ...
    
    def UpdateSceneNode(self, takeData: TakeData, descID: DescID) -> None:
        """    
        | Updates the scene node whenever data is directly changed on the base Override (for example with :meth:`C4DAtom.SetParameter`).
        | This ensures the scene node is properly updated if the Override affects the current document state.
        
        .. note::
        
        An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see :meth:`TakeData.GetUndoState`/:meth:`TakeData.SetUndoState`).
        
        :type takeData: c4d.modules.takesystem.TakeData
        :param takeData: The Take System context.
        :type descID: c4d.DescID
        :param descID: The edited parameter.
        
        
        """
        ...
    


def IsTakeRenderRunning() -> bool:
    """    
    Checks if a Take render is running.
    
    .. versionadded:: R17.048
    
    :rtype: bool
    :return: **True** if a Take render is running, otherwise **False**.
    
    
    """
    ...

def StopTakeRender() -> None:
    """    
    Stops the Take render if it is running.
    
    .. versionadded:: R17.048
    
    
    """
    ...

