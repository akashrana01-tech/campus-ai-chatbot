#!/usr/bin/env python3
"""
Test runner script for CampusAI test suite.
Executes all unit and integration tests using Python's standard unittest framework.
"""

import unittest
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

if __name__ == "__main__":
    print("=" * 70)
    print("CareerPilot AI Automated Test Suite (G H Raisoni University - BCA Science)")
    print("=" * 70)

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(BASE_DIR / "tests"), pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"✓ ALL {result.testsRun} TESTS PASSED SUCCESSFULLY!")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"✗ FAILURES: {len(result.failures)}, ERRORS: {len(result.errors)}")
        print("=" * 70)
        sys.exit(1)
