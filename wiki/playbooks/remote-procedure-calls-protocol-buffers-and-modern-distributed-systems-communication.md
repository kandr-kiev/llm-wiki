---
title: "remote procedure calls protocol buffers and modern distributed systems communication"
type: playbook
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - distributed
  - edge
  - gpt
  - news
  - search
---

# remote procedure calls protocol buffers and modern distributed systems communication

> **Source:** from-rpc-to-grpc-understanding-remote-procedure-calls-protocol-buffers-and-modern-distributed-system-2026-07-23.md
> **Type:** playbook
> **Created:** 2026-07-23
> **Updated:** 2026-07-23
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/ ingested: 2026-07-23 sha256: ee71747c1b9423d97765531fd19364c16ea...
> **Sources:**
>   - from-rpc-to-grpc-understanding-remote-procedure-calls-protocol-buffers-and-modern-distributed-system-2026-07-23.md
> **Links:**
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[Automating Ai Away]]
- [[5 Agent Skills I Use Every Day]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/remote-procedure-calls-protocol-buffers-and-modern-distributed-systems-communication/
ingested: 2026-07-23
sha256: ee71747c1b9423d97765531fd19364c16ea875b9d668799591a4e48c48483e0f
blog_source: FreeCodeCamp Blog
---
From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication 
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
#gRPC
# From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication 
![Oluwaseyi Fatunmole](https://cdn.hashnode.com/uploads/avatars/692776609bbf6fdcde84192d/71ac313f-d9ed-4c0c-8990-e1b362645ecc.png)
[
Oluwaseyi Fatunmole
](/news/author/foluwaseyi/)
![From RPC to gRPC: Understanding Remote Procedure Calls, Protocol Buffers, and Modern Distributed Systems Communication ](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/1205581e-5729-44fa-837e-0f30981ea059.png)
Every application, at some point, needs to talk to another system. A mobile app talks to a backend. A backend service talks to a payment gateway. An authentication service talks to a user service. A data pipeline talks to a storage layer.
The question is never whether systems need to communicate. The question is always how.
For years, REST over HTTP with JSON was the default answer. It works, it's simple, and the tooling is everywhere. But as systems grow in scale (in the number of services talking to each other, the volume of data being exchanged, and the need for real-time communication), REST starts to show its limits.
This is where Remote Procedure Calls, Protocol Buffers, and gRPC enter the picture.
In this handbook, you'll learn what RPC is and the problem it was designed to solve. You'll also understand Protocol Buffers: what they are, why they exist, and how they work.
You'll then see how Google combined these ideas into gRPC, one of the most powerful communication frameworks in modern distributed systems. You'll learn all four gRPC communication patterns, see code generated across multiple languages from a single contract file, and walk through a complete end-to-end Flutter implementation with production-grade concerns including authentication, error handling, and timeouts.
By the end, you won't just know what gRPC is. You'll understand when to use it, when not to, and how to think about service communication as a systems engineer.
## Table of Contents
- [What is a Remote Procedure Call](#heading-what-is-a-remote-procedure-call)?
- [The Problem RPC Solves](#heading-the-problem-rpc-solves)
- [Why gRPC Over REST: The Real Case](#heading-why-grpc-over-rest-the-real-case)
- [Protocol Buffers: A New Language fo

## Summary

r Data](#heading-protocol-buffers-a-new-language-for-data)
- [The Proto File](#heading-the-proto-file)
- [JSON vs Protocol Buffers](#heading-json-vs-protocol-buffers)
- [The Protoc Compiler and Code Generation](#heading-the-protoc-compiler-and-code-generation)
- [What is gRPC](#heading-what-is-grpc)?
- [Why HTTP/2 Matters for gRPC](#heading-why-http2-matters-for-grpc)
- [The Four gRPC Communication Patterns](#heading-the-four-grpc-communication-patterns)
- [The Protobuf Repository: Organizational Best Practice](#heading-the-protobuf-repository-organizational-best-practice)
- [Building a Complete gRPC System with Dart and Flutter](#heading-building-a-complete-grpc-system-with-dart-and-flutter)
- [Production Concerns](#heading-production-concerns)
- [gRPC vs REST vs WebSockets: When to Use What](#heading-grpc-vs-rest-vs-websockets-when-to-use-what)
- [The Hybrid Architecture](#heading-the-hybrid-architecture)
- [Conclusion](#heading-conclusion)
## What is a Remote Procedure Call?
To understand RPCs, you first need to understand what a procedure call is.
A procedure call means invoking a procedure or function so that its code executes. For example, in Dart:
```
double calculateTax(double amount) {
return amount * 0.075;
}
final tax = calculateTax(50000); // local procedure call
```
You call `calculateTax`, pass an argument, and get a result back. The function lives on the same machine, in the same process, in the same memory space. This is a local procedure call.
A Remote Procedure Call takes this same idea and stretches it across a network. The function you're calling lives on a different machine, in a different process, and potentially in a different country. But from the caller's perspective, it feels exactly like calling a local function.
```
// This looks like a local function call
final tax = await taxService.calculateTax(amount: 50000);
// But under the hood, this:
// 1. Serializes the argument into a binary format
// 2. Sends it over a network connection to a remote server
// 3. The server executes calculateTax with your argument
// 4. Serializes the result
// 5. Sends it back over the network
// 6. Deserializes it into a Dart object
// 7. Returns it to you as if it were local
```
The network complexity is completely hidden. You call a function. You get a result. Everything in between is handled by the RPC framework.
This is the fundamental idea behind RPC: make calling a remote function feel as natural as calling a local one.
## The Problem RPC Solves
To appreciate why RPC matters, you need to understand what the alternative looks like.
Without RPC, calling a remote service looks like this:
```
Future<double> calculateTax(double amount) async {
final response = await http.post(
Uri.parse('https://tax-service.internal/api/v1/calculate'),
headers: {
'Content-Type': 'application/json',
'Authorization': 'Bearer $token',
},
body: jsonEncode({'amount': amount}),
);
if (response.statusCode != 200) {
throw Exception('Tax calculation failed: ${respo

## Related Articles

- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[Automating Ai Away]]
- [[5 Agent Skills I Use Every Day]]
