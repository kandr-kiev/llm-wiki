---
title: "upgrading oracle e business suite r122 016"
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

# upgrading oracle e business suite r122 016

> **Source:** upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-vi-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01681079011.html ingested: 2026-07-17 sha256: 5e02784a19990f6252927f37f88620e3114cc4361adf16aff0a7500aeac5...
> **Sources:**
>   - upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-vi-2026-07-17.md
> **Links:**
- [[upgrading oracle e business suite r122 014]]
- [[upgrading oracle e business suite r122 01]]
- [[upgrading oracle e business suite r122 019]]
- [[upgrading oracle e business suite r122]]
- [[changing oracle applications user]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01681079011.html
ingested: 2026-07-17
sha256: 5e02784a19990f6252927f37f88620e3114cc4361adf16aff0a7500aeac52b8c
blog_source: Oracle DBA Soyma
---
- 
- 
- 
- 
- 
- 
- 
Soumya's Database Blog : Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part VI
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## May 25, 2026
### 
Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part VI
  This post is continuation of the fifth part of the post : [Part V](https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01453238672.html)
Apply datapatch
 
[oraprod@non-prod-db ~]$ 19cdb_env
[oraprod@non-prod-db 19.3.0]$ export
ORACLE_SID=EBS
[oraprod@non-prod-db 19.3.0]$ sqlplus
/ as sysdba
SQL> select open_mode from
v$database;
 
OPEN_MODE
--------------------
READ WRITE
 
SQL> select description, action,
to_char(action_time,'DD/MM/RR HH24:MI:SS') action_date, ' ' version from
dba_registry_sqlpatch;
 
DESCRIPTION                                                                                         
ACTION          ACTION_DATE       V
----------------------------------------------------------------------------------------------------
--------------- ----------------- -
Database Release Update :
19.27.0.0.250415 (37642901)                                               
APPLY           02/06/25
19:10:06
SQL>exit
 
[oraprod@non-prod-db ~]$ **datapatch
-verbose**
SQL Patching tool version 19.27.0.0.0
Production on Tue Jun  3 11:30:57 2025
Copyright (c) 2012, 2025,
Oracle.  All rights reserved.
 
Log file for this invocation:
/dbdata/erp/cfgtoollogs/sqlpatch/sqlpatch_27077_2025_06_03_11_30_57/sqlpatch_invocation.log
 
Connecting to database...OK
Gathering database info...done
Bootstrapping registry and package to
current versions...done
Determining current state...done
 
Current state of interim SQL patches:
 
No interim patches found
 
Current state of release update SQL
patches:
 
Binary registry:
   
19.27.0.0.0 Release_Update 250406131139: Installed
 
SQL registry:
   
Applied 19.27.0.0.0 Release_Update 250406131139 successfully on
02-JUN-25 07.10.06.159334 PM
 
Adding patches to installation queue
and performing prereq checks...done
Installation queue:
 
No interim patches need to be rolled back
 
No release update patches need to be installed
 
No interim patches need to be applied
Change compatible parameter.Before changing we need to drop
the restore points.
SQL> drop restore point
pre_upgrade; 
Restore point dropped.
 SQL> alter system set
compatible='19.0.0' sco

## Summary

See Key Findings for full content.

## Related Articles

- [[upgrading oracle e business suite r122 014]]
- [[upgrading oracle e business suite r122 01]]
- [[upgrading oracle e business suite r122 019]]
- [[upgrading oracle e business suite r122]]
- [[changing oracle applications user]]
