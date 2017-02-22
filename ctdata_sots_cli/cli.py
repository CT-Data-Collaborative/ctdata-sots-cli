# -*- coding: utf-8 -*-

"""
ctdata_sots_cli.cli
-----------------------

Main `ctdata_sots_cli` CLI.
"""

import click

from .cleaner import cleaner
from .prep import prep_release_files
from .load import connectDB, dropTables, buildStatusAndSubtypeTable, buildTables

@click.group()
def main():
    """Command line tool for cleaning, preparing and publishing SOTS data"""
    pass


@main.command()
@click.option('--outdir', type=click.Path(),
              help='Output directory where cleaned files should be written to.')
@click.option('--indir', type=click.Path(),
              help='Input directory where unzipped files are stored.')
@click.option('--logdir', type=click.Path(), default='./log',
              help='Directory where cleaning log files should be written')
@click.argument('schema', type=click.Path(), default='.', required=False)
def clean(indir, outdir, schema, logdir):
    """
    Parse unzipped raw SOTS data using the provided schema.

    Raw SOTS data needs to be parsed according to a set of crosswalks and schema tables. This command is
    responsible for the main parsing work. The command requires a schema directory as its primary argument.
    This schema directory should contain YAML files for each table in the SOTS database.

    See <insert url for sots db schema> for more information about schema formatting.
    """
    sots_cleaner = cleaner(datapath=indir, outpath=outdir, schemapath=schema, logpath=logdir)
    sots_cleaner.clean()

@main.command()
@click.option('--zipdir', type=click.Path(),
              help='Input directory where files from SOTS FTP server are stored.')
def unzip(zipdir):
    """
    Unzip raw SOTS data to the target folder.

    SOTS data is pushed to an FTP server by IT at the Secretary of State. This data
    is stored in a zipfile structure that not easy to parse. This command unzips the
    downloaded files and generates the correct directory structure as expected by the
    clean command.
    """
    prep_release_files(zipdir)


@main.command()
@click.option('--dbhost', default='0.0.0.0',
              help='IP address of database server where data should be published to.')
@click.option('--dbuser', default='postgres',
              help='Database user.')
@click.option('--dbpass', default='',
              help='Password for database.')
@click.option('--dbname', default='postgres',
              help='Name of database on host where data should be publish to.')
@click.option('--data', type=click.Path(),
              help='Path to cleaned data')
@click.argument('schema', type=click.Path(), default='.', required=False)
def prepdb(dbhost, dbuser, dbpass, dbname, data, schema):
    """
    Publish SOTS data to the provided database

    This will prepare the database, build tables, load data, build indices, and then cleanup
    """
    conn, cursor = connectDB(dbname, dbuser, dbpass, dbhost)
    dropTables(conn, cursor, schema)
    buildTables(conn, cursor, schema)
    buildStatusAndSubtypeTable(conn, cursor)
    conn.close()


if __name__ == '__main__':
    main()

