from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable


class C4DThread(object):
    def Get(self) -> BaseThread:
        """    
        Get the :class:`BaseThread <c4d.threading.BaseThread>` for this thread.
        
        :rtype: c4d.threading.BaseThread
        :return: The :class:`BaseThread <c4d.threading.BaseThread>` of this thread.
        
        
        """
        ...
    
    def Start(self, mode: int, priority: int) -> bool:
        """    
        Start the thread running.
        
        :type mode: int
        :param mode: Thread mode:
        
        .. include:: /consts/THREADMODE.rst
        :start-line: 3
        
        :type priority: int
        :param priority: Thread priority:
        
        .. include:: /consts/THREADPRIORITY.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the thread was started, otherwise **False**.
        
        
        """
        ...
    
    def End(self, wait: bool) -> None:
        """    
        End the thread.
        
        .. note::
        
        If the thread does not check for :meth:`TestBreak` then this function will not return and you will get a deadlock.
        
        :type wait: bool
        :param wait: This parameter determines if thread termination is synchronous or asynchronous. If **True** the function will not return until the thread is finished. If **False** the function returns immediately although the thread will still run until it is finished.
        
        
        """
        ...
    
    def IsRunning(self) -> bool:
        """    
        Checks if the thread is running.
        
        :rtype: bool
        :return: **True** if the thread is running, otherwise **False**.
        
        
        """
        ...
    
    def Wait(self, checkevents: bool) -> None:
        """    
        Waits until the thread has finished.
        
        :type checkevents: bool
        :param checkevents: If **False** then wait until the thread has finished. If **True** then additionally return if a Cinema 4D event occurred.
        
        
        """
        ...
    
    def TestBreak(self) -> bool:
        """    
        | Checks if the thread received a break command to stop processing.
        | Normally this is only **True** when Cinema 4D is closing, or when :meth:`End` has been called.
        
        .. note::
        
        You can add more break conditions, such as if `ESC` has been pressed, in :meth:`TestDBreak`.
        
        :rtype: bool
        :return: **True** if processing should be terminated, otherwise **False**.
        
        
        """
        ...
    
    def Main(self) -> None:
        """    
        Override with your thread main code.
        
        .. note::
        
        | Remember that a scope might be done even the threaded code is still executed.
        | In this situation you have to use :meth:`Wait` to wait until the code is finished or you should create an instance of your thread class into a scope which is longer alive than the code needs to run.
        
        
        """
        ...
    
    def TestDBreak(self) -> bool:
        """    
        Override this to add user breaks such as pressing ESC. This function is called by :meth:`TestBreak`.
        
        :rtype: bool
        :return: **True** if processing should be terminated, otherwise **False**.
        
        
        """
        ...
    

class BaseThread(C4DThread):
    def TestBreak(self) -> bool:
        """    
        Check if the thread received a break command to stop processing.
        
        :rtype: bool
        :return: **True** when Cinema 4D closes, or when a stopping condition has occurred, such as :meth:`End`.
        
        
        """
        ...
    
    def End(self, wait: bool) -> None:
        """    
        End the thread. This function will not return before the thread has completely stopped.
        
        .. note::
        
        If the thread does not check for :meth:`TestBreak` then this function will not return and you will get a deadlock.
        
        :type wait: bool
        :param wait: This parameter determines if thread termination is synchronous or asynchronous. If **True** the function will not return until the thread is finished. If **False** the function returns immediately although the thread will still run until it is finished.
        
        
        """
        ...
    
    def IsRunning(self) -> bool:
        """    
        Check if the thread is running.
        
        :rtype: bool
        :return: **True** if the thread is running, otherwise **False**.
        
        
        """
        ...
    


def GeThreadLock() -> None:
    """    
    | Locks using a global semaphore.
    | When locked, any other thread trying to acquire the lock will have to wait.
    | Other threads will continue.
    
    .. note::
    
    | As this blocks all threads it should only be used if and when necessary.
    | A local semaphore is a more elegant and efficient solution to multiple thread data access.
    
    
    """
    ...

def GeThreadUnlock() -> None:
    """    
    Continues blocked threads after a call to :meth:`GeThreadLock`.
    
    
    """
    ...

def GeIsMainThread() -> bool:
    """    
    Checks if the code is run from within the main thread of Cinema 4D.
    
    :rtype: bool
    :return: **True** if called from the main thread, otherwise **False**.
    
    
    """
    ...

