---

title: "Databricks"
type: entity
description: Data and AI platform company behind Delta Lake, MLflow, and open-weight AI models
created: 2026-07-06
updated: 2026-07-06
tags: [llm-wiki, company, open-source-llm]
sources: [raw/articles/open-source-llm-landscape-2026.md]
confidence: high
links: [llm-wiki, open-source-llm, mlflow, delta-lake, apache-spark]

---


# Databricks

## Overview

Databricks is a data and AI platform company founded in 2013 by the original creators of Apache Spark. The company provides a unified platform for data engineering, data science, machine learning, and AI applications. Databricks has become a leader in enterprise AI, offering tools for building, deploying, and managing AI applications at scale. The company is known for its open-source contributions, Delta Lake data format, and MLflow machine learning lifecycle management.

## Key Facts

| Field | Details |
|
|---|
| **Founded** | 2013 |
| **Headquarters** | San Francisco, California, USA |
| **Co-founders** | Ali Ghodsi (CEO), Matei Zaharia (Apache Spark creator), Ion Stoica |
| **Type** | Public company (NYSE: DATABRICKS) |
| **Key Investors** | Adobe, Salesforce Ventures, Greycroft, Dragoneer |
| **Valuation (2024)** | ~$42B (post-IPO) |
| **Employees** | ~10,000+ |

## Models & Products

### Open-Source AI Models
- **DBRX** (2024) — 132B parameters, MoE architecture, open-weight
- **MPT (MosaicML)** (2023) — Acquired from MosaicML, 7B/30B/70B parameters
- **Dolly** (2022) — Early open-weight instruction-tuned model
- **Llama fine-tuning** — Optimized Llama variants for enterprise use

### AI Platform Products
- **Databricks AI** — Unified AI platform for building and deploying models
- **Databricks Runtime** — Optimized runtime for ML and data workloads
- **Databricks Studio** — Interactive development environment
- **Databricks Workflows** — Orchestration for ML pipelines
- **Databricks Model Serving** — Production model deployment
- **Databricks Feature Store** — ML feature management
- **Databricks Model Registry** — ML model lifecycle management
- **Databricks SQL** — SQL analytics on data lakehouse
- **Databricks AutoML** — Automated machine learning
- **Databricks MLOps** — Machine learning operations tools

### Data Platform Products
- **Delta Lake** — Open-source storage format for reliable data lakes
- **MLflow** — ML lifecycle management (tracking, packaging, deployment)
- **Apache Spark** — Distributed data processing engine (created by Databricks)
- **Photon** — Accelerated query engine for Delta Lake
- **Unity Catalog** — Unified governance for data and AI
- **Databricks Marketplace** — Data and AI model marketplace

## Infrastructure

- **Training hardware**: NVIDIA GPU clusters, Databricks Runtime optimization
- **Compute partnerships**: AWS (primary), Azure, Google Cloud
- **Context window**: Varies by model (DBRX: 32K, MPT: 8K)
- **Fine-tuning**: Supports custom fine-tuning via Databricks AI
- **Safety**: Enterprise-grade security, compliance certifications

## Business Model

Databricks operates a platform-focused model:
- **Platform subscription**: Per-user, per-workload pricing
- **Cloud marketplace**: Revenue share with AWS, Azure, GCP
- **Enterprise**: Custom deployments, dedicated infrastructure
- **Marketplace**: Revenue from data and AI model marketplace
- **Competitive strategy**: Unified data + AI platform vs point solutions

## Open Source Policy

Databricks is **strongly committed to open-source**:
- **Open-weight models**: DBRX, MPT, Dolly — freely available
- **Open-source tools**: MLflow, Delta Lake, Apache Spark — all open-source
- **Community-driven**: Strong open-source community contributions
- **Competes with**: OpenAI (closed), Anthropic (closed), Google (partially open)
- **Philosophy**: "Open-source accelerates data and AI progress"

## Relationships

- **AWS**: Primary cloud partner, significant AWS investment
- **NVIDIA**: GPU supplier, co-developer
- **Microsoft**: Azure partnership
- **Google**: GCP partnership
- **Meta**: Competitor and collaborator (both open-weight)
- **Community**: Strong open-source community (Spark, MLflow, Delta Lake)

## Recent Developments (2024-2026)

1. **IPO** (2024) — Public listing on NYSE
2. **DBRX launch** (2024) — 132B MoE open-weight model
3. **MosaicML acquisition** (2023) — Acquired MosaicML for $1.3B
4. **Databricks AI** — Unified AI platform launch
5. **Unity Catalog** — Unified governance for data and AI
6. **MLflow 3.0** — Enhanced ML lifecycle management
7. **Delta Lake 3.0** — New features for performance and reliability
8. **Enterprise growth** — Growing Fortune 500 customer base

## Controversies

- **MosaicML acquisition** — Concerns about open-source company acquisition
- **Data privacy** — Enterprise data handling and security
- **Competition with open-source** — Platform vs. open-source debate
- **Pricing complexity** — Enterprise pricing can be opaque

## See Also
- [[openai]]
- [[anthropic]]
- [[deepmind]]
- [[meta-ai]]
- [[mistral-ai]]
- [[qwen]]
- [[hugging-face]]
- [[llm-quantization]]
- [[llm-fine-tuning]]