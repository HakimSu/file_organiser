def list_files(path):
    """
    List all files in the given directory path.

    Args:
        path (str): The directory path to list files from.

    Returns:
        list: A list of file names in the specified directory.
    """
    import os

    try:
        # Get a list of all files in the directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except Exception as e:
        print(f"Error listing files in {path}: {e}")
        return []
def get_extension(filename):
    """
    Get the file extension from a filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The file extension.
    """
    return os.path.splitext(filename)[1]