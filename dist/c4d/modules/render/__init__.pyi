from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import Vector, BaseList2D
from c4d.documents import BaseDocument


class BaseVolumeData(object):
    ...

class VolumeData(BaseVolumeData):
    def GetObjCount(self) -> int:
        """    
        Returns the overall number of objects.
        
        :rtype: int
        :return: The total number of objects.
        
        
        """
        ...
    
    def GetSkyCount(self) -> int:
        """    
        Returns the number of skies.
        
        :rtype: int
        :return: The number of skies.
        
        
        """
        ...
    
    def GetCurrentCPU(self) -> int:
        """    
        Returns the current CPU on which the shader is executed.
        
        :rtype: int
        :return: The running CPU id.
        
        
        """
        ...
    
    def GetCPUCount(self) -> int:
        """    
        Returns the CPU count the renderer is utilizing.
        
        :rtype: int
        :return: The number of CPUs.
        
        
        """
        ...
    
    def OutOfMemory(self) -> None:
        """    
        | Notify Cinema 4D that a (severe) out-of-memory condition occurred.
        | Cinema 4D will stop as soon as possible, but there is no guarantee when exactly.
        | It is possible that your shader could still be called several times, so it has to be programmed to handle this and to be crash-proof.
        
        
        """
        ...
    
    def SkipRenderProcess(self) -> None:
        """    
        Skips the render process. (Useful for custom renderers.)
        
        
        """
        ...
    
    def ScreenToCamera(self, p: Vector) -> Vector:
        """    
        Transform screen to camera coordinates. During QTVR rendering same point is returned.
        
        :type p: c4d.Vector
        :param p: The screen coordinate.
        :rtype: c4d.Vector
        :return: The camera coordinate.
        
        
        """
        ...
    
    def CameraToScreen(self, p: Vector) -> Vector:
        """    
        Transform camera to screen coordinates. During QTVR rendering same point is returned.
        
        :type p: c4d.Vector
        :param p: The camera coordinate.
        :rtype: c4d.Vector
        :return: The screen coordinate.
        
        
        """
        ...
    
    def StatusSetText(self, str: str) -> None:
        """    
        Set the status bar text during initialization of your shader or videopost effect.
        
        .. note::
        
        If an empty string is passed the status bar will be cleared.
        
        :type str: str
        :param str: The status text to display.
        
        
        """
        ...
    
    def StatusSetBar(self) -> None:
        """    
        Set the progress bar during initialization of your shader or videopost effect.
        
        .. note::
        
        The value passed will only be displayed if it is bigger than the previous one. To reset the bar call *StatusSetText* ("").
        
        
        """
        ...
    
    def StatusSetSpinMode(self, on: bool) -> None:
        """    
        Set the render progress bar spinning. Use this to indicate that your plugin is still processing even if the progress bar is not increasing.
        
        :type on: bool
        :param on: **True** to set the progress bar spinning, **False** to stop it.
        
        
        """
        ...
    
    def GetLightCount(self) -> int:
        """    
        Returns the overall number of lights.
        
        :rtype: int
        :return: The number of lights.
        
        
        """
        ...
    
    def GetLight(self, index: int) -> Any:
        """    
        Get the given light source.
        
        :type index: int
        :param index: The index of the light source to return.
        :rtype: ptr
        :return: The light source.
        
        
        """
        ...
    
    def CalcArea(self, light: Any, nodiffuse: bool, nospecular: bool, specular_exponent: float, ray_vector: Vector, p: Vector, bumpn: Vector, orign: Vector, raybits: int, ignoreLightColor: bool) -> None:
        """    
        | If you code custom illumination models (e.g. different specular function) you can do this for standard lightsources easily.
        | For area lights you'll usually want to fall back to the default illumination model though, as otherwise you'd have to rebuild the sample code of area lights!
        
        :type light: ptr
        :param light: The area light to calculate.
        :type nodiffuse: bool
        :param nodiffuse: **True** if the diffuse value should not be calculated, otherwise **False**.
        :type nospecular: bool
        :param nospecular: **True** if the specular value should not be calculated, otherwise **False**.
        :type specular_exponent: float
        :param specular_exponent: Specular exponent to use.
        :type ray_vector: c4d.Vector
        :param ray_vector: Ray vector.
        :type p: c4d.Vector
        :param p: The surface point.
        :type bumpn: c4d.Vector
        :param bumpn: The bump normal.
        :type orign: c4d.Vector
        :param orign: The original normal.
        :type raybits: int
        :param raybits: The ray bits:
        
        .. include:: /consts/RAYBIT.rst
        :start-line: 3
        
        :type ignoreLightColor: bool
        :param ignoreLightColor:
        
        .. versionadded:: R20
        
        **True** to ignore the light color into the result, otherwise **False**.
        
        :rtype: tuple(:class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
        :return: The diffuse and specular components.
        
        
        """
        ...
    
    def CalcShadow(self, l: Any, p: Vector, bumpn: Vector, phongn: Vector, orign: Vector, rayv: Vector, transparency: bool, hitid: Any, raybits: int) -> Vector:
        """    
        Compute a shadow.
        
        :type l: ptr
        :param l: The illuminating light source.
        :type p: c4d.Vector
        :param p: The point in global coordinates.
        :type bumpn: c4d.Vector
        :param bumpn: The bump normal.
        :type phongn: c4d.Vector
        :param phongn: The phong normal.
        :type orign: c4d.Vector
        :param orign: The original normal.
        :type rayv: c4d.Vector
        :param rayv: The ray vector.
        :type transparency: bool
        :param transparency: **True** if transparencies/alphas for inbetween objects should be evaluated.
        :type hitid: ptr
        :param hitid: The global RayHitID for the surface intersection (to avoid self shadowing), or RayHitID() if you are not on a surface or do not wish to make use of this avoidance.
        :type raybits: int
        :param raybits: The ray bits:
        
        .. include:: /consts/RAYBIT.rst
        :start-line: 3
        
        :rtype: c4d.Vector
        :return: The returned shadow value. If there is no shadow, 0.0 will be returned. 1.0 is the maximum shadow value for each component.
        
        """
        ...
    
    def IlluminanceAnyPoint(self, p: Vector, flags: int, raybits: int) -> Vector:
        """    
        | Calculates the light intensity for a given point *p*.
        | This routine can calculate the illumination for any point in space and is widely used for transparent volumetric shaders (gases, clouds etc.).
        
        :type p: c4d.Vector
        :param p: The point in global coordinates.
        :type raybits: c4d.Vector
        :param raybits: The global coordinate point to calculate the illumination for.
        :type flags: int
        :param flags: The illuminate flags:
        
        .. include:: /consts/ILLUMINATEFLAGS.rst
        :start-line: 3
        
        :type raybits: int
        :param raybits: The ray bits:
        
        .. include:: /consts/RAYBIT.rst
        :start-line: 3
        
        :rtype: c4d.Vector
        :return: The returned color.
        
        .. note::
        
        The returned color components can exceed values of 1.0!
        
        
        """
        ...
    
    def IlluminateSurfacePoint(self, rl: Any, p: Vector, bumpn: Vector, phongn: Vector, orign: Vector, ray_vector: Vector, flags: int, hitid: Any, raybits: int, cosine_cutoff: bool) -> Tuple[Vector, Vector]:
        """    
        Calculates the intensity of incoming light for a given light and surface point.
        
        .. note::
        
        Used for custom illumination models.
        
        :type rl: PyCObject
        :param rl: The illuminating light.
        :type p: c4d.Vector
        :param p: The surface point.
        :type bumpn: c4d.Vector
        :param bumpn: The bump normal.
        :type phongn: c4d.Vector
        :param phongn: The phong normal.
        :type orign: c4d.Vector
        :param orign: The original normal.
        :type ray_vector: c4d.Vector
        :param ray_vector: The ray vector.
        :type flags: int
        :param flags: The illuminate flags:
        
        .. include:: /consts/ILLUMINATEFLAGS.rst
        :start-line: 3
        
        :type hitid: PyCObject
        :param hitid: The global RayHitID.
        :type raybits: int
        :param raybits: The ray bits:
        
        .. include:: /consts/RAYBIT.rst
        :start-line: 3
        
        :type cosine_cutoff: bool
        :param cosine_cutoff: **True** if cosine cut-off should be used, otherwise **False**.
        :rtype: Tuple(c4d.Vector, c4d.Vector)
        :return: A tuple with the color result for the calculation and the light to point vector.
        
        
        """
        ...
    
    def CalcVisibleLight(self, ray: Vector, maxdist: float) -> None:
        """    
        Returns the mixed color of all visible lights on a given ray span.
        
        :type ray: c4d.Vector
        :param ray: The ray span.
        :type maxdist: float
        :param maxdist: The maximum distance for the lights.
        :rtype: tuple(:class:`Vector <c4d.Vector>`, :class:`Vector <c4d.Vector>`)
        :return: The mixed color of the lights and a value indicating if some light sources have a dust effect (!= 0 in this case).
        
        
        """
        ...
    
    def GetRS(self, hitid: Any, p: Vector) -> Tuple[bool, float, float]:
        """    
        | Calculates the R/S parameters for a point.
        |
        | If you want to calculate weighted data (e.g. based upon a color for each polygon point) you can do this the following way:
        
        .. code-block:: python
        
        r, s = GetRS(hitid, p)
        result = [color a] * (1.0-r-s) + [color d]*r + [color c]*s
        
        :type hitid: ptr
        :param hitid: The global RayHitID.
        :type p: c4d.Vector
        :param p: The point.
        :rtype: tuple(bool, float, float)
        :return:
        
        | If the polygon is a quadrangle then the first value holds True for the second part (a-c-d) of the quadrangle or False for the first part (a-b-c). If the polygon is a triangle then this is the same as the first part of a quadrangle (a-b-c).
        | The 2nd and 3rd values are the R and S parameters for point *p*.
        
        
        """
        ...
    
    def GetWeights(self, hitid: Any, p: Vector) -> Tuple[float, float, float, float]:
        """    
        | Returns barycentric coordinates for a point on the surface of a polygon.
        | Cinema 4D uses enhanced interpolation routines for quadrangles, so you'll get a higher quality using it instead of considering a quadrangle as two triangles.
        | The routine works for any type of polygon, including triangles and non-coplanar quadrangles.
        
        .. note::
        
        | The function returns a tuple with the weight factors for the global polygon with ID *hitid* at *p*.
        | Works similar to :meth:`GetRS`, but has a higher quality.
        
        :type hitid: ptr
        :param hitid: The global RayHitID.
        :type p: c4d.Vector
        :param p: Point on polygon.
        :rtype: tuple(float, float, float, float)
        :return: A tuple with the respective weight factors for points A, B, C and D.
        
        
        """
        ...
    
    def GetSmoothedNormal(self, hitid: Any, p: Vector) -> Vector:
        """    
        Returns the phong normal for a point.
        
        :type hitid: ptr
        :param hitid: The global RayHitID.
        
        .. note::
        
        Must be a valid RayHitID.
        
        :type p: c4d.Vector
        :param p: The point for the phong normal.
        
        .. note::
        
        The point must be within the surface boundaries of the polygon.
        
        :rtype: c4d.Vector
        :return: The phong normal.
        
        
        """
        ...
    
    def GetXY(self) -> Tuple[int, int, int]:
        """    
        Returns the current X/Y pixel position in render resolution. Render resolution is the screen resolution multiplied by 'scale'.
        
        :rtype: tuple(int, int, int)
        :return: The X, Y pixel positions and render scale.
        
        .. note::
        
        X/scale and Y/scale is the screen position.
        
        
        """
        ...
    
    def SetXY(self, x: float, y: float) -> None:
        """    
        Sets the current X/Y pixel position in render resolution. Render resolution is the screen resolution multiplied by 'scale'.
        
        .. note::
        
        X/scale and Y/scale is the screen position.
        
        .. note::
        
        Some Shaders use the screen pixel position. Plugins (like the Baker for instance) can change this position without having to render an image.
        
        :type x: float
        :param x: The X pixel position to set.
        :type y: float
        :param y: The Y pixel position to set.
        
        
        """
        ...
    
    def CalcFgBg(self, foreground: bool, x: int, y: int, subx: int, suby: int) -> None:
        """    
        Calculates the foreground or background color and alpha at (*x*, *y*).
        
        :type foreground: bool
        :param foreground: **True** to calculate the foreground color. Otherwise the background color is calculated.
        :type x: int
        :param x: X coordinate.
        :type y: int
        :param y: Y coordinate.
        :type subx: int
        :param subx: Sub pixel X position. (0 <= subx <= 15)
        :type suby: int
        :param suby: Sub pixel Y position. (0 <= suby <= 15)
        :rtype: tuple(:class:`Vector <c4d.Vector>`, float)
        :return: The background/foreground color and alpha.
        
        
        """
        ...
    
    def GetLightFalloff(self) -> None:
        """    
        Calculate the light falloff function (light intensity for a distance).
        
        
        """
        ...
    
    def GetRay(self, x: float, y: float, ray: Ray) -> None:
        """    
        Generate the view ray for a position.
        
        .. note::
        
        This function does not set :attr:`Ray.pp` [0..2], :attr:`Ray.vv` [0..2], :attr:`Ray.transport` and :attr:`Ray.ior`.
        
        :type x: float
        :param x: The X position for the view ray in screen space coordinates.
        :type y: float
        :param y: The Y position for the view ray in screen space coordinates.
        :type ray: c4d.modules.render.Ray
        :param ray: The view ray.
        
        
        """
        ...
    
    def GetVideoPost(self, nth: Any) -> BaseList2D:
        """    
        Returns the n-th video post effect for this render process.
        
        :type int: int
        :param int: nth	The nth index of the videopost effect.
        :rtype: c4d.BaseList2D
        :return: The video post, or **None** if the index is too large.
        
        
        """
        ...
    
    def FindVideoPost(self, id: int) -> BaseList2D:
        """    
        Returns a video post effect for this render process by ID.
        
        :type id: int
        :param id: The video post effect ID.
        :rtype: c4d.BaseList2D
        :return: The found video post, or **None** if it doesn't exist.
        
        
        """
        ...
    
    def Init(self, from_: VolumeData) -> None:
        """    
        Initializes this :class:`VolumeData <c4d.modules.render.VolumeData>` object with the data from the *from* object.
        
        .. note::
        
        Only the most essential parts are copied over, including the render instance.
        
        :type from_: c4d.modules.render.VolumeData
        :param from_: Source object.
        
        
        """
        ...
    
    def CopyTo(self, dst: VolumeData) -> None:
        """    
        Copy this to another :class:`VolumeData <c4d.modules.render.VolumeData>`.
        
        :type dst: c4d.modules.render.VolumeData
        :param dst: The destination VolumeData.
        
        
        """
        ...
    

class Ray(object):
    ...

class InitRenderStruct(object):
    def __init__(self, doc: Optional[BaseDocument] = ...) -> None:
        """    
        Initializes a new :class:`InitRenderStruct <c4d.modules.render.InitRenderStruct>`, optionally from *doc* :class:`BaseDocument <c4d.documents.BaseDocument>` if passed.
        
        .. versionadded:: R18.020
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The optional document to initialize with.
        :rtype: c4d.modules.render.InitRenderStruct
        :return: A new :class:`InitRenderStruct <c4d.modules.render.InitRenderStruct>`.
        
        
        """
        ...
    

class ChannelData(object):
    def __init__(self, t_vd: BaseVolumeData) -> None:
        """    
        Initializes a new channel data, optionally from *t_vd* :class:`BaseVolumeData <c4d.modules.render.BaseVolumeData>` if passed.
        
        :type t_vd: c4d.modules.render.BaseVolumeData
        :param t_vd: The volume data to take :attr:`p`, :attr:`n` and :attr:`d` from.
        :rtype: c4d.modules.render.ChannelData
        :return: A new channel data.
        
        
        """
        ...
    

