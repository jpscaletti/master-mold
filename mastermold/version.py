import pkg_resources


try:
    __version__ = pkg_resources.require("mastermold")[0].version
except Exception:
    # Run pytest without needing to install the library
    __version__ = None
