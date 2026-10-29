import unittest

import numpy as np
import trimesh

import prepare_k6ark as paddle
import prepare_dj9fm as straight


class K6arkTests(unittest.TestCase):
    def test_delivered_exports_match_original_geometry(self):
        for collection in (paddle, straight):
            for source, target in collection.FILES.items():
                with self.subTest(target=target):
                    expected = paddle.prepare(source, collection.SOURCE)
                    actual = trimesh.load_mesh(paddle.ROOT / "stl" / target)
                    self.assertTrue(actual.is_watertight)
                    self.assertTrue(actual.is_winding_consistent)
                    self.assertGreater(actual.volume, 0)
                    self.assertEqual(len(actual.split(only_watertight=False)), 1)
                    np.testing.assert_allclose(actual.bounds, expected.bounds, atol=1e-4)
                    self.assertAlmostEqual(actual.volume / expected.volume, 1, places=5)

    def test_dj9fm_parts_preserve_geometry(self):
        self.assertEqual(len(straight.FILES), 8)
        for source in straight.FILES:
            with self.subTest(source=source):
                original = paddle.load_original(source, straight.SOURCE)
                printable = paddle.prepare(source, straight.SOURCE)
                np.testing.assert_allclose(original.extents, printable.extents)
                self.assertAlmostEqual(original.volume, printable.volume, places=4)
                self.assertAlmostEqual(printable.bounds[0, 2], 0, places=6)

    def test_selected_parts_preserve_geometry_and_rest_on_bed(self):
        for source in paddle.FILES:
            with self.subTest(source=source):
                original = paddle.load_original(source)
                printable = paddle.prepare(source)
                np.testing.assert_allclose(original.extents, printable.extents)
                self.assertAlmostEqual(original.volume, printable.volume, places=4)
                self.assertAlmostEqual(printable.bounds[0, 2], 0, places=6)
                self.assertEqual(len(printable.split()), 1)

    def test_standard_paddle_dimensions(self):
        model = paddle.load_original("paddles-standard.stl")
        np.testing.assert_allclose(model.extents, (48, 24, 13.9), atol=0.01)


if __name__ == "__main__":
    unittest.main()
