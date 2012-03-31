##
# Copyright 2009-2012 Stijn Deweirdt, Dries Verdegem, Kenneth Hoste, Pieter De Baets, Jens Timmerman
#
# This file is part of EasyBuild,
# originally created by the HPC team of the University of Ghent (http://ugent.be/hpc).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
This initializes EasyBuild.
The EasyBuild version is defined here in VERSION,
appended by the git commit id in VERBOSE_VERSION.
"""
from distutils.version import LooseVersion
import os
import sys

VERSION = LooseVersion("0.5")


def get_git_revision():
    """
    Returns the git revision (e.g. aab4afc016b742c6d4b157427e192942d0e131fe),
    or UNKNOWN is getting the git revision fails

    relies on GitPython (see http://gitorious.org/git-python)
    """
    try:
        import git
    except ImportError:
        return "UNKNOWN"
    try:
        path = os.path.dirname(__file__)
        gitrepo = git.Git(path)
        return gitrepo.rev_list("HEAD").splitlines()[0]
    except git.GitCommandError:
        return "UNKNOWN"

VERBOSE_VERSION = LooseVersion("%s-r%s" % (VERSION, get_git_revision()))

# make sure that required Python modules are present,
# because EasyBuild will not work properly without it (and you won't notice)
try:
    import pkg_resources
except ImportError, err:
    sys.stderr.write("Failed to import pkg_resources module: %s\n" % err)
    sys.stderr.write("Please make sure that the pkg_resources module is available for your Python environment.")
    sys.stderr.write("See http://pypi.python.org/pypi/setuptools.")
    sys.exit(1)