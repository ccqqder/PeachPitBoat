---
title: "Dream of the Red Chamber Simulator: The Holy Grail of Social Science, and LLMs as Prophetic Verse"
date: 2026-03-22T03:31:45.090Z
draft: false
author: "QQder"
categories:
  - The Workshop
tags:
  - ontology
  - ontology
  - Eileen Chang
  - LLM
  - Dream of the Red Chamber
  - prophetic verse
keywords:
  - LLM
  - large language model
  - Dream of the Red Chamber
  - Dream of the Red Chamber
  - Cao Xueqin
  - social science
  - prediction
  - literary analysis
  - knowledge graph
  - Word Embedding
  - Redology
  - prophetic verse
  - psychohistory
  - multi-agent
description: "Predicting the future — from fortune and misfortune to the fate of humanity — has been a grand challenge since the dawn of civilization. LLMs offer us a glimpse of hope for tackling this problem."
---

***

## Preface

Predicting the future — from fortune and misfortune to the fate of humanity — has been one of the grand challenges of human civilization since antiquity. Large Language Models (LLMs) now offer us a glimpse of hope for tackling this problem.

This article explores the use of LLMs as the latest tool, with *Dream of the Red Chamber* (紅樓夢) serving as a sandbox, to find methods for predicting the novel's lost final forty chapters.

Let me state upfront: I have not succeeded. Perhaps one day when someone does, this article will surface in their search results.

This piece is more of a meditation on the nature of text itself. While text lacks the precision of physical formulas,

as a tool for humanity to grasp reality and speculate about the future, it is far more important than we imagine.

Text is not merely an "imagined" reality — it is not inherently subjective. It simply mirrors objective reality in the most cost-effective way possible.

And LLMs, as automated mechanisms for predicting text, will radically compress the cost of extracting, generating, and mirroring objective reality.

The latest implementation will be updated in the iOS app: Dream of the Red Chamber Simulator.

