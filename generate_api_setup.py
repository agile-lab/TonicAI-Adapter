"""
    The script uses the fastapi-code-generator that creates a FastAPI application from an openapi file.
    For more details on using fastapi-code-generator, see the following documentation:
    https://koxudaxi.github.io/fastapi-code-generator/?ref=morioh.com&utm_source=morioh.com
"""  # noqa: E501

import os

from pyutil import filereplace

# Specification path
INPUT_SPEC = "specific-provisioner/interface-specification.yml"

# Code output path
PATH_FOLDER = "specific-provisioner/src/"

# Path of the main program related to the API
PATH_MAIN = f"{PATH_FOLDER}/main.py"

# Path of the models program related to the API
PATH_MODELS = f"{PATH_FOLDER}/models.py"

init_message = f"""
SETTING PARAMETERS:

    Specification_Path = {INPUT_SPEC}
    Output_folder_Path = {PATH_FOLDER}

"""
print(init_message)

os.system(f"fastapi-codegen --input {INPUT_SPEC} --output {PATH_FOLDER}")
print("Generating the API code structure.........")

# To avoid possible errors when importing the module related to models
# (default: models.py), we replace '.models' with 'models' in the import
# of main.py using a functionality of the pyutil library
filereplace(PATH_MAIN, ".models", "models")
print("COMPLETED!")
print(
    "______________________________________________________________________________\n"
)

# Install and run pre-commit hooks to run automated ad-hoc tasks before
# submitting a new git commit. Documentation: https://pre-commit.com/
print("Installing 'pre-commit'.......")
cwd1 = os.getcwd()
os.chdir(f"{cwd1}/specific-provisioner")
os.system("pre-commit install")

print("\nAdding 'noqa' for autogenerated code......")
# Add noqa for autogenerated code
cwd2 = os.getcwd()
os.chdir(f"{cwd2}/src")
os.system("ruff main.py --add-noqa")
os.system("ruff models.py --add-noqa")

print(
    "______________________________________________________________________________\n"
)
print("pre-commit init running.......\n")
os.chdir(f"{cwd1}/specific-provisioner")
os.system("pre-commit run --all-files")

print("\n\n SETUP COMPLETED!\n")
