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

1) Unzip monthlies folders from FTP server, run: (approx 2 min)

::

    sots unzip --zipdir monthlies/07_20_2018/

2) Clean text files using individual schema files for each table to create csv files (approx 15 minutes)

::

    sots clean --indir monthlies/07_20_2018/ --outdir clean/07_2018 ../sots-db-schema

3) Data base prep, preps the Postgres server (creates the tables) on the docker-environment for the data to be loaded in (if tables/indices/views already exist, they are dropped and created again) (approx 15min)

::

    sots prepdb --dbhost 0.0.0.0 --dbport 15432 --dbuser sots --dbpass [password] --data clean/07_2018 ../sots-db-schema

--dbhost 0.0.0.0 (hosts the application on your local machine at your localhost)
--dbport 5432 (port at which the postgres server listens on the docker container)
--dbuser sots (server configuration, set in the dev.env file)
--dbpass [password] (server password, set in the dev.env file)
--data [link to data] (points to where the .csvs live)
[link to schema directory] (.yml files for sots db schema) 

If you have another non-docker related postgres service running on the 5432 port, you may update the port configuration in the dev.yml file to connect to 15432:5432, This will bypass the 5432 port on your local machine and only required for local deployment (i.e. would not be needed in the docker-compose.yml file)

4) Drop supplemental tables

::

    sots drop_supplemental --dbhost 0.0.0.0 --dbport 15432 --dbuser sots --dbpass [password]

5) Recreate supplemental tables

::

    sots add_supplemental --dbhost 0.0.0.0 --dbport 15432 --dbuser sots --dbpass  [password]

6) Load the database into the postgres db

::

    sots loaddb --dbhost 0.0.0.0 --dbport 15432 --dbuser sots --dbpass [password] --data clean/07_2018 ../sots-db-schema



-----
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
