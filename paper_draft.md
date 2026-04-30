---
title: "What AI Can’t Reconstruct: 
A Comparative Analysis of Pop Songs and Their AI-Generated Reconstructions"
author: "Yichong Zhang"
date: "Music 159r · Analyzing Popular Music after 2000 · Prof. Michèle Duguay · Spring 2026"
mainfont: "Times New Roman"
fontsize: 12pt
linestretch: 2.0
geometry: margin=1in
colorlinks: true
urlcolor: blue
linkcolor: black
---

\begin{abstract}
\noindent Listener-perception work shows that people can distinguish AI-generated music in controlled pairwise settings, and that explanations often cluster around vocal and technical cues (Figueiredo et al.\ 2025). This paper maps that perceptual gap onto production decisions. Using Moore's (2012) sound-box, textural-layer, and formal-functional vocabulary, I close-read four AI reconstructions: three Suno versions of Olivia Rodrigo's \emph{drivers license}, built on close-mic intimacy, an instrumentally stripped bridge, and a long reverb-tail outro; and one Suno version of Taylor Swift's \emph{Love Story}, treated as a country-pop control. The control lands closer to its template. The \emph{drivers license} reconstructions keep the bridge above surrounding choruses, make Verse 1 louder/brighter than the original, and replace slow outro dissolution with a near-hard cut. I use \emph{centroid pull} as a descriptive label for this observed pattern: centroid-distant production choices repeatedly move toward typical pop defaults.
\end{abstract}

\vspace{0.6em}

