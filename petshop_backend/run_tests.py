import subprocess, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

print("Running test suite...\n")
result=subprocess.run(
    ["pytest", "-v"],
    capture_output=True,
    text=True
)
with open("test_report.txt", "w", encoding="utf-8")as report:
    report.write(result.stdout)

print(result.stdout)

print("\nReport generated:")
print("test_report.txt")