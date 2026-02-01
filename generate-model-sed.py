#!/usr/bin/env python3
"""Generate sed replacements for AI models from models.json.

Usage: python generate-model-sed.py [--apply]

Without --apply: prints the sed lines to stdout
With --apply: updates the AI Models section in pre-ai.sh
"""
import json
import sys
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MODELS_JSON = SCRIPT_DIR / "models.json"
PRE_AI_SH = SCRIPT_DIR / "pre-ai.sh"

# Markers for the auto-generated section
START_MARKER = "  # === AI MODELS (auto-generated) ==="
END_MARKER = "  # === END AI MODELS ==="


def load_models():
    with open(MODELS_JSON) as f:
        data = json.load(f)
    return data.get("companies", {}), data.get("models", {})


def generate_sed_lines(companies, models):
    """Generate sed replacement lines."""
    lines = []

    # Companies first
    lines.append("  # Companies")
    for correct, variants in sorted(companies.items()):
        for variant in variants:
            if variant.lower() != correct.lower():
                lines.append(f"  -e 's/{variant}/{correct}/gi' \\")

    # Then models
    lines.append("  # Models")
    for correct, variants in sorted(models.items()):
        for variant in variants:
            if variant.lower() != correct.lower():
                lines.append(f"  -e 's/{variant}/{correct}/gi' \\")

    return lines


def apply_to_script(sed_lines):
    """Replace the AI Models section in pre-ai.sh."""
    content = PRE_AI_SH.read_text()

    # Check if markers exist
    if START_MARKER not in content:
        print(f"ERROR: Could not find start marker in pre-ai.sh")
        print(f"Add these markers where you want the AI models section:")
        print(f"  {START_MARKER}")
        print(f"  {END_MARKER}")
        return False

    if END_MARKER not in content:
        print(f"ERROR: Could not find end marker in pre-ai.sh")
        return False

    # Build new section
    new_section = START_MARKER + "\n" + "\n".join(sed_lines) + "\n" + END_MARKER

    # Replace old section
    pattern = re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER)
    new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)

    PRE_AI_SH.write_text(new_content)
    print(f"Updated {PRE_AI_SH}")
    print(f"  {len(sed_lines)} sed replacements generated")
    return True


def main():
    companies, models = load_models()
    sed_lines = generate_sed_lines(companies, models)

    if "--apply" in sys.argv:
        apply_to_script(sed_lines)
    else:
        print("# Generated sed replacements for AI models")
        print("# Run with --apply to update pre-ai.sh")
        print()
        for line in sed_lines:
            print(line)


if __name__ == "__main__":
    main()
