#!/usr/bin/env python3
import os
import sys
import sqlite3
import time

import bcrypt
from prettytable import PrettyTable


print("""
 _______    ______    ______    ______          ______   ________  __    __ 
/       \  /      \  /      \  /      \        /      \ /        |/  \  /  |
$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |      /$$$$$$  |$$$$$$$$/ $$  \ $$ |
$$ |__$$ |$$ |__$$ |$$ \__$$/ $$ \__$$/       $$ | _$$/ $$ |__    $$$  \$$ |
$$    $$/ $$    $$ |$$      \ $$      \       $$ |/    |$$    |   $$$$  $$ |
$$$$$$$/  $$$$$$$$ | $$$$$$  | $$$$$$  |      $$ |$$$$ |$$$$$/    $$ $$ $$ |
$$ |      $$ |  $$ |/  \__$$ |/  \__$$ |      $$ \__$$ |$$ |_____ $$ |$$$$ |
$$ |      $$ |  $$ |$$    $$/ $$    $$/       $$    $$/ $$       |$$ | $$$ |
$$/       $$/   $$/  $$$$$$/   $$$$$$/         $$$$$$/  $$$$$$$$/ $$/   $$/                                                                       
""")


db_name = input('Enter db name [auth.db] >>> ')
if db_name == '':
  db_name = 'auth.db'

# Check whether db_name exist in cwd
if not os.path.exists(db_name):
  print(f'File "{db_name}" doesn\'t exist! Should be in current dir!')
  time.sleep(3)
  sys.exit()

# List for username and password pair
users_to_add = []

while True:
  while True:
    username = input('Username >>> ')
    if username:
      break

  password_plain = input('Password >>> ')

  users_to_add.append({'username': username, 'password_plain': password_plain})
  while True:
    more_users = input('More users to add? [N] >>> ')
    if more_users.lower() in 'yn':
      break
    print('Error: Wrong input!')
  if more_users.lower() == 'n' or more_users == '':
    break

# Connection to db
conn = sqlite3.connect(db_name)
c = conn.cursor()
print('\nConnected to DB...')

for user in users_to_add:
  # Very very simple papper
  username_plus_pass = user['username'] + user['password_plain']

  # Generate random salt and bcrypt hash
  salt = bcrypt.gensalt(prefix=b"2a", rounds=10)
  password_hash = bcrypt.hashpw(username_plus_pass.encode('utf-8'), salt).decode('utf-8')
  # password_hash = bcrypt.hashpw(username_pass.encode('utf-8'), b'$2a$10$/.Ewl7SneM0Yj5necmC5Zu')

  # Check whether username exist in db
  query = 'SELECT * FROM "TBLUSER" WHERE "USERNAME" = ?;'
  c.execute(query, (username, ))
  item = c.fetchone()

  if item:
    query_update = 'UPDATE "TBLUSER" SET "PASSWORD" = ? WHERE "USERNAME" = ?;'
    c.execute(query_update, (password_hash, user['username']))
    print('DB has been updated...')
  else:
    query_insert = 'INSERT INTO "TBLUSER" VALUES (?, 1, 1, ?, "OPERATOR");'
    c.execute(query_insert, (user['username'], password_hash))
    print(f'User \"{user["username"]}\" has been added to DB..')


# Table
TOutput = PrettyTable()
TOutput.field_names = ['Username', 'Password']
for row in users_to_add:
  TOutput.add_row([row['username'], row['password_plain']])
print('\nData added or updated...')
print(TOutput)

conn.commit()
conn.close()
print('Disconnected from DB...')
time.sleep(3)