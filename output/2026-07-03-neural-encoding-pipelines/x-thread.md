# X Thread

## 1/11

Neuroscience papers often say:

"this brain area encodes X."

But "encodes" can mean different things. A useful reading habit is to ask: what kind of evidence chain did the paper actually build?

## 2/11

For "what encodes what" papers, four evidence chains show up often:

1. representation / readout
2. behavioral-model variables
3. population dynamics
4. causal perturbation

They are related, but they do not prove the same thing.

## 3/11

1. Representation / readout

Question: can a task variable be read out from neural activity?

Typical flow:

define variable -> test tuning/encoding -> decode from population activity -> control for movement, reward, time, engagement.

## 4/11

Example: Steinmetz et al. 2019.

In mice, they used Neuropixels recordings during a visual decision task to compare how visual stimuli, choices, actions, and engagement were distributed across brain areas.

This is a readout/representation story.

## 5/11

2. Behavioral-model variables

Here, the paper first fits behavior with a model, then asks whether neural activity tracks variables from that model:

value, belief, confidence, policy, prediction error, etc.

Logic:

behavior -> model variable -> neural correlate.

## 6/11

Reinforcement learning is the classic example, but not the whole category.

In Schultz, Dayan & Montague 1997, monkey dopamine neuron activity was interpreted through reward prediction error.

The model is what makes the neural variable precise.

## 7/11

3. Population dynamics

This shifts the unit of explanation.

Instead of asking "which neuron encodes X?", it treats population activity at each moment as a point in state space.

The question becomes: how does the trajectory support computation?

## 8/11

Population dynamics papers may analyze low-dimensional trajectories, subspaces, rotational dynamics, fixed points, manifolds, and stability across time.

Here, the key object is the geometry and evolution of the population state.

## 9/11

Examples:

Churchland et al. 2012: rotational dynamics in macaque motor cortex during reaching.

Mante et al. 2013: macaque PFC dynamics for context-dependent decisions.

Vyas et al. 2020: review of computation through population dynamics.

## 10/11

4. Causal perturbation

This moves from correlation toward causal function:

find a representation/dynamic -> perturb the neural system -> measure changes in behavior and neural state.

Example: Li et al. 2016 in mouse premotor cortex.

## 11/11

Checklist when a paper says "the brain encodes X":

Can X be decoded?
Is X from a behavioral model?
Is it about population geometry/dynamics?
Was the system perturbed?

Same word, different evidence.
