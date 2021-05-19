from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseObject


class MtTrkGid(object):
    def ToInt(self) -> int:
        """    
        Retrieves the track global ID as an integer.
        
        :rtype: int
        :return: The global ID.
        
        
        """
        ...
    

class MtFootageData(object):
    def GetFootageName(self) -> str:
        """    
        Retrieves the filename of the footage (the first frame if an image sequence).
        
        :rtype: str
        :return: The filename.
        
        
        """
        ...
    
    def GetFirstFrameNumber(self) -> int:
        """    
        Retrieves the frame number of the first frame in the footage. `-1` if no footage loaded.
        
        :rtype: int
        :return: The first frame number.
        
        
        """
        ...
    
    def GetLastFrameNumber(self) -> int:
        """    
        Retrieves the last number of the first frame in the footage. `-1` if no footage loaded.
        
        :rtype: int
        :return: The last frame number.
        
        
        """
        ...
    
    def GetResolutionWidthPix(self, originalRes: int) -> int:
        """    
        Retrieves the width in pixels of the footage.
        
        :type originalRes: int
        :param originalRes:
        
        | If **True**, returns the original resolution of the footage.
        | If **False**, returns the downsampled resolution.
        
        :rtype: int
        :return: The width of footage in pixels.
        
        
        """
        ...
    
    def GetResolutionHeightPix(self, originalRes: int) -> int:
        """    
        Retrieves the height in pixels of the footage.
        
        :type originalRes: int
        :param originalRes:
        
        | If **True**, returns the original resolution of the footage.
        | If **False**, returns the downsampled resolution.
        
        :rtype: int
        :return: The height of footage in pixels.
        
        
        """
        ...
    
    def GetResolutionAspectRatio(self) -> float:
        """    
        Retrieves the ratio of the horizontal to vertical resolution. Ignores pixel aspect ratio.
        
        :rtype: float
        :return: The aspect ratio from resolution.
        
        
        """
        ...
    
    def GetImageAspectRatio(self) -> float:
        """    
        Retrieves the aspect ratio of the footage including effects of pixel aspect ratio.
        
        .. note::
        
        :meth:`GetImageAspectRatio` == :meth:`GetResolutionAspectRatio` * :meth:`GetPixelAspectRatio`
        
        :rtype: float
        :return: The image aspect ratio.
        
        
        """
        ...
    
    def GetPixelAspectRatio(self) -> float:
        """    
        Retrieves the pixel aspect ratio of the footage.
        
        :rtype: float
        :return: The pixel aspect ratio.
        
        
        """
        ...
    
    def GetDownsamplingFactor(self) -> float:
        """    
        Retrieves the downsampling factor used for the footage.
        
        :rtype: float
        :return: The downsampling factor.
        
        
        """
        ...
    

class MtData(object):
    def GetNormalisedPosition(self) -> None:
        """    
        Retrieves the track position in normalized coordinates.
        
        .. note::
        
        | x is in range `-0.5` to `+0.5` from left to right of image.
        | y is in range `-0.5/aspect` to `+0.5/aspect` from top to bottom of image, where `aspect` is the image aspect ratio.
        
        :rtype: :class:`c4d.Vector`
        :return: The track position in normalized coordinates.
        
        
        """
        ...
    
    def GetPixelPosition(self, footageData: MtFootageData, originalRes: int) -> None:
        """    
        Retrieves the track position in pixel coordinates.
        
        :type footageData: c4d.modules.motiontracker.MtFootageData
        :param footageData: The footage object (used to define resolution and aspect ratio).
        :type originalRes: int
        :param originalRes:
        
        | If **True**, returns pixel coordinates for the original footage.
        | If **False**, returns pixel coordinates for the downsampled footage.
        
        :rtype: :class:`c4d.Vector`
        :return: The track position in pixel coordinates.
        
        
        """
        ...
    
    def GetCameraSpaceDirection(self, focalLength: float, sensorWidth: float) -> None:
        """    
        Retrieves the camera space ray corresponding to track position.
        
        :type focalLength: float
        :param focalLength: The focal length to use for the camera (mm).
        :type sensorWidth: float
        :param sensorWidth: The sensor width to use for the camera (mm).
        :rtype: :class:`c4d.Vector`
        :return: The ray in camera space corresponding to the position of the track.
        
        
        """
        ...
    

