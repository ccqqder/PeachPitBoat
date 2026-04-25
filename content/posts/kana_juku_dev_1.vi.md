---
isStub: true
title: "Kana Juku Dev Log (Part 1): From Chatbots to AI Agents"
date: 2026-02-22T13:16:34.278Z
author: "QQder"
categories:
  - The Workshop
tags:
  - iOS App
  - On-Device AI
  - Handwriting Recognition
  - udemy
  - claude
  - claude code
  - gemini
  - gemini cli
  - swiftUI
  - UIKit
keywords:
  - AI agent
  - claude code
  - gemini cli
  - iOS development
  - indie developer
  - kana juku
  - Japanese learning
  - swiftUI
  - On-Device AI
  - opus
  - chatbot
description: "Sharing my experience developing my first app, Kana Juku — a journey that also traces my shift from chatbots to AI agents"
---

# Preface

Kana Juku is the first app I ever built and shipped to the App Store.

Since it was my first, there's a full story arc to share.

This series covers the development process, how I used AI assistance and how that evolved, working with public datasets and copyright considerations, and more.

If other apps have noteworthy stories, I'll publish those separately.

This post focuses on the transition from chatbots to AI agents starting in **Q4 2025**.

Things move fast in this space, so I've bluntly timestamped the key moments.

## About the App

If you have an Apple device, feel free to download it and give it a try.

