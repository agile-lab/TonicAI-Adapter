# Python Specific Provisioner

This REST application mocks a specific provisioner for data product components.

This project uses OpenAPI as standard API specification and the [fastapi-code-generator](https://pypi.org/project/fastapi-code-generator/)

#### Setup Python environment
To set up a Python environment we use [Poetry](https://python-poetry.org/docs/):

```
curl -sSL https://install.python-poetry.org | python3 -
```
Once Poetry is installed and in your `$PATH`, you can execute the following:
```
poetry --version
```
If you see something like `Poetry (version x.x.x)`, your install is ready to use!

Install the dependencies defined in `specific-provisioner/pyproject.toml`:
```
cd specific-provisioner
poetry install
```

#### Generate FastAPI server starting from OpenAPI specification
Activate the Python virtual environment generated by Poetry:
```
source $(poetry env info --path)/bin/activate
```
Start the script `generate_api_setup.py`:
```
cd ..
python generate_api_setup.py
```
For default settings, Python scripts `specific-provisioner/src/main.py` and `specific-provisioner/src/models.py` will be generated by exploiting the specification file `specific-provisioner/interface-specification.yml`.

The script `generate_api_setup.py` also installs the [pre-commit](https://pre-commit.com/) framework to automatically handle the linter, formatter, and static type checker.

#### Remarks
The autogenerated code from `fastapi-code-generator` contains `pass` within the various functions. In order for `mypy` not to report errors, it is necessary to properly modify the return type of the output according to the specified types by the functions.
Finally, note that Gitlab's CI pipeline expects to find unit tests in the `tests/` folder otherwise the whole process will be blocked.
