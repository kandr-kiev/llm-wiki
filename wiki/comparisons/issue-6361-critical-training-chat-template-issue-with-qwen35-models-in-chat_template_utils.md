---
title: "Issue #6361: Critical training chat-template issue with Qwen3.5 models (in `chat_template_utils`)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - foundation-model
  - nlp
  - open-source
  - pipeline
  - prompt-tuning
  - pytorch
  - review
  - system-design
  - training
---
# Issue #6361: Critical training chat-template issue with Qwen3.5 models (in `chat_template_utils`)

> **Source:** gh-huggingfacetrl-issue-6361-2026-07-11.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: https://github.com/huggingface/trl/issues/6361 ingested: 2026-07-11 sha256: b70d66079f98d6344b3325d40dd3fefa5744459374e4f2e20ccc7ede843c4baa blog_source: github:huggingface/trl --- # I...
> **Sources:**
>   - gh-huggingfacetrl-issue-6361-2026-07-11.md
> **Links:**
- [[issue-47254-checkpointerror-with-peft-deepspeed-zero-3-gradient-checkpointing]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[llm-deployment-qa]]

## Key Findings

---
source_url: https://github.com/huggingface/trl/issues/6361
ingested: 2026-07-11
sha256: b70d66079f98d6344b3325d40dd3fefa5744459374e4f2e20ccc7ede843c4baa
blog_source: github:huggingface/trl
---
# Issue #6361: Critical training chat-template issue with Qwen3.5 models (in `chat_template_utils`)
**State:** open | **Author:** giladfrid009 | **Created:** 2026-07-11T10:11:40Z
### Reproduction
**The issue:**
The issue affects Qwen3.5 models and possibly also Qwen3.6 models as well (and maybe others)
For Qwen3.5 models, TRL patches chat templates to a training variant (`trl.chat_template_utils.get_training_chat_template`) which is prefix-preserving. But the issue is that the patched chat template tokenizes the conversation in this format:
`[SOME USER TOKENS AND STUFF] [THE ACTUAL THINKING HERE] [ASSISTANT OUTPUT]`
while it should be this way:
`[SOME USER TOKENS AND STUFF] [THE ACTUAL THINKING HERE] [ASSISTANT OUTPUT]`
**Faithful Reproduction Code:**
```python
from transformers import AutoTokenizer, AutoModelForCausalLM, PreTrainedTokenizerBase
from trl.chat_template_utils import get_training_chat_template
from transformers import pipeline
MODEL_NAME = "Qwen/Qwen3.5-4B"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(MODEL_NAME)
FIRST_USER_PROMPT = {"role": "user", "content": "What is 2+2?"}
SECOND_USER_PROMPT = {"role": "user", "content": "And 3+3?"}
qwen_pipeline = pipeline(
"text-generation",
model=model,
tokenizer=tokenizer,
device_map="auto",
max_length=1000,
do_sample=False,
)
# First, we get a natural response from the model to the first user prompt
response_text = qwen_pipeline([FIRST_USER_PROMPT], return_full_text=False)[0]["generated_text"]
print(f"Response text: {response_text!r}")
CONVERSATION = [FIRST_USER_PROMPT, {"role": "assistant", "content": response_text}, SECOND_USER_PROMPT]
# Now, we switch to the prefix-preserving chat-template and tokenize the conversation
tokenizer.chat_template = get_training_chat_template(tokenizer)
ids = tokenizer.apply_chat_template(
[CONVERSATION],
add_generation_prompt=True,
tokenize=True,
enable_thinking=True,
return_tensors="pt",
return_dict=True,
)
tids = ids.input_ids[0]
for i, (tid, piece) in enumerate(zip(tids, tokenizer.convert_ids_to_tokens(tids))):
print(f"{i:4} {tid:>8} {piece!r}")
```
outputs:
The raw detokenized response text to the `FIRST_USER_PROMPT` is:
```
Response text: 'Thinking Process:\n\n1. **Analyze the Request:** The user is asking a simple arithmetic question: "What is 2+2?"\n\n2. **Identify the Core Fact:** The sum of 2 and 2 is 4.\n\n3. **Formulate the Answer:** The answer should be direct and clear. "4" or "The answer is 4."\n\n4. **Review for Constraints:** There are no special constraints (like "think silently" - wait, I am already doing that, but the output should be the final answer). No complex reasoning needed.\n\n5. **Final Output Generation:** "4" or "2 + 2 = 4". Let\'s keep it simple.\n\n6. **Saf

## Summary

ety Check:** Is this harmful? No. Is it controversial? No.\n\n7. **Final Decision:** State the answer clearly.cw\n\n\n2 + 2 = 4\n'
```
Then, the tokenized conversation looks like this:
```
0 248045 ''
1 846 'user'
2 198 'Ċ'
3 3710 'What'
4 369 'Ġis'
5 220 'Ġ'
6 17 '2'
7 10 '+'
8 17 '2'
9 30 '?'
10 248046 ''
11 198 'Ċ'
12 248045 ''
13 74455 'assistant'
14 198 'Ċ'
15 248068 ''
16 271 'ĊĊ' '
18 271 'ĊĊ'
19 90700 'Thinking'
20 8340 'ĠProcess'
21 25 ':'
22 271 'ĊĊ'
23 16 '1'
24 13 '.'
25 220 'Ġ'
26 2972 'Ġ**'
27 2014 'An'
28 53983 'alyze'
29 279 'Ġthe'
30 5952 'ĠRequest'
31 64700 ':**'
32 561 'ĠThe'
33 1156 'Ġuser'
34 369 'Ġis'
35 9859 'Ġasking'
36 264 'Ġa'
37 4145 'Ġsimple'
38 33633 'Ġarithmetic'
39 3296 'Ġquestion'
40 25 ':'
41 328 'Ġ"'
42 3710 'What'
43 369 'Ġis'
44 220 'Ġ'
45 17 '2'
46 10 '+'
47 17 '2'
48 7285 '?"'
49 271 'ĊĊ'
50 17 '2'
51 13 '.'
52 220 'Ġ'
53 2972 'Ġ**'
54 27382 'Ident'
55 1386 'ify'
56 279 'Ġthe'
57 9237 'ĠCore'
58 35495 'ĠFact'
59 64700 ':**'
60 561 'ĠThe'
61 2542 'Ġsum'
62 314 'Ġof'
63 220 'Ġ'
64 17 '2'
65 321 'Ġand'
66 220 'Ġ'
67 17 '2'
68 369 'Ġis'
69 220 'Ġ'
70 19 '4'
71 13 '.'
72 271 'ĊĊ'
73 18 '3'
74 13 '.'
75 220 'Ġ'
76 2972 'Ġ**'
77 1774 'Form'
78 6134 'ulate'
79 279 'Ġthe'
80 21134 'ĠAnswer'
81 64700 ':**'
82 561 'ĠThe'
83 4087 'Ġanswer'
84 1220 'Ġshould'
85 381 'Ġbe'
86 2050 'Ġdirect'
87 321 'Ġand'
88 2708 'Ġclear'
89 13 '.'
90 328 'Ġ"'
91 19 '4'
92 1 '"'
93 466 'Ġor'
94 328 'Ġ"'
95 760 'The'
96 4087 'Ġanswer'
97 369 'Ġis'
98 220 'Ġ'
99 19 '4'
100 1149 '."'
101 271 'ĊĊ'
102 19 '4'
103 13 '.'
104 220 'Ġ'
105 2972 'Ġ**'
106 18842 'Review'
107 364 'Ġfor'
108 84457 'ĠConstraints'
109 64700 ':**'
110 2532 'ĠThere'
111 513 'Ġare'
112 874 'Ġno'
113 3175 'Ġspecial'
114 16484 'Ġconstraints'
115 318 'Ġ('
116 4650 'like'
117 328 'Ġ"'
118 26003 'think'
119 47733 'Ġsilently'
120 1 '"'
121 471 'Ġ-'
122 3655 'Ġwait'
123 11 ','
124 353 'ĠI'
125 1044 'Ġam'
126 2582 'Ġalready'
127 3604 'Ġdoing'
128 421 'Ġthat'
129 11 ','
130 694 'Ġbut'
131 279 'Ġthe'
132 2468 'Ġoutput'
133 1220 'Ġshould'
134 381 'Ġbe'
135 279 'Ġthe'
136 1534 'Ġfinal'
137 4087 'Ġanswer'
138 553 ').'
139 2233 'ĠNo'
140 6150 'Ġcomplex'
141 31626 'Ġreasoning'
142 4221 'Ġneeded'
143 13 '.'
144 271 'ĊĊ'
145 20 '5'
146 13 '.'
147 220 'Ġ'
148 2972 'Ġ**'
149 18770 'Final'
150 8984 'ĠOutput'
151 22738 'ĠGeneration'
152 64700 ':**'
153 328 'Ġ"'
154 19 '4'
155 1 '"'
156 466 'Ġor'
157 328 'Ġ"'
158 17 '2'
159 478 'Ġ+'
160 220 'Ġ'
161 17 '2'
162 283 'Ġ='
163 220 'Ġ'
164 19 '4'
165 3158 '".'
166 6558 'ĠLet'
167 579 "'s"
168 2426 'Ġkeep'
169 424 'Ġit'
170 4145 'Ġsimple'
171 13 '.'
172 271 'ĊĊ'
173 21 '6'
174 13 '.'
175 220 'Ġ'
176 2972 'Ġ**'
177 70554 'Safety'
178 4109 'ĠCheck'
179 64700 ':**'
180 2091 'ĠIs'
181 411 'Ġthis'
182 26857 'Ġharmful'
183 30 '?'
184 2233 'ĠNo'
185 13 '.'
186 2091 'ĠIs'
187 424 'Ġit'
188 19516 'Ġcontroversial'
189 30 '?'
190 2233 'ĠNo'
191 13 '.'
192 271 'ĊĊ'
193 22 '7'
194 13 '.'
195 220 'Ġ'
196 2972 'Ġ**'
197 18770 'Final'
198 39087 'ĠDecision'
199 64700 ':*

## Related Articles

- [[issue-47254-checkpointerror-with-peft-deepspeed-zero-3-gradient-checkpointing]]
- [[issue-6359-truncate-gold-on-policy-prompts-before-generation-keeping-the-prompt-end]]
- [[issue-14166-fix-hub-download-filtering-for-flashpack-pipelines]]
- [[how-gpt3-works---visualizations-and-animations-2026-07-07]]
- [[llm-deployment-qa]]
