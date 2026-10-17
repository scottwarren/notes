from pathlib import Path
import shutil

from pypdf import PdfReader, PdfWriter


FILES = [
    Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Bank Statements/cba-2026-07-31-to-2026-08-28-cba-joint-scott-kristina.pdf"),
    Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Bank Statements/cba-2025-08-25-to-2026-02-28-cba-joint-scott-kristina.pdf"),
    Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Bank Statements/cba-2026-03-01-to-2026-07-30-cba-joint-scott-kristina.pdf"),
    Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Leases/Prince-street-Coffs-lease-extension-2026.pdf"),
    Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Leases/Prince-street-Coffs-initial-lease-12-months-07:2025-07-2026.pdf"),
]


def decrypt_pdf(source: Path, output: Path) -> tuple[int, int]:
    reader = PdfReader(source)
    original_pages = len(reader.pages)
    if reader.is_encrypted:
        result = reader.decrypt("")
        if result == 0:
            raise RuntimeError(f"Could not decrypt {source}")

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    with output.open("wb") as stream:
        writer.write(stream)

    check = PdfReader(output)
    if check.is_encrypted:
        raise RuntimeError(f"Output is still encrypted: {output}")
    output_pages = len(check.pages)
    if output_pages != original_pages:
        raise RuntimeError(
            f"Page count changed for {source}: {original_pages} -> {output_pages}"
        )
    return original_pages, output_pages


def main() -> None:
    work_dir = Path(__file__).resolve().parent / "decrypted"
    work_dir.mkdir(parents=True, exist_ok=True)

    staged: list[tuple[Path, Path, int]] = []
    for index, source in enumerate(FILES, start=1):
        output = work_dir / f"{index:02d}-{source.name}"
        original_pages, _ = decrypt_pdf(source, output)
        staged.append((source, output, original_pages))

    for source, output, original_pages in staged:
        shutil.copyfile(output, source)
        check = PdfReader(source)
        if check.is_encrypted or len(check.pages) != original_pages:
            raise RuntimeError(f"Final validation failed for {source}")
        print(f"Accessible: {source} ({original_pages} pages)")


if __name__ == "__main__":
    main()
