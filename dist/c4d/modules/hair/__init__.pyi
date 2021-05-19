from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import Vector, BaseSelect, Matrix, SplineObject, BaseTag, BaseObject
from c4d.documents import BaseDocument
from c4d.threading import BaseThread


class HairVertexMapTag(BaseTag):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.hair.HairVertexMapTag
        :return: A new hair vertex map tag.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Gets the number of points.
        
        :rtype: int
        :return: Point count.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Gets the tangent count.
        
        :rtype: int
        :return: Tangent count.
        
        
        """
        ...
    
    def GetSegments(self) -> int:
        """    
        Gets the segment count.
        
        :rtype: int
        :return: Segment count.
        
        
        """
        ...
    

class HairTangentTag(BaseTag):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.hair.HairTangentTag
        :return: A new hair tangent tag.
        
        
        """
        ...
    
    def GetPolygonsSegments(self) -> int:
        """    
        Gets the number of polygon segments.
        
        :rtype: int
        :return: Polygons segments count.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Gets the number of points.
        
        :rtype: int
        :return: Point count.
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Gets the tangent count.
        
        :rtype: int
        :return: Tangent count.
        
        
        """
        ...
    
    def GetSegments(self) -> int:
        """    
        Gets the segment count.
        
        :rtype: int
        :return: Segment count.
        
        
        """
        ...
    
    def GetTangents(self) -> None:
        """    
        Returns a list of tangents.
        
        :rtype: list of :class:`Vector <c4d.Vector>`
        :return: The vector list.
        
        
        """
        ...
    
    def SetTangent(self, i: int, p: Vector) -> None:
        """    
        Set a tangent.
        
        :type i: int
        :param i: The tangent index.
        :raise IndexError: If the tangent index *i* is out of range : *0<=i<*:meth:`GetCount`.
        :type p: c4d.Vector
        :param p: The tangent.
        
        
        """
        ...
    

