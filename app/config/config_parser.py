import os, configargparse, sys

parser = configargparse.ArgParser(
    config_file_parser_class=configargparse.YAMLConfigFileParser,
    auto_env_var_prefix=""
)

parser.add("--postgres_catalog_read_write", help='POSTGRES_CATALOG_READ_WRITE')
parser.add("--port", help="PORT")

arguments = sys.argv
argument_options = parser.parse_known_args(arguments)
config_args = argument_options[0]
