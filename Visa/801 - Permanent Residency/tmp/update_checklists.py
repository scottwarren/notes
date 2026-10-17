from pathlib import Path

def repl(path, pairs):
    p=Path(path); s=p.read_text()
    for old,new in pairs:
        if old not in s:
            print(f'MISSING in {path}: {old[:90]}')
        s=s.replace(old,new)
    p.write_text(s)

repl('Visa 801 - Document Checklist.md', [
("* [ ] **[P1] Two updated Form 888 witness statements** — Mum's draft has been received and reviewed; correct the issues listed in the review notes, then complete signing and witnessing. Jaya's updated statement is still required.",
 "* [ ] **[P1] Two updated Form 888 witness statements** — Mum's draft has been received and reviewed. Jaya's first review draft has now been prepared from her 2024 Form 888 using the current agency template. Both witnesses must confirm their drafts, remove review notes, attach identity evidence as directed, and complete signing and witnessing."),
("* [ ] **[P1] Legal commitments** — Scott's IOOF beneficiary nomination has been captured and shows Kristina as 100% beneficiary under a binding non-lapsing nomination. Retrieve Kristina's beneficiary nomination and decide whether any other evidence is relevant.",
 "* [x] **[P1] Legal commitments** — beneficiary evidence has been gathered for both partners, together with the joint leases. Scott's IOOF nomination shows Kristina as 100% beneficiary under a binding non-lapsing nomination."),
("* [x] Scott's IOOF beneficiary nomination captured; Kristina is nominated for 100% under a binding non-lapsing nomination.",
 "* [x] Superannuation beneficiary evidence gathered for both partners. Scott's IOOF nomination shows Kristina as 100% beneficiary under a binding non-lapsing nomination."),
("* [x] Mum's witness statement draft received and reviewed; corrections and signing remain.",
 "* [x] Mum's witness statement draft received and reviewed; corrections and signing remain. Jaya's review draft has been prepared from her 2024 Form 888 in the current agency template."),
("* [ ] Subclass 820 Grant Letter","* [x] Subclass 820 Grant Letter — filed locally and in the Google Drive Evidence folder."),
("* [ ] [P1] Legal commitments that you and your partner have undertaken as a couple — **PARTIAL: joint leases and Scott's IOOF beneficiary nomination gathered; Kristina's beneficiary nomination remains.**",
 "* [x] [P1] Legal commitments that you and your partner have undertaken as a couple — **GATHERED: joint leases and superannuation beneficiary evidence for both partners are available.**"),
("\t* [ ] Scott's passport","\t* [x] Scott's passport — current biographical page added to Evidence."),
("* [ ] **Kristina's superannuation beneficiary evidence** — Scott has personally seen the nomination in Kristina's AustralianSuper account. Log in with Kristina and capture evidence showing Scott as beneficiary; record the nomination type and percentage if displayed.",
 "* [x] **Kristina's superannuation beneficiary evidence** — added to Evidence; no further review requested."),
("* [ ] Legal commitments — Scott's IOOF nomination is gathered and shows Kristina at 100% under a binding non-lapsing nomination. Locate Kristina's nomination naming Scott and identify any other relevant commitments, if applicable.",
 "* [x] Legal commitments — beneficiary evidence for both partners and the joint leases have been gathered."),
("Resolved — England wedding did not proceed and is removed. Christmas 2024 is clearly earlier context. Current plans for Sydney, a home in 3–4 years and ongoing conversations about children are incorporated. The superannuation home-deposit wording records your intention, not an eligibility assessment.",
 "Resolved — the social section now records the February 2026 Bad Bunny concert in Sydney, the August 2026 whale-watching outing with Kristina's friends, time with Kristina's friend and her husband in January 2026, and the way family and friendships have continued since the move to Coffs Harbour. Christmas 2024 remains earlier context. Current plans for Sydney, a home in 3–4 years and ongoing conversations about children are incorporated. The superannuation home-deposit wording records your intention, not an eligibility assessment.")
])

