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

--------------------------------------------------------------------------------------------------------------------------

Speaker: [Bernd Finkbeiner](https://cispa.de/en/people/finkbeiner)

Title: Hyperproperties: the exciting world beyond k-hypersafety

Abstract: System requirements related to concepts like information flow, knowledge, and robustness cannot be judged in terms of individual system executions, but rather require an analysis of the relationship between multiple executions. Such requirements belong to the class of hyperproperties, which generalize classic trace properties to properties of sets of traces. 

A key idea in the verification of hyperproperties has been to analyze self-compositions of programs. Hyperproperties that need to hold for all possible combinations of k traces, such as k-hypersafety properties, can be analyzed as standard trace properties of the k-fold self-composition. The implicit universal quantification over the traces is, however, an inherent limitation of this paradigm, which makes it difficult to abstract in an existential manner from phenomena like scheduling in concurrent programs, nondeterministic choice, or speed of execution in asynchronous computations. Alternations between quantifiers are furthermore essential for counterfactual reasoning about causation and blame.

In this talk, we will explore the exciting world of hyperproperties beyond k-hypersafety. I will discuss the decidability and complexity of reasoning about such hyperproperties and present algorithmic techniques for the effective resolution of quantifier alternations. I will also give an overview of recently introduced logics for the specification of hyperproperties beyond k-hypersafety, including logics that combine hyperproperties with reasoning over strategies, and logics for second-order hyperproperties.