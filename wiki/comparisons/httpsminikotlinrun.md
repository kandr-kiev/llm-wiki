---
title: "https://minikotlin.run"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - analysis
  - backend
  - data
  - foundation-model
  - frontend
  - image-generation
  - multi-agent
  - news
  - nlp
  - open-source
  - pipeline
  - prompt-tuning
  - system-design
  - use-case
---

# https://minikotlin.run

> **Source:** minikotlin-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** [ ![](./assets/favicon.svg) minikotlin ](#top) [pipeline](#pipeline) [language](#features) [lowerings](#lowering) [specimen](#specimen) [coverage](coverage.html) [Open Studio ](studio/) Kotlin **â**...
> **Sources:**
>   - minikotlin-2026-07-17.md
> **Links:**
- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]

## Key Findings

[
![](./assets/favicon.svg)
minikotlin
](#top)
[pipeline](#pipeline)
[language](#features)
[lowerings](#lowering)
[specimen](#specimen)
[coverage](coverage.html)
[Open Studio
](studio/)
Kotlin **â** WebAssembly  Â·  a compiler written in C
# A Kotlin compiler
that runs in a *browser tab.*
minikotlin is written from scratch in C and emits **WebAssembly GC bytecode by hand** â no JVM, no LLVM, no Binaryen, no Gradle. The compiler is itself compiled to WASM, so `.kt` source goes in and a running `.wasm` module comes out, **entirely in the tab**.
[Open the Studio
](studio/)
[Read a specimen](#specimen)
backendWASM-GCstructs Â· call_ref Â· EH
servernoneruns client-side
end-to-end tests366frontend: 657
runtime deps0nothing installed
**greeter** â minikotlin Studio
RUN
greeter / src
Main.kt
Greeter.kt
output
Console
12345678
// Main.kt + Greeter.kt compile as one unit
fun main() {
val g = Greeter("WebAssembly")
println(g.greet())
(1..3).forEach { println("tick $it") }
}
build 2 .kt → main.wasm Â· ok, 41ms
Hello, WebAssembly
tick 1
tick 2
tick 3
the pipeline
**.kt**â
lexâ
parseâ
semaâ
**HIR**â
**MIR**â
**WASM-GC**â
run
01
## One pass, all the way down to bytecode.
No intermediate VM, no external backend. The frontend â lexer, parser, semantic analysis (it’s called **mkf**) â hands off to two of its own IRs before writing WASM-GC by hand.
**input
Kotlin source
Multiple `.kt` files, compiled as one unit so they can see each other.
**frontend Â· mkf
lex Â· parse Â· sema
Names, types and smart-casts resolved. 657 frontend tests.
**high IR
HIR
A desugared, typed tree that still sits close to the language.
**mid IR
MIR
Lowered to ops, locals, struct layouts and vtables.
**codegen
WASM-GC
Bytecode emitted directly. No LLVM, no Binaryen in the loop.
**output
main.wasm
Instantiated and run in the same browser tab.
The compiler **ships as WASM itself**, so it runs where your code runs â no toolchain to install.
---
02
## The Kotlin it speaks today.
Not a token subset. These are lowered properly onto the WASM-GC type system â each one has end-to-end tests behind it.
Classes & objectsobject model
Inheritance (`open`/`override`), interfaces with default methods, `data class` with generated `equals`/`hashCode`/`copy`, `enum`, and named, companion & anonymous `object` expressions.
Sealed & smart-castscontrol flow
`sealed` hierarchies with exhaustive `when`, `is` checks compiled to `ref.test`, and flow-sensitive smart-casting that holds across branches.
Null safetytypes
Nullable types end to end â `?.` safe calls, `?:` elvis and `!!` assertions â including nullable primitives, boxed through `Any`.
Genericstypes
Type parameters on functions and classes â `fun <T> id(x: T): T` â lowered over a boxed `Any` representation.
Operators & extensionsergonomics
Operator overloading (`plus`, `get`, …) dispatched to the LHS class, extension functions in their own namespace, and custom accessors with a backing `field`.
Coroutinesnon-blocking
`laun

## Summary

See Key Findings for full content.

## Related Articles

- [[Sites That Block Ai Training Crawlers Mostly Ignore The Answer Time Bots]]
- [[Automating Ai Away]]
- [[Automating away]]
- [[Mesh LLM: distributed AI computing on iroh]]
- [[[karpathy](https://gist.github.com/karpathy)/**[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**]]
