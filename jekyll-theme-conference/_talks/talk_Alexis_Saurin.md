---
name: Special Session - Saurin
speakers: Alexis Saurin
title: On the dynamics of cut-elimination for circular and non-wellfounded proofs
categories:
  - Special Session
ss: true
session: csl
abstract: /sc/Saurin.pdf
onsite: true
---
<p>In this talk, I will consider the structural proof theory of
fixed-point logics and their cut-elimination
theorems, focusing on their computational content. </p><p>More specifically, I will consider logics with least and
greatest fixed-points, expressing inductive and coinductive
properties, and proof systems for those logics 
admitting &#x201C;circular&#x201D; and non-wellfounded
proofs&#xA0;[<a href="#bouncing22">1</a>, <a href="#mumall16">2</a>, <a href="#fortier13">4</a>, <a href="#santo02">5</a>].
Those derivations are finitely branching but admit infinitely
deep branches, possibly subject to some regularity conditions.
Circular derivations are closely related with
proofs by infinite descent&#xA0;[<a href="#broth11">3</a>] and shall be equipped with a
global condition preventing vicious circles in proofs.</p><p>In order to unveil the computational content of those logical systems,
I will concentrate on linear logic
extended with least and greatest fixed points (&#xB5;<span style="font-family:sans-serif"><span style="font-style:italic">LL</span></span>),
that is, on the &#xB5;-calculus considered
in a linear setting, where the structural rules of contraction
and weakening are prohibited (or carefully controlled at least).
In particular, following the spirit of structural proof-theory
and of the Curry-Howard correspondence, we will be interested
not only in the structure of provability but also in the
structure of proofs themselves, corresponding to programs (while
formulas correspond to data and codata types).
</p><p>I will first introduce the non-wellfounded proof systems
for &#xB5;<span style="font-family:sans-serif"><span style="font-style:italic">LL</span></span> and for its exponential-free fragment,
&#xB5;<span style="font-family:sans-serif"><span style="font-style:italic">MALL</span></span> (that is, multiplicative and additive linear
logic with least and greatest fixed points).
After establishing cut-elimination for &#xB5;<span style="font-family:sans-serif"><span style="font-style:italic">MALL</span></span>&#xA0;[<a href="#mumall16">2</a>], I
will show how to generalize the cut-elimination result to 
&#xB5;<span style="font-family:sans-serif"><span style="font-style:italic">LL</span></span> (as well as to the intuitionistic and
classical non-wellfounded sequent calculi).
After that, I will discuss limitations of the validity condition
considered above, from a computational perspective, and introduce
a more flexible validity condition, called bouncing-validity&#xA0;[<a href="#bouncing22">1</a>],
and establish a cut-elimination theorem for this richer system which,
while proving the same theorems, admits more valid proofs that is,
through the bridge of the Curry-Howard correspondence, more programs.
</p><!--TOC section id="sec1" References-->
<h2 id="sec1" class="section">References</h2><!--SEC END --><dl class="thebibliography"><dt class="dt-thebibliography">
<a id="bouncing22">[1]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">David Baelde, </span><span style="font-variant:small-caps">Amina
Doumane</span><span style="font-variant:small-caps">, </span><span style="font-variant:small-caps">Denis Kuperberg</span><span style="font-variant:small-caps">, </span><span style="font-variant:small-caps">and</span><span style="font-variant:small-caps"> </span><span style="font-variant:small-caps">Alexis Saurin</span>,
<span style="font-style:italic">Bouncing Threads for Circular and Non-wellfounded
Proofs &#x2013; Towards Compositionality with Circular Proofs</span>,
<span style="font-weight:bold"><span style="font-style:italic">To appear in 37th Annual ACM/IEEE Symposium on Logic in Computer Science, LICS 2022</span></span>
(Haifa, Israel), 2022.
long version of the present paper,
available at https://hal.archives-ouvertes.fr/hal-03682126.</dd><dt class="dt-thebibliography"><a id="mumall16">[2]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">David Baelde, Amina Doumane, and Alexis Saurin</span>,
<span style="font-style:italic">Infinitary
Proof Theory: the Multiplicative Additive Case</span>,
<span style="font-weight:bold"><span style="font-style:italic">In 25th EACSL Annual Conference on Computer Science Logic, CSL 2016</span></span>
(Marseille, France),
(LIPIcs), Vol. 62. Schloss Dagstuhl -
Leibniz-Zentrum fuer Informatik, 42:1-42:17.
http://www.dagstuhl.de/dagpub/978-3-95977-022-4</dd><dt class="dt-thebibliography"><a id="broth11">[3]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">James Brotherston and Alex Simpson</span>,
<span style="font-style:italic">Sequent Calculi for Induction and Infinite Descent</span>,
<span style="font-weight:bold"><span style="font-style:italic">Journal of Logic and Computation</span></span>,
vol.&#xA0;21 (2011), no.&#xA0;6, pp.&#xA0;1177&#x2013;1216.</dd><dt class="dt-thebibliography"><a id="fortier13">[4]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">J&#xE9;r&#xF4;me Fortier and Luigi Santocanale</span>,
<span style="font-style:italic">Cuts for Circular Proofs: Semantics and Cut-elimination</span>,
<span style="font-weight:bold"><span style="font-style:italic">Computer Science Logic 2013 (CSL 2013), CSL 2013</span></span>
(Torino, Italy),
(Simona Ronchi Della Rocca, editor),
(LIPIcs), , Vol. 23. Schloss Dagstuhl - Leibniz-Zentrum
fuer Informatik, 2013, 248-262.</dd><dt class="dt-thebibliography"><a id="santo02">[5]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">Luigi Santocanale</span>,
<span style="font-style:italic">A Calculus of Circular Proofs and Its Categorical Semantics</span>,
<span style="font-weight:bold"><span style="font-style:italic">Foundations of Software Science and Computation
Structures</span></span>,
(Mogens Nielsen and Uffe Engberg, editors),
vol.&#xA0;2303,
Lecture Notes in Computer Science, Springer,
2002,
pp.&#xA0;357&#x2013;371</dd></dl><!--CUT END -->
<!--HTMLFOOT-->
<!--ENDHTML-->
<!--FOOTER-->
<hr style="height:2"><blockquote class="quote"><em>This document was translated from L<sup>A</sup>T<sub>E</sub>X by
</em><a href="http://hevea.inria.fr/index.html"><em>H</em><em><span style="font-size:small"><sup>E</sup></span></em><em>V</em><em><span style="font-size:small"><sup>E</sup></span></em><em>A</em></a><em>.</em></blockquote>
