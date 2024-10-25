#!/usr/bin/env python3
"""Parse logs, compute metrics."""
import sys
import signal
import re


def show_stats(file_size, status_counts):
    """Print accumulated statistics."""
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


def parse_log_line(line, file_size, status_counts):
    """Extract data from a single log line."""
    try:
        match = re.search(r'"\S+ \S+ \S+" (\d+) (\d+)', line)
        if not match:
            return file_size, status_counts
        status_code, size = map(int, match.groups())
        file_size += size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
        return file_size, status_counts
    except (ValueError, IndexError):
        return file_size, status_counts


def handle_interrupt(sig, frame, file_size, status_counts):
    """Handle SIGINT (CTRL+C) signal."""
    show_stats(file_size, status_counts)
    sys.exit(0)


if __name__ == "__main__":
    file_size_total = 0
    status_code_counts = {}
    signal.signal(signal.SIGINT, lambda sig, frame: (
        handle_interrupt(sig, frame, file_size_total, status_code_counts))
    )
    count = 0
    for line in sys.stdin:
        count += 1
        file_size_total, status_code_counts = (
            parse_log_line(line, file_size_total, status_code_counts)
        )
        if count % 10 == 0:
            show_stats(file_size_total, status_code_counts)
    show_stats(file_size_total, status_code_counts)
