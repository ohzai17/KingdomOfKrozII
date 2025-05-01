import sys
import os

# Handle the path for both .exe and script execution
if getattr(sys, 'frozen', False):  # If running as a bundled .exe
    # sys._MEIPASS is the temporary folder PyInstaller uses to extract files
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.executable)))
else:  # If running as a script
    base_path = os.path.dirname(os.path.abspath(__file__))

# Add the src directory to sys.path so Python can find it
sys.path.append(os.path.join(base_path, 'src'))

# Now try importing the main module from src
from src.main import *

if __name__ == "__main__":
    main()  