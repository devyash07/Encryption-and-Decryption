"""
Cryptographic utilities for secure file encryption and decryption.

This module handles:
- Secure password-based key derivation using PBKDF2-HMAC-SHA256
- AES-256-GCM authenticated encryption
- Random salt and nonce generation
- Encryption metadata management
"""

import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
import struct

# Cryptographic constants
SALT_SIZE = 32  # 256 bits for salt
NONCE_SIZE = 12  # 96 bits for GCM nonce (standard for GCM)
AES_KEY_SIZE = 32  # 256 bits for AES-256
PBKDF2_ITERATIONS = 100000  # High iteration count for security
VERSION = 1  # File format version


def generate_salt() -> bytes:
    """
    Generate a cryptographically secure random salt.
    
    Returns:
        bytes: Random salt of SALT_SIZE bytes
    """
    return os.urandom(SALT_SIZE)


def generate_nonce() -> bytes:
    """
    Generate a cryptographically secure random nonce for AES-GCM.
    
    Returns:
        bytes: Random nonce of NONCE_SIZE bytes
    """
    return os.urandom(NONCE_SIZE)


def derive_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Derive a 256-bit AES key from a password using PBKDF2-HMAC-SHA256.
    
    This function implements password-based key derivation:
    - Password is never used directly as the encryption key
    - Salt is used to prevent rainbow table attacks
    - High iteration count makes brute-force attacks computationally expensive
    
    Args:
        password (str): User's password (will be encoded to UTF-8)
        salt (bytes): Random salt for this key derivation
        
    Returns:
        bytes: Derived 256-bit AES key
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    
    key = kdf.derive(password.encode('utf-8'))
    return key


def encrypt_file(file_data: bytes, password: str) -> bytes:
    """
    Encrypt file data using AES-256-GCM with password-based key derivation.
    
    Encryption workflow:
    1. Generate random salt
    2. Derive 256-bit AES key from password using PBKDF2
    3. Generate random nonce
    4. Encrypt file data using AES-256-GCM
    5. Package: VERSION | SALT | NONCE | CIPHERTEXT | TAG
    
    Args:
        file_data (bytes): Original file content (binary)
        password (str): User's encryption password
        
    Returns:
        bytes: Encrypted file in format: [VERSION][SALT][NONCE][CIPHERTEXT+TAG]
        
    Raises:
        ValueError: If password is empty
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Generate random salt and nonce
    salt = generate_salt()
    nonce = generate_nonce()
    
    # Derive AES key from password
    key = derive_key_from_password(password, salt)
    
    # Perform AES-256-GCM encryption
    cipher = AESGCM(key)
    ciphertext = cipher.encrypt(nonce, file_data, None)
    
    # Package encrypted data: VERSION | SALT | NONCE | CIPHERTEXT+TAG
    # VERSION: 1 byte
    # SALT: 32 bytes
    # NONCE: 12 bytes
    # CIPHERTEXT+TAG: variable length (ciphertext + 16-byte authentication tag)
    encrypted_package = struct.pack('B', VERSION) + salt + nonce + ciphertext
    
    return encrypted_package


def decrypt_file(encrypted_data: bytes, password: str) -> bytes:
    """
    Decrypt file data using AES-256-GCM with password-based key derivation.
    
    Decryption workflow:
    1. Extract VERSION, SALT, NONCE from encrypted file
    2. Derive AES key from password using extracted SALT
    3. Extract CIPHERTEXT and authentication TAG
    4. Verify authentication tag and decrypt
    5. Return original file data
    
    Args:
        encrypted_data (bytes): Encrypted file content
        password (str): User's decryption password
        
    Returns:
        bytes: Decrypted file content (original data)
        
    Raises:
        ValueError: If password is empty, file is corrupted, or authentication fails
        cryptography.exceptions.InvalidTag: If authentication tag is invalid
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    try:
        # Extract metadata from encrypted file
        if len(encrypted_data) < 1 + SALT_SIZE + NONCE_SIZE + 16:
            raise ValueError("Encrypted file is corrupted (too small)")
        
        offset = 0
        
        # Extract VERSION
        version = struct.unpack('B', encrypted_data[offset:offset+1])[0]
        offset += 1
        
        if version != VERSION:
            raise ValueError(f"Unsupported encrypted file version: {version}")
        
        # Extract SALT
        salt = encrypted_data[offset:offset+SALT_SIZE]
        offset += SALT_SIZE
        
        # Extract NONCE
        nonce = encrypted_data[offset:offset+NONCE_SIZE]
        offset += NONCE_SIZE
        
        # Extract CIPHERTEXT+TAG (everything remaining)
        ciphertext = encrypted_data[offset:]
        
        if len(ciphertext) < 16:
            raise ValueError("Encrypted file is corrupted (no authentication tag)")
        
        # Derive AES key from password using extracted salt
        key = derive_key_from_password(password, salt)
        
        # Perform AES-256-GCM decryption
        cipher = AESGCM(key)
        plaintext = cipher.decrypt(nonce, ciphertext, None)
        
        return plaintext
        
    except ValueError:
        # Re-raise ValueError as-is
        raise
    except Exception as e:
        # Catch InvalidTag and other cryptography exceptions
        error_msg = str(e)
        if "InvalidTag" in type(e).__name__ or "authentication" in error_msg.lower():
            raise ValueError(
                "Decryption failed. The password may be incorrect or "
                "the encrypted file may have been modified."
            )
        else:
            raise ValueError(
                "Decryption failed. The password may be incorrect or "
                "the encrypted file may have been modified."
            )


def get_encryption_metadata(encrypted_data: bytes) -> dict:
    """
    Extract metadata from an encrypted file without decrypting it.
    
    Args:
        encrypted_data (bytes): Encrypted file content
        
    Returns:
        dict: Metadata including version and file size info
    """
    try:
        offset = 0
        version = struct.unpack('B', encrypted_data[offset:offset+1])[0]
        offset += 1
        
        encrypted_size = len(encrypted_data) - offset
        
        return {
            "version": version,
            "total_size": len(encrypted_data),
            "encrypted_payload_size": encrypted_size
        }
    except:
        return {"error": "Invalid encrypted file"}