APP: [Link](https://apps.apple.com/tw/app/%E7%B4%85%E6%A8%93%E5%A4%A2%E6%A8%A1%E6%93%AC%E5%99%A8/id6759855416)

![紅樓夢模擬器](/images/1024x1024bb.png)

> The three great regrets in life: First, that the shad has too many bones; second, that the crabapple blossom has no fragrance; third, that *Dream of the Red Chamber* was never finished.

— Eileen Chang (張愛玲)

***

## Celestial Patterns: More Than Just Word Prediction

Predicting the future has always been a matter of great importance in human societies. Every ancient civilization had priests or officials dedicated to observing the stars.

Symbol systems such as astronomy and hydrology textualized natural phenomena and physical laws. The most quintessential example is the coordinate system of latitude and longitude — text became a crucial tool for humanity to understand and influence the objective world.

The practical power of this mapping between text and reality has been validated in these recent years of explosive LLM capability.

In the past, language as a tool was not sufficiently deterministic. After the Industrial Revolution, when science became the primary driver of productivity, language was perpetually relegated to the bottom of the prestige hierarchy.

The age of LLMs has finally brought the digestion and production of text into the millisecond domain, freeing it from the bottlenecks of human reading speed, typing speed, and typographical errors.

Work that once consumed enormous mental energy and time now has the potential to be assembled and configured like a production line.

But what does this production line produce? The essence of an LLM is "predicting" the next token. Is this actually productive? Does the model "sort of" "understand" what it is saying?

Ilya Sutskever (former co-founder and chief scientist of OpenAI) once gave this example:

> Say you read a detective novel, and on the last page, the detective says "I am going to reveal the identity of the criminal, and that person's name is..."

If an LLM can consistently and correctly guess the identity of the culprit, then we can tentatively say it "understands" the novel — at least surpassing the many readers who guessed wrong.

And we must properly appreciate what "understanding" means. Understanding is ultimately for predicting the future. Every ancient civilization, without exception, studied astronomy and hydrology

precisely to forecast upcoming climate patterns, changes in river courses, droughts and floods — to survive better in the objective environment.

One could even argue that predicting correctly matters more than understanding.

***

## The Humanities: Both People and Agents Remain Black Boxes

Predicting the future is the pursuit and prerequisite (reproducibility) of the natural sciences, and the holy grail of the social sciences.

This admittedly sounds like science fiction. In Isaac Asimov's *Foundation* series, such a discipline for predicting the future was fictionalized as "psychohistory" (心理史學).

Economists, historians, psychologists, social scientists — all want to know how individuals and societies will react to specific events.

Finance, in particular, is probably the field outside of software where AI is being applied most aggressively.

Although we cannot yet see the finish line, the feasibility of this endeavor has improved significantly.

The improvement — and its limitation — is that we now have a remarkable black box (the LLM agent).

For tasks at a level comparable to human performance, it is blazingly fast and extremely cheap, making it suitable for replacing human labor.

The limitation is that its current mode of use resembles a slot machine. We can use certain techniques (prompt/context engineering) to improve the hit rate, but that is about it.

We struggle to open the black box. Chaining multiple black boxes together (multi-agent) yields only limited improvement.

Currently, tasks that a single agent can handle are done quickly and well, but more abstract tasks are difficult to improve linearly.

Applied to social science: a single agent cannot adequately simulate even one individual's memory and emotions, let alone having multi-agent systems simulate an entire community.

On the optimistic side, this feels more like a performance problem — and performance within this paradigm will continue to improve.

***

## The Sandbox: Don't Aim for a One-Hit Kill

Since we are dealing with a black box, the intuitive approach is to find a smaller box to attempt to crack.

Assume the current baseline model capability is what was described earlier: throw any detective novel into the LLM slot machine, and it can directly (one-shot) and correctly output who the culprit is.

Building on this baseline, if we put in extra effort — erecting scaffolding, going back and forth with the LLM in discussion, finding ways to linearly accumulate results across each exchange — we should theoretically be able to make predictions of higher difficulty.

*Dream of the Red Chamber* is the perfect target. Based on the content of the first eighty chapters, we ask the model to predict, to some degree, the final forty chapters.

This prediction is extremely difficult, but it is just right for my working objectives. Theoretically the probability is not zero; practically it is highly unlikely. This makes it an ideal benchmark for observing LLM capability growth over the coming years.

Having written this far, I can finally articulate two working objectives:

1. How can we put in additional effort so that answers unattainable through one-shot prompting can be progressively approached?
2. How should we choose our battleground so that our results are not immediately rendered obsolete by stronger models — and ideally, so that our framework also benefits when future models improve?

Below, I begin considering research methods based on the characteristics of *Dream of the Red Chamber* and LLMs.

### Assumptions

We assume that the ending of *Dream of the Red Chamber* did once exist, and that the first eighty chapters and the subsequent conclusion were written as an organic, intentional, continuous work — exhibiting the same internal coherence found within the first eighty chapters themselves.

If the ending never actually existed, the prediction difficulty is even higher — approaching the prediction of a parallel universe. The question becomes: if Cao Xueqin had written the ending, what would it *necessarily* have been?

This word "necessarily" is the crux. One must reach this level of confidence for generating something from nothing to be meaningful.

### The Writing of *Dream of the Red Chamber*

The novel was composed around the 1750s. At that time it circulated mostly among friends and relatives. It was not until 1791, when Cheng Weiyuan published it using movable wooden type, that it became widely known.

### Redology and AI-Assisted Research

Wang Guowei and Hu Shi were pioneers of Redology (紅學 — the scholarly study of *Dream of the Red Chamber*). The field has continued to develop, and in recent years has trended toward popularization and entertainment. The attention given to textual archaeology (探佚學) and the controversial Guiyou manuscript (癸酉本) reflects the public's curiosity about the ending.

Key research achievements incorporating the latest technology include:

* Machine learning once again confirming that the final forty chapters were not written by the original author
* Using LLMs for more nuanced semantic vectorization of text (Word Embedding)
* Using LLMs to build domain-specific knowledge graphs
* Models trained specifically on the first eighty chapters and Qing dynasty historical texts as input data

### LLM Characteristics

The LLM characteristic most relevant to this task is: it has been trained on all data available on the internet, plus all valuable materials these frontier AI labs could obtain.

For information already in its training data, the model's predictive capability and tendency are very high. For instance, if you input a passage from *Harry Potter*, it can recite the subsequent paragraphs from memory.

But the final forty chapters of *Dream of the Red Chamber* were never transmitted to posterity. They are not in the model's training data. It cannot recite them.

#### Problem 1: Context Window Limitations

Can we simply input chapters one through eighty and ask the LLM to output the remaining forty?

On the input side, the current top-tier models (Gemini 3.1 / GPT-5.4 / Opus 4.6) using API mode can support up to 1M tokens, which is sufficient.

However, under the current paradigm, the output token window is far smaller than the input. Output is limited to roughly four to eight thousand Chinese characters at most — approximately one chapter's worth of content.

#### Problem 2: Listless Prose and Quality Degradation

What if we modify the prompt to ask the LLM to output only the content of chapter eighty-one?

The model gets "contaminated" by the massive text input. Its writing style closely resembles Cao Xueqin's, and it can reasonably continue the known plot — but the result reads like a flat chronicle of events.

Then, repeating the process for chapters eighty-two, eighty-three, and so on, the quality drops precipitously.

#### Problem 3: Prior Contamination in the Model

Another issue is that during training, the model has already seen Gao E's continuation (高鶚續書), various scholarly speculations, and other secondary sources. If these materials diverge from the original ending, the output will be biased.

## To Be Continued

Due to the length of this piece, I will wrap up here with a preview of what comes next.

We cannot simply have the LLM directly produce unknown information.

So we still need more traditional, mechanical, or programmatic methods.

The good news is: for the tireless researchers of literature, history, and philosophy — we now have a tractor for the field!

*Dream of the Red Chamber* possesses a highly structured nature. Important characters have their own 判詞 (prophetic verses, known as "pànCí") — poetic passages that cryptically foreshadow each character's fate.

Moreover, the first eighty chapters can be cross-validated against one another, making the novel more amenable to prediction than many other works of fiction.

Although the cast of characters is large and their backgrounds complex, what we are ultimately predicting is Cao Xueqin's artistic vision — his creative will permeates the entire work. This is a tremendous aid for predicting the ending.

## Next: The Thermodynamics of *Dream of the Red Chamber*

The next article will introduce the experimental approach: structurally extracting content from the text, iteratively experimenting to extract the rules embedded in the novel, and using code to run repeated experiments.

The idealized scenario is something akin to a thermodynamic system: given initial conditions (premises — e.g., characters, family wealth, socioeconomic status, interpersonal networks...) plus the system's operating mechanisms (human psychology, social hierarchy, economic dynamics, cultural norms, karmic retribution, etc.), one could predict the system's state at any subsequent point in time.
