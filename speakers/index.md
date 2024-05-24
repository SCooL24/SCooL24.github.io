---
layout: home
title: Invited Speakers
---

Speaker: [Bernd Finkbeiner](https://cispa.de/en/people/finkbeiner)

Title: Hyperproperties: the exciting world beyond k-hypersafety

Abstract: System requirements related to concepts like information flow, knowledge, and robustness cannot be judged in terms of individual system executions, but rather require an analysis of the relationship between multiple executions. Such requirements belong to the class of hyperproperties, which generalize classic trace properties to properties of sets of traces. 

A key idea in the verification of hyperproperties has been to analyze self-compositions of programs. Hyperproperties that need to hold for all possible combinations of k traces, such as k-hypersafety properties, can be analyzed as standard trace properties of the k-fold self-composition. The implicit universal quantification over the traces is, however, an inherent limitation of this paradigm, which makes it difficult to abstract in an existential manner from phenomena like scheduling in concurrent programs, nondeterministic choice, or speed of execution in asynchronous computations. Alternations between quantifiers are furthermore essential for counterfactual reasoning about causation and blame.

In this talk, we will explore the exciting world of hyperproperties beyond k-hypersafety. I will discuss the decidability and complexity of reasoning about such hyperproperties and present algorithmic techniques for the effective resolution of quantifier alternations. I will also give an overview of recently introduced logics for the specification of hyperproperties beyond k-hypersafety, including logics that combine hyperproperties with reasoning over strategies, and logics for second-order hyperproperties.

--------------------------------------------------------------------------------------------------------------------------

Speaker: [Kim Guldstrand Larsen](https://kgl.cs.aau.dk/)

Title: Shielded Reinforcement Learning for Safe and Optimal Cyber Physical Systems

Abstract:
I will present recent advances and applications of the tool UPPAAL Stratego (www.uppaal.org) supporting automatic synthesis of guaranteed safe and near-optimal control strategies for cyber physical systems. UPPAAL Stratego support reinforcement learning methods to construct near-optimal controller. However, thir behavior is not guaranteed to be safe, even when it is encouraged by reward engineering. One way of imposing safety to a learned controller is to use a safety shield, synthesized using symbolic methods from checking, and hence  correct by design. To make synthesis of shields for hybrid environments tractable UPPAAL Stratego are using various abstraction techniques for hybrids systems.

We study the impact of the synthesized shield when applied as either a pre-shield (applied before learning a controller) or a post-shield (only applied after learning a controller). In addition trade-offs between efficiency of strategy representation and degree of optimality subject to safety constraints will be discussed, as well as successful on-going applications (water-management, heating systems, and traffic control).

------------------------------------------------------------------------------------------------------------------------------

Speaker: [Brigitte Pientka](https://www.cs.mcgill.ca/~bpientka/)

Title: Mechanizing Session-Types: Challenges and Lessons Learned

Abstract: Process calculi provide a tool for the high-level description of interactions, communications, and synchronizations between a collection of independent processes. Session types allow us to statically  verify that processes communicate according to prescribed protocols.  Hence, they rule  out a wide class of communication-related bugs before executing a given process. They also statically guarantee safety properties such as session fidelity and deadlock freedom, analogous to preservation and progress in the simply typed lambda-calculus.

Although there have been many efforts to mechanize process calculi such as the pi-calculi in proof assistants, mechanizing these systems  remains an art.  Process calculi use channel or action names to specify process interactions, and they often feature rich binding structures and semantics such as channel mobility. Both of these features can be challenging to mechanize, for we must track names to avoid conflicts, ensure that \alpha-equivalence and renaming are well-defined, etc. Moreover, session types employ a linear type system, where variables cannot be  implicitly copied or dropped, and therefore, many mechanizations of these systems require modeling the context and carefully ensuring that its variables are handled linearly.

In this talk, I give an introduction to the challenges that arise when mechanizing session types, and showcase two different kinds of solutions focusing on a session typed system based on classical linear logic: first, I show how to mechanize the a session tysystem directly using explicit contexts identifying key context operations to manage linear contexts; then I show a technique to localize linearity conditions as additional predicates embedded within type judgments, which allows us to use unrestricted typing contexts instead of linear ones. This latter technique is especially relevant when leveraging (weak) higher-order abstract syntax to defer the intricate channel mobility and bindings that arise in a session typed system. 

From this mechanization, we discuss key design decisions and draw some key lessons for mechanizing substructural systems, such as session types. The goal of this talk is to engage the community in  discussions on what support in proof environments is needed to support the mechanization of substructural systems.

This is joint work with Chuta Sano, Daniel Zackon, Ryan Kavanagh, and Alberto Momigliano.

---------------------------------------------------------------------------------------------------------------------------

Speaker: [Azalea Raad](https://www.soundandcomplete.org/index.html) 

Title: Bug Detection at Scale

Abstract:  Incorrectness Logic (IL) has recently been advanced as a logical under-approximate theory for proving the presence of bugs--dual to Hoare Logic, which is an over-approximate theory for proving the absence of bugs. To facilitate scalable bug detection, we developed incorrectness separation logic (ISL) by marrying the under-approximate reasoning of IL with the local reasoning of separation logic. This locality leads to techniques that are compositional both in code (concentrating on a program component) and in the resources accessed (spatial locality), without tracking the entire global state or the global program within which a component sits. This enables reasoning to scale to large teams and codebases: reasoning can be done even when a global program is not present. To demonstrate this, we developed Pulse, an automatic program analysis for catching memory safety errors, underpinned by ISL. Using Pulse, deployed at Meta, we found a number of real bugs in large codebases such as OpenSSL.

Inspired by this success, we later studied the power of under-approximation for detecting non-termination bugs. Program termination is a classic non-safety property that cannot in general be witnessed by a finite trace. This makes testing for non-termination challenging, and also makes it a natural target for symbolic proof.  Discovering non-termination is an under-approximate problem. We thus developed an under-approximate logic for proving non-termination, resulting in a compositional proof method. We prototyped this in an automated tool, Pulse∞ (an extension of Pulse), which has already discovered a number of non-termination bugs in large open-source libraries.
