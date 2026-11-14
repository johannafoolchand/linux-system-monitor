"""Unit tests for the system monitor."""

import unittest
from unittest.mock import patch, Mock

import monitor


class CollectMetricsTests(unittest.TestCase):
    @patch("monitor.psutil.cpu_percent", return_value=12.5)
    @patch("monitor.psutil.virtual_memory")
    @patch("monitor.shutil.disk_usage")
    @patch("monitor.platform.release", return_value="test-release")
    @patch("monitor.platform.system", return_value="TestOS")
    def test_collect_metrics_returns_expected_values(
        self, _system, _release, disk_usage, virtual_memory, _cpu
    ):
        virtual_memory.return_value = Mock(
            percent=40.0,
            available=2 * 1024**3,
        )
        disk_usage.return_value = Mock(
            total=100 * 1024**3,
            used=25 * 1024**3,
            free=75 * 1024**3,
        )

        metrics = monitor.collect_metrics()

        self.assertEqual(metrics["system"], "TestOS")
        self.assertEqual(metrics["release"], "test-release")
        self.assertEqual(metrics["cpu_percent"], 12.5)
        self.assertEqual(metrics["memory_percent"], 40.0)
        self.assertEqual(metrics["memory_available_gb"], 2.0)
        self.assertEqual(metrics["disk_percent"], 25.0)
        self.assertEqual(metrics["disk_free_gb"], 75.0)


class CommandLineTests(unittest.TestCase):
    @patch("monitor.collect_metrics", return_value={"cpu_percent": 12.5})
    @patch("builtins.print")
    def test_json_option_outputs_machine_readable_metrics(
        self, mocked_print, _collect_metrics
    ):
        monitor.main(["--json"])

        mocked_print.assert_called_once_with('{\n  "cpu_percent": 12.5\n}')


class DisplayMetricsTests(unittest.TestCase):
    def test_display_metrics_prints_summary(self):
        metrics = {
            "system": "Linux",
            "release": "test",
            "cpu_percent": 10.0,
            "memory_percent": 30.0,
            "memory_available_gb": 4.0,
            "disk_percent": 50.0,
            "disk_free_gb": 20.0,
        }

        with patch("builtins.print") as mocked_print:
            monitor.display_metrics(metrics)

        printed = " ".join(str(call.args[0]) for call in mocked_print.call_args_list)
        self.assertIn("SYSTEM MONITOR", printed)
        self.assertIn("Linux", printed)
        self.assertIn("10.0%", printed)


if __name__ == "__main__":
    unittest.main()
