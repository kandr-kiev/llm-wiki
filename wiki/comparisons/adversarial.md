---
title: "adversarial"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - compliance
  - distributed
  - edge
  - nlp
  - software
  - system-design
  - use-case
---
# adversarial

> **Source:** adversarial-reprogramming-of-neural-cellular-automata-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/selforg/2021/adversarial ingested: 2026-07-10 sha256: 446dfd476f6ad199a8b486e3384a8764d3b68f6a2c1f795fd1be676fa6bf9b5f blog_source: Distill AI --- -  -  -  Adversar...
> **Sources:**
>   - adversarial-reprogramming-of-neural-cellular-automata-2026-07-10.md
> **Links:**
- [[gnn-intro]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[train-large-neural-networks]]

## Key Findings

---
source_url: https://distill.pub/selforg/2021/adversarial
ingested: 2026-07-10
sha256: 446dfd476f6ad199a8b486e3384a8764d3b68f6a2c1f795fd1be676fa6bf9b5f
blog_source: Distill AI
---
- 
- 
- 
Adversarial Reprogramming of Neural Cellular Automata
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Adversarial Reprogramming of Neural Cellular Automata
A robustness investigation.
### Authors
### Affiliations
[Ettore Randazzo](https://oteret.github.io/)
[Google](https://ai.google/)
[Alexander Mordvintsev](https://znah.net/)
[Google](https://ai.google/)
[Eyvind Niklasson](https://eyvind.me/)
[Google](https://ai.google/)
[Michael Levin](http://www.drmichaellevin.org)
[Allen Discovery Center at Tufts University](http://allencenter.tufts.edu)
### Published
May 6, 2021
### DOI
[10.23915/distill.00027.004](https://doi.org/10.23915/distill.00027.004)
### Contents
[Adversarial MNIST CAs](#adversarial-mnist-cas) | [](https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_mnist_ca.ipynb)
[Adversarial Injections for Growing CAs](#adversarial-injections-for-growing-cas) | [](https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_growing_ca.ipynb#scrollTo=ByHbsY0EuyqB)
[Perturbing the states of Growing CAs](#perturbing-the-states-of-growing-cas) | [](https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_growing_ca.ipynb#scrollTo=JaITnQv0k1iY)
[Related Work](#related-work)
[Discussion](#discussion)
![](images/multiple-pages.svg)
This article is part of the
[Differentiable Self-organizing Systems Thread](/2020/selforg/),
an experimental format collecting invited short articles delving into
differentiable self-organizing systems, interspersed with critical
commentary from several experts in adjacent fields.
[Self-Organising Textures](/selforg/2021/textures/)
This article makes strong use of colors in figures and demos. Click [here](#colorwheel) to adjust the color palette.
In a complex system, whether biological, technological, or social, how can we discover signaling events that will alter system-level behavior in desired ways? Even when the rules governing the individual components of these complex systems are known, the inverse problem - going from desired behaviour to system design - is at the heart of many barriers for the advance of biomedicine, robotics, and other fields of importance to society.
Biology, specifically, is transitioning from a focus on mechanism (what is required for the system to work) to a focus on information (what algorithm is sufficient to implement adaptive behavior). Advances in machine learning represent an exciting and largely untapped source of inspiration and tooling to assist the biological sciences. Growing Neural Cellular Automata and Self-classifying MNIST Digits introduced

## Summary

 the Neural Cellular Automata (Neural CA) model and demonstrated how tasks requiring self-organisation, such as pattern growth and self-classification of digits, can be trained in an end-to-end, differentiable fashion. The resulting models were robust to various kinds of perturbations: the growing CA expressed regenerative capabilities when damaged; the MNIST CA were responsive to changes in the underlying digits, triggering reclassification whenever necessary. These computational frameworks represent quantitative models with which to understand important biological phenomena, such as scaling of single cell behavior rules into reliable organ-level anatomies. The latter is a kind of anatomical homeostasis, achieved by feedback loops that must recognize deviations from a correct target morphology and progressively reduce anatomical error.
In this work, we *train adversaries *whose goal is to reprogram CA into doing something other than what they were trained to do. In order to understand what kinds of lower-level signals alter system-level behavior of our CA, it is important to understand how these CA are constructed and where local versus global information resides.
The system-level behavior of Neural CA is affected by:
- **Individual cell states. **States store information which is used for both diversification among cell behaviours and for communication with neighbouring cells.
- **The model parameters. **These describe the input/output behavior of a cell and are shared by every cell of the same family. The model parameters can be seen as *the way the system works*.
- **The perceptive field. **This is how cells perceive their environment. In Neural CA, we always restrict the perceptive field to be the eight nearest neighbors and the cell itself. The way cells are perceived by each other is different between the Growing CA and MNIST CA. The Growing CA perceptive field is a set of weights fixed both during training and inference, while the MNIST CA perceptive field is learned as part of the model parameters.
Perturbing any of these components will result in system-level behavioural changes.
We will explore two kinds of adversarial attacks: 1) injecting a few adversarial cells into an existing grid running a pretrained model; and 2) perturbing the global state of all cells on a grid.
For the first type of adversarial attacks we train a new CA model that, when placed in an environment running one of the original models described in the previous articles, is able to hijack the behavior of the collective mix of adversarial and non-adversarial CA. This is an example of injecting CA with differing *model parameters* into the system. In biology, numerous forms of hijacking are known, including viruses that take over genetic and biochemical information flow , bacteria that take over physiological control mechanisms and even regenerative morphology of whole bodies , and fungi and toxoplasma that modulate host behavior . Especially fascinating are the many 

## Related Articles

- [[gnn-intro]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
- [[automating-ai-away-2026-07-07]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[train-large-neural-networks]]
