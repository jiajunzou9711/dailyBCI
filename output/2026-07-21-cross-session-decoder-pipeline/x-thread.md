# X Thread — Cross-session neural decoder pipeline (2026-07-21)

1/16 How do you build a neural decoder that survives across recording sessions? A methodology thread — using POYO+ (Azabou et al., ICLR 2025) as a worked example.

2/16 The core problem: neural decoders map brain activity to behavior (e.g. motor cortex spikes → hand velocity). But switch sessions, electrodes, or subjects, and performance drops. Why? The neurons you record are never the same set twice.

3/16 Training = picking one rule from a candidate set defined by the model architecture. Error decomposes into: approximation error (best candidate vs truth) and estimation error (what you picked vs best candidate). The second one blows up when data is scarce.

4/16 Estimation error scales roughly with trainable_params ÷ data. A spike-tokenizing decoder has ~7.6M trainable params. A single calibration session yields tens of trials. That ratio is absurd — from-scratch training is not slow, it's informationally impossible.

5/16 Fix: pretrain on many sessions, fine-tune on few. But neural data has a problem language doesn't: every session changes the input dimension AND identity. A weight tied to "channel 12" is wrong the moment channel 12 records a different neuron.

6/16 The key insight: split the model along the boundary of what changes vs what doesn't. Neuron identity changes every session. How a population evolves over time into an action does not. Make the first part small and disposable; make the second part large and reusable.

7/16 Piece 1 — Lookup table. Each spike-sorted unit gets a row of learnable numbers (64-dim, illustrative). The unit ID from spike sorting is arbitrary and non-transferable: unit 12 today and unit 12 tomorrow occupy different rows, unrelated.

8/16 Piece 2a — Why rotate? A spike at t=0.10s carries a timestamp, but absolute time is meaningless (shift the clock, same activity becomes different numbers). What matters is the interval between spikes.

9/16 Piece 2b — RoPE (Su et al., 2024) encodes time as a rotation angle (angle = frequency × time). Any comparison between two spikes then depends only on their time difference, not when recording started. No learnable parameters — pure formula.

10/16 A spike's representation = its neuron's lookup row, rotated by its timestamp. Same neuron firing 3 times → 3 copies of the same row, each rotated differently. The 64 dims pair into 32 independent planes with different rotation speeds → multi-scale temporal resolution.

11/16 Piece 3 — The count problem. Slice 1 second into 50 bins of 20ms. Each bin has a variable number of spikes (7 here, 40 there). The downstream sequence model needs fixed-size input. Averaging would destroy spike-level information.

12/16 Fix: cross-attention. 16 learned query vectors (fixed count, independent of spike count) each score every spike in the bin, then take a weighted sum. Output: always 16 vectors per bin, regardless of input count. Weighted aggregation, not averaging.

13/16 Result: 50 bins × 16 latents = 800 fixed-size vectors (each 64-dim). This is what the backbone sees — a clean, rectangular tensor, no matter how many neurons fired or how irregularly.

14/16 Piece 4 — Backbone. A sequence model (self-attention or state-space, e.g. Mamba) processes the 800 latents, letting different time bins inform each other. This is the "unchanging half" — it learns temporal dynamics, not neuron identities.

15/16 Backbone = asset (frozen at deployment, reused across sessions/subjects). Lookup table = consumable (discarded and relearned each session). In MOJO-POSSM: UI fine-tuning uses <18K params and matches full fine-tuning at >7.6M params — two orders of magnitude fewer.

16/16 This pipeline is the POYO family's shared foundation. Next: MOJO (Mao et al., arXiv 2607.14086) adds SSL so unlabelled recordings also fuel pretraining — another thread.

Refs: Azabou+ ICLR 2025 · Su+ Neurocomputing 568:127063 · Mao+ arXiv 2607.14086
