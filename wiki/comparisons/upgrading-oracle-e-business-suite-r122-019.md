---
title: "upgrading oracle e business suite r122 019"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - async
  - data
  - image-generation
  - vector-database
---

# upgrading oracle e business suite r122 019

> **Source:** upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-ii-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01949795077.html ingested: 2026-07-17 sha256: dae94efbc8d4bc959ef264c7c223d542ada7abb1f33b4588d2582b097c47...
> **Sources:**
>   - upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-ii-2026-07-17.md
> **Links:**
- [[upgrading-oracle-e-business-suite-r122]]
- [[changing-oracle-applications-user]]
- [[how-to-patch-oracle-database-to-1931-on]]
- [[oracle-database-26ai-installation-using]]
- [[sequoia-ascent]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01949795077.html
ingested: 2026-07-17
sha256: dae94efbc8d4bc959ef264c7c223d542ada7abb1f33b4588d2582b097c4796cb
blog_source: Oracle DBA Soyma
---
- 
- 
- 
- 
- 
- 
- 
- 
Soumya's Database Blog : Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part II
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## May 24, 2026
### 
Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part II
 This post is continuation of the first part of the post : [Part I](https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122.html)
*[oraprod@non-prod-db patch]$ sh checkDBpatch.sh*
In the application server, run checkMTpatch.sh
cd
/apdata/patch/ETCC
 
Invoke run filesystem
 
[appltest@testapp
~]$ . /apdata/erp/EBSapps.env run
 
[appltest@testapp
patch]$ sh checkMTpatch.sh
 +===============================================================+
 
===============================================================================
PATCH
RECOMMENDATION SUMMARY
===============================================================================
One or
more products have bugfixes missing.
The
default patch recommendations to install these missing bugfixes are:
 
-------------------------------------------------------------------------------
Oracle Forms and Reports 10.1.2.3.0
-------------------------------------------------------------------------------
  Patch 27491934
    - Filename: p27491934_101232_LINUX.zip
 
  Patch 32922089
    - Filename: p32922089_101232_LINUX.zip
 
 
-------------------------------------------------------------------------------
Oracle Fusion Middleware (FMW) - Web
Tier 11.1.1.9.0
-------------------------------------------------------------------------------
  Patch 35540062
    - Filename:
p35540062_111190_Linux-x86-64.zip
 
  Patch 32287205 [IMPORTANT: Follow Note
2555355.1 before applying.]
    - Filename:
p32287205_111190_Linux-x86-64.zip
 
  Patch 23716938
    - Filename: p23716938_111190_Generic.zip
 
  Patch 32928416
    - Filename:
p32928416_111190_Linux-x86-64.zip
 
  Patch 33144848
    - Filename:
p33144848_111190_Linux-x86-64.zip
 
Patch
34067016
    - Filename:
p34067016_11119210420OSS_Linux-x86-64.zip
 
 
-------------------------------------------------------------------------------
FMW - Web Tier 11.1.0.7.0
-------------------------------------------------------------------------------
  Patch 22290164
    - Filename:
p22290164_111070_Linux-x86-64.zip
 
 
-------------------------------------------------------------------------------
Oracle Fusion Mi

## Summary

See Key Findings for full content.

## Related Articles

- [[upgrading-oracle-e-business-suite-r122]]
- [[changing-oracle-applications-user]]
- [[how-to-patch-oracle-database-to-1931-on]]
- [[oracle-database-26ai-installation-using]]
- [[sequoia-ascent]]
