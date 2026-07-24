---
title: "upgrading oracle e business suite r122"
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

# upgrading oracle e business suite r122

> **Source:** upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-i-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122.html ingested: 2026-07-17 sha256: 6e174fbf98c652185a714949dcf618143f17feb494e741716ec13c2a3b9aa10e blog_so...
> **Sources:**
>   - upgrading-oracle-e-business-suite-r122-database-from-12102-to-19c---part-i-2026-07-17.md
> **Links:**
- [[changing-oracle-applications-user]]
- [[how-to-patch-oracle-database-to-1931-on]]
- [[oracle-database-26ai-installation-using]]
- [[sequoia-ascent]]
- [[rust-1960]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122.html
ingested: 2026-07-17
sha256: 6e174fbf98c652185a714949dcf618143f17feb494e741716ec13c2a3b9aa10e
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
Soumya's Database Blog : Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part I
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## May 23, 2026
### 
Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part I
Source
Environment(12c)
Orace Database Version
12.1.0.2
E Business Suite Version
R12.2.5
Database Home path
/dbdata/erp/12.1.0
Application base
/apdata/erp/fs2/EBSapps
 
Target
Environment(19c)
Orace Database Version
19.27
E Business Suite Version
R12.2.5
Database Home path
/dbdata/erp/19.3.0
Application base
/apdata/erp/fs2/EBSapps
This is running on OEL 7.9
Reference DOC ID: **2552181.1**
Important Information Regarding the Upgrade to Oracle Database 19c :-
-          When
upgrading your Oracle E-Business Suite to Oracle Database 19c, your database
will be converted to the multitenant architecture, with a Container Database
(CDB) and a single Pluggable Database. Only multitenant architecture databases
are certified for Oracle E-Business Suite with Oracle Database 19c.
-          During
the upgrade, you will also perform steps to migrate directories defined for
PL/SQL File I/O to database directory objects. This requirement is due to the
desupport in Oracle Database 19c of the UTL_FILE_DIR database initialization
parameter.
-          Oracle
19c Database Release Update Information for Oracle E-Business Suite:
Oracle
Database Release Update 19.3 as well as Release Update 19.5 and later are
certified.
Oracle
recommends that you upgrade to the latest Oracle Database Release Update that
is certified with Oracle E-Business Suite. Applying the latest Release Update
will ensure that you have the security-related fixes and high-priority
non-security fixes. See My Oracle Support Knowledge Document 2285040.1, Release
Update Introduction and FAQ, for more details.
-          You can
upgrade directly from an earlier Oracle Database version to either:
-          Oracle
Database 19c Release Update 19.3
-       Oracle Database 19c
Release Update 19.6 or a later Oracle E-Business Suite certified RU
-       You can upgrade to
Oracle Database 19c Release Update 19.5 indirectly
- 
<span style="font-

## Summary

See Key Findings for full content.

## Related Articles

- [[changing-oracle-applications-user]]
- [[how-to-patch-oracle-database-to-1931-on]]
- [[oracle-database-26ai-installation-using]]
- [[sequoia-ascent]]
- [[rust-1960]]