class HairSelectionTag(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.hair.HairSelectionTag
        :return: A new hair selection tag.
        
        
        """
        ...
    
    def GetSelected(self) -> BaseSelect:
        """    
        Gets the selection.
        
        :rtype: c4d.BaseSelect
        :return: The selection or **None**.
        
        
        """
        ...
    
    def SetSelected(self, bs: BaseSelect) -> bool:
        """    
        Sets the selection.
        
        :type bs: c4d.BaseSelect
        :param bs: The selection.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetSelectionType(self) -> int:
        """    
        Get the selection type.
        
        :rtype: int
        :return: The type:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetSelectionType(self, mode: int) -> None:
        """    
        Set the selection type.
        
        :type mode: int
        :param mode: The type:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetCount(self) -> int:
        """    
        Gets the count.
        
        :rtype: int
        :return: Number of elements.
        
        
        """
        ...
    
    def GetSegments(self) -> int:
        """    
        Gets the segment count.
        
        :rtype: int
        :return: Number of segments.
        
        
        """
        ...
    

class HairObject(BaseObject):
    def Lock(self, pDoc: BaseDocument, pThread: BaseThread, bValidate: bool, flags: int) -> bool:
        """    
        Locks the hair object.
        
        :param pDoc: The document.
        :type pDoc: c4d.documents.BaseDocument
        :param pThread: The thread.
        :type pThread: c4d.threading.BaseThread
        :param bValidate: Validate the lock.
        :type bValidate: bool
        :param flags: Lock flags
        
        .. include:: /consts/HAIR_LOCK_FLAGS.rst
        :start-line: 3
        
        :type flags: int
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def IsLocked(self) -> bool:
        """    
        Checks if the hair object is locked.
        
        :rtype: bool
        :return: **True** if the hair object is locked, otherwise **False**.
        
        
        """
        ...
    
    def Unlock(self) -> None:
        """    
        Unlocks the hair object.
        
        
        """
        ...
    
    def GetGuides(self) -> HairGuides:
        """    
        Gets the guides of this hair object.
        
        :rtype: c4d.modules.hair.HairGuides
        :return: The guides.
        
        
        """
        ...
    
    def GetDynamicGuides(self) -> HairGuides:
        """    
        Gets the dynamic guides of this hair object.
        
        :rtype: c4d.modules.hair.HairGuides
        :return: The dynamic guides.
        
        
        """
        ...
    
    def GenerateHair(self, flags: int, count: int, segments: int) -> None:
        """    
        Generates hair for the hair object.
        
        :type flags: int
        :param flags: The generate flags:
        
        .. include:: /consts/HAIR_GENERATE_FLAGS.rst
        :start-line: 3
        
        :type count: int
        :param count: The hair count.
        :type segments: int
        :param segments: The segments.
        
        
        """
        ...
    
    def RemoveGuides(self) -> None:
        """    
        Removes the guides of this hair object.
        
        
        """
        ...
    
    def GetRootObject(self) -> None:
        """    
        Gets the root object and tag!
        
        
        .. code-block:: python
        
        root = ho.GetRootObject()
        if not root: return
        
        print root["pObject"], root["pTag"]
        
        :rtype: dict{"pObject": c4d.BaseObject, "pTag": c4d.BaseTag}
        :return: The root object and tag or **None**.
        
        
        """
        ...
    
    def Update(self) -> bool:
        """    
        Updates this hair object.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetGuides(self, guides: HairGuides, clone: bool) -> None:
        """    
        Sets guides for this hair object.
        
        :type guides: c4d.modules.hair.HairGuides
        :param guides: Guides to set.
        :type clone: bool
        :param clone: Clone the supplied guides.
        
        
        """
        ...
    

class HairLibrary(object):
    def SetMode(self, doc: BaseDocument, mode: int) -> None:
        """    
        Set hair mode.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: Document.
        :type mode: int
        :param mode: New hair mode:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMode(self, doc: BaseDocument) -> int:
        """    
        Get hair mode.
        
        :type doc: c4d.documents.BaseDocument
        :param doc: Document.
        :rtype: int
        :return: Hair mode:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        
        """
        ...
    
    def BlendColors(self, mode: int, colA: Vector, colB: Vector) -> Vector:
        """    
        Blend colors.
        
        :type mode: int
        :param mode: Blend mode. (See *mhairmaterial.h* for modes, e.g. *HAIRMATERIAL_BLENDMODE_AVERAGE*.)
        :type colA: c4d.Vector
        :param colA: First color.
        :type colB: c4d.Vector
        :param colB: Second color.
        :rtype: c4d.Vector
        :return: Resulting color.
        
        
        """
        ...
    
    def MixST(self, s: float, t: float, pa: Vector, pb: Vector, pc: Vector, pd: Vector, bQuad: bool) -> Tuple[float, float]:
        """    
        Mix by the *s* and *t* coordinates among *pa*, *pb*, *pc* and *pd*.
        
        :type s: float
        :param s: S coordinate.
        :type t: float
        :param t: T coordinate.
        :type pa: c4d.Vector
        :param pa: First point value.
        :type pb: c4d.Vector
        :param pb: Second point value.
        :type pc: c4d.Vector
        :param pc: Third point value.
        :type pd: c4d.Vector
        :param pd: Fourth point value.
        :type bQuad: bool
        :param bQuad: **True** means quadrangle, **False** means triangle.
        :rtype: tuple(float, float)
        :return: The `s` and `t` coordinates.
        
        
        """
        ...
    
    def GetPolyPointST(self, p: Vector, pa: Vector, pb: Vector, pc: Vector, pd: Vector, bQuad: bool) -> Tuple[float, float]:
        """    
        Calculate the `s` and `t` coordinates of the point *p* in the polygon described by *pa*, *pb*, *pc* and *pd*.
        
        :type p: c4d.Vector
        :param p: Point to get the coordinates for.
        :type pa: c4d.Vector
        :param pa: First point value.
        :type pb: c4d.Vector
        :param pb: Second point value.
        :type pc: c4d.Vector
        :param pc: Third point value.
        :type pd: c4d.Vector
        :param pd: Fourth point value.
        :type bQuad: bool
        :param bQuad: **True** means quadrangle, **False** means triangle.
        :rtype: tuple(float, float)
        :return: The `s` and `t` coordinates.
        
        
        """
        ...
    
    def GetHairVersion(self) -> int:
        """    
        Get the hair version.
        
        :rtype: int
        :return: Hair version number.
        
        
        """
        ...
    

class HairGuides(object):
    def GetCount(self) -> int:
        """    
        Gets the number of guides.
        
        :rtype: int
        :return: Guide count.
        
        
        """
        ...
    
    def GetSegmentCount(self) -> int:
        """    
        Gets the number of segments per guide (number of points is one more than this).
        
        :rtype: int
        :return: Number of segments per guide.
        
        
        """
        ...
    
    def GetPointCount(self) -> int:
        """    
        Gets the number of points per guide. (One more than segments.)
        
        :rtype: int
        :return: Number of points per guide.
        
        
        """
        ...
    
    def GetGuidePointCount(self) -> int:
        """    
        Gets the number of points per segment.
        
        :rtype: int
        :return: Number of points per segment.
        
        
        """
        ...
    
    def GetPoints(self) -> None:
        """    
        Gets a list of points for the guides.
        
        :rtype: list of :class:`Vector <c4d.Vector>`
        :return: Point list.
        
        
        """
        ...
    
    def SetPoint(self, id: int, p: Vector) -> None:
        """    
        Set the point *p* at index *id*.
        
        :type id: int
        :param id: The point index.
        :raise IndexError: If the point index *id* is out of range : *0<=id<*:meth:`GetPointCount`.
        :type p: c4d.Vector
        :param p: The point.
        
        
        """
        ...
    
    def GetMg(self) -> Matrix:
        """    
        Gets the global matrix.
        
        :rtype: c4d.Matrix
        :return: Global matrix.
        
        
        """
        ...
    
    def SetMg(self, mg: Matrix) -> None:
        """    
        Sets the global matrix.
        
        :type mg: c4d.Matrix
        :param mg: New global matrix.
        
        
        """
        ...
    
    def GetObject(self) -> HairObject:
        """    
        Gets the corresponding hair object.
        
        :rtype: c4d.modules.hair.HairObject
        :return: Hair object.
        
        
        """
        ...
    
    def GetSelected(self, mode: int) -> BaseSelect:
        """    
        Gets the selection state.
        
        :type mode: int
        :param mode: Selection mode:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        :rtype: c4d.BaseSelect
        :return: The selection or **None**.
        
        
        """
        ...
    
    def SetSelected(self, mode: int, select: BaseSelect) -> bool:
        """    
        Sets the selection state.
        
        :type mode: int
        :param mode: Selection mode:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        :type select: c4d.BaseSelect
        :param select: The selection.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ConvertSelection(self, from_mode: int, to_mode: int, from_select: BaseSelect, to_select: BaseSelect) -> None:
        """    
        Converts the selection state.
        
        :type from_mode: int
        :param from_mode: Selection mode:
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        :type to_mode: int
        :param to_mode: To mode.
        
        .. include:: /consts/HAIR_MODE.rst
        :start-line: 3
        
        :type from_select: c4d.BaseSelect
        :param from_select: From selection.
        :type to_select: c4d.BaseSelect
        :param to_select: To selection.
        
        
        """
        ...
    
    def CopyFrom(self, src: BaseSelect) -> bool:
        """    
        Copies the guide data from *src* to this instance.
        
        :type src: c4d.BaseSelect
        :param src: Source.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetTangent(self, guide: int, segment: int, t: float) -> None:
        """    
        Gets the tangent of *guide* at *segment* and *t*.
        
        :type guide: int:
        :param guide: Guide index.
        :type segment: int
        :param segment: Segment index.
        :type t: float
        :param t: T coordinate.
        
        
        """
        ...
    
    def CreateSpline(self) -> SplineObject:
        """    
        Create splines from the guides.
        
        :rtype: c4d.SplineObject
        :return: Created splines.
        
        
        """
        ...
    
    def ToLocal(self) -> None:
        """    
        Changes all the points for the guides into a local coordinate system.
        
        
        """
        ...
    
    def ToWorld(self) -> None:
        """    
        Changes all the points for the guides into the world coordinate system.
        
        
        """
        ...
    
    def DisplaceRoots(self) -> None:
        """    
        | Used when HNs have affected the guide roots.
        | Call :meth:`HairGuides.DisplaceRoots` and it will ensure they are in the correct displaced state for HNs,
        :meth:`HairGuides.UndisplaceRoots` will make sure they are not.
        | Generally not needed if using ToInitial(), as the initial state is undisplaced.
        
        
        """
        ...
    
    def UndisplaceRoots(self) -> None:
        """    
        Inverse of :meth:`HairGuides.DisplaceRoots`.
        
        
        """
        ...
    
    def GetRootAxis(self, index: int, bAlign: bool, bLocal: bool, bInitial: bool, bZAxis: Any) -> Matrix:
        """    
        Gets the root axis of guide index.
        
        :type index: int
        :param index: Guide index.
        :type bAlign: bool
        :param bAlign: Aligned.
        :type bLocal: bool
        :param bLocal: 	Local.
        :type bInitial: bool
        :param bInitial: Initial
        :type bLocal: bool
        :param bLocal: If **True** then the alignment is done along the Z axis, otherwise it is Y.
        :rtype: c4d.Matrix
        :return: The root axis.
        
        
        """
        ...
    
    def GetRootUV(self, index: int) -> Vector:
        """    
        Gets the root UV at index.
        
        :type index: int
        :param index: Guide index.
        :rtype: c4d.Vector
        
        
        """
        ...
    
    def GetTransformMatrix(self, index: int) -> List[Matrix]:
        """    
        Gets the transformation matrix list.
        
        :type index: int
        :param index: Guide index.
        :rtype: List[c4d.Matrix]
        :return: The transformation matrix list.
        
        
        """
        ...
    
    def GetFlags(self) -> int:
        """    
        Gets the flags.
        
        :rtype: int
        :return: Flags:
        
        .. include:: /consts/HAIR_GUIDE_FLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def SetFlags(self, flags: int) -> int:
        """    
        Sets the flags.
        
        :type flags: int
        :param flags: New flags:
        
        .. include:: /consts/HAIR_GUIDE_FLAGS.rst
        :start-line: 3
        
        :rtype: int
        :return: Old flags.
        
        
        """
        ...
    

