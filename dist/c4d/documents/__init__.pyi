from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseList2D, BaseContainer, BaseDraw, GeListNode, DescID, BaseTime, BaseObject, BaseTag, BaseMaterial, C4DAtom, CKey
from c4d.modules.net import RenderJob
from uuid import UUID
from c4d.bitmaps import BaseBitmap
from c4d.modules.thinkingparticles import TP_MasterSystem
from c4d.threading import BaseThread
from c4d.modules.takesystem import TakeData
from c4d.storage import MemoryFileStruct


class RenderData(BaseList2D):
    def __init__(self) -> None:
        """    
        :rtype: c4d.documents.RenderData
        :return: The new render data.
        
        
        """
        ...
    
    def GetFirstVideoPost(self) -> BaseVideoPost:
        """    
        Returns the first videopost of the render setting.
        
        :rtype: c4d.documents.BaseVideoPost
        :return: The first videopost.
        
        .. versionchanged:: R19
        
        Returns a :class:`BaseVideoPost <c4d.documents.BaseVideoPost>` object.
        
        
        """
        ...
    
    def InsertVideoPost(self, pvp: BaseVideoPost, pred: BaseVideoPost) -> None:
        """    
        Inserts *pvp* as the last videopost in the render setting.
        
        :type pvp: c4d.documents.BaseVideoPost
        :param pvp:
        
        The videopost to insert.
        
        .. versionchanged:: R19
        
        Accepts a :class:`BaseVideoPost <c4d.documents.BaseVideoPost>` object.
        
        :type pred: c4d.documents.BaseVideoPost
        :param pred:
        
        The videopost to insert *pvp* after, or do not pass anything to insert *pvp* first.
        
        .. versionchanged:: R19
        
        Accepts a :class:`BaseVideoPost <c4d.documents.BaseVideoPost>` object.
        
        
        """
        ...
    
    def InsertVideoPostLast(self, pvp: BaseVideoPost) -> None:
        """    
        Inserts *pvp* as the last videopost in the render setting.
        
        :type pvp: c4d.documents.BaseVideoPost
        :param pvp:
        
        The videopost to insert.
        
        .. versionchanged:: R19
        
        Accepts a :class:`BaseVideoPost <c4d.documents.BaseVideoPost>` object.
        
        
        """
        ...
    
    def GetFirstMultipass(self) -> BaseList2D:
        """    
        Returns the first multipass of the render setting.
        
        :rtype: c4d.BaseList2D
        :return: The first multipass.
        
        
        """
        ...
    
    def InsertMultipass(self, obj: BaseList2D, pred: Optional[BaseList2D] = ...) -> None:
        """    
        | Inserts the multipass channel into the render setting.
        | Optionally specify the insertion position with the *pred* parameter, giving the multipass channel before (right above) the wanted position.
        | Otherwise the multipass channel is inserted at the first position in the list::
        
        .. code-block:: python
        
        import c4d
        
        # Create a depth object in the multipass object list
        
        def main(doc):
        rd = doc.GetActiveRenderData()          # Get the current renderdata
        vdepth=c4d.BaseList2D(c4d.Zmultipass)   # create a multipass object (all have the same plugin type ID 'Zmultipass')
        vdepth.GetDataInstance()[c4d.MULTIPASSOBJECT_TYPE] = c4d.VPBUFFER_DEPTH #Set type to 'Depth'
        rd.InsertMultipass(vdepth)              # Insert into Multipass list
        c4d.EventAdd()                          # Send global event
        
        if __name__=='__main__':
        main(doc)
        
        :type obj: c4d.BaseList2D
        :param obj: The multipass object to insert.
        :type pred: c4d.BaseList2D
        :param pred: Optional point to insert the multipass channel.
        
        
        """
        ...
    

class LayerObject(BaseList2D):
    def __init__(self) -> None:
        """    
        :rtype: c4d.documents.LayerObject
        :return: The new layer object.
        
        
        """
        ...
    

class BatchRender(object):
    def Open(self) -> bool:
        """    
        Open the batch render.
        
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def AddFile(self, file: str, number: int) -> bool:
        """    
        Add a scene file to the batch render.
        
        :type file: str
        :param file: Path to the scene.
        :type number: int
        :param number: The index of the scene file in the list.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def DelFile(self, file: str) -> bool:
        """    
        Delete a file from the list.
        
        :type file: str
        :param file: Path to the scene.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def IsRendering(self) -> bool:
        """    
        Check if the batch render is in the render mode.
        
        :rtype: bool
        :return: **True** if the batch render is in render mode, otherwise **False**.
        
        
        """
        ...
    
    def GetElementCount(self) -> int:
        """    
        Return the count how many scenes are in the batch render list.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def SetRendering(self, set: int) -> None:
        """    
        Start or stop the rendering of the batch render.
        
        :type set: int
        :param set: One of the modes:
        
        .. include:: /consts/BR.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetElement(self, n: int) -> str:
        """    
        Return the scene path of the element.
        
        :type n: int
        :param n: The element.
        :raise IndexError: If the element index *n* is out of range : *0<=n<*:meth:`GetElementCount`.
        :rtype: str
        :return: The path.
        
        
        """
        ...
    
    def EnableElement(self, n: int, bSet: bool) -> None:
        """    
        Enable or disable the element for the rendering.
        
        :type n: int
        :param n: The element.
        :raise IndexError: If the element index *n* is out of range : *0<=n<*:meth:`GetElementCount`.
        :type bSet: bool
        :param bSet: **True** to enable the element, otherwise **False**.
        
        
        """
        ...
    
    def GetEnableElement(self, n: int) -> bool:
        """    
        Enable or disable the element for the rendering.
        
        :type n: int
        :param n: The element.
        :raise IndexError: If the element index *n* is out of range : *0<=n<*:meth:`GetElementCount`.
        :rtype: bool
        :return: **True** when the element is enabled, otherwise **False**.
        
        
        
        """
        ...
    
    def GetElementStatus(self, n: int) -> int:
        """    
        Get the status of the element.
        
        :type n: int
        :param n: The element.
        :raise IndexError: If the element index *n* is out of range : *0<=n<*:meth:`GetElementCount`.
        :rtype: int
        :return: The status:
        
        .. include:: /consts/RM.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetJsonJobs(self) -> List[RenderJob]:
        """    
        Get the JSON jobs.
        
        .. versionadded: 15.037
        
        :rtype: List[c4d.modules.net.RenderJob]
        :return: The JSON jobs.
        
        
        """
        ...
    
    def GetFrameBitmap(self, nodeUuid: UUID, frameUuid: UUID) -> None:
        """    
        Private.
        
        .. versionadded: 15.037
        
        :type nodeUuid: uuid.Uuid
        :param nodeUuid: Uuid of the internal node.
        :type frameUuid: uuid.uuid
        :param frameUuid: Uuid of the internal bitmap of the frame.
        
        
        """
        ...
    
    def SetUseNet(self, n: int, on: bool) -> None:
        """    
        Enable or disable the use of NET/Team Render.
        
        :type n: int
        :param n: The element.
        :raise IndexError: If the element index *n* is out of range : *0<=n<*:meth:`GetElementCount`.
        :type on: bool
        :param on: **True** to enable NET, **False** to disable it.
        
        
        """
        ...
    

