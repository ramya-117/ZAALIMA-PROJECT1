"""
Streamlit Cloud Entry Point - Uses your original dashboard
"""

import sys
import os

# Add your project directory to Python path
sys.path.append(os.path.dirname(__file__))

# Import your original dashboard
from dashboard import main

if __name__ == "__main__":
    main()
