CTData SOTS CLI
===================

What is it?
-----------

CLI Tool for handling the prep, cleaning and publishing of monthly data dumps from the CT Secretary of State for the
SOTS search portal.


How and why we use it?
----------------------

Data updates from the Secretary of State are not incremental. Each month we are given a complete copy of the database
at that point in time. Rather than attempt to diff changes and make incremental changes, we leverage the disposable
infrastructure model facilitated by Docker and AWS. Each month we spin up a new ec2 instance, build out the application
stack and then rebuild the database using the most recent dump. When the data load is complete, we re-point the dns
information and then destroy the old server.

These scripts handle the process of processing the raw snapshot provided to use via the SOTS FTP server. The starting
point for using the scripts is that the latest months data has been downloaded to a local computer.


Installation
-------

::

    $ pip install git+https://github.com/CT-Data-Collaborative/ctdata-sots-cli.git#egg=sotscli


Configuration and Use
---------------------

The tool is built with click to provide a number of command line options.

Use depends on providing sufficient information to allow for a database connection to be made. Some
defaults are provided which allow the tool to connect directly to the sots database created by the
SOTS Search application local docker-compose manifest. If you are running this script on a production instance,
you will need to provide the security credentials being used for that infrastructure.

Data needs to be built and prepared in a particular order. Currently, the CLI commands should be executed in the
following order:

1. unzip
2. clean
3. prepdb
4. drop_supplemental
5. add_supplemental
6. loaddb
7. extract_formations

::

     $ sots --dbbame postgres --host 52.123.44.23



ToDos
-----

1. Add in default locations for functions that output data and use the date of processing
2. Consolidate commands:
     a. unzip and clean should be combined to process_raw
     b. prepdb should be renamed to load_raw
     c. add_supplemental should also drop tables
     d. loaddb should be renamed to build_indices
     e. add a rebuild command which executes all steps