class BaseVideoPost(BaseList2D):
    def __init__(self, type: int) -> None:
        """    
        Initializes a new :class:`BaseVideoPost <c4d.documents.BaseVideoPost>`.
        
        :type type: int
        :param type: The videopost type: :doc:`/types/videoposts`.
        :rtype: c4d.documents.BaseVideoPost
        :return: A new videopost.
        
        
        """
        ...
    
    def RenderEngineCheck(self, type: int) -> bool:
        """    
        Checks if a videopost is available for a certain render engine.
        
        :type type: int
        :param type: The ID of the render engine.
        :rtype: bool
        :return: **True** if the videopost is available for the specified render engine, otherwise **False**.
        
        
        """
        ...
    
    def StereoMergeImages(self, dest: BaseBitmap, source: List[BaseBitmap], settings: BaseContainer, transform: int) -> bool:
        """    
        Merges stereoscopic images for rendering.
        
        :type dest: c4d.bitmaps.BaseBitmap
        :param dest: The destination bitmap to be filled with the merged stereoscopic image.
        :type source: List[c4d.bitmaps.BaseBitmap]
        :param source: A list containing the stereoscopic images.
        :type settings: c4d.BaseContainer
        :param settings: The stereoscopic render settings: See `RDATA_STEREO` in `drendersettings.h`.
        :type transform: int
        :param transform: The color space transformation mode:
        
        .. include:: /consts/COLORSPACETRANSFORMATION.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the stereo images were merged, otherwise **False**.
        
        
        """
        ...
    
    def StereoGetCameraCountEditor(self, doc: BaseDocument, bd: BaseDraw) -> int:
        """    
        Returns the number of stereoscopic editor cameras.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type bd: c4d.BaseDraw
        :param bd: The active view.
        :rtype: int
        :return: The number of stereoscopic cameras.
        
        
        """
        ...
    
    def StereoGetCameraCountRenderer(self, doc: BaseDocument, rd: RenderData) -> int:
        """    
        Returns the number of stereoscopic cameras used for rendering.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type rd: c4d.documents.RenderData
        :param rd: The active render settings.
        :rtype: int
        :return: The number of stereoscopic cameras.
        
        
        """
        ...
    
    def StereoGetCameraInfo(self, doc: BaseDocument, bd: BaseDraw, rd: RenderData, index: int) -> None:
        """    
        Retrieves the information for a stereoscopic camera.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The active document.
        :type bd: c4d.BaseDraw
        :param bd: The active view.
        :type rd: c4d.documents.RenderData
        :param rd: The active render settings.
        :type index: int
        :param index: The index of the stereoscopic camera.
        :rtype: dict{'m': :class:`c4d.Matrix`, 'off_x': float, 'off_y': float, 'name': str}
        :return: A dictionary (**None** if the function failed) with the following information for the stereoscopic camera:
        
        |
        | `m`: :class:`c4d.Matrix`: Matrix of the stereoscopic camera.
        | `off_x`: `float`: Stereoscopic camera film X offset.
        | `off_y`: `float`: Stereoscopic camera film Y offset.
        | `name`: `str`: Name of the stereoscopic camera.
        
        
        """
        ...
    

