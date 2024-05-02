import sys

def parse_line(line):
    """
    Parses a log line and extracts relevant information.
    Returns a tuple (status_code, file_size) or None if the line format is invalid.
    """
    try:
        _, _, request, status_code, file_size = line.split()
        if request != '"GET /projects/260 HTTP/1.1"':
            return None
        return int(status_code), int(file_size)
    except ValueError:
        return None

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f"Total file size: {total_size}")
                    for code in sorted(status_counts.keys()):
                        if status_counts[code] > 0:
                            print(f"{code}: {status_counts[code]}")
                    print()

    except KeyboardInterrupt:
        # User interrupted the script
        print("\nScript interrupted by user.")
        print(f"Total file size: {total_size}")
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")

if __name__ == "__main__":
    main()