def GeIsMainThreadAndNoDrawThread() -> bool:
    """    
    Checks if code is run from within the main thread of Cinema 4D and if the main thread does not execute any drawing code currently.
    
    .. versionadded:: R16.038
    
    .. note::
    
    | This routine can be used to make sure that no illegal code is called during a drawing operation.
    | In Cinema 4D the drawing will be started threaded or non-threaded, depending on the situation.
    | It is not allowed to add e.g. undo or delete objects or materials while the drawing is in progress (this would lead to immediate crashes).
    | If code calls other routines that are not aware of their context (e.g. some code within a Message() that does not know whether it was called from a drawing thread or during a command call).
    | :func:`GeIsMainThreadAndNoDrawThread` can be used to detect the correct situation.
    
    :rtype: bool
    :return: **True** if called from the main thread and main thread does not execute a drawing operation, otherwise **False**.
    
    
    """
    ...

def GeGetCPUCount() -> int:
    """    
    Gets the number of threads available.
    
    .. deprecated:: R16
    
    Use :func:`threading.GeGetCurrentThreadCount`
    
    :rtype: int
    :return: The number of current threads.
    
    
    """
    ...

def GeGetCurrentThreadCount() -> int:
    """    
    Gets the number of threads available.
    
    .. versionadded:: R16.021
    
    :rtype: int
    :return: The number of current threads.
    
    
    """
    ...

def GeGetCurrentThreadId() -> int:
    """    
    Returns a unique ID for the current thread.
    
    .. note::
    
    Usually do not care about this.
    
    :rtype: int
    :return: The unique ID for the current thread.
    
    
    """
    ...

def IdentifyThread(bt: BaseThread) -> int:
    """    
    Identifies a thread's type.
    
    :type bt: BaseThread
    :param bt: The thread to identify.
    :rtype: int
    :return: The thread type:
    
    .. include:: /consts/THREADTYPE.rst
    :start-line: 3
    
    
    """
    ...

def GeGetCurrentThread() -> None:
    """    
    Returns the current thread.
    
    :rtype: :class:`BaseThread`
    :return: The current thread.
    
    
    """
    ...

def GeGetDummyThread() -> None:
    """    
    Returns a dummy thread. The thread's :meth:`BaseThread.TestBreak` function always returns **False**.
    
    .. versionadded:: R17.048
    
    :rtype: :class:`BaseThread`
    :return: A dummy thread .
    
    
    """
    ...

def GeGetEscTestThread() -> None:
    """    
    | Returns a dummy thread for escape key testing.
    | The thread's :meth:`BaseThread.TestBreak` function returns **True** when the user presses the escape key.
    
    .. versionadded:: R17.048
    
    :rtype: :class:`BaseThread`
    :return: An escape key test thread.
    
    
    """
    ...

def GeCheckBackgroundThreadsRunning(typeclass: int, all: bool) -> bool:
    """    
    Checks if any of the threads matching *typeclass* is running.
    
    :type typeclass: int
    :param typeclass:
    
    | The type class of the background threads to check. If `0`, all threads are checked. Pass **BACKGROUNDHANDLER_TYPECLASS_C4D** to check Cinema 4D background handlers.
    |
    | For example `GeCheckBackgroundThreadsRunning(BACKGROUNDHANDLER_TYPECLASS_C4D, True)` checks if Cinema 4D is doing anything right now.
    | If **False** were passed it would not check for the external renderer (which are always running in a BodyPaint 3D selection).
    
    :type all: bool
    :param all: If **True** then background handler with negative priority are also checked.
    :rtype: bool
    :return: **True** if the specified threads are running, otherwise **False**.
    
    
    """
    ...

def GeStopBackgroundThreads(typeclass: int, flags: int) -> None:
    """    
    Stops all running background threads of the given *typeclass*.
    
    :type typeclass: int
    :param typeclass: The type class of the background threads to stop. If `0`, all threads are stopped. Pass **BACKGROUNDHANDLER_TYPECLASS_C4D** to stop Cinema 4D background handlers.
    :type flags: int
    :param flags:
    
    | If *typeclass* is **BACKGROUNDHANDLER_TYPECLASS_C4D** then the following flags can be used:
    
    .. include:: /consts/BACKGROUNDHANDLERFLAGS.rst
    :start-line: 3
    
    |
    | `GeStopBackgroundThreads(BACKGROUNDHANDLER_TYPECLASS_C4D, BACKGROUNDHANDLER_FLAGS_EDITORRENDDER)` only stops the editor renderer (if it was running).
    | `GeStopBackgroundThreads(0, BACKGROUNDHANDLERFLAGS_SHUTDOWN)` kills anything running.
    |
    | Pass flags as needed for custom type classes, they will be routed to the background handler function.
    
    
    
    """
    ...

