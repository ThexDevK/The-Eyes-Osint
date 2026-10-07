#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
THE EYES - Advanced Website OSINT Intelligence Tool
Version: 1.0.0
Author: ThexDevK
License: MIT

A powerful, all-in-one OSINT tool for extracting comprehensive 
intelligence from any website.
"""

import sys
import json
import socket
import ssl
import re
import subprocess
import urllib.request
import urllib.error
from datetime import datetime
from urllib.parse import urlparse, urljoin
import argparse

# Colors for terminal output
class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96
