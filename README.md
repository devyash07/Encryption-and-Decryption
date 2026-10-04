# Secure File Encryption and Decryption System

**Data Security and Privacy - College Programming Assignment**

---

## 1. Project Title

**Secure File Encryption and Decryption System**

A desktop application that demonstrates secure file encryption using modern cryptographic algorithms and best practices.

---

## 2. Problem Statement

**How can we protect confidential files from unauthorized access?**

In today's digital world, sensitive documents, personal files, and confidential data are constantly at risk of unauthorized access. Whether stored on personal computers, shared drives, or backup systems, unencrypted files can be read by anyone with access to the storage medium.

This project addresses this security challenge by implementing a practical file encryption solution that:
- Protects file contents using strong encryption
- Prevents unauthorized access without the correct password
- Detects tampering or modifications to encrypted files
- Works with any file type (documents, images, archives, etc.)

---

## 3. Introduction

This project demonstrates the practical application of cryptographic principles to solve a real-world security problem: protecting files from unauthorized access.

The system uses **AES-256-GCM** (Advanced Encryption Standard with 256-bit keys in Galois/Counter Mode) for authenticated encryption, combined with **PBKDF2** (Password-Based Key Derivation Function 2) for secure key derivation from user passwords.

---

## 4. Motivation

**Why is this important?**

1. **Confidentiality**: Files contain sensitive information that must remain private
2. **Privacy**: Personal data should only be accessible to authorized individuals
3. **Compliance**: Many regulations (GDPR, HIPAA, etc.) require data encryption
4. **Security**: Strong cryptography is the foundation of data protection
5. **Trust**: Users need confidence that their files are secure

This project shows students how these concepts translate into working code.

---

## 5. Objectives

By completing this project, we demonstrate:

1. **Understanding of Encryption**: Implementing symmetric encryption for file protection
2. **Password Security**: Using password-based key derivation instead of direct password usage
3. **Authenticated Encryption**: Implementing AES-GCM to ensure both confidentiality and integrity
4. **Secure Random Number Generation**: Using cryptographically secure randomness
5. **Error Handling**: Providing clear error messages without exposing security details
6. **User Interface Design**: Creating an intuitive GUI for cryptographic operations
7. **Software Engineering**: Organizing code into modular, maintainable components

---

## 6. Security Problem

**Scenario:**

Alice has confidential project files stored on her computer. She is concerned that:
- If her computer is stolen, thieves can access her files
- If she uses cloud storage, the service provider shouldn't read her files
- If files are transferred, they might be intercepted
- Backup copies might be accessible to unauthorized people

**Traditional Solution (Insecure):**
- Store files in a "secure folder" (not actually encrypted)
- Use weak passwords
- Store files with obvious names
- No authentication or tampering detection

**Better Solution (This Project):**
- Use AES-256-GCM encryption (military-grade security)
- Derive encryption keys from passwords using PBKDF2 (resistant to brute-force)
- Generate unique random salt and nonce for every encryption (prevents patterns)
- Use authenticated encryption (detects tampering)
- Never store the password (only the derived key)

---

## 7. Proposed Solution

**System Architecture:**

```
┌──────────────────────────────────────────────────────────┐
│                  User Interface (Tkinter)                │
│  - File Selection Dialogs                                │
│  - Password Entry Fields                                 │
│  - Status Messages                                       │
└──────────────┬───────────────────────────────────────────┘
               │
┌──────────────┴───────────────────────────────────────────┐
│               Application Logic (main.py)                │
│  - Button Click Handlers                                 │
│  - Input Validation                                      │
│  - Error Handling                                        │
└──────────────┬───────────────────────────────────────────┘
               │
┌──────────────┴───────────────────────────────────────────┐
│            Cryptographic Operations (crypto_utils.py)    │
│  - PBKDF2 Key Derivation                                 │
│  - AES-256-GCM Encryption/Decryption                    │
│  - Random Salt & Nonce Generation                        │
└──────────────┬───────────────────────────────────────────┘
               │
┌──────────────┴───────────────────────────────────────────┐
│              File Operations (file_utils.py)             │
│  - Binary File Reading/Writing                           │
│  - Filename Management                                   │
│  - File Validation                                       │
└──────────────────────────────────────────────────────────┘
```

**Key Components:**

1. **Graphical User Interface**: Tkinter-based desktop application
2. **Encryption Module**: AES-256-GCM with PBKDF2 key derivation
3. **File Handler**: Binary file I/O for any file type
4. **Error Management**: User-friendly error messages
5. **Secure Randomness**: Cryptographically secure random number generation

---

## 8. Technologies Used

### Programming Language
- **Python 3.8+**: Modern, readable, perfect for educational projects

### Libraries
- **cryptography**: Industry-standard cryptographic library
  - Provides AES-GCM implementation
  - Provides PBKDF2-HMAC-SHA256
  - Backed by OpenSSL/BoringSSL
  - Production-ready and audited

