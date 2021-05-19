# c4dstubs

This repository provides alternative class and function definitions for MAXON's python dummy package[1] with support for the type hints introduced in python 3.5 and available in Cinema 4D with python 3.7 as specified by [PEP 484](https://www.python.org/dev/peps/pep-0484), [PEP 526](https://www.python.org/dev/peps/pep-0526), [PEP 544](https://www.python.org/dev/peps/pep-0544), [PEP 586](https://www.python.org/dev/peps/pep-0586), [PEP 589](https://www.python.org/dev/peps/pep-0589), and [PEP 591](https://www.python.org/dev/peps/pep-0591).

> Note The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

I am using those definitions with pylance and Visual Studio Code which gives nice enough results.

This project has no association with MAXON and is entirely maintained by me in my free time. Please feel free to fork or contribute by writing issues.

I can not guarantee that the definitions provided here are 100% accurate. Roughly 95% of the type hints are derived automatically from the provided docstrings, which themselves are sometimes not accurate compared with the official documentation. The rest has been manually provided by me.

This repository also provides the means to convert your local installation of the dummy package based on the docstring type and rtype notation. Edge cases will prompt for user input, overrides may be defined in the appropriate **classes.yaml** / **functions.yaml** file.

I am currently

[1]: [Dummy Package](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/introduction/autocompletion_dummy_package.html)

Excerpt from the extended definition of **c4d.Vector**

```python
class Vector(object):
    x: float
    y: float
    z: float

    def __init__(self, x: Optional[Union[int, float, Vector]] = ..., y: Optional[Union[int, float]] = ..., z: Optional[Union[int, float]] = ...) -> None:
        """
        | Initializes a new :class:`Vector <c4d.Vector>`.
        | All arguments are optional so it is possible to create a new vector without any arguments. All components are simply `0`.
        | Otherwise *x* can be a :class:`Vector <c4d.Vector>` so all components of the passed vector will be copied to the new vector.
        | If only a number is passed, all components will be set to this.

        .. code-block:: python

        c4d.Vector()
        # => Vector(0,0,0)

        c4d.Vector(100)
        # => Vector(100,100,100)

        v = c4d.Vector(100,100,100)
        c4d.Vector(v)
        # => Vector(100,100,100)

        c4d.Vector(1,2,3)
        # => Vector(1,2,3)

        :type x: Union[int, float, c4d.Vector]
        :param x: If *x* is a number and is the only passed argument, set this to all components. If *x* is a vector, clone it. Otherwise set the X component.
        :type y: number
        :param y: Set the Y component.
        :type z: number
        :param z: Set the Z component.
        :rtype: c4d.Vector
        :return: A new vector.


        """
        ...
```