class Mt2dTrackData(object):
    def GetTrackCount(self) -> int:
        """    
        Retrieves the number of tracks.
        
        :rtype: int
        :return: The number of tracks.
        
        
        """
        ...
    
    def GetTrackByIndex(self, index: int) -> Mt2dTrack:
        """    
        Retrieves the track with the given *index*.
        
        :type index: int
        :param index: The track index.
        :rtype: c4d.modules.motiontracker.Mt2dTrack
        :return: The track.
        
        
        """
        ...
    
    def GetTrackByGid(self, trkGid: MtTrkGid) -> Mt2dTrack:
        """    
        Retrieves the track with the given global ID.
        
        :type trkGid: c4d.modules.motiontracker.MtTrkGid
        :param trkGid: The track global ID.
        :rtype: c4d.modules.motiontracker.Mt2dTrack
        :return: The track.
        
        
        """
        ...
    
    def GetTrackByName(self, name: str) -> Mt2dTrack:
        """    
        Retrieves the track with the given name.
        
        :type name: str
        :param name: The name of the track to search for.
        :rtype: c4d.modules.motiontracker.Mt2dTrack
        :return: The track.
        
        
        """
        ...
    
    def GetTrackIndices(self, userTracks: bool, autoTracks: bool) -> None:
        """    
        Retrieves the indices of all tracks.
        
        :type userTracks: bool
        :param userTracks: **True** to include User created tracks, otherwise **False**.
        :type autoTracks: bool
        :param autoTracks: **True** to include Automatic tracks, otherwise **False**.
        :rtype: :class:`c4d.BaseSelect`
        :return: The indices of all tracks.
        
        
        """
        ...
    

class Mt2dTrack(object):
    def GetName(self) -> str:
        """    
        Retrieves the name of the track.
        
        :rtype: str
        :return: The name of the track.
        
        
        """
        ...
    
    def GetId(self) -> MtTrkGid:
        """    
        Retrieves the global ID of the track.
        
        :rtype: c4d.modules.motiontracker.MtTrkGid
        :return: The global ID of the track.
        
        
        """
        ...
    
    def GetStatus(self) -> int:
        """    
        Retrieves the track status.
        
        :rtype: int
        :return: The track status:
        
        .. include:: /consts/Mt2dTrackStatus.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetFramesWithTrackData(self) -> None:
        """    
        Retrieves the frames on which the track has data.
        
        :rtype: :class:`c4d.BaseSelect`
        :return: The frames with track data.
        
        
        """
        ...
    
    def GetDataForFrame(self, frameNum: int) -> MtData:
        """    
        Retrieves the motion tracking data for the given frame.
        
        :type frameNum: int
        :param frameNum: The frame number.
        :rtype: c4d.modules.motiontracker.MtData
        :return: The tracking data, or **None** if it does not exist for the requested frame.
        
        
        """
        ...
    
    def GetDataForCurrentFrame(self) -> MtData:
        """    
        Retrieves the track data for the current frame.
        
        :rtype: c4d.modules.motiontracker.MtData
        :return: The tracking data for the current frame, or **None** if it does not exist.
        
        
        """
        ...
    

class MotionTrackerObject(BaseObject):
    def GetFootageData(self) -> MtFootageData:
        """    
        Retrieves data about the footage.
        
        :rtype: c4d.modules.motiontracker.MtFootageData
        :return: The footage data.
        
        
        """
        ...
    
    def Get2dTrackData(self) -> Mt2dTrackData:
        """    
        Retrieves 2D tracking data.
        
        :rtype: c4d.modules.motiontracker.Mt2dTrackData
        :return: The 2D tracking data.
        
        
        """
        ...
    

