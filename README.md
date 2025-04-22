A beginner-friendly Python package that includes simple tools to:
- Clean data by removing nulls
- Calculate basic statistics like mean
- Visualize data with basic text-based charts

Project Structure:

![image](https://github.com/user-attachments/assets/c6777c53-92b7-454f-a522-9060c280092b)

## How to Use

```bash
python main.py
```

## Install in Development Mode

To install the package locally and work with it while developing:

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate       # Windows

# Install the package in editable mode
pip install -e .
```

Now, you can `import datacraft` from anywhere in your project, and changes in `src/datacraft/` are instantly reflected.

## Build & Install
```bash
python -m build
pip install dist/datacraft-0.1.0-py3-none-any.whl
```

## Run Tests
```bash
pytest
```

## Configuration
Edit `config.json` to update the input data.
```json
{
  "data": {
    "a": 5,
    "b": null,
    "c": 8,
    "d": null,
    "e": 3
  }
}
```

## Definitions and Concepts

1. __init__.py file - Without this file, Python won’t recognize the folder as something you can import from.
2. Building a project creates .tar.gz and .whl files
3. Once build is done - you can install the .whl/.tar.gz distributable package in any machine.
4. The package will be installed in site-packages folder in your python source folder.(lib/site-packages/).
5. You can also un-install the build whenever.
`pip uninstall datacraft`
6. Create a .gitignore file to ignore the folders that you don't want to push to git.
7. Don't forget to create a virtual environment to work on a project.
8. pip install the requirements file before executing your main.py code.
`pip install -r requirements.txt` 
9.  pycache,pytestcache and egg-info
![image](https://github.com/user-attachments/assets/b18fc0ac-d0a0-4c63-8ec3-998b0cac4d7c)

When you run python -m build or pip install -e ., setuptools generates an .egg-info directory.

![image](https://github.com/user-attachments/assets/34857e87-c5e7-4c75-9278-45aec2ef759c)



 
