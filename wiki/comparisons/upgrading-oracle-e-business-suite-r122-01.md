---
title: "upgrading oracle e business suite r122 01"
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

# upgrading oracle e business suite r122 01

> **Source:** upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-iii-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_0156654061.html ingested: 2026-07-17 sha256: bb9fe3b52f2086b818e48f3b850dc35b767649473753b6ff92042fa40c179...
> **Sources:**
>   - upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-iii-2026-07-17.md
> **Links:**
- [[upgrading oracle e business suite r122 019]]
- [[upgrading oracle e business suite r122]]
- [[changing oracle applications user]]
- [[how to patch oracle database to 1931 on]]
- [[oracle database 26ai installation using]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_0156654061.html
ingested: 2026-07-17
sha256: bb9fe3b52f2086b818e48f3b850dc35b767649473753b6ff92042fa40c1793a6
blog_source: Oracle DBA Soyma
---
- 
- 
- 
- 
- 
- 
- 
Soumya's Database Blog : Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part III
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## May 24, 2026
### 
Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part III
  This post is continuation of the second part of the post : [Part II](https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01949795077.html)
**Applying
the Latest AD and TXK Release Update Packs to Oracle E-Business Suite Release
12.2 (Doc ID 1617461.1)**
 
Before applying the AD/TXK patches check following.
Login to DB,
check for optimizer_adaptive_features
 parameter, the output
should be false
SQL> show parameter
optimizer_adaptive_features 
NAME                                 TYPE        VALUE
------------------------------------
----------- ------------------------------
optimizer_adaptive_features          boolean     FALSE
SQL> alter system set
"_disable_actualization_for_grant" = true scope=both;
 
**Apply AD 16 Patches(36119925 , 36989014, 36303698  ):-**
Unzip  [Patch 36989014](https://support.oracle.com/epmos/faces/ui/patch/PatchDetail.jspx?parent=DOCUMENT&sourceId=1617461.1&patchId=36119925) (R12.AD.C)
[oraprod@testdb 12.1.0]$ cd
$ORACLE_HOME
[oraprod@testdb 12.1.0]$ cp -r
appsutil appsutil_bkp
Create $ORACLE_HOME/appsutil/admin on
database server if it doesn’t exist.
 
**Note: we applied adgrants.sql from
patch 36989014 while applied patch 36119925 because it had higher version of
adgrants.sql**
** **
**Copy the patches inside $PATCH_TOP**
[appltest@testapp scripts]$ cd
/apdata/patch/
[appltest@testapp patch]$ cp -r
36989014 36119925 36303698**  **$PATCH_TOP
 
 Compare version of adgrants.sql in
$APPL_TOP/admin to version in patch directory.
[oraprod@non-prod-db 36119925]$ cd
/apdata/erp/fs_ne/EBSapps/patch/36989014/admin
 
[oraprod@non-prod-db admin]$ cat
adgrants.sql | grep Header
REM $Header: adgrants.sql
120.67.12020000.140 2024/08/29 16:00:07 rsatyava ship $
 /* $Header: adgrants.sql 120.67.12020000.140
2024/08/29 16:00:07 rsatyava ship $ */
 /* $Header: adgrants.sql 120.67.12020000.140
2024/08/29 16:00:07 rsatyava ship $ */
 /* $Header: adgrants.sql 120.67.12020000.140
2024/08/29 16:00:07 rsatyava ship $ */
 /* $Header: adgrants.sql 120.67.12020000.140
2024/08/29 16:00:07 rsatyava ship $ */
 
 Copy whichever is the higher version of
adgrants.sql to $

## Summary

See Key Findings for full content.

## Related Articles

- [[upgrading oracle e business suite r122 019]]
- [[upgrading oracle e business suite r122]]
- [[changing oracle applications user]]
- [[how to patch oracle database to 1931 on]]
- [[oracle database 26ai installation using]]
