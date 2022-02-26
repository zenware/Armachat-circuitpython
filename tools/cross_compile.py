#!/usr/bin/env python3
"""

"""
import argparse
import os
import os.path


def download(arguments):
    """

    :param arguments:
    :type arguments: argparse.Namespace
    :return:
    """
    print(arguments)


def cross_compile(arguments):
    """

    :param arguments:
    :type arguments: argparse.Namespace
    :return:
    """
    arguments.dir = arguments.dir.rstrip("/")  # Strip trailing slashes from source directory path.
    if not arguments.out:  # If an output directory is not specified
        arguments.out = arguments.dir  # Use the source directory

    path_prefix_len = len(arguments.dir) + 1  # Counts the number of characters in the source path.

    for path, subdirs, files in os.walk(arguments.dir):  # For all objects in the source directory
        for f in files:  # For all files found in the source directory
            if f.endswith(".py"):  # If the file is a Python file
                fpath = path + "/" + f  # Create the absolute filepath for the source

                out_fpath = arguments.out + "/" + fpath[path_prefix_len:-3] + ".mpy"  # Create the output filepath
                out_dir = os.path.dirname(out_fpath)  # Set the output directory
                if not os.path.isdir(out_dir):  # If the output directory doesn't exist
                    os.makedirs(out_dir)  # Create the output directory

                cmd = "mpy-cross -v -s %s %s -o %s" % (
                    fpath[path_prefix_len:],
                    fpath,
                    out_fpath,
                )  # Build command string

                res = os.system(cmd)  # Run command
                assert res == 0  # Ensure return code was 0


"""Main entry point into the script if run via CLI"""
if __name__ == "__main__":
    parent_parser = argparse.ArgumentParser(
        prog="cross_compile.py",
        description="Compile all .py files to .mpy recursively"
    )
    parent_parser.add_argument("--verbose", "-v", action="count")
    subparsers = parent_parser.add_subparsers(title="commands")

    """Subparser for downloading mpy-cross"""
    parser_download = subparsers.add_parser("download", parents=[parent_parser], add_help=False)
    parser_download.set_defaults(func=download)
    parser_download.add_argument("--version", "-V",
                                 help="Specify the version of mpy-cross to download",
                                 type=str,
                                 required=False,
                                 dest="version")

    """Subparser for compiling .py into .mpy"""
    parser_compile = subparsers.add_parser("compile", parents=[parent_parser], add_help=False)
    parser_compile.set_defaults(func=cross_compile)
    parser_compile.add_argument("--source", "-s",
                                help="input directory",
                                type=str,
                                required=False)
    parser_compile.add_argument("--destination", "-d", help="output directory (default: input dir)")

    """Parse the arguments and execute the functions"""
    args = parent_parser.parse_args()
    args.func(args)
