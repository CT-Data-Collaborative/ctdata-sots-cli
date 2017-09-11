CTData SOTS CLI
===================

What is it?
-----------

CLI Tool for handling the prep, cleaning and publishing of monthly data dumps from the CT Secretary of State for the
SOTS search portal


Install
-------

Install it easily:

Using git
---------

::

    $ git clone https://github.com/CT-Data-Collaborative/ctdata-sots-cli.git
    $ cd ctdata-sots-cli
    $ pip install -e .


Configuration and Use
---------------------

::

     $ sots --dbbame postgres --host 52.123.44.23


Data needs to be built and prepared in a particular order. Currently, the CLI commands should be executed in the
following order:

1. unzip
2. clean
3. prepdb
4. drop_supplemental
5. add_supplemental
6. loaddb
7. extract_formations

ToDos
-----

1. Rename functions for legibility
2. Add in default locations for functions that output data and use the date of processing
3. Consolidate commands:
     a. unzip and clean should be combined to process_raw
     b. prepdb should be renamed to load_raw
     c. add_supplemental should also drop tables
     d. loaddb should be renamed to build_indices
     e. add a rebuild command which executes all steps
