# pyMeteo
Simple weather app using open-meteo.

## Use a Virtual Environment for pyMeteo:

### Navigate to your project folder
cd /path/to/your/project

### Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

### Install packages
pip install --upgrade pip
pip install requests

### Run the project
python3.14 src/main.py 

### Deactivate Virtual Environment
deactivate

### Checkstyle before push
 + Format: ruff format --target-version=py313 .
 + Check:  ruff format --diff --target-version=py313