import argparse
import contextlib
import io
import unittest
from unittest.mock import patch

import geom as b
from check_electronics import layouts, main, positive_mm


class ElectronicsLayoutTests(unittest.TestCase):
    def test_small_boards_fit(self):
        self.assertTrue(list(layouts([30, 20, 3], [25, 20, 4], 0.5)))

    def test_depth_includes_margin_on_both_faces(self):
        self.assertTrue(list(layouts([30, 20, 6], [25, 20, 6], 0.5)))
        self.assertFalse(list(layouts([30, 20, 6.01], [25, 20, 4], 0.5)))

    def test_oversized_board_does_not_fit(self):
        self.assertFalse(list(layouts([80, 60, 3], [25, 20, 4], 0.5)))

    def test_rotated_boards_fit(self):
        self.assertTrue(list(layouts([55, 30, 3], [55, 30, 4], 0.5)))

    def test_nonpositive_or_nonfinite_measurements_rejected(self):
        for value in ("0", "-1", "nan", "inf"):
            with self.subTest(value=value), self.assertRaises(argparse.ArgumentTypeError):
                positive_mm(value)

    def test_layouts_preserve_clearance_and_do_not_overlap(self):
        for layout in layouts([30, 20, 3], [25, 20, 4], 0.5):
            for origin, size in layout:
                for start, length, low, high in zip(origin, size,
                                                    (7, 2.1, 2.5), (83, 8.1, 59.5)):
                    self.assertGreaterEqual(start, low)
                    self.assertLessEqual(start + length, high)
            (a, sa), (c, sc) = layout
            self.assertTrue(any(a[i] + sa[i] + 0.5 <= c[i] or
                                c[i] + sc[i] + 0.5 <= a[i] for i in (0, 2)))

    def test_plastic_inside_cavity_rejects_all_layouts(self):
        obstruction = b.trimesh.creation.box(extents=(90, 40, 60))
        obstruction.apply_translation((45, 10, 30))
        argv = ["check_electronics.py", "--bms", "30", "20", "3",
                "--charger", "25", "20", "4"]
        with patch("sys.argv", argv), patch("geom.trimesh.load_mesh", return_value=obstruction):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(main(), 1)
            self.assertIn("NO CABE", output.getvalue())


if __name__ == "__main__":
    unittest.main()