class BaseDocument(BaseList2D):
    def __init__(self) -> None:
        """    
        :rtype: c4d.documents.BaseDocument
        :return: The new document.
        
        
        """
        ...
    
    def SetFps(self, fps: int) -> None:
        """    
        Set the frames per second.
        
        :type fps: int
        :param fps: The fps.
        
        
        """
        ...
    
    def GetFps(self) -> int:
        """    
        Returns the fps of the document.
        
        :rtype: int
        :return: The fps
        
        
        """
        ...
    
    def SetLOD(self, lod: float) -> None:
        """    
        Get the Level of Detail for this document.
        
        :type lod: float
        :param lod: The default level of detail values are:
        
        ======= =======
        Low       0.25
        Medium    0.5
        High      1.0
        ======= =======
        
        
        """
        ...
    
    def GetLOD(self) -> float:
        """    
        Get the Level of Detail for this document.
        
        :rtype: float
        :return: The default level of detail values are:
        
        ======= =======
        Low       0.25
        Medium    0.5
        High      1.0
        ======= =======
        
        
        """
        ...
    
    def GetRenderLod(self) -> bool:
        """    
        Get if the level of detail for rendering should be used in the editor.
        
        :rtype: bool
        :return: **True** if using the render lod.
        
        
        """
        ...
    
    def SetRenderLod(self, lod: bool) -> None:
        """    
        Set the level of detail for rendering.
        
        :type lod: bool
        :param lod: **True** if using the render lod.
        
        
        """
        ...
    
    def GetDrawTime(self) -> int:
        """    
        Get the editor redraw time.
        
        :rtype: int
        :return: The editor redraw time.
        
        
        """
        ...
    
    def GetLayerObjectRoot(self) -> GeListNode:
        """    
        Returns the list of layers of the document.
        
        .. code-block:: python
        
        def GetFirstLayer(doc):
        # Returns the first layer, if available, otherwise None
        
        return doc.GetLayerObjectRoot().GetDown()
        
        .. warning::
        
        The hierarchy method :meth:`GeListNode.GetDown` can only be called on the returned object.
        
        :rtype: c4d.GeListNode
        :return: The head of the list of the document's layers.
        
        
        """
        ...
    
    def GetSplinePlane(self) -> int:
        """    
        Get the plane in which the splines are created, such as XY plane.
        
        :rtype: int
        :return: Values for this are:
        
        .. include:: /consts/PRIM_PLANE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetRewind(self, flags: int) -> None:
        """    
        Rewinds the whole document (from time 0 to current time) when the next event *EVMSG_CHANGE* or :func:`DrawViews() <c4d.DrawViews>` is processed.
        
        :type flags: int
        :param flags: Not used.
        
        
        """
        ...
    
    def GetBaseDrawCount(self) -> int:
        """    
        Get the :class:`BaseDraw <c4d.BaseDraw>` count in the editor view.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def Flush(self) -> None:
        """    
        Empties the document, deleting and freeing all resources used.
        
        
        """
        ...
    
    def SetDocumentName(self, name: str) -> None:
        """    
        Set the file name of the document.
        
        .. note::
        
        *name* must contain the filename part only.
        
        :type name: str
        :param name: The file name part of the document to set.
        
        
        """
        ...
    
    def SetDocumentPath(self, path: str) -> None:
        """    
        Set the path of the document.
        
        .. note::
        
        *path* must contain the path part only.
        
        :type path: str
        :param path: The path part of the document to set.
        
        
        """
        ...
    
    def GetDocumentName(self) -> str:
        """    
        Returns the file name of the document.
        
        :rtype: str
        :return: The file name of the document.
        
        .. note::
        
        If the document has not been saved then the name is in the form 'Untitled 1', for instance for the first unsaved document.
        
        
        """
        ...
    
    def GetDocumentPath(self) -> str:
        """    
        Returns the path of the document.
        
        :rtype: str
        :return: The path of the document.
        
        .. note::
        
        If the document has not been saved then the path is empty.
        
        
        """
        ...
    
    def GetParticleSystem(self) -> TP_MasterSystem:
        """    
        Returns the particle master system of the document.
        
        :rtype: c4d.modules.thinkingparticles.TP_MasterSystem
        :param type: The particle system of the document. Is useless when the document was deleted, **None** if Thinking Particles is not installed.
        
        
        """
        ...
    
    def ForceCreateBaseDraw(self) -> None:
        """    
        | Makes sure that :meth:`GetBaseDraw` (0) is accessible.
        | This is only important in import filters where, at the time, there are no valid base draws.
        
        
        """
        ...
    
    def ExecutePasses(self, bt: Union[None, BaseThread], animation: bool, expressions: bool, caches: bool, flags: int) -> bool:
        """    
        | Animate the current frame of the document.
        | To update the editor you then need to send an update message using :func:`c4d.EventAdd() <c4d.EventAdd>`.
        
        :type bt: Union[None, c4d.threading.BaseThread]
        :param bt: This thread can either be **None** (for the main Cinema 4D thread) or if you are within your own thread then you pass the thread.
        :type animation: bool
        :param animation: Animations are evaluated.
        :type expressions: bool
        :param expressions: Expressions are evaluated.
        :type caches: bool
        :param caches: Caches are evaluated.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/BUILDFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FindSceneHook(self, id: int) -> BaseList2D:
        """    
        Finds a scene hook by ID.
        
        :type id: int
        :param id: The scene hook ID.
        :rtype: c4d.BaseList2D
        :return: The found scene hook, or **None**.
        
        
        """
        ...
    
    def StartUndo(self) -> bool:
        """    
        Tells Cinema 4D to start building a list of undos into a single undo action for the user.
        
        .. warning:
        
        This must be paired with :meth:`EndUndo`.
        
        :rtype: bool
        :return: Success of starting the undo list.
        
        Here is a small example how to write a redo support for newly inserted objects.
        
        .. code-block:: python
        
        import c4d
        
        doc.StartUndo()                     # Start undo support
        cube = c4d.BaseObject(c4d.Ocube)
        
        doc.InsertObject(cube)              # Insert the object
        doc.AddUndo(c4d.UNDOTYPE_NEW, cube) # Support redo the insert operation
        doc.EndUndo()                       # Do not forget to close the undo support
        
        
        """
        ...
    
    def AddUndo(self, type: int, data: BaseList2D, allowFromThread: bool) -> bool:
        """    
        Adds an undo *type* to the list of undo operations started with :meth:`StartUndo`.
        
        .. note::
        
        | Always has to be called before a change is made.
        | In the case of the creation of a new object the call is done afterwards, after insertion into the document/object/track/sequence but before calling subsequent functions like :meth:`BaseDocument.SetActiveObject` which creates another undo:
        
        .. code-block:: python
        
        tag = c4d.UVWTag(op.GetPointCount())
        op.InsertTag(tag)
        doc.AddUndo(c4d.UNDOTYPE_NEW, tag)
        c4d.EventAdd()
        
        :type type: int
        :param type: The undo type:
        
        .. include:: /consts/UNDOTYPE.rst
        :start-line: 3
        
        :type data: c4d.BaseList2D
        :param data: The object the undo has been added for.
        :type allowFromThread: bool
        :param allowFromThread:
        
        .. versionadded:: R14.014
        
        If an undo is added from a thread this is not executed. (As a safety measure, because normally this doesn't make any sense.)
        
        For explicit cases where a thread has to call :meth:`AddUndo` (the view redraw and everything else is blocked) this can be set to **True**.
        
        :rtype: bool
        :return: Success of adding the undo.
        
        
        """
        ...
    
    def GetUndoPtr(self) -> BaseList2D:
        """    
        Returns the element of the last undo action. E.g. if you have added a :class:`BaseObject <c4d.BaseObject>` undo you can retrieve the object by calling this method.
        
        .. note::
        
        Always be sure to check the type of the result first.
        
        :rtype: c4d.BaseList2D
        :return: The last undo element.
        
        
        """
        ...
    
    def FlushUndoBuffer(self) -> None:
        """    
        Flushes the complete undo + redo buffer.
        
        .. versionadded:: R14.014
        
        .. warning::
        
        Only call when absolutely needed.
        
        
        """
        ...
    
    def FindUndoPtr(self, bl: BaseList2D, type: int) -> BaseList2D:
        """    
        Returns the last undo state of the Cinema 4D element bl (object, tag, material, etc.) for the specified undo action type.
        
        .. versionadded:: R14.014
        
        Here is an how to retrieve the pre-undo object after a change has made
        
        .. code-block:: python
        
        preundo = doc.FindUndoPtr(obj, c4d.UNDOTYPE_CHANGE)
        
        .. note::
        
        Always check the type of the returned object.
        
        :type bl: c4d.BaseList2D
        :param bl: The element from which to obtain the last undo action.
        :type type: int
        :param type: The undo type to check:
        
        .. include:: /consts/UNDOTYPE.rst
        :start-line: 3
        
        :rtype: c4d.BaseList2D
        :return: The last undo element.
        
        
        """
        ...
    
    def DoRedo(self) -> bool:
        """    
        Perform a redo on this document (undo the last undo).
        
        :rtype: bool
        :return: Success of the operation.
        
        
        """
        ...
    
    def DoUndo(self, multiple: bool) -> bool:
        """    
        Perform an undo operation, same as the user selecting Undo from within Cinema 4D.
        
        :type multiple: bool
        :param multiple: This parameter only matters if this method is called between :meth:`AddUndo` and :meth:`EndUndo`. If *multiple* is **True** then all the :meth:`AddUndo` steps will be undone. Otherwise only the last :meth:`AddUndo` step will be undone. If :meth:`EndUndo` has been called then all steps are always undone.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def EndUndo(self) -> bool:
        """    
        End the building of multiple undo actions into a single user undo.
        
        .. note::
        
        This must be paired with :meth:`StartUndo`.
        
        :rtype: bool
        :return: Success of finishing the undo list.
        
        
        """
        ...
    
    def RecordKey(self, op: BaseList2D, id: DescID, time: BaseTime, undo: BaseList2D, autoKey: bool, eval_attribmanager: bool) -> bool:
        """    
        Records a key for *op* at *time*.
        
        .. versionadded:: R16.021
        
        :type op: c4d.BaseList2D
        :param op: The object to record.
        :type id: c4d.DescID
        :param id: The description ID to record.
        :type time: c4d.BaseTime
        :param time: The time to record.
        :type undo: c4d.BaseList2D
        :param undo:
        
        | The object in the old state.
        | This is necessary e.g. for autokeyframing so that Cinema 4D can compare values
        | Usually this is the object from the undo buffer.
        | To record keys (no autokeying) **None** can be passed.
        
        :type autoKey: bool
        :param autoKey: If **True** then autokeying is used and undo needs to be passed for comparison.
        :type eval_attribmanager: bool
        :param eval_attribmanager: Evaluate attributes manager.
        :rtype: bool
        :return: **True** if successful, otherwise *False*.
        
        
        """
        ...
    
    def AutoKey(self, op: BaseObject, undo: BaseList2D, recursive: bool, pos: bool, scale: bool, rot: bool, param: bool, pla: bool) -> None:
        """    
        Compares the object chain *op* to *undo* and sets keyframes for all the changes.
        
        .. versionadded:: R16.021
        
        :type op: c4d.BaseObject
        :param op: The object chain to add the keys to.
        :type undo: c4d.BaseList2D
        :param undo:  The object chain to compare to. This is necessary e.g. for autokeyframing so that Cinema 4D can compare values. Usually this is the object from the undo buffer.
        :type recursive: bool
        :param recursive: If **True** then the function applies to all children of *op* as well. The hierarchy of *op* and *undo* must match.
        :type pos: bool
        :param pos: If **True** keyframes are added for differences in position.
        :type scale: bool
        :param scale: If **True** keyframes are added for differences in scale.
        :type rot: bool
        :param rot: If **True** keyframes are added for differences in rotation.
        :type param: bool
        :param param: If **True** keyframes are added for differences in parameters.
        :type pla: bool
        :param pla: If **True** keyframes are added as PLA for differences in point positions.
        
        
        """
        ...
    
    def Record(self) -> None:
        """    
        Records the active objects in the document.
        
        .. versionadded:: R19
        
        
        """
        ...
    
    def AnimateObject(self, op: BaseList2D, time: BaseTime, flags: int) -> None:
        """    
        Animate a node in this document at the given time.
        
        .. note::
        
        Does not take expressions into account.
        
        :type op: c4d.BaseList2D
        :param op: This is the node to animate.
        :type time: c4d.BaseTime
        :param time: The time at which it is being animated.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/ANIMATEFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def Polygonize(self, keepanimation: bool) -> BaseDocument:
        """    
        Make a clone of the document and turn all objects into polygon based objects.
        
        :type keepanimation: bool
        :param keepanimation: Keep animation.
        :rtype: c4d.documents.BaseDocument
        :return: The cloned polygon based document or **None** if failed.
        
        
        """
        ...
    
    def SetMinTime(self, time: Any) -> None:
        """    
        Set the starting time for the timeline of this document.
        
        .. note::
        
        | For conversion of FPS or other time units, see :class:`BaseTime <c4d.BaseTime>`
        | You may also find the :meth:`GetFps` useful when using this method.
        
        :type type: c4d.BaseTime
        :param type: The time.
        
        
        """
        ...
    
    def SetMaxTime(self, time: Any) -> None:
        """    
        Set the end time of the timeline for this document.
        
        .. note::
        
        | For conversion of FPS or other time units, see :class:`BaseTime <c4d.BaseTime>`
        | You may also find the :meth:`GetFps` useful when using this method.
        
        :type type: c4d.BaseTime
        :param type: The time.
        
        
        """
        ...
    
    def GetMinTime(self) -> BaseTime:
        """    
        Get the starting time for the timeline of this document.
        
        .. note::
        
        | For conversion of FPS or other time units, see :class:`BaseTime <c4d.BaseTime>`
        | You may also find the :meth:`GetFps` useful when using this method.
        
        :rtype: c4d.BaseTime
        :return: The time.
        
        
        """
        ...
    
    def GetMaxTime(self) -> BaseTime:
        """    
        Get the end time for the timeline of this document.
        
        .. note::
        
        | For conversion of FPS or other time units, see :class:`BaseTime <c4d.BaseTime>`
        | You may also find the :meth:`GetFps` useful when using this method.
        
        :rtype: c4d.BaseTime
        :return: The time.
        
        
        """
        ...
    
    def GetTime(self) -> BaseTime:
        """    
        Returns the min time.
        
        :rtype: c4d.BaseTime
        :return: The current time.
        
        
        """
        ...
    
    def SetTime(self, time: Any) -> None:
        """    
        Set the current time for this documents timeline.
        
        .. note::
        
        This function only changes the document time, it does not start a redraw and/or animation/expressions.
        
        :type type: c4d.BaseTime
        :param type: The time.
        
        
        """
        ...
    
    def GetLoopMinTime(self) -> BaseTime:
        """    
        Returns the time of the left boundary of the document's preview range (loop range).
        
        :rtype: c4d.BaseTime
        :return: The time.
        
        
        """
        ...
    
    def SetLoopMinTime(self, time: Any) -> None:
        """    
        Sets the left boundary of the document's preview range (loop range) to the given time.
        
        :type type: c4d.BaseTime
        :param type: The time.
        
        
        """
        ...
    
    def GetLoopMaxTime(self) -> BaseTime:
        """    
        Returns the time of the right boundary of the document's preview range (loop range).
        
        :rtype: c4d.BaseTime
        :return: The time.
        
        
        """
        ...
    
    def SetLoopMaxTime(self, time: Any) -> None:
        """    
        Sets the right boundary of the document's preview range (loop range) to the given time.
        
        :type type: c4d.BaseTime
        :param type: The time.
        
        
        """
        ...
    
    def SetActiveObject(self, op: BaseObject, mode: int) -> None:
        """    
        Modifies the current multi selection with *op*, depending on *mode*.
        
        .. note::
        
        :meth:`BaseDocument.GetActiveObject` Should be called afterward to update the internal selection state.
        
        :type op: c4d.BaseObject
        :param op: The object.
        :type mode: int
        :param mode: The selection flag:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetActiveTag(self, tag: BaseTag, mode: int) -> None:
        """    
        Sets a tag be the currently active one.
        
        .. note::
        
        :meth:`BaseDocument.GetActiveTag` Should be called afterward to update the internal selection state.
        
        :type tag: c4d.BaseTag
        :param tag: The tag to set active.
        :type mode: int
        :param mode: The selection flag:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetActiveMaterial(self, mp: BaseMaterial, mode: int) -> None:
        """    
        Modifies the current multi selection with *op*, depending on *mode*.
        
        .. note::
        
        :meth:`BaseDocument.GetActiveMaterial` Should be called afterward to update the internal selection state.
        
        :type mp: c4d.BaseMaterial
        :param mp: The material to set active.
        :type mode: int
        :param mode: The selection flag:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetActiveRenderData(self, rd: RenderData) -> None:
        """    
        Sets the active render settings for the document, these are the settings that are used for rendering.
        
        :type rd: c4d.documents.RenderData
        :param rd: The render data that you want to make active.
        
        
        """
        ...
    
    def GetAllTextures(self, isNet: bool, ar: List[C4DAtom]) -> BaseContainer:
        """    
        Returns a collection of all used textures in the document and optionally only for the objects in *ar*.
        
        .. note::
        
        | If *isNet* is passed **True** (default) then the function only delivers the textures of the current take.
        | Set the parameter to **False** to get all.
        
        :type isNet: bool
        :param isNet:
        
        .. versionadded:: R16.021
        
        Pass **True** (default) to retrieve the textures used in the current NET rendering.
        
        :type ar: List[c4d.C4DAtom]
        :param ar: An atom array to get the textures for. If **None** (default), all used textures in the document will be returned.
        :rtype: c4d.BaseContainer
        :return: A container with all filenames of used textures in the document.
        
        
        """
        ...
    
    def SetAction(self, a: int) -> None:
        """    
        Set the current tool in the editor.
        
        :type a: int
        :param a: The values are *ID_MODELING_MOVE*, *ID_MODELING_SCALE*, *ID_MODELING_ROTATE* etc. The IDs are listed in *modelingids.h*.
        
        
        """
        ...
    
    def GetAction(self) -> int:
        """    
        Get the ID of the current active tool in the editor.
        
        :rtype: int
        :return: The ID.
        
        
        """
        ...
    
    def GetActiveToolData(self) -> BaseContainer:
        """    
        Gets the original tool data container.
        
        .. note::
        
        The container is alive until the host object is freed.
        
        :rtype: c4d.BaseContainer
        :return:  Tool data container.
        
        
        """
        ...
    
    def SetMode(self, m: int) -> None:
        """    
        Set the main mode of the editor.
        
        :type m: int
        :param m: The value:
        
        .. include:: /consts/MEditorModes.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMode(self) -> int:
        """    
        Get the main mode of the editor.
        
        :rtype: int
        :return: The value:
        
        .. include:: /consts/MEditorModes.rst
        :start-line: 3
        
        
        """
        ...
    
    def IsEditMode(self) -> bool:
        """    
        Check if the editor is in an editable mode.
        
        .. note::
        
        This checks if :meth:`GetMode` is *Mpoints*, *Medges* or *Mpolygons*.
        
        :rtype: bool
        :return: **True** if the editor is in point/poly editing mode.
        
        
        """
        ...
    
    def GetBaseDraw(self, bd: int) -> BaseDraw:
        """    
        Returns the BaseDraw hook of the editor *bd*.
        
        :type bd: int
        :param bd: If there are multiple views (multiple basedraws), this selects the view.
        :rtype: c4d.BaseDraw
        :return: The requested view in the editor, or **None**
        
        
        """
        ...
    
    def GetActiveBaseDraw(self) -> BaseDraw:
        """    
        Get the activate BaseDraw in the editor, this is where all drawing should be performed.
        
        :rtype: c4d.BaseDraw
        :return: The active view in the editor.
        
        
        """
        ...
    
    def GetRenderBaseDraw(self) -> BaseDraw:
        """    
        This is the BaseDraw belonging to the view that the user has chosen as 'Render View' (see View menu in Cinema 4D).
        
        :rtype: c4d.BaseDraw
        :return: The render view in the editor.
        
        
        """
        ...
    
    def GetActiveTag(self) -> BaseTag:
        """    
        Returns the active selected tag.
        
        :rtype: c4d.BaseTag
        :return: The active tag, or **None**.
        
        
        """
        ...
    
    def GetMaterials(self) -> List[BaseMaterial]:
        """    
        Returns all materials in a list.
        
        :rtype: List[c4d.BaseMaterial]
        :return: The list of all materials.
        
        
        """
        ...
    
    def GetActiveObject(self) -> BaseObject:
        """    
        Returns the active selected object.
        
        :rtype: c4d.BaseObject
        :return: The active object, or **None**.
        
        
        """
        ...
    
    def GetActiveRenderData(self) -> RenderData:
        """    
        Returns the active selected render data.
        
        :rtype: c4d.documents.RenderData
        :return: The active render data.
        
        .. note::
        
        Guaranteed to never be **None**.
        
        
        """
        ...
    
    def GetFirstRenderData(self) -> RenderData:
        """    
        Gets the first render data or options of the document.
        
        .. note::
        
        The other render settings in the document can be accessed by using the list functions :meth:`GetNext() <GeListNode.GetNext>`, :meth:`GetPred() <GeListNode.GetPred>`, :meth:`GetDown() <GeListNode.GetDown>` and :meth:`GetUp() <GeListNode.GetUp>`.
        
        :rtype: c4d.documents.RenderData
        :return: The first render data of the document, or **None** if there are no render data associated with the document.
        
        
        """
        ...
    
    def InsertRenderData(self, rd: RenderData, parent: Optional[RenderData] = ..., pred: Optional[RenderData] = ...) -> None:
        """    
        | Inserts the render data into the document's render settings hierarchy.
        | Optionally the insertion position can either be specified by the *parent* parameter, inserting the render data as the first child of the specified *parent*, or by the *pred* parameter, inserting the render data below the specified *pred* render data.
        | If neither is given, the render data is inserted at the top of the hierarchy.
        
        :type rd: c4d.documents.RenderData
        :param rd: The render data to insert.
        :type parent: c4d.documents.RenderData
        :param parent: An optional parent to insert the render data as a child of.
        :type pred: c4d.documents.RenderData
        :param pred: An optional render data of the document to use as insertion point.
        
        
        """
        ...
    
    def InsertRenderDataLast(self, rd: RenderData) -> None:
        """    
        Inserts the render data as last child into the document's render data list.
        
        :type rd: c4d.documents.RenderData
        :param rd: The render data to insert.
        
        
        """
        ...
    
    def GetActiveMaterial(self) -> BaseMaterial:
        """    
        Returns the active selected material.
        
        :rtype: c4d.BaseMaterial
        :return: The active material, or **None**.
        
        
        """
        ...
    
    def GetData(self, type: int) -> BaseContainer:
        """    
        .. deprecated:: R16 :meth:`GetDocumentData()` should be used instead.
        
        Get the :class:`BaseContainer <c4d.BaseContainer>` settings of the specified *type*.
        
        :type type: int
        :param type: The **DOCUMENTSETTINGS** type of the settings to get. See :doc:`/consts/DOCUMENTSETTINGS`.
        :rtype: c4d.BaseContainer
        :return: The settings for the document.
        
        
        """
        ...
    
    def GetDocumentData(self, type: int) -> BaseContainer:
        """    
        Get the :class:`BaseContainer <c4d.BaseContainer>` settings of the specified *type*.
        
        .. versionadded:: R16.021
        
        .. warning::
        
        | Use :meth:`GetSettingsInstance` to retrieve **DOCUMENTSETTINGS_TOOLS**.
        | :meth:`GetDocumentData` does not return these settings.
        
        :type type: int
        :param type: The **DOCUMENTSETTINGS** type of the settings to get. See :doc:`/consts/DOCUMENTSETTINGS`.
        :rtype: c4d.BaseContainer
        :return: The settings for the document.
        
        
        """
        ...
    
    def SetDocumentData(self, type: int, bc: BaseContainer) -> None:
        """    
        Merges the :class:`BaseContainer <c4d.BaseContainer>` for the settings of the specified *type*.
        
        .. versionadded:: R16.021
        
        .. warning::
        
        | Use :meth:`GetSettingsInstance` to change **DOCUMENTSETTINGS_TOOLS**.
        | :meth:`SetDocumentData` does not affect these settings.
        
        :type type: int
        :param type: The **DOCUMENTSETTINGS** type of the settings to merge for the document. See :doc:`/consts/DOCUMENTSETTINGS`.
        :type bc: c4d.BaseContainer
        :param bc: The container to take the new settings from.
        
        
        """
        ...
    
    def GetSettingsInstance(self, type: int) -> BaseContainer:
        """    
        Returns the internal settings object.
        
        .. note::
        
        Changes to the returned container are reflected in the document so it is not needed to call :meth:`SetDocumentData` manually.
        
        .. warning::
        
        | Use :meth:`GetDocumentData`/:meth:`SetDocumentData` to retrieve/change **DOCUMENTSETTINGS_GENERAL**.
        | :meth:`GetSettingsInstance` does not return these settings.
        
        :type type: int
        :param type: The **DOCUMENTSETTINGS** type of the settings to get. See :doc:`/consts/DOCUMENTSETTINGS`.
        :rtype: c4d.BaseContainer
        :return: The settings for the document.
        
        
        """
        ...
    
    def GetFirstObject(self) -> BaseObject:
        """    
        Returns the first object.
        
        :rtype: c4d.BaseObject
        :return: The first object, or **None** if no objects are contained in this document.
        
        
        """
        ...
    
    def GetFirstMaterial(self) -> BaseMaterial:
        """    
        Returns the first material.
        
        :rtype: c4d.BaseMaterial
        :return: The active material, or **None**.
        
        
        """
        ...
    
    def GetActiveMaterials(self) -> List[BaseMaterial]:
        """    
        Returns the material selection.
        
        :rtype: List[c4d.BaseMaterial]
        :return: The selected materials in a list.
        
        
        """
        ...
    
    def GetOrderedActiveObjects(self) -> List[BaseList2D]:
        """    
        .. deprecated:: R13.051
        
        Use :meth:`GetActiveObjects` with the corresponding flag instead.
        
        Returns the objects in an ordered list.
        
        :rtype: List[c4d.BaseList2D]
        :return: The oredered list.
        
        
        """
        ...
    
    def GetActiveObjects(self, flags: int) -> List[BaseList2D]:
        """    
        Returns the object selection.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/GETACTIVEOBJECTFLAGS.rst
        :start-line: 3
        
        :rtype: List[c4d.BaseList2D]
        :return: The selected objects in a list.
        
        
        """
        ...
    
    def GetActiveTags(self) -> List[BaseTag]:
        """    
        Returns the tag selection.
        
        :rtype: List[c4d.BaseTag]
        :return: The selected tags in a list.
        
        
        """
        ...
    
    def GetSelection(self) -> List[BaseList2D]:
        """    
        Returns the selection of materials, tags and objects in a list.
        
        :rtype: List[c4d.BaseList2D]
        :return: The selected objects in a list.
        
        
        """
        ...
    
    def GetActiveObjectsFilter(self, children: bool, type: int, instanceof: int) -> List[BaseList2D]:
        """    
        Returns the active object multi selection and removes objects that do not match the filter given by type and instanceof.
        
        :type children: bool
        :param children: If **True** then children are also added to selection, provided that they are selected. Otherwise only the topmost parent in each chain is added.
        :type type: int
        :param type: Checked against :meth:`C4DAtom.GetType`. Pass *NOTOK* to ignore this test.
        :type instanceof: int
        :param instanceof: Checked against :meth:`C4DAtom.IsInstanceOf`. Pass *NOTOK* to ignore this test.
        :rtype: List[c4d.BaseList2D]
        :return: The selected objects in a list.
        
        
        """
        ...
    
    def GetRealActiveObject(self, help: Iterable[BaseObject]) -> Tuple[BaseObject, bool]:
        """    
        Returns the active object or the dummy axis if multiple objects are selected.
        
        .. versionadded:: R19
        
        :type help: Iterable[c4d.BaseObject]
        :param help: Can be set to **None** or for speedup purposes pass a list/tuple of active objects.
        :rtype: Tuple[c4d.BaseObject, bool]
        :return: A tuple with the real active object and a bool telling if multiple objects are selected. **None** if the method failed.
        
        
        """
        ...
    
    def GetObjects(self) -> List[BaseObject]:
        """    
        Returns the highest objects without children.
        
        :rtype: List[c4d.BaseObject]
        :return: The objects.
        
        
        """
        ...
    
    def SetSelection(self, bl: BaseList2D, mode: int) -> None:
        """    
        | Sets the active selection.
        | This function deals with both objects, tags and materials.
        
        :type bl: c4d.BaseList2D
        :param bl: The baselist object within this document that you want to make active. Must be in the document already.
        :type mode: int
        :param mode: The selection mode:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def SearchMaterial(self, name: str) -> BaseMaterial:
        """    
        Search for a material with the same case sensitive name.
        
        :type name: str
        :param name: The name of the material to search for.
        :rtype: c4d.BaseMaterial
        :return: The material or **None** if nothing was found.
        
        
        """
        ...
    
    def SearchObject(self, name: str) -> BaseObject:
        """    
        Search for an object with the same case sensitive name.
        
        :type name: str
        :param name: The name of the object to search for.
        :rtype: c4d.BaseObject
        :return: The object or **None** if nothing was found.
        
        
        """
        ...
    
    def GetHighest(self, type: int, editor: bool) -> BaseObject:
        """    
        | The first object in object manager hierarchy of type *type*.
        | It searches objects that are not deactivated in the object manager (set to red).
        
        :type type: int
        :param type: the object type
        :type editor: bool
        :param editor: **True** will search using the 'editor dot' in the Object Manager, **False** will use the 'render dot'.
        :rtype: c4d.BaseObject
        :return: The first requested object or **None** if nothing was found.
        
        
        """
        ...
    
    def InsertObject(self, op: Optional[BaseObject] = ..., parent: Optional[BaseObject] = ..., pred: Optional[BaseObject] = ..., checknames: Optional[bool] = ...) -> None:
        """    
        | Inserts the object into the document's object hierarchy.
        | The insertion position can either be specified by the parent parameter, inserting the object as the first child of the specified parent, or by the *pred* parameter, inserting the object below the specified
        *prev* object.
        | If neither is given, the object is inserted at the top of the hierarchy.
        
        .. note ::
        
        If both *pred* and *parent* are provided then pred has precedence.
        
        :raise ReferenceError: If the passed objects (*parent* and *pred*) are not in the same document.
        :type op: Optional[c4d.BaseObject]
        :param op: Object to insert into the document.
        :type parent: Optional[c4d.BaseObject]
        :param parent: Optional parent to insert the object as a child of.
        :type pred: Optional[c4d.BaseObject]
        :param pred: Optional insertion point.
        :type checknames: bool
        :param checknames: Check for duplicate names and append .1, .2 etc.
        
        
        """
        ...
    
    def InsertMaterial(self, op: BaseMaterial, pred: Optional[BaseObject] = ..., checknames: Optional[bool] = ...) -> None:
        """    
        | Inserts the material into the document's material list.
        | Optionally you can specify the insertion position with the pred parameter, giving the material before (just to the left of) the wanted position.
        | Otherwise the material is inserted at the first position in the list.
        
        :type op: c4d.BaseMaterial
        :param op: Material to insert into the document.
        :type pred: Optional[c4d.BaseObject]
        :param pred:
        
        Optional insertion point for the material.
        
        .. note::
        
        | Require condition *pred.GetDocument()==op.GetDocument()==op*.
        | That means, the object has to be in the same document.
        
        :type checknames: bool
        :param checknames: Check for duplicate names and append .1, .2 etc.
        
        
        """
        ...
    
    def GetHelperAxis(self) -> BaseObject:
        """    
        Get the helper axis for the current multi selection.
        
        :rtype: c4d.BaseObject
        :return: The axis object.
        
        
        """
        ...
    
    def GetChanged(self) -> bool:
        """    
        Checks if the document has been changed since it was last saved.
        
        :rtype: bool
        :return: **True** if the document has been changed.
        
        
        """
        ...
    
    def SetChanged(self) -> None:
        """    
        Set the changed state of the document to reflect it has been modified.
        
        
        """
        ...
    
    def IsAxisEnabled(self) -> bool:
        """    
        Returns the state of the object axis modifier.
        
        .. versionadded:: R14.014
        
        .. note::
        
        `c4d.CallCommand(12102)` toggles the tool.
        
        :rtype: bool
        :return: **True** if the object axis modifier is enabled, otherwise **False**.
        
        
        """
        ...
    
    def SendInfo(self, type: int, format: int, fn: str, bl: BaseList2D, hooks_only: bool) -> None:
        """    
        Sends *MSG_DOCUMENTINFO* messages.
        
        .. versionadded:: R14.014
        
        :type type: int
        :param type: The message type:
        
        .. include:: /consts/MSG_DOCUMENTINFO_TYPE.rst
        :start-line: 3
        
        :type format: int
        :param format: The file format: (Set for load, merge and before/after save only. Otherwise *NOTOK*.)
        
        .. include:: /consts/FORMAT_export.rst
        :start-line: 3
        
        :type fn: str
        :param fn: The document filename.
        
        .. note:: This is not always the same as :meth:`GetDocumentPath`. E.g. for *MSG_DOCUMENTINFO_TYPE_SAVE_BEFORE* :meth:`GetDocumentPath` still contains the old path whereas *fn* designates the real file.
        
        :type bl: c4d.BaseList2D
        :param bl: The object/tag/material that got inserted. It is used if type is of one of the following types:
        
        | *MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT*
        | *MSG_DOCUMENTINFO_TYPE_TAG_INSERT*
        | *MSG_DOCUMENTINFO_TYPE_MATERIAL_INSERT*
        
        :type hooks_only: bool
        :param hooks_only: If **True** send only to scene hooks.
        
        
        """
        ...
    
    def GetDocPreviewBitmap(self) -> BaseBitmap:
        """    
        Get the preview bitmap of the document.
        
        .. versionadded:: R15.037
        
        :rtype: c4d.bitmaps.BaseBitmap
        :return: The preview bitmap of the document, or **None** if it could not be retrieved.
        
        
        """
        ...
    
    def GetTakeData(self) -> TakeData:
        """    
        Gets the take data for the document.
        
        .. versionadded:: R17.032
        
        :rtype: c4d.modules.takesystem.TakeData
        :return: The take data.
        
        
        """
        ...
    
    def GetTargetObject(self) -> BaseObject:
        """    
        Gets the target object within a multi-selection.
        
        .. versionadded:: R17.048
        
        .. note::
        
        | This is the last object selected and is used by commands such as Spline Boolean in order to allow the user to control which object will be used as the target for the command.
        | The target object displays in the Object Manager as highlighted.
        
        :rtype: c4d.BaseObject
        :return: The target object, or **None** if it fails or there is no selection.
        
        
        """
        ...
    
    def SetTargetObject(self, op: BaseObject) -> None:
        """    
        Sets the target object within a multi-selection.
        
        .. versionadded:: R17.048
        
        .. note::
        
        | This is the last object selected and is used by commands such as Spline Boolean in order to allow the user to control which object will be used as the target for the command.
        | The target object displays in the Object Manager as highlighted.
        
        :type op: c4d.BaseObject
        :param op: The object to set as the target.
        
        
        """
        ...
    
    def GetDefaultKey(self) -> Tuple[CKey, bool]:
        """    
        Retrieves the document's default keying settings.
        
        .. versionadded:: R19
        
        :rtype: Tuple[c4d.CKey, bool]
        :return:
        
        | A tuple containing a key with the document's default settings and a bool giving the document's default overdub state.
        | **None** if the function failed.
        
        
        """
        ...
    
    def SetDefaultKey(self, key: CKey, overdub: bool) -> None:
        """    
        Sets the document's default keying settings.
        
        .. versionadded:: R19
        
        :type key: c4d.CKey
        :param key: The key to set the new default document's settings.
        :type overdub: bool
        :param overdub:
        
        | The new document's default overdub.
        | If a keyframe already exists, the existing keyframe's interpolation type will be maintained when a new keyframe is recorded (only the value key will be overwritten).
        
        
        """
        ...
    
    def GetPickSession(self) -> Tuple[List[C4DAtom], bool]:
        """    
        Returns information about the current pick session.
        
        .. versionadded:: R19
        
        :rtype: Tuple[List[c4d.C4DAtom], bool]
        :return:
        
        | A tuple with the list of picked objects and the multi-pick state.
        | **None** if there is no active pick session.
        
        
        """
        ...
    
    def StartPickSession(self, callback: Callable[..., Any], multi: bool) -> None:
        """    
        Starts a pick session.
        
        .. versionadded:: R19
        
        :type callback: function(*active*, *multi*)
        :param callback:
        
        The pick session callback. The function does not need to return a value. The passed arguments are:
        
        | *active*: `list` of :class:`c4d.BaseObject`: The list of picked objects.
        | *multi*: `bool`: The multi-pick state.
        
        :type multi: bool
        :param multi: Pass **True** for multi-pick sessions. Usually a pick session ends when something is selected. With a multi-pick session it ends when the user terminates it (ESC key or double-click).
        
        
        """
        ...
    
    def StopPickSession(self, cancel: bool) -> None:
        """    
        | Ends the pick session.
        | For instance after filling the pick session array.
        
        .. versionadded:: R19
        
        :type cancel: bool
        :param cancel: Pass **True** to cancel a pick session, for instance if an error occurred. Pass **False** if the pick session is ended regularly.
        
        
        """
        ...
    


def GetRecentDocumentsList(isBodyPaint: bool) -> None:
    """    
    Retrieves the recent documents list.
    
    .. versionadded:: R21
    
    :param isBodyPaint: **True** to retrieve BodyPaint's list.
    :type isBodyPaint: bool
    :rtype: :class:`maxon.BaseArray` (:class:`maxon.Url`)
    :return: The recent documents list.
    
    
    """
    ...

def GetActiveDocument() -> BaseDocument:
    """    
    Returns the active document of Cinema 4D.
    
    :rtype: c4d.documents.BaseDocument
    :return: The active document.
    
    
    """
    ...

def GetFirstDocument() -> BaseDocument:
    """    
    Returns the first document in the list of documents within Cinema 4D.
    
    :rtype: c4d.documents.BaseDocument
    :return: The first document.
    
    
    """
    ...

def SetActiveDocument(doc: BaseDocument) -> None:
    """    
    Sets *doc* as active document in Cinema 4D.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    
    
    """
    ...

def SaveDocument(doc: BaseDocument, name: Union[str, MemoryFileStruct], saveflags: int, format: int) -> bool:
    """    
    Saves the document to a file.
    
    .. seealso::
    
    The :maxongithub:`script <scripts/03_application_development/files_media/export_alembic_r14.py>` that shows how to effectively access and change the settings of an importer/exporter.
    
    .. seealso::
    
    Warning note in :meth:`SceneSaverData.Save`.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: Command ID
    :type name: Union[str, c4d.storage.MemoryFileStruct]
    :param name: File to save the document to.
    :type saveflags: int
    :param saveflags: The flags
    
    .. include:: /consts/SAVEDOCUMENTFLAGS.rst
    :start-line: 3
    
    :type format: int
    :param format: The file format to save the document as.
    
    .. include:: /consts/FORMAT_export.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def RenderDocument(doc: BaseDocument, rdata: BaseContainer, bmp: BaseBitmap, renderflags: int, th: BaseThread, prog: Callable[..., Any], wprog: Callable[..., Any]) -> int:
    """    
    Renders the document to a bitmap. You need to initialize the image with the size of the render data
    
    .. note::
    
    A :class:`MultipassBitmap <c4d.bitmaps.MultipassBitmap>` must be passed to render the image with an alpha channel.
    
    .. literalinclude:: /../../doc.python.github/scripts/04_3d_concepts/rendering/render_with_progress_hook_r21.py
    :language: python
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document you want to render.
    :type rdata: c4d.BaseContainer
    :param rdata: The render data.
    :type bmp: c4d.bitmaps.BaseBitmap
    :param bmp: The bitmap where the rendered picture will be saved in. Initialize the image with the size of the render data.
    :type renderflags: int
    :param renderflags: Some renderflags.
    
    .. include:: /consts/RENDERFLAGS.rst
    :start-line: 3
    
    .. note::
    
    If you are in a safe context you might use *RENDERFLAG_NODOCUMENTCLONE* to speed up the render process especially on big scenes.
    
    :type th: c4d.threading.BaseThread
    :param th: The thread to test for a break or **None**.
    :type prog: function
    :param prog:
    
    .. versionadded:: R21
    
    A function that will be called during the rendering with information about the current progress.
    
    The expected function signature is `functionName(p, progress_type)` and parameters correspond to:
    
    - p (float): The progress, between 0.0 and 1.0.
    - progress_type: The render Progress type:
    
    .. include:: /consts/RENDERPROGRESSTYPE.rst
    :start-line: 3
    
    :type wprog: function
    :param wprog:
    
    .. versionadded:: R21
    
    The write progress hook for the render operation.
    
    The expected function signature is `functionName(mode, bmp, fn, mainImage, frame, renderTime, streamnum, streamname)` and parameters correspond to:
    
    - mode: the write mode type:
    
    .. include:: /consts/WRITEMODE.rst
    :start-line: 5
    
    - bmp (:class:`c4d.bitmaps.BaseBitmap`): The bitmap written to. Can be **None**.
    - fn (str): The filename where the file is going to be written to.
    - mainImage (bool): **True** for main image, otherwise **False**.
    - frame (int): The frame number.
    - renderTime (int): The bitmap frame time.
    - streamnum (int): The stream number.
    - streamname (str): The stream name.
    
    :rtype: int
    :return: The result:
    
    .. include:: /consts/RENDERRESULT.rst
    :start-line: 5
    
    
    """
    ...

def MergeDocument(doc: BaseDocument, name: Union[str, MemoryFileStruct], loadflags: int, thread: BaseThread) -> bool:
    """    
    Merges the file *name* into the document *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to merge the loaded document *name* into.
    :type name: Union[str, c4d.storage.MemoryFileStruct]
    :param name: The file to merge into *doc*.
    :type loadflags: int
    :param loadflags: The scene filter flags for the loader:
    
    .. include:: /consts/SCENEFILTER.rst
    :start-line: 3
    
    :type thread: c4d.threading.BaseThread
    :param thread: The current thread, or **None** for the main Cinema 4D thread.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def LoadFile(name: str) -> None:
    """    
    Loads a file into Cinema 4D and opens it.
    
    .. _LoadFile-note:
    
    .. note::
    
    This function can be used to open any kind of file Cinema 4D handles i.e. a document, an image, a layout or a lib4d/cat4d file.
    
    :type name: str
    :param name: The file to load.
    
    
    """
    ...

def KillDocument(doc: BaseDocument) -> None:
    """    
    Removes and free all resources of this document.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to free.
    
    
    """
    ...

def InsertBaseDocument(doc: BaseDocument) -> None:
    """    
    Inserts a document into the Cinema 4D editor list of documents.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to insert.
    
    
    """
    ...

def LoadDocument(name: Union[str, MemoryFileStruct], loadflags: int, thread: Optional[BaseThread] = ...) -> BaseDocument:
    """    
    Similar to :func:`LoadFile` but this time the document is not put into the editors list of documents and it gives control over the loaded document.
    
    :type name: Union[str, c4d.storage.MemoryFileStruct]
    :param name: The name of the file to load the document from.
    :type loadflags: int
    :param loadflags: The scene filter flags for the loader:
    
    .. include:: /consts/SCENEFILTER.rst
    :start-line: 3
    
    :type thread: c4d.threading.BaseThread
    :param thread: The current thread, or **None** for the main Cinema 4D thread.
    :rtype: c4d.documents.BaseDocument
    :return: The document that was loaded, or **None** if it failed.
    
    
    """
    ...

def CloseAllDocuments() -> bool:
    """    
    Closes all open documents in Cinema 4D.
    
    :rtype: bool
    :return: **True** on success, otherwise **False**
    
    
    """
    ...

def SetDocumentTime(doc: BaseDocument, time: BaseTime) -> bool:
    """    
    Controls the time of the active document doc.
    
    .. note::
    
    Unlike :meth:`BaseDocument.SetTime` it handles running animation.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to control.
    :type time: c4d.BaseTime
    :param time: The time to set.
    :rtype: bool
    :return: **True** on success, otherwise **False**
    
    
    """
    ...

def RunAnimation(doc: BaseDocument, stop: bool, forward: bool) -> bool:
    """    
    Controls the animation in the active document *doc*.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to control. Usually :func:`GetActiveDocument() <c4d.documents.GetActiveDocument>`
    :type stop: bool
    :param stop: If this is **True** the animation is stopped, otherwise it is running.
    :type forward: bool
    :param forward: If this is **True** the direction is set to forward, otherwise it is set to backward.
    :rtype: bool
    :return: **True** on success, otherwise **False**
    
    
    """
    ...

def InteractiveModeling_Restart(doc: BaseDocument) -> bool:
    """    
    | Used for modeling tools with GUI input.
    | Applies the last modeling undo so that new values of the modeling tool can be applied.
    
    An example from the edge cut code.
    
    .. code-block:: python
    
    import c4d
    
    class TestTool(c4d.plugins.ToolData):
    
    def MouseInput(self, doc, data, draw, win, msg):
    if not doc: return False
    
    if doc.GetMode() == c4d.Medges:
    active = p.GetActiveObjects(True)
    
    #undo step before
    c4d.documents.InteractiveModeling_Restart(doc)
    
    self.ModelingEdgeCut(active, c4d.MODIFY_EDGESELECTION, data, doc, win, msg, True)
    c4d.EventAdd()
    
    return True
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def IsolateObjects(doc: BaseDocument, t_objects: List[BaseObject]) -> BaseDocument:
    """    
    A helper routine to copy the objects *t_objects* of document *doc* to a new document (returned).
    
    .. note::
    
    All materials associated are also copied over and the links are corrected.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document that contains the objects in *t_objects*.
    :type t_objects: List[c4d.BaseObject]
    :param t_objects: The objects to isolate.
    :rtype: c4d.documents.BaseDocument
    :return: The document containing the isolated objects.
    
    
    """
    ...

def StopExternalRenderer() -> bool:
    """    
    Stop the external renderer.
    
    :rtype: bool
    :return: **True** if the rendering has been canceled, otherwise **False**.
    
    
    """
    ...

def GetBatchRender() -> BatchRender:
    """    
    Get the batch render instance.
    
    :rtype: c4d.documents.BatchRender
    :return: The batch render.
    
    
    """
    ...

def GetAllAssets(doc: BaseDocument, allowDialogs: bool, lastPath: str, flags: int) -> List[Dict[str, Any]]:
    """    
    | Get all assets from a document.
    | It is e.g. used by `"Save Project with Assets"` menu and :func:`SaveProject`.
    
    .. versionadded:: R15.057
    
    .. deprecated:: S22
    
    Use :func:`c4d.GetAllAssetsNew`.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to save as project.
    :type allowDialogs: bool
    :param allowDialogs: If **True** the function can open dialogs. For example a file select dialog is opened if a node of the scene points to a file which does not exist anymore.
    :type lastPath: str
    :param lastPath:
    
    | Pass an empty string, that will be filled with the last path used.
    | If a file dialog is opened and the user selects the missing file on the harddisk, the folder of this asset is assigned to *lastPath*.
    | The developer can store this value somewhere and pass it next time so Cinema 4D knows where to look first before asking the user again.
    
    :type flags: int
    :param flags:
    
    .. versionadded:: R20
    The flags to decide which assets should be collected:
    
    .. include:: /consts/ASSETDATA_FLAG.rst
    :start-line: 3
    
    :rtype: List[Dict]
    :return: The assets in the document, or **None** if there was an error.
    
    The dictionary for each returned asset is:
    
    - `filename`: str: The asset filename.
    - `assetname`: str: The asset name.
    - `channelId`: int: The asset channel ID.
    - `netRequestOnDemand`: bool: NET request on demand.
    - `owner`: :class:`c4d.BaseList2D`: The owner object. Since R20.
    - `exists`: bool: Tells if the asset could be found. Since R20.
    - `paramId`: int: The parameter ID. Since R20.
    - `nodePath`: str: The node path of the port the asset is assigned to in case of a nimbus material. Since R20.
    - `nodeSpace`: str: The node space id in case of a nimbus material. Since R21.
    
    
    """
    ...

def GetAllAssetsNew(doc: BaseDocument, allowDialogs: bool, lastPath: str, flags: int, assetList: List[Dict[str, Any]]) -> int:
    """    
    | Get all assets from a document.
    | It is e.g. used by `"Save Project with Assets"` menu and :func:`SaveProject`.
    
    .. versionadded:: S22
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to get the assets from.
    :type allowDialogs: bool
    :param allowDialogs: If **True** the function can open dialogs. For example a file select dialog is opened if a node of the scene points to a file which does not exist anymore.
    :type lastPath: str
    :param lastPath:
    
    | Pass an empty string, that will be filled with the last path used.
    | If a file dialog is opened and the user selects the missing file on the harddisk, the folder of this asset is assigned to *lastPath*.
    | The developer can store this value somewhere and pass it next time so Cinema 4D knows where to look first before asking the user again.
    
    :type flags: int
    :param flags:
    
    The flags to decide which assets should be collected:
    
    .. include:: /consts/ASSETDATA_FLAG.rst
    :start-line: 3
    
    :type assetList: List[Dict]
    :param assetList: A list filled with assets in the document.
    
    The dictionary for each returned asset is:
    
    - `filename`: str: The asset filename.
    - `assetname`: str: The asset name.
    - `channelId`: int: The asset channel ID.
    - `netRequestOnDemand`: bool: NET request on demand.
    - `owner`: :class:`c4d.BaseList2D`: The owner object. Since R20.
    - `exists`: bool: Tells if the asset could be found. Since R20.
    - `paramId`: int: The parameter ID. Since R20.
    - `nodePath`: str: The node path of the port the asset is assigned to in case of a nimbus material. Since R20.
    - `nodeSpace`: str: The node space id in case of a nimbus material. Since R21.
    :rtype: int
    :return: The success state.
    
    .. include:: /consts/GETALLASSETSRESULT.rst
    :start-line: 3
    
    
    """
    ...

def SaveProject(doc: BaseDocument, flags: int, targetPath: str, assets: Any, missingAssets: Any) -> bool:
    """    
    Save the document as a project (menu `"Save Project with Assets"`).
    
    .. versionadded:: R15.057
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document to save as project.
    :type flags: int
    :param flags: Flags:
    
    .. include:: /consts/SAVEPROJECT.rst
    :start-line: 3
    
    :type targetPath: str
    :param targetPath: The path to save the project to.
    :type assets: list of dict{**filename**: str, **assetname**: str, **channelId**: int, **netRequestOnDemand**: bool}
    :param assets: Pass an empty list that will be filled with the found assets.
    :type missingAssets: list of dict{**filename**: str, **assetname**: str, **channelId**: int, **netRequestOnDemand**: bool}
    :param missingAssets: Pass an empty list that will be filled with the missing assets.
    :rtype: bool
    :return: **True** if the document was successfully saved as a project, otherwise **False**.
    
    .. code-block:: python
    
    missingAssets = []
    assets = []
    targetPath = "some path"
    res = c4d.documents.SaveProject(doc, c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE, targetPath, assets, missingAssets)
    
    
    """
    ...

def GetFirstMarker(doc: BaseDocument) -> BaseList2D:
    """    
    Returns the first timeline marker of the document.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :rtype: c4d.BaseList2D
    :return: The first timeline marker.
    
    
    """
    ...

def AddMarker(doc: BaseDocument, pPred: Optional[BaseList2D] = ..., time: Optional[BaseTime] = ..., name: Optional[str] = ...) -> BaseList2D:
    """    
    Inserts a timeline marker into the document at a given time. Optionally an insertion point *pPred* in the timeline marker list can be specified, giving the marker before the wanted insertion point.
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document in which to insert.
    :type pPred: c4d.BaseList2D
    :param pPred: The optional timeline marker to use as list insertion point.
    :type time: c4d.BaseTime
    :param time: The time position of the timeline marker.
    :type name: str
    :param name: The name of the timeline marker.
    :rtype: c4d.BaseList2D
    :return: The added timeline marker, or **None** if insertion failed.
    
    
    """
    ...

