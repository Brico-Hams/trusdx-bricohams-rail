import unittest

import antenna_accessories
import toroid_case


class PortableAccessoryTests(unittest.TestCase):
    def test_antenna_accessories(self):
        pieces = antenna_accessories.parts()
        self.assertEqual(len(pieces), 2)
        for name, solid in pieces.items():
            with self.subTest(name=name):
                model = antenna_accessories.validate(solid)
                self.assertAlmostEqual(model.bounds[0, 2], 0)
                self.assertAlmostEqual(model.extents[2], 5)

    def test_reference_case(self):
        base, lid, total = toroid_case.build(50, 26)
        toroid_case.validate(base, lid, 50, 26)
        self.assertEqual(total, 30)

    def test_minimum_case(self):
        base, lid, total = toroid_case.build(20, 10)
        toroid_case.validate(base, lid, 20, 10)
        self.assertEqual(total, 14)

    def test_case_rejects_small_dimensions(self):
        for diameter, height in ((19, 26), (50, 9)):
            with self.subTest(diameter=diameter, height=height), self.assertRaises(ValueError):
                toroid_case.build(diameter, height)

    def test_case_validation_detects_wrong_cavity(self):
        base, lid, _ = toroid_case.build(50, 26)
        with self.assertRaisesRegex(RuntimeError, "hueco"):
            toroid_case.validate(base, lid, 54, 26)


if __name__ == "__main__":
    unittest.main()
