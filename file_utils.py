"""
File handling utilities for encryption and decryption.

This module handles:
- Reading files as binary data
- Writing encrypted files
- Filename management and preservation
- File size validation
"""

import os
from pathlib import Path


def read_file_as_bytes(file_path: str) -> bytes:
    """
    Read a file as binary data (works for any file type).
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        bytes: File content as binary data
        
    Raises:
        FileNotFoundError: If file does not exist
        IOError: If file cannot be read
        PermissionError: If user lacks read permissions
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


def write_file_from_bytes(file_path: str, data: bytes) -> None:
    """
    Write binary data to a file.
    
    Args:
        file_path (str): Path where file should be written
        data (bytes): Binary data to write
        
    Raises:
        IOError: If file cannot be written
        PermissionError: If user lacks write permissions
    """
    try:
        # Create parent directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'wb') as f:
            f.write(data)
    except PermissionError:
        raise PermissionError(f"Permission denied writing file: {file_path}")
    except IOError as e:
        raise IOError(f"Error writing file: {e}")


def get_encrypted_filename(original_path: str) -> str:
    """
    Generate encrypted filename by appending .enc extension.
    
    Example: document.pdf -> document.pdf.enc
    
    Args:
        original_path (str): Original file path
        
    Returns:
        str: Encrypted filename path
    """
    return original_path + ".enc"


def get_decrypted_filename(encrypted_path: str) -> str:
    """
    Generate decrypted filename by removing .enc extension.
    
    If the original extension is known and preserved in the encrypted file,
    this recovers the original filename.
    
    Example: document.pdf.enc -> document_decrypted.pdf
    
    Args:
        encrypted_path (str): Encrypted file path
        
    Returns:
        str: Decrypted filename path with "_decrypted" suffix
    """
    path = Path(encrypted_path)
    
    # Remove .enc extension if present
    if path.suffix == '.enc':
        base_path = str(path.with_suffix(''))
    else:
        base_path = encrypted_path
    
    # Add _decrypted suffix before final extension
    base_path_obj = Path(base_path)
    if base_path_obj.suffix:
        # Has extension: document.pdf -> document_decrypted.pdf
        result = str(base_path_obj.with_stem(base_path_obj.stem + '_decrypted'))
    else:
        # No extension: document -> document_decrypted
        result = base_path + '_decrypted'
    
    return result


def get_file_size_formatted(file_path: str) -> str:
    """
    Get human-readable file size.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        str: Formatted file size (e.g., "1.5 MB")
    """
    try:
        size_bytes = os.path.getsize(file_path)
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        
        return f"{size_bytes:.1f} TB"
    except:
        return "Unknown"


def validate_file_exists(file_path: str) -> bool:
    """
    Check if file exists and is readable.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        bool: True if file exists and is readable, False otherwise
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)


def validate_file_writable(file_path: str) -> bool:
    """
    Check if file can be written to (or if parent directory is writable).
    
    Args:
        file_path (str): Path to file
        
    Returns:
        bool: True if file can be written, False otherwise
    """
    parent_dir = os.path.dirname(file_path)
    if not parent_dir:
        parent_dir = '.'
    
    return os.access(parent_dir, os.W_OK)


def get_file_info(file_path: str) -> dict:
    """
    Get information about a file.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        dict: File information including name, size, path
    """
    try:
        path_obj = Path(file_path)
        return {
            "name": path_obj.name,
            "size": os.path.getsize(file_path),
            "size_formatted": get_file_size_formatted(file_path),
            "path": os.path.abspath(file_path),
            "exists": True
        }
    except:
        return {
            "name": None,
            "size": None,
            "size_formatted": None,
            "path": file_path,
            "exists": False
        }
