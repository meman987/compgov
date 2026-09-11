#!/usr/bin/env python3
import sys
import subprocess
import secrets
import string
import os
from datetime import datetime
from pathlib import Path

def generate_password():
    """Generate a random 16-character password."""
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(16))

def commit_and_push(archive_file):
    """Commit and push the archive file to git."""
    try:
        # Check if in a git repository
        subprocess.run(["git", "rev-parse", "--git-dir"],
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Stage the archive file
        subprocess.run(["git", "add", archive_file], check=True)

        # Create commit
        commit_msg = f"Add {os.path.basename(archive_file)}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)

        # Push to remote
        subprocess.run(["git", "push", "origin", "HEAD"], check=True)

        print("  Committed and pushed to git")
        return True
    except subprocess.CalledProcessError:
        return False

def create_archive(archive_type, files, password=None, commit=True):
    """Create a zip or 7z archive with optional password."""
    if not files:
        print(f"Usage: archive {archive_type} [--rpass|--pass PASSWORD] [--no-commit] <file1> [file2] ...")
        sys.exit(1)

    # Verify all files exist
    for f in files:
        if not Path(f).exists():
            print(f"Error: File not found: {f}")
            sys.exit(1)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = f"archive_{timestamp}.{archive_type}"

    if archive_type == "7z":
        if password:
            cmd = ["7z", "a", f"-p{password}", archive_file] + files
        else:
            cmd = ["7z", "a", archive_file] + files
        subprocess.run(cmd, stdout=subprocess.DEVNULL, check=True)

    elif archive_type == "zip":
        if password:
            cmd = ["zip", "-e", "-P", password, archive_file] + files
        else:
            cmd = ["zip", archive_file] + files
        subprocess.run(cmd, stdout=subprocess.DEVNULL, check=True)

    print(f"\n✓ Archive created: {archive_file}")
    if password:
        print(f"  Password: {password}")
    print(f"  Files: {', '.join(files)}")

    if commit:
        if not commit_and_push(archive_file):
            print("  ⚠️  Warning: Could not commit/push (not in a git repo or push failed)")

def main():
    if len(sys.argv) < 3:
        print("Usage: archive <7z|zip> [--rpass|--pass PASSWORD] [--no-commit] <file1> [file2] ...")
        sys.exit(1)

    archive_type = sys.argv[1]
    args = sys.argv[2:]

    password = None
    files = []
    commit = True

    # Parse arguments
    i = 0
    while i < len(args):
        if args[i] == "--rpass":
            password = generate_password()
            i += 1
        elif args[i] == "--pass":
            if i + 1 >= len(args):
                print("Error: --pass requires a password argument")
                sys.exit(1)
            password = args[i + 1]
            i += 2
        elif args[i] == "--no-commit":
            commit = False
            i += 1
        else:
            files.append(args[i])
            i += 1

    create_archive(archive_type, files, password, commit)

if __name__ == "__main__":
    main()
