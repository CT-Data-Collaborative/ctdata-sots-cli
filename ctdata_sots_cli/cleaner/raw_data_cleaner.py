# coding=utf-8
from os import walk, path
from datetime import datetime, time
import yaml
from collections import namedtuple
import codecs
import unicodecsv as ucsv
import json
from uuid import uuid4
import click

def toChar(string):
    val = string.rstrip(' \t\r\n\0').lstrip(' \t\r\n\0')
    if val == '.' or val == '':
        return '.'
    else:
        return val

def toTime(string):
    try:
        return time.strptime(string, "%I:%M %p")
    except:
        return 'null'

def toTimestamp(string):
    try:
        return datetime.strptime(string, "%Y-%m-%d-%H.%M.%S.%f")
    except:
        return 'null'

def toDate(string):
    try:
        return datetime.strptime(string, "%Y%m%d").strftime("%Y-%m-%d")
    except:
        return 'null'

def toUni(string):
    val = string.rstrip(' \t\r\n\0').lstrip(' \t\r\n\0')
    if val == '.' or val == '':
        return 'null'
    else:
        return val

def toNumeric(string):
    try:
        return int(string)
    except:
        return 'null'

def toFloat(string):
    if string == '':
        return 'null'
    try:
        return round(float(string), 2)
    except ValueError:
        return 'null'

def default(string):
    return string.rstrip(' \t\r\n\0')



# class schema(object):
#     """ Object for holding database table schema and helper functions """