- **tkinter**: Python's standard GUI library
  - Built into Python
  - Simple and effective for desktop applications
  - No external dependencies for GUI

### Tools
- **Python Package Manager (pip)**: For dependency installation

---

## 9. Cryptographic Algorithms Used

### AES-256-GCM (Advanced Encryption Standard)

**What is it?**
- Symmetric block cipher (same key for encryption and decryption)
- 256-bit key size (2^256 possible keys)
- GCM mode: Provides both encryption AND authentication
- Industry standard (used by governments, banks, enterprises)

**How it works:**
```
Plaintext (Original File)
    ↓
AES Encryption Transform
    ↓
Ciphertext + Authentication Tag (Encrypted File)
    ↓
AES Decryption Transform (requires correct key)
    ↓
Plaintext (Original File Recovered)
```

**Why GCM mode?**
- Provides Confidentiality (encryption)
- Provides Integrity (authentication tag detects tampering)
- Efficient (can process data in parallel)
- Authenticated (detects if ciphertext was modified)

**Key size: 256-bit**
- Provides 2^256 ≈ 1.15 × 10^77 possible keys
- Considered secure against all known attacks
- Even quantum computers (in theory) wouldn't break it in reasonable time

---

### PBKDF2-HMAC-SHA256 (Password-Based Key Derivation Function)

**What is it?**
- Derives cryptographic keys from passwords
- Uses HMAC-SHA256 as the underlying hash function
- Applies many iterations to slow down brute-force attacks
- Standard: NIST SP 800-132

**Why not use password directly as key?**
- Passwords are typically 8-50 characters (low entropy)
- AES keys must be truly random (high entropy)
- Users can't remember random 256-bit numbers
- PBKDF2 bridges this gap securely

**How it works:**

```
User Password: "MySecurePassword123!"
              ↓
    PBKDF2 (100,000 iterations)
              ↓
          Salt (32 random bytes)
              ↓
    256-bit Derived Key
              ↓
    AES-256-GCM Encryption Key
```

**Iteration count: 100,000**
- Each iteration takes ~1 millisecond
- Slows down password guessing (100,000 iterations = 100 seconds per attempt)
- Makes brute-force attacks impractical
- Standard for modern applications (OWASP recommends 100,000+)

---

### Salt (Random)

