#!/usr/bin/env python3
"""
CLI script to securely create an administrator account for CampusAI.
Usage:
    python create_admin.py
    python create_admin.py --username manager --email manager@college.edu --password SecurePassword@123
"""

import sys
import argparse
import getpass
from app import create_app
from models import db, Admin


def main():
    parser = argparse.ArgumentParser(description="Create a new administrator for CampusAI.")
    parser.add_argument("--username", help="Admin username", default=None)
    parser.add_argument("--email", help="Admin email address", default=None)
    parser.add_argument("--password", help="Admin password (leave blank to prompt securely)", default=None)

    args = parser.parse_args()

    username = args.username or input("Enter admin username: ").strip()
    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)

    email = args.email or input("Enter admin email address: ").strip()
    if not email:
        print("Error: Email cannot be empty.")
        sys.exit(1)

    password = args.password
    if not password:
        password = getpass.getpass("Enter secure admin password: ")
        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Error: Passwords do not match.")
            sys.exit(1)

    if len(password) < 6:
        print("Error: Password should be at least 6 characters long.")
        sys.exit(1)

    app = create_app()
    with app.app_context():
        # Check if username or email already exists
        existing = Admin.query.filter((Admin.username == username) | (Admin.email == email)).first()
        if existing:
            print(f"Error: An administrator with username '{username}' or email '{email}' already exists.")
            sys.exit(1)

        admin = Admin(username=username, email=email)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()

        print(f"✓ Administrator '{username}' successfully created with ID #{admin.id}!")
        print(f"  Login at: http://127.0.0.1:5000/admin/login")


if __name__ == "__main__":
    main()