Several upcoming posts will also use this app as a running example — topics like cleaning [ETL datasets](https://etlcdb.db.aist.go.jp/), [Apple Create ML](https://developer.apple.com/machine-learning/create-ml/), [PyTorch](https://pytorch.org/), [VOICEVOX](https://voicevox.hiroshiba.jp/), on-device large language models, and more.

Kana Juku: [URL](https://apps.apple.com/us/app/%E5%81%87%E5%90%8D%E7%A7%81%E5%A1%BE/id6756785942)

![](/images/IMG_2433.JPG)

***

# Development Timeline

### Motivation

My family and I are both interested in learning Japanese, and I've long wanted a Japanese-learning app that perfectly fits our needs.

My family's pain point is that they don't read English, so the romaji in most textbooks and apps is meaningless to them.

For me, I really wanted kana displayed alongside their kanji origins (e.g., "あ" derives from "安").

Another annoyance: I installed the Japanese keyboard for occasional use, but switching input methods every day meant an extra tap to skip past the Japanese keyboard — a small friction that added up.

### Early Preparation

**[Q4 2024]**

I was between jobs at the time, so I had the bandwidth to take [Udemy](https://www.udemy.com/) courses. Since I had some JavaScript experience, I started with [React](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih6Kzo2O-SAxUl3zQHHZoSL-kQFnoECDYQAQ&url=https%3A%2F%2Fzh-hant.legacy.reactjs.org%2F&usg=AOvVaw3Q6fqYyboB_gQOnPVX_tbN&opi=89978449) & [Expo](https://expo.dev/).

At this stage I was following along with course content — simple web-style pages, plus extras like GPS, camera control, and fetching remote data.

But since it wasn't Apple's native ecosystem, there was a lot of extra tooling to manage.

**[Q1 2025]**

After hesitating for a long time, I bought a Mac Mini and switched entirely to Apple's own SwiftUI. Again, I learned from Udemy courses.

Most of my time went into getting comfortable with basic UI components and layouts, plus all the fundamental features — data persistence, fetching data, embedding maps — and their SwiftUI equivalents.

SwiftUI is more modern and isn't as tightly coupled to Xcode as UIKit, but it's also harder to predict how a SwiftUI layout will actually look. Early on I cared too much about that and burned a lot of time experimenting.

**[Q3 2025]**

Since I had a day job and could only code in the evenings — and not every evening at that — progress was slow. I was basically building out the basic skeleton and plugging in the Japanese language data.

With a first app, it's hard to foresee the final shape, so I kept revising. Sometimes I'd circle back to rewatch course videos for features I now knew I needed. Essentially, I was paying tuition.

Up to this point, starting from **Q1 2024**, plain chatbots like ChatGPT were already a big help for coding.

But the copy-paste cycle and having to explain mountains of context was incredibly time-consuming. The output often missed the mark on the first try or drifted off course, sending me right back to the copy-paste loop. It never reached a positive feedback cycle — it was only useful as a learning reference.

At the time, the hottest tool was actually the Cursor editor with its tab-autocomplete, but it required a subscription for meaningful usage, so I **didn't try it**.

Meanwhile, Claude was already gaining popularity as the best model for coding, and Anthropic had released Claude Code — an AI agent that runs on your local machine. But again, it required a subscription, so I didn't try it.

***

### Pivoting to AI Agents

**[Q4 2025]**

At this point I expected I'd only ever subscribe to one chatbot at a time, and I had just switched from ChatGPT to Google Gemini.

Spec-Driven Development (SDD) was trending, and Google had launched Gemini CLI — their answer to Claude Code — so I finally **gave it a shot**.

I discovered that agents eliminated the copy-paste step entirely, massively boosting efficiency. The step of pasting code back and hunting for which lines to change was also gone.

By then I was convinced: for coding, you should use an agent, not a chatbot. So I went ahead and subscribed to Claude to use Claude Code (CC from here on).

CC's underlying model was clearly stronger. Its comprehension of conversations and its ability to execute as expected were already remarkably reliable.

#### Controlling the Computer, and Opus 4.5

One time my Mac Mini's disk was completely full and the machine was unusable. I just asked CC what to do — the same way I'd ask a question on a chatbot's web page.

CC came back with a concrete plan: which directories could be cleared, what could be moved to an external drive, and so on.

I was worried it might brick my computer, so I approved each step one at a time. In the end, everything went smoothly.

I wasn't very familiar with macOS or the Xcode build environment. That's when I realized AI has at least an 80% understanding of *everything* — including things I don't know — and that being able to write code is roughly equivalent to being able to operate a computer.

Because CC could directly control the machine, it moved freely between directories, wrote code, saw its own errors, and fixed them — a fully self-sustaining positive feedback loop.

The development speed with an agent was on a completely different level, and the fact that I'd waited three extra months before switching to CC made me feel pretty foolish.

The time wasted was staggering, both subjectively and objectively.

Subjectively: if I had adopted the latest tools earlier, the previous three months of work could have been done in two to three weeks.

Objectively: other people using the latest tools were more productive than me and shipping their products sooner.

My earlier refusal to try — saving maybe half an hour of setup time and a few hundred dollars in subscription fees — ended up wasting vast stretches of my life.

This might also explain why so many people are obsessed with chasing the latest AI product news.

At least that's how it is for me — I can't afford not to stay on top of the latest releases. It's a form of time-management risk hedging.

**[November 24, 2025]**

Opus 4.5 was released. Opus is Claude's highest-tier flagship model, and version 4.5 had just dropped.

Beyond significant performance improvements across the board compared to its predecessor, the biggest difference was its understanding of intent.

The old version essentially did exactly what you pointed at (which was already quite good, honestly). Starting with 4.5, after receiving your request, it would first summarize and plan to some degree. In human terms: it became sharper, more experienced.

You no longer needed to spell out which file to modify and how. You could describe the end goal like a manager or executive, and it would break it down and plan the next couple of steps on its own.

This planning capability boosted efficiency even further. As I mentioned, AI already knows at least 80% of everything — now it was proactively doing the next steps of work, and doing them well.

Combined with this, I was able to operate at a much higher level of abstraction. More and more was delegated to CC. Gradually, I stopped needing to read or edit code myself.

After Opus 4.5 came out, the debate on social media about whether AI can write code essentially ended.

For full-time software engineers and seasoned pros, I can't speak to their experience.

But compared to myself: things that would have taken me one to two years could now be done in two to three months.

The output settled at just beyond the edges of my own knowledge — I was actually the biggest bottleneck.

*End of Part 1*
