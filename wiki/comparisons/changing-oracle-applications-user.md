---
title: "changing oracle applications user"
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

# changing oracle applications user

> **Source:** changing-oracle-applications-user-password-using-fndcpass--step-by-step-guide-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://dbasoumya.blogspot.com/2026/05/changing-oracle-applications-user.html ingested: 2026-07-17 sha256: 0bc5c5f22e03cd6a667b928406a2f61723c8627bfef64ab8e5193a5d9c055161 blog_source:...
> **Sources:**
>   - changing-oracle-applications-user-password-using-fndcpass--step-by-step-guide-2026-07-17.md
> **Links:**
- [[Rust 1.96.0]]
- [[Rust 1.97.1]]
- [Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)
- [[REST API]]
- [[Rust 1.97.0]]

## Key Findings

---
source_url: https://dbasoumya.blogspot.com/2026/05/changing-oracle-applications-user.html
ingested: 2026-07-17
sha256: 0bc5c5f22e03cd6a667b928406a2f61723c8627bfef64ab8e5193a5d9c055161
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
Soumya's Database Blog : Changing Oracle Applications User Password Using FNDCPASS – Step-by-Step Guide
- 
- - 
# 
Soumya's Database Blog 
Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.
## May 23, 2026
### 
Changing Oracle Applications User Password Using FNDCPASS – Step-by-Step Guide
As an oracle apps dba , we often need to reset password for
apps user in E-Business suite . FNDCPASS is an Oracle E-Business Suite utility
used to change application user passwords, Oracle schema passwords, and
APPS/APPLSYS passwords while keeping Oracle EBS metadata synchronized.      
 
Steps to change:-
1.      First ensure application is not running or shutdown
application by
Invoke application environment from run file
system
[oracle@ebstest
VIS]$ cd /u01/oracle/VIS/fs1/EBSapps/appl
[oracle@ebstest
VIS]$ . APPSVIS_ebstest.env
[oracle@ebstest
sql]$ cd $ADMIN_SCRIPTS_HOME
[oracle@ebstest
sql]$  ./adstpall.sh 
1.     
Change the APPLSYS password using
Syntax:- FNDCPASS apps/<appspwd> 0 Y
system/<system_manager> SYSTEM APPLSYS <new_apps_passwd>
 
[oracle@ebstest sql]$  FNDCPASS apps/apps 0 Y system/manager SYSTEM
APPLSYS apps123#
 
1.     
Run autoconfig on appstier
[oracle@ebstest VIS]$ cd
/u01/oracle/VIS/fs1/EBSapps/appl
[oracle@ebstest VIS]$ . APPSVIS_ebstest.env
[oracle@ebstest scripts]$ cd $ADMIN_SCRIPTS_HOME
[oracle@ebstest scripts]$ adautocfg.sh
……
……
AutoConfig completed successfully
 
1.     
Now start weblogic admin server using following
script
[oracle@ebstest
scripts]$ pwd
/u01/oracle/VIS/fs1/inst/apps/VIS_ebstest/admin/scripts 
[oracle@ebstest
scripts]$ sh adadminsrvctl.sh start
You are
running adadminsrvctl.sh version 120.10.12020000.2
 Enter
the WebLogic Admin password:
Enter
the APPS Schema password:
 
Confirm
the admin server running status. Don’t start any other application services.
[oracle@ebstest
scripts]$ sh adadminsrvctl.sh status 
You are
running adadminsrvctl.sh version 120.10.12020000.2
 Enter
the WebLogic Admin password:
Enter
the APPS Schema password:
  The
AdminServer is running 
adadminsrvctl.sh:
exiting with status 0
 adadminsrvctl.sh:
check the logfile
/u01/oracle/VIS/fs1/inst/apps/VIS_ebstest/logs/appl/admin/log/adadminsrvctl.txt
for more information ...
 
