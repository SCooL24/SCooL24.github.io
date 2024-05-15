---
layout: home
title: Invited Speakers
---

Speaker: [Kim Guldstrand Larsen](https://kgl.cs.aau.dk/)

Title: Shielded Reinforcement Learning for Safe and Optimal Cyber Physical Systems

Abstract:
I will present recent advances and applications of the tool UPPAAL Stratego (www.uppaal.org) supporting automatic synthesis of guaranteed safe and near-optimal control strategies for cyber physical systems. UPPAAL Stratego support reinforcement learning methods to construct near-optimal controller. However, thir behavior is not guaranteed to be safe, even when it is encouraged by reward engineering. One way of imposing safety to a learned controller is to use a safety shield, synthesized using symbolic methods from checking, and hence  correct by design. To make synthesis of shields for hybrid environments tractable UPPAAL Stratego are using various abstraction techniques for hybrids systems.

We study the impact of the synthesized shield when applied as either a pre-shield (applied before learning a controller) or a post-shield (only applied after learning a controller). In addition trade-offs between efficiency of strategy representation and degree of optimality subject to safety constraints will be discussed, as well as successful on-going applications (water-management, heating systems, and traffic control).

---------------------------------------------------------------------------------------------------------------------------

Speaker: [Azalea Raad](https://www.soundandcomplete.org/index.html) 

Title: Bug Detection at Scale

Abstract:  Incorrectness Logic (IL) has recently been advanced as a logical under-approximate theory for proving the presence of bugs--dual to Hoare Logic, which is an over-approximate theory for proving the absence of bugs. To facilitate scalable bug detection, we developed incorrectness separation logic (ISL) by marrying the under-approximate reasoning of IL with the local reasoning of separation logic. This locality leads to techniques that are compositional both in code (concentrating on a program component) and in the resources accessed (spatial locality), without tracking the entire global state or the global program within which a component sits. This enables reasoning to scale to large teams and codebases: reasoning can be done even when a global program is not present. To demonstrate this, we developed Pulse, an automatic program analysis for catching memory safety errors, underpinned by ISL. Using Pulse, deployed at Meta, we found a number of real bugs in large codebases such as OpenSSL.

Inspired by this success, we later studied the power of under-approximation for detecting non-termination bugs. Program termination is a classic non-safety property that cannot in general be witnessed by a finite trace. This makes testing for non-termination challenging, and also makes it a natural target for symbolic proof.  Discovering non-termination is an under-approximate problem. We thus developed an under-approximate logic for proving non-termination, resulting in a compositional proof method. We prototyped this in an automated tool, Pulse∞ (an extension of Pulse), which has already discovered a number of non-termination bugs in large open-source libraries.
