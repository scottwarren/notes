from __future__ import annotations

import json
import re
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1] / "Visa 801 - Document Checklist.md"


def clean_inline(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).replace("`", "")


def main() -> None:
    output: list[str] = []
    styles: list[dict[str, object]] = []
    cursor = 1

    for raw in SOURCE.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# "):
            text, style = clean_inline(raw[2:]), "TITLE"
        elif raw.startswith("## "):
            text, style = clean_inline(raw[3:]), "HEADING_1"
        elif raw.startswith("### "):
            text, style = clean_inline(raw[4:]), "HEADING_2"
        else:
            style = None
            indent = len(raw) - len(raw.lstrip("\t "))
            stripped = raw.lstrip("\t ")
            match = re.match(r"\* \[([ xX])\] (.*)", stripped)
            if match:
                mark = "☑" if match.group(1).lower() == "x" else "☐"
                text = ("    " if indent else "") + mark + " " + clean_inline(match.group(2))
            elif stripped.startswith("* "):
                text = ("    " if indent else "") + "• " + clean_inline(stripped[2:])
            else:
                text = clean_inline(raw)

        line = text + "\n"
        output.append(line)
        if style:
            styles.append({"start": cursor, "end": cursor + len(line), "style": style})
        cursor += len(line)

    print(json.dumps({"text": "".join(output), "styles": styles}, ensure_ascii=False))


if __name__ == "__main__":
    main()
