"""Basic Antivirus Scanner — beginner-friendly educational project."""

from pathlib import Path

# Fake test signatures for learning only. These are NOT real malware signatures.
SIGNATURES = [
    b"DEMO_MALWARE_MARKER",
    b"ANTIVIRUS_DEMO_TEST_PATTERN",
]


def scan_file(file_path):
    """Return True when one of the demonstration signatures is found."""
    try:
        with open(file_path, "rb") as file:
            content = file.read()

        for signature in SIGNATURES:
            if signature in content:
                return True

        return False
    except OSError as error:
        print(f"Could not read {file_path}: {error}")
        return False


def main():
    folder = Path("sample_files")

    if not folder.exists():
        print("Error: the 'sample_files' folder was not found.")
        return

    print("Basic Antivirus Scanner")
    print("=======================")

    files_scanned = 0
    matches_found = 0

    for file_path in folder.iterdir():
        if file_path.is_file():
            files_scanned += 1
            if scan_file(file_path):
                matches_found += 1
                print(f"[ALERT] Demo marker found: {file_path.name}")
            else:
                print(f"[CLEAN] No demo marker found: {file_path.name}")

    print("-----------------------")
    print(f"Files scanned: {files_scanned}")
    print(f"Demo marker matches: {matches_found}")
    print("Note: This is an educational demo, not real antivirus software.")


if __name__ == "__main__":
    main()
