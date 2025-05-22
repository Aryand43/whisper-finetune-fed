import sys
import os

# Append the absolute path to the src directory (where the package root is)
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "whisper-finetune", "src"))

from whisper_finetune.scripts.finetune import main

if __name__ == "__main__":
    config_path = sys.argv[1] if len(sys.argv) > 1 else "configs/spc-fed-example.yaml"
    main(config_path)
