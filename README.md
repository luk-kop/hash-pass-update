# hash-pass-update

[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

The **hash-pass-update** is simple script that allows you to add (or update if exist) a new user with hashed password to existing database.

Detailed info:
- The **bcrypt** algorithm is used to generate password hash.
- The script use a **SQLite** database.
- The input value for the hash function is a string created from the username and plain password combination.
- To create an example database, use a script `init_db.py`.

### Requirements
Python third party packages:
* [bcrypt](https://pypi.org/project/bcrypt/)
* [PTable](https://pypi.org/project/PTable/)


### Installation
The script can be build locally with `virtualenv` tool. Run following commands in order to create virtual environment and install the required packages.

```bash
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
### Create database
Below command will create `auth.db` SQLite database file with proper table:
```bash
(venv) $ python init_db.py
```
### Running the script
You can start the script using the following command:
```bash
(venv) $ python main.py
```
After starting the script correctly, the following prompt should appear in the OS console:
```bash
 _______    ______    ______    ______          ______   ________  __    __ 
/       \  /      \  /      \  /      \        /      \ /        |/  \  /  |
$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |      /$$$$$$  |$$$$$$$$/ $$  \ $$ |
$$ |__$$ |$$ |__$$ |$$ \__$$/ $$ \__$$/       $$ | _$$/ $$ |__    $$$  \$$ |
$$    $$/ $$    $$ |$$      \ $$      \       $$ |/    |$$    |   $$$$  $$ |
$$$$$$$/  $$$$$$$$ | $$$$$$  | $$$$$$  |      $$ |$$$$ |$$$$$/    $$ $$ $$ |
$$ |      $$ |  $$ |/  \__$$ |/  \__$$ |      $$ \__$$ |$$ |_____ $$ |$$$$ |
$$ |      $$ |  $$ |$$    $$/ $$    $$/       $$    $$/ $$       |$$ | $$$ |
$$/       $$/   $$/  $$$$$$/   $$$$$$/         $$$$$$/  $$$$$$$$/ $$/   $$/                                                                       

Enter db name [auth.db] >>> 
```
