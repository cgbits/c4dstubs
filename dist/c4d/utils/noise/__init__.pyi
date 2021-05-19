from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseContainer, Vector


class C4DNoise(object):
    def __init__(self, seed: int) -> None:
        """    
        :type seed: int
        :param seed: Noise seed.
        :rtype: c4d.utils.noise.C4DNoise
        :return: A new noise object.
        
        
        """
        ...
    
    @staticmethod
    def CreateMenuContainer(bIncludeNone: bool) -> BaseContainer:
        """    
        Creates a menu container with the different noise options available:
        
        .. literalinclude:: /../../doc.python.code/c4d/utils/noise/c4dnoise/createmenucontainer.py
        :language: python
        
        :type bIncludeNone: bool
        :param bIncludeNone: Include the none option.
        :rtype: c4d.BaseContainer
        :return: Generated noise menu.
        
        
        """
        ...
    
    @staticmethod
    def HasOctaves(t: int) -> bool:
        """    
        Checks if a certain noise type supports the octaves parameter.
        
        :type t: int
        :param t: Noise type.
        :rtype: bool
        :return: **True** if octaves is supported, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def HasCycles(t: int) -> bool:
        """    
        Checks if a certain noise type supports the cycles parameter.
        
        :type t: int
        :param t: Noise type.
        :rtype: bool
        :return: **True** if cycles is supported, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def HasAbsolute(t: int) -> bool:
        """    
        Checks if a certain noise type supports the absolute parameter.
        
        :type t: int
        :param t: Noise type.
        :rtype: bool
        :return: **True** if absolute is supported, otherwise **False**.
        
        
        """
        ...
    
    @staticmethod
    def EvaluateSampleOffset(type: int, rOctaves: float, rDelta: float) -> float:
        """    
        Evaluates the sample offset.
        
        :type type: int
        :param type: Noise type.
        :type rOctaves: float
        :param rOctaves: Number of octaves.
        :type rDelta: float
        :param rDelta: Delta.
        :rtype: float
        :return: The sample offset.
        
        
        """
        ...
    
    def InitFbm(self, lMaxOctaves: int, rLacunarity: float, h: float) -> bool:
        """    
        Initializes fractal brownian motion.
        
        :type lMaxOctaves: int
        :param lMaxOctaves: The maximum octave.
        :type rLacunarity: float
        :param rLacunarity: This parameter controls the scale of each successive fractal overlay.
        :type h: float
        :param h: H-Parameter
        :rtype: bool
        :return: Initializes fractal brownian motion
        
        
        """
        ...
    
    def Noise(self, t: int, two_d: bool, p: Vector, time: float, octaves: float, absolute: bool, sampleRad: float, detailAtt: float, t_repeat: int) -> float:
        """    
        Samples a 2D or 3D noise.
        
        :type t: int
        :param t:  The noise **Type:** :doc:`/types/noise`
        
        .. note::
        
        Please use :meth:`InitFbm` before you use one of the following noise types:  NOISE_ZADA, NOISE_DISPL_VORONOI, NOISE_OBER, NOISE_FBM, NOISE_BUYA.
        
        :type two_d: bool
        :param two_d: **True** for 2D Sampling, **False** for 3D Sampling
        :type p: c4d.Vector
        :param p: Noise coordinate.
        :type time: float
        :param time: Time.
        :type octaves: float
        :param octaves: Octaves, if supported. See :meth:`HasOctaves`
        :type absolute: bool
        :param absolute: Absolute value, if supported. See :meth:`HasAbsolute`
        :type sampleRad: float
        :param sampleRad: Sample radius.
        :type detailAtt: float
        :param detailAtt: Detail attenuation.
        :type t_repeat: int
        :param t_repeat: Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller repeat the noise will repeat at an earlier time.
        :rtype: float
        :return: Noise sample.
        
        
        """
        ...
    
    def SNoise(self, p: Vector, lRepeat: int, t: float) -> float:
        """    
        Generate a periodic signed noise value.
        
        :type p: c4d.Vector
        :param p:  Noise coordinate.
        :type lRepeat: int
        :param lRepeat: Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller *lRepeat* the noise will repeat at an earlier time.
        :type t: float
        :param t: The time.
        :rtype: float
        :return: Signed noise value, this is between -1.0 and 1.0.
        
        
        """
        ...
    
    def Turbulence(self, p: Vector, rOctaves: float, bAsolute: Any, lRepeat: int, t: float) -> float:
        """    
        Generate a turbulence value, this is a sum of multiple noises with different frequency.
        
        :type p: c4d.Vector
        :param p:  Turbulence coordinate
        :type rOctaves: float
        :param rOctaves: The number of octaves.
        :type bAbsolute: bool
        :param bAbsolute: **True** for absolute values.
        :type lRepeat: int
        :param lRepeat: Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller *lRepeat* the noise will repeat at an earlier time.
        :type t: float
        :param t:  The time.
        :rtype: float
        :return: Noise sample.
        
        
        """
        ...
    
    def Fbm(self, p: Vector, rOctaves: float, lRepeat: int, t: float) -> float:
        """    
        Generate a periodic Fractional Brownian Motion value.
        
        .. note:: Needs the call :meth:`InitFbm` before.
        
        .. warning::
        
        The *rOctaves* value must not exceed the value passed to :meth:`InitFbm` but can be lower.
        
        :type p: c4d.Vector
        :param p:  The evaluation point.
        :type rOctaves: float
        :param rOctaves: The octaves
        :type lRepeat: int
        :param lRepeat: Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller repeat the noise will repeat at an earlier time.
        :type t: float
        :param t: The time
        :rtype: float
        :return: The fbm value.
        
        
        """
        ...
    
    def RidgedMultifractal(self, p: Vector, rOctaves: float, rOffset: float, rGain: float, lRepeat: float, t: float) -> float:
        """    
        Generate a periodic fractal function used for such things as landscapes or mountain ranges.
        
        .. note::
        
        Needs the call :meth:`InitFbm` before.
        
        .. warning::
        
        The *rOctaves* value must not exceed the value passed to :meth:`InitFbm` but can be lower.
        
        :type p: c4d.Vector
        :param p: The evaluation point.
        :type rOctaves: float
        :param rOctaves: The octave.
        :type rOffset: float
        :param rOffset: The zero offset, this controls the multifractality.
        :type rGain: float
        :param rGain: The amplification of the fractal value.
        :type lRepeat: float
        :param lRepeat: Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller lrepeat the noise will repeat at an earlier time.
        :type t: float
        :param t: The time.
        :rtype: float
        :return: The fractal value.
        
        
        """
        ...
    


