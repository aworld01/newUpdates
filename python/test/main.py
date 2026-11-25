import os
import subprocess
import sys

# Run everything from the folder that contains main.py, since step1.py and
# step2.py look for their input files (*.txt, *.srt, *.json) in the current folder.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

STEPS = ["step1.py", "step2.py"]


def run_step(script):
    print(f"\n=== Running {script} ===")
    result = subprocess.run([sys.executable, os.path.join(BASE_DIR, script)])
    if result.returncode != 0:
        print(f"\n{script} failed (exit code {result.returncode}). Stopping.")
        sys.exit(result.returncode)


def main():
    for script in STEPS:
        run_step(script)
    print("\nAll steps completed successfully.")


if __name__ == "__main__":
    main()
