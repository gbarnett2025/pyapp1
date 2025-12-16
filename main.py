import sys
from pathlib import Path


# Add submodule to Python path
sys.path.append(str(Path(__file__).parent / "pycommon"))


from appcommon import print_message


if __name__ == "__main__":
    print_message("app1")