def Noise(p: Vector, t: float) -> float:
    """    
    Generates a noise value.
    
    :type p: c4d.Vector
    :param p: The noise coordinate.
    :type t: float
    :param t: The time.
    :rtype: float
    :return: The noise value, between `0.0` and `1.0`.
    
    
    """
    ...

def SNoise(p: Vector, t: float) -> float:
    """    
    Generates a signed noise value.
    
    :type p: c4d.Vector
    :param p: The noise coordinate.
    :type t: float
    :param t: The time.
    :rtype: float
    :return: The signed noise value, this is between `-1.0` and `1.0`.
    
    
    """
    ...

def PNoise(p: Vector, d: Vector, dt: float, t: float) -> float:
    """    
    Generates a periodical noise value.
    
    :func:`PNoise` is based on :func:`SNoise`:
    
    .. literalinclude:: /../../doc.python.code/c4d/utils/noise/pnoise.py
    :language: python
    
    :type p: c4d.Vector
    :param p: The noise coordinate.
    :type d: c4d.Vector
    :param d: The period.
    :type dt: float
    :param dt: The time period.
    :type t: float
    :param t: The time.
    :rtype: float
    :return: The periodical noise value.
    
    
    """
    ...

def WavyTurbulence(p: Vector, t: float, oct: int, start: int) -> float:
    """    
    Generates a wavy turbulence value, this is a sum of multiple noises with different frequency.
    
    :type p: c4d.Vector
    :param p: The turbulence coordinate.
    :type t: float
    :param t: The time.
    :type oct: int
    :param oct: The number of octaves.
    :type start: int
    :param start: The start value.
    :rtype: float
    :return: Turbulence value, this is between `-1.0` and `1.0`.
    
    
    """
    ...

def Turbulence(p: Vector, oct: int, abs: bool, t: int) -> float:
    """    
    Generates a turbulence value, this is a sum of multiple noises with different frequency.
    
    :type p: c4d.Vector
    :param p: The turbulence coordinate.
    :type oct: int
    :param oct: The number of octaves.
    :type abs: bool
    :param abs: **True** for the absolute value.
    :type t: int
    :param t: The time.
    :rtype: float
    :return: The turbulence value, between `-1.0` and `1.0` unless *abs* is true, in which case it will be between `0.0` to `1.0`.
    
    
    """
    ...