\noindent\textbf{Project repository:} \url{https://github.com/ET823828/AI-music-generation}

\vspace{0.6em}

# Introduction

Commercial AI music generators have moved quickly from novelty to near-professional pop. In this project, Suno v5.5 produced coherent tracks from text prompts, while research systems such as Google's MusicLM (Agostinelli et al. 2023) and Meta's MusicGen (Copet et al. 2023) establish the broader text-to-music paradigm. Yet Figueiredo et al. (2025), using a randomized controlled crossover design with author-uncontrolled Suno stimuli, show that listeners can distinguish AI music, especially when pairs are similar, and that their explanations often focus on vocal and technical cues.

The workflow is a **describe-and-reconstruct experiment**. I select Olivia Rodrigo's *drivers license* (2021, prod. Daniel Nigro) as a stress-test case: a chart-topping record whose close vocal, instrumental subtraction, and extended reverb-tail outro sit far from the mainstream-pop defaults audible in the retained generations. I describe the original with course vocabulary, paraphrase the lyrics, generate AI reconstructions, and analyze each output with the same toolkit.

I use *centroid pull* descriptively, not as a proven mechanism. In prompt-conditioned generative systems, outputs are sampled from, or otherwise generated under, learned distributions (Copet et al. 2023; Agostinelli et al. 2023). Here, *centroid* is shorthand for recurring production norms audible across the outputs: mastered loudness, filled mid-frequency texture, polished mid-distance vocal staging, and the verse–pre-chorus–chorus template.

The thesis is that the divergences between the AI reconstructions of *drivers license* and the original, distributed across vocal proximity, dynamic restraint, mix density, bridge structure, and outro design, are best understood as one systematic offset projected through five dimensions. For contrast, I treat *Love Story* as centroid-typical: its production design aligns with a familiar mainstream country-pop crossover template. The analytical work remains grounded in course tools — formal function, textural layers, sound-box space, vocal staging, timbre, and section-level energy — and uses machine-learning language only as a shorthand for patterns those tools make audible.

The project contributes a close-reading account of an AI perceptual gap: it projects that gap onto five Moore-style production dimensions, compares a centroid-distant song with a template-conforming control, and uses Suno v4.5/YuE comparisons to bound the claim beyond one v5.5 output.

---

# Selecting *drivers license* as a Centroid-Distant Stress Test

*drivers license* held the Billboard Hot 100 No. 1 position for eight weeks (Trust 2021) and broke Spotify's single-day non-holiday streaming record on release (Spotify 2026). Commercially, it is mainstream pop. Sonically, however, it depends on production choices that mainstream pop typically does not employ: silence over fill, a single sustaining piano over layered synths, and a vocal proximity close enough that breath becomes part of the texture. Its hit status therefore rests on conventions that depart from the contemporary chart-pop centroid.

This makes the song an ideal stress test. If text-to-music models pull centroid-distant decisions toward familiar defaults, *drivers license* should expose that pull; if the same pipeline works better on Taylor Swift's "Love Story" (2008, prod. Taylor Swift and Nathan Chapman; ProSoundNetwork Editorial Staff 2009), then the divergence is less likely generic inability and more likely a function of requested production design.

---

# Original Close-Reading and Prompt Design

## Five Production Dimensions

Following Moore's (2012) framework and Zagorski-Thomas's (2014) argument that record production should be a primary analytical object for popular music, I close-read *drivers license* across five dimensions.

**D1 — Vocal proximity.** Verses 1, 2, and 3 use close-mic ASMR staging: dry, breathy, barely processed voice, centered with minimal reverb. This proximity establishes intimacy as the song's baseline (Moore 2012, on vocal staging).

**D2 — Dynamic restraint.** Verse 1 is nearly empty: spare upright piano plus breath. The bridge, by contrast, releases a vocal saturation peak. The verse-to-bridge spread is large by 2020s mastered-pop standards, where section-level loudness is typically flattened.

**D3 — Mix density.** Through Moore's textural-layer typology, the song is unusually thin. There is no conventional snare/hi-hat beat; kick and sub-bass appear mainly in choruses; verses and bridge lack a low-frequency anchor. The melodic layer is lead vocal in the verses, doubled and widened in choruses, then expanded into a stacked vocal bridge. What the song chooses *not* to fill is itself the production decision.

**D4 — Bridge structural inversion.** At 2:23, the piano thins, kick and sub-bass drop out, and stacked vocal harmonies enter immediately in a long reverb wash. The bridge's spatial peak is achieved by *subtracting* instruments and *multiplying* voices, so vocal saturation and instrumental density no longer coincide.

**D5 — Outro spatial dissolution.** The 45-second outro (3:17–4:02), nearly one-fifth of the track, performs a slow reverb-tail fade rather than a hard cut. The energy settles rather than ends.

Each dimension sits some distance from contemporary pop's familiar production center; together, they make *drivers license* a useful centroid-pull test.

![Formal-functional diagram (after Moore 2012). The original *drivers license* eight-section design and four AI reconstructions are plotted on a shared time axis. Verse-blue, chorus-orange, bridge-green, outro-brown; the modulated final chorus of *Love Story* is rendered in darker red. The diagram makes legible at a glance what each generation does to the song's macro-form — the original's V-V-C-V-C-Br-C-O double-verse opening, and which generations follow, compress, or stretch it, against the V-PC-C × 2 template that *Love Story* is treated here as exemplifying.](figures/figA_formal_functional_timeline.png)

![Sound-box of the original *drivers license* at three section types (after Moore 2012). Each box maps the lateral × proximity × frequency-register space of a section's mix. (a) Verse 1 places only the lead vocal (close, central, mid-high) and a sparse upright piano (mid, central). (b) The chorus fills the box laterally and depthwise with full band: octave-down doubled vocal at center-front, harmonies panned wide, pad pushed to extreme L/R and back, sub-bass and soft kick anchoring the low register. (c) The bridge enacts the song's central inversion — kick and sub-bass drop out, the piano weakens, and multi-layer stacked vocal harmonies plus ad-libs spread laterally and into the back of the box. The vocal saturation peak does not coincide with the instrumental density peak; this paradox is the song's spatial signature.](figures/figB_sound_box_triptych.png)

## Prompt Construction

In the Suno v5.5 interface used for this project, the Style field was limited to 1000 characters and the retained generations ranged from 3:43 to 4:30. I wrote a roughly 800-character Style description specifying genre, tempo, key, form, vocal staging, instrumentation, and the five dimensions above. It deliberately omits the opening car-door/ignition/seatbelt sound design, testing whether the model derives it from the title.

The lyrics field receives a paraphrase rather than the original text. This avoids content-filter issues and tests whether production decisions emerge from the Style description rather than from memorized lyric tokens. The paraphrase preserves Genius's eight-section macroform for *drivers license*, line counts, narrative arc, and imagery cluster while replacing every specific phrase; section labels follow the Genius page exactly (Genius n.d.-a).

I generated two Suno v5.5 variants. **Variant A** uses the Style description plus plain paraphrased lyrics. **Variant B** embeds inline emotional and production meta-tags inside the section labels. This adds a denser direction channel, though I treat it as a prompt convention rather than a guaranteed control interface.

**A note on scope.** Close listening guided by Moore's framework is the primary evidence; section-level loudness, brightness, key, and boundaries are supporting anchors. Metric windows use the same Genius-derived reference-section assumptions across retained generations, so they are descriptive anchors rather than automated segmentation claims. The four retained files are selected representatives from at least three candidates per condition; the study is a close analytical comparison, not a population-level estimate.

---

# Reconstruction Attempts on Suno v5.5

## Variant A — Direct Prompt

**Analytical question.** Variant A asks whether a direct prompt — Style description plus paraphrased lyrics with section labels — suffices to specify production decisions away from the mainstream centroid.

The simplest specifications are unstable: neither v5.5 variant honors the prompt's 4:00 duration, the chroma-based key estimate places Variant A a semitone above the prompted B♭, and the original's half-time feel becomes a faster full-time pulse. The main divergence is the **bridge inversion** (D4): where the original strips instruments, Variant A keeps the bridge-region loud and adds continuous snare/hi-hat. The bridge column in Figure 3 is the key comparison: panels (a) versus (b)/(c) show that v5.5 never strips the bridge, while panel (d) shows v4.5 partially recovering the inversion. The result lacks the original's ethereal suspension because the generated track pushes energy too early. The **outro** (D5) is also held near chorus loudness, replacing the 45-second reverb-tail dissolution with a near-hard cut. Form is the main success: layers enter and exit near the prompted eight-section structure.

![Textural-layer comparison: original design versus three Suno reconstructions, on the same Genius eight-section grid (after Moore 2012, on textural layers). Filled square (×) = layer present; light square (·) = weak / partial; blank = absent. The bridge column is boxed (red = no inversion, green = partial inversion). The original (panel a) deploys an unusually thin texture: no drum kit (no snare, no hi-hat), and a strip-and-stack inversion at the bridge. Variants A and B (panels b, c) on Suno v5.5 introduce a full drum kit across every section and never strip the bridge — the inversion does not occur on either. Variant B on Suno v4.5 (panel d) preserves the drum-kit drop and the piano-weakening at the bridge, the only generation to produce the inversion in direction.](figures/figC_textural_comparison.png)

## Variant B — Inline Emotional Meta-Tags

**Analytical question.** Variant B asks whether inline emotional and production meta-tags — embedded in each section label — can compensate for what the observed Style-field limit leaves unsaid.

The meta-tags improve some dimensions while degrading others. They make the overall dynamic curve clearer, but the bridge still ramps up rather than inverting density. They also create an affective mismatch: despite the heartbreak/late-night prompt, the generated mood feels lighter and breezier than the original.

Verse 1 is the revealing case. The original's V1 anchors the song's intimacy: dry, breathy, sparse, dark. Variant A, without tags, comes closest to that quietness. Variant B, despite explicitly demanding hushed close-mic intimacy, is louder and brighter. In Figure 4, note that the loudness axis is inverted: higher on the plot means quieter. The tags push the most distinctive section away from the original.

![Verse-1 retreat under inline emotional meta-tags. Although Variant B's tags explicitly demand "hushed, breathy, ASMR-close intimacy; held-back tear," V1 emerges louder (–25 dB versus Variant A's –32 dB; left panel, with axis inverted so that quieter is up) and brighter (2392 Hz versus 1732 Hz; right panel). RMS and spectral centroid do not measure breathiness directly; they mark the section-level loudness and brightness shift that supports the close-listening judgment that the tags did not preserve V1 restraint.](figures/fig5_v1_retreat.png)

This is the prompt-engineering paradox: tags improve macro-contour, a centroid-aligned property, while pulling V1's near-silence toward the centroid. They reshape the contour around the prior without reaching the prior's far extremes.

## Synthesis

Both v5.5 variants diverge on the same five dimensions. They differ in which dimensions worsen, but the direction — toward polished contemporary pop — is constant. Suno does not completely fail: it captures form, tempo class, lyrical structure, and much of the instrumentation list. What it does not fully reproduce is production atmosphere: V1 stillness, bridge subtraction, and the dissolving outro. The output is musically intelligible; it is just not Daniel Nigro's record.

---

# Mainstream Control: "Love Story"

**Comparison question.** The *Love Story* experiment asks whether the divergences in §4 are properties of *drivers license* as a song — its specific lyrics, its specific production fingerprint — rather than of the AI's relation to centroid-distant production in general.

I applied the same workflow to Taylor Swift's "Love Story" (2008, *Fearless*, prod. Taylor Swift and Nathan Chapman; ProSoundNetwork Editorial Staff 2009). Here I treat it as centroid-typical: a dense, mainstream-mastered country-pop crossover built from acoustic guitar, banjo, mandolin, fiddle, full drum kit, bright bass, and doubled vocals. Its macroform follows a familiar Verse → Pre-Chorus → Chorus template, doubled and extended with Post-Chorus, Bridge, modulated Chorus 3, and Outro (Genius n.d.-b). This classification is an analytical judgment by ear and course vocabulary, not a measured corpus position. The control cannot separate centroid distance from confounds: *Love Story* may be better represented in training data, easier to describe in 1000 characters, and easier to reproduce because its dynamic profile is simpler. It therefore shows that the same workflow succeeds better on template-conforming production, not that centroid distance is the sole explanatory variable.

The AI version handles *Love Story* as a stable, bright, mid-density sound-box rather than as a sequence of extreme contrasts. Its chroma-based key estimate is D major and its estimated tempo is 119.7 BPM, matching the prompt closely. Its whole-track p95-p5 dynamic range is 13.29 dB; under the same reference-window analysis used for the other outputs, section-mean RMS values stay within about 4.6 dB. This means the bridge does not dramatically thin in loudness; it remains near the mastered level, signaling contrast more by formal position and brightness than by the kind of density inversion that defines *drivers license*.

Texturally, the control succeeds because the requested layers are conventional and cumulative: acoustic guitar and bright upper strings/mandolin occupy the mid-high range, drums and bass stabilize the choruses, and doubled vocals sit at a polished mid-distance rather than ASMR closeness. The final chorus functions as a peak because texture, harmony, and narrative all point in the same direction. That is the opposite of *drivers license*, where the peak depends on a paradoxical split between vocal saturation and instrumental subtraction.

The AI's task is therefore to reproduce a familiar template rather than an unfamiliar one, and it does so with comparatively high fidelity. The key estimator places the AI *Love Story* on D major, while all three *drivers license* generations are estimated away from the prompted B♭. Its dynamic profile is also flatter and more mainstream-mastered; the *drivers license* generations widen dynamic spread but never reach the original's near-silent valleys.

Form fidelity is high as well: the AI *Love Story*'s section boundaries roughly follow the V → PC → C → V → PC → C → PostC → Br → C(modulated) → Outro structure used in the Genius-derived comparison grid. Estimated key, broad dynamic profile, and form are all reproduced more closely for *Love Story*. The model has not become better; it has been asked for less. The control weakens a purely song-specific explanation and supports the centroid-position account as an exploratory reading.

---

# Cross-Model Robustness

**Comparison question.** This section asks whether the divergences in §4 are properties of Suno v5.5 as a single checkpoint.

The controlled comparison is Suno v5.5 versus Suno v4.5; YuE is included only as a boundary case.

**Suno v4.5 (older proprietary checkpoint).** Running Variant B on v4.5 yields the most counter-intuitive finding. On the bridge-inversion dimension, the reference-window metric shows the clearest bridge-region dip in v4.5, and close listening also finds instrumental thinning. Voice density does not stack to the original's level, but the thinning direction is present. By contrast, the v5.5 bridges become the loudest regions. This suggests a tradeoff: v4.5 has rougher form control, but in this case it preserves more of the production-decision axis.

![Vocal-staging summary across five versions: how each AI generation realizes the original's voice-and-space decisions across seven analytical dimensions (after Moore 2012, on staging). Cell color encodes proximity to the relevant design target — deep green = on-design, light green = close, yellow = partial, red = off-design. Variant A's V1 proximity matches the original (close-mic, audible breath) but its bridge collapses to an open mid-distance staging; Variant B's tags trade some V1 fidelity for a slightly more dramatic macro-contour (yellow throughout); v4.5 partially recovers the bridge's vocal foregrounding at the cost of generic, mid-distance verses; the *Love Story* control matches its own template more consistently because that template uses familiar mid-distance country-pop staging.](figures/figD_vocal_staging.png)

**YuE (open LLaMA2-based autoregressive system, locally deployed).** YuE (Yuan et al. 2025) is a boundary comparison only, not a fully parallel test of the Suno finding. It accepts the prompt but diverges differently: at most two simultaneous instrumental layers, heavily off-prompt style, and modified lyrics. Because its failure mode is so different, it mainly marks the limits of the comparison; the Suno v4.5/v5.5 bridge result carries the interpretive weight here.

The hypothesis that the divergence is specific to one Suno checkpoint is weakened mainly by the v4.5/v5.5 comparison. Read left to right in Figure 5: the *Love Story* row is mostly green because its target is close to familiar country-pop staging, while the *drivers license* rows show more yellow-to-red drift in voice and space.

![Bridge-inversion test across the three *drivers license* generations, using the shared Genius-derived reference windows described in Appendix C. Pale bars: mean RMS of the surrounding chorus windows (C1, C2, C3); solid bars: the bridge-region RMS. The original design requires the bridge to sit *below* the surrounding choruses in instrumental energy (red dashed reference). Under this reference-window alignment, Suno v4.5 is the only retained generation whose bridge region shows a loudness dip relative to its chorus windows. The RMS bars are a supporting loudness anchor, not a standalone segmentation claim; Figure 3 supplies the complementary textural-layer evidence.](figures/fig6_bridge_inversion.png)

---

# Discussion: Centroid Pull as Analytical Pattern

A structural reading is consistent with the observations, though further work would be needed to confirm it. Modern text-to-music systems, whether research systems such as MusicLM and MusicGen or commercial systems such as Suno, can be understood as prompt-conditioned generators that sample from, or otherwise generate under, learned audio/music distributions. The outputs analyzed here make audible a *mainstream pop centroid*: mastered loudness, filled frequency spectrum, polished mid-distance vocal staging, V-PC-C structure, and mid-up tempo. The prompt can tilt this distribution, but in these cases it does not fully relocate the prior.

*drivers license* sits away from this centroid along all five dimensions. Across the four AI generations, each dimension is pulled inward in the same direction, though magnitude varies. The present close readings suggest that this is not five unrelated gaps but one recurring pattern: prompt engineering can specify many discrete features, yet it has difficulty carrying emotional contour, cumulative energy, and the weight of a producer's silences.

This is where popular-music analysis adds resolution to listener-perception work. Figueiredo et al. establish that listeners distinguish AI music and often cite broad vocal/technical cues; close reading names the dimension-by-dimension offsets. Morreale (2021) frames AI music generation around authorial responsibility. Centroid pull sharpens that question: if reconstruction repeatedly moves uncommon production choices toward mainstream defaults, then the system does not preserve those choices so much as homogenize them.

---

# Limitations

Three limitations bound the precision of the claim. First, a multi-listener design would strengthen the perceptual side. Second, only one selected sample per condition is analyzed, though each was chosen after hearing at least three candidates. Third, the evidence is observational rather than statistical; a larger sample would be needed for hypothesis testing. 

Prompt difficulty is an additional confound. The five *drivers license* dimensions may require a richer vocabulary than the Style field can carry, whereas *Love Story*'s production aligns with terms the model already handles fluently: bright country-pop, full band, harmonized chorus, key change. This design cannot fully distinguish "the model prior pulls outputs toward the centroid" from "the prompt is insufficiently expressive to specify centroid-distant decisions."

These limitations mean the centroid-pull pattern observed here should be treated as an exploratory hypothesis for future testing rather than a confirmed finding.

---

# Conclusion

This project began with a practical reconstruction task: describe a pop record in enough analytical detail that an AI system could remake it. The hardest details are not the obvious ones. Suno follows section labels and generates coherent pop; what it does not reliably preserve are the decisions farthest from the mainstream center of its learned style space: the near-silent close-mic verse, the bridge that peaks by subtracting instruments, and the outro that dissolves rather than closes. The *Love Story* control matters because it shows the inverse: when the requested design already resembles a familiar country-pop template, the same workflow produces a closer result.

I call this tendency *centroid pull*. The term does not replace close listening with machine-learning jargon; it names a pattern observed across these cases. Across voice, texture, form, dynamics, and space, the AI does not simply make random errors. It repeatedly moves centroid-distant production choices toward typical pop defaults. In Morreale's (2021) authorship terms, the gap clarifies that what makes *drivers license* distinctive is not only melody or lyrics but production authorship: the weight of Daniel Nigro's silences, the spatial inversion, and the dissolving outro. By flattening what is unusual, the reconstructions inadvertently map the contours of a producer's creative signature.

---

# Bibliography

Agostinelli, Andrea, Timo I. Denk, Zalán Borsos, Jesse Engel, Mauro Verzetti, Antoine Caillon, Qingqing Huang, Aren Jansen, Adam Roberts, Marco Tagliasacchi, Matt Sharifi, Neil Zeghidour, and Christian Frank. 2023. "MusicLM: Generating Music from Text." *arXiv preprint* arXiv:2301.11325.

Copet, Jade, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve, Yossi Adi, and Alexandre Défossez. 2023. "Simple and Controllable Music Generation." *Advances in Neural Information Processing Systems* 36.

Figueiredo, Flavio, Giovanni Martinelli, Henrique Sousa, Pedro Rodrigues, Frederico Pedrosa, and Lucas N. Ferreira. 2025. "Echoes of Humanity: Exploring the Perceived Humanness of AI Music." *arXiv preprint* arXiv:2509.25601.

Genius. n.d.-a. "drivers license — Olivia Rodrigo." Accessed April 28, 2026. https://genius.com/Olivia-rodrigo-drivers-license-lyrics.

Genius. n.d.-b. "Love Story — Taylor Swift." Accessed April 28, 2026. https://genius.com/Taylor-swift-love-story-lyrics.

Krumhansl, Carol L. 1990. *Cognitive Foundations of Musical Pitch*. Oxford University Press.

Moore, Allan F. 2012. *Song Means: Analysing and Interpreting Recorded Popular Song*. Farnham: Ashgate.

Morreale, Fabio. 2021. "Where Does the Buck Stop? Ethical and Political Issues with AI in Music Creation." *Transactions of the International Society for Music Information Retrieval* 4 (1): 105–113.

ProSoundNetwork Editorial Staff. 2009. "Taylor Swift — Love Story." *Mix*, April 17, 2009. Accessed April 30, 2026. https://www.mixonline.com/recording/taylor-swift-love-story.

Spotify. 2026. "100 Greatest Pop Songs of the Streaming Era." *Spotify Newsroom*, February 24, 2026. Accessed April 30, 2026. https://newsroom.spotify.com/2026-02-24/greatest-pop-songs-streaming-era/.

Trust, Gary. 2021. "Olivia Rodrigo's 'Drivers License' Leads Hot 100 for 8th Week, The Weeknd's 'Blinding Lights' Marks a Year in Top 10." *Billboard*, March 8, 2021. Accessed April 30, 2026. https://www.billboard.com/pro/olivia-rodrigo-drivers-license-number-one-eighth-week-hot-100/.

Yuan, Ruibin, et al. 2025. "YuE: Scaling Open Foundation Models for Long-Form Music Generation." *arXiv preprint* arXiv:2503.08638.

Zagorski-Thomas, Simon. 2014. *The Musicology of Record Production*. Cambridge: Cambridge University Press.

---

# Appendix A — Style Descriptions Used as Prompts

**A.1 *drivers license* Style description.** Provided verbatim to Suno v4.5 and v5.5.

> Olivia Rodrigo / Daniel Nigro style 2020s alt-pop / bedroom-pop ballad. 72 BPM half-time (144 notated), B♭ major, 4:00. Form: V1, V2, Chorus, V3, Chorus, Bridge, Chorus, Outro (double-verse opening, no pre-chorus). Vocal: young female, breathy, fragile, close-mic ASMR in verses; minimal autotune. Verses solo dry, no doubling. Chorus: main + octave-down doubling + L/R harmonies. Bridge: 4-5 stacked choir-like harmonies with "ooh" ad-libs. Instrumentation: sparse upright piano throughout (weak in bridge); warm pad + sub-bass + soft kick only in choruses (NONE in bridge). No snare, no hi-hat. SPATIAL INVERSION: verses close/intimate; choruses wide/full; BRIDGE = stripped instruments + stacked vocals = spatial peak; outro 45s reverb-tail fade, no hard cut. Mood: heartbreak, late-night drive, lo-fi warm.

**A.2 *Love Story*.** *Note: the prompt uses an upward-modulation cue as a stylistic instruction. The paper does not treat the modulation interval as a verified feature of the original.*

> Taylor Swift "Love Story" 2008 country-pop crossover. Bright, polished, radio-pop aesthetic. 119 BPM, 4/4, D major, with an upward modulation before the final chorus. Form: Intro, V1, V2, Chorus, V3, Chorus, Bridge, Final Chorus (KEY MODULATION upward), Outro. Vocal: young female, bright, clear, light country twang; doubled + L/R harmonies in chorus; mainstream polish, light pitch correction. Instrumentation: acoustic guitar foundational; mandolin (intro + accents); fiddle (verses + bridge); full drum kit (kick + snare + hi-hat) in choruses; bright bass; strings/pad swell into final chorus. Filled mid-density country-pop mix. Spatial: medium-distance vocal; wide stereo spread; mid-depth reverb; mastered loudness throughout. CLIMAX: upward KEY MODULATION before final chorus — signature release. Tension-release: verses=narrative build; choruses=full release; bridge=brief soften; MODULATED FINAL CHORUS=peak; outro=resolved fade. Mood: hopeful, romantic, defiant young love.

# Appendix B — Lyrics Paraphrase Mapping

The paraphrase preserves the section count, per-section line counts, narrative arc, and imagery cluster while replacing specific lyric phrases. For copyright reasons, the public support repository excludes complete commercial lyrics, near-verbatim lyric prompts, and line-by-line lyric mappings; it includes only the style descriptions, section-level methodology, generated audio artifacts, metrics, scripts, and figures needed to evaluate the paper's analytical claims. A private working copy retains the full lyric mappings for course audit.

# Appendix C — Generated Audio and Selection

Four AI generations were retained as final outputs after listening to ≥3 candidates per (model, variant) condition and selecting on the structural-fit criteria specified in §3.2. The generated audio analyzed here is included in the support repository under `private/audio/` for auditability, with large files tracked through Git LFS:

- `driver_license_with_no_emotion.wav` — Suno v5.5, Variant A, 4:28
- `driver_license_with_detailed_emotion.wav` — Suno v5.5, Variant B, 3:43
- `driver_license_suno_v4.5.wav` — Suno v4.5, Variant B, 3:59
- `love_story_suno.wav` — Suno v5.5, Variant B (control), 4:30

Per-generation objective metrics (chroma/Krumhansl-style key estimate, tempo estimate, RMS by reference window, spectral centroid, auto-detected segment boundaries) and figures (mel-spectrogram, RMS envelope, spectral centroid time-course, chromagram) are compiled in `data/ai_audio_metrics.json` and `figures/` respectively, generated by `scripts/analyze_ai_audio.py`. The metric summaries were generated with the same analysis script and reference-section assumptions across all retained generations; RMS and spectral-centroid values are used as supporting anchors rather than as substitutes for close listening.
