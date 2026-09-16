# Grumpy AI-Scripter Manifesto v0.1

I have watched too many AoE2 AIs die from the same mistakes. They do not die because the author forgot a clever strategy. They die because control, resources, construction, and state were allowed to disagree.

This project will not repeat those mistakes.

## Rule 1 — The engine is not your imagination

If the `.per` command was issued, write **command issued**.

Do not write **built**, **trained**, **researched**, or **completed** unless the source or runtime evidence establishes it.

## Rule 2 — Source order is code

In a reactive `.per` machine, textual order can be computational structure. Jumps, fall-through, disabled rules, and re-entry regions are part of the program.

Do not rearrange rules because the new order looks cleaner.

## Rule 3 — State is a scarce resource too

A goal or strategic number can be a state register, selector, counter, scratch location, or shared arbitration point.

Before changing one, find every writer and reader.

## Rule 4 — Escrow deserves respect

Most scripts treat escrow as a financial footnote. Shadow appears to use it in a much more interesting way: resource protection can become part of behavioral commitment.

If that pattern survives corpus-wide analysis, use it.

Do not replace it with a fashionable abstract priority manager merely because the latter has prettier diagrams.

## Rule 5 — Every reservation needs an exit

A commitment without release is starvation.

For every protected resource path, identify:

- success release;
- failure release;
- timeout/reassessment;
- substitution if applicable;
- re-entry.

If none exists, the design is unfinished.

## Rule 6 — Pending is not finished

`up-pending-objects` and `up-pending-placement` are observations about pending work. They are not magic completion flags.

World state wins.

## Rule 7 — Do not build an architecture around nouns

`economy`, `military`, `escrow`, `construction`, `verification`: these are useful analytical labels, not proof that the source has those module boundaries.

Find the control mechanisms first.

## Rule 8 — A static parser can lie by omission

A parser can tell us that syntax is balanced. It cannot tell us that the AI will execute the intended behavior under every game state.

Static analysis establishes static facts.

Replay analysis establishes observed runtime facts.

Keep the two ledgers separate.

## Rule 9 — Cleverness must survive starvation

A strategy that looks intelligent while resources are abundant is worthless if it collapses when three objectives demand the same 100 wood.

Arbitration is where the real bot lives.

## Rule 10 — Byzantines get policy, not a new physics engine

Shadow's reconstructed machine should provide the control discipline. Byzantine logic should supply civilization-specific capability and preference.

Do not throw away the machine because the civilization changed.

## Rule 11 — Improvements must beat something

Every extension needs a baseline, a failure mode, a hypothesis, and a verification method.

"Cleaner" is not a behavioral metric.

## Rule 12 — If the evidence disagrees, stop

Do not average conflicting source interpretations into a comforting story.

Record the conflict.

Find more evidence.

## The operating doctrine

```text
Understand the machine.
Preserve the machine.
Adapt the machine.
Improve the machine.
Prove the improvement.
```

And if the bot still behaves badly, do not add fifty rules.

Find out which assumption was wrong.
