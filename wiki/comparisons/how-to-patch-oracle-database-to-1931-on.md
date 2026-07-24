---
title: "how to patch oracle database to 1931 on"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - async
  - data
  - guide
  - image-generation
  - vector-database
---

# how to patch oracle database to 1931 on

> **Source:** how-to-patch-oracle-database--to-1931-on-windows-step-by-step-guide-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/06/how-to-patch-oracle-database-to-1931-on.html ingested: 2026-07-17 sha256: 92a19efe3b7935f8f406e475bf887aec3e195943ffac1323a8515e7c88722c6e blog_s...
> **Sources:**
>   - how-to-patch-oracle-database--to-1931-on-windows-step-by-step-guide-2026-07-17.md
> **Links:**
- [[changing-oracle-applications-user]]
- [Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)
- [[5-agent-skills-i-use-every-day]]
- [[cloudflare-workers-ai-rest-api-2026]]
- [[rust-1960]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/06/how-to-patch-oracle-database-to-1931-on.html
ingested: 2026-07-17
sha256: 92a19efe3b7935f8f406e475bf887aec3e195943ffac1323a8515e7c88722c6e
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
Soumya's Database Blog : How to Patch Oracle Database to 19.31 on Windows: Step-by-Step Guide
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## June 4, 2026
### 
How to Patch Oracle Database to 19.31 on Windows: Step-by-Step Guide
 
[![](https://blogger.googleusercontent.com/img/a/AVvXsEhzievA6KA9xwrLiOQmYW0ColGM9vzDBGrkBLwKdOh9gyQHQPrEK3mhG4gGXpalnD1HohRgqcOLqfbY7GxkJQK6vpIEP6-qqZHEu6m0MY_Ij0SixQhzuPotATVZy0fim5JJy9OV9eRI8VBjS7nzqgFYoiaaKJz5iEoQXS9LJCYG20sJO39kzE4eni90Lzo=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEhzievA6KA9xwrLiOQmYW0ColGM9vzDBGrkBLwKdOh9gyQHQPrEK3mhG4gGXpalnD1HohRgqcOLqfbY7GxkJQK6vpIEP6-qqZHEu6m0MY_Ij0SixQhzuPotATVZy0fim5JJy9OV9eRI8VBjS7nzqgFYoiaaKJz5iEoQXS9LJCYG20sJO39kzE4eni90Lzo)
In this article, I'll walk you through the steps I used to
patch an Oracle Database 19c environment from version 19.29 to 19.31 following
Oracle's April 2026 Quarterly Release Update.
Quarterly patching is a regular responsibility for Oracle
DBAs, and while the version numbers may change, the underlying process remains
largely consistent across Oracle 19c Release Updates. This guide is intended to
serve as a practical reference that you can use during your own patching
activities.
**Note:** Never apply a patch directly to a Production
environment without first validating it in Development or Test. Thorough
testing helps identify potential issues before they impact business-critical
systems.
**Requirements**
Before proceeding, ensure that the following prerequisites
are met:
- Oracle
Database 19c (Windows x86-64)
- Active
My Oracle Support (MOS) account
- Appropriate
access to ORACLE_HOME and ORACLE_BASE directories
- Minimum
12 GB free disk space in Oracle Home
- WinSCP
or equivalent file transfer utility
- Scheduled
maintenance window and approved downtime
 
**Step 1: Download the Patch and OPatch Utility**
Log in to [Oracle
Support](https://support.oracle.com/) and download the following:
- Patch
file: **38818049** → p38818049_190000_MSWIN-x86-64.zip
- OPatch
utility: **6880880** → p6880880_190000_MSWIN -x86-64.zip
Steps to download: Select *Patches & Updates* →
enter patch number → select platform *Windows x86-64* → download
both files and review the README.
 
**Step 2: Check and Update OPatch**
On the server, check your current OPatch version:
cd
%ORACLE_HOME%/OPatch
opatch
version
 
 
You need version **12.2.0.1.48 or higher**. If

## Summary

 it's
older, update it:
cd
%ORACLE_HOME%
ren OPatch
OPatch_backup1
robocopy
p6880880_190000_MSWIN -x86-64.zip   %ORACLE_HOME%
cd
%ORACLE_HOME%
unzip
p6880880_190000_MSWIN -x86-64.zip
 
 
**Step 3: Run Pre-checks**
Before applying the patch, check for conflicts with existing
patches:
 
C:\Users\Administrator>cd
C:\software\oracle_patch_19.31\38818049
 
C:\software\oracle_patch_19.31\38818049>D:\oracle\product\19.3.0\dbhome_1\OPatch\opatch
prereq CheckConflictAgainstOHWithDetail -ph ./
Oracle
Interim Patch Installer version 12.2.0.1.51
Copyright (c)
2026, Oracle Corporation.  All rights reserved.
 
PREREQ
session
 
Oracle
Home       :
D:\oracle\product\19.3.0\dbhome_1
Central
Inventory : C:\Program Files\Oracle\Inventory
   from           :
OPatch
version    : 12.2.0.1.51
OUI
version       : 12.2.0.7.0
Log file
location : D:\oracle\product\19.3.0\dbhome_1\cfgtoollogs\opatch\opatch2026-06-06_19-40-37PM_1.log
 
Invoking
prereq "checkconflictagainstohwithdetail"
 
Prereq
"checkConflictAgainstOHWithDetail" passed.
 
OPatch
succeeded.
 
 
As we see "OPatch succeeded", we are good to
go. If there are conflicts, resolve them before proceeding.
**Step 4: Stop the Database and Listener**
sqlplus / as
sysdba
 
SQL>
shutdown immediate
SQL> exit
 
lsnrctl stop
 
 
Verify all services are completely down before moving to the
next step.
**Step 5: Clean Up Inactive Patches (Optional but
Recommended)**
This frees up Oracle Home space before applying the new
patch:
cd
%ORACLE_HOME%/OPatch
 
./opatch util
listOrderedInactivePatches
 
./opatch util
deleteInactivePatches
 
 
**Step 6: Check Available Disk Space**
Do not proceed if space is insufficient in oracle home
**Step 7: Apply the Patch**
C:\Software\oracle_patch_19.31\38818049>D:\oracle\product\19.3.0\dbhome_1\OPatch\opatch
apply
Oracle
Interim Patch Installer version 12.2.0.1.51
Copyright (c)
2026, Oracle Corporation.  All rights
reserved.
 
 
Oracle
Home       :
D:\oracle\product\19.3.0\dbhome_1
Central
Inventory : C:\Program Files\Oracle\Inventory
   from           :
OPatch
version    : 12.2.0.1.51
OUI
version       : 12.2.0.7.0
Log file
location :
D:\oracle\product\19.3.0\dbhome_1\cfgtoollogs\opatch\opatch2026-06-04_06-01-03AM_1.log
 
Verifying
environment and performing prerequisite checks...
 
--------------------------------------------------------------------------------
Start OOP by
Prereq process.
Launch OOP...
 
Oracle
Interim Patch Installer version 12.2.0.1.51
Copyright (c)
2026, Oracle Corporation.  All rights
reserved.
 
 
Oracle
Home       :
D:\oracle\product\19.3.0\dbhome_1
Central
Inventory : C:\Program Files\Oracle\Inventory
   from           :
OPatch
version    : 12.2.0.1.51
OUI
version       : 12.2.0.7.0
Log file
location :
D:\oracle\product\19.3.0\dbhome_1\cfgtoollogs\opatch\opatch2026-06-04_06-04-26AM_1.log
 
Verifying
environment and performing prerequisite checks...
OPatch
continues with these patches:  
38818049
 
Do you want
to proceed? [y|n]
y
User
Responded with: Y
All checks
passed

## Related Articl[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)[Issue #8330: Dataset Studio and Viewer down]]
- [[5-agent-skills-i-use-every-day]]
- [[cloudflare-workers-ai-rest-api-2026]]
- [[rust-1960]]
