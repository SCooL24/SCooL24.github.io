---
name: Special Session - Mogavero
speakers: Fabio Mogavero
title: Alternating (In)Dependence-Friendly Logic&#xA0;&#x2021;
categories:
  - Special Session
ss: true
session: csl
abstract: /sc/Mogavero.pdf
onsite: false
---
<p><em>Informational independence</em> is a phenomenon that emerges quite naturally
in <em>game theory</em>, as players in a game make moves based on what they know
about the state of the current play&#xA0;[<a href="#NM44">8</a>].
In games such as Chess or Go, both players have <em>perfect information</em>
about the current state of the play and the moves they and their adversary
have previously made.
For other games, like Poker and Bridge, the players have to make decisions
based only on <em>imperfect information</em> on the state of the play.
Given the tight connection between games and logics, think for instance at
<em>game-theoretic semantics</em>&#xA0;[<a href="#Lor61">5</a>, <a href="#Lor68">4</a>, <a href="#Hin73">1</a>], a number of
proposals have been put forward to reason with or about informational
independence, most notably, <em>Independence-Friendly Logic</em>&#xA0;[<a href="#HS89">2</a>],
<em>Dependence Logic</em>&#xA0;[<a href="#Vaa07">7</a>], and logics derived thereof.</p><p>Independence-Friendly Logic (IF) was originally introduced by Hintikka and
Sandu&#xA0;[<a href="#HS89">2</a>], and later extensively studied, emphe.g., in&#xA0;[<a href="#MSS11">6</a>], as an
extension of <em>First-Order Logic</em> (FOL) with informational independence
as first-class notion.
Unlike in FOL, where quantified variables always functionally depend on all
the previously quantified ones, the values for quantified variables in IF can
be chosen independently of the values of specific variables quantified before
in the formula.
From a general game-theoretic viewpoint, however, the IF semantics exhibits
some limitations.
It treats the players asymmetrically, truly allowing only one of the two
players to have imperfect information. In addition, sentences of the logic can
only encode the existence of a uniform winning strategy for one of the two
players and, as a consequence, IF does admit undetermined sentences, which
are neither true nor false.</p><p>In this talk I will present an extension of IF, called <em>Alternating
(In)Dependence Friendly Logic</em> (ADIF), tailored to overcome these limitations
and that appears more adequate when reasoning about games with full imperfect
information is the main concern.
To this end, we introduce a novel compositional semantics, generalising
Hodges&#x2019; semantics for IF based on trumps/teams&#xA0;[<a href="#Hod97a">3</a>, <a href="#Vaa07">7</a>, <a href="#MSS11">6</a>],
which
</p><ol class="enumerate" type=1><li class="li-enumerate">
allows for restricting the two players, aiming at describing both
symmetric and asymmetric imperfect information games,
</li><li class="li-enumerate">recovers the law of excluded middle for sentences, and
</li><li class="li-enumerate">grants ADIF the full descriptive power of <em>Second Order Logic</em>.
</li></ol><p>
We also provide both an equivalent Herbrand-Skolem semantics and a
game-theoretic semantics for the prenex fragment of ADIF, the latter being
defined in terms of a determined infinite-duration game that precisely
captures the compositional semantics on finite structures.</p><!--TOC section id="sec1" References-->
<h2 id="sec1" class="section">References</h2><!--SEC END --><dl class="thebibliography"><dt class="dt-thebibliography">
<a id="Hin73">[1]</a></dt><dd class="dd-thebibliography">
J.&#xA0;Hintikka.
<em>Logic, Language-Games and Information: Kantian Themes in the
Philosophy of Logic.</em>
Oxford University Press, 1973.</dd><dt class="dt-thebibliography"><a id="HS89">[2]</a></dt><dd class="dd-thebibliography">
J.&#xA0;Hintikka and G.&#xA0;Sandu.
Informational Independence as a Semantical Phenomenon.
In <em>ICLMPS&#x2019;89</em>, pages 571&#x2013;589. Elsevier, 1989.</dd><dt class="dt-thebibliography"><a id="Hod97a">[3]</a></dt><dd class="dd-thebibliography">
W.&#xA0;Hodges.
Compositional Semantics for a Language of Imperfect Information.
<em>LJIGPL</em>, 5(4):539&#x2013;563, 1997.</dd><dt class="dt-thebibliography"><a id="Lor68">[4]</a></dt><dd class="dd-thebibliography">
K.&#xA0;Lorenz.
Dialogspiele als Semantische Grundlage von Logikkalk&#xFC;len.
<em>AMLG</em>, 11:32&#x2013;55, 1968.</dd><dt class="dt-thebibliography"><a id="Lor61">[5]</a></dt><dd class="dd-thebibliography">
P.&#xA0;Lorenzen.
Ein Dialogisches Konstruktivit&#xE4;tskriterium.
In <em>SFM&#x2019;59</em>, pages 193&#x2013;200. PWN, 1961.</dd><dt class="dt-thebibliography"><a id="MSS11">[6]</a></dt><dd class="dd-thebibliography">
A.L. Mann, G.&#xA0;Sandu, and M.&#xA0;Sevenster.
<em>Independence-Friendly Logic - A Game-Theoretic Approach.</em>
CUP, 2011.</dd><dt class="dt-thebibliography"><a id="Vaa07">[7]</a></dt><dd class="dd-thebibliography">
J.A. V&#xE4;&#xE4;n&#xE4;nen.
<em>Dependence Logic: A New Approach to Independence Friendly
Logic.</em>, volume&#xA0;70 of <em>London Mathematical Society Student Texts.</em>
CUP, 2007.</dd><dt class="dt-thebibliography"><a id="NM44">[8]</a></dt><dd class="dd-thebibliography">
J.&#xA0;von Neumann and O.&#xA0;Morgenstern.
<em>Theory of Games and Economic Behavior.</em>
Princeton University Press, 1944.</dd></dl><p>&#x2021;&#xA0;Joint work with Dylan Bellier, Massimo Benerecetti, and Dario Della
Monica.</p><!--CUT END -->
<!--HTMLFOOT-->
<!--ENDHTML-->
<!--FOOTER-->
<hr style="height:2"><blockquote class="quote"><em>This document was translated from L<sup>A</sup>T<sub>E</sub>X by
</em><a href="http://hevea.inria.fr/index.html"><em>H</em><em><span style="font-size:small"><sup>E</sup></span></em><em>V</em><em><span style="font-size:small"><sup>E</sup></span></em><em>A</em></a><em>.</em></blockquote>
