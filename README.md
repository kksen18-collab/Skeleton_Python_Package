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
