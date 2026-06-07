"""Shared helpers for the glaze-calc scripts: data loading, material lookup,
and converting a recipe (materials by weight) into oxide grams and moles.

No third-party dependencies (Python 3.8+).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def load_oxides():
    d = load("oxides.json")
    d.pop("_meta", None)
    return d


def load_materials():
    d = load("materials.json")
    d.pop("_meta", None)
    return d


def load_base_recipes():
    d = load("base-recipes.json")
    d.pop("_meta", None)
    return d


def _norm(s):
    return " ".join(str(s).lower().replace("-", " ").replace("_", " ").split())


def material_index(materials):
    """Map normalized name/alias -> (canonical_name, material_dict)."""
    idx = {}
    for name, m in materials.items():
        idx[_norm(name)] = (name, m)
        for alias in m.get("aliases", []):
            idx.setdefault(_norm(alias), (name, m))
    return idx


def combined_batch(recipe):
    """Merge 'materials' and 'additions' into one {name: weight} dict.
    Additions are added on top of the base (the studio '+X%' convention)."""
    combined = {}
    for section in ("materials", "additions"):
        for k, v in (recipe.get(section) or {}).items():
            combined[k] = combined.get(k, 0.0) + float(v)
    return combined


def recipe_to_oxides(recipe, materials, oxides):
    """Return (oxide_grams, oxide_moles, unknown_materials)."""
    idx = material_index(materials)
    oxide_g = {}
    unknown = []
    for name, amt in combined_batch(recipe).items():
        hit = idx.get(_norm(name))
        if not hit:
            unknown.append(name)
            continue
        _, m = hit
        for ox, pct in m["analysis"].items():
            oxide_g[ox] = oxide_g.get(ox, 0.0) + amt * pct / 100.0
    oxide_mol = {}
    for ox, g in oxide_g.items():
        if ox not in oxides:
            unknown.append("oxide:" + ox)
            continue
        oxide_mol[ox] = g / oxides[ox]["molar_mass"]
    return oxide_g, oxide_mol, unknown


def load_recipe(arg, base_recipes=None):
    """Resolve a recipe from: a base-recipe code, a path to a JSON file, or '-' for stdin."""
    import sys
    base_recipes = base_recipes if base_recipes is not None else load_base_recipes()
    if arg in base_recipes:
        return base_recipes[arg]
    # case-insensitive base code match
    for code, rec in base_recipes.items():
        if code.lower() == str(arg).lower():
            return rec
    if arg == "-":
        return json.load(sys.stdin)
    with open(arg, encoding="utf-8") as f:
        return json.load(f)
