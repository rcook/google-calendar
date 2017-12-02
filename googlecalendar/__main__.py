##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import argparse
import oauth2client.tools
import os
import sys

from pyprelude.file_system import make_path

from googlecalendar import __description__, __project_name__, __version__
from googlecalendar.calendar import run_demo
from googlecalendar.config import Config
from googlecalendar.credentials import get_credentials

def _do_dump(config, args):
    credentials = get_credentials(config, args)
    run_demo(credentials)

def _main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    config_dir = make_path(os.path.expanduser(os.environ.get("GOOGLE_CALENDAR_DIR", "~/.google-calendar")))
    config = Config(config_dir)

    parser = argparse.ArgumentParser(
        prog=__project_name__,
        description=__description__,
        parents=[oauth2client.tools.argparser])
    parser.add_argument("--version", action="version", version="{} version {}".format(__project_name__, __version__))

    subparsers = parser.add_subparsers(help="subcommand help")

    dump_parser = subparsers.add_parser("dump", help="Show calendar entries")
    dump_parser.set_defaults(func=_do_dump)

    args = parser.parse_args(argv)
    args.func(config, args)

if __name__ == "__main__":
    _main()