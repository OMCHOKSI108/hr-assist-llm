"""Entrypoint to run the Streamlit app from the `frontend/` folder.
This module ensures the project root is on sys.path so top-level imports
(`backend`, etc.) work when Streamlit runs the script from `frontend/`.
It then imports the top-level `app` module so the original Streamlit app
executes as before.
"""
from importlib import import_module
import sys
import os

# Prepend the repository root (parent of this file) to sys.path so
# imports like `backend.config` resolve when Streamlit executes the
# script with CWD set to the frontend folder.
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

# Import the original top-level Streamlit app module so its code executes
import_module('app')

