# Setup Instructions

- Create Venv
    - py -m venv venv
    - venv/Scripts/activate (Windows)
    - venv/bin/activate (Mac)
- Install dependencies
    - pip install -r requirements.txt
- Run following commands
    - flask db init
    - flask db migrate
    - python main.py