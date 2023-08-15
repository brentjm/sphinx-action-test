#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is the entrypoint for a Docker container that builds a Sphinx
documentation site. It is intended to be used as part of a Github Action
workflow.
"""
__author__ = "Brent Maranzano"
__version__ = "1.0.0"
__license__ = "MIT"


import os
import logging
import sphinx.action as action

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("[sphinx-action] Starting sphinx-action build.")

    if "INPUT_PRE-BUILD-COMMAND" in os.environ:
        pre_command = os.environ["INPUT_PRE-BUILD-COMMAND"]
        logging.info(f"Running: {pre_command}")
        os.system(pre_command)

    github_env = action.GithubEnvironment(
        build_command=os.environ.get("INPUT_BUILD-COMMAND"),
    )

    action.build_all_docs(github_env, [os.environ.get("INPUT_DOCS-FOLDER")])
