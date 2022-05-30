# python_factory

Shows how to create factory methods and private constructors in Python using decorators.

Factory methods are a great possibility to create instances of a class in a more controlled and verbose way.
To implement this pattern, a **private** constructor is required. By construction, hiding the constructor is not
possible in Python. Thus, this repository shows an alternative to achieve a "private-like" behavior for Python
constructors and to efficiently create
factory methods - both using Python **decorators**.

## Run the tests

- Create a python environment: ``python -m venv env``
- Activate the python environment: ``.\env\Scripts\activate``
- Install pytest: ``pip install pytest``
- Run the tests: ``pytest``