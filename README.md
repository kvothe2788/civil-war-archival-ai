# Civil War Archival AI

**Investigating historical evidence with AI assistance, archival records and geospatial analysis — while testing the limits of what the evidence can support.**

This independent research project began with a family question: where was Modesto Fernández Abad, a railway worker who died in 1937, buried? His family has preserved an account involving a path near Matarrosa del Sil, a small watercourse and a pool. We are using this case to explore how AI-assisted research can help navigate fragmented historical records without turning an unverified account into a false conclusion.

**The burial site has not been identified.** The reported pool, the account of remains exposed by rain, and the relationship between historical and modern locations remain unverified.

## Why this project matters for AI research

Searching imperfect records can encourage language models to invent citations, merge people with similar names, overinterpret maps, or express unwarranted confidence. These errors are particularly consequential when researching missing people and family memory.

The project combines a real-world archival investigation with a proposed research direction: evaluating whether AI systems can make traceable claims, distinguish evidence from inference, and abstain when documents do not support an answer. This evaluation is **planned**, not a completed benchmark.

## Research workflow

1. **Define the question and record uncertainty.** Separate family testimony, primary sources, secondary accounts and hypotheses.
2. **Find and inspect sources.** Consult archival catalogues, historical gazettes, mine concession records, railway records and cartography. A catalogue entry does not mean an entire file has been inspected.
3. **Use AI as an assistant.** Explore document discovery, transcription and synthesis; check citations and consequential claims against the underlying source. AI output is not primary evidence.
4. **Compare historical geography.** Examine historic aerial photography, maps, modern mapped watercourses and a terrain model to identify questions for further checking.
5. **Track negative results and limitations.** A steep modelled slope is not evidence of a waterfall, a pool, human remains or a grave. Locations and interpretations require independent verification.

## Selected documented observations

- A 1916 mining record identifies a bridge or culvert over the *arroyo del Escandal* on the Ponferrada–La Espina road. It does not establish the identity of the modern crossing or identify a burial site.
- A 1947 provincial gazette refers to a washery associated with the Escandal mining group. It does not establish that the currently labelled location is the same facility or that it existed in 1937.
- Exploratory profiles were sampled from a modern 2 m terrain model along present-day mapped watercourses. The terrain model and mapped line have spatial and historical uncertainties and do not establish a waterfall or pool.

See the [evidence register](docs/evidence-register.md) for source links, scope and limitations.

## Repository

- [Research method and evidence standards](docs/methodology.md)
- [Evidence register and open questions](docs/evidence-register.md)
- [Reproduction notes](docs/reproducibility.md)
- [Exploratory terrain-profile script](src/lidar2_analisis.py)

The script is an early research artifact, not a packaged pipeline. It requires separately obtained source data and geospatial dependencies. See the reproduction notes before using it.

## Proposed AI safety evaluation

The next stage is to curate a small, source-grounded test set from records that can be used and shared appropriately. Candidate tasks include identifying unsupported claims, verifying citations against supplied documents, handling conflicting place names, and declining to infer a burial location when evidence is insufficient. Proposed measurements include claim support, citation accuracy, appropriate abstention and useful partial answers, with human review and a held-out evaluation set.

No benchmark results, safety claims or automated grave-location capability are asserted here.

## Privacy and responsible use

This public repository is a curated research overview. It excludes private family photographs, correspondence, personal documents and the full local working archive. Third-party source material and maps remain subject to their respective rights and access conditions. Do not use this repository to direct excavation or treat candidate areas as confirmed burial sites.

**Project status:** ongoing, independent research. Contributions and corrections should preserve source attribution and distinguish verified evidence from inference.

