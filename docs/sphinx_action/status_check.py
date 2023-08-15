# -*- coding: utf-8 -*-

"""
This module interacts with the Github Actions API to create in-line warnings
and errors.
"""
__author__ = "Brent Maranzano"
__version__ = "1.0.0"
__license__ = "MIT"


import collections
import sys


class AnnotationLevel:
    # Notices are not currently supported.
    # NOTICE = "notice"
    WARNING = "warning"
    FAILURE = "failure"


CheckAnnotation = collections.namedtuple(
    "CheckAnnotation", ["path", "start_line", "end_line", "annotation_level", "message"]
)


def output_annotation(annotation, where_to_print=sys.stdout):
    """
    This method is responsible for printing the annotation to the correct
    output stream.

    Args:
        annotation (CheckAnnotation): The annotation to print
        where_to_print (file): The file to print to, defaults to stdout

    Returns:
        None
    """
    level_to_command = {
        AnnotationLevel.WARNING: "warning",
        AnnotationLevel.FAILURE: "error",
    }

    command = level_to_command[annotation.annotation_level]

    print(
        "::{command} file={file},line={line}::{message}".format(
            command=command,
            file=annotation.path,
            line=annotation.start_line,
            message=annotation.message,
        ),
        file=where_to_print,
    )
