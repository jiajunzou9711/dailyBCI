# X Thread — Calibrating a cross-session decoder, by hand (2026-07-22)

1/16 When a neural decoder meets a new recording, it doesn't retrain the whole model — it only relearns "who each neuron is." Let's calibrate one by hand, with real numbers. Follow-up to the previous POYO+ pipeline thread; anchored on MOJO (Mao et al., 2026).

2/16 Premise: a decoder = a frozen backbone (how a population evolves into movement, reused across recordings) + a lookup table (one row per neuron = its identity). A new session brings new neurons with no rows. Calibration = fill those rows.

3/16 Setup (dims shrunk to 2 for hand-calc; operations faithful). New neuron N1's identity row starts random: r = [1.00, −0.50]. The labeled moment has true cursor velocity = [0.80, 0.00]. Backbone Q/K/V etc. are frozen (learned in pretraining).

4/16 Step 1 — spike to token. N1 fires twice. Each spike = its row r, rotated by its timestamp (RoPE). Angles 0.20 and 0.40 give: token1 = [1.079, −0.291], token2 = [1.116, −0.071]. Same content, different rotation.

5/16 Step 2 — compress variable count to fixed. A query scores each token, softmax → weights [0.491, 0.509], weighted sum → z1 = [1.098, −0.179]. Other two bins likewise: z2 = [0.961, 0.571], z3 = [0.038, 1.117].

6/16 Step 3a — let bins talk (self-attention, frozen Q/K/V). Dot-product scores: bin1·bin1 = 1.24, bin1·bin2 = 0.95, bin1·bin3 = −0.16. Bins 1 and 3 point apart → negative score.

7/16 Step 3b — softmax the scores → bin1 attends [0.50, 0.38, 0.12], bin3 attends [0.14, 0.31, 0.55]. Each bin leans on itself + neighbors, ignores the opposing far bin. This is how temporal structure enters.

8/16 Weighted-sum the values → context-mixed latents: z1' = [1.047, 0.264], z2' = [1.011, 0.463], z3' = [0.855, 0.772]. Bin 1 no longer equals itself (was [1.098, −0.179]) — it now carries the surrounding trend.

9/16 Step 4 — pool + readout → predicted velocity = [1.219, −0.006], vs true [0.80, 0.00]. Squared loss = (1.219−0.80)² + (−0.006)² = 0.176. Way off — because r is still random.

10/16 Step 5 — backprop. The error flows back through readout ← backbone ← compression ← rotation ← row. Every stage is frozen; the gradient passes through but changes nothing there. It lands only on N1's row: grad = [0.899, −0.247].

11/16 The frozen backbone acts as a fixed translator: it converts "velocity is off by this much" into "which way should r's two numbers move," without changing itself.

12/16 Step 6 — update. r = [1.00, −0.50] − 0.05×[0.899, −0.247] = [0.955, −0.488], loss 0.176 → 0.135. Repeat ~40 steps: r → [0.655, −0.357], prediction → [0.80, 0.00], loss → 0. The random row became N1's identity.

13/16 Zoom out: only that one row moved. Rotation, compression, self-attention, readout — all frozen, untouched. At real scale, calibration updates ~18K params (the new neurons' embeddings); the frozen backbone (~7.6M) doesn't move.

14/16 So why not unfreeze everything? With only tens of calibration trials, fitting 7.6M params overfits. On the hardest transfer (unseen monkey, random-target), learning only the identity rows (<18K) MATCHES full retraining (>7.6M). The dynamics don't need to change.

15/16 One-line method: adapting to a new recording isn't retraining the decoder — it's recomputing a few identity rows against a frozen, already-correct backbone. Cheap and overfitting-resistant because you only change what actually changed.

16/16 Still owed: identity rows relearn from scratch each session, and a few labels are still needed. Next thread — pretraining by hand: how Q/K/V get trained, and how self-supervision (SSL) cuts the label need.

Refs: Mao+ arXiv 2607.14086, 2026 · Azabou+ ICLR 2025 (POYO+)
