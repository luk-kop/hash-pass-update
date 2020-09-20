# hash-pass-update

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
The application can be build locally with `virtualenv` tool. Run following commands in order to create virtual environment and install the required packages.

```bash
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```