repl('Prepared Documents/Visa 801 Central Review Checklist.md', [
("[ ] Kristina's superannuation beneficiary evidence — Scott has personally seen the nomination in Kristina's AustralianSuper account. Log in with Kristina and capture evidence showing Scott as beneficiary; record the nomination type and percentage if displayed.",
 "[x] Kristina's AustralianSuper beneficiary evidence has been added to Evidence; no further review is requested."),
("[ ] P1 Legal commitments — leases and Scott's IOOF beneficiary nomination are gathered. Kristina is shown as Scott's 100% beneficiary under a binding non-lapsing nomination. Retrieve Kristina's nomination naming Scott and identify any other relevant commitments, if applicable.",
 "[x] P1 Legal commitments — joint leases and superannuation beneficiary evidence for both partners have been gathered."),
("[ ] P1 Witnesses — obtain two updated Form 888s. Jaya and Mum are the people tagged in the original checklist; confirm the intended witnesses and track both responses.",
 "[ ] P1 Witnesses — Mum's draft has been reviewed. Jaya's first review draft has been prepared from her 2024 Form 888 using the current agency template. Both drafts still need witness confirmation, removal of review notes, identity attachments as directed, and signing/witnessing."),
("[ ] Identity — current passport biographical pages for Kristina and Scott (and any other included applicant), Kristina’s Bulgarian national ID and NSW licence. Confirm with Affinity whether her Bulgarian licence is also wanted.",
 "[ ] Identity — current passport biographical pages for Kristina and Scott and Kristina's NSW licence have been added to Evidence. Kristina's Bulgarian national ID remains outstanding. Confirm with Affinity whether her Bulgarian licence is also wanted."),
("[ ] Grant letter — provide the Subclass 820 grant letter.",
 "[x] Grant letter — the Subclass 820 grant letter dated 24 September 2025 has been filed locally and uploaded to Evidence."),
("Resolved — Scott's IOOF beneficiary nomination has been captured. It names Kristina as 100% beneficiary under a binding non-lapsing nomination.",
 "Resolved — superannuation beneficiary evidence has been gathered for both partners. Scott's IOOF nomination names Kristina as 100% beneficiary under a binding non-lapsing nomination."),
("Resolved — England wedding did not proceed and is removed. Christmas 2024 is clearly earlier context. Current plans for Sydney, a home in 3–4 years and ongoing conversations about children are incorporated. The superannuation home-deposit wording records your intention, not an eligibility assessment.",
 "Resolved — the social section now records the February 2026 Bad Bunny concert in Sydney, the August 2026 whale-watching outing with Kristina's friends, time with Kristina's friend and her husband in January 2026, and ongoing family and friendship contact since the move to Coffs Harbour. Christmas 2024 remains earlier context. Current plans for Sydney, a home in 3–4 years and ongoing conversations about children are incorporated. The superannuation home-deposit wording records your intention, not an eligibility assessment.")
])

repl('Prepared Documents/Visa 801 Outstanding Items Report.md', [
("* [ ] **Two updated Form 888 statements** — correct Mum's reviewed draft, then arrange signing and witnessing. Obtain Jaya's updated statement and arrange signing and witnessing.",
 "* [ ] **Two updated Form 888 statements** — correct Mum's reviewed draft. Review Jaya's newly prepared draft, confirm the highlighted details, remove the review notes, then arrange identity attachments, signing and witnessing for both statements."),
("* [ ] **Kristina's AustralianSuper beneficiary evidence** — log in with Kristina and capture a clear page showing Scott as beneficiary. Record the nomination type and percentage if displayed.\n", ""),
("* [ ] Current passport biographical page for Kristina.","* [x] Current passport biographical page for Kristina — added to Evidence."),
("* [ ] Current passport biographical page for Scott.","* [x] Current passport biographical page for Scott — added to Evidence."),
("* [ ] Kristina's current NSW driver licence.","* [x] Kristina's current NSW driver licence — added to Evidence."),
("* [ ] Subclass 820 grant letter.","* [x] Subclass 820 grant letter — filed locally and uploaded to Evidence."),
("* [x] Scott has personally seen that he is a beneficiary of Kristina's AustralianSuper account. Documentary evidence remains to be captured.",
 "* [x] Kristina's AustralianSuper beneficiary evidence naming Scott has been added to Evidence."),
("* [x] Scott's IOOF beneficiary evidence naming Kristina as 100% beneficiary under a binding non-lapsing nomination.",
 "* [x] Superannuation beneficiary evidence for both partners; Scott's IOOF nomination names Kristina as 100% beneficiary under a binding non-lapsing nomination."),
("* [x] Add broader ordinary-activity and social coverage, including walking, sailing and time with friends.",
 "* [x] Add broader ordinary-activity and social coverage, including walking, whale watching and time with friends."),
("## 3. Relationship statement facts now confirmed", "## 3. Relationship statement facts now confirmed\n\n* [x] Social details added: Bad Bunny concert in Sydney in February 2026; whale watching with Kristina's friends in August 2026; January 2026 time with Kristina's friend and her husband; closer family relationships maintained mainly by telephone and video calls; and Kristina's local friendship group in Coffs Harbour.")
])
