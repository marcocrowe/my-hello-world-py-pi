# Hello Package

A simple Python package that prints "Hello, World!" to the console.

## Build

To build the package follow this guide.

## Recommended IDEs

- [VS Code](https://code.visualstudio.com/): [*Python*](https://code.visualstudio.com/docs/languages/python)

## Requirements

- [Python &GreaterEqual; 3.10.0](https://www.python.org/downloads/)

## Install Python Package Builders

The packages required to build this package are:

- [pip &GreaterEqual; 21.2.4](https://pip.pypa.io/en/stable/installation/)
- [build &GreaterEqual; 0.7.0](https://packaging.python.org/tutorials/packaging-projects/)
- [twine &GreaterEqual; 3.4.2](https://twine.readthedocs.io/en/stable/)
- [pipreqs &GreaterEqual; 0.4.10](https://pypi.org/project/pipreqs/)

To install/upgrade Python packages to build a Python package run these commands:

```bash
pip install -r requirements.txt
```

```bash
pip install --upgrade pip
pip install --upgrade build
pip install --upgrade twine
```

In the event of an error, consider running the following commands:

```bash
python -m pip cache purge
python -m pip install -U pip
```

## Build and publish a Python package

*All these commands must be run from the project root:*

### Update the required packages

To build the requirements.txt file run these commands:

```bash
pipreqs --force
```

### Build/rebuild the Python package

To build the Python package, run the following command:

```bash
python -m build
```

### Publish the Python package

To publish the package to PyPI, run the following command:

```bash
python -m twine upload dist/*
```

For username enter `__token__` and then your password.

The package is then available at [my-hello-world](https://pypi.org/project/my-hello-world/ "hello-world")

### Installation of the Python package

#### Remote installation

To install the package from [pypi.org](https://pypi.org), run the following command:

```bash
pip install hello-world
```

#### Local installation

To install the package from local sources, run the following command:

```bash
pip install .\dist\my-hello-world-1.0.0-py3-none-any.whl
```

To force a reinstall of the package from local sources, run the following command:

```bash
pip install .\dist\my-hello-world-1.0.0-py3-none-any.whl --force-reinstall
```

Conda:

```bash
conda install .\dist\my-hello-world-1.0.0-py3-none-any.whl --channel conda-forge
```

---

Copyright &copy; 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
