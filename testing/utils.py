"""Utility function used in testing."""

import os


def read_test_data_file(filename: str):
    """Read in XML test data file."""
    here = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(here, "test_data", filename)
    with open(xml_file, encoding="utf-8") as infile:
        return infile.read()
