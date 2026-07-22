#!/usr/bin/env python3
"""Stable CLI entry point for structured adapter conformance validation v2."""

from conformance_validation import *  # noqa: F401,F403
from conformance_validation import cli


if __name__ == "__main__":
    raise SystemExit(cli())
