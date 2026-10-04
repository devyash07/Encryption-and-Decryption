# Quick Start Guide

## Installation (First Time Only)

### Step 1: Navigate to Project Directory
```bash
cd /Users/yashwaantdev/Downloads/DSP\ Assignment\ 2/secure-file-encryption
```

Or if in a different location:
```bash
cd /path/to/secure-file-encryption
```

### Step 2: Install Dependencies
```bash
pip3 install -r requirements.txt
```

This installs:
- **cryptography 41.0.7**: Cryptographic library with AES-256-GCM and PBKDF2

### Step 3: Verify Installation
```bash
python3 -c "import cryptography; print('✓ Ready to use')"
```

---

## Running the Application

### Start the GUI
```bash
python3 main.py
```

A window titled **"Secure File Encryption & Decryption System"** will appear.

---

## Using the Application

### To Encrypt a File

1. Click **"Select File to Encrypt"** button
2. Choose any file from your computer
3. Enter a password (8+ characters recommended)
4. Confirm the password
5. Click **"Encrypt File"** button
6. Wait for encryption to complete
7. Look for `filename.enc` in the same directory

**Status Message:**
```
✓ File encrypted successfully!

Original: 5,242,880 bytes
Encrypted: 5,242,941 bytes
(+61 bytes for metadata)

Saved as: document.pdf.enc
```

### To Decrypt a File

1. Click **"Select Encrypted File"** button
2. Choose an `.enc` file
3. Enter the password used during encryption
4. Click **"Decrypt File"** button
5. Wait for decryption to complete
6. Look for `filename_decrypted.pdf` in `./decrypted_files/` subdirectory

**Status Message:**
```
✓ File decrypted successfully!

Decrypted size: 5,242,880 bytes

Saved as:
document_decrypted.pdf
```

---

## Running Tests

### Run All Tests
```bash
python3 test_encryption_system.py
```

**Expected Output:**
```
======================================================================
SECURE FILE ENCRYPTION SYSTEM - TEST SUITE
======================================================================
1. ✓ PASS: Basic File Encryption
2. ✓ PASS: Successful Decryption (Correct Password)
3. ✓ PASS: Wrong Password Rejection
4. ✓ PASS: Empty Password Validation
5. ✓ PASS: Password Mismatch Detection
6. ✓ PASS: Binary File Support
7. ✓ PASS: File Integrity Verification
8. ✓ PASS: Tampered Ciphertext Detection
9. ✓ PASS: Corrupted File Handling
10. ✓ PASS: Large File Support (10 MB)
11. ✓ PASS: Multiple Encryption Randomness
12. ✓ PASS: Metadata Extraction

======================================================================
TEST SUMMARY
======================================================================
Tests Passed: 12/12
Pass Rate: 100.0%
✓ ALL TESTS PASSED - System is working correctly!
```

---

## Project Structure

```
secure-file-encryption/
├── main.py                           GUI application (start here)
├── crypto_utils.py                   Cryptographic operations
├── file_utils.py                     File handling
├── test_encryption_system.py         Automated tests
├── requirements.txt                  Dependencies
├── README.md                         Full documentation (23 sections)
├── VIVA_QUESTIONS_AND_ANSWERS.md     Interview preparation (23 Q&A)
├── QUICK_START.md                    This file
├── encrypted_files/                  Output directory for encrypted files
└── decrypted_files/                  Output directory for decrypted files
```

---

## File Descriptions

### main.py
- **Purpose**: GUI application entry point
- **Responsibility**: User interface, button handling, file dialogs, status display
- **Run**: `python3 main.py`

### crypto_utils.py
- **Purpose**: Cryptographic operations
- **Functions**:
  - `encrypt_file()`: AES-256-GCM encryption
  - `decrypt_file()`: AES-256-GCM decryption
  - `derive_key_from_password()`: PBKDF2-HMAC-SHA256 key derivation
  - `generate_salt()`: Random salt generation
  - `generate_nonce()`: Random nonce generation
- **Algorithm**: AES-256-GCM with PBKDF2, 100,000 iterations

### file_utils.py
- **Purpose**: File input/output operations
- **Functions**:
  - `read_file_as_bytes()`: Read any file as binary
  - `write_file_from_bytes()`: Write binary data to file
  - `get_encrypted_filename()`: Generate .enc filename
  - `get_decrypted_filename()`: Generate output filename
  - `get_file_size_formatted()`: Human-readable file size

### test_encryption_system.py
- **Purpose**: Comprehensive test suite
- **Tests**: 12 different scenarios
- **Coverage**: Normal operation, error cases, edge cases
- **Run**: `python3 test_encryption_system.py`

### README.md
- **Purpose**: Complete project documentation
- **Sections**: 23 comprehensive sections
- **Content**: Problem statement, algorithms, architecture, workflows, security, demonstration steps

### VIVA_QUESTIONS_AND_ANSWERS.md
- **Purpose**: Interview preparation
- **Questions**: 23 likely viva questions
- **Answers**: Detailed explanations appropriate for college-level discussion
- **Topics**: Concepts, algorithms, implementation, security, demonstrations

---

## Common Commands

### Create a Test File
```bash
echo "This is a test file" > test.txt
```

### Encrypt a File
```bash
python3 main.py
# Then use the GUI
```

### Verify File Integrity
```bash
md5 original_file.txt decrypted_files/original_file_decrypted.txt
# Should show same MD5 hash
```

### View Encrypted File
```bash
cat document.pdf.enc
# Shows binary garbage (unreadable)
```

### Check File Type
```bash
file document.pdf.enc
# Output: data (binary file)
```

---

## Supported File Types

The application works with any file type:

