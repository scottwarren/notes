from pathlib import Path
import re


ROOT = Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa")
PROPOSAL = Path("/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/Document Rename Proposal - WaKr-2631-801-3.md")


def load_renames() -> list[tuple[Path, Path]]:
    current_dir: Path | None = None
    renames: list[tuple[Path, Path]] = []
    row_pattern = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \|$")

    for line in PROPOSAL.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            heading = line[3:]
            if heading == "(root)":
                current_dir = ROOT
            elif heading.startswith("Evidence/") or heading in {
                "ID Documents",
                "Seed Documents",
                "Seed documents from Agency",
            }:
                current_dir = ROOT / heading
            else:
                current_dir = None
            continue

        match = row_pattern.match(line)
        if match and current_dir is not None:
            old_name, new_name = match.groups()
            renames.append((current_dir / old_name, current_dir / new_name))

    return renames


def main() -> None:
    renames = load_renames()
    if len(renames) != 92:
        raise RuntimeError(f"Expected 92 approved renames, found {len(renames)}")

    for source, target in renames:
        if not source.is_file():
            raise FileNotFoundError(f"Source missing: {source}")
        if target.exists():
            raise FileExistsError(f"Target already exists: {target}")
        if source.parent != target.parent:
            raise RuntimeError(f"Rename would move a file: {source} -> {target}")

    for source, target in renames:
        source.rename(target)

    failures = []
    for source, target in renames:
        if source.exists() or not target.is_file():
            failures.append(f"{source} -> {target}")
    if failures:
        raise RuntimeError("Rename verification failed:\n" + "\n".join(failures))

    print(f"Applied and verified {len(renames)} approved renames.")


if __name__ == "__main__":
    main()
