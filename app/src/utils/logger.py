import logging
"""
logging levels:
INFO: Confirmation that things are working as expected.
DEBUG: Detailed information for diagnosing issues.
WARNING: An indication of something unexpected or a potential problem.
ERROR: A serious issue that prevents part of the program from functioning.
CRITICAL: A severe error that may cause the program to terminate.
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)