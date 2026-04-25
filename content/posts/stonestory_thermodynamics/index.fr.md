---
isStub: true
title: "Dream of the Red Chamber Simulator: Thermodynamics and Artistic Choice"
date: 2026-03-29T15:28:32.157Z
draft: false
categories:
  - The Workshop
tags:
  - Thermodynamics
  - Dream of the Red Chamber
  - LLM
  - Rule Engine
  - Literary Simulation
keywords:
  - thermodynamics
  - Dream of the Red Chamber
  - 紅樓夢
  - Red Chamber simulator
  - LLM
  - large language model
  - rule engine
  - Cao Xueqin
  - structured analysis
  - literary prediction
  - Twelve Beauties of Jinling
  - prophetic verse
  - artistic choice
  - simulation engine
description: "What has changed is that productivity has suddenly become much higher. What the Dream of the Red Chamber Simulator aims to do is, with such productivity at hand, use traditional structured methods to rapidly produce and accumulate results with minimal human effort."
author: "QQder"
---

App URL: [LINK](https://apps.apple.com/tw/app/%E7%B4%85%E6%A8%93%E5%A4%A2%E6%A8%A1%E6%93%AC%E5%99%A8/id6759855416)

## Preface

The key point from the previous installment

was to regard text as fundamentally symbolic --

astronomy, hydrology, the humanities... all the "wen" (文, pattern/text) of heaven, earth, and humankind.

Text maps the world and thought in a cost-effective way,

becoming our primary tool for understanding and interfacing with objective reality.

Once you grasp this, you realize that

although LLMs (Large Language Models) are essentially just next-token predictors,

once their capability reaches a certain level, they become nuclear-grade instruments of national importance.

Their significance made me want to verify their capabilities

and to do so repeatedly as they improve over time.

A near-perfect benchmark for this is *Dream of the Red Chamber* (紅樓夢, *Hong Lou Meng*).

Suppose there existed an omniscient, omnipotent LLM --

it could take Cao Xueqin's original first 80 chapters of *Dream of the Red Chamber* as input and output the subsequent chapters.

But because LLM training data is limited,

it is like a Sudoku puzzle with too few given numbers -- the answer cannot be determined with certainty.

What current LLMs can do is produce at very high throughput within the scope of what they understand.

What the *Dream of the Red Chamber Simulator* aims to do is, with such productivity at hand,

use traditional structured methods to rapidly produce and accumulate results with minimal human effort.

## Assumptions

We need some assumptions, biases, and theories to make the task of predicting the ending sufficiently feasible and mechanical.

When it comes to accurate prediction, my intuition goes to classical physics -- specifically thermodynamics.

In a closed system, if we specify the initial conditions and the governing laws,

the evolution of a thermodynamic system is predictable and deterministic.

Another assumption is that LLM capabilities will keep improving,

but in the foreseeable future we will not gain additional training data from the Qing Dynasty or from Cao Xueqin himself.

Therefore, we can establish a structured workflow that both current and future LLMs can execute.

### Initial Conditions

The initial conditions are primarily data extracted from the original novel.

Now we use LLMs to perform what was previously highly labor-intensive work.

In the past, human labor costs were too high, and throwing more people at the problem could not compress the timeline.

If you got halfway through and wanted to tweak the extraction rules and start over, it was simply impractical.

Time and cost are no longer obstacles; extraction quality now depends on model capability.

For example, I extracted:

- Key character profiles, personality dossiers, family genealogies;

- Per-chapter snapshots of each character's economic, social, emotional, health, and interpersonal states across all 120 chapters;

- A basic spatial map of the Jia (賈) estate with spatial metadata;

- All dialogue records, poetry corpora...

The approach was to start with broad, not-yet-rigorous extraction that at least achieves high coverage -- ensuring every piece of text is classified into some category.

### Governing Laws

I divide the governing laws into two types by my own judgment: fundamental world rules and the author's artistic will.

This is admittedly arbitrary, but without making some such judgment the work cannot proceed at all.

World rules include but are not limited to:

- Society: class hierarchy, power dynamics, master-servant relationships, marriage;

- Economy: income and expenditure, debt, risk of property confiscation;

- Culture: Confucian propriety, festivals, feudal values;

- Psychology: character emotions, personality-driven behavior, internal conflict;

- Politics: imperial favor, court dynamics, external forces...

The artistic will is precisely what makes *Dream of the Red Chamber* -- apart from the fact that it lacks a definitive ending -- an ideal prediction target.

Cao Xueqin embedded hints about the characters' fates throughout the novel, from the very beginning.

The most iconic example is the 判詞 (prophetic verses / judgment poems) of the 十二金釵 (Twelve Beauties of Jinling), which explicitly foreshadow the fates of the female lead and deuteragonist:

> 可嘆停機德，堪憐詠絮才。玉帶林中掛，金簪雪裡埋。

*(How lamentable, her virtue of halting the loom; how pitiable, her talent of chanting the willow catkins. A jade belt hangs in the forest; a golden hairpin lies buried in the snow.)*

### Rule Engine

Given the initial conditions and governing laws, how do we apply them?

The more ideal approach would be to build a 3D physics engine similar to a game engine, where each character possesses only the information they would know, and let an AI chatbot role-play each character like an actor performing a part.

But first, the cost would be too high and would only increase spectacle -- we would not be introducing new information, and the 3D engine would not produce new results.

Second, we are not running a wind-tunnel fluid dynamics simulation; we are trying to guess what Cao Xueqin had in mind. Staying at the textual level is sufficient for now.

Based on the previously extracted data, we derive a set of computational subjects and rules.

In practice, this is the traditional process of evaluating evidence, confidence, and additive/subtractive adjustments for whether an event occurs --

made systematic, repeatable, modifiable, and exhaustively brute-forced.

The simulation steps for each round are:

1. Process delayed effects -- check pending\_effects; apply any that have reached their due chapter.

2. Evaluate all laws -- check each law's premises to see if all are satisfied (skip those with confidence \< 0.3).

3. Conflict resolution -- simultaneously triggered laws may contradict each other; adjudicate which one wins.

4. Apply effects -- those with a delay go into the queue; those without directly modify state.

5. Snapshot -- compress the current state into a numerical vector.

6. chapter += 1

A complete example -- the death of Lin Daiyu (林黛玉) in Chapter 98 -- is appended at the end of this article.

### Workflow Summary

Among the several components in the above workflow,

whether the **extracted data** is academically rigorous, whether the **rules** are reasonable and applicable, whether the **simulation steps** are sound --

none of this is critically important, because each part can be improved and regenerated independently.

From a software engineering perspective, my goal is to make this engine work well at the interface level,

and continuously refine prediction results as more information is incorporated and the methodology improves.

### Current Results: Objective vs. Subjective Parallel Comparison

Here I must introduce another self-imposed methodology to enable structured comparison:

dividing the inference engine's layers into two main parts -- objective conditions and artistic choice.

![](</images/Simulator Screenshot - iPhone 17 - 2026-03-30 at 22.45.27.png>)![](</images/Simulator Screenshot - iPhone 17 - 2026-03-30 at 22.45.20.png>)

#### Objective Conditions

The historical backdrop of the era in which the novel was written -- its characters, settings, feudal system, economy, and so on -- constitutes the first layer of objective conditions. This can delimit the entire scope of what the story is capable of containing. We have already extracted some objective laws based on period-appropriate historical context and academic literature.

Conversely, anything that actually existed in that era could, in theory, appear and influence the story.

For instance, the novel already features some Western modern objects such as self-striking clocks and pocket watches. What if Western firearms appeared and became a significant plot driver?

Exhaustively exploring such first-layer objective possibilities is a direction for future work, and might achieve an effect that is "within reason yet beyond expectation."

#### Artistic Choice

The second layer is the author Cao Xueqin's (曹雪芹) cultivation of this fictional world.

Many characters and the overall trajectory of the family carry a heavy fatalistic coloring.

The novel's countless poems and metaphors -- as well as marginal annotations by a friend who reportedly read the ending -- hint at this.

Therefore, we can use the author's background and life experiences

to infer what fates he chose for his characters,

and thereby reveal the values he truly wished to express.

#### Cross-Comparison

From here, we can treat the Gao E (高鶚) continuation as the work of the most advanced "player" to date.

What he did is essentially the same thing I am doing now:

based on the characters and setting in the novel, attempting to divine Cao Xueqin's artistic choices as closely as possible.

Moreover, Gao E completed the existing ending, which greatly increased the novel's circulation, and his version has been widely accepted -- so we place his version in a parallel position for comparison.

#### Realistic Simulation

What if we stripped away all artistic treatment and retained only objective laws, letting the story evolve naturally?

The result is that most plot events would not occur within the span of 120 chapters. The narrative would be less dramatic and contain fewer tragedies.

## Methods for Improving Prediction Quality

- Re-extract text when LLM capabilities improve

- More human intervention for fine-tuning and experimenting with different prompts

- Enlist scholars of Redology (紅學, the academic study of *Dream of the Red Chamber*) or historians to assist with data cleaning and engine logic adjustments

- Incorporate newly discovered or previously undigitized materials (if any) into training

- Experiment with alternative methodologies

- Establish a fixed workflow and let AI agents continuously fine-tune and produce many versions; since there is no clear termination criterion, quality can only be judged manually

## Conclusion

Due to the constraints of existing and pre-trained data, and the strong internal consistency of *Dream of the Red Chamber* as a work of art,

deus ex machina predictions are unlikely to emerge. What we see instead are internal comparative differences --

for example, the confiscation and decline of the Jia family is fated to happen regardless; the difference lies only in timing.

### A Final Reflection

This kind of work would originally have required at least one to two years and at least one full-time person to complete.

Now I can use my after-work hours to play a different professional role -- which also satisfies a regret from when financial pressure forced me to switch fields years ago.

I hope that sharing the thinking process behind building the *Dream of the Red Chamber Simulator* is helpful to you,

and I look forward to the social sciences -- not just computer science and the natural sciences -- benefiting from the rapid advances in AI.

***

### Appendix: Full Simulation Process Example

Chapters 97-98, "The Death of Lin Daiyu" (黛玉之死) -- a complete walk-through of all six steps (the following content was generated by AI):

---

Example: Chapter 97 -- The Switcheroo Plot (掉包計) -> Burning Manuscripts and Severing Ties (焚稿斷情) -> Daiyu's Death

Background State (entering Chapter 97)

After more than a dozen chapters of cumulative decline, Lin Daiyu's state is:

agent.林黛玉:  health=0.12, mood=0.08, isolation=0.72, tragedy\_risk=0.95, alive=True

agent.賈寶玉:  monk\_tendency=0.35, mood=0.20

economy:       debt\_ratio=0.65

politics:      family\_decides\_marriage=True

relation.賈寶玉::林黛玉:    marriage\_probability=0.15

relation.賈寶玉::薛寶釵:    marriage\_probability=0.72

Why did Daiyu's health drop from an initial 0.35 to 0.12? Because this law has been silently triggering every chapter:

▎ PSY\_E1\_DAIYU\_DECAY "Daiyu's health slowly decays"

▎ Premise: health > 0.0 AND isolation > 0.3 AND alive = True -> Effect: health sub 0.017

▎ At -0.017 per chapter, over a dozen chapters this amounts to a lethal chronic drain.

---

① Process Delayed Effects

Check the pending\_effects queue. Suppose the following was triggered in Chapter 13:

▎ FATE\_010 "Qin Keqing's deathbed dream: the peak foretells the fall" delay\_chapters: 20

Its effect, economy.spending\_pressure add 0.1, already came due and was executed in Chapter 33. The queue is now empty. Skip.

---

② Evaluate All 369 Laws

The engine scans each law in sequence. The key laws that trigger this chapter:

Law A -- VAR\_MARRIAGE\_SWAP "The Switcheroo: Secretly marrying Baochai instead" conf=0.95

Premise check:

```
agent.林黛玉.health \< 0.15       -> 0.12 \< 0.15  ✅

agent.林黛玉.alive == True        -> True          ✅

politics.family\_decides\_marriage  -> True          ✅

relation.寶玉::黛玉.marriage\_probability \< 0.5  -> 0.15 \< 0.5  ✅

All passed -> 🔥 Triggered!
```

Law B -- PSY\_E1\_DAIYU\_DECAY "Daiyu's health decay" conf=0.9

```
health > 0.0  -> 0.12 > 0  ✅

isolation > 0.3 -> 0.72 > 0.3  ✅

alive == True  ✅

-> 🔥 Triggered!
```

Law C -- VAR\_MARRIAGE\_DAIYU "The Stone-and-Wood Bond: Baoyu and Daiyu marry" conf=0.9

```
relation.寶玉::黛玉.marriage\_probability > 0.7  -> 0.15 > 0.7  ❌

-> Not triggered (Baoyu-Daiyu marriage probability too low)
```

This chapter also simultaneously triggers over a dozen other laws (economic decline, political risk, etc.), but the above are the ones directly relevant to Daiyu.

---

③ Conflict Resolution

VAR\_MARRIAGE\_SWAP, VAR\_MARRIAGE\_NORMAL\_BAOCHAI, and VAR\_MARRIAGE\_DAIYU belong to the same variant\_group (marriage outcomes are mutually exclusive).

Only VAR\_MARRIAGE\_SWAP passed the premise check, so there is no actual conflict. However, if Daiyu were already dead (alive=False), then VAR\_MARRIAGE\_NORMAL\_BAOCHAI would trigger instead of the switcheroo version --

that would be a different evolutionary path.

PSY\_E1\_DAIYU\_DECAY's effect is additive (sub), so it does not conflict with other laws. All effects are retained.

---

④ Apply Effects

Law A's effects execute immediately (delay=0):

marriage trigger\_event BAOYU\_MARRIED\_BAOCHAI   -> fate\_flags\["BAOYU\_MARRIED\_BAOCHAI"] = True

relation.寶玉::寶釵.marriage\_probability set 1.0  -> 1.0

agent.賈寶玉.mood sub 0.5                        -> 0.20 -> 0.00 (clamp)

agent.賈寶玉.monk\_tendency add 0.3               -> 0.35 -> 0.65

agent.林黛玉.health sub 0.1                       -> 0.12 -> 0.02

Law B's effects:

agent.林黛玉.health sub 0.017                    -> 0.02 -> 0.003

At this point Daiyu's health = 0.003, approaching zero.

---

⑤ Snapshot

Compress the current world state into a numerical vector:

snapshot = {

```
economy\_vector: \[0.42, 0.82, 0.65, 0.55, 0.80, 0.35],

agent\_vectors: {

  "林黛玉": \[0.003, 0.08, 0.10, 0.00, 0.30, 0.00, 0.72, 0.95],

  "賈寶玉": \[0.80, 0.00, 0.30, 0.72, 0.80, 0.65, 0.42, 0.92],

  ...

},

politics\_vector: \[0.0, 0.60, 0.75]
```

}

This vector will later be compared via Euclidean distance against the actual vector for Chapter 97 in actual\_checkpoints.json.

---

⑥ chapter = 98

Enter the next chapter. At this point Daiyu's health = 0.003, and BAOYU\_MARRIED\_BAOCHAI = True.

When Chapter 98 runs step ② again, two lethal laws trigger simultaneously:

▎ VAR\_DAIYU\_HEARTBREAK "Burning manuscripts, severing ties: Daiyu dies of heartbreak" conf=0.95

▎ health ≤ 0.05        -> 0.003 ≤ 0.05   ✅

▎ BAOYU\_MARRIED\_BAOCHAI -> True           ✅

▎ -> death trigger\_event FATE\_DAIYU\_DEATH

▎ -> monk\_tendency add 0.4 -> Baoyu 0.65 -> 1.0 (clamp)

▎ -> alive set False

Then SYS\_E19\_ZERO\_DAIYU triggers (checkpoint.FATE\_DAIYU\_DEATH = True), zeroing out all of Daiyu's attributes.

A few chapters later, Baoyu's monk\_tendency has reached 1.0 and mood ≤ 0.15, triggering VAR\_MONK\_DESPAIR "All hopes extinguished: Baoyu renounces the world" (萬念俱灰：寶玉出家).
