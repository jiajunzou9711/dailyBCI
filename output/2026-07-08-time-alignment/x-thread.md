1/ Neural decoding starts before the model.

The first question is temporal: when did the behavioral event occur on the neural recording clock?

If that answer is wrong, the decoder may learn feedback from the future instead of intent from the present.

2/ This is a causality problem, not just a precision problem.

Spikes are millisecond-scale events. Population activity can evolve over tens to hundreds of milliseconds.

A 500 ms label error can move a signal from “movement preparation” to “post-movement feedback.”

3/ The safe anchor is the neural clock.

Behavior logs, camera frames, task software, and acquisition systems can all carry different timestamps.

For decoding, the event must eventually become a sample index on the neural data stream.

4/ That is why labs use TTL pulses.

A TTL pulse turns “this event happened” into a clean voltage edge.

The acquisition system records the rising or falling edge alongside neural data, so the event is marked on the neural time axis.

5/ But TTL does not define the behavior for you.

In a rodent lever task, “the event” could mean paw lift, first contact, lever displacement, switch closure, force threshold, or reward delivery.

The edge is precise only for the event you actually wired.

6/ A trial is a state-transition chain.

Cue onset, delay, movement onset, press threshold, hold, reward, and feedback ask different neural questions.

Event marker design is therefore experiment design.

7/ Timing errors have different meanings.

Delay is a fixed offset. Jitter is variable delay. Drift is clocks slowly walking apart.

A fixed offset can be corrected. Jitter smears peri-event dynamics. Drift breaks long recordings unless measured.

8/ Hardware synchronization has three layers.

Event TTL marks specific events.

Periodic sync pulses estimate offset and drift.

Shared clocks make multiple devices derive time from the same reference clock.

They solve different parts of the timing problem.

9/ High-channel probes add another layer.

Neuropixels 1.0 has 384 recording channels and 960 selectable electrode sites. Its circuit design uses 32 ADCs, with groups of 12 channels multiplexed into each 10-bit SAR ADC.¹ ²

10/ That means high-channel systems often combine local serial scanning with global parallelism.

Within an ADC group, channels are sampled in sequence. Across ADC groups, scanning can proceed in parallel.

The result is deterministic channel-to-channel skew.

11/ This skew is usually not the first-order issue for 50 ms spike-count decoding.

It matters more for millisecond spike timing, phase analysis, short-latency connectivity, or closed-loop stimulation.

The rule is: compare timing error to the timescale of the question.

12/ In software, alignment becomes a simple subtraction.

Find the TTL edge sample.
Find each spike sample.

relative_sample = spike_sample - event_sample

Convert to milliseconds only at the end. Sample index is the native coordinate.

13/ Good neural decoding begins with time definitions.

A model can report strong offline accuracy while learning future feedback, software latency, or a drifted label.

Before training the decoder, put events, neural signals, and device clocks on one defensible timeline.

14/ Sources

¹ Jun et al., Nature, 2017: https://pmc.ncbi.nlm.nih.gov/articles/PMC5955206/
² Mora Lopez et al., IEEE TBioCAS, 2017: https://doi.org/10.1109/TBCAS.2016.2646901

15/ Other materials

Open Ephys synchronization docs:
https://open-ephys.github.io/gui-docs/Tutorials/Data-Synchronization.html

Bilibili videos discussed:
BV1q84y1g7no
BV17uN9zyEsu
