from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d.documents import BaseDocument
from c4d import BaseObject, Matrix, DescID, Vector, BaseList2D, BaseTag
from c4d.modules.character import builder


class CAWeightTag(BaseTag):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.character.CAWeightTag
        :return: The new weight tag.
        
        
        """
        ...
    
    def GetJoint(self, index: int, doc: BaseDocument) -> CAJointObject:
        """    
        Get joint object at *index*.
        
        :type index: int
        :param index: The joint index.
        :type doc: c4d.documents.BaseDocument
        :param doc: Document or **None**.
        
        
        """
        ...
    
    def GetJointCount(self) -> int:
        """    
        Get total joint count.
        
        :rtype: int
        :return: Total joint count.
        
        
        """
        ...
    
    def FindJoint(self, op: BaseObject, doc: BaseDocument) -> None:
        """    
        Return the index of this object or *NOTOK* if not found.
        
        :type op: c4d.BaseObject
        :param op: Host object.
        :type doc: c4d.documents.BaseDocument
        :param doc: Document or **None**.
        
        
        """
        ...
    
    def GetJointRestState(self, index: int) -> None:
        """    
        Get the rest state for the joint at *index*.
        
        :type index: int
        :param index: The index of the joint.
        :raise IndexError: If the joint index is out of range : *0<=index<*:meth:`GetJointCount`.
        :rtype: dict{**m_bMg**: c4d.Matrix, **m_bMi**: c4d.Matrix, **m_oMg**: c4d.Matrix, **m_oMi**: c4d.Matrix}
        :return: The state.
        
        
        """
        ...
    
    def SetJointRestState(self, index: int, m_bMg: Matrix, m_bMi: Matrix, m_oMg: Matrix, m_oMi: Matrix, m_Len: float) -> None:
        """    
        Set the rest state for the joint at *index*.
        
        :type index: int
        :param index: The index of the joint.
        :type m_bMg: c4d.Matrix
        :param m_bMg: Joint global matrix.
        :type m_bMi: c4d.Matrix
        :param m_bMi: Joint inverse matrix.
        :type m_oMg: c4d.Matrix
        :param m_oMg: Object global matrix.
        :type m_oMi: c4d.Matrix
        :param m_oMi: Object inverse matrix.
        :type m_Len: float
        :param m_Len: Length.
        
        
        """
        ...
    
    def GetWeightCount(self, index: int) -> int:
        """    
        Gets the total number of stored weights for the given joint *index*.
        
        :type index: int
        :param index: Joint index.
        :rtype: int
        :return: The number of weights. 0 means weights are not stored.
        
        
        """
        ...
    
    def GetIndexWeight(self, index: int, windex: int) -> Tuple[int, int]:
        """    
        Get the *windex* weight and which point index *pntindex* it is as well as the *weight*
        
        .. code-block:: python
        
        pntindex, weight = caweighttag.GetIndexWeight(0, 0)
        
        :type index: int
        :param index: Joint index.
        :type windex: int
        :param windex: Weight index.
        :rtype: Tuple[int, int]
        :return: Returns the point index, and the corresponding weight.
        
        
        """
        ...
    
    def GetWeightMap(self, index: int, cnt: int, includeEffectors: bool) -> List[float]:
        """    
        Returns all the weights.
        
        .. versionadded:: R21
        
        :type index: int
        :param index: The joint index: <= index < :meth:`CAWeightTag.GetJointCount`.
        :type cnt: int
        :param cnt: The point count. Size of map. (Normally same as the point count).
        :type includeEffectors: bool
        :param includeEffectors: If **True** the effectors weights are added to the map.
        :rtype: list[float] * `cnt`
        :return: A list of float filled with the weight data.
        
        
        """
        ...
    
    def SetWeightMap(self, index: int, map: List[float]) -> bool:
        """    
        Sets the weights with `map`.
        
        .. versionadded:: R21
        
        :type index: int
        :param index: The joint index: <= index < :meth:`CAWeightTag.GetJointCount`.
        :type map: list[float]
        :param map: A list of float to set the new weight map.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetWeight(self, index: int, pntindex: int) -> float:
        """    
        Return the weight for the point *pntindex*.
        
        :type index: int
        :param index: Joint index.
        :type pntindex: int
        :param pntindex: Point index.
        :rtype: float
        :return: Weight.
        
        
        """
        ...
    
    def SetWeight(self, index: int, pntindex: int, weight: float) -> bool:
        """    
        Set the weight for *pntindex*.
        
        :type index: int
        :param index: Joint index.
        :type pntindex: int
        :param pntindex: Point index.
        :type weight: float
        :param weight: New weight.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetWeightDirty(self) -> int:
        """    
        Get the dirty state of the weights.
        
        :rtype: long
        :return: The weight's dirty state.
        
        
        """
        ...
    
    def WeightDirty(self) -> None:
        """    
        Marks the weights dirty.
        
        
        """
        ...
    
    def GetGeomMg(self) -> Matrix:
        """    
        | Get the global matrix for the bind geometry.
        | Use this with the global matrices of the joints to get the local transforms.
        
        :rtype: c4d.Matrix
        :return: The global matrix for the bind geometry.
        
        
        """
        ...
    
    def SetGeomMg(self, mg: Matrix) -> None:
        """    
        Set the global matrix for the bind geometry.
        
        :type mg: c4d.Matrix
        :param mg: The global matrix for the bind geometry.
        
        
        """
        ...
    
    def AddJoint(self, op: BaseObject) -> int:
        """    
        Add a Joint object to the Weight tag's "Joints" list.
        
        :type op: c4d.BaseObject
        :param op: The Joint object to add to the Weight tag's "Joints" list.
        :rtype: int
        :return: Joint object's index in the "Joints" list.
        
        
        """
        ...
    
    def RemoveJoint(self, op: BaseObject) -> None:
        """    
        Remove Joint object from the Weight tag's "Joints" list.
        
        :type op: c4d.BaseObject
        :param op: The Joint object to remove from the Weight tag's "Joint" list.
        
        
        """
        ...
    
    def CalculateBoneStates(self, index: int) -> None:
        """    
        Helper function to initialize the Joint at *index*.
        
        .. note::
        
        The Joints must be in the document.
        
        :type index: int
        :param index:
        
        The Joint index.
        .. note::
        
        Set to *NOTOK* to process all joints.
        
        
        """
        ...
    
    def TransferWeightMap(self, doc: BaseDocument, dst: CAWeightTag, sindex: int, dindex: int, offset: int, cnt: int) -> None:
        """    
        Transfer the weights from one Weight tag to another.
        
        .. note::
        
        Pass *NOTOK* for *sindex*, *dindex* and *cnt* if they shouldn't be evaluated.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the Weight tags.
        :type dst: c4d.modules.character.CAWeightTag
        :param dst: The destination Weight tag.
        :type sindex: int
        :param sindex: Index of the source Joint.
        :type dindex: int
        :param dindex: Index of the destination Joint.
        :type offset: int
        :param offset: Offset to move the weight indices when they are copied to the destination.
        :type cnt: int
        :param cnt: Number of weights to be transferred.
        
        
        """
        ...
    

class CAWeightMgr(object):
    def Update(self, doc: BaseDocument) -> bool:
        """    
        | Updates the internal weighted object list.
        |
        | Call before using other methods of CAWeightMgr if the Weight Manager dialog is closed and if the weight tool is inactive. Any of the two condition is enough to have the update run automatically each frame.
        | Also call if the weighted object list was changed programmatically. For instance after adding a new tag, performing undo redo, or any reason where an update is needed immediately.
        
        .. note::
        
        | Update has no effect if nothing dirty is detected.
        | Call :func:`c4d.EventAdd() <c4d.EventAdd>` to refresh the Weight Manager UI to show the updated changes.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetDirty(self, doc: BaseDocument) -> bool:
        """    
        | Sets the Weight Manager dirty to force an update on the next call to :meth:`Update`.
        |
        | If the Weight Manager dialog is open or if the Weight Manager is active, the update happens automatically at the next frame.
        | To force an update after a parameter change, use :meth:`SetDirty`, then call :meth:`Update`. Call :meth:`SetDirty` if a Weight Manager's parameter was directly modified in its container.
        
        .. note::
        
        Call :func:`c4d.EventAdd() <c4d.EventAdd>` to refresh the Weight Manager UI to show the updated changes.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetAutoWeightDictionary(self, doc: BaseDocument, stringId: int) -> Any:
        """    
        Get autoweight dictionary of the Weight Manager.
        
        .. versionadded:: R21
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type stringId: maxon.Id
        :param stringId: The maxon id of the autoweight algorithm.
        :rtype: maxon.DataDictionary
        :return: The data dictionary with the autoweight parameters inside.
        
        
        """
        ...
    
    def SetAutoWeightDictionary(self, doc: BaseDocument, dataDictionary: Any, stringId: int) -> bool:
        """    
        Get autoweight dictionary of the Weight Manager.
        
        .. versionadded:: R21
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :param dataDictionary: The data dictionary with the autoweight parameters inside.
        :type dataDictionary: maxon.The data dictionary with the autoweight parameters inside.
        :type stringId: maxon.Id
        :param stringId: The maxon id of the autoweight algorithm.
        :rtype: bool
        :return: **True** if it worked.
        
        
        """
        ...
    
    def GetAutoWeightAlgoIndex(self, doc: BaseDocument, stringId: int) -> int:
        """    
        Get the AutoWeightRef algorithm's index associated with the given id.
        
        .. versionadded:: R21
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type stringId: maxon.Id
        :param stringId: The autoweight id.
        :rtype: int
        :return: The index of the autoweight id.
        
        
        """
        ...
    
    def GetAutoWeightAlgoId(self, doc: BaseDocument, index: int) -> int:
        """    
        Get the AutoWeightRef algorithm's id associated with the given index.
        
        .. versionadded:: R21
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type index: int
        :param index: The autoweight int.
        :rtype: maxon.Id
        :return: The index of the autoweight id.
        
        
        """
        ...
    
    def SetParameter(self, doc: BaseDocument, id: int, newValue: Any) -> bool:
        """    
        | Sets a parameters of the Weight Manager.
        | Result is the same as setting a parameter on the Weight Manager's container directly except that :meth:`SetParameter` allows to specify the document in which to set the parameter.
        
        .. warning::
        
        | Setting parameters directly into the Weight Manager's container is not recommended.
        | Doing so requires to make the Weight Manager dirty and to update it manually.
        
        .. note::
        
        Call :func:`c4d.EventAdd() <c4d.EventAdd>` to refresh the Weight Manager UI to show the updated changes.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type id: int
        :param id: The ID of the parameter to set.
        :type newValue: any
        :param newValue: The parameter data to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetParameter(self, doc: BaseDocument, id: int) -> Any:
        """    
        Retrieves a parameter of the Weight Manager.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type id: int
        :param id: The ID of the parameter to set.
        :rtype: Any
        :return: The parameter data, otherwise **None** if the function failed.
        
        
        """
        ...
    
    def GetTagCount(self, doc: BaseDocument) -> int:
        """    
        Queries the number of weight tags for the passed document *doc*.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: int
        :return: The weight tags count.
        
        
        """
        ...
    
    def GetJointCount(self, doc: BaseDocument, tagIdx: int) -> int:
        """    
        Queries the number of joints bound to a weight tag.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag index in the list: `0` <= *tagIdx* < :meth:`GetTagCount`.
        :rtype: int
        :return: The joints count.
        
        
        """
        ...
    
    def GetTagIndex(self, doc: BaseDocument, tag: CAWeightTag) -> int:
        """    
        Finds a tag's index in the joint list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tag: c4d.modules.character.CAWeightTag
        :param tag: The weight tag to search for.
        :rtype: int
        :return: The tag's index in the list, or **NOTOK**/**-1** if not found.
        
        
        """
        ...
    
    def GetJointIndex(self, doc: BaseDocument, tag: CAWeightTag, joint: CAJointObject) -> Tuple[int, int]:
        """    
        Finds a joint's main (tag) and sub (joint) indices in the joint list.
        
        .. note::
        
        | The joint index might not match the joint index on the tag.
        | It is not recommended to keep indices over time, some operations might change the list ordering or length.
        | Only the Ids to reference joints can be kept over time.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tag: c4d.modules.character.CAWeightTag
        :param tag: The weight tag to search for.
        :type joint: c4d.modules.character.CAJointObject
        :param joint: The joint to search for.
        :rtype: tuple(int, int)
        :return: The tag's index in the joint list, or **NOTOK**/**-1** if not found, and the joint's index in the joint list, or **NOTOK**/**-1** if not found.
        
        
        """
        ...
    
    def GetJointId(self, doc: BaseDocument, tag: CAWeightTag, joint: CAJointObject) -> int:
        """    
        Returns the unique Id of a joint.
        
        .. note::
        
        This Id remains valid even if the joint list changes or if undo/redo is used.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tag: c4d.modules.character.CAWeightTag
        :param tag: The weight tag to search for.
        :type joint: c4d.modules.character.CAJointObject
        :param joint: The joint to search for.
        :rtype: int
        :return: The joint unique Id, or **sys.maxsize** if not found.
        
        
        """
        ...
    
    def GetJointObject(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> CAJointObject:
        """    
        Finds a joint object from its indices or Id in the joint list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: c4d.modules.character.CAJointObject
        :return: The joint object, or **None** if not found.
        
        
        """
        ...
    
    def GetWeightTag(self, doc: BaseDocument, tagIdx: int) -> CAWeightTag:
        """    
        Finds a weight tag from its index in the joint list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :rtype: c4d.modules.character.CAWeightTag
        :return: The weight tag, or **None** if not found.
        
        
        """
        ...
    
    def GetMeshObject(self, doc: BaseDocument, tagIdx: int) -> BaseObject:
        """    
        Finds the object owning the weight tag from a tag index in the joint list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :rtype: c4d.BaseObject
        :return: The mesh object, or **None** if not found.
        
        
        """
        ...
    
    def ValidateJointIndex(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> bool:
        """    
        Validates tag and joint indices before access.
        
        .. warning::
        
        Call before functions that require tag and joint indices to avoid crashes.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: bool
        :return: **True** if tag and joint indices are valid, otherwise **False**.
        
        
        """
        ...
    
    def IsJointSelected(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> bool:
        """    
        Checks if a joint of the Weight Manager list is selected.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: bool
        :return: **True** if the joint was found and is selected, otherwise **False**.
        
        
        """
        ...
    
    def SelectJoint(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> bool:
        """    
        Selects a joint of the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: bool
        :return: **True** if the joint was selected, otherwise **False**.
        
        
        """
        ...
    
    def UnselectJoint(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> bool:
        """    
        Deselects a joint of the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: bool
        :return: **True** if the joint was deselected, otherwise **False**.
        
        
        """
        ...
    
    def SelectAllJoints(self, doc: BaseDocument) -> None:
        """    
        Selects all joints of all tags in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        
        
        """
        ...
    
    def UnselectAllJoints(self, doc: BaseDocument) -> None:
        """    
        Deselects all joints of all tags in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        
        
        """
        ...
    
    def UnselectAllJointListNodes(self, doc: BaseDocument) -> None:
        """    
        Deselects all of the nodes in the Weight Manager joint list. This includes all type of nodes (mesh/tag/folder/joint).
        
        .. note::
        
        | The CAWeightMgr API does not allow selecting/deselecting mesh and tags at the moment.
        | As a parent mesh, tag, or folder activates the child joints for painting, call this function to get rid of any mesh/tag that could have been already selected.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        
        
        """
        ...
    
    def IsJointLocked(self, doc: BaseDocument, tagIdx: int, jointIdx: int) -> bool:
        """    
        Checks if a joint of the Weight Manager list is locked.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type tagIdx: int
        :param tagIdx: The tag's index in the joint list.
        :type jointIdx: int
        :param jointIdx: The joint's index in the joint list.
        :rtype: bool
        :return: **True** if the joint was found and is locked, otherwise **False**.
        
        
        """
        ...
    
    def LockAllJoints(self, doc: BaseDocument) -> bool:
        """    
        Locks all joints of all tags in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if all joints got locked, otherwise **False**.
        
        
        """
        ...
    
    def LockSelectedJoints(self, doc: BaseDocument) -> bool:
        """    
        Locks selected joints in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def UnlockAllJoints(self, doc: BaseDocument) -> bool:
        """    
        Unlocks all joints of all tags in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def UnlockSelectedJoints(self, doc: BaseDocument) -> bool:
        """    
        Unlocks selected joints in the Weight Manager list.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def NormalizeWeights(self, doc: BaseDocument) -> bool:
        """    
        Applies a normalization on the selected joints.
        
        .. note::
        
        Some joints can be locked prior to normalization to avoid touching some joints.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ClearWeights(self, doc: BaseDocument) -> bool:
        """    
        Clears all weights on the selected joints.
        
        .. note::
        
        Adds an undo.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def AutoWeight(self, doc: BaseDocument) -> bool:
        """    
        | Runs an auto weight algorithm on the selected joints.
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        .. versionchanged:: R21
        
        `allowNull` parameter no more there.
        
        .. note::
        
        Adds an undo.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def MirrorWeights(self, doc: BaseDocument) -> bool:
        """    
        | Mirrors the weights for the selected joints.
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        .. note::
        
        Adds an undo.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def BakeWeights(self, doc: BaseDocument, normalize: bool) -> bool:
        """    
        | Bakes the effector weights.
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type normalize: bool
        :param normalize: **True** to normalize after bake operation, otherwise **False**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def CopyWeights(self, doc: BaseDocument) -> bool:
        """    
        Copies the weights of the selected joints into the weights clipboard.
        
        .. note::
        
        | Document must be in either point, edge or polygon edit mode.
        | If no selection is present on the mesh, all the point are copied, otherwise only the selected points are copied.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def PasteWeights(self, doc: BaseDocument, merge: bool) -> bool:
        """    
        | Pastes the copied weights on the selected joints.
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type merge: bool
        :param merge:
        
        | **True** to merge with target weights, **False** to replace target weights:
        | **True** adds the source weights to the target weights. For instance, source point with null weight does not affect the final result.
        | **False** replaces all the target weights with the source weights including null source weights. For instance, all target weights are lost and replaced with source weights.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FlipWeights(self, doc: BaseDocument) -> bool:
        """    
        Flips the weights of the selected joints. Each joint is flipped on itself using the local axis specified in Weight Manager container.
        
        .. note::
        
        Both zero and non zero weights are flipped.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SmoothWeights(self, doc: BaseDocument) -> bool:
        """    
        | Smooths the weights of the selected joints.
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :rtype: bool
        :return: **True** if successful, otherwise **True**.
        
        
        """
        ...
    
    def ApplyWeightFunction(self, doc: BaseDocument, allPoints: BaseDocument) -> bool:
        """    
        | Applies the currently selected weighting function to the selected joints (add, smooth, remap etc.).
        | Uses the parameters currently set in the Weight Manager's container for the document.
        
        .. note::
        
        The point selection is fetched from the actual component mode or from point mode if the document is not in component mode.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document for the Weight Manager.
        :type allPoints: c4d.documents.BaseDocument
        :param allPoints: **True** to apply on all the points of the mesh, **False** to apply on point selection.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    

class CAReferencePSD(object):
    def SetInterpolationMode(self, interpMode: int) -> None:
        """    
        Sets the auto weighting interpolation mode.
        
        :type interpMode: int
        :param interpMode: The interpolation mode to set:
        
        .. include:: /consts/CAMORPH_PSDINTERPOLATION_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetInterpolationMode(self) -> int:
        """    
        Returns the auto weighting interpolation mode.
        
        :rtype: int
        :return: The interpolation mode:
        
        .. include:: /consts/CAMORPH_PSDINTERPOLATION_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def ForceJointAsDriver(self, jointIndex: int, forceDriver: bool) -> None:
        """    
        Forces the joint index to be a driver.
        
        .. note::
        
        If any of the joints is marked as a forced driver, only those are considered in automatic weighting.
        
        :type jointIndex: int
        :param jointIndex: The weight tag joint index to use as driver.
        :type forceDriver: bool
        :param forceDriver: **True** if the joint is used as a driver, otherwise **False**.
        
        
        """
        ...
    
    def IsJointForcedAsDriver(self, jointIndex: int) -> bool:
        """    
        Checks if the joint index is a user forced driver.
        
        .. note::
        
        If any of the joints is marked as a forced driver, only those are considered in automatic weighting.
        
        :type jointIndex: int
        :param jointIndex: The weight tag joint index to use as driver.
        :rtype: bool
        :return: **True** if the joint is forced as a driver, otherwise **False**.
        
        
        """
        ...
    
    def ClearAllForcedDrivers(self) -> None:
        """    
        Removes all user defined joint as driver and let the system manage it automatically.
        
        
        """
        ...
    
    def RestoreReferencePose(self) -> None:
        """    
        Displays skeleton and user defined controller at the reference pose.
        
        
        """
        ...
    
    def UpdateReferencePose(self) -> None:
        """    
        Updates the current skeleton state as the PSD reference pose.
        
        
        """
        ...
    
    def ClearAllExternalControllers(self) -> None:
        """    
        Removes all external controllers assigned to the reference pose.
        
        
        """
        ...
    
    def GetExternalControllerCount(self) -> int:
        """    
        Return the number of external controllers associated with the reference pose.
        
        :rtype: int
        :return: The external controller count.
        
        
        """
        ...
    
    def GetExternalController(self, controllerIndex: int) -> BaseObject:
        """    
        Returns the controller assigned to the given index.
        
        :type controllerIndex: int
        :param controllerIndex: The controller index: `0` <= *controllerIndex* < :meth:`GetExternalControllerCount`.
        :rtype: c4d.BaseObject
        :return: The external controller, or **None** if the function failed.
        
        
        """
        ...
    
    def GetExternalControllerMatrix(self, controllerIndex: int) -> Matrix:
        """    
        Returns the matrix stored at the given index.
        
        :type controllerIndex: int
        :param controllerIndex: The controller index: `0` <= *controllerIndex* < :meth:`GetExternalControllerCount`.
        :rtype: c4d.Matrix
        :return: The external controller global matrix, or a default :class:`c4d.Matrix() <c4d.Matrix>` if the function failed.
        
        
        """
        ...
    
    def SetExternalControllerMatrix(self, controllerIndex: int, globalMatrix: Matrix) -> int:
        """    
        Adds or adjusts the given controller global matrix to be part of the reference pose.
        
        :type controllerIndex: int
        :param controllerIndex: The controller index: `0` <= *controllerIndex* < :meth:`GetExternalControllerCount`.
        :type globalMatrix: c4d.Matrix
        :param globalMatrix: The global matrix used as a reference.
        :rtype: int
        :return: The index of the controller, **NOTOK**/**-1** if invalid.
        
        
        """
        ...
    
    def RemoveExternalController(self, controllerIndex: int) -> bool:
        """    
        Removes the external controller at the given index.
        
        :type controllerIndex: int
        :param controllerIndex: The controller index: `0` <= *controllerIndex* < :meth:`GetExternalControllerCount`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    

class CAPoseMorphTag(BaseTag):
    def __init__(self) -> None:
        """    
        Create a new pose morph tag.
        
        :rtype: c4d.modules.character.CAPoseMorphTag
        :return: The new pose morph tag.
        
        
        """
        ...
    
    def AddMorph(self) -> CAMorph:
        """    
        Add a morph to the morph tag.
        
        :rtype: c4d.modules.character.CAMorph
        :return: The new morph.
        
        
        """
        ...
    
    def GetMorphBase(self) -> CAMorph:
        """    
        Get the morph base of the morph tag.
        
        :rtype: c4d.modules.character.CAMorph
        :return: The morph base.
        
        
        """
        ...
    
    def GetMorphIndex(self, morph: CAMorph) -> int:
        """    
        Retrieves the index for the given *morph*.
        
        .. versionadded:: R17.053
        
        :type morph: c4d.modules.character.CAMorph
        :param morph: The morph to search for.
        :rtype: int
        :return: The index for *morph*.
        
        
        """
        ...
    
    def GetMorphCount(self) -> int:
        """    
        Returns the Morph count.
        
        :rtype: int
        :return: The morph count.
        
        
        """
        ...
    
    def GetMorphID(self, index: int) -> DescID:
        """    
        Return the morph ID.
        
        :type index: int
        :param index: The index of the morph.
        :raise IndexError: If the morph *index* is out of range : *0<=index<*:meth:`GetMorphCount`.
        :rtype: c4d.DescID
        :return: The morph ID.
        
        
        """
        ...
    
    def GetMorph(self, index: int) -> CAMorph:
        """    
        Return the morph.
        
        :type index: int
        :param index: The index of the morph.
        :raise IndexError: If the morph *index* is out of range : *0<=index<*:meth:`GetMorphCount`.
        :rtype: c4d.modules.character.CAMorph
        :return: The morph.
        
        
        """
        ...
    
    def GetActiveMorph(self) -> CAMorph:
        """    
        Retrieves the active morph (usually the one selected).
        
        .. versionadded:: R17.053
        
        :rtype: c4d.modules.character.CAMorph
        :return: The active morph.
        
        
        """
        ...
    
    def RemoveMorph(self, index: int) -> None:
        """    
        Remove a morph by *index*.
        
        :type index: int
        :param index: The index of the morph.
        :raise IndexError: If the morph *index* is out of range : *0<=index<*:meth:`GetMorphCount`.
        
        
        """
        ...
    
    def GetActiveMorphIndex(self) -> int:
        """    
        Get the index of the current active morph.
        
        :rtype: int
        :return: The index.
        
        
        """
        ...
    
    def SetActiveMorphIndex(self, index: int) -> None:
        """    
        Set the active morph index.
        
        .. versionadded:: R17.053
        
        :type index: int
        :param index: The active morph index to set.
        :raise IndexError: If the morph *index* is out of range : *0<=index<*:meth:`GetMorphCount`.
        
        
        """
        ...
    
    def GetMode(self) -> int:
        """    
        Get the mode of the morph tag.
        
        :rtype: int
        :return: The mode.
        
        
        """
        ...
    
    def InitMorphs(self) -> None:
        """    
        Initialize the morphs.
        
        
        """
        ...
    
    def UpdateMorphs(self) -> None:
        """    
        Update the morphs.
        
        
        """
        ...
    
    def ExitEdit(self, doc: BaseDocument, apply: bool) -> bool:
        """    
        | Must be called before doing anything to a morph tag.
        | If the user is in Edit mode and making changes to the morph, these are not applied until this function is called and, if not called, they are lost.
        | Set apply to **True** if any user changes should be stored. This is normally the case.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type apply: bool
        :param apply: Set to **False** if any user changes should be stored, otherwise set to **True**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPSDFeedbackColor(self) -> Vector:
        """    
        Retrieves the PSD color used for feedback.
        
        .. versionadded:: R19
        
        :rtype: c4d.Vector
        :return: The PSD feedback color.
        
        
        """
        ...
    
    def SetPSDFeedbackColor(self, color: Vector) -> bool:
        """    
        Sets the PSD color used for feedback.
        
        .. versionadded:: R19
        
        :type color: c4d.Vector
        :param color: The PSD feedback color to set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPSDFeedbackColorEnabled(self) -> bool:
        """    
        Checks if PSD color feedback is enabled or disabled.
        
        .. versionadded:: R19
        
        :rtype: bool
        :return: **True** if PSD color feedback is enabled, otherwise **False**.
        
        
        """
        ...
    
    def SetPSDFeedbackColorEnabled(self, active: bool) -> bool:
        """    
        Sets the enable/disable state of the PSD color used for feedback.
        
        .. versionadded:: R19
        
        :type active: bool
        :param active: **True** to enable PSD color feedback, otherwise **False**.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPSDOrientThreshold(self) -> float:
        """    
        Retrieves the PSD orient radian threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :rtype: float
        :return: The PSD orient threshold (in radian).
        
        
        """
        ...
    
    def SetPSDOrientThreshold(self, radianThreshold: float) -> bool:
        """    
        Sets the PSD orient radian threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :type radianThreshold: float
        :param radianThreshold: The PSD orient threshold to set (in radian).
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPSDTwistThreshold(self) -> float:
        """    
        Retrieves the PSD twist radian threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :rtype: float
        :return: The PSD twist threshold (in radian).
        
        
        """
        ...
    
    def SetPSDTwistThreshold(self, radianThreshold: float) -> bool:
        """    
        Sets the PSD twist radian threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :type radianThreshold: float
        :param radianThreshold: The PSD twist threshold to set (in radian).
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPSDPositionThreshold(self) -> float:
        """    
        Retrieves the PSD position distance threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :rtype: float
        :return: The PSD position threshold (distance).
        
        
        """
        ...
    
    def SetPSDPositionThreshold(self, distanceThreshold: float) -> bool:
        """    
        Sets the PSD position distance threshold used in automatic weighting.
        
        .. versionadded:: R19
        
        :type distanceThreshold: float
        :param distanceThreshold: The PSD position threshold to set (distance).
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetMorphPSDID(self, morphIndex: int, psdAttributeID: int) -> DescID:
        """    
        Retrieves the description ID for the morph slider at *morphIndex*.
        
        .. versionadded:: R19
        
        :type morphIndex: int
        :param morphIndex: The morph index: `0` <= *morphIndex* < :meth:`GetMorphCount`.
        :raise IndexError: If *morphIndex* is out of range.
        :type psdAttributeID: int
        :param psdAttributeID: The attribute ID defined in `tcaposemorph.h`: **ID_CA_POSE_PSD_ORIENT_INTERP_WEIGHT** <= *psdAttributeID* < **ID_CA_POSE_PSD_AUTOWEIGHT_INTERP**.
        :rtype: c4d.DescID
        :return: The description ID of the specified attribute.
        
        
        """
        ...
    

class CAMorphNode(object):
    def GetUp(self) -> CAMorphNode:
        """    
        Retrieves the parent morph node.
        
        :rtype: c4d.modules.character.CAMorphNode
        :return: The parent node.
        
        
        """
        ...
    
    def GetNext(self) -> CAMorphNode:
        """    
        Retrieves the next morph node.
        
        :rtype: c4d.modules.character.CAMorphNode
        :return: The next node.
        
        
        """
        ...
    
    def GetPrev(self) -> CAMorphNode:
        """    
        Retrieves the previous morph node.
        
        :rtype: c4d.modules.character.CAMorphNode
        :return: The previous node.
        
        
        """
        ...
    
    def GetDown(self) -> CAMorphNode:
        """    
        Retrieves the first child of the morph node.
        
        :rtype: c4d.modules.character.CAMorphNode
        :return: The first child.
        
        
        """
        ...
    
    def GetLink(self, tag: CAPoseMorphTag, morph: CAMorph, doc: BaseDocument) -> BaseList2D:
        """    
        Retrieves the object linked to the morph node.
        
        .. versionadded:: R18.057
        
        :type tag: c4d.modules.character.CAPoseMorphTag
        :param tag: The morph tag containing the morph data.
        :type morph: c4d.modules.character.CAMorph
        :param morph: The morph containing the morph node.
        :type doc: c4d.documents.BaseDocument
        :param doc: The document containing the linked object.
        :rtype: c4d.BaseList2D
        :return: The linked object if there is one, or **None**.
        
        
        """
        ...
    
    def GetInfo(self) -> int:
        """    
        Returns the information on what morph data is stored in the morph node.
        
        :rtype: int
        :return: The data flags:
        
        .. include:: /consts/CAMORPH_DATA_FLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetP(self) -> Vector:
        """    
        Returns the position of the morph node.
        
        :rtype: c4d.Vector
        :return: The position.
        
        
        """
        ...
    
    def GetS(self) -> Vector:
        """    
        Returns the scale of the morph node.
        
        :rtype: c4d.Vector
        :return: The scale.
        
        
        """
        ...
    
    def GetR(self) -> Vector:
        """    
        Returns the rotation of the morph node.
        
        :rtype: c4d.Vector
        :return: The rotation.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Returns the point count.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The point count.
        
        
        """
        ...
    
    def SetPointCount(self, cnt: int) -> bool:
        """    
        Sets the point count.
        
        :type cnt: int
        :param cnt: The point count to be set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetPoint(self, index: int) -> Vector:
        """    
        Retrieves a point of the morph node.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type index: int
        :param index: The index of the point to get.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetPointCount`.
        :rtype: c4d.Vector
        :return: The point at *index*.
        
        
        """
        ...
    
    def SetPoint(self, index: int, pnt: Vector) -> None:
        """    
        Sets a point of the morph node.
        
        :type index: int
        :param index: The index of the point.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetPointCount`.
        :type pnt: c4d.Vector
        :param pnt: The point to be set.
        
        
        """
        ...
    
    def GetTangentCount(self) -> int:
        """    
        Returns the tangent count.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The tangent count.
        
        
        """
        ...
    
    def SetTangentCount(self, cnt: int) -> bool:
        """    
        Sets the tangent count.
        
        :type cnt: int
        :param cnt: The tangent count to be set.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetTangent(self, index: int) -> Vector:
        """    
        Retrieves a tangent of the morph node.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type index: int
        :param index: The index of the tangent to get.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetTangentCount`.
        :rtype: c4d.Vector
        :return: The tangent.
        
        
        """
        ...
    
    def SetTangent(self, index: int, v: Vector) -> None:
        """    
        Sets the tangent at *index*.
        
        :type index: int
        :param index: The tangent index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetTangentCount`.
        :type v: c4d.Vector
        :param v: The tangent to be set.
        
        
        """
        ...
    
    def GetVertexMapTagCount(self) -> int:
        """    
        Retrieves the number of vertex map tags of the morph node.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The vertex map tag count.
        
        
        """
        ...
    
    def GetVertexMapCount(self, tindex: int) -> int:
        """    
        Retrieves the size of the vertex map at *tindex*.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int
        :param tindex: The vertex map tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetVertexMapTagCount`.
        :rtype: int
        :return: The vertex map count.
        
        
        """
        ...
    
    def SetVertexMapTagCount(self, tindex: int, cnt: int) -> bool:
        """    
        Sets the size of the vertex map at *tindex*.
        
        :type tindex: int
        :param tindex: The vertex map tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetVertexMapTagCount`.
        :type cnt: int
        :param cnt: The count.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetVertexMap(self, tindex: int, index: int) -> float:
        """    
        Retrieves the vertex map value at *index* of the *tindex* vertex map.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int
        :param tindex: The vertex map tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetVertexMapTagCount`.
        :type index: int
        :param index: The vertex map index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetVertexMapCount`.
        :rtype: float
        :return: The vertex map value.
        
        
        """
        ...
    
    def SetVertexMap(self, tindex: int, index: int, v: float) -> None:
        """    
        Sets the vertex map value at *index* of the *tindex* vertex map.
        
        :type tindex: int
        :param tindex: The vertex map tag index.
        :raise IndexError: If *tindex* is out of range : *0<=index<*:meth:`GetVertexMapTagCount`.
        :type index: int
        :param index: The vertex map index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetVertexMapCount`.
        :type v: float
        :param v: The vertex map value to be set.
        
        
        """
        ...
    
    def GetParamCount(self) -> int:
        """    
        Retrieves the parameter count.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The parameter count.
        
        
        """
        ...
    
    def SetParamCount(self, cnt: int) -> None:
        """    
        Sets the parameter count.
        
        :type cnt: int
        :param cnt: The parameter count to be set.
        
        
        """
        ...
    
    def GetUVTagCount(self) -> int:
        """    
        Retrieves the UV tag count.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The UV tag count.
        
        
        """
        ...
    
    def GetUVCount(self, tindex: int) -> int:
        """    
        Retrieves the UV coordinates count of the UV tag at *tindex*.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int
        :param tindex: The UV tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetUVTagCount`.
        :rtype: int
        :return: The UV coordinates count.
        
        
        """
        ...
    
    def GetUV(self, tindex: int, index: int) -> None:
        """    
        Retrieves the UV coordinate *index* of the *tindex* UV tag.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int
        :param tindex: The UV tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetUVTagCount`.
        :type index: int
        :param index: The UV coordinates index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetUVCount`.
        :rtype: tuple(:class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
        :return: The UV structure.
        
        
        """
        ...
    
    def SetUV(self, tindex: int, index: int, a: Vector, b: Vector, c: Vector, d: Vector) -> None:
        """    
        Sets the UV coordinate *index* of the *tindex* UV tag.
        
        :type tindex: int
        :param tindex: The UV tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetUVTagCount`.
        :type index: int
        :param index: The UV coordinates index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetUVCount`.
        :type a: c4d.Vector
        :param a: The UVW coordinate for the first point.
        :type b: c4d.Vector
        :param b: The UVW coordinate for the second point.
        :type c: c4d.Vector
        :param c: The UVW coordinate for the third point.
        :type d: c4d.Vector
        :param d: The UVW coordinate for the fourth point.
        
        
        """
        ...
    
    def SetUVCount(self, tindex: int, cnt: int) -> bool:
        """    
        Sets the UV coordinates count of the UV tag at *tindex*.
        
        :type tindex: int
        :param tindex: The UV tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetUVTagCount`.
        :type cnt: int
        :param cnt: The new UV coordinates count.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetParam(self, index: int) -> None:
        """    
        Returns a parameter.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type index: int
        :param index: The parameter index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetParamCount`.
        :rtype: dict{**data**: any, **id**: :class:`DescID <c4d.DescID>`}
        :return: The parameter.
        
        
        """
        ...
    
    def SetParam(self, index: int, data: Any, id: DescID) -> None:
        """    
        Sets a parameter.
        
        :type index: int
        :param index: The parameter index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetParamCount`.
        :type data: any
        :param data: The data to be set.
        :type id: c4d.DescID
        :param id: The id.
        
        
        """
        ...
    
    def GetWeightMapTagCount(self) -> int:
        """    
        Retrieves the number of weight map tags.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: int
        :return: The weight map tag count.
        
        
        """
        ...
    
    def GetWeightMapJointCount(self, tindex: int) -> int:
        """    
        Retrieves the joint count of the weight tag at *tindex*.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int.
        :param tindex: The weight tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetWeightMapTagCount`.
        :rtype: int
        :return: The weight map joint count.
        
        
        """
        ...
    
    def GetWeightMapCount(self, tindex: int, jindex: int) -> int:
        """    
        Retrieves the weights count of the joint at *jindex* of *tindex* weight tag.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int.
        :param tindex: The weight tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetWeightMapTagCount`.
        :type jindex: int
        :param jindex: The joint index.
        :raise IndexError: If *jindex* is out of range : *0<=jindex<*:meth:`GetWeightMapJointCount`.
        :rtype: int
        :return: The weight count of the specified joint.
        
        
        """
        ...
    
    def SetWeightMapCount(self, tindex: int, jindex: int, cnt: int) -> bool:
        """    
        Sets the weights count of the joint at *jindex* of *tindex* weight tag.
        
        :type tindex: int.
        :param tindex: The weight tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetWeightMapTagCount`.
        :type jindex: int
        :param jindex: The joint index.
        :raise IndexError: If *jindex* is out of range : *0<=jindex<*:meth:`GetWeightMapJointCount`.
        :type cnt: int
        :param cnt: The new weight count.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetWeightMap(self, tindex: int, jindex: int, index: int) -> float:
        """    
        Retrieves the weight at *index* of *jindex* joint and *tindex* weight tag.
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :type tindex: int.
        :param tindex: The weight tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetWeightMapTagCount`.
        :type jindex: int
        :param jindex: The joint index.
        :raise IndexError: If *jindex* is out of range : *0<=jindex<*:meth:`GetWeightMapJointCount`.
        :type index: int
        :param index: The weight index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetWeightMapCount`.
        :rtype: float
        :return: The weight value.
        
        
        """
        ...
    
    def SetWeightMap(self, tindex: int, jindex: int, index: int, v: float) -> None:
        """    
        Sets the weight at *index* of *jindex* joint and *tindex* weight tag.
        
        :type tindex: int.
        :param tindex: The weight tag index.
        :raise IndexError: If *tindex* is out of range : *0<=tindex<*:meth:`GetWeightMapTagCount`.
        :type jindex: int
        :param jindex: The joint index.
        :raise IndexError: If *jindex* is out of range : *0<=jindex<*:meth:`GetWeightMapJointCount`.
        :type index: int
        :param index: The weight index.
        :raise IndexError: If *index* is out of range : *0<=index<*:meth:`GetWeightMapCount`.
        :type v: float
        :param v: The new weight value.
        
        
        """
        ...
    
    def GetPSDReference(self) -> CAReferencePSD:
        """    
        Retrieves the PSD data for a point pose holding the reference pose and providing multiple functions dedicated to PSD behavior.
        
        .. versionadded:: R19
        
        .. seealso::
        
        :meth:`CAMorph.SetMode` to retrieve all data.
        
        :rtype: c4d.modules.character.CAReferencePSD
        :return: The PSD referential for the morph node.
        
        
        """
        ...
    

class CAMorph(object):
    def GetName(self) -> str:
        """    
        Get the name of the morph.
        
        :rtype: str
        :return: The name.
        
        
        """
        ...
    
    def SetName(self, name: str) -> None:
        """    
        Set the name of the morph.
        
        :type name: str
        :param name: The name.
        
        
        """
        ...
    
    def GetID(self) -> int:
        """    
        Get the ID of the morph.
        
        :rtype: int
        :return: The ID.
        
        
        """
        ...
    
    def CopyFrom(self, src: CAMorph, trn: Any, flags: int) -> bool:
        """    
        Get the ID of the morph.
        
        :type src: c4d.modules.character.CAMorph
        :param src: The source morph.
        :type trn: any
        :param trn: Set to **None**, currently not used.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/CAMORPH_COPY.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetFirst(self) -> CAMorphNode:
        """    
        Get the first morph node.
        
        :rtype: c4d.modules.character.CAMorphNode
        :return: The first morph node.
        
        
        """
        ...
    
    def FindIndex(self, tag: CAPoseMorphTag, bl: BaseList2D) -> int:
        """    
        Retrieves the index of the morph node for the object specified by bl.
        
        .. note::
        
        A single morph can be applied to a hierarchy of objects,
        each has a representation in the morph as a :class:`CAMorphNode`.
        
        :param tag: The morph tag containing the morph node.
        :type tag: c4d.modules.character.CAPoseMorphTag
        :param bl: The object connected to the morph node.
        :type bl: c4d.BaseList2D
        :return: The index of the morph node of the specified object.
        :rtype: int
        
        
        """
        ...
    
    def SetMode(self, doc: BaseDocument, tag: CAPoseMorphTag, flags: int, mode: int) -> int:
        """    
        Set the mode.
        
        .. note::
        
        | This is not the mode a user would change but data inside the morph.
        | It must be restored to the original mode once changes are finished.
        | To change the morph tag's modes or parameters use C4DAtom::SetParameter().
        
        | Example: Point data could be stored as rotational or correctional and in a delta form (only differences from the base).
        | This can not be edited in this form so the data mode must be changed to relative (c4d.CAMORPH_MODE_REL)
        or absolute (c4d.CAMORPH_MODE_ABS) before editing and then restored to (c4d.CAMORPH_MODE_AUTO) when finished.
        | The flags must be passed as c4d.CAMORPH_MODE_FLAGS_EXPAND to expand the data from the delta form and
        then returned with c4d.CAMORPH_MODE_FLAGS_COLLAPSE when finished.
        | For example VAMP uses the following line to expand all data types to relative data
        
        .. code-block:: python
        
        smorph.SetMode(doc, s_morphtag, c4d.CAMORPH_MODE_FLAGS_ALL | c4d.CAMORPH_MODE_FLAGS_EXPAND, c4d.CAMORPH_MODE_REL)
        
        It then does some changes and finally restores all types to collapsed (delta) form and to the users mode (AUTO):
        
        .. code-block:: python
        
        smorph.SetMode(doc, s_morphtag, c4d.CAMORPH_MODE_FLAGS_ALL | c4d.CAMORPH_MODE_FLAGS_COLLAPSE, c4d.CAMORPH_MODE_AUTO)
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type tag: c4d.modules.character.CAPoseMorphTag
        :param tag: The morph tag.
        :type flags: int
        :param flags: The value:
        
        .. include:: /consts/CAMORPH_MODE_FLAGS.rst
        :start-line: 3
        
        :type mode: int
        :param mode: The mode:
        
        .. include:: /consts/CAMORPH_MODE.rst
        :start-line: 3
        
        :rtype: int
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def Store(self, doc: BaseDocument, tag: CAPoseMorphTag, flags: int) -> None:
        """    
        Store the morph.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type tag: c4d.modules.character.CAPoseMorphTag
        :param tag: The morph tag.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/CAMORPH_DATA_FLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def Apply(self, doc: BaseDocument, tag: CAPoseMorphTag, flags: int) -> None:
        """    
        Apply the morph.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type tag: c4d.modules.character.CAPoseMorphTag
        :param tag: The morph tag.
        :type flags: int
        :param flags: The flags:
        
        .. include:: /consts/CAMORPH_DATA_FLAGS.rst
        :start-line: 3
        
        
        """
        ...
    

class CAJointObject(BaseObject):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.character.CAJointObject
        :return: The new joint object.
        
        
        """
        ...
    
    def GetBone(self) -> None:
        """    
        Get the bone data for this joint
        
        .. code-block:: python
        
        m, len = cajointobject.GetBone()
        
        :rtype: list[:class:`Matrix <c4d.Matrix>`, float]
        :return: The matrix and the length of the bone.
        
        
        """
        ...
    
    def GetWeightTag(self) -> None:
        """    
        Get the weight tag corresponding to this joint
        
        .. code-block:: python
        
        weight = cajointobject.GetWeightTag()
        if not weight: return
        
        print weight["op"] #c4d.BaseTag
        print weight["index"] #int
        
        :rtype: dict{**op**: :class:`BaseTag <c4d.BaseTag>`, **index**: int}
        :return: The weight tag and the index of the tag.
        
        
        """
        ...
    

