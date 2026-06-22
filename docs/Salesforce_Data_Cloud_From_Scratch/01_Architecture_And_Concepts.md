# 01 — Architecture & Core Concepts

## 🧠 The One Idea

**Data Cloud is an assembly line for customer data.** Raw materials (data) come in one end, move
through stations (ingest → map → unify → enrich → act), and finished products (segments, insights,
grounded AI answers) come out the other. If you learn the **order of the stations**, every feature
later has an obvious place.

The one-liner: **"Data Cloud is a pipeline: ingest → model → map → unify → insights → segment →
activate."**

---

## 1. The pipeline (memorize this order)

1. **Data Streams** ingest from sources → land as **DLOs** (raw).
2. **Mapping** connects DLO fields to the **Customer 360 Data Model** → **DMOs** (harmonized).
3. **Identity Resolution** merges duplicate individuals → **Unified Profile**.
4. **Calculated Insights** compute metrics/KPIs on top.
5. **Segmentation** builds audiences.
6. **Activation** sends segments out; **AI** grounds on the unified data.

Every later lesson is just one of these stations in depth.

---

## 2. The lakehouse foundation

Under the hood Data Cloud is a **lakehouse**: the cheap, huge storage of a **data lake** plus the
structure and query power of a **data warehouse**. This is why it can hold billions of events and
still let you query and segment them. It's built on open formats so other tools can read it.

---

## 3. Data Spaces — tenancy within your org

A **Data Space** is a logical partition of your Data Cloud — like separate folders for different
brands, regions, or business units. Data, segments, and insights can be isolated per space (e.g.,
"EMEA" vs "Americas") so teams don't step on each other. Most learning happens in the **default**
data space.

---

## 4. The object layers (preview of Lesson 03)

- **DLO (Data Lake Object)** — raw ingested data, schema preserved.
- **DSO (Data Stream Object)** — a normalized view of a DLO that feeds processing.
- **DMO (Data Model Object)** — the harmonized, semantic model the rest of Salesforce queries.
- **Unified DMO** — DMO data after identity resolution.
- **CIO (Calculated Insight Object)** — stored computed metrics.

That `DLO → DMO → Unified` flow is the spine of the whole platform.

---

## 5. The Customer 360 Data Model

Salesforce ships a **standard semantic model** with entities like **Individual**, **Contact
Point Email/Phone**, **Sales Order**, **Engagement**, etc. You **map** your messy source fields
onto these standard objects so everything speaks one language. You can extend it with custom DMOs.

---

## 6. Key building blocks you'll meet

| Concept | One-liner |
|---|---|
| Data Stream | the pipe bringing a source's data in |
| DLO / DSO / DMO | raw / normalized / harmonized layers |
| Identity Resolution | merges duplicates into a unified profile |
| Calculated Insight | a computed metric (batch or streaming) |
| Segment | a filtered audience of unified profiles |
| Activation | sending a segment to a target system |
| Data Space | logical partition of the platform |

---

## 🌍 Real-World Example

**A retailer traces one purchase through every station.** A loyalty member's in-store purchase
enters via the POS data stream (landing in a DLO), gets mapped to the Sales Order DMO, links to her
Unified Individual after identity resolution, pushes her Lifetime Value insight past $5,000,
qualifies her for the "VIP, no recent purchase" segment, and finally activates into a win-back
email. The architecture is just those six stations in order — and being able to name them is what
makes debugging tractable.

---

## 🔬 Under the Hood (In-Depth)

- **Lakehouse = open table formats** — Data Cloud stores data in open columnar formats
  (Iceberg/Parquet-style), which is what enables zero-copy sharing with Snowflake/BigQuery without
  duplicating storage.
- **Data Spaces are logical, not separate orgs** — they partition data, segments, and permissions
  within one Data Cloud instance for brand/region isolation, without multi-tenant overhead.
- **DLO/DSO/DMO are layers, not copies you manage** — the DSO is auto-created to normalize the DLO;
  you mainly curate the DLO→DMO mapping and the platform handles the plumbing between.
- **Storage and compute are separate** — segmentation, identity resolution, and insights are jobs
  that scan the lakehouse on demand, so cost scales with *processing*, not just stored volume.
- **The Customer 360 model is a shared contract** — because every Salesforce cloud agrees on the
  same DMO schema, mapping once makes data usable everywhere downstream.

---

## 🎤 Say this in the interview

- *"The pipeline is **ingest → map → unify → insights → segment → activate**; everything in Data
  Cloud is one of those stations."*
- *"It's built on a **lakehouse** — data-lake scale plus warehouse-style query — using open
  formats."*
- *"**Data Spaces** partition the org by brand/region/BU, and the **Customer 360 Data Model** is
  the standard semantic schema I map sources onto."*

➡️ **Next:** [02 — Data streams & ingestion](./02_Data_Streams_And_Ingestion.md)
