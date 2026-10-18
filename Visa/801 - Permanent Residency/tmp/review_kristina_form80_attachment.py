from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from pathlib import Path

base = Path('/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency')
src = base / 'Prepared Documents/Form 80 Attachment - Kristina Aleksandrova Warren - Kristina Completed Draft - WaKr-2631-801-3.docx'
out = base / 'Prepared Documents/Form 80 Attachment - Kristina Aleksandrova Warren - Reviewed Draft - WaKr-2631-801-3.docx'
doc = Document(src)

# Travel: the new Jetstar confirmation shows departure from Bali on 10 October
# and arrival back in Australia on 11 October 2025.
doc.tables[1].rows[3].cells[1].text = '11.10.2025'

# Remove drafting prompts now that Kristina supplied the missing job details.
doc.tables[2].rows[1].cells[4].text = (
    'Animal Attendant - care for animals, prepare and provide diets, '
    'and give educational presentations'
)
doc.tables[2].rows[2].cells[4].text = (
    'Not employed; supported by husband. Studied at TAFE NSW and '
    'volunteered with wildlife organisations.'
)

# Correct clear typographical/omission issues without changing substantive facts.
for row in doc.tables[2].rows:
    for cell in row.cells:
        if 'weight tables' in cell.text:
            cell.text = cell.text.replace('weight tables', 'wait tables')
doc.tables[2].rows[11].cells[6].text = 'Bulgaria'
doc.tables[1].rows[15].cells[3].text = 'Nice, Marseille / France'

# Remove the template-only placeholder row from the visa-history table.
placeholder_row = doc.tables[4].rows[2]._tr
placeholder_row.getparent().remove(placeholder_row)

# Remove a duplicated trailing name paragraph that otherwise creates a blank sixth page.
for paragraph in list(doc.paragraphs):
    if paragraph.text.strip() == 'Kristina Aleksandrova WARREN':
        paragraph._element.getparent().remove(paragraph._element)

# Standardise obvious presentation only.
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.highlight_color = None

# Keep signature handling in the main PDF; this attachment is an agency-review draft.
doc.core_properties.title = 'Form 80 Attachment - Kristina Aleksandrova Warren - Reviewed Draft'
doc.core_properties.subject = 'Subclass 801 Form 80 supporting attachment for agency review'
doc.save(out)
print(out)
