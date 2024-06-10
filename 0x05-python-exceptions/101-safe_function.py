#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (ValueError, TypeError, NameError, ZeroDivisionError, IndexError) as e:
        print(f"Exception:{e}", file=sys.stderr)
        return (None)