1.     
Now login to weblogic console from browser
[![](https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tU

## Summary

hvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U=w640-h342)](https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U)
Click on Lock and Edit button
[![](https://blogger.googleusercontent.com/img/a/AVvXsEht8CNCScfwH6uN_CJIEOMBcIOfsuyiHuV9AB4Ce0iVi-MEwFaYDTlsDSPQg0QFnQgqzgva28O99HMsW0IoKWA25P6zsXwPD8ijslfwvdvlih2klcVMojNqE16UU0b6hw7IfqQYzNqOWEfcMCqMiZVcQ-9IsZxEvpa6XZQoIcnCp7K8j1SavG6wuYmd7e4=w640-h230)](https://blogger.googleusercontent.com/img/a/AVvXsEht8CNCScfwH6uN_CJIEOMBcIOfsuyiHuV9AB4Ce0iVi-MEwFaYDTlsDSPQg0QFnQgqzgva28O99HMsW0IoKWA25P6zsXwPD8ijslfwvdvlih2klcVMojNqE16UU0b6hw7IfqQYzNqOWEfcMCqMiZVcQ-9IsZxEvpa6XZQoIcnCp7K8j1SavG6wuYmd7e4)
Now under Domain structure, click
on services - > Data Sources
[![](https://blogger.googleusercontent.com/img/a/AVvXsEgnwqxgVpRg-VGuDbJec3VBsEQrb9Eei-c7BWKLwOEFpPpgCLRSk1yooWzibpy9zhfBjPRAEsRCmv_r7O8zTHsrFI3_Wr-bEtka6NAgiDTQxeaXL4FoxhtWZVy8XyC_TuYuBLS5DuASvkldOctrmlkh3C1j7gl1Wtg9gyxfJiaG1qpP2OrxdSCJRwLaj4Y=w640-h438)](https://blogger.googleusercontent.com/img/a/AVvXsEgnwqxgVpRg-VGuDbJec3VBsEQrb9Eei-c7BWKLwOEFpPpgCLRSk1yooWzibpy9zhfBjPRAEsRCmv_r7O8zTHsrFI3_Wr-bEtka6NAgiDTQxeaXL4FoxhtWZVy8XyC_TuYuBLS5DuASvkldOctrmlkh3C1j7gl1Wtg9gyxfJiaG1qpP2OrxdSCJRwLaj4Y)
Now click on “EBSDataSource”
[![](https://blogger.googleusercontent.com/img/a/AVvXsEgWDqIVj6UxRUvoNniKdoeX4XSR_-yWpqB2LkbpUK0rW90eQCBoUwGjbk5IiBO8yseTJ5hTClhdQC5CyXJqZwfQRapESe3uGGt8FVlg0QRodBxvtfonly6M9a3DtEXeXWxXaH-HK-vnDYrf5sUa50pi_ncIOI2TmmcUo_UubOM6pmLVh446i9aNcLBN2UI=w640-h210)](https://blogger.googleusercontent.com/img/a/AVvXsEgWDqIVj6UxRUvoNniKdoeX4XSR_-yWpqB2LkbpUK0rW90eQCBoUwGjbk5IiBO8yseTJ5hTClhdQC5CyXJqZwfQRapESe3uGGt8FVlg0QRodBxvtfonly6M9a3DtEXeXWxXaH-HK-vnDYrf5sUa50pi_ncIOI2TmmcUo_UubOM6pmLVh446i9aNcLBN2UI)
Now on the page of “Settings of
EBSDataSoure” click on connection pool and  provide the changed apps
password and save it.
[![](https://blogger.googleusercontent.com/img/a/AVvXsEigOz7xHJO1cdevhWNOPd17z89usksj6DaSVHjWV77y4O4o8z_tNjygH032z2LAHgE2CcYKnMgqvcZ7T_emKVfPRulF5qmQ-zKqsANYgFh6SSwnCYBDIb-XokDXVlphRZ7ZpE4Tf_wBQ2oBa_NaT-6Ak-j6p-eUmSzVMAK8nKp_npbJEiNyzRruuQaEm48=w640-h414)](https://blogger.googleusercontent.com/img/a/AVvXsEigOz7xHJO1cdevhWNOPd17z89usksj6DaSVHjWV77y4O4o8z_tNjygH032z2LAHgE2CcYKnMgqvcZ7T_emKVfPRulF5qmQ-zKqsANYgFh6SSwnCYBDIb-XokDXVlphRZ7ZpE4Tf_wBQ2oBa_NaT-6Ak-j6p-eUmSzVMAK8nKp_npbJEiNyzRruuQaEm48)
Click on Activate changes.
[![](https://blogger.googleusercontent.com/img/a/AVvXsEg1z7yoQ2YbweROld9-_GzMwhmqf7HSqnfCmW6fvjqTgKP6tYDyzFAMSnNG5Is4daNDFfUc1ULs0LZa1tDLWL3eT-khQfM2B8Be7BSt_ZxWggp3O6cvXrTNVFlGUz4XyMTV_HTQFwPLUbqlqU09ADp8I-SYG5WGdm1D2xRxgvs1Cvn6zroDHi9DKOwMQs4=w640-h444)](https://blogger.googleusercontent.com/img/a/AVvXsEg1z7yoQ2YbweROld9-_GzMwhmqf7HSqnfCmW6fvjqTgKP6tYDyzFAMSnNG5Is4daNDFfUc1ULs0LZa1tDLWL3eT-khQfM2B8Be7BSt_ZxW

## Related Ar[Issue #8330: Dataset Studio and Viewer down](https://github.com/pytorch/pytorch/issues/8330)[Issue #8330: Dataset Studio and Viewer down]]
- [[REST API]]
- [[Rust 1.97.0]]
