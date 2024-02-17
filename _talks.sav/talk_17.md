---
name: Foundations of team semantics.
title: Foundations of team semantics.
speakers: Fredrik Engstrom
categories: Talk
abstract: /ct/Engstrom.pdf
---
<p>Dependence logic, see [<a href="#vaananen">3</a>], and its relatives are defined using team semantics, in which formulas are satisfied by sets of assignments, teams, rather than single assignments. 
The team semantics construction is widely applicable and can be used to
understand notions from many different areas; model theory, game theory,
database theory, probabilistic reasoning and program verification, to name a
few. </p><p>The denotatiton of a first-order formula in classical Tarskian semantics is the set of assignments satisfying the formula, &#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">c</span></sub>. In team semantics it is the set of teams satisfying the formula, i.e., a set of sets of assignments, &#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">t</span></sub>. The standard team semantic construction is via the <em>flatness principle</em> according to which &#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">t</span></sub> = <span style="color:red"><span style="font-style:italic">P</span></span> (&#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">c</span></sub>). </p><p>This construction can, at least partially, be described using the free functor from the category of partially ordered monoids to the category of quantales, i.e., partially ordered monoids equipped with a complete semilattice structure, see [<a href="#abramsky">1</a>]. This functor maps the space of Tarskian denotations, <span style="color:red"><span style="font-style:italic">P</span></span> (<span style="font-style:italic">X</span><sup><span style="font-style:italic">V</span></sup>), where <span style="font-style:italic">X</span> is the domain and <span style="font-style:italic">V</span> a set of variables, into the space <span style="color:red"><span style="font-style:italic">H</span></span>(<span style="color:red"><span style="font-style:italic">P</span></span>(<span style="font-style:italic">X</span><sup><span style="font-style:italic">V</span></sup>)), the set of downwards-closed subsets of <span style="color:red"><span style="font-style:italic">P</span></span> (<span style="font-style:italic">X</span><sup><span style="font-style:italic">V</span></sup>). The embedding is based on the flatness principle in that &#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">t</span></sub> = <span style="color:red"><span style="font-style:italic">P</span></span> (&#x27E6; &#x3D5; &#x27E7;<sub><span style="font-style:italic">c</span></sub>). </p><p>However, the space of downwards-closed sets can not be used as the space of denotations for some logics: One example is the well-studied Independence logic, which isn&#x2019;t downward-closed; another is a logic constructed to handle branching of non-monotone generalized quantifiers, which isn&#x2019;t based on the flatness principle. I will in this talk revisit the description of the team semantic construction as the free functor from a more general perspective that also includes these logics.</p><!--TOC section id="sec1" References-->
<h2 id="sec1" class="section">References</h2><!--SEC END --><dl class="thebibliography"><dt class="dt-thebibliography">
<a id="abramsky">[1]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">Samson Abramsky &#xA0;&#xA0;Jouko V&#xE4;&#xE4;n&#xE4;nen</span>,
<span style="font-style:italic">From IF to BI</span>,
<span style="font-weight:bold"><span style="font-style:italic">Synthese</span></span>,
vol.&#xA0;167 (2009), pp.&#xA0;207&#x2013;230.</dd><dt class="dt-thebibliography"><a id="engstrom">[2]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">Fredrik Engstr&#xF6;m</span>,
<span style="font-style:italic">Generalized quantifiers in Dependence logic</span>,
<span style="font-weight:bold"><span style="font-style:italic">Journal of Logic, Language and Information</span></span>,
vol.&#xA0;21 (2012), pp.&#xA0;299&#x2013;324.</dd><dt class="dt-thebibliography"><a id="vaananen">[3]</a></dt><dd class="dd-thebibliography">
<span style="font-variant:small-caps">Jouko V&#xE4;&#xE4;n&#xE4;nen</span>,
<span style="font-weight:bold"><span style="font-style:italic">Dependence logic. A new approach to independence friendly logic</span></span>,
London Mathematical Society Student Texts, 
Cambridge University Press,
2007.</dd></dl><!--CUT END -->
<!--HTMLFOOT-->
<!--ENDHTML-->
<!--FOOTER-->
<hr style="height:2"><blockquote class="quote"><em>This document was translated from L<sup>A</sup>T<sub>E</sub>X by
</em><a href="http://hevea.inria.fr/index.html"><em>H</em><em><span style="font-size:small"><sup>E</sup></span></em><em>V</em><em><span style="font-size:small"><sup>E</sup></span></em><em>A</em></a><em>.</em></blockquote>
