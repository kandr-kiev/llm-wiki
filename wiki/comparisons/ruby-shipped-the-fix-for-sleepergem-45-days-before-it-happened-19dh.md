---
title: "ruby shipped the fix for sleepergem 45 days before it happened 19dh"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - devops
  - image-generation
  - mobile
  - open-source
  - prompt-engineering
  - search
  - security
  - software
  - standards
  - video-generation
  - web
---
backlinks:
  - ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-19dh
---


# ruby shipped the fix for sleepergem 45 days before it happened 19dh

> **Source:** ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-2026-07-21.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: https://dev.to/svyatov/ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-19dh ingested: 2026-07-21 sha256: 8fe86baddec097c30605dea53ed02ecb5afc46a6358a171fb1d94673dbe64e03...
> **Sources:**
>   - ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-2026-07-21.md
> **Links:**
- [[its-ok-to-get-lucky-1laf]]
- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[the-part-of-this-year-i-dont-put-in-the-commit-messages-l6m]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[hollowtest-find-tests-that-pass-but-prove-nothing-2iii]]

## Key Findings

---
source_url: https://dev.to/svyatov/ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-19dh
ingested: 2026-07-21
sha256: 8fe86baddec097c30605dea53ed02ecb5afc46a6358a171fb1d94673dbe64e03
blog_source: Dev Community
---
Ruby shipped the fix for SleeperGem 45 days before it happened - DEV Community
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[Skip to content](#main-content)
Navigation menu
[
![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)
](/)
Search
[
Powered by Algolia
Search
](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)
[
Log in
](https://dev.to/enter?signup_subforem=1)
[
Create account
](https://dev.to/enter?signup_subforem=1&state=new-user)
## DEV Community
Close
![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
Add reaction
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
Like
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
Unicorn
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
Exploding Head
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
Raised Hands
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
Fire
Jump to Comments
Save
Boost
More...
Copy link
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
[Share Post via...](#)
[Report Abuse](/report-abuse)
[
![Cover image for Ruby shipped the fix for SleeperGem 45 days before it happened](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F4r40yhc2qj4wejzj1prj.png)
](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F4r40yhc2qj4wejzj1prj.png)
[![Leonid Svyatov](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F122709%2F4d89b6fb-d4ad-4af4-9c12-8cb53789179c.jpeg)](/svyatov)
[Leonid Svyatov](/svyatov)
Posted on Jul 21
# 
Ruby shipped the fix for SleeperGem 45 days before it happened
[#ruby](/t/ruby)
[#security](/t/security)
[#opensource](/t/opensource)
[#devops](/t/devops)
On June 3rd, Bundler 4.0.13 shipped [a feature called cooldown](https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html). The release post described the problem it solves like this: "an account is compromised, a malicious version ships, and any `bundle 

## Summary

install` in the minutes that follow resolves straight to it."
Forty-five days later, someone did exactly that to three gems.
[Aikido Security disclosed the campaign](https://www.aikido.dev/blog/sleepergem-rubygems-supply-chain-attack) on July 19th and named it SleeperGem: malicious versions of `git_credential_manager`, `Dendreo`, and `fastlane-plugin-run_tests_firebase_testlab`. Two of those gems had sat untouched since 2019 and 2020, which is where the name comes from. (The third impersonates Microsoft's Git Credential Manager, and no report says whether that account was hijacked or simply the attacker's.)
The clever part is what the payload does when it lands. Aikido found a `skip_install?` check that "scans for roughly 30 environment variables belonging to CI platforms, GitHub Actions, GitLab CI, CircleCI, Travis, Jenkins, Vercel, and does nothing if it spots one." It sits still in your pipeline and wakes up on your laptop. [StepSecurity reversed the native binary](https://www.stepsecurity.io/blog/sleepergem-compromised-rubygems-drop-persistent-backdoor) it drops: a daemon in `~/.local/share/gcm/`, a systemd user unit, a cron entry, and if you installed as root, a setuid shell at `/usr/local/sbin/ping6`.
Most of the coverage stopped at "supply chain attack, be careful out there," then repeated numbers that do not survive a look at the registry.
## 
The numbers being repeated are not the numbers
[The most-syndicated writeup](https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html) lists `Dendreo` versions 1.1.3 and 1.1.4 as "Published on October 14, 2017." The registry says 2017-10-14 is version **1.0.1**'s date, and that 1.1.2 shipped in October 2020. A 1.1.3 published three years before 1.1.2 is not a date, it is a copy-paste of the gem's first release. Same error on the fastlane plugin, where "February 06, 2018" belongs to 0.1.0. Both malicious releases went up in July 2026. That is the article the aggregators spent the next day copying.
The scale number has the same shape. Aikido's "574,661 total downloads" is honest in context (it says all versions), but downstream it sits next to the attack and reads like blast radius. Here is where they live:
`fastlane-plugin-run_tests_firebase_testlab`
published
downloads
0.3.1
2019-03-04
**531,859**
`################################`
0.2.0
2018-07-17
16,509
`#`
0.1.0
2018-02-06
10,619
`#`
0.2.2
2018-11-29
6,323
0.3.0
2019-01-11
4,965
0.2.1
2018-09-27
4,892
**0.3.2**
**2026-07-19**
yanked, count deleted
One benign release from 2019 is 92.5% of it. `Dendreo` has 14,435 downloads across its entire seven-year life. Nobody publishes install counts for the malicious versions, and they can't: yanking a version removes it from the API.
## 
The mitigation was already on the shelf
Cooldown makes Bundler refuse to resolve to a release younger than N days. The first malicious version went up on July 18th, and all of them were gone from the registry by the 21st. Nobody published the actual yank time,

## Related Articles

- [[its-ok-to-get-lucky-1laf]]
- [[i-tried-kimi-k3-for-a-week-heres-what-happened]]
- [[the-part-of-this-year-i-dont-put-in-the-commit-messages-l6m]]
- [[adding-an-ai-chatbot-to-echostats-290m]]
- [[hollowtest-find-tests-that-pass-but-prove-nothing-2iii]]
## Backlinks

```dataview
LIST FROM ""
WHERE contains(backlinks, "ruby-shipped-the-fix-for-sleepergem-45-days-before-it-happened-19dh")
```
