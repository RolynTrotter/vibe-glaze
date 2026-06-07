#!/usr/bin/env python3
"""Unit and batch conversions for glaze work.

Subcommands:
  g-oz   <grams>                 grams -> ounces
  oz-g   <ounces>                ounces -> grams
  c-f    <celsius>               degC -> degF
  f-c    <fahrenheit>            degF -> degC
  cone   <cone>                  cone -> approx temperature (e.g. cone 6)
  batch  <recipe> <dry_grams>    scale a recipe to a dry batch weight (grams)
  add    <base_dry_grams> <pct>  grams for a +pct% addition on a dry batch
  sg     <specific_gravity>      slurry SG -> % solids by weight
                                 (optional 2nd arg: solids density, default 2.6)

Examples:
  python3 convert.py cone 6
  python3 convert.py batch G2926B 5000
  python3 convert.py add 5000 3        # +3% on a 5000 g batch
  python3 convert.py sg 1.45
"""
import sys

import glazelib as g

# Orton large cones, ~60 degC/hr (heatwork - not a thermometer reading).
# Approximate; ramp rate shifts these by ~10-20 degC. Source: Orton cone charts.
CONE_C = {
    "022": 600, "021": 614, "020": 635, "019": 683, "018": 717, "017": 747,
    "016": 792, "015": 804, "014": 838, "013": 852, "012": 884, "011": 894,
    "010": 900, "09": 923, "08": 955, "07": 984, "06": 999, "05": 1046,
    "04": 1060, "03": 1101, "02": 1120, "01": 1137,
    "1": 1154, "2": 1162, "3": 1168, "4": 1186, "5": 1196, "6": 1222,
    "7": 1240, "8": 1263, "9": 1280, "10": 1305, "11": 1315, "12": 1326,
}


def cone_key(s):
    s = s.lower().replace("cone", "").replace("^", "").strip()
    if s.startswith("0") and len(s) > 1:
        return s  # 04, 06, 010 ...
    return str(int(s)) if s.lstrip("-").isdigit() else s


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    cmd = a[0]
    try:
        if cmd == "g-oz":
            print(f"{float(a[1]):.1f} g = {float(a[1]) / 28.3495:.3f} oz")
        elif cmd == "oz-g":
            print(f"{float(a[1]):.3f} oz = {float(a[1]) * 28.3495:.1f} g")
        elif cmd == "c-f":
            print(f"{float(a[1]):.1f} degC = {float(a[1]) * 9 / 5 + 32:.1f} degF")
        elif cmd == "f-c":
            print(f"{float(a[1]):.1f} degF = {(float(a[1]) - 32) * 5 / 9:.1f} degC")
        elif cmd == "cone":
            k = cone_key(a[1])
            if k not in CONE_C:
                sys.exit(f"Unknown cone '{a[1]}'. Known: {', '.join(CONE_C)}")
            c = CONE_C[k]
            print(f"Cone {k} ~ {c} degC / {c * 9 / 5 + 32:.0f} degF "
                  "(large cone, ~60 degC/hr; heatwork, varies with ramp).")
        elif cmd == "batch":
            recipe = g.load_recipe(a[1])
            dry = float(a[2])
            combined = g.combined_batch(recipe)
            total = sum(combined.values())
            factor = dry / total
            print(f"Scale {recipe.get('name', a[1])} to {dry:.0f} g dry "
                  f"(recipe total {total:.1f}):\n")
            for name, amt in combined.items():
                print(f"  {name:<24} {amt * factor:8.1f} g")
            print(f"  {'-' * 24} {'-' * 8}")
            print(f"  {'TOTAL':<24} {dry:8.1f} g")
        elif cmd == "add":
            base, pct = float(a[1]), float(a[2])
            print(f"+{pct}% on {base:.0f} g = {base * pct / 100:.1f} g addition")
        elif cmd == "sg":
            sg = float(a[1])
            rho = float(a[2]) if len(a) > 2 else 2.6
            if sg <= 1:
                sys.exit("SG must be > 1.0")
            solids = (sg - 1) * rho / (rho - 1)  # g solids per mL slurry
            pct = solids / sg * 100
            print(f"SG {sg:.3f} (solids density {rho}) -> "
                  f"{pct:.1f}% solids by weight, "
                  f"{solids:.3f} g solids/mL. "
                  "(dipping ~1.40-1.50; brushing ~1.25-1.35)")
        else:
            print(__doc__)
            sys.exit(f"Unknown subcommand '{cmd}'.")
    except (IndexError, ValueError) as e:
        sys.exit(f"Bad arguments for '{cmd}': {e}\n\n{__doc__}")


if __name__ == "__main__":
    main()
