---
title: "Step 2: Create the virtual ethernet cable (veth pair)"
type: concept
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - gpt
  - kubernetes
  - news
  - search
---

# Step 2: Create the virtual ethernet cable (veth pair)

> **Source:** how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand-2026-07-23.md
> **Type:** concept
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/ ingested: 2026-07-23 sha256: 16069428789f727cd7008e8bac44ef97ad57e...
> **Sources:**
>   - how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand-2026-07-23.md
> **Links:**
- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[i started a dirt notebook]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[the great software regress how move fast and break things broke our lives]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-build-kubernetes-networking-without-kubernetes-do-what-the-cni-does-by-hand/
ingested: 2026-07-23
sha256: 16069428789f727cd7008e8bac44ef97ad57e50cd1c78a65b99fe40c69616195
blog_source: FreeCodeCamp Blog
---
How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand
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
- 
- 
- 
[![freeCodeCamp.org](https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg)](https://www.freecodecamp.org/news/)
- 
English
- 
Español
- 
中文（简体字）
- 
Italiano
- 
Português
- 
Українська
- 
日本語
- 
한국어
Menu
- 
- Forum
- Curriculum
- 
Night Mode
Donate
July 22, 2026
/
#Kubernetes
# How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand
![Shubham Katara](https://cdn.hashnode.com/res/hashnode/image/upload/v1675689472065/wxn78xg7Q.jfif)
[
Shubham Katara
](/news/author/katara/)
![How to Build Kubernetes Networking Without Kubernetes: Do What the CNI Does By Hand](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/8fc3683f-15c8-45ff-8424-bb1b427f68e2.png)
In this article, you'll build an accurate mental model of what a Container Network Interface (CNI) actually does. Not by reading YAML, but by doing every single step it does by hand with raw Linux kernel primitives.
The Container Network Interface (CNI) is one of the great black boxes of Kubernetes. Most people who run clusters every day have never once looked inside it. They know the *name* of their CNI ("we run Calico," "we're on Cilium") the way you know the brand of the alternator in your car: as a label, not as a thing you actually understand.
It lives at the very bottom of the stack, beneath the kubelet, beneath your pods, quietly moving every single packet. And precisely because it never fails loudly on a good day, almost nobody learns what it does.
We won't run `helm install cilium`. We won't apply a single manifest. Instead, we'll wire up pod networking from scratch, feel exactly where it breaks the moment traffic tries to leave a physical machine, and fix it manually.
By the end, you'll understand it in your bones, not just in theory, why tools like Cilium exist and what they're really solving under the hood.
**Who this is for:**
- Developers, platform engineers, and SREs who use Kubernetes every day but quietly treat pod-to-pod networking as magic.
- Anyone who has ever watched a pod flip to `Running` and assumed the network "just works" and wants to know what's actually happening.
**What you'll build with your own hands:**
- Two isolated network namespaces wired together with a virtual cable (`veth` pair).
- A three-namespace virtual switch using a Linux bridge, the same trick legacy CNIs use on a single node.
- A deliberately broken two-node setup where a packet gets dropped on the floor, plus the manual fix that makes it work.
- A clear picture of the three jobs every CNI does, and why cloud providers force advanced CNIs like Cilium to use ov

## Summary

erlays and eBPF.
**Note:** Every command here needs a Linux host and `root`. Run this in a throwaway VM or lab environment, not on anything you care about. The whole point is to make a mess and learn from it.
## Table of Contents
- [Prerequisites](#heading-prerequisites)
- [The Illusion: Kubernetes Routes Zero Packets](#heading-the-illusion-kubernetes-routes-zero-packets)
- [The Foundation: Virtual Ethernet (veth) Pairs](#heading-the-foundation-virtual-ethernet-veth-pairs)
- [How to Scale Locally with a Linux Bridge](#heading-how-to-scale-locally-with-a-linux-bridge)
- [The Multi-Node Boundary Problem](#heading-the-multi-node-boundary-problem)
- [How to Fix It Manually with Direct Routing](#heading-how-to-fix-it-manually-with-direct-routing)
- [So What Is a CNI, Really?](#heading-so-what-is-a-cni-really)
- [The Cloud Catch and Why Cilium Changes the Game](#heading-the-cloud-catch-and-why-cilium-changes-the-game)
- [Conclusion](#heading-conclusion)
## Prerequisites
Before following along, you'll need:
- Two Linux VMs on the same network for the multi-node section so you can watch traffic cross a real machine boundary.
- The `ip` command from the `iproute2` package (already installed on virtually every modern distro).
- A basic comfort with IP addresses, subnets, and the word "gateway." You don't need to be a network engineer.
- **No Kubernetes.** That's not a typo. We're going underneath Kubernetes on purpose.
## The Illusion: Kubernetes Routes Zero Packets
Here's the uncomfortable truth most people never confront: **Kubernetes can't route a single network packet.**
Not one. Kubernetes is a orchestrator. It schedules pods, watches their health, and updates state in etcd. But when it comes to actually moving a packet from one container to another, it has zero built-in capability. None.
So how do your pods talk to each other? They rely completely on an external agent to wire up the virtual network plumbing on every node. That agent is the **Container Network Interface (CNI)**. What the CNI does under the hood quietly, is what we would do ourselves to feel the pain and then the solution a CNI provides.
Here's the proof that it's load-bearing. Spin up a brand-new cluster with `kubeadm` and look at your nodes:
```
$ kubectl get nodes
NAME STATUS ROLES AGE VERSION INTERNAL-IP EXTERNAL-IP OS-IMAGE KERNEL-VERSION CONTAINER-RUNTIME
no-cni NotReady control-plane,master 52s v1.35.0 192.168.117.2 <none> Ubuntu 24.04.3 LTS 7.0.11-orbstack-00360-gc9bc4d96ac70 containerd://2.1.6
worker-1 NotReady <none> 46s v1.35.0 192.168.117.3 <none> Ubuntu 24.04.3 LTS 7.0.11-orbstack-00360-gc9bc4d96ac70 containerd://2.1.6
worker-2 NotReady <none> 40s v1.35.0 192.168.117.4 <none> Ubuntu 24.04.3 LTS 7.0.11-orbstack-00360-gc9bc4d96ac70 containerd://2.1.6
```
`NotReady`. Every node. The control plane is healthy, etcd is up, the scheduler is alive, and the cluster still flatly refuses to be `Ready`. If you describe the node, it tells you precisely what's missing:
```
Conditions:
T

## Related Articles

- [[Automating Ai Away]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[i started a dirt notebook]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[the great software regress how move fast and break things broke our lives]]
