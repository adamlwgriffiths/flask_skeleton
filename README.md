# Install Dependencies

## Install Node.js (Development only)

Node.js is used for compiling the Javascript code (ironic, eh?).
This is only required for development, the compiled resources can be deployed to production on their own.

```bash
# TODO: nodejs installation instructions

# install global build tools
$ sudo npm install -g webpack
# install npm dependencies
$ npm install
```

## Install SQLCipher

Python libs require this, so install prior to installing python libraries.

```bash
$ apt-get install sqlcipher libsqlcipher-dev
```

## Install Python

```bash
# TODO: install anaconda instructions
```

## Setup Python environment

Anaconda manages python versions and packages for you.
Each anaconda "environment" is silo'ed.
When installing -and using- you must make the anaconda environment active.

```bash
# TODO: create anaconda environment
$ pip install -r requirements.txt
```

# Setup Development Database

## Create database

PRAGMA values must be added to the `SQLALCHEMY_DATABASE_URI` environment value.
http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#module-sqlalchemy.dialects.sqlite.pysqlcipher
https://groups.google.com/forum/#!msg/sqlcipher/bd1R13RpZHQ/SEPK8YrRt1gJ

```
# NOTE: the first commands MUST be the PRAGMA commands
$ sqlcipher test.db
SQLCipher version 2.2.1 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> PRAGMA key='mypass';
sqlite> PRAGMA cipher = 'aes-256-cfb';
sqlite> create table user (`id` integer primary key autoincrement, `username` varchar, `email` varchar);
sqlite> .tables
mytable
sqlite> .q
# check database is encrypted
$ hexdump -C test.db | head -5
00000000  1f 38 c5 70 dc 28 3e ef  48 6c 1d 47 ca d8 93 2c  |.8.p.(>.Hl.G...,|
00000010  95 0a 17 98 9d b7 53 59  66 0b e8 e2 60 91 0e 39  |......SYf...`..9|
00000020  3f 1c 08 bf a3 0d c8 0d  dd 70 e9 e8 71 bc 1e 35  |?........p..q..5|
00000030  9c d6 bf 5b 58 45 c0 0b  17 22 9c fc 20 84 2c d0  |...[XE...".. .,.|
00000040  e4 4a 20 61 ba ca 8a 7b  17 53 3b 87 76 d4 72 34  |.J a...{.S;.v.r4|
```

# Build Javascript

```bash
# builds source from `webserver/js` and places it in `webserver/static/js`
# runs the `build` script in `package.json`
# this just called `webpack`, which uses `webpack.config.js`
$ npm run build
```

# Run Development Webserver

Run using Flask's own wsgi libraries.

Note: Don't use this in production! It is slow and potentially unsafe.

```bash
# TODO: activate the anaconda environment
$ flask run -h 0.0.0.0 -p 5000
```

# Run Production Webserver

Using Honcho

Honcho is a clone of Heroku's application manager.
It uses a `Procfile` to define application resources

Note: the `web` process is a unique resource name that will get HTTP redirected to it.
No other resources will have incoming HTTP ports.

```bash
# TODO: activate the anaconda environment
$ source .env
$ honcho start
```