**What is it?**
- Random data mixed with the password before key derivation
- Different salt for every encryption
- Stored in the encrypted file (doesn't need to be secret)

**Why use salt?**
- Prevents rainbow table attacks
- Even if two users have the same password, they get different keys
- Adds randomness to the key derivation process

```
Password: "password123"
Salt #1 (Random): [32 random bytes]
         ↓
      PBKDF2
         ↓
      Key #1

Password: "password123" (same)
Salt #2 (Random): [32 different random bytes]
         ↓
      PBKDF2
         ↓
      Key #2 (completely different from Key #1)
```

---

### Nonce (Initialization Vector for GCM)

**What is it?**
- Random data used to initialize the encryption mode
- 96 bits (12 bytes) for GCM
- Different nonce for every encryption
- Stored in the encrypted file (doesn't need to be secret)

**Why use nonce?**
- Prevents pattern recognition attacks
- Must never be reused with the same key
- Makes identical plaintexts encrypt to different ciphertexts

```
Plaintext: "secret.txt contents"
Key: [same across multiple encryptions]
Nonce #1: [random 12 bytes]
    ↓
Ciphertext #1 (completely different appearance)

Plaintext: "secret.txt contents" (same)
Key: [same across multiple encryptions]
Nonce #2: [different random 12 bytes]
    ↓
Ciphertext #2 (completely different from Ciphertext #1)
```

---

## 10. System Architecture

**Data Flow:**

```
┌─────────────────────────────────────────────────────────┐
│                     USER INTERACTION                    │
└────────────────────────┬────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
   ENCRYPTION                        DECRYPTION
        │                                 │
        ├─ Select File                    ├─ Select .enc File
        ├─ Enter Password                 ├─ Enter Password
        ├─ Confirm Password               └─ Click Decrypt
        └─ Click Encrypt
        
        ▼                                 ▼
   ┌────────────────────────────────────────────┐
   │  Read File as Binary Bytes                 │
   │  Validate Inputs                           │
   └────────────┬─────────────────────────────┘
                │
   ┌────────────▼─────────────────────────────┐
   │  Generate Random Salt (32 bytes)          │
   │  Derive Key: PBKDF2(password, salt)      │
   │  Generate Random Nonce (12 bytes)         │
   └────────────┬─────────────────────────────┘
                │
   ┌────────────▼─────────────────────────────┐
   │  AES-256-GCM Encryption/Decryption        │
   │  Produce Ciphertext + Auth Tag            │
   └────────────┬─────────────────────────────┘
                │
   ┌────────────▼─────────────────────────────┐
   │  Package Format:                          │
   │  [VERSION | SALT | NONCE | CIPHER + TAG] │
   └────────────┬─────────────────────────────┘
                │
                ▼
   ┌────────────────────────────────────────────┐
   │  Write to File (.enc or restored)         │
   │  Clear Sensitive Data from Memory          │
   │  Display Success/Error Message             │
   └────────────────────────────────────────────┘
```

---

## 11. Encryption Workflow

**Step-by-step encryption process:**

```
1. USER INITIATES
   │ User selects file for encryption
   └─→ Application reads entire file as binary
   
2. PASSWORD VALIDATION
   │ User enters password
   │ User confirms password
   └─→ Application verifies passwords match

3. KEY DERIVATION
   │ Generate random Salt (32 bytes using os.urandom)
   │ Derive Key from Password: PBKDF2-HMAC-SHA256
   │   - Input: password (UTF-8 encoded)
   │   - Salt: random bytes from step 1
   │   - Iterations: 100,000 (PBKDF2)
   │   - Output: 256-bit key
   └─→ Key is suitable for AES-256

4. ENCRYPTION SETUP
   │ Generate random Nonce (12 bytes using os.urandom)
   │ Initialize AES-256-GCM cipher with derived key
   └─→ Ready for encryption

5. ENCRYPT DATA
   │ AES-256-GCM Encryption:
   │   - Input: plaintext (original file bytes)
   │   - Key: derived 256-bit key
   │   - Nonce: random 12-byte nonce
   │   - Output: ciphertext + authentication tag (16 bytes)
   └─→ Ciphertext is same size as plaintext
       Authentication tag adds 16 bytes

6. PACKAGE FOR STORAGE
   │ Create encrypted file format:
   │   [1 byte: VERSION]
   │   [32 bytes: SALT]
   │   [12 bytes: NONCE]
   │   [n bytes: CIPHERTEXT + TAG]
   │
   │ Total size = 1 + 32 + 12 + len(plaintext) + 16
   │           = 61 + len(plaintext) bytes
   └─→ All components needed for decryption are included

7. SAVE TO DISK
   │ Write encrypted package to file
   │ Filename: original_filename.enc
   │ Location: same directory as original
   └─→ Encryption complete

8. CLEANUP
   │ Clear password fields from memory
   │ Display success message
   │ Show file size information
   └─→ Original password never stored anywhere

RESULT: ✓ File encrypted and protected
        ✓ Password not stored in file
        ✓ Unique salt per encryption
        ✓ Unique nonce per encryption
        ✓ Authentication tag for integrity
```

**Example:**

```
Original File: document.pdf (5 MB)
            ↓
    User enters password: "MySecurePass123!"
            ↓
    PBKDF2 derives key with random salt
            ↓
    AES-256-GCM encrypts with random nonce
            ↓
Encrypted File: document.pdf.enc (5 MB + 61 bytes)
```

---

## 12. Decryption Workflow

**Step-by-step decryption process:**

```
1. USER INITIATES
   │ User selects encrypted file (.enc)
   └─→ Application reads entire encrypted file as binary

2. EXTRACT METADATA
   │ Parse encrypted file format:
   │   - Read VERSION byte (check compatibility)
   │   - Read SALT (32 bytes)
   │   - Read NONCE (12 bytes)
   │   - Read remaining: CIPHERTEXT + TAG
   └─→ All required components extracted

3. PASSWORD ENTRY
   │ User enters password (same password used in encryption)
   └─→ Provided for key derivation

4. KEY DERIVATION
   │ Derive Key from Password: PBKDF2-HMAC-SHA256
   │   - Input: password (UTF-8 encoded)
   │   - Salt: extracted from encrypted file (step 2)
   │   - Iterations: 100,000 (same as encryption)
   │   - Output: 256-bit key
   │
   │ If password is correct: derived key matches original
   │ If password is wrong: derived key is completely different
   └─→ Key ready for decryption

5. DECRYPT DATA
   │ AES-256-GCM Decryption:
   │   - Input: ciphertext + tag (from step 2)
   │   - Key: derived 256-bit key
   │   - Nonce: extracted nonce (from step 2)
   │   - Output: plaintext (if authentication succeeds)
   │
   │ CRITICAL: Authentication verification
   │   - GCM mode verifies the authentication tag
   │   - If tag doesn't match:
   │     * Password is wrong, OR
   │     * File was modified/corrupted
   │   - Decryption fails safely
   │   - Plaintext is NOT returned
   └─→ Only returns plaintext if authentication passes

6. SAVE RESTORED FILE
   │ Write plaintext to file
   │ Filename: original_filename_decrypted.pdf
   │ Location: ./decrypted_files/ subdirectory
   └─→ Original file contents restored

7. CLEANUP
   │ Clear password field from memory
   │ Display success message
   │ Show restored file information
   └─→ Decryption complete

8. VERIFICATION
   │ Restored file should be byte-for-byte identical
   │ Original file unchanged (encryption doesn't modify)
   └─→ No data loss

RESULT: ✓ File decrypted and restored
        ✓ Correct password verified through key derivation
        ✓ Authentication tag verified
        ✓ Tampering detected if file modified
        ✓ Wrong password rejected
        ✓ Original file not modified
```

**Example:**

```
Encrypted File: document.pdf.enc (5 MB + 61 bytes)
            ↓
    User enters password: "MySecurePass123!"
            ↓
    Extract salt from encrypted file
            ↓
    PBKDF2 derives key using extracted salt
            ↓
    AES-256-GCM decrypts using extracted nonce
            ↓
    Authentication tag verified
            ↓
Restored File: decrypted_files/document_decrypted.pdf (5 MB)
```

---

## 13. Algorithm Explanation

### AES-256-GCM Encryption Algorithm

**Simplified Explanation (for college students):**

Think of AES like a complex mathematical lock:
- **Key (256-bit)**: Like a physically unique key
- **Plaintext**: The message you want to lock
- **Encryption**: The mathematical transformation that "locks" your message
- **Ciphertext**: The locked message (appears random, unreadable)
- **GCM Mode**: Also creates a "security seal" (authentication tag) to detect tampering

**In GCM Mode:**
1. AES performs block cipher operations on your data
2. Simultaneously computes an authentication tag
3. Anyone modifying the ciphertext will have a different tag
4. Receiver can detect modifications immediately

**Real-world analogy:**
```
┌─────────────────────────────┐
│  Original Message           │
│  "Confidential Report"      │
└────────────┬────────────────┘
             │
        AES Encryption
        (using derived key & nonce)
             │
┌────────────▼────────────────┐
│  Locked Message             │
│  "k7#$@!%^&*(JHgf8h2..."   │  ← Looks like random garbage
│  TAG: "A1B2C3D4..."        │  ← Security seal
└────────────────────────────┘
```

### Why AES-256?

| Aspect | Explanation |
|--------|-------------|
| **256-bit key** | 2^256 possible keys; brute-force would take longer than the age of the universe |
| **Block cipher** | Processes data in 128-bit blocks; very efficient |
| **Symmetric** | Same key for encryption and decryption |
| **NIST Standard** | Approved by National Institute of Standards and Technology |
| **Industry Use** | Used by governments, banks, and enterprises worldwide |

### Why PBKDF2?

| Aspect | Explanation |
|--------|-------------|
| **Iteration count** | 100,000 iterations make password guessing slow |
| **Salt** | Prevents rainbow tables and adds randomness |
| **HMAC-SHA256** | Cryptographically secure hash function |
| **NIST Approved** | Recommended standard in SP 800-132 |
| **No GPU Advantage** | Resistant to GPU/ASIC-based attacks compared to simpler hash functions |

### Authentication Tag (GCM)

```
┌──────────────────────────────────────────────┐
│  Authentication Tag (16 bytes)               │
│                                              │
│  Generated from:                             │
│  - Ciphertext (encrypted data)               │
│  - Key (derived from password)               │
│  - Nonce (random initialization vector)      │
│                                              │
│  Purpose:                                    │
│  - Proves data hasn't been modified          │
│  - Proves correct password was used          │
│  - If wrong password: tag won't verify       │
│  - If file modified: tag won't verify        │
└──────────────────────────────────────────────┘
```

---

## 14. Security Features

### 1. Confidentiality (Encryption)

**What it protects:**
- File contents hidden from unauthorized readers
- Even with disk access, ciphertext appears random
- Without correct password, plaintext cannot be recovered

**How:**
```
AES-256-GCM with unique key + nonce for each encryption
```

### 2. Integrity (Authentication)

**What it protects:**
- Detects if encrypted file was modified (even 1 bit change)
- Detects corruption during storage or transmission
- Detects tampering attempts

**How:**
```
GCM authentication tag verified before decryption
If tag doesn't match: decryption rejected
```

### 3. Authentication (Password Verification)

**What it protects:**
- Only person with correct password can decrypt
- Wrong password produces wrong key
- Wrong key produces invalid authentication tag

**How:**
```
PBKDF2 derives unique key from each password+salt combination
Incorrect password → incorrect key → authentication failure
```

### 4. Secure Randomness

**What it protects:**
- Salt and nonce are truly random, not predictable
- Same plaintext + password → different ciphertext (due to random nonce)
- Prevents pattern recognition attacks

**How:**
```
os.urandom() uses OS's cryptographic random number generator
- macOS: /dev/urandom backed by Fortuna
- Linux: /dev/urandom backed by kernel entropy
- Windows: CryptGenRandom API
```

### 5. Salt Reuse Prevention

**What it protects:**
- Each encryption generates new salt
- Even encrypting same file twice gives different result
- Prevents rainbow table attacks

**How:**
```
for each encryption:
    salt = os.urandom(32)  # new random salt every time
    key = PBKDF2(password, salt)
    result = AES-GCM(key, ...)
```

### 6. Nonce Reuse Prevention

**What it protects:**
- Different nonce for each encryption
- Never reusing nonce with same key (critical for GCM security)
- Prevents cryptanalytic attacks

**How:**
```
for each encryption:
    nonce = os.urandom(12)  # new random nonce every time
```

### 7. No Password Storage

**What it protects:**
- Password never written to disk
- Password never logged
- Password cleared from memory after use
- Only derived key used in cryptographic operations

**How:**
```
user_password → PBKDF2 → derived_key (stored in memory, used for crypto)
                  ↓
         (password discarded)
```

### 8. User-Friendly Error Messages

**What it protects:**
- Doesn't expose cryptographic internals
- Doesn't leak information about authentication failures
- Doesn't print stack traces with sensitive data

**Examples:**

```python
# ✗ BAD (leaks information)
Error: InvalidTag: authentication tag verification failed at line 273

# ✓ GOOD (safe, user-friendly)
Decryption failed. The password may be incorrect or the encrypted file 
may have been modified.
```

---

## 15. Project Structure

```
secure-file-encryption/
│
├── main.py
│   └── GUI application using Tkinter
│       - File selection dialogs
│       - Password entry (masked)
│       - Encrypt/Decrypt buttons
│       - Status messages
│
├── crypto_utils.py
│   └── Cryptographic operations
│       - AES-256-GCM encryption/decryption
│       - PBKDF2-HMAC-SHA256 key derivation
│       - Random salt generation
│       - Random nonce generation
│       - Metadata extraction
│
├── file_utils.py
│   └── File operations
│       - Binary file reading
│       - Binary file writing
│       - Filename management
│       - File validation
│       - File size formatting
│
├── requirements.txt
│   └── Python dependencies
│       - cryptography==41.0.7
│
├── README.md
│   └── This comprehensive documentation
│
├── encrypted_files/
│   └── Directory for encrypted output files
│
└── decrypted_files/
    └── Directory for decrypted output files
```

### File Responsibilities

**main.py**
- Creates Tkinter GUI window
- Handles user interactions (button clicks)
- Manages file dialogs
- Validates user inputs
- Calls encryption/decryption functions
- Displays status messages
- Error handling and user feedback

**crypto_utils.py**
- `generate_salt()`: Creates random 32-byte salt
- `generate_nonce()`: Creates random 12-byte nonce
- `derive_key_from_password()`: PBKDF2-HMAC-SHA256
- `encrypt_file()`: AES-256-GCM encryption
- `decrypt_file()`: AES-256-GCM decryption
- `get_encryption_metadata()`: Extracts file metadata

**file_utils.py**
- `read_file_as_bytes()`: Reads any file as binary
- `write_file_from_bytes()`: Writes binary data to file
- `get_encrypted_filename()`: Generates .enc filename
- `get_decrypted_filename()`: Generates output filename
- `get_file_size_formatted()`: Human-readable sizes
- `validate_file_exists()`: File validation
- `get_file_info()`: Retrieves file information

---

## 16. Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- macOS, Linux, or Windows

### Step 1: Install Python

**macOS (using Homebrew):**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3 python3-pip
```

**Windows:**
Download from https://www.python.org/downloads/

Verify installation:
```bash
python3 --version
```

### Step 2: Navigate to Project Directory

```bash
cd /Users/yashwaantdev/Downloads/DSP\ Assignment\ 2/secure-file-encryption
```

Or if in different location:
```bash
cd path/to/secure-file-encryption
```

### Step 3: Install Dependencies

```bash
pip3 install -r requirements.txt
```

Or if pip3 is not available:
```bash
python3 -m pip install -r requirements.txt
```

This installs:
- **cryptography 41.0.7**: Provides AES-GCM and PBKDF2

### Step 4: Verify Installation

```bash
python3 -c "import cryptography; print('✓ cryptography installed:', cryptography.__version__)"
python3 -c "import tkinter; print('✓ tkinter available')"
```

Both should print success messages.

---

## 17. How to Run

### Start the Application

```bash
python3 main.py
```

Or:
```bash
python main.py
```

### GUI Window Opens

A window titled "Secure File Encryption & Decryption System" appears with:
- Encryption section (top)
- Decryption section (bottom)

### Encryption Workflow

1. Click **"Select File to Encrypt"** button
2. Choose any file from your computer
3. Enter a password (8+ characters recommended)
4. Confirm the password
5. Click **"Encrypt File"** button
6. Wait for encryption to complete
7. Status shows: "✓ File encrypted successfully!"
8. Look for `filename.enc` in same directory

### Decryption Workflow

1. Click **"Select Encrypted File"** button
2. Choose an `.enc` file
3. Enter the password used during encryption
4. Click **"Decrypt File"** button
5. Wait for decryption to complete
6. Status shows: "✓ File decrypted successfully!"
7. Look for `filename_decrypted.pdf` in `decrypted_files/` subdirectory

### Keyboard Shortcuts

- **Tab**: Navigate between fields
- **Enter**: Activate focused button
- Password fields: Type normally (characters shown as dots)

---

## 18. Demonstration Steps

### Demo 1: Successful Encryption

**Goal:** Show that encryption works and creates an encrypted file

**Steps:**

1. Prepare a sample file
   ```bash
   echo "This is confidential data from the company" > sample.txt
   ```

2. Run application
   ```bash
   python3 main.py
   ```

3. In GUI:
   - Click "Select File to Encrypt"
   - Choose `sample.txt`
   - Enter password: `SecurePass123`
   - Confirm password: `SecurePass123`
   - Click "Encrypt File"

4. Wait for encryption (shows "Encrypting file...")

5. Observe success message:
   ```
   ✓ File encrypted successfully!
   
   Original: 43 bytes
   Encrypted: 104 bytes
   (+61 bytes for metadata)
   
   Saved as: sample.txt.enc
   ```

6. Show `sample.txt.enc` exists and is unreadable:
   ```bash
   ls -la sample.txt*
   file sample.txt.enc
   head sample.txt.enc  # Shows binary garbage
   ```

**Key Points to Explain:**
- Original file is readable (plaintext)
- Encrypted file appears as random bytes
- File size increased by 61 bytes (metadata)
- No password stored in encrypted file

---

### Demo 2: Successful Decryption with Correct Password

**Goal:** Show that decryption works with correct password

**Steps:**

1. Continue from Demo 1 (have `sample.txt.enc` ready)

2. In GUI:
   - Click "Select Encrypted File"
   - Choose `sample.txt.enc`
   - Enter password: `SecurePass123` (CORRECT)
   - Click "Decrypt File"

3. Wait for decryption (shows "Decrypting file...")

4. Observe success message:
   ```
   ✓ File decrypted successfully!
   
   Decrypted size: 43 bytes
   
   Saved as:
   sample_decrypted.txt
   ```

5. Show restored file:
   ```bash
   ls -la decrypted_files/
   cat decrypted_files/sample_decrypted.txt
   ```

6. Verify content matches original:
   ```bash
   diff sample.txt decrypted_files/sample_decrypted.txt
   # Should show no differences
   ```

**Key Points to Explain:**
- Correct password derived correct key
- AES-256-GCM decryption succeeded
- Authentication tag verified
- Original content fully restored
- Byte-for-byte identical to original

---

### Demo 3: Failed Decryption with Wrong Password

**Goal:** Show that wrong password is rejected safely

**Steps:**

1. Have `sample.txt.enc` ready

2. In GUI:
   - Click "Select Encrypted File"
   - Choose `sample.txt.enc`
   - Enter password: `WrongPassword123` (INCORRECT)
   - Click "Decrypt File"

3. Wait briefly

4. Observe error message:
   ```
   ERROR: Decryption failed. The password may be incorrect or 
   the encrypted file may have been modified.
   ```

5. Show that no file was created/corrupted:
   ```bash
   ls -la decrypted_files/
   # No corrupted file created
   ```

**Key Points to Explain:**
- Wrong password → wrong derived key
- Wrong key → authentication tag verification fails
- Decryption rejected BEFORE plaintext exposed
- No data leaked (safe failure)
- File not modified/corrupted

---

### Demo 4: Tampering Detection

**Goal:** Show that modified ciphertext is detected

**Steps:**

1. Have `sample.txt.enc` ready

2. Create a modified copy and corrupt it:
   ```bash
   cp sample.txt.enc sample.txt.enc.corrupted
   # Modify a byte in the middle
   python3 -c "
   with open('sample.txt.enc.corrupted', 'rb') as f:
       data = bytearray(f.read())
   # Flip one byte in the middle
   data[50] ^= 0xFF
   with open('sample.txt.enc.corrupted', 'wb') as f:
       f.write(data)
   "
   ```

3. In GUI:
   - Click "Select Encrypted File"
   - Choose `sample.txt.enc.corrupted`
   - Enter password: `SecurePass123` (CORRECT password)
   - Click "Decrypt File"

4. Observe error message:
   ```
   ERROR: Decryption failed. The password may be incorrect or 
   the encrypted file may have been modified.
   ```

5. Explain:
   ```
   Tampered Ciphertext
           ↓
   AES-256-GCM Decryption
           ↓
   Authentication Tag Verification
           ↓
   TAG MISMATCH! (Modified ciphertext detected)
           ↓
   Decryption Rejected
           ↓
   Original Content NOT Exposed
   ```

**Key Points to Explain:**
- GCM mode detects ANY modification (even 1-bit change)
- Authentication tag serves as integrity check
- Even with correct password, tampering is detected
- Corrupted files are safely rejected
- This is stronger than regular encryption

---

### Demo 5: Binary File Support

**Goal:** Show encryption works for any file type

**Steps:**

1. Create a sample image (or use existing image):
   ```bash
   # If you have an image file, use it
   # Or create a binary file
   python3 -c "
   import os
   with open('sample_image.bin', 'wb') as f:
       f.write(os.urandom(1024))  # 1 KB of random binary data
   "
   ```

2. In GUI:
   - Click "Select File to Encrypt"
   - Choose `sample_image.bin`
   - Enter password: `BinaryTest123`
   - Confirm password: `BinaryTest123`
   - Click "Encrypt File"

3. Observe encryption succeeds

4. Now decrypt:
   - Click "Select Encrypted File"
   - Choose `sample_image.bin.enc`
   - Enter password: `BinaryTest123`
   - Click "Decrypt File"

5. Verify binary file is restored correctly:
   ```bash
   md5 sample_image.bin decrypted_files/sample_image_decrypted.bin
   # Should show same MD5 hash (byte-for-byte identical)
   ```

**Key Points to Explain:**
- Application treats all files as binary data
- Works for images, PDFs, zips, executables, etc.
- No data loss (MD5 hashes match)
- Binary file restoration is perfect

---

## 19. Sample Input/Output

### Example 1: Text File Encryption

**Input:**
```
File: document.txt
Content: "Important business confidential data"
Password: MySecurePassword123!
```

**Output:**
```
File: document.txt.enc
Content: [Binary - appears as random garbage]
Size: Original + 61 bytes
No password stored in file
```

**File Size Comparison:**
```
Original:   35 bytes
Encrypted:  96 bytes (35 + 1 + 32 + 12 + 16)
  1 byte  : VERSION
  32 bytes: SALT
  12 bytes: NONCE
  35 bytes: CIPHERTEXT
  16 bytes: AUTHENTICATION TAG
```

### Example 2: Image File Decryption

**Input:**
```
File: photo.jpg.enc
Password: MySecurePassword123!
```

**Output:**
```
File: decrypted_files/photo_decrypted.jpg
Content: [Exact binary reproduction of original]
Verified: MD5 hash matches original
Status: ✓ File decrypted successfully!
```

### Example 3: Wrong Password

**Input:**
```
File: document.txt.enc
Password: WrongPassword
```

**Output:**
```
Error Message: "Decryption failed. The password may be incorrect 
               or the encrypted file may have been modified."

File Created: None
Reason: Authentication tag verification failed
Result: Safe rejection without data corruption
```

### Example 4: Multiple Encryptions Same File

**Input:**
```
File: secret.pdf
Password: SamePassword

Encryption #1:
  - Salt: A1B2C3D4E5F6... (random)
  - Nonce: X1Y2Z3W4V5... (random)
  - Result: secret.pdf.enc (version 1)

Encryption #2:
  - Same file, same password
  - Salt: 9K8L7M6N5O4P... (different random)
  - Nonce: Q9R8S7T6U5... (different random)
  - Result: secret.pdf.enc (version 2)
```

**Output:**
```
secret.pdf.enc (version 1) and secret.pdf.enc (version 2)
appear COMPLETELY DIFFERENT
(same plaintext + same password → different ciphertext)

Why: Different salt & nonce for each encryption

Reason: Prevents pattern recognition attacks
```

---

## 20. Advantages

### 1. Strong Encryption

- **AES-256-GCM**: Military-grade, NIST-approved encryption
- **Unbreakable**: 2^256 possible keys (brute-force impossible)
- **Fast**: Modern computers can still encrypt/decrypt quickly
- **Authenticated**: Detects tampering with authentication tag

### 2. Password Security

- **PBKDF2**: Industry-standard password-based key derivation
- **100,000 iterations**: Slows down brute-force attacks by 100x
- **Never stored**: Password is never written to disk
- **Unique key**: Each password+salt pair produces unique key

### 3. No Key Management

- **User-friendly**: No need to manage separate encryption keys
- **Password-based**: Users already know how to create passwords
- **Accessible**: Anyone can use it without cryptography knowledge

### 4. File Type Agnostic

- **Binary support**: Works with any file type
- **No file analysis**: Treats all files as binary data
- **Compression-friendly**: Can encrypt compressed files
- **Metadata preserved**: Filename structure maintained

### 5. Easy Demonstration

- **GUI-based**: Simple click-based interface
- **No terminal commands**: Perfect for non-technical users
- **Clear messages**: Status updates show progress
- **Visual feedback**: Success/error messages displayed

### 6. Educational Value

- **Clear code**: Well-commented, easy to understand
- **Modular design**: Each component has clear responsibility
- **Industry standard**: Uses real libraries (cryptography)
- **Best practices**: Implements security correctly

### 7. Portable

- **Python**: Cross-platform (Windows, macOS, Linux)
- **Standard library**: Tkinter included with Python
- **Single dependency**: Only cryptography library needed
- **No installation**: Just download and run

---

## 21. Limitations

### 1. Local-Only Encryption

- Encryption happens on local machine
- No cloud integration or backup
- Files must fit in available memory
- Not suitable for very large files (>available RAM)

### 2. No Key Recovery

- Forgotten password = no recovery
- No "master key" or backdoor
- This is intentional (security feature)
- User must remember password

### 3. Password Strength

- User responsible for strong password
- Weak passwords can be brute-forced (eventually)
- No password strength meter in current version
- Users must create good passwords

### 4. Single User

- Not designed for multi-user scenarios
- No user authentication
- Anyone with access can use the application
- No audit logging of who encrypted/decrypted

### 5. No Advanced Features

- No partial encryption (whole file only)
- No file compression
- No fragmentation or splitting
- No archiving support

### 6. File Size

- Very large files (GBs) load entirely in memory
- Not optimized for streaming encryption
- Desktop storage dependent
- No network backup integration

### 7. No Long-Term Key Rotation

- No built-in mechanism to re-encrypt with new key
- Files encrypted now must use same key forever
- Password change requires re-encryption

---

## 22. Future Enhancements

### Possible Improvements

1. **Streaming Encryption**
   - Process files in chunks
   - Support files larger than RAM
   - Better performance for large files

2. **Key Rotation**
   - Ability to change password without re-encrypting entire file
   - Update encryption key while preserving ciphertext

3. **Batch Operations**
   - Encrypt/decrypt multiple files at once
   - Folder-level encryption
   - Recursive directory encryption

4. **Password Strength Meter**
   - Real-time password strength feedback
   - Recommendations for stronger passwords
   - Entropy calculation

5. **File Compression**
   - Optional gzip compression before encryption
   - Reduced file sizes
   - Faster transmission

6. **Cloud Integration**
   - Upload encrypted files to cloud storage
   - Download and decrypt from cloud
   - Sync capabilities

7. **Audit Logging**
   - Log encryption/decryption operations
   - Track which files were encrypted when
   - User authentication support

8. **Advanced Security**
   - Hardware security key support (USB security keys)
   - Multi-factor authentication
   - Secure erasure of original file after encryption

9. **Platform Improvements**
   - Web-based interface
   - Mobile app version
   - Command-line interface

10. **Additional Algorithms**
    - Support for different key sizes (128-bit, 192-bit)
    - Alternative algorithms (ChaCha20-Poly1305)
    - Configurable iteration counts

---

## 23. Conclusion

This project demonstrates how cryptographic principles translate into practical, working software that protects user data.

### What We Learned

1. **Cryptography is practical**: Modern encryption is fast and accessible
2. **Passwords need processing**: Direct password use is insecure; PBKDF2 fixes this
3. **Randomness matters**: Different salt/nonce for each operation prevents attacks
4. **Authentication is essential**: Detecting tampering is as important as encryption
5. **Security details matter**: Small implementation choices affect overall security
6. **User experience matters**: Even excellent cryptography needs clear interface

### Key Takeaways

```
Confidentiality    ← AES-256-GCM Encryption
Integrity          ← GCM Authentication Tag
Authentication     ← Password-Based Key Derivation
Availability       ← No data loss or corruption
Non-Repudiation    ← File wasn't modified after encryption
```

### Why This Matters

- Personal data deserves protection
- Strong encryption is the foundation of digital privacy
- Cryptography is trustworthy when implemented correctly
- Even students can build secure systems

### Final Thoughts

This project is an educational implementation demonstrating secure file encryption using established cryptographic primitives. While it implements strong encryption correctly, remember:

- Security is a process, not a product
- Always keep software and dependencies updated
- Use for educational and personal file protection
- For production systems, consult security professionals
- Cryptography is one layer of a comprehensive security strategy

---

## References and Further Reading

### Cryptography Standards

- **NIST SP 800-38D**: Galois/Counter Mode (GCM) Specification
- **NIST SP 800-132**: PBKDF2 Specification
- **FIPS 197**: Advanced Encryption Standard (AES) Standard

### Python Cryptography

- [cryptography.io](https://cryptography.io) - Official documentation
- [Python secrets module](https://docs.python.org/3/library/secrets.html) - Secure random generation
- [Python cryptography API](https://cryptography.io/en/latest/hazmat/primitives/aead/) - AEAD ciphers

### Security Best Practices

- [OWASP: Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [OWASP: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

### Related Topics

- Public-key cryptography (RSA, ECC)
- Hashing algorithms (SHA-256, SHA-512)
- Digital signatures and certificates
- Perfect forward secrecy
- Post-quantum cryptography

---

**Project Created:** September 2024  
**For:** Data Security and Privacy (DSP) - College Programming Assignment  
**Language:** Python 3.8+  
**Status:** Educational Implementation - Fully Functional

---

*This project is designed for educational purposes. While it implements cryptography correctly, always consult security professionals for production systems handling sensitive data.*
