import sys
from pathlib import Path

project_path = str(Path(__file__).parents[1])
if project_path not in sys.path:
    sys.path.append(project_path)