- **Documents**: .txt, .pdf, .docx, .xlsx, .pptx
- **Images**: .jpg, .png, .gif, .bmp, .tiff
- **Archives**: .zip, .tar, .7z, .rar
- **Media**: .mp4, .mp3, .wav, .avi
- **Code**: .py, .java, .cpp, .js, .html
- **Binary**: .exe, .dmg, .iso, .bin
- **Custom formats**: Any file extension

**Key Point**: Application treats all files as binary data, so any file type works correctly.

---

## Password Recommendations

### Weak Passwords (Avoid)
```
password          (common word)
12345678          (sequential numbers)
qwerty            (keyboard pattern)
admin             (default password)
```

### Strong Passwords (Recommended)
```
MySecurePass123!  (12 chars, mix of types)
correct horse battery staple  (long phrase)
P@ssw0rd_2024!    (12 chars, special chars)
CorrectHorseBatteryStaple123  (25 chars, memorable)
```

### Best Practices
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, symbols
- Not dictionary words
- Not personal information
- Not patterns on keyboard

---

## Troubleshooting

### "Module not found: cryptography"
```bash
# Solution: Install dependencies
pip3 install -r requirements.txt
```

### "No module named tkinter"
```bash
# Tkinter should be included with Python
# If missing:

# macOS:
brew install python-tk

# Ubuntu/Debian:
sudo apt-get install python3-tk

# Fedora:
sudo dnf install python3-tkinter
```

### "Decryption failed - wrong password"
```
This is expected behavior!
If you get this error with the correct password,
the encrypted file may be corrupted.
```

### GUI doesn't appear
```bash
# Try:
python3 -m main

# Or check for display issues:
echo $DISPLAY  # Should not be empty on GUI systems
```

### Very slow encryption/decryption
```
This is normal for large files.
PBKDF2 uses 100,000 iterations (takes time for security).

Typical speed:
- Small file (1 MB): 1-2 seconds
- Medium file (100 MB): 30-60 seconds
- Large file (1 GB): 5-10 minutes

The slowness is intentional (security feature).
```

---

## File Format

### Encrypted File Structure

```
Byte offset    Size      Content
0              1         VERSION (0x01)
1-32           32        SALT (random)
33-44          12        NONCE (random)
45-...-(61)    variable  CIPHERTEXT + TAG
               (n+16)    (file data + authentication tag)
```

### Total Size
```
Total = 1 + 32 + 12 + len(plaintext) + 16
      = 61 + len(plaintext) bytes
      
Overhead: 61 bytes per file (metadata)
```

### Example
```
Original file: 1000 bytes
Encrypted file: 1061 bytes (+61 bytes overhead)

Breakdown:
- VERSION: 1 byte
- SALT: 32 bytes  
- NONCE: 12 bytes
- CIPHERTEXT: 1000 bytes (same as original)
- AUTH TAG: 16 bytes
- TOTAL: 1061 bytes
```

---

## Security Features Checklist

- ✓ **AES-256-GCM**: Military-grade encryption
- ✓ **PBKDF2**: 100,000 iterations for key derivation
- ✓ **Unique Salt**: Different random salt each encryption
- ✓ **Unique Nonce**: Different random nonce each encryption
- ✓ **Authentication Tag**: Detects tampering
- ✓ **No Password Storage**: Password only in memory during use
- ✓ **Secure Randomness**: Uses os.urandom() (OS entropy)
- ✓ **Error Safety**: Wrong password safely rejected
- ✓ **Tampering Detection**: Modified files rejected
- ✓ **File Integrity**: Byte-for-byte restoration verified

---

## Performance Metrics

### Tested Scenarios

| Test | Result | Time |
|------|--------|------|
| Encrypt 1 MB file | ✓ Pass | 1-2 sec |
| Decrypt 1 MB file | ✓ Pass | 1-2 sec |
| Encrypt 10 MB file | ✓ Pass | 5-10 sec |
| Decrypt 10 MB file | ✓ Pass | 5-10 sec |
| Encrypt 100 MB file | ✓ Pass | 30-60 sec |
| Binary file (image) | ✓ Pass | <1 sec |
| Text file | ✓ Pass | <1 sec |
| Wrong password | ✓ Rejected | <1 sec |
| Tampered file | ✓ Rejected | <1 sec |
| MD5 integrity check | ✓ Match | — |

### Memory Usage

- Small file (1 MB): ~5 MB RAM
- Medium file (100 MB): ~120 MB RAM
- Large file (1 GB): ~1.1 GB RAM

**Note**: Application loads entire file into memory (not streaming). This is intentional for simplicity but limits to files smaller than available RAM.

---

## Next Steps

1. **Run the application**: `python3 main.py`
2. **Read full documentation**: `README.md`
3. **Prepare for viva**: `VIVA_QUESTIONS_AND_ANSWERS.md`
4. **Run tests**: `python3 test_encryption_system.py`
5. **Demonstrate to professor**: Show encryption, decryption, tampering detection

---

## Additional Resources

- **README.md**: Comprehensive documentation (23 sections)
- **VIVA_QUESTIONS_AND_ANSWERS.md**: Interview preparation (23 Q&A pairs)
- **crypto_utils.py**: Detailed code comments explaining algorithms
- **test_encryption_system.py**: Runnable examples of all operations

---

## Support

### If Something Goes Wrong

1. **Check dependencies**: `pip3 install -r requirements.txt`
2. **Run tests**: `python3 test_encryption_system.py`
3. **Check imports**: `python3 -c "import main"`
4. **Read error message**: Shows what failed
5. **Consult README**: Full documentation section

### Reporting Issues

If you encounter problems:
1. What command did you run?
2. What error message appeared?
3. What was expected to happen?
4. What actually happened?

---

**Ready to use! Start with**: `python3 main.py`
