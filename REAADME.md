# Welcome to my TurnBase Rpg game (still in progress)


## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Technologies used](#technologies-used)

## Getting Started
Before getting access to the game there is couple of things you should do:
1. Clone repository - `https://github.com/gitLonan/Flask-projects.git`
2. Create virtual environment
   * Windows (cmd or PowerShell) - `python -m venv venv`
   * Mac & Linux (Terminal) - `python3 -m venv venv`
3. Activate virtual environment
   * Windows(PowerShell) - `venv\Scripts\Activate.ps1`
   * Windows (CMD) - `virtual\Scripts\activate.bat`
   * macOS/Linux - virtual/bin/activate
4. Run dependencies.sh file 
   If by any chance it doesn't work you can install all of these on their own, just make sure you are inside of the virtual environment:
    pip install flask
    pip install "flask<3" "werkzeug<3"
    pip install flask-wtf
    pip install flask-sqlalchemy
    pip install flask-migrate
    pip install python-dotenv

## Technologies and Libraries Used

- Python 3.9.5
### Dependencies
alembic==1.14.1
blinker==1.9.0
click==8.1.8
colorama==0.4.6
Flask==2.3.3
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
importlib_metadata==8.6.1
itsdangerous==2.2.0
Jinja2==3.1.5
Mako==1.3.9
MarkupSafe==3.0.2
python-dotenv==1.0.1
SQLAlchemy==2.0.38
typing_extensions==4.12.2
Werkzeug==2.3.8
WTForms==3.2.1
zipp==3.21.0