class cleaner(object):
    """  Read sots configuration and schema and present methods for cleaning and loading data.

    SOTS data files present a number of issues for cleaning and loading.
    Data encoding, special characters and odd representation of data types
    make it difficult to execute one-step loading to database. The `dataLoader`
    class contains a number of methods that facilitate cleaning and loading, including
    type handling functions and data loading functions.
        Args:
            scriptVarFile (str): path reference to yaml file containing configuration parameters.

        Attributes:
            _scriptVarPath (str): cached path reference
            _connected (boolean): holds state of db connections
            _cursor: psycopg2 cursor for open db connection
            _currentlyProcessing (str): internal referance to table currently being processed
            scriptVars (list): structure containing parsed variables from config file
            offset (int): used to sample rows
            log (dict): dictionary holding bad rows by data table
            countLog (dict): dictionary holding row counts for files processed

    """
    def __init__(self, datapath, schemapath, outpath, logpath):
        """Accepts path reference to configuration yaml file and generates schema."""
        self.datapath = datapath
        self.schemapath = schemapath
        self.outpath = outpath
        self.logpath = logpath
        self.structure = None
        self.loadSchema()
        self.offset = None
        self.load = False
        self.build = False
        self.log = {}
        self.countLog = {}
        self._currently_processing = None
        self.goodlines = None

    @property
    def currentLog(self):
        return self.log[self._currently_processing]

    # def loadVars(self):
    #     """Helper function for loading variables from self._scriptVarPath specified YAML file."""
    #     print("...loading config")
    #     scriptVarFile = open(self._scriptVarPath, 'r')
    #     self.scriptVars = yaml.load(scriptVarFile.read())

    def loadSchema(self):
        """Helper function for loading schema files as defined by script variables."""
        click.echo("...loading schema")
        structureFile = open(path.join(self.schemapath, "structure.yml"), "r")
        self.structure = yaml.load(structureFile.read())


    def _buildFileStruct(self, table):
        """Internal helper function for walking dir tree and building list of files to process. Returns a list."""
        dataFiles = []
        dataDir = path.join(self.datapath, table["directory"])
        for root, subFolders, files in walk(dataDir):
            for file in files:
                if file == "DATA":
                    dataFiles.append(path.join(root,file))
        return dataFiles


    def _schemaBuilderTypeHelper(self, type):
        """Internal helper function for cleaning. Checks type and returns validation function."""
        if type == 'date':
            return toDate
        elif type == 'char':
            return toChar
        elif type == 'varchar':
            return toUni
        elif type == "numeric(10,0)":
            return toNumeric
        elif type == "numeric(8,2)":
            return toFloat
        elif type == 'timestamp':
            return toTimestamp
        elif type == 'time':
            return toTime
        else:
            return default

    def _buildSchemaObj(self, field, startPos):
        """Internal helper function for creating a SchemaField namedtuple.

        Data files are space delimited. Schema files provide start/end points for each
        field as well as expected types. This function returns a namedtuple which holds references
        to helper function, as detected by self._schemaBuilderTypeHelper, slice objects constructed
        using the start/end positions and other required fields for parsing.
        """
        SchemaField = namedtuple('SchemaField', 'name typeHelper slice default pk fk')
        endPos = startPos + int(field['length'])
        helper = self._schemaBuilderTypeHelper(field['type'])
        schemaObj = SchemaField(field['name'], helper,
                                slice(startPos, endPos),
                                field['default'],
                                field['pk'], field['fk'])
        return schemaObj, endPos

    def _prepSchema(self, table_name):
        """Internal helper function for building row parsing using schema files.

            Data files are space delimited. Schema files provide start/end points for each
            field as well as expected types. This function builds a list of namedtuples, each of which
            contain the necessary information for parsing a field in a row.
            """
        caret = 0
        schemaList = []
        schema_file_path = "{}.yml".format(table_name)
        with open(path.join(self.schemapath, schema_file_path), 'r') as schemaFile:
            schema = yaml.load((schemaFile.read()))
            for field in schema['fields']:
                schemaObj, caret = self._buildSchemaObj(field, caret)
                schemaList.append(schemaObj)
        return schemaList


    def _logger(self, line):
        """Helper for writing bad lines to log."""
        self.log[self._currently_processing].append(line)

    def writeLogs(self):
        """Function for outputting internal log to csv files named by table type."""
        for key in iter(self.log):
            outfile = path.join(self.logpath, key + '.log')
            with codecs.open(outfile, 'w', 'utf-8') as file:
                for line in self.log[key]:
                    if not line == '\x1a':
                        file.write(line)

    def _check_null_pk(self, line, schema):
        pk = [x for x in schema if x.pk][0]
        pk_val = line[pk.slice]
        if pk.typeHelper(pk_val) == 'null':
            return True
        else:
            return False

    def _handle_logged_errors(self, bad_lines, schema, outfilename, line_length):
        filtered_bad_lines = [row for row in bad_lines if not row == '\x1a']
        good_lines = []
        holding = ""
        for line in filtered_bad_lines:
            edited = False
            new = list(line)
            #if line.find("…") == 0:
            #    new_line = line.replace("…", ", ")
            #else:
            #   new_line = line.replace("\r", "")
            #holding += new_line

            # New block:
            for c in range(0, len(new)):
                if ord(new[c]) >= 128:
                    edited = True
                    new[c] = ","
                    new.insert(c+1, " ")
            #line = ''.join(new)

            if edited:
                new_line = ''.join(new)
            else:
                new_line = line.replace("\r", "")

            #new_line = line.replace("\r", "")
            holding += new_line

        if len(holding) == line_length:
            good_lines.append(holding)
            holding = ""
            self.goodlines = good_lines
            with open(outfilename, 'ab') as csvfile:
                tablewriter = ucsv.writer(csvfile, delimiter=',', lineterminator='\n')
                for line in good_lines:
                    parsed_vals = [x.typeHelper(line[x.slice]) for x in schema]
                    id = uuid4()
                    parsed_vals.append(id)
                    tablewriter.writerow(parsed_vals)

    def _load_file(self, data_file_path, schema, outfilename, lineLength):
        """Internal helper for managing the data loading process."""
        row = 0
        with open(outfilename, 'ab') as csvfile:
            tablewriter = ucsv.writer(csvfile, delimiter=',', lineterminator='\n')
            try:
                for line in codecs.open(data_file_path, encoding='cp1252', errors = 'replace'):
                    if not len(line) == lineLength and not self._currently_processing == 'BUS_OTHER':
                        self._logger(line)
                    elif self._check_null_pk(line, schema):
                        self._logger(line)
                    else:
                        parsed_vals = [x.typeHelper(line[x.slice]) for x in schema]
                        id = uuid4()
                        parsed_vals.append(id)
                        tablewriter.writerow(parsed_vals)
                    row += 1
            except UnicodeDecodeError as e:
                print(e)
        print("Rows for {}: {}".format(data_file_path, row))
        self.countLog[self._currently_processing][data_file_path] = row


    def clean(self):
        """Main function for routing type of processing to correct helpers."""
        # Get all data files in appropriate directory
        for table in self.structure['tables']:
            print(table['name'])

            # Set flag with current table name. This gets used by the logging function to correctly id where
            # bad rows were founds
            self._currently_processing = table['name']

            # Initialize log
            self.log[self._currently_processing] = []

            # Reset the log helpers
            self.countLog[self._currently_processing] = {}

            # Setup the output file
            outfilename = table['name'] + ".csv"
            clean_file_path = path.join(self.outpath,outfilename)

            # Get the schema for the given table and build the list of files to process
            dataFiles = self._buildFileStruct(table)
            schema = self._prepSchema(table['name'])

            # Prep and write the headers
            headers = [x.name for x in schema]
            headers.append('id')
            with open(clean_file_path, 'wb') as csvfile:
                tablewriter = ucsv.writer(csvfile, delimiter=',', lineterminator='\n')
                tablewriter.writerow(headers)

            # Walk the datafiles for the given table
            for data in dataFiles:
                # Reset the log
                self.countLog[self._currently_processing][data] = []

                # Load, parse and write data for given partial data file
                self._load_file(data, schema, clean_file_path, table['length'])

                # Log any errors
                self._handle_logged_errors(self.log[self._currently_processing], schema, clean_file_path, table['length'])
                # Reset log
                self.log[self._currently_processing] = []
        self._currently_processing = None

        with open('countLog.json', 'w') as logfile:
            json.dump(self.countLog, logfile)
