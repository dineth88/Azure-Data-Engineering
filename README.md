<img width="6952" height="2768" alt="Image" src="https://github.com/user-attachments/assets/afa0463a-aa35-4285-a543-4a2b909c0c8d" />
<br>
<br>

# Spotify Azure Data Lakehouse | End-to-End Azure Data Engineering Project

This project implements a production-grade Azure Data Lakehouse architecture using Spotify-like datasets, following Bronze → Silver → Gold layers with incremental ingestion, CDC, SCD Type 2, and Unity Catalog governance.

The solution demonstrates how to design, build, and orchestrate scalable data pipelines using Azure Data Factory, Azure Data Lake Gen2, Azure Databricks (Unity Catalog), Delta Live Tables, and Databricks Asset Bundles.

## 🚀 Key Features

Metadata-driven incremental ingestion using Azure Data Factory

Watermark-based CDC with backfill support

Parameterized pipelines with ForEach looping

Bronze → Silver → Gold layered data architecture

Real-time ingestion using Databricks Auto Loader

Delta Live Tables with SCD Type 2 (Auto CDC)

Centralized governance with Unity Catalog

Data quality checks using DLT Expectations

Dynamic SQL generation using Jinja templates

Automated failure notifications via Logic Apps

Fully deployable using Databricks Asset Bundles

## 🏗 Architecture

Azure SQL Database (Source)

Azure Data Factory (Orchestration)

Azure Data Lake Storage Gen2 (Bronze / Silver / Gold)

Azure Databricks (Serverless Compute)

Unity Catalog & Metastore

Delta Lake & Delta Live Tables

## 📂 Data Model

Dimensions: DimUser, DimArtist, DimTrack, DimDate, FactStream

Fact: FactStream

## 🛠 Tech Stack

Azure Data Factory · Azure Data Lake Gen2 · Azure Databricks ·
Unity Catalog · Delta Lake · Delta Live Tables ·
PySpark · SQL · Jinja2 · Logic Apps

### Bronze layer pipeline

<img width="784" height="314" alt="Image" src="https://github.com/user-attachments/assets/7bd0af2e-4b1e-43c7-a818-126dec94b2d1" />
<img width="739" height="234" alt="Image" src="https://github.com/user-attachments/assets/692a0f0d-aba5-4ea5-82b0-750e4781e773" />

### Gold layer pipeline

<img width="629" height="586" alt="Image" src="https://github.com/user-attachments/assets/7d3f787a-7135-4843-bd21-f0cd89e236e2" />

### Resource group

<img width="6952" height="2768" alt="Image" src="https://github.com/user-attachments/assets/74ad7e8a-322c-432e-a5c2-ac253b37b3cc" />
