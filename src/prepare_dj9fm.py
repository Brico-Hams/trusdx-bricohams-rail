"""Prepara originales DJ9FM / willie42, CC BY-NC 4.0, sin cambiar la geometria."""
from prepare_k6ark import ROOT, export_parts


SOURCE = ROOT / "vendor" / "dj9fm-key"
FILES = {
    "taste-base2.stl": "dj9fm-key-base.stl",
    "taste-arm2.stl": "dj9fm-key-arm2.stl",
    "taste-button2.stl": "dj9fm-key-button2.stl",
    "taste-distance.stl": "dj9fm-key-distance.stl",
    "taste-magnetmount.stl": "dj9fm-key-magnetmount.stl",
    "taste-arm.stl": "dj9fm-key-arm-alternative.stl",
    "taste-button.stl": "dj9fm-key-button-alternative.stl",
    "taste-knopf2.stl": "dj9fm-key-knopf2-alternative.stl",
}


if __name__ == "__main__":
    export_parts(SOURCE, FILES)
    print("DJ9FM / willie42; CC BY-NC 4.0. Orientacion final de laminado y montaje pendientes.")
