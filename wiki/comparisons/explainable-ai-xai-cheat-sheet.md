---
title: "Explainable AI (XAI) Cheat Sheet"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - analysis
  - best-practice
  - compliance
  - computer-vision
  - deep-learning
  - embedding
  - evaluation
  - foundation-model
  - machine-learning
  - open-source
  - use-case
---
# Explainable AI (XAI) Cheat Sheet

> **Source:** explainable-ai-cheat-sheet.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- type: concept title: Explainable AI (XAI) Cheat Sheet description: Comprehensive cheat sheet covering interpretability methods for AI/ML models, including feature attribution, surrogate models, vi...
> **Sources:**
>   - explainable-ai-cheat-sheet.md
> **Links:**
- [[explainable-ai-cheat-sheet]]
- [[semi-supervised-learning]]
- [[ai-safety-alignment-2026-synthesis]]
- [[llm-fine-tuning]]
- [[explainable-ai]]

## Key Findings


# Explainable AI (XAI) Cheat Sheet
## Overview
Comprehensive cheat sheet covering interpretability methods for AI/ML models. This resource provides practical guidance on selecting and applying explainability techniques across different model types and use cases.
## Key Methods
### Feature Attribution
- **SHAP (SHapley Additive exPlanations)**: Game-theoretic approach to feature importance
- **LIME (Local Interpretable Model-agnostic Explanations)**: Local surrogate models
- **Integrated Gradients**: Gradient-based attribution for deep networks
- **Grad-CAM**: Gradient-weighted class activation mapping for vision models
### Surrogate Models
- **Decision Trees**: Interpretable approximations of complex models
- **Linear Models**: Simple explanations for local behavior
- **Rule-based Systems**: Extracted rules from black-box models
### Visualization Techniques
- **Partial Dependence Plots (PDP)**: Marginal effects of features
- **ICE (Individual Conditional Expectation)**: Individual-level effects
- **Attention Maps**: Visualizing attention weights in transformers
- **t-SNE/UMAP**: High-dimensional embedding visualization
### Model Auditing
- **Bias Detection**: Fairness metrics and bias analysis
- **Robustness Testing**: Adversarial robustness evaluation
- **Sensitivity Analysis**: Input perturbation effects
- **Counterfactual Explanations**: Minimal changes for different outcomes
## When to Use What
| Scenario | Recommended Method |
|----------|-------------------|
| Global model understanding | SHAP summary, PDP |
| Local prediction explanation | LIME, SHAP values |
| Deep learning visualization | Grad-CAM, attention maps |
| Regulatory compliance | Counterfactuals, feature importance |
| Debugging model errors | ICE plots, residual analysis |
## Best Practices
1. **Match method to audience**: Technical vs. non-technical stakeholders
2. **Validate explanations**: Ensure explanations are stable and faithful
3. **Combine methods**: Use multiple approaches for comprehensive understanding
4. **Document limitations**: Be transparent about explanation fidelity
5. **Iterate**: Refine explanations based on stakeholder feedback
## Related Concepts
- [[feature-attribution]] — Feature attribution methods (SHAP, LIME)
- [[model-interpretability]] — Model interpretability techniques

## Summary

See Key Findings for full content.

## Related Articles

- [[explainable-ai-cheat-sheet]]
- [[semi-supervised-learning]]
- [[ai-safety-alignment-2026-synthesis]]
- [[llm-fine-tuning]]
- [[explainable-ai]]
