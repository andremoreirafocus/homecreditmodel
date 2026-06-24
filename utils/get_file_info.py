import subprocess
from pathlib import Path


def get_file_sizes_dir(data_dir: Path):
    for name in sorted(data_dir.glob("*.csv")):
        size_mb = name.stat().st_size / 1024**2
        num_lines = subprocess.run(
            f"wc -l {name} | cut -f1 -d ' '",
            shell=True, capture_output=True, text=True
        ).stdout.strip()
        print(f"{name.name:<40} {size_mb:>8.1f} MB  {int(num_lines):>15,} lines")
        
def get_file_sizes(filename: Path):
    filename = Path(filename)
    size_mb = filename.stat().st_size / 1024**2
    num_lines = subprocess.run(
        f"wc -l {filename} | cut -f1 -d ' '",
        shell=True, capture_output=True, text=True
    ).stdout.strip()
    print(f"{filename.name:<40} {size_mb:>8.1f} MB  {int(num_lines):>15,} lines")
