# Python virtual environment
VIrtual environment is managed by poetry. Poetry setting `poetry config virtualenvs.in-project true` was run to have poetry create a venv folder to be checked into source control

To have VS Code use the poetry env as the python interperter, you must either:
- Open the python project as the vs code workspace, so the venv folder is discoverable
- Get the path for the venv and feed it to the interperter selection manually

