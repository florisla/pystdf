PySTDF - The Pythonic STDF parser
=================================
Developed by Casey Marshall <casey.marshall@gmail.com>

PySTDF is a parser for Standard Test Data Format (STDF) version 4 data
files.

STDF is a commonly used file format in semiconductor test -- automated
test equipment (ATE) from such vendors as Teradyne, Verigy, LTX, Credence,
and others.


PySTDF provides event-based stream parsing of STDF version 4, along with
indexers that can help you rearrange the data into a more useful tabular
form, as well as generate missing summary records or new types of
derivative records.

The parser architecture is very flexible and can easily be extended to
support STDF version 3 as well as custom record types.

Potential applications of PySTDF include:
* Debugging a vendor's STDF implementation
* Straight conversion to ASCII-readable form
* Repairing STDF files
* Developing an application that leverages STDF
  - Conversion to tabular form for statistical analysis tools
  - Loading data into a relational database

Architecture
============
I wrote PySTDF to get familiar with functional programming idioms and
metaclasses in Python.  As such, it uses some of the more powerful and 
expressive features of the Python language.

PySTDF is an event-based parser.  As an STDF file is parsed, you receive
record "events" in callback functions

Refer to the provided command line scripts for ideas on how to use PySTDF:

script/totext.py, convert STDF to '|' delimited text format.
script/toexcel.py, convert STDF to MS Excel.
script/slice.py, an example of how to seek to a specific record offset in the STDF.

Installation
============
Use the standard distutils setup.py.

On Windows: "python setup.py install"
On Unix: "sudo python setup.py install"

Bugs
====
PySTDF has no known bugs.  However, it is my experience that every ATE vendor 
has its quirks and "special interpretation" of the STDFv4 specification.

If you find a bug in PySTDF, please send me the STDF file that demonstrates it.
This will help me improve the library.

License
=======
PySTDF is released under the terms and conditions of the GPL version 2 license.
You may freely use PySTDF, but you may not distribute it in closed-source 
proprietary applications.  Please contact me if you are interested in 
purchasing an alternative license agreement to develop commercial software 
with PySTDF.

If you need some STDF consulting/development work, I might be able to help you.
I have over 5 years experience with STDF and semiconductor data analysis 
systems.

If you're in the Austin area and just want to get some lunch, that is cool too :)

Thanks
======
Thanks for your interest in PySTDF.  You're the reason I open-sourced it.

Cheers,
Casey
