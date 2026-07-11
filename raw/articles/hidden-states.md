---
title: "hidden states"
type: comparison
tags: [comparison]
description: Comparison page for hidden states

sources: []
links: []
description: Comparison page for hidden states

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
# hidden states

> **Source:** finding-the-words-to-say-hidden-state-visualizations-for-language-models-2026-07-07.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

---
source_url: http://jalammar.github.io/hidden-states/
ingested: 2026-07-07
sha256: c5fe0855dbe7ae5936b12f62415f0b012449c4d2bf762b8be0d7395bbf766e4e
blog_source: Jay Alammar
---
Finding the Words to Say: Hidden State Visualizations for Language Models – Jay Alammar – Visualizing machine learning one concept at a time.
- 
- 
- 
- 
- 
- 
[![](https://avatars0.githubusercontent.com/u/1007956?s=460&v=4)](/)
# [Jay Alammar](/)
Visualizing machine learning one concept at a time.
Read our book, [Hands-On Large Language Models](https://www.LLM-book.com) and follow me on [LinkedIn](https://www.linkedin.com/in/jalammar/), [Bluesky](https://bsky.app/profile/jayalammar.bsky.social), [Substack](https://newsletter.languagemodels.co/), [X](https://x.com/JayAlammar),[YouTube ](https://www.youtube.com/channel/UCmOwsoHty5PrmE-3QhUBfPQ)
[Blog](/)
[About](/about)
# Finding the Words to Say: Hidden State Visualizations for Language Models
- 
By visualizing the hidden state between a model's layers, we can get some clues as to the model's "thought process".
![](/images/explaining/rankings-gpt2xl.png)
**Figure: Finding the words to say**
After a language model generates a sentence, we can visualize a view of how the model came by each word (column). Each row is a model layer. The value and color indicate the ranking of the output token at that layer. The darker the color, the higher the ranking. Layer 0 is at the top. Layer 47 is at the bottom.
**Model:**GPT2-XL
Part 2: Continuing the pursuit of making Transformer language models more transparent, this article showcases a collection of visualizations to uncover mechanics of language generation inside a pre-trained language model. These visualizations are all created using [Ecco](https://www.eccox.io), the open-source package we're releasing
In the first part of this series, [Interfaces for Explaining Transformer Language Models](/explaining-transformers/), we showcased interactive interfaces for input saliency and neuron activations. In this article, we will focus on the hidden state as it evolves from model layer to the next. By looking at the hidden states produced by every transformer decoder block, we aim to gleam information about how a language model arrived at a specific output token. This method is explored by Voita et al.. Nostalgebraist 
presents compelling visual treatments showcasing the evolution of token rankings, logit scores, and softmax
probabilities for the evolving hidden state through the various layers of the model.
## Recap: Transformer Hidden States
The following figure recaps how a transformer language model works. How the layers result in a final hidden state. And how that final state is then projected to the output vocabulary which results in a score assigned to each token in
the model's vocabulary. We can see here the top scoring tokens when DistilGPT2 is fed the input sequence " 1, 1,
":
![](/images/explaining/transformer-language-model-steps.png)
**Figure: Recap of transformer language mo

## Summary

dels.**
This figure shows how the model arrives at the top five output token candidates and their probability scores. This shows us that at the final layer, the
model is 59% sure the next token is ' 1', and that would be chosen as the output token by greedy decoding.
Other probable outputs include ' 2' with 18% probability (maybe we are counting) and ' 0' with 5%
probability (maybe we are counting down).
Ecco provides a view of the model's top scoring tokens and their probability scores.
```
# Generate one token to complete this input string
output = lm.generate(" 1, 1, 1,", generate=1)
# Visualize
output.layer_predictions(position=6, layer=5)
```
Which would show the following breakdown of candidate output tokens and their probability scores:
![](/images/explaining/prediction_scores.PNG)
**Figure: Ten tokens with highest probabilities at the final layer of the model.**
## Scores after each layer
Applying the same projection to internal hidden states of the model gives us a view of how the model's conviction
for the output scoring developed over the processing of the inputs. This projection of internal hidden states
gives us a sense of which layer contributed the most to elevating the scores (and hence ranking) of a certain
potential output token.
![](/images/explaining/predictions.PNG)
**Figure: projecting inner hidden states to the model's vocabulary reveals cues of processing between layers.**
Viewing the evolution of the hidden states means that instead of looking only at the candidates output tokens from
projecting the final model state, we can look at the top scoring tokens after projecting the hidden state
resulting from each of the model's six layers.
This visualization is created using the same method above with omitting the 'layer' argument (which we set to the final layer in the previous example, layer #5):
```
# Visualize the top scoring tokens after each layer
output.layer_predictions(position=6)
```
Resulting in: 
![](/images/explaining/predictions%20all%20layers.PNG)
**Figure: Top scoring tokens after each of the model's six layers.**
Each row shows the top ten predicted tokens obtained by projecting each hidden state to the output
vocabulary. The probability scores are shown in pink (obtained by passing logit scores through softmax). We
can see that **Layer 0** has no digits in its top ten predictions. **Layer 1**
gives the token ' 1' a 0.03%, probability which, while low, still ranks the token as the seventh highest
ranking token. Subsequent layers keep elevating the probability and ranking of ' 1', until **the final
layer** injects a bit more caution by reducing the probability from 100% to ~60%, still retaining the
token as the highest ranked in the model's output.
**Note:** This figure is incorrect in showing 0 probability assigned to some tokens due to rounding. The current version of Ecco fixes this by showing '<0.01%'.
You can experiment with these visualizations and experiment with them on your own input sentences at the f

## Related Articles

- 
- 
- [[finding-the-words-to-say-hidden-state-visualizations-for-language-models-2026-07-07]]
- 
- [[interfaces-for-explaining-transformer-language-models-2026-07-07]]
