---
title: "curve circuits"
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
# curve circuits

> **Source:** curve-circuits-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://distill.pub/2020/circuits/curve-circuits ingested: 2026-07-10 sha256: e53602fbdbeda144b0ef4260b89a752f49cf87c525970e78c1a85c6ceac3afcd blog_source: Distill AI --- -  -  -  Curv...
> **Sources:**
>   - curve-circuits-2026-07-10.md
> **Links:**
- [[branch-specialization]]
- [[gnn-intro]]
- [[animals-vs-ghosts]]
- [[chemical-hygiene]]
- [[finding-the-words-to-say-hidden-state-visualizations-for-language-models-2026-07-07]]

## Key Findings

---
source_url: https://distill.pub/2020/circuits/curve-circuits
ingested: 2026-07-10
sha256: e53602fbdbeda144b0ef4260b89a752f49cf87c525970e78c1a85c6ceac3afcd
blog_source: Distill AI
---
- 
- 
- 
Curve Circuits
- 
[
Distill
](/)
[About](/about/)
[Prize](/prize/)
[Submit](/journal/)
# Curve Circuits
We reverse engineer a non-trivial learned algorithm from the weights of a
neural network and use its core ideas to craft an 
*artificial artificial neural network* from scratch that reimplements
it.
Artificial Curve Neurons
Natural InceptionV1 Curve Neurons
![](banner-artificial.png)
![](banner-natural.png)
We can compare the curve detectors in a neural network we hand-crafted
with the curve detectors in InceptionV1 by measuring how they activate
to synthetic curve stimuli. We see that across a range of radii and
orientations, our artificial curve neurons approximate the natural ones.
### Authors
### Affiliations
[Nick Cammarata](http://nickcammarata.com)
[OpenAI](https://openai.com)
[Gabriel Goh](http://gabgoh.github.io)
[OpenAI](https://openai.com)
[Shan Carter](http://shancarter.com)
[Observable](https://observablehq.com)
[Chelsea Voss](https://twitter.com/cvoss)
[OpenAI](https://openai.com)
[Ludwig Schubert](https://schubert.io/)
[Chris Olah](https://colah.github.io)
### Published
Jan. 30, 2021
### DOI
[10.23915/distill.00024.006](https://doi.org/10.23915/distill.00024.006)
### Author Contributions
As we mentioned in Curve Detectors, our first investigation into curve neurons, it’s hard to separate author contributions between different papers in the Circuits project. Much of the original research on curve neurons came before we decided to separate the publications into the behavior of curve neurons and how they are built. In this section we’ve tried to isolate contributions specific to the mechanics of the curve neurons.
**Interface Design & Prototyping.** Many weight diagrams were first prototyped by Chris during his first investigations of different families of neurons in early early vision, and some of these were turned into presentations. Nick extended them for use in this paper. Chris designed and implemented the decomposed feature visualization figure in the first section. Many of the other interfaces were designed by Nick with the help of Shan and Chris. In particular, Shan helped to design the figure showing how the different families of early vision connect leading up to the curve family.
**Conceptual Contributions.** The earliest understandings of how curve neurons are built from lines and edges came from Chris, and the details came from further investigation by Nick. Nick investigated the line families in detail, including finding cliff line neurons and studying they are used. Nick studied through neuron families in the early layers, studying how shape neurons incrementally incorporate increasingly sophisticated texture and cosmetic neurons, working towards the neuron families diagram in the first section. The artificial artificial neur

## Summary

al network was done by Chris and Nick expanded on it for use in the article. Gabe was instrumental in helping discover many of the techniques used for closely studying Circuits, and provided input and suggestions at many steps throughout our investigation of the curve circuit.
**Writing.** Nick and Chris wrote the text of the article with significant help editing from Chelsea.
**Infrastructure.** Nick built the infrastructure for extracting figures from the paper for reproduction in Colab. Ludwig is responsible for the distributed infrastructure that was used for many experiments.
### Acknowledgements
Our article was greatly improved thanks to the detailed feedback by Patricia Robinson, Jennifer Lin, Adam Shimi, Sam Havens, Stefan Sietzen, Dave Vladman, Maxim Liu, Fred Hohman, Vincent Tjeng, and Humza Iqbal.
We also really appreciate the conversations in the #circuits channel of the open [Distill Slack](http://slack.distill.pub/), which at the time of publishing contains more than 600 people.
### Updates and Corrections
If you see mistakes or want to suggest changes, please [create an issue on GitHub](https://github.com/distillpub/post--circuits-curve-circuits/issues/new). 
### Reuse
Diagrams and text are licensed under Creative Commons Attribution [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) with the [source available on GitHub](https://github.com/distillpub/post--circuits-curve-circuits), unless noted otherwise. The figures that have been reused from other sources don’t fall under this license and can be recognized by a note in their caption: “Figure from …”.
### Citation
For attribution in academic contexts, please cite this work as
Cammarata, et al., "Curve Circuits", Distill, 2021.
BibTeX citation
@article{cammarata2021curve,
author = {Cammarata, Nick and Goh, Gabriel and Carter, Shan and Voss, Chelsea and Schubert, Ludwig and Olah, Chris},
title = {Curve Circuits},
journal = {Distill},
year = {2021},
note = {https://distill.pub/2020/circuits/curve-circuits},
doi = {10.23915/distill.00024.006}
}
[["olah2017feature",{"author":"Olah, Chris and Mordvintsev, Alexander and Schubert, Ludwig","title":"Feature Visualization","journal":"Distill","year":"2017","url":"https://distill.pub/2017/feature-visualization","doi":"10.23915/distill.00007","type":"article"}],["1326611",{"author":"K. {Raghupathy} and T. W. {Parks}","booktitle":"2004 IEEE International Conference on Acoustics, Speech, and Signal Processing","title":"Improved curve tracing in images","year":"2004","volume":"3","number":"","pages":"iii-581","type":"INPROCEEDINGS"}],["ballard1987generalizing",{"title":"Generalizing the Hough transform to detect arbitrary shapes","author":"Ballard, Dana H","booktitle":"Readings in computer vision","pages":"714--725","year":"1987","publisher":"Elsevier","type":"incollection"}],["lecun2015deep",{"title":"Deep learning","author":"LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey","url":"https://s3.us-east-2.amazonaws.com/hkg-website-assets/

## Related Articles

- [[branch-specialization]]
- [[gnn-intro]]
- [[animals-vs-ghosts]]
- [[chemical-hygiene]]
- [[finding-the-words-to-say-hidden-state-visualizations-for-language-models-2026-07-07]]
