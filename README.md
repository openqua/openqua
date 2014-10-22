openqua
=======

*OpenQUA - Have you heard news of .... ?*

Introduction
------------

OpenQUA is a web application that scrapes amateur radio callsign information
from a variety of sources and then presents it to users in useful ways.

Installation
------------

You're insane. This isn't ready for you to install.

If you insist:

1. Import the `openqua.sql` file into MySQL. This will create the database.
2. Run each of the scrapers (`repeater_*.py` in `scrapers/`) to import the data.
3. Run `python app.py` in the `web/` directory.
4. Browse to http://localhost:5000/ and enjoy.

License
-------

(C) 2014 Iain R. Learmonth, Derecho and contributors. See LICENSE for more
details on terms for use and distrubtion.

