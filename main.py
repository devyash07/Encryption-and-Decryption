"""
Secure File Encryption and Decryption System - GUI Application

This is the main application entry point with the Tkinter graphical user interface.
It provides a user-friendly interface for encrypting and decrypting files using
AES-256-GCM encryption with password-based key derivation.

Main Features:
- File selection dialogs
- Password entry with masking
- Real-time status updates
- Error handling with user-friendly messages
- Support for any file type (binary files, documents, images, etc.)
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from pathlib import Path
import traceback

from crypto_utils import encrypt_file, decrypt_file
from file_utils import (
    read_file_as_bytes, write_file_from_bytes,
    get_encrypted_filename, get_decrypted_filename,
    get_file_size_formatted, get_file_info
)


class SecureFileEncryptionApp:
    """Main application class for the encryption/decryption GUI."""
    
    def __init__(self, root):
        """
        Initialize the application.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Secure File Encryption & Decryption System")
        self.root.geometry("700x850")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg='#f0f0f0')
        
        # Application state
        self.encrypt_file_path = None
        self.decrypt_file_path = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create and configure all UI elements."""
        # Configure colors
        self.root.configure(bg='#1e1e2e')  # Dark background
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1e1e2e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Separator
        sep1 = tk.Frame(main_frame, height=2, bg='#00ff00')
        sep1.pack(fill=tk.X, pady=15)
        
        # Encryption section
        self.create_encryption_section(main_frame)
        
        # Separator
        sep2 = tk.Frame(main_frame, height=2, bg='#00ff00')
        sep2.pack(fill=tk.X, pady=15)
        
        # Decryption section
        self.create_decryption_section(main_frame)
    
    def create_header(self, parent):
        """Create header section with title and subtitle."""
        header_frame = tk.Frame(parent, bg='#1e1e2e')
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(
            header_frame,
            text="Secure File Encryption & Decryption System",
            font=("Arial", 16, "bold"),
            bg='#1e1e2e',
            fg='#00ff00'  # Bright green
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Protect your confidential files using AES-256-GCM encryption",
            font=("Arial", 10, "italic"),
            bg='#1e1e2e',
            fg='#00cc00'  # Lighter green
        )
        subtitle_label.pack()
    
    def create_encryption_section(self, parent):
        """Create encryption section with file selection, password, and encrypt button."""
        enc_frame = tk.LabelFrame(
            parent, 
            text="ENCRYPT FILE", 
            bg='#1e1e2e',
            fg='#00ff00',
            font=("Arial", 10, "bold")
        )
        enc_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=0)
        
        # Add padding inside the frame
        padding_frame = tk.Frame(enc_frame, bg='#1e1e2e')
        padding_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # File selection
        file_frame = tk.Frame(padding_frame, bg='#1e1e2e')
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(file_frame, text="Selected File:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        self.encrypt_file_label = tk.Label(
            file_frame,
            text="No file selected",
            foreground="#ff6b6b",
            bg='#1e1e2e',
            font=("Arial", 10)
        )
        self.encrypt_file_label.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            padding_frame,
            text="Select File to Encrypt",
            command=self.select_file_to_encrypt
        ).pack(fill=tk.X, pady=(0, 15))
        
        # Password entry
        password_label = tk.Label(
            padding_frame,
            text="Password:",
            font=("Arial", 10, "bold"),
            bg='#1e1e2e',
            fg='#00ff00'
        )
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.encrypt_password = tk.Entry(padding_frame, show="•", width=40, bg='#2e2e3e', fg='#00ff00', insertbackground='#00ff00')
        self.encrypt_password.pack(fill=tk.X, pady=(0, 15))
        
        # Confirm password entry
        confirm_label = tk.Label(
            padding_frame,
            text="Confirm Password:",
            font=("Arial", 10, "bold"),
            bg='#1e1e2e',
            fg='#00ff00'
        )
        confirm_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.encrypt_password_confirm = tk.Entry(padding_frame, show="•", width=40, bg='#2e2e3e', fg='#00ff00', insertbackground='#00ff00')
        self.encrypt_password_confirm.pack(fill=tk.X, pady=(0, 20))
        
        # Encrypt button
        ttk.Button(
            padding_frame,
            text="Encrypt File",
            command=self.encrypt_file_action
        ).pack(fill=tk.X, pady=(0, 15))
        
        # Status message
        self.encrypt_status = tk.Text(
            padding_frame,
            height=4,
            width=50,
            state=tk.DISABLED,
            bg='#2e2e3e',
            fg='#00ff00',
            relief=tk.FLAT,
            borderwidth=1
        )
        self.encrypt_status.pack(fill=tk.BOTH, expand=True)
    
    def create_decryption_section(self, parent):
        """Create decryption section with file selection, password, and decrypt button."""
        dec_frame = tk.LabelFrame(
            parent, 
            text="DECRYPT FILE", 
            bg='#1e1e2e',
            fg='#00ff00',
            font=("Arial", 10, "bold")
        )
        dec_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=0)
        
        # Add padding inside the frame
        padding_frame = tk.Frame(dec_frame, bg='#1e1e2e')
        padding_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # File selection
        file_frame = tk.Frame(padding_frame, bg='#1e1e2e')
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(file_frame, text="Encrypted File:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        self.decrypt_file_label = tk.Label(
            file_frame,
            text="No file selected",
            foreground="#ff6b6b",
            bg='#1e1e2e',
            font=("Arial", 10)
        )
        self.decrypt_file_label.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            dec_frame,
            text="Select Encrypted File",
            command=self.select_file_to_decrypt
        ).pack(fill=tk.X, pady=(0, 15))
        
        # Password entry
        password_label = tk.Label(
            dec_frame,
            text="Password:",
            font=("Arial", 10, "bold"),
            bg='#1e1e2e',
            fg='#00ff00'
        )
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.decrypt_password = tk.Entry(dec_frame, show="•", width=40, bg='#2e2e3e', fg='#00ff00', insertbackground='#00ff00')
        self.decrypt_password.pack(fill=tk.X, pady=(0, 20))
        
        # Decrypt button
        ttk.Button(
            dec_frame,
            text="Decrypt File",
            command=self.decrypt_file_action
        ).pack(fill=tk.X, pady=(0, 15))
        
        # Status message
        self.decrypt_status = tk.Text(
            dec_frame,
            height=4,
            width=50,
            state=tk.DISABLED,
            bg='#2e2e3e',
            fg='#00ff00',
            relief=tk.FLAT,
            borderwidth=1
        )
        self.decrypt_status.pack(fill=tk.BOTH, expand=True)
    
    def select_file_to_encrypt(self):
        """Open file dialog to select a file for encryption."""
        file_path = filedialog.askopenfilename(
            title="Select file to encrypt",
            initialdir=os.path.expanduser("~")
        )
        
        if file_path:
            self.encrypt_file_path = file_path
            file_info = get_file_info(file_path)
            display_text = f"{file_info['name']} ({file_info['size_formatted']})"
            self.encrypt_file_label.config(text=display_text)
            self.update_status("encrypt", "File selected successfully")
    
    def select_file_to_decrypt(self):
        """Open file dialog to select an encrypted file for decryption."""
        file_path = filedialog.askopenfilename(
            title="Select encrypted file to decrypt",
            filetypes=[("Encrypted Files", "*.enc"), ("All Files", "*.*")],
            initialdir=os.path.expanduser("~")
        )
        
        if file_path:
            self.decrypt_file_path = file_path
            file_info = get_file_info(file_path)
            display_text = f"{file_info['name']} ({file_info['size_formatted']})"
            self.decrypt_file_label.config(text=display_text)
            self.update_status("decrypt", "File selected successfully")
    
    def encrypt_file_action(self):
        """Handle file encryption."""
        try:
            # Validate inputs
            if not self.encrypt_file_path:
                self.update_status("encrypt", "ERROR: No file selected")
                return
            
            password = self.encrypt_password.get()
            password_confirm = self.encrypt_password_confirm.get()
            
            if not password:
                self.update_status("encrypt", "ERROR: Password cannot be empty")
                return
            
            if password != password_confirm:
                self.update_status("encrypt", "ERROR: Passwords do not match")
                return
            
            # Read file
            self.update_status("encrypt", "Reading file...")
            self.root.update()
            
            try:
                file_data = read_file_as_bytes(self.encrypt_file_path)
            except Exception as e:
                self.update_status("encrypt", f"ERROR: Could not read file\n{str(e)}")
                return
            
            # Encrypt file
            self.update_status("encrypt", "Encrypting file (this may take a moment)...")
            self.root.update()
            
            try:
                encrypted_data = encrypt_file(file_data, password)
            except Exception as e:
                self.update_status("encrypt", f"ERROR: Encryption failed\n{str(e)}")
                return
            
            # Save encrypted file
            self.update_status("encrypt", "Saving encrypted file...")
            self.root.update()
            
            encrypted_path = get_encrypted_filename(self.encrypt_file_path)
            
            try:
                write_file_from_bytes(encrypted_path, encrypted_data)
            except Exception as e:
                self.update_status("encrypt", f"ERROR: Could not save encrypted file\n{str(e)}")
                return
            
            # Success
            original_size = len(file_data)
            encrypted_size = len(encrypted_data)
            overhead = encrypted_size - original_size
            
            success_msg = (
                f"✓ File encrypted successfully!\n"
                f"\nOriginal: {original_size:,} bytes\n"
                f"Encrypted: {encrypted_size:,} bytes\n"
                f"(+{overhead:,} bytes for metadata)\n\n"
                f"Saved as: {os.path.basename(encrypted_path)}"
            )
            self.update_status("encrypt", success_msg)
            
            # Clear passwords
            self.encrypt_password.delete(0, tk.END)
            self.encrypt_password_confirm.delete(0, tk.END)
            
        except Exception as e:
            error_msg = f"ERROR: Unexpected error\n{str(e)}"
            self.update_status("encrypt", error_msg)
            print(traceback.format_exc())
    
    def decrypt_file_action(self):
        """Handle file decryption."""
        try:
            # Validate inputs
            if not self.decrypt_file_path:
                self.update_status("decrypt", "ERROR: No file selected")
                return
            
            password = self.decrypt_password.get()
            
            if not password:
                self.update_status("decrypt", "ERROR: Password cannot be empty")
                return
            
            # Read encrypted file
            self.update_status("decrypt", "Reading encrypted file...")
            self.root.update()
            
            try:
                encrypted_data = read_file_as_bytes(self.decrypt_file_path)
            except Exception as e:
                self.update_status("decrypt", f"ERROR: Could not read file\n{str(e)}")
                return
            
            # Decrypt file
            self.update_status("decrypt", "Decrypting file (this may take a moment)...")
            self.root.update()
            
            try:
                file_data = decrypt_file(encrypted_data, password)
            except ValueError as e:
                self.update_status("decrypt", f"ERROR: {str(e)}")
                self.decrypt_password.delete(0, tk.END)
                return
            except Exception as e:
                error_msg = (
                    "ERROR: Decryption failed. The password may be incorrect\n"
                    "or the encrypted file may have been modified."
                )
                self.update_status("decrypt", error_msg)
                self.decrypt_password.delete(0, tk.END)
                return
            
            # Save decrypted file
            self.update_status("decrypt", "Saving decrypted file...")
            self.root.update()
            
            # Determine output directory
            output_dir = os.path.join(
                os.path.dirname(self.decrypt_file_path),
                "decrypted_files"
            )
            
            decrypted_filename = get_decrypted_filename(
                os.path.basename(self.decrypt_file_path)
            )
            decrypted_path = os.path.join(output_dir, decrypted_filename)
            
            try:
                write_file_from_bytes(decrypted_path, file_data)
            except Exception as e:
                self.update_status("decrypt", f"ERROR: Could not save decrypted file\n{str(e)}")
                return
            
            # Success
            success_msg = (
                f"✓ File decrypted successfully!\n"
                f"\nDecrypted size: {len(file_data):,} bytes\n\n"
                f"Saved as:\n{decrypted_filename}"
            )
            self.update_status("decrypt", success_msg)
            
            # Clear password
            self.decrypt_password.delete(0, tk.END)
            
        except Exception as e:
            error_msg = f"ERROR: Unexpected error\n{str(e)}"
            self.update_status("decrypt", error_msg)
            print(traceback.format_exc())
    
    def update_status(self, section: str, message: str):
        """
        Update status message in the specified section.
        
        Args:
            section (str): "encrypt" or "decrypt"
            message (str): Status message to display
        """
        if section == "encrypt":
            status_widget = self.encrypt_status
        else:
            status_widget = self.decrypt_status
        
        status_widget.config(state=tk.NORMAL)
        status_widget.delete('1.0', tk.END)
        status_widget.insert('1.0', message)
        status_widget.config(state=tk.DISABLED)


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = SecureFileEncryptionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
