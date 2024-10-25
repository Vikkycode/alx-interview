#!/usr/bin/env python3
"""Log Parsing."""
import sys
import signal
import re

total_file_size = 0
status_codes = {}


def display_statistics():
    """Display the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


def process_line(line):
    """Process a single log line."""
    global total_file_size
    try:
        match = re.match(r'.+\[.+\] "GET .+" (\d+) (\d+)', line)
        if not match:
            return
        status_code, file_size = map(int, match.groups())
        total_file_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    except (ValueError, IndexError):
        return


def signal_handler(sig, frame):
    """Handle SIGINT (CTRL+C) signal."""
    display_statistics()

    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        process_line(line)
        if line_count % 10 == 0:
            display_statistics()
    display_statistics()
