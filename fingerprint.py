import hashlib


def generate_fingerprint(uploaded_file):
    sha256 = hashlib.sha256()

    file_data = uploaded_file.getvalue()

    sha256.update(file_data)

    return sha256.hexdigest()