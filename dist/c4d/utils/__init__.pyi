from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import PolygonObject, Vector, BaseSelect, BaseObject, Matrix, LineObject, BaseList2D, SplineObject, BaseDraw, BaseContainer, PointObject, UVWTag, TextureTag, BaseView, SplineData, Quaternion, UnitScaleData
from c4d.gui import EditorWindow
from c4d.documents import BaseDocument
from c4d.threading import BaseThread
from c4d.bitmaps import BaseBitmap
from c4d.utils import noise


class GeRayCollider(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.utils.GeRayCollider
        :return: A new ray collider.
        
        
        """
        ...
    
    def Init(self, goal: PolygonObject, force: bool) -> bool:
        """    
        Initializes the ray collider with the object specified by *goal*.
        
        :type goal: c4d.PolygonObject
        :param goal: The object to check for intersections. The object is copied.
        :type force: bool
        :param force:
        
        | If **False** then Cinema checks if the passed object's :meth:`C4DAtom.GetDirty(c4d.DIRTYFLAGS_DATA) <C4DAtom.GetDirty>` is unchanged. If yes, it does nothing and returns **True**.
        | If **True** it always rebuilds the cache.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Intersect(self, ray_p: Vector, ray_dir: Vector, length: Any, only_test: bool) -> bool:
        """    
        Checks if the line segment specified by *ray_p* to *ray_p + ray_dir*ray_length* intersects the object.
        
        :type ray_p: c4d.Vector
        :param ray_p: Start point of the ray in object coordinates
        :type ray_dir: c4d.Vector
        :param ray_dir: Ray direction in object coordinates.
        :type ray_length: number
        :param ray_length: Ray length.
        :type only_test: bool
        :param only_test: If this is **True** no information about the intersections are stored, so only the return value can be used to tell if there were intersections or not.
        :rtype: bool
        :return: **True** if there was in intersection, otherwise **False**
        
        
        """
        ...
    
    def GetIntersectionCount(self) -> int:
        """    
        Returns the number of intersections found by :meth:`Intersect`.
        
        :rtype: int
        :return: Number of intersections.
        
        
        """
        ...
    
    def GetIntersection(self, number: int) -> Dict[str, Any]:
        """    
        Retrieves the intersection information, found by :meth:`GeRayCollider.Intersect`, by index:
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/geraycollider/getintersection.py
        :language: python
        
        :type number: int
        :param number: Intersection index.
        :raise IndexError: If intersection index is out of range : *0<=number<*:meth:`GetIntersectionCount`.
        :rtype: dict
        :return: The intersection information.
        
        
        """
        ...
    
    def GetNearestIntersection(self) -> Dict[str, Any]:
        """    
        Retrieves the intersection, found by :meth:`Intersect`, closest to the start of the ray.
        
        :rtype: dict
        :return: The nearest intersection or **None** if there was no intersection.
        
        
        """
        ...
    

class Neighbor(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.utils.Neighbor
        :return: The new neighbor object.
        
        
        """
        ...
    
    def Init(self, op: PolygonObject, bs: Optional[BaseSelect] = ...) -> None:
        """    
        Initialise the internal polygon information.
        
        .. note::
        
        This function must be called before the class can be used to get the neighbouring polygons.
        
        :type op: c4d.PolygonObject
        :param op: The class object.
        :type bs: c4d.BaseSelect
        :param bs:  The polygon selection that will be used to build the neighbor information. By default **None** to use all polygons.
        
        
        """
        ...
    
    def Flush(self) -> None:
        """    
        Flushes the neighbor information.
        
        
        """
        ...
    
    def GetNeighbor(self, a: int, b: int, poly: int) -> None:
        """    
        .. image:: /_imgs/modules/utils/neighbor_neighbor.png
        :align: right
        
        Gets the polygon opposite to *poly* with respect to the edge from point *a* to *b*.
        
        :type a: int
        :param a: The point index that defines the first edge point.
        :type b: int
        :param b: The point index that defines the second edge point.
        :type poly: int
        :param poly: The index of the polygon to get the polygon opposite to.
        :raise IndexError: If *a*, *b* or *poly* is out of range.
        :return: The opposite polygon index, or *NOTOK* if none exists or if *poly* is not one of the edge polygons.
        :param poly: The index of the polygon to get the polygon opposite to.
        
        
        """
        ...
    
    def GetPointPolys(self, pnt: int) -> List[int]:
        """    
        .. image:: /_imgs/modules/utils/neighbor_pointpolys.png
        :align: right
        
        Get the polygons that are attached to the given point index.
        
        For example:
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/neighbor/getpointpolys.py
        :language: python
        
        :type pnt: int
        :param pnt: The point index to use to find the associated polygons.
        :raise IndexError: If *pnt* is out of range.
        :rtype: list
        :return: A list of returned polygons.
        
        
        """
        ...
    
    def GetEdgePolys(self, a: int, b: int) -> Tuple[int, int]:
        """    
        .. image:: /_imgs/modules/utils/neighbor_edgepolys.png
        :align: right
        
        Get the polygons that neighbor the given edge:
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/neighbor/getedgepolys.py
        :language: python
        
        :type a: int
        :param a: The point index that defines the first edge point.
        :type b: int
        :param b: The point index that defines the second edge point.
        :raise IndexError: If *a* or *b* is out of range.
        :rtype: tuple(int, int)
        :return: The first and second polygon associated with the edge.
        
        
        """
        ...
    
    def GetEdgeCount(self) -> int:
        """    
        Get the total number of edges found.
        
        :rtype: int
        :return: The number of edges.
        
        
        """
        ...
    
    def GetPolyInfo(self, poly: int) -> None:
        """    
        Get a dict that contains neighbor information about the given polygon. One can use this to browse through all available edges using the following code
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/neighbor/getpolyinfo.py
        :language: python
        
        | `0`-`1`-`2`-`3` are the indices for `a`-`b`/`b`-`c`/`c`-`d`/`d`-`a`.
        | For triangles the face/edge index 2 is set to *NOTOK* (as `c` == `d`). e.g. a value of `5-8-2-1` for `face` means: `a`-`b` neighbor
        `face` is `5`, `b`-`c` neighbor `face` is `8` etc.
        
        :type poly: int
        :param poly: The polygon index to get the neighbor information for.
        :rtype: dict{**mark**: bool*4, **face**: int*4, **edge**: int*4}
        :return: The neighbor information about the given polygon.
        :key mark: **False** if that polygon "generated" an edge, for example think of two polygons that share an edge, one has set mark = **False** for this edge because it was the first and "built" this edge and the other(s) will set mark = **True** as no new edge had to be generated.
        :key face: The neighbouring polygons. **Note**: If a value is *NOTOK* this means there is no neighbor.
        :key edge: The edges of the polygon.
        
        
        """
        ...
    
    def GetPointOneRingPoints(self, pnt: int) -> List[int]:
        """    
        Gets the points that are attached through one edge to the given point.
        
        .. versionadded:: R19
        
        :type pnt: int
        :param pnt: The point index to use to find the associated one ring points.
        :rtype: List[int]
        :return: A list of points indices.
        
        
        """
        ...
    

class PolygonReduction(object):
    def __init__(self) -> None:
        """    
        Creates a polygon reduction object.
        
        :rtype: c4d.utils.PolygonReduction
        :return: A new polygon reduction object.
        
        
        """
        ...
    
    def PreProcess(self, data: Dict[str, Any]) -> bool:
        """    
        Starts the background or synchronous preprocessing that sets up the polygon reduction cache.
        
        :type data: dict
        :param data: The data for the reduction. See :ref:`polygonreductiondata_dictionary`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def IsPreprocessing(self) -> bool:
        """    
        Checks whether the background preprocessing thread is still running.
        
        :rtype: bool
        :return: **True** if preprocessing is ongoing, otherwise **False**.
        
        
        """
        ...
    
    def StopPreprocessing(self) -> None:
        """    
        Aborts preprocessing if it is running in the background. Resets the interactive settings values.
        
        
        """
        ...
    
    def Reset(self) -> None:
        """    
        Aborts preprocessing if it is running in the background and frees all temporary data.
        
        
        """
        ...
    
    def SetReductionStrengthLevel(self, strengthLevel: float) -> bool:
        """    
        Sets the reduction strength level if the desired level is different than the current one.
        
        :type strengthLevel: float
        :param strengthLevel: The desired reduction strength level.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetTriangleLevel(self, desiredLevel: int) -> bool:
        """    
        Reduces or restores the mesh to the desired number of triangles.
        
        .. note::
        
        | If the desired level is different than the current level, at least one edge collapse or restore will be performed.
        | The actual resulting number of triangles may be slightly different.
        
        :type desiredLevel: int
        :param desiredLevel: The desired number of triangles on call.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetVertexLevel(self, desiredLevel: int) -> bool:
        """    
        Reduces or restores the mesh to the desired number of vertices.
        
        .. note::
        
        | If the desired level is different than the current level, at least one edge collapse or restore will be performed.
        | The actual resulting number of vertices may be slightly different.
        
        :type desiredLevel: int
        :param desiredLevel: The desired number of vertices on call.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def SetRemainingEdgesLevel(self, desiredLevel: int) -> bool:
        """    
        Reduces or restores the mesh to the desired number of edges remaining to collapse.
        
        .. note::
        
        | If the desired level is different than the current level, at least one edge collapse or restore will be performed.
        | The actual resulting number of edges may be slightly different.
        
        :type desiredLevel: int
        :param desiredLevel: The desired number of collapse stack.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetReductionStrengthLevel(self) -> int:
        """    
        Queries the current reduction strength level.
        
        :rtype: int
        :return: The reduction strength percentage: `0` means no reduction performed, `1` means maximum reduction performed.
        
        
        """
        ...
    
    def GetTriangleLevel(self) -> int:
        """    
        Queries the current triangle count.
        
        :rtype: int
        :return: The triangle count.
        
        
        """
        ...
    
    def GetVertexLevel(self) -> int:
        """    
        Queries the current vertex count.
        
        :rtype: int
        :return: The vertex count.
        
        
        """
        ...
    
    def GetRemainingEdgesLevel(self) -> int:
        """    
        Queries the current remaining number of edges available to collapse.
        
        :rtype: int
        :return: The remaining edges level.
        
        
        """
        ...
    
    def GetMaxReductionStrengthLevel(self) -> float:
        """    
        Queries the maximum reduction strength percentage.
        
        :rtype: float
        :return: The maximum reduction strength percentage. Always `1.0`.
        
        
        """
        ...
    
    def GetMaxTriangleLevel(self) -> int:
        """    
        Queries the triangle count when no reduction has been performed.
        
        :rtype: int
        :return: The maximum triangle count.
        
        
        """
        ...
    
    def GetMaxVertexLevel(self) -> int:
        """    
        Queries the vertex count when no reduction has been performed.
        
        :rtype: int
        :return: The maximum vertex count.
        
        
        """
        ...
    
    def GetMaxRemainingEdgesLevel(self) -> int:
        """    
        Queries the total number of possible edge collapses.
        
        :rtype: int
        :return: The maximum collapse count.
        
        
        """
        ...
    
    def GetMinTriangleLevel(self) -> int:
        """    
        Queries the triangle count when complete reduction has been performed.
        
        :rtype: int
        :return: The minimum triangle count. May be non-zero if border constraints are enabled.
        
        
        """
        ...
    
    def GetMinVertexLevel(self) -> int:
        """    
        Queries the vertex count when complete reduction has been performed.
        
        :rtype: int
        :return: The minimum vertex count. May be non-zero if border constraints are enabled.
        
        
        """
        ...
    
    def GetData(self) -> Dict[str, Any]:
        """    
        Retrieves the associated data for the polygon reduction.
        
        :rtype: dict
        :return: The associated data. See :ref:`polygonreductiondata_dictionary`.
        
        
        """
        ...
    
    def IsValid(self) -> bool:
        """    
        Checks if a valid object and a valid document are associated with the :class:`PolygonReduction <c4d.utils.PolygonReduction>` instance.
        
        :rtype: bool
        :return: **True** if the :class:`PolygonReduction <c4d.utils.PolygonReduction>` instance is valid, otherwise **False**.
        
        
        """
        ...
    

class SplineHelp(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.utils.SplineHelp
        :return: A new spline help object.
        
        
        """
        ...
    
    def InitSpline(self, op: BaseObject, up: Optional[Vector] = ..., rail: Optional[BaseObject] = ..., target_rail: Optional[bool] = ..., use_deformed_points: Optional[bool] = ..., force_update: Optional[bool] = ..., use_global_space: Optional[bool] = ...) -> bool:
        """    
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>`. Must be called before any other function.
        
        .. deprecated:: R17.048
        
        Instead use the specialized **Init()** methods: :meth:`InitSplineWith`, :meth:`InitSplineWithUpVector`, :meth:`InitSplineWithRail`
        
        :type op: c4d.BaseObject
        :param op: The spline object to use.
        :type up: c4d.Vector
        :param up: Optional upvector for the spline normals generation. This is only used at the start of splines/segments; this way it avoids gimbal lock if at all possible.
        :type rail: c4d.BaseObject
        :param rail: Optional rail spline object for the spline normals generation.
        :type target_rail: bool
        :param target_rail: The optional rail spline is not only used as up-vector but also as target. This is used for instance in MoGraph's Rail options (Cloner, Spline effector, Spline Wrap etc.).
        :type use_deformed_points: bool
        :param use_deformed_points: Use deformed point positions of the spline.
        :type force_update: bool
        :param force_update: The spline help class internally caches its own content. Thus it will be much faster if the same splines are used for initialization. However, a full initialization can be forced by setting this parameter to **True**.
        :type use_global_space: bool
        :param use_global_space: If **True** the resulting matrices are in global space rather than in the spline objects' local space.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitSplineWith(self, op: BaseObject, flags: int) -> bool:
        """    
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>` with the passed spline *op*.
        
        .. versionadded:: R17.048
        
        .. warning:: Must be called before any other function.
        
        :type op: c4d.BaseObject
        :param op: The spline object to use.
        :type flags: int
        :param flags: The optional flags used to control how the :class:`SplineHelp <c4d.utils.SplineHelp>` is setup:
        
        .. include:: /consts/SPLINEHELPFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitSplineWithUpVector(self, op: BaseObject, upvector: Vector, flags: int) -> bool:
        """    
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>` with the passed spline *op* and *upvector*.
        
        .. versionadded:: R17.048
        
        .. warning:: Must be called before any other function.
        
        :type op: c4d.BaseObject
        :param op: The spline object to use.
        :type upvector: c4d.Vector
        :param upvector: The initial up-vector for the spline.
        :type flags: int
        :param flags: The optional flags used to control how the :class:`SplineHelp <c4d.utils.SplineHelp>` is setup:
        
        .. include:: /consts/SPLINEHELPFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def InitSplineWithRail(self, op: BaseObject, rail: BaseObject, flags: int) -> bool:
        """    
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>` with the passed spline *op* and *rail*.
        
        .. versionadded:: R17.048
        
        .. warning:: Must be called before any other function.
        
        :type op: c4d.BaseObject
        :param op: The spline object to use.
        :type rail: c4d.BaseObject
        :param rail: The rail spline.
        :type flags: int
        :param flags: The optional flags used to control how the :class:`SplineHelp <c4d.utils.SplineHelp>` is setup:
        
        .. include:: /consts/SPLINEHELPFLAGS.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def FreeSpline(self) -> None:
        """    
        Called to free the spline data. Recalling :meth:`InitSpline` or calling **SplineHelp.__free__** will automatically call this.
        
        
        """
        ...
    
    def Exists(self) -> bool:
        """    
        Useful check to see if the spline helper contains data and has been inited.
        
        :rtype: bool
        :return: **True** if the spline helper is ready to use.
        
        
        """
        ...
    
    def GetSegmentCount(self) -> int:
        """    
        Gets the number of segments in the spline.
        
        .. note::
        
        Unlike the way Cinema 4D handles segments where a segmenet count of 0 means there's either no segments or 1 segment, this returns 1 segment if there is 1 and 0 if there are 0.
        
        :rtype: int
        :return: Segment count.
        
        
        """
        ...
    
    def GetVertexMatrix(self, index: int) -> Matrix:
        """    
        Retrieves a full matrix for a specific point of the line.
        
        .. note::
        
        This is not the spline vertex, but instead the line object's vertex. (Calculated with LOD=1.0.)
        
        :type index: int
        :param index: Line object's vertex.
        :raise IndexError: If the point *index* is out of range : *0<=segment<*:meth:`PointObject.GetPointCount`.
        :rtype: c4d.Matrix
        :return: Coordinate system matrix at *index*.
        
        
        """
        ...
    
    def GetPointValue(self, offset: float, segment: int) -> float:
        """    
        Converts a natural offset value to a real percentage offset value.
        
        .. note::
        
        | This percentage uses the real world units for its offset.
        | So regardless of how the spline's points and interpolation is set, a gap of 2% on a 100m long spline will always be 2m whereas normally in spline natural space, a gap of 2% can vary a great deal depending on the spline's interpolation etc.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: float
        :return: The realworld percentage offset.
        
        
        """
        ...
    
    def GetPointIndex(self, offset: float, segment: int) -> int:
        """    
        Retrieves the nearest line point index to the given real *offset*.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: int
        :return: The nearest line object point index, rounded down.
        
        
        """
        ...
    
    def GetPos(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Vector:
        """    
        .. deprecated:: R15
        
        Use :meth:`SplineHelp.GetPosition`.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed position.
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution.
        :rtype: c4d.Vector
        :return: The position given by *offset* in global space.
        
        
        """
        ...
    
    def GetPosition(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Vector:
        """    
        Retrieves the nearest line point index to the given real *offset*.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed position.
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution.
        :rtype: c4d.Vector
        :return: The position given by *offset* in global space.
        
        
        """
        ...
    
    def GetTangent(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Vector:
        """    
        Gets a tangent vector for any point along the spline.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed tangent.
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution.
        :rtype: c4d.Vector
        :return: The tangent given by *offset* in global space.
        
        
        """
        ...
    
    def GetNormal(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Vector:
        """    
        Gets a normal vector for any point along the spline.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed normal.
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution.
        :rtype: c4d.Vector
        :return: The normal given by *offset* in global space.
        
        
        """
        ...
    
    def GetCrossNormal(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Vector:
        """    
        Gets a cross normal vector (i.e. perpendicular to the normal and the tangent) for any point along the spline.
        
        :type offset: float
        :param offset: The offset given in spline space.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed cross normal.
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution.
        :rtype: c4d.Vector
        :return: The cross normal given by *offset* in global space.
        
        
        """
        ...
    
    def GetSegmentLength(self, segment: int) -> float:
        """    
        Returns a specific segment's realworld unit length.
        
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: float
        :return: The length of the specified segment.
        
        
        """
        ...
    
    def GetSplineLength(self) -> float:
        """    
        Returns the spline's realworld unit length including all segments.
        
        :rtype: float
        :return: Spline length.
        
        
        """
        ...
    
    def GetOffsetFromUnit(self, unitoffset: float, segment: int) -> float:
        """    
        | Retrieve an offset from a realworld unit.
        |
        | For example, if a spline is 50 units long, 25 would be 50% of the length, i.e. 0.5.
        
        :type unitoffset: float
        :param unitoffset: The real unit offset to convert.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: float
        :return: The offset in spline space.
        
        
        """
        ...
    
    def GetOffsetFromReal(self, offset: float, segment: int) -> float:
        """    
        | Convert a percentage offset into a natural offset.
        | Percentage offsets ignore spline interpolation etc. and are always x% along the spline.
        
        :type offset: float
        :param offset: A percentage offset, *0<=offset<=1.0*.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: float
        :return: The natural offset.
        
        
        """
        ...
    
    def SplineToLineIndex(self, index: int) -> int:
        """    
        Converts a spline vertex index to its corresponding line object vertex index.
        
        :type index: int
        :param index: The spline vertex index.
        :rtype: int
        :return: The line object vertex index.
        
        
        """
        ...
    
    def GetSize(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> float:
        """    
        Get the distance to an existing rail spline for any point along the spline.
        
        :type offset: float
        :param offset: The spline offset.
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed position
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution
        :rtype: float
        :return: The distance given by **offset**.
        
        
        """
        ...
    
    def GetMatrix(self, offset: float, segment: int, smooth: bool, realoffset: bool) -> Matrix:
        """    
        | Retrieve a full matrix for any point along the spline, constructed as a local coordinate system at that point.
        | Optionally use realworld percentage rather than spline natural space for the offset.
        
        :type offset: float
        :param offset: The spline offset.
        :type segment: int
        :param segment: Segment index.
        :raise IndexError: If *segment* index is out of range : *0<=segment<*:meth:`GetSegmentCount`.
        :type smooth: bool
        :param smooth: Smoothed position
        :type realoffset: bool
        :param realoffset: **True** to use uniform spline distribution
        :rtype: c4d.Matrix
        :return: Coordinate system matrix at **offset**.
        
        
        """
        ...
    
    def GetVertexCount(self, segment: int) -> int:
        """    
        Get the number of vertices for a spline segment.
        
        :type segment: int
        :param segment: The segment index.
        :raise IndexError: If the *segment* index is out of range : must be *0<=segment<*:meth:`GetSegmentCount`.
        :rtype: int
        :return: The number of vertices.
        
        
        """
        ...
    
    def GetVertexSize(self, index: int) -> int:
        """    
        Get the distance to an existing rail spline for a spline vertex specified by *index*.
        
        :type index: int
        :param index: The vertex index.
        :raise IndexError: If the vertex *index* is out of range : must be *0<=segment<*:meth:`GetVertexCount`.
        :rtype: int
        :return: The distance given by *index*.
        
        
        """
        ...
    
    def GetDirty(self) -> int:
        """    
        Gets the dirty value for the :class:`SplineHelp <c4d.utils.SplineHelp>` which indicates how often the help has been updated with new values. i.e. how often the source spline has changed, and or the spline has been cleared.
        
        .. versionadded:: R17.048
        
        :rtype: int
        :return: The dirty checksum.
        
        
        """
        ...
    
    def GetPointMatrix(self, splineVertexIndex: int) -> Matrix:
        """    
        Gets the matrix for a spline vertex.
        
        .. versionadded:: R17.048
        
        :type splineVertexIndex: int
        :param splineVertexIndex: The zero-based index of the spline vertex.
        :rtype: c4d.Matrix
        :return: The resulting matrix for the point along the spline.
        
        
        """
        ...
    
    def GetLineObject(self) -> LineObject:
        """    
        Gets a :class:`LineObject <c4d.LineObject>` from SplineHelp functions.
        
        .. versionadded:: R17.048
        
        .. note::
        
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>` with **SPLINEHELPFLAGS_RETAINLINEOBJECT** for this method to return a line object.
        
        :rtype: c4d.LineObject
        :return: The line object. **None** if it fails or if the :class:`SplineHelp <c4d.utils.SplineHelp>` was not initialized with **SPLINEHELPFLAGS_RETAINLINEOBJECT**
        
        
        """
        ...
    
    def GetCacheObject(self) -> Union[None, BaseList2D]:
        """    
        | Gets the cache SplineObject.
        | Useful if you need to access the point array from outside the helper while avoiding duplicating the cache and deform fetch code duplication.
        
        .. versionadded:: S22
        
        .. note::
        
        Initializes the :class:`SplineHelp <c4d.utils.SplineHelp>` with :meth:'SplineHelp.InitSpline'.
        
        :return: The cache object or **None** if it fails or if the SplineHelp was not initialized.
        :rtype: Union[None, c4d.BaseList2D]
        
        
        """
        ...
    

class SplineLengthData(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.utils.SplineLengthData
        :return: A new spline length data object.
        
        
        """
        ...
    
    def Init(self, op: SplineObject, segment: int) -> None:
        """    
        Initialize the spline length data object with a spline.
        
        :type op: c4d.SplineObject
        :param op: The spline object to use.
        :type segment: int
        :param segment: The segment of the spline.
        :raise IndexError: If the *segment* index is out of range : *0<=segment<*:meth:`SplineObject.GetSegmentCount`.
        
        
        """
        ...
    
    def Free(self) -> None:
        """    
        Called to free the spline.
        
        
        """
        ...
    
    def UniformToNatural(self, t: float) -> float:
        """    
        | Get the natural position along the spline.
        | The uniform position is with respect to the actual length of the spline, whereas the natural position only cares about the interpolation of the curve parameter.
        
        :type t: float
        :param t: The uniform position along the spline.
        :rtype: float
        :return: The natural position in the segment.
        
        
        """
        ...
    
    def GetLength(self) -> float:
        """    
        Returns the length of the spline data object.
        
        :rtype: float
        :return: The length.
        
        
        """
        ...
    
    def GetSegmentLength(self, a: int, b: int) -> None:
        """    
        Get the length of the segment.
        
        :type a: int
        :param a: Start of the segment.
        :type b: int
        :param b: End of the segment.
        
        
        """
        ...
    

class ViewportSelect(object):
    def __init__(self) -> None:
        """    
        :rtype: c4d.utils.ViewportSelect
        :return: A new viewport select object.
        
        
        """
        ...
    
    def Init(self, w: int, h: int, bd: BaseDraw, ops: Any, mode: int, onlyvisible: bool, flags: int) -> None:
        """    
        Initializes the viewport information for multiple objects. This has to be done before the pixel information can be retrieved. You have to retrieve the width and height of the viewport manually:
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/viewportselect/init.py
        :language: python
        
        :type w: int
        :param w: Width of the viewport in pixels.
        :type h: int
        :param h: Height of the viewport in pixels.
        :type bd: c4d.BaseDraw
        :param bd: The viewport base draw.
        :type ops: list of :class:`BaseObject <c4d.BaseObject>`
        :param ops: A list with objects to get the information for.
        :type mode: int
        :param mode: Editor mode:
        
        .. include:: /consts/MEditorModes_ViewportSelect.rst
        :start-line: 3
        
        :type onlyvisible: bool
        :param onlyvisible: If this is **True** only visible elements are included.
        
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/VIEWPORTSELECTFLAGS.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetPixelInfoPoint(self, x: int, y: int) -> None:
        """    
        Retrieves point information at the pixel position (*x*, *y*):
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/viewportselect/getpixelinfopoint.py
        :language: python
        
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def GetPixelInfoPolygon(self, x: int, y: int) -> None:
        """    
        Retrieves polygon information at the pixel position (*x*, *y*):
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/viewportselect/getpixelinfopolygon.py
        :language: python
        
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def GetPixelInfoEdge(self, x: int, y: int) -> None:
        """    
        Retrieves edge information at the pixel position (*x*, *y*):
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/viewportselect/getpixelinfoedge.py
        :language: python
        
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def GetNearestPoint(self, op: BaseObject, x: int, y: int, maxrad: int, onlyselected: bool, ignorelist: List[Any], ignorecnt: int) -> None:
        """    
        Retrieves nearest point information at the pixel position (*x*, *y*).
        
        :type op: c4d.BaseObject
        :param op: The object to search for the closest element.
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`. If an element was found the reference is updated to reflect the X coordinate of the nearest point.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`. If an element was found the reference is updated to reflect the Y coordinate of the nearest point.
        :type maxrad: int
        :param maxrad: A maximal radius for the search in pixels.
        :type onlyselected: bool
        :param onlyselected: If this is True only selected elements are included in the search.
        :type ignorelist: list
        :param ignorelist: List of points to ignore.
        :type ignorecnt: int
        :param ignorecnt: Ignore list count.
        
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float, **x**: float, **y**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **x**  | float                                | X pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **y**  | float                                | Y pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def GetNearestPolygon(self, op: BaseObject, x: int, y: int, maxrad: int, onlyselected: bool, ignorelist: List[Any], ignorecnt: int) -> None:
        """    
        Retrieves nearest polygon information at the pixel position (*x*, *y*).
        
        :type op: c4d.BaseObject
        :param op: The object to search for the closest element.
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`. If an element was found the reference is updated to reflect the X coordinate of the nearest point.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`. If an element was found the reference is updated to reflect the Y coordinate of the nearest point.
        :type maxrad: int
        :param maxrad: A maximal radius for the search in pixels.
        :type onlyselected: bool
        :param onlyselected: If this is True only selected elements are included in the search.
        :type ignorelist: list
        :param ignorelist: List of points to ignore.
        :type ignorecnt: int
        :param ignorecnt: Ignore list count.
        
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float, **x**: float, **y**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **x**  | float                                | X pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **y**  | float                                | Y pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def GetNearestEdge(self, op: BaseObject, x: int, y: int, maxrad: int, onlyselected: bool, ignorelist: List[Any], ignorecnt: int) -> None:
        """    
        Retrieves nearest edge information at the pixel position (*x*, *y*).
        
        :type op: c4d.BaseObject
        :param op: The object to search for the closest element.
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`. If an element was found the reference is updated to reflect the X coordinate of the nearest point.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *y* is the width given to :meth:`Init`. If an element was found the reference is updated to reflect the Y coordinate of the nearest point.
        :type maxrad: int
        :param maxrad: A maximal radius for the search in pixels.
        :type onlyselected: bool
        :param onlyselected: If this is True only selected elements are included in the search.
        :type ignorelist: list
        :param ignorelist: List of points to ignore.
        :type ignorecnt: int
        :param ignorecnt: Ignore list count.
        
        :rtype: dict{**i**: int, **op**: :class:`BaseObject <c4d.BaseObject>`, **z**: float, **x**: float, **y**: float}
        
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **i**  | int                                  | Element index. The index depends on the element type: |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | point                                                 | point index                        |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | polygon                                               | polygon index                      |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | edge                                                  | 4*polygon + edge index             |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        |        |                                      | spline                                                | point segment offset + point index |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **op** | :class:`BaseObject <c4d.BaseObject>` | Object.                                               |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **z**  | float                                | Z coordinate of the current element.                  |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **x**  | float                                | X pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        | **y**  | float                                | Y pixel position.                                     |                                    |
        +--------+--------------------------------------+-------------------------------------------------------+------------------------------------+
        
        :return: The retrieved pixel information or **None** if no information could be retrieved.
        
        
        """
        ...
    
    def DrawPolygon(self, p: Any, i: int, op: BaseObject, onlyvisible: int) -> bool:
        """    
        Draws a polygon into the internal pixel structure, so that pixels inside the polygon will be associated with *i* and *op* in the viewport pixel retrieved.
        
        :type p: *array* (:class:`Vector <c4d.Vector>`)
        :param p: An array of points that make up the polygon.
        
        .. note:: All coordinates are in screen space.
        
        :type i: int
        :param i: The polygon index to associate with this polygon.
        :type op: c4d.BaseObject
        :param op: The object to associate with this polygon.
        :type onlyvisible: int
        :param onlyvisible: If this is **True**, only visible parts of the polygon are drawn.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def DrawHandle(self, p: Vector, i: int, op: BaseObject, onlyvisible: int) -> bool:
        """    
        Draws a handle into the internal pixel structure, so that pixels inside the handle will be associated with *i* and *op* in the viewport pixel retrieved.
        
        :type p: c4d.Vector
        :param p: The position of the handle.
        
        .. note:: All coordinates are in screen space.
        
        :type i: int
        :param i: The polygon index to associate with this polygon.
        :type op: c4d.BaseObject
        :param op: The object to associate with this polygon.
        :type onlyvisible: int
        :param onlyvisible: If this is **True**, only visible parts of the handle are drawn.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def ShowHotspot(self, bw: EditorWindow, x: int, y: int) -> None:
        """    
        Draws an XOR circle to the view *bw* at the pixel position (*x*, *y*). The radius is set by :meth:`SetBrushRadius`.
        
        :type bw: c4d.gui.EditorWindow
        :param bw: The editor window to draw to.
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        
        
        """
        ...
    
    def SetBrushRadius(self, r: float) -> None:
        """    
        Sets the radius for :meth:`ShowHotspot`.
        
        :type r: float
        :param r: The new radius in pixels.
        
        
        """
        ...
    
    def ClearPixelInfo(self, x: int, y: int, mask: int) -> None:
        """    
        Deletes the pixel information at (*x*, *y*) according to mask.
        
        This is used for example in the live edge selection with "tolerant" deactivated to find out how many pixels of a certain edge was selected. If an edge is determined under the cursor, the pixel counter is decremented and the edge information is deleted afterwards.
        
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        :type mask: int
        :param mask: A bitfield of what to clear:
        
        .. include:: /consts/VIEWPORT_CLEAR.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetCameraCoordinates(self, x: float, y: float, z: float) -> Vector:
        """    
        Converts the pixel position (*x*, *y*, *z*) to camera coordinates.
        
        :type x: float
        :param x: An X coordinate within the viewport.
        :type y: float
        :param y: An Y coordinate within the viewport.
        :type z: float
        :param z: A Z coordinate.
        :rtype: c4d.Vector
        :return: The calculated camera coordinate.
        
        
        """
        ...
    
    def PickObject(self, bd: BaseDraw, doc: BaseDocument, x: int, y: int, rad: int, flags: int) -> None:
        """    
        Pick objects.
        
        :type bd: c4d.BaseDraw
        :param bd: The viewport base draw.
        :type doc: c4d.documents.BaseDocument
        :param doc: Document.
        :type x: int
        :param x: An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to :meth:`Init`.
        :type y: int
        :param y: An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to :meth:`Init`.
        :type rad: int
        :param rad: A radius for the search in pixels.
        :type flags: int
        :param flags: Flags:
        
        .. include:: /consts/VIEWPORT_PICK_FLAGS.rst
        :start-line: 3
        
        :rtype: list[:class:`BaseObject <c4d.BaseObject>`]
        :return: Object list or **None** on failure.
        
        
        """
        ...
    


def SendModelingCommand(command: int, list: Any, mode: int, bc: BaseContainer, doc: BaseDocument, flags: int) -> None:
    """    
    | With this function one can apply nearly all modeling commands.
    | The function is applied to the objects in *list*. With the parameter *mode* you can decide
    if the current selection should be used to control what points/polygons are affected.
    
    .. note::
    
    | Current State to Object(CSTO) has to be executed on a duplicate of an object because CSTO modifies the existing caches.
    | In some cases you have to use a temporary document as well :meth:`ObjectData.GetVirtualObjects`.
    
    This is a small example how you can use this function
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/sendmodelingcommand.py
    :language: python
    
    :param command: The modeling command. See :doc:`MCOMMAND </consts/MCOMMAND>`.
    :type command: int
    :param list: A list with objects which you want to apply the modeling command.
    :type list: list of :class:`BaseObjects <c4d.BaseObject>`
    :param bc: This is a settings container which contains all the values of the tool you want to apply.
    :type bc: c4d.BaseContainer
    :param mode: Modeling mode:
    
    .. include:: /consts/MODELINGCOMMANDMODE.rst
    :start-line: 3
    
    :type mode: int
    :param doc:
    
    | The document for the operation. Should be set if possible. Must be set for *MCOMMAND_JOIN*, *MCOMMAND_MAKEEDITABLE*, *MCOMMAND_CURRENTSTATETOOBJECT* and *MCOMMAND_SPLINE_PROJECT*.
    | If you set the document, the objects which you pass to this function have to be in the same document. So pay attention that you use one send_modeling_command per document for objects.
    
    :type doc: c4d.documents.BaseDocument
    :param flags: The flags:
    
    .. include:: /consts/MODELINGCOMMANDFLAGS.rst
    :start-line: 3
    
    :type flags: int
    :return: **True** if the command succeeded, otherwise **False** if something went wrong. Some commands do not apply their task to the passed objects, they return a cloned object so just check it.
    :rtype: **False**, **True** or list of :class:`BaseObject <c4d.BaseObject>`
    
    
    """
    ...

def DisjointMesh(op: PointObject) -> bool:
    """    
    | Separates the mesh of the object to make each polygon/line segment independent.
    | Each polygon/line will be given its own points thereby separating them so they can be moved independently, such as the Explosion object.
    
    :type op: c4d.PointObject
    :param op: The point object to disjoint.
    :rtype: bool
    :param: **True** if the mesh was disjointed successfully, otherwise **False**.
    
    
    """
    ...

def FitCurve(padr: Any, error: float, bt: BaseThread) -> None:
    """    
    Creates a spline object that has the best fit through the given points.
    
    :type padr: list of :class:`c4d.Vector`
    :param padr: The points to fit a curve to.
    :type error: float
    :param error: Sets how closely the curve must match the passed points. The lower the value then the closer the curve will match.
    :type bt: c4d.threading.BaseThread
    :param bt:
    
    .. versionadded:: R18.057
    
    An optional thread.
    
    :rtype: :class:`c4d.SplineObject`
    :return: A Spline object that fits the given points, or AllocationFailed error if a spline object cannot be obtained.
    
    
    """
    ...

def CheckDisplayFilter(op: BaseObject, filter: int) -> bool:
    """    
    Checks if object *op* would be displayed with the given *filter*.
    
    Example:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/checkdisplayfilter.py
    :language: python
    
    :type op: c4d.BaseObject
    :param op: The object to check.
    :type filter: int
    :param filter: The filter bitmask:
    
    .. include:: /consts/DISPLAYFILTER.rst
    :start-line: 3
    
    :rtype: bool
    :return: **True** if the object would be displayed, otherwise **False**.
    
    
    """
    ...

def CalculateVisiblePoints(bd: BaseDraw, op: PolygonObject, visible: Optional[bool] = ...) -> List[int]:
    """    
    Checks if points in the polygon object *op* are visible in the view *bd*.
    
    :type bd: c4d.BaseDraw
    :param bd: The base draw to check.
    :type op: c4d.PolygonObject
    :param op: The object to check.
    :type visible: Optional[bool]
    :param visible:
    
    .. versionadded:: R19.068
    
    **True** to include only visible points, otherwise **False** (default) to also include hidden points like for example those from the back of an object.
    
    :rtype: List[int]
    :return:
    
    | A list of integers with the visibility status for each point: `1` if the point is visible otherwise `0`.
    | **None** if the function fails.
    
    
    """
    ...

def GenerateUVW(op: BaseObject, opmg: Matrix, tp: TextureTag, texopmg: Matrix, view: Optional[BaseView] = ...) -> UVWTag:
    """    
    Generates a UVW tag for an object.
    
    :type op: c4d.BaseObject
    :param op: The object to generate the UVW coordinates for.
    :type opmg: c4d.Matrix
    :param opmg: The object's global matrix.
    :type tp: c4d.TextureTag
    :param tp: The texture tag to generate the UVW coordinates from.
    :type texopmg: c4d.Matrix
    :param texopmg: The global matrix of the object that carries the texture tag.
    :type view: c4d.BaseView
    :param view: The optional current view.
    :rtype: c4d.UVWTag
    :return:
    
    | The created UVW tag, or **None** if the texture type is already UV or if the function failed.
    | If **None** is returned the UVW tag must be retrieved from the object itself.
    
    
    """
    ...

def GetBBox(pObj: BaseObject, mg: Matrix) -> None:
    """    
    Calculates the bounding box of a hierarchy.
    
    :type pObj: c4d.BaseObject
    :param pObj: The root object of a hierarchy.
    :type mg: c4d.Matrix
    :param mg: The transformation matrix for the bounding box.
    :rtype: tuple(:class:`c4d.Vector`, :class:`c4d.Vector`)
    :return: The center and the radius of the bounding box.
    
    
    """
    ...

def FormatNumber(val: Any, format: int, fps: int, bUnit: bool) -> str:
    """    
    Converts *val* to a string.
    
    :type val: any
    :param val: The value to convert to a string. Must be of type float, int or :class:`c4d.BaseTime`.
    :type format: int
    :param format: The format:
    
    .. include:: /consts/FORMAT.rst
    :start-line: 3
    
    :type fps: int
    :param fps: The frames per second, for time values.
    :type bUnit: bool
    :param bUnit: If **True** the unit is included in the formatted string.
    :rtype: str
    :return: The formatted string.
    
    
    """
    ...

def StringToNumber(text: str, format: int, fps: int, lengthunit: int) -> Any:
    """    
    Converts a string to a data value of type float, int or :class:`c4d.BaseTime`.
    
    :type text: str
    :param text: The string to convert to a value.
    :type format: int
    :param format: The format:
    
    .. include:: /consts/FORMAT.rst
    :start-line: 3
    
    :type fps: int
    :param fps: The frames per second, for time values.
    :type lengthunit: int
    :param lengthunit:
    
    .. versionadded:: R18.057
    
    | Can be used to override the units conversion. By default the function uses the document's units.
    | For example a string of "50" results in `0.5` if the document's units are Meters and the unit display setting is centimeters.
    | If *lengthunit* is specified its value will be used instead of the document's units setting.
    
    :rtype: Any
    :return: The converted value.
    
    
    """
    ...

def GetAngle(v1: Vector, v2: Vector) -> float:
    """    
    Calculates the angle of two vectors.
    
    :type v1: c4d.Vector
    :param v1: First position.
    :type v2: c4d.Vector
    :param v2: Second position.
    :rtype: float
    :return: The angle in radians.
    
    
    """
    ...

def RangeMap(value: float, mininput: float, maxinput: float, minoutput: float, maxoutput: float, clampval: bool, curve: Optional[SplineData] = ...) -> float:
    """    
    Map the value of a range to another, optionnaly applying a spline curve. Similiar to the RangeMapper Node in XPresso.
    
    Here are several examples:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/rangemap.py
    :language: python
    
    :type value: float
    :param value: The value to map.
    :type mininput: float
    :param mininput: The minimum input.
    :type maxinput: float
    :param maxinput: The maximum input.
    :type minoutput: float
    :param minoutput: The minimum output.
    :type maxoutput: float
    :param maxoutput: The maximum output.
    :type clampval: bool
    :param clampval: Pass **True** to clamp the value in the range [*minoutput*, *maxoutput*].
    :type curve: c4d.SplineData
    :param curve: The optional curve to use.
    
    
    """
    ...

def DegToRad(d: Any) -> float:
    """    
    Convert a degrees value into radians.
    
    .. versionadded:: R18.039
    
    :type r: number
    :param r: Input value in degrees.
    :rtype: number
    :return: Converted value in radians.
    
    
    """
    ...

def Rad(d: Any) -> float:
    """    
    .. deprecated:: R18.039
    
    Use :func:`DegToRad` instead for better understanding of code.
    
    Convert a degrees value into radians.
    
    
    :type r: number
    :param r: Input value in degrees.
    :rtype: number
    :return: Converted value in radians.
    
    
    """
    ...

def RadToDeg(r: float) -> float:
    """    
    Convert a radians value into degrees.
    
    .. versionadded:: R18.039
    
    :type r: number
    :param r: Input value in radians.
    :rtype: number
    :return: Converted value in degrees.
    
    
    """
    ...

def Deg(r: float) -> float:
    """    
    .. deprecated:: R18.039
    
    Use :func:`RadToDeg` instead for better understanding of code.
    
    Convert a radians value into degrees.
    
    :type r: number
    :param r: Input value in radians.
    :rtype: number
    :return: Converted value in degrees.
    
    
    """
    ...

def MixVec(v1: Vector, v2: Vector, t: float) -> Vector:
    """    
    Mixes the two vectors together, such as mixing two colours.
    
    :type v1: c4d.Vector
    :param v1: Vector to mix.
    :type v2: c4d.Vector
    :param v2: Vector to mix.
    :type t: number
    :param t: Mix amount: `0` < *t* < `1.0`.
    :rtype: c4d.Vector
    :return: The mixed vector.
    
    
    """
    ...

def MixNum(v1: float, v2: float, t: float) -> float:
    """    
    Returns a mixed value of v1 and v2 using the parameter t, as calculated by *v1+(v2-v1)*t*.
    
    :type v1: float
    :param v1: Value to mix.
    :type v2: float
    :param v2: Value to mix.
    :type t: number
    :param t: Mix amount: `0` < *t* < `1.0`.
    :rtype: float
    :return: Mix amount, with *0 <= t <= 1.0*.
    
    
    """
    ...

def Clamp(a: float, b: float, x: float) -> float:
    """    
    Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.
    
    .. note:: The order of parameters are different to Peachey's definition.
    
    :type a: number
    :param a: The float value.
    :type b: number
    :param b: The float value.
    :type x: number
    :param x: The float value.
    :rtype: float
    :return: The clamped value.
    
    
    """
    ...

def ClampValue(x: float, a: float, b: float) -> float:
    """    
    Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.
    
    .. versionadded:: R15.037
    
    .. note::
    
    The order of parameters are the same to Peachey's definition.
    
    :type x: number
    :param x: The float value.
    :type a: number
    :param a: The float value.
    :type b: number
    :param b: The float value.
    :rtype: float
    :return: The clamped value.
    
    
    """
    ...

def Step(a: float, b: float) -> float:
    """    
    Returns 1.0 if *b* is greater than or equal to *a*, else 0.0.
    
    :type a: number
    :param a: The float value.
    :type b: number
    :param b: The float value.
    :rtype: float
    :return: The step value (1.0 or 0.0).
    
    
    """
    ...

def Smoothstep(a: float, b: float, x: float) -> float:
    """    
    Returns *0.0* if *x* is less than *a* and *1.0* if *x* is greater than *b*, else returns *x* mapped on the range [a,b] (a number between 0.0 and 1.0). The mapping is smoothed using an ease-in/ease-out curve.
    
    :type a: float
    :param a: The float value.
    :type b: float
    :param b: The float value.
    :type x: float
    :param x: The float value.
    :rtype: float
    :return: The smoothed value.
    
    
    """
    ...

def Boxstep(a: float, b: float, x: float) -> float:
    """    
    Returns 0.0 if *x* is less than *a* and 1.0 if *x* is greater than *b*, else returns *x* mapped on the range *[a,b]* (*a* number between 0.0 and 1.0).
    
    :type a: number
    :param a: The float value.
    :type b: number
    :param b: The float value.
    :type x: number
    :param x: The float value.
    :rtype: float
    :return: The stepped value.
    
    
    """
    ...

def MatrixRotX(w: float) -> Matrix:
    """    
    Creates a rotation matrix about the X axis.
    
    :type w: float
    :param w: The angle around X.
    :rtype: c4d.Matrix
    :return: The rotation matrix.
    
    
    """
    ...

def MatrixRotY(w: float) -> Matrix:
    """    
    Creates a rotation matrix about the Y axis.
    
    :type w: float
    :param w: The angle around Y.
    :rtype: c4d.Matrix
    :return: The rotation matrix.
    
    
    """
    ...

def MatrixRotZ(w: float) -> Matrix:
    """    
    Creates a rotation matrix about the Z axis.
    
    :type w: float
    :param w: The angle around Z.
    :rtype: c4d.Matrix
    :return: The rotation matrix.
    
    
    """
    ...

def QSlerp(q1: Quaternion, q2: Quaternion, alfa: float) -> Quaternion:
    """    
    Spherical interpolation of the quaternions *q1* and *q2* with the parameter *alfa*.
    
    .. versionadded:: R17.048
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :type alfa: float
    :param alfa: The interpolation parameter. Between `0.0` (*q1*) and `1.0` (*q2*).
    :rtype: c4d.Quaternion
    :return: The interpolated quaternion.
    
    
    """
    ...

def QSquad(q0: Quaternion, q1: Quaternion, q2: Quaternion, q3: Quaternion, alfa: float) -> Quaternion:
    """    
    | Cubic interpolates the quaternions *q1* and *q2* with parameter *alfa* using spherical quadrangle interpolation.
    | *q0* and *q3* are used to provide C1-continuity at the borders (tangents): *q0* = i-1, *q1* = i, *q2* = i+1, *q3*  = i+2
    
    .. versionadded:: R17.048
    
    :type q0: c4d.Quaternion
    :param q0: The first quaternion to provide continuity.
    :type q1: c4d.Quaternion
    :param q1: The first quaternion to interpolate from.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion to interpolate from.
    :type q3: c4d.Quaternion
    :param q3: The second quaternion to provide continuity.
    :type alfa: float
    :param alfa: The interpolation parameter. Between `0.0` (*q1*) and `1.0` (*q2*).
    :rtype: c4d.Quaternion
    :return: The interpolated quaternion.
    
    
    """
    ...

def QBlend(q1: Quaternion, q2: Quaternion, r: Any) -> Quaternion:
    """    
    Linear interpolation of the quaternions *q1* and *q2* with parameter *r*.
    
    .. versionadded:: R17.048
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :type alfa: float
    :param alfa: The blending parameter. Between `0.0` (*q1*) and `1.0` (*q2*).
    :rtype: c4d.Quaternion
    :return: The interpolated quaternion.
    
    
    """
    ...

def QSpline(qn_m1: Quaternion, qn: Quaternion, qn_p1: Quaternion, qn_p2: Quaternion, t: float) -> Quaternion:
    """    
    | Smooth blends the quaternions *qn* and *qn_p1* using spherical spline interpolation with parameter *t*.
    | *qn_m1* (-1) and *qn_p2* (-1+2) are used to provide C1-continuity at the borders (tangents).
    
    .. versionadded:: R17.048
    
    :type qn_m1: c4d.Quaternion
    :param qn_m1: The first quaternion (-1) to provide continuity.
    :type qn: c4d.Quaternion
    :param qn: The first quaternion to interpolate from.
    :type qn_p1: c4d.Quaternion
    :param qn_p1: The second quaternion to interpolate from.
    :type qn_p2: c4d.Quaternion
    :param qn_p2: The second quaternion (+2) to provide continuity.
    :type t: float
    :param t: The blending parameter. Between `0.0` (*qn*) and `1.0` (*qn_p1*).
    :rtype: c4d.Quaternion
    :return: The interpolated quaternion.
    
    
    """
    ...

def QSmoothCubic(qn_m1: Quaternion, qn: Quaternion, qn_p1: Quaternion, t: float) -> Quaternion:
    """    
    | Smooth blends the quaternions *qn* and *qn_p1* using Cubic interpolation with parameter *t*.
    | *qn_m1* (-1) and *qn_p2* (-1+2) are used to provide C1-continuity at the borders (tangents).
    
    .. versionadded:: R18.020
    
    :type qn_m1: c4d.Quaternion
    :param qn_m1: The first quaternion (-1) to provide continuity.
    :type qn: c4d.Quaternion
    :param qn: The first quaternion to interpolate from.
    :type qn_p1: c4d.Quaternion
    :param qn_p1: The second quaternion to interpolate from.
    :type t: float
    :param t: The blending parameter. Between `0.0` (*qn*) and `1.0` (*qn_p1*).
    :rtype: c4d.Quaternion
    :return: The interpolated quaternion.
    
    
    """
    ...

def QNorm(q: Quaternion) -> Quaternion:
    """    
    Gets a normalized copy of quaternion *q*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion to normalize.
    :rtype: c4d.Quaternion
    :return: A normalized copy of *q*.
    
    
    """
    ...

def QMul(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """    
    Calculates the quaternion product of quaternions *q1* and *q2*.
    
    .. versionadded:: R17.048
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :rtype: c4d.Quaternion
    :return: The quaternion product of *q1* and *q2*.
    
    
    """
    ...

def QMulS(q: Quaternion, s: float) -> Quaternion:
    """    
    Calculates the product of quaternion *q* with scalar *s*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion.
    :type s: float
    :param s: The scalar.
    :rtype: c4d.Quaternion
    :return: The product of *q* with *s*.
    
    
    """
    ...

def QAdd(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """    
    Calculates the quaternion addition of quaternions *q1* and *q2*.
    
    .. versionadded:: R17.048
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :rtype: c4d.Quaternion
    :return: The quaternion addition  of *q1* and *q2*.
    
    
    """
    ...

def QSub(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """    
    Calculates the quaternion subtraction of quaternions *q1* and *q2*.
    
    .. versionadded:: R17.048
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :rtype: c4d.Quaternion
    :return: The quaternion subtraction  of *q1* and *q2*.
    
    
    """
    ...

def QInvert(q: Quaternion) -> Quaternion:
    """    
    Calculates the inverse of quaternion *q*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion to invert.
    :rtype: c4d.Quaternion
    :return: The quaternion inverse of q.
    
    
    """
    ...

def QDot(q1: Quaternion, q2: Quaternion) -> float:
    """    
    Calculates the Dot Product between *q1* and *q2*.
    
    .. versionadded:: R18.020
    
    :type q1: c4d.Quaternion
    :param q1: The first quaternion.
    :type q2: c4d.Quaternion
    :param q2: The second quaternion.
    :rtype: float
    :return: The Dot Product of *q1* and *q2*.
    
    
    """
    ...

def QDeriv(q: Quaternion, w: Vector) -> Quaternion:
    """    
    Calculates the derivative of quaternion *q* by vector *w*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion.
    :type w: c4d.Vector
    :param w: The vector.
    :rtype: c4d.Quaternion
    :return: The quaternion derivative of *q* by *w*.
    
    
    """
    ...

def QLogN(q: Quaternion) -> Quaternion:
    """    
    Calculates the natural logarithm of quaternion *q*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion.
    :rtype: c4d.Quaternion
    :return: The natural logarithm of *q*.
    
    
    """
    ...

def QExpQ(q: Quaternion) -> Quaternion:
    """    
    Calculates the exponential of quaternion *q*.
    
    .. versionadded:: R17.048
    
    :type q: c4d.Quaternion
    :param q: The quaternion.
    :rtype: c4d.Quaternion
    :return: The exponential of *q*.
    
    
    """
    ...

def MatrixToRotAxis(m: Matrix) -> List[Any]:
    """    
    Calculates rotation axis and angle from matrix *m*:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/matrixtorotaxis.py
    :language: python
    
    :type m: c4d.Matrix
    :param m: Rotation matrix.
    :rtype: list
    :return: The rotation axis, and the angle.
    
    
    """
    ...

def RotAxisToMatrix(v: Vector, w: float) -> Matrix:
    """    
    Calculate matrix from rotation axis *v* and angle *w*.
    
    :type v: c4d.Vector
    :param v: The axis.
    :type w: float
    :param w: The angle of rotation.
    :rtype: c4d.Matrix
    :return: The rotation matrix.
    
    
    """
    ...

def GetOptimalAngle(hpb_old: Vector, hpb_new: Vector, rotation_order: int) -> Vector:
    """    
    Modify *hpb_new* so that the "distance" to the last angle *hpb_old* is at minimum. This helps to avoid HPB singularity effects.
    
    :type hpb_old: c4d.Vector
    :param hpb_old: The old HPB.
    :type hpb_new: c4d.Vector
    :param hpb_new: The new HPB.
    :type rotation_order: int
    :param rotation_order: The order of rotation:
    
    .. include:: /consts/ROTATIONORDER.rst
    :start-line: 3
    
    :rtype: c4d.Vector
    :return: The optimal angle.
    
    
    """
    ...

def PointLineDistance(p0: Vector, v: Vector, p: Vector) -> Vector:
    """    
    Calculates the distance from a point to a line.
    
    :type p0: c4d.Vector
    :param p0: The starting point of the line.
    :type v: c4d.Vector
    :param v: The line vector.
    :type p: c4d.Vector
    :param p: The point.
    :rtype: c4d.Vector
    :return: Point-line vector.
    
    
    """
    ...

def ReflectRay(v: Vector, n: Vector) -> Vector:
    """    
    Find the ray vector after a reflection about a surface normal.
    
    :type v: c4d.Vector
    :param v: The incoming ray.
    :type n: c4d.Vector
    :param n: The surface normal.
    :rtype: c4d.Vector
    :return: The reflected ray.
    
    
    """
    ...

def CalcSpline(x: float, knots: List[float]) -> float:
    """    
    Calculates the value of a spline at a point.
    
    :type x: float
    :param x: The position on the spline.
    :type knots: list of float
    :param knots: The knots list.
    :rtype: float
    :return: The spline value.
    
    
    """
    ...

def CalcSplineV(x: float, knots: Any) -> Vector:
    """    
    Calculates the value of a spline at a point.
    
    :type x: float
    :param x: The position on the spline.
    :type knots: list of :class:`Vector <c4d.Vector>`
    :param knots: The knots list.
    :rtype: c4d.Vector
    :return: The spline value.
    
    
    """
    ...

def CalcSplinePoint(offset: float, type: int, closed: bool, pcnt: int, padr: Any, tadr: List[Dict[str, Any]]) -> Vector:
    """    
    Calculates a point along a spline curve from a set of points in 3D space.
    
    .. versionadded:: R17.048
    
    :type offset: float
    :param offset: The offset along the spline from `0.0` to `1.0`.
    :type type: int
    :param type: The type of spline. Check out :ref:`spline_type`.
    
    .. include:: /consts/SPLINETYPE.rst
    :start-line: 3
    
    :type closed: bool
    :param closed: Whether the spline is closed or not.
    :type pcnt: int
    :param pcnt: The number of points in the spline.
    :type padr: list of :class:`Vector <c4d.Vector>`
    :param padr: The points array.
    :type tadr: list of tangent(dict)
    :param tadr:
    | The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).
    | A tangent dictionary has to be defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    :rtype: c4d.Vector
    :return: The resulting point calculated from the offset.
    
    
    """
    ...

def CalcSplineTangent(offset: float, type: int, closed: bool, pcnt: int, padr: Any, tadr: List[Dict[str, Any]]) -> Vector:
    """    
    Calculates the tangent of a point along a spline curve from a given set of points and optional tangents.
    
    .. versionadded:: R17.048
    
    :type offset: float
    :param offset: The offset along the spline from `0.0` to `1.0`.
    :type type: int
    :param type: The type of spline. Check out :ref:`spline_type`.
    
    .. include:: /consts/SPLINETYPE.rst
    :start-line: 3
    
    :type closed: bool
    :param closed: Whether the spline is closed or not.
    :type pcnt: int
    :param pcnt: The number of points in the spline.
    :type padr: list of :class:`Vector <c4d.Vector>`
    :param padr: The points array.
    :type tadr: list of tangent(dict)
    :param tadr:
    
    | The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).
    | A tangent dictionary has to be defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    
    :rtype: c4d.Vector
    :return: The resulting tangent (normalized) for the given offset.
    
    
    """
    ...

def CalcSplineInsert(offset: float, type: int, closed: bool, pcnt: int, padr: Any, tadr: List[Dict[str, Any]]) -> None:
    """    
    Calculates data about a point would if it were inserted into the spline at the passed offset.
    
    .. versionadded:: R17.048
    
    :type offset: float
    :param offset: The offset along the spline from `0.0` to `1.0`.
    :type type: int
    :param type: The type of spline. Check out :ref:`spline_type`.
    
    .. include:: /consts/SPLINETYPE.rst
    :start-line: 3
    
    :type closed: bool
    :param closed: Whether the spline is closed or not.
    :type pcnt: int
    :param pcnt: The number of points in the spline.
    :type padr: list of :class:`Vector <c4d.Vector>`
    :param padr: The points array.
    :type tadr: list of tangent(dict)
    :param tadr:
    
    | The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).
    | A tangent dictionary has to be defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    
    :rtype: dict(int, :class:`Vector <c4d.Vector>`, Tangent, :class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
    :return: A dictionary with the following information:
    
    - "pointIndex": The index that the resulting point would be if it were inserted into the spline.
    - "resultPoint": The position of the resulting point.
    - "resultTangent": The spline tangent information of the resulting point. dict('vl': :class:`Vector <c4d.Vector>`,'vr': :class:`Vector <c4d.Vector>`)
    - "leftTangent": The correct new left tangent (`tadr[pointIndex - 1].vr`).
    - "rightTangent": The correct new right tangent (`tadr[pointIndex].vl`).
    
    
    """
    ...

def TransformTangent(newPos: Vector, planeNormal: Vector, position: Vector, tangent: Dict[str, Any], tangentSide: int, flags: int) -> None:
    """    
    Creates a transformed tangent around a point and plane, allowing to directly set the position of one of the tangent handles and automatically rotating the rest of the tangent to match.
    
    .. versionadded:: R17.048
    
    :type newPos: c4d.Vector
    :param newPos: The new position for the tangent handle.
    :type planeNormal: c4d.Vector
    :param planeNormal: The normal of the plane for rotation of the handles.
    :type position: c4d.Vector
    :param position: The position of the center of the tangent being modified.
    :type tangent: dict
    :param tangent:
    | The tangent to modify/derive the resulting tangent from.
    | A tangent dictionary has to be defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    :type tangentSide: int
    :param tangentSide: The handle to modify of the tangent, left, right, or none:
    
    .. include:: /consts/TANGENTSIDE.rst
    :start-line: 3
    
    :type flags: int
    :param flags: The flags for controlling tangent breaking, rotation and scale locking etc.
    
    .. include:: /consts/TANGENTTRANSFORMFLAG.rst
    :start-line: 3
    
    :rtype: dict('vl': :class:`Vector <c4d.Vector>`,'vr': :class:`Vector <c4d.Vector>`)
    :return: The resulting transformed tangent.
    
    
    """
    ...

def CalcSplineMovement(newPos: Vector, offset: float, type: int, splineMg: Matrix, bd: Optional[BaseDraw] = ..., planeNormal: Optional[Vector] = ..., closed: Optional[bool] = ..., lockTangentAngle: Optional[bool] = ..., lockTangentLength: Optional[bool] = ..., breakTangents: Optional[int] = ..., pcnt: Optional[int] = ..., padr: Optional[Any] = ..., tadr: Optional[List[Dict[str, Any]]] = ...) -> None:
    """    
    Moves a point on a spline curve to a user specified new position.
    
    .. versionadded:: R17.048
    
    :type newPos: c4d.Vector
    :param newPos: The new position for the point of the curve at *offset*.
    :type offset: float
    :param offset: The offset to move to the position newPos.
    :type type: int
    :param type: The type of spline to move. Check out :ref:`spline_type`.
    
    .. include:: /consts/SPLINETYPE.rst
    :start-line: 3
    
    :type splineMg: c4d.Matrix
    :param splineMg: The matrix of the spline.
    :type bd: c4d.BaseDraw
    :param bd: The optional basedraw. Can be **None**.
    :type planeNormal: c4d.Vector
    :param planeNormal: The normal for tangent rotation, typically `Vector(0,0,1)`.
    :type closed: bool
    :param closed: The closed state of the spline.
    :type lockTangentAngle: bool
    :param lockTangentAngle: **True** if tangents angle may not be changed by this routine.
    :type lockTangentLength: bool
    :param lockTangentLength: **True** if the tangents length may not be changed by this routine.
    :type breakTangents: int
    :param breakTangents: Set to break the tangents while manipulating the curve if tangents exist:
    
    .. include:: /consts/BREAKTANGENTS.rst
    :start-line: 3
    
    :type pcnt: int
    :param pcnt: The number of points in the spline.
    :type padr: list of :class:`Vector <c4d.Vector>`
    :param padr: The points that describe the spline.
    :type tadr: list of tangent(dict)
    :param tadr:
    
    | The tangents that are used by the spline.
    | A tangent dictionary has to be defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    
    :rtype: tuple(list of :class:`Vector <c4d.Vector>`, list of tangents)
    :return: The resulting lists of points and tangents.
    
    
    """
    ...

def CalcSplineDefaultTangents(type: int, closed: bool, pcnt: int, padr: Any) -> List[Dict[str, Any]]:
    """    
    Calculates the default tangents for the passed points (spline segment) based on the spline type.
    
    .. versionadded:: R17.048
    
    :type type: int
    :param type: The type of spline to move. Check out :ref:`spline_type`.
    
    .. include:: /consts/SPLINETYPE.rst
    :start-line: 3
    
    :type closed: bool
    :param closed: The closed state of the spline.
    :type pcnt: int
    :param pcnt: The number of points in the spline.
    :type padr: list of :class:`Vector <c4d.Vector>`
    :param padr: The points that describe the spline.
    :rtype: list of dict
    :return: The resulting tangents. A tangent dictionary is defined as: dict('vl': :class:`Vector <c4d.Vector>`, 'vr': :class:`Vector <c4d.Vector>`)
    
    
    """
    ...

def BooleanSplines(initialSpline: BaseObject, booleanObjects: List[SplineObject], doc: BaseDocument, bd: BaseDraw, projectionAxis: int, booleanMode: int) -> BaseList2D:
    """    
    Booleans an initial spline object with an array of other spline objects along a passed projection axis (in 2D).
    
    .. versionadded:: R17.048
    
    :type initialSpline: c4d.BaseObject
    :param initialSpline: The original spline object that will have the operations applied to it.
    :type booleanObjects: List[c4d.SplineObject]
    :param booleanObjects: The array of spline objects to boolean with *initialSpline*.
    :type doc: c4d.documents.BaseDocument
    :param doc: The active document that the objects belong to.
    :type bd: c4d.BaseDraw
    :param bd: The active basebraw.
    :type projectionAxis: int
    :param projectionAxis: The projection axis to use:
    
    .. include:: /consts/SPLINEBOOL_AXIS.rst
    :start-line: 3
    
    :type booleanMode: int
    :param booleanMode: The type of boolean to apply:
    
    .. include:: /consts/SPLINEBOOL_MODE.rst
    :start-line: 3
    
    :rtype: c4d.BaseList2D
    :return: The spline object result of the Boolean operation, **None** if there was an error.
    
    
    """
    ...

def RGBToHSV(col: Vector) -> Vector:
    """    
    Converts RGB into the HSV color space and returns the converted value.
    
    :type col: c4d.Vector
    :param col: RGB color.
    :rtype: c4d.Vector
    :return: HSV color.
    
    
    """
    ...

def HSVToRGB(col: Vector) -> Vector:
    """    
    Converts HSV into the RGB color space and returns the converted value.
    
    :type col: c4d.Vector
    :param col: HSV color.
    :rtype: c4d.Vector
    :return: RGB color.
    
    
    """
    ...

def RGBToHSL(col: Vector) -> Vector:
    """    
    Converts RGB into the HSL color space and returns the converted value.
    
    .. versionadded:: R14.014
    
    :type col: c4d.Vector
    :param col: RGB color.
    :rtype: c4d.Vector
    :return: HSL color.
    
    .. note:: If you want the Hue value to be in degree, you have to multiply it yourself.
    
    
    """
    ...

def HSLtoRGB(col: Vector) -> Vector:
    """    
    Converts HSL into the RGB color space and returns the converted value.
    
    .. versionadded:: R14.014
    
    :type col: c4d.Vector
    :param col: HSL color.
    :rtype: c4d.Vector
    :return: RGB color.
    
    
    """
    ...

def VectorEqual(v1: Vector, v2: Vector, epsilon: float) -> bool:
    """    
    Check if vector v1 and v2 are within *epsilon* of each other.
    
    :type v1: c4d.Vector
    :param v1: The first vector.
    :type v2: c4d.Vector
    :param v2: The second vector.
    :type epsilon: float
    :param epsilon: The epsilon value.
    :rtype: bool
    :return: **True** if the vectors are equal.
    
    
    """
    ...

def Bias(b: float, x: float) -> float:
    """    
    Returns the bias as the defined in the book "Texturing and Modeling" by Ebert.
    
    The internal code::
    
    import math
    
    def Bias(b, x):
    return math.pow(x, -math.log(b) / 0.693147180559945)
    
    :type b: number
    :param b: Bias value.
    :type x: number
    :param x: The real value.
    :rtype: float
    :return: The bias.
    
    
    """
    ...

def FCut(a: float, b: float, c: float) -> None:
    """    
    Limit the value of *a* to between *b* and *c*.
    
    :type a: float
    :param a: Value
    :type b: float
    :param b: Lower bound
    :type c: float
    :param c: Upper bound
    
    
    """
    ...

def CutColor(vec: Vector) -> Vector:
    """    
    Limit a color vector between 0.0 and 1.0.
    
    :type vec: c4d.Vector
    :param vec: Bias value.
    :rtype: c4d.Vector
    :return: The limited color vector.
    
    
    """
    ...

def Truncate(x: float) -> float:
    """    
    Limit a color vector between 0.0 and 1.0.
    
    The internal code:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/truncate.py
    :language: python
    
    :type x: number
    :param x: The value to truncate.
    :rtype: float
    :return: The truncated value.
    
    
    """
    ...

def VectorSum(vec: Any) -> float:
    """    
    Sum the vector components.
    
    :type x: c4d.Vector
    :param x: A color
    :rtype: float
    :return: The sum of the components.
    
    
    """
    ...

def VectorGray(vec: Vector) -> float:
    """    
    Sum the vector components and multiply by 1/3.
    
    :type vec: c4d.Vector
    :param vec: A color
    :rtype: float
    :return: The gray value.
    
    
    """
    ...

def VectorAngle(vec1: Vector, vec2: Vector) -> float:
    """    
    Calculates the angle between two vectors in radians.
    
    :type vec1: c4d.Vector
    :param vec1: The first vector.
    :type vec2: c4d.Vector
    :param vec2: The second vector.
    :rtype: float
    :return: The angle in radians.
    
    
    """
    ...

def VectorMin(vec: Vector) -> float:
    """    
    Find the minimum component of the vector.
    
    :type vec: c4d.Vector
    :param vec: The vector to find the minimum component of.
    :rtype: float
    :return: The minimum component of the vector.
    
    
    """
    ...

def VectorMax(vec: Vector) -> float:
    """    
    Find the maximum component of the vector.
    
    :type vec: c4d.Vector
    :param vec: The vector to find the maximum component of.
    :rtype: float
    :return: The maximum component of the vector.
    
    
    """
    ...

def MatrixMove(vec: Vector) -> Matrix:
    """    
    Create a translation matrix.
    
    :type vec: c4d.Vector
    :param vec: The translation vector.
    :rtype: c4d.Matrix
    :return: The translation matrix.
    
    
    """
    ...

def MatrixScale(s: Vector) -> Matrix:
    """    
    Create a scaling matrix.
    
    :type s: c4d.Vector
    :param s: The scaling vector for the axes.
    :rtype: c4d.Matrix
    :return: The scaling matrix.
    
    
    """
    ...

def VectorToHPB(p: Vector) -> Vector:
    """    
    Calculate euler angles from the vector *p*. The bank is always set to 0.0.
    
    :type p: c4d.Vector
    :param p: The vector to find the HPB for.
    :rtype: c4d.Vector
    :return: The rotation HPB.
    
    
    """
    ...

def MatrixToHPB(m: Matrix, order: Optional[int] = ...) -> Vector:
    """    
    Calculate euler angles from the matrix *m*.
    
    :type m: c4d.Matrix
    :param m: The rotation matrix.
    :type order: int
    :param order: The order of rotation:
    
    .. include:: /consts/ROTATIONORDER.rst
    :start-line: 3
    
    :rtype: c4d.Vector
    :return: The HPB.
    
    
    """
    ...

def HPBToMatrix(hpb: Vector, order: Optional[int] = ...) -> Matrix:
    """    
    Construct matrix from the euler angles *hpb*.
    
    :type hpb: c4d.Vector
    :param hpb: The input HPB.
    :type order: int
    :param order: The order of rotation:
    
    .. include:: /consts/ROTATIONORDER.rst
    :start-line: 3
    
    :rtype: c4d.Matrix
    :return: The rotation matrix.
    
    
    """
    ...

def CalcLOD(val: int, lod: float, min: int, max: int) -> None:
    """    
    This is a helper function to modify a user chosen subdivision value.
    
    For example:
    
    .. code-block:: python
    
    sub = c4d.utils.CalcLOD(op[TUBEOBJECT_SUB, 1], hh["lod"], 1, 1000)
    
    :type val: int
    :param val: The user chosen lod value.
    :type lod: float
    :param lod: The LOD value.
    :type min: int
    :param min: The minimum lod.
    :type max: int
    :param max: The maximum lod.
    
    
    """
    ...

def CompareFloatTolerant(a: float, b: float) -> bool:
    """    
    Compares if two floats are close to each other on a bit basis (rather than a fixed epsilon).
    
    :type a: float
    :param a: The first parameter.
    :type b: float
    :param b: The second parameter.
    :rtype: bool
    :return: **True** if *a* and *b* are sufficiently close to each other, otherwise **False**.
    
    
    """
    ...

def SinCos(w: float) -> List[Any]:
    """    
    Get sine and cosine of w:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/sincos.py
    :language: python
    
    :type w: float
    :param w: Value.
    :rtype: list
    :return: Sine and Cosine.
    
    
    """
    ...

def TransformColor(input: Vector, colortransformation: int) -> Vector:
    """    
    Transforms a color from one color profile to another.
    
    :type input: c4d.Vector
    :param input: The color to transform.
    :type colortransformation: int
    :param colortransformation: Transformation mode:
    
    .. include:: /consts/COLORSPACETRANSFORMATION.rst
    :start-line: 3
    
    :rtype: c4d.Vector
    :return: The transformed color.
    
    
    """
    ...

def CalculateTranslationScale(src: Union[BaseDocument, UnitScaleData], dst: Union[BaseDocument, UnitScaleData]) -> float:
    """    
    Calculates the scale between *src* and *dst*.
    
    .. note::
    
    Both *src* and *dst* have to be of the same type: either :class:`c4d.documents.BaseDocument` or :class:`c4d.UnitScaleData`.
    
    :type src: Union[c4d.documents.BaseDocument, c4d.UnitScaleData]
    :param src: The source document or unit scale data.
    :type dst: Union[c4d.documents.BaseDocument, c4d.UnitScaleData]
    :param dst: The destination document or unit scale data.
    :rtype: float
    :return: The scale.
    
    
    """
    ...

def SphereLineIntersection(linePoint1: Vector, linePoint2: Vector, sphereCenter: Vector, sphereRadius: float) -> None:
    """    
    Calculates the intersection points between a line and a sphere in 3D space.
    
    .. versionadded:: R16.021
    
    :type linePoint1: c4d.Vector
    :param linePoint1: The first point of the line.
    :type linePoint2: c4d.Vector
    :param linePoint2: The second point of the line.
    :type sphereCenter: c4d.Vector
    :param sphereCenter: The center of the sphere.
    :type sphereRadius: float
    :param sphereRadius: The radius of the sphere.
    :rtype: tuple(bool, float, float, :class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
    :return: A tuple with the following information:
    
    1. bool: **True** if the line segment intersected the sphere, otherwise **False**.
    2. float: The first intersection point (lowest) as an offset between *linePoint1* and *linePoint2*.
    3. float: The second intersection point (highest) as an offset between *linePoint1* and *linePoint2*.
    4. :class:`Vector <c4d.Vector>`: The actual 3D point where the line first intersects (enters) the sphere.
    5. :class:`Vector <c4d.Vector>`: The actual 3D point where the line subsequently intersects (exits) the sphere.
    
    
    """
    ...

def CircleLineIntersection(linePoint1: Vector, linePoint2: Vector, circleCenter: Vector, circleRadius: float) -> None:
    """    
    Calculates the intersection points between a line and a circle in 2D space (although `Z` will also be calculated on the resulting hit points).
    
    .. versionadded:: R16.021
    
    :type linePoint1: c4d.Vector
    :param linePoint1: The first point of the line.
    :type linePoint2: c4d.Vector
    :param linePoint2: The second point of the line.
    :type circleCenter: c4d.Vector
    :param circleCenter: The center of the circle.
    :type circleRadius: float
    :param circleRadius: The radius of the circle.
    :rtype: tuple(bool, float, float, :class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
    :return: A tuple with the following information:
    
    1. bool: **True** if the line segment intersected the circle, otherwise **False**.
    2. float: The first intersection point (lowest) as an offset between *linePoint1* and *linePoint2*.
    3. float: The second intersection point (highest) as an offset between *linePoint1* and *linePoint2*.
    4. :class:`Vector <c4d.Vector>`: The actual 3D point where the line first intersects (enters) the circle, `Z` may also be calculated.
    5. :class:`Vector <c4d.Vector>`: The actual 3D point where the line subsequently intersects (exits) the circle, `Z` may also be calculated.
    
    
    """
    ...

def PointLineSegmentDistance(segmentPoint1: Vector, segmentPoint2: Vector, pos: Vector) -> None:
    """    
    Calculates the distance from a point to a line segment between two points.
    
    .. versionadded:: R17.048
    
    :type segmentPoint1: c4d.Vector
    :param segmentPoint1: The line segment first point.
    :type segmentPoint2: c4d.Vector
    :param segmentPoint2: The line segment second point.
    :type pos: c4d.Vector
    :param pos: The point to test against the line segment.
    :rtype: tuple(float, :class:`Vector <c4d.Vector>`, float)
    :return: A tuple with the following information:
    
    1. The distance between the point and the line segment.
    2. The intersection point on the segment.
    3. The offset along the segment of the intersection point.
    
    
    """
    ...

def PointLineSegmentDistance2D(segmentPoint1: Vector, segmentPoint2: Vector, pos: Vector) -> None:
    """    
    Calculates the distance from a point to a line segment between two points in 2D ignoring the Z value.
    
    .. versionadded:: R17.048
    
    :type segmentPoint1: c4d.Vector
    :param segmentPoint1: The line segment first point.
    :type segmentPoint2: c4d.Vector
    :param segmentPoint2: The line segment second point.
    :type pos: c4d.Vector
    :param pos: The point to test against the line segment.
    :rtype: tuple(float, :class:`Vector <c4d.Vector>`, float)
    :return: A tuple with the following information:
    
    1. The distance between the point and the line segment.
    2. The intersection point on the segment.
    3. The offset along the segment of the intersection point.
    
    
    """
    ...

def InitBakeTexture(doc: BaseDocument, textags: TextureTag, texuvws: UVWTag, destuvws: UVWTag, bc: BaseContainer, th: Optional[BaseThread] = ...) -> None:
    """    
    Initializes a bake operation of a single tag for :func:`BakeTexture`.
    
    .. versionadded:: R18.011
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type textags: c4d.TextureTag
    :param textags: The texture tag(s) to bake. Must be assigned to an object.
    :type texuvws: c4d.UVWTag
    :param texuvws: The UVW tag(s) to bake. Must be valid if UVW projection is selected in the texture tag(s), ignored otherwise.
    :type destuvws: c4d.UVWTag
    :param destuvws: The destination UVW tag for the bake. If not **None**, the current projection is transformed into the UVW tag.
    :type bc: c4d.BaseContainer
    :param bc: The bake settings:
    
    .. include:: /consts/BAKE_TEX.rst
    :start-line: 3
    
    :type th: c4d.threading.BaseThread
    :param th: The optional thread. Can be **None**. New in version R18.039.
    :rtype: tuple(:class:`BaseDocument <c4d.documents.BaseDocument>`, int)
    :return: A tuple with the following information:
    
    | :class:`c4d.documents.BaseDocument`: The document for the bake to use for the call to :func:`BakeTexture`.
    | int: The error result. *BAKE_TEX_ERR_NONE* if successful, otherwise one of these errors:
    
    .. include:: /consts/BAKE_TEX_ERR.rst
    :start-line: 3
    
    
    """
    ...

def BakeTexture(doc: BaseDocument, data: BaseContainer, bmp: BaseBitmap, th: BaseThread, hook: Callable[..., Any]) -> int:
    """    
    Bakes the texture(s) specified by the last :func:`InitBakeTexture()` call into *bmp*.
    
    .. versionadded:: R18.011
    
    :type doc: c4d.documents.BaseDocument
    :param doc: The document.
    :type data: c4d.BaseContainer
    :param data: The bake settings:
    
    .. include:: /consts/BAKE_TEX.rst
    :start-line: 3
    
    :type bmp: c4d.bitmaps.BaseBitmap
    :param bmp: The bitmap to bake to.
    :type th: c4d.threading.BaseThread
    :param th: The current thread. Can be **None**.
    :type hook: function(*dict*)
    :param hook: The bake progress hook callback function. This function gets passed a dictionary with the following information:
    
    .. include:: /consts/BakeProgressHook.rst
    :start-line: 3
    
    If the state is *BAKE_STATE_RESIZENOTIFY*, the return value has to be a bool to set the result of the resize operation. Otherwise the hook must return **None**.
    
    :rtype: int
    :return: *BAKE_TEX_ERR_NONE* if successful, otherwise one of these errors:
    
    .. include:: /consts/BAKE_TEX_ERR.rst
    :start-line: 3
    
    
    """
    ...

