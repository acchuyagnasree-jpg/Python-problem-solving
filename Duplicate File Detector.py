import os
import hashlib


def calculate_hash(file_path):
    hasher = hashlib.md5()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hasher.update(chunk)

        return hasher.hexdigest()

    except (PermissionError, OSError):
        return None


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, folders, files in os.walk(folder):

        for filename in files:
            file_path = os.path.join(root, filename)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in hashes:
                duplicates.append((hashes[file_hash], file_path))
            else:
                hashes[file_hash] = file_path

    return duplicates


folder = input("Enter folder path: ")

if os.path.exists(folder):

    duplicates = find_duplicates(folder)

    if duplicates:
        print("\nDuplicate files found:\n")

        for original, duplicate in duplicates:
            print("Original :", original)
            print("Duplicate:", duplicate)
            print("-" * 60)

    else:
        print("\nNo duplicate files found.")

else:
    print("Folder does not exist.")
