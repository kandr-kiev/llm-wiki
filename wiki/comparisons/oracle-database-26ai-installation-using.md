---
title: "oracle database 26ai installation using"
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

# oracle database 26ai installation using

> **Source:** oracle-database-26ai-installation-using-rpm-on-oracle-linux-9-oel-9--step-by-step-guide-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/06/oracle-database-26ai-installation-using.html ingested: 2026-07-17 sha256: 819a5e46832819544cfcb21939caf34b5a75ea6dc8c88dd894f9e5b80952c97f blog_s...
> **Sources:**
>   - oracle-database-26ai-installation-using-rpm-on-oracle-linux-9-oel-9--step-by-step-guide-2026-07-17.md
> **Links:**
- [[how to patch oracle database to 1931 on]]
- [[changing oracle applications user]]
- [[sequoia ascent]]
- [[v0.27.0]]
- [Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/06/oracle-database-26ai-installation-using.html
ingested: 2026-07-17
sha256: 819a5e46832819544cfcb21939caf34b5a75ea6dc8c88dd894f9e5b80952c97f
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
Soumya's Database Blog : Oracle Database 26ai Installation Using RPM on Oracle Linux 9 (OEL 9) – Step-by-Step Guide
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## June 6, 2026
### 
Oracle Database 26ai Installation Using RPM on Oracle Linux 9 (OEL 9) – Step-by-Step Guide
 
[![](https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc=w640-h430)](https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc)
In this post I will describe the installation of Oracle
Database 26ai 64-bit on Oracle Linux 9 (OL8) 64-bit. The installation requires
a minimum of 2g swap memory and secure Linux set to permissive or disabled.
Add hosts entry in hosts file
[root@dbvm-1 opc]# cat
/etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4
localhost4.localdomain4
::1         localhost localhost.localdomain
localhost6 localhost6.localdomain6
10.0.0.45
dbvm-1.subnet09221504.vcn09221504.oraclevcn.com dbvm-1
Download
the RPM for oracle installation:-
The
required rpm can be downloaded directly from oracle website 
[https://www.oracle.com/database/free/get-started/](https://www.oracle.com/database/free/get-started/)
[![](https://blogger.googleusercontent.com/img/a/AVvXsEim3jWAnPEZPILB5IVGTgd73dhwXODRUGM1Jgde3VawGCZb7PT8TWBCs-Iur5xdJ9FRqNseY12Adzbd6T7V_MVNYlG2nipcWtDEY4Ry3dp5WwxJNllbZSvnZeCDyLQjUWQI-U6vjiZQCsGemodL3So2mOqZsVMKq-_l4UaG2B8FTEEyuWgrWQQh89IUZl8=w640-h264)](https://blogger.googleusercontent.com/img/a/AVvXsEim3jWAnPEZPILB5IVGTgd73dhwXODRUGM1Jgde3VawGCZb7PT8TWBCs-Iur5xdJ9FRqNseY12Adzbd6T7V_MVNYlG2nipcWtDEY4Ry3dp5WwxJNllbZSvnZeCDyLQjUWQI-U6vjiZQCsGemodL3So2mOqZsVMKq-_l4UaG2B8FTEEyuWgrWQQh89IUZl8)
Rpm url : [oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm](https://yum.oracle.com/repo/OracleLinux/OL9/appstream/aarch64/getPackage/oracle-ai-database-preinstall-26ai-1.0-2.el9.aarch64.rpm)
Download
the rpm as root user
[root@dbvm-1 opc]# wget https://yum.oracle.com/repo/OracleLinux/OL9/appstream/x86_64/getPackage/oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm
 
[root@dbvm-1 opc]# **dnf inst

## Summary

all
-y oracle-ai-database-preinstall-26ai**
 
Last metadata expiration check:
0:04:32 ago on Sat 06 Jun 2026 06:11:34 AM GMT.
Dependencies resolved.
==============================================================================================================================================================================================
 Package                                                        
Architecture                       
Version                                
Repository                                  Size
==============================================================================================================================================================================================
Installing:
 oracle-ai-database-preinstall-26ai                              x86_64                              1.0-1.el9                              
ol9_appstream                               34 k
 
Transaction Summary
==============================================================================================================================================================================================
Install  1 Package
 
Total download size: 34 k
Installed size: 81 k
Downloading Packages:
oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm                                                                                                      
416 kB/s |  34 kB     00:00
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                        
407 kB/s |  34 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
 
Preparing        :                                                                                                                                                                     
1/1
 
Installing       :
oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64                                                                                                                 
1/1
 
Running scriptlet:
oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64                                                                                                                 
1/1
 
Verifying        :
oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64                                                                                                                 
1/1
 
Installed:
 
oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64
 
Complete! [root@dbvm-1 opc]# **dnf
install -y oracle-ai-database-preinstall-26ai**
 
Last metadata expiration check:
0:04:32 ago on Sat 06 Jun 2026 06:11:34 AM GMT.
Dependencies resolved.
==================================================================

## Related Articles

- [[how to patch oracle database to 1931 on]]
- [[changing oracle application[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)[Issue #8330: Dataset Studio and Viewer down]]
