"""Display a snapshot of CPU, memory and disk usage."""

from __future__ import annotations

import shutil
import platform

import psutil


def collect_metrics() -> dict[str, float | str]:
    """Collect system information and return normalised metrics."""
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    return {
        "system": platform.system(),
        "release": platform.release(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": memory.percent,
        "memory_available_gb": memory.available / (1024**3),
        "disk_percent": disk.used / disk.total * 100,
        "disk_free_gb": disk.free / (1024**3),
    }


def display_metrics(metrics: dict[str, float | str]) -> None:
    """Print collected metrics in a readable terminal layout."""
    print("=" * 42)
    print("             SYSTEM MONITOR")
    print("=" * 42)
    print(f"System          : {metrics['system']} {metrics['release']}")
    print(f"CPU usage       : {metrics['cpu_percent']:.1f}%")
    print(f"RAM usage       : {metrics['memory_percent']:.1f}%")
    print(f"RAM available   : {metrics['memory_available_gb']:.2f} GB")
    print(f"Disk usage      : {metrics['disk_percent']:.1f}%")
    print(f"Disk free       : {metrics['disk_free_gb']:.2f} GB")
    print("=" * 42)


def main() -> None:
    """Run the system monitor."""
    display_metrics(collect_metrics())


if __name__ == "__main__":
    main()
