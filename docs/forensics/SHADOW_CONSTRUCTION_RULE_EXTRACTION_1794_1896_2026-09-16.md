# Shadow Construction Rule Extraction — Rules 1794–1896

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per` on `main`  
**Canonical blob SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

## Evidence status

This artifact records **DIRECT** source evidence recovered from the canonical `ShadowSource.per` blob. Source offsets are line-addressed against the `.per` file itself. No semantic interpretation is substituted for the source bodies.

## Verified construction anchors

### Rule 1794 — lines 20851–20857

```lisp
(defrule
    (or (goal gl-current-build-item MARKET1)
    (or (up-pending-placement c: blacksmith)
    (up-compare-goal gl-strategy != FLUSH)))
=>
    (up-jump-rule 1)
)
```

### Rule 1795 — lines 20859–20871

```lisp
(defrule ;basically, build farms unless time for blacksmith (12 farms with berries
    (idle-farm-count < 2)
    (current-age >= feudal-age)
    (up-compare-goal MILL != YES)
    (up-pending-objects c: farm < 3)
    (building-type-count-total farm < 50)
    (building-type-count-total archery-range >= 2)
    (or (wood-amount >= 120)
    (and (wood-amount >= 80)
    (building-type-count-total farm < 10)))
=>
    (set-goal SPLIT 1)
)
```

### Rule 1796 — lines 20873–20881

```lisp
(defrule
    (goal SPLIT 1)
    (or (building-type-count-total blacksmith >= 1)
    (or (and (up-compare-goal rt >= 2)
    (building-type-count-total farm < 7))
    (and (up-compare-goal rt < 2)
    (building-type-count-total farm < 10))))
=>
    (set-goal SPLIT 2)
)
```

### Rule 1797 — lines 20883–20891

```lisp
(defrule
    (goal SPLIT 2)
    (or (nand (current-age == castle-age)
    (up-compare-goal gl-current-build-item == ESKIRMS))
    (up-research-status c: ri-elite-skirmisher >= research-pending))
=>
    (up-build place-normal gl-escrow-state c: farm)
    ; (chat-to-player me "GeneralFarm")
)
```

### Rule 1798 — lines 20893–20898

```lisp
(defrule
    (true)
=>
    (set-goal gl-escrow-state with-escrow)
    (set-goal SPLIT 0)
)
```

### Rule 1799 — lines 20900–20907

```lisp
(defrule
    (can-build farm)
    (wood-amount >= 90)
    (idle-farm-count < 2)
    (up-compare-goal MILL != YES)
    (up-pending-objects c: farm < 2)
    (building-type-count-total farm < 50)
=>
    (set-goal SPLIT 1)
)
```

### Rule 1800 — lines 20909–20918

```lisp
(defrule
    (goal SPLIT 1)
    (or (current-age >= castle-age)
    (and (goal gl-strategy KRUSH)
    (up-research-status c: ri-horse-collar >= research-complete)))
    (or (wood-amount >= 260)
    (up-compare-goal gl-current-build-item != EXTRA-STABLES))
=>
    ; (chat-to-player me "CastleFarm")
    (build farm)
)
```

## Critical ordinal correction: rules 1890–1896

The earlier navigation hypothesis that identified **rule 1890** as the principal `up-find` placement/search control point is **not supported by the direct `ShadowSource.per` line-addressed extraction**. The canonical source places the placement/search sequence later in the local construction stream.

### Rule 1890 — lines 21966–21970

```lisp
(defrule
    (true)
=>
    (up-jump-rule 5)
)
```

### Rule 1891 — lines 21972–21985

```lisp
(defrule
    (nand (goal gl-strategy FLUSH)
    (up-compare-goal pause >= 1)
    (can-build-with-escrow gold)
    (up-compare-goal gl-current-build-item == GOLD))
=>
    (set-goal pause 0)
    (up-set-target-object c: gold 1)
    (up-modify-goal gl-escrow-state c: gold 1)
    (up-get-point gold)
    (up-modify-goal gl-current-build-item c: GOLD2)
    (up-modify-goal gl-escrow-state c: gold -1)
    (up-remove-target-object c: gold)
)
```

### Rule 1892 — lines 21987–22005

```lisp
(defrule
    (nand (goal gl-strategy FLUSH)
    (up-compare-goal pause >= 1)
    (can-build-with-escrow gold)
    (up-compare-goal gl-current-build-item == GOLD)
    (up-target-object c: gold)
    ; (up-compare-goal lumber-timer >= 200))
=>
    (up-get-point gold)
    (up-set-target-point c: gold)
    ; (chat-to-player me "Gold3")
    (set-strategic-number sn-placement-zone-size 1)
    (set-strategic-number sn-placement-fail-delta 0)
    (set-strategic-number sn-allow-adjacent-dropsites 1)
    (set-strategic-number sn-dropsite-separation-distance 1)
    (release-escrow wood)
    (build gold)
    ; (set-strategic-number sn-lumber-camp-max-distance 0)
)
```

### Rule 1893 — lines 22007–22021

```lisp
(defrule
    (goal gl-strategy FLUSH)
    (up-compare-goal pause >= 1)
    (can-build-with-escrow stone)
    (up-compare-goal gl-current-build-item == STONE)
=>
    (up-set-target-object c: stone 1)
    (up-modify-goal gl-escrow-state c: stone 1)
    (up-get-point stone)
    (up-modify-goal gl-current-build-item c: STONE2)
    (up-modify-goal gl-escrow-state c: stone -1)
    (up-remove-target-object c: stone)
)
```

### Rule 1894 — lines 22023–22042

```lisp
(defrule
    (goal gl-strategy FLUSH)
    (up-compare-goal pause >= 1)
    (can-build-with-escrow stone)
    (up-compare-goal gl-current-build-item == STONE)
    ; (goal gl-current-build-item STONE)
    (up-target-object c: stone)
=>
    ; (chat-to-player me "Stone2")
    (up-get-point stone)
    (up-set-target-point c: stone)
    ; (chat-to-player me "Stone3")
    (set-strategic-number sn-placement-zone-size 1)
    (set-strategic-number sn-placement-fail-delta 0)
    (set-strategic-number sn-allow-adjacent-dropsites 1)
    (set-strategic-number sn-dropsite-separation-distance 1)
    (release-escrow wood)
    (build stone)
)
```

### Rule 1895 — lines 22044–22050

```lisp
(defrule
    (goal gl-strategy FLUSH)
    (up-compare-goal pause >= 1)
    (up-compare-goal gl-current-build-item == STONE2)
=>
    (set-goal pause 0)
)
```

### Rule 1896 — lines 22052–22060

```lisp
(defrule
    (goal gl-strategy FLUSH)
    (up-compare-goal gl-current-build-item == STONE2)
    (up-compare-goal gl-build-progress < StoneNumber)
=>
    ; (chat-to-player me "Stone4")
    (up-modify-goal gl-build-progress c:+ 1)
    (set-goal gl-escrow-state with-escrow)
)
```

## Consequence for the construction-source audit

1. `ShadowSource.per` is now the authoritative line-addressable forensic source for this extraction.
2. Rules 1794–1800 are directly verified at the previously identified offsets.
3. Rules 1890–1896 are directly verified and demonstrate that the earlier navigation index assigned the wrong semantic role to rule 1890.
4. The `up-find` / placement-search construction sequence must therefore be re-indexed from the canonical `.per` source rather than inherited from the prior offset hypothesis.
5. Any AEGIS transplant specification must preserve the distinction between **state transition**, **placement search**, **placement configuration**, **resource/escrow mutation**, and **engine build command**.
6. No `build` command in this artifact is treated as proof of completed construction. Completion remains a separate runtime/world-state verification question.

## Next forensic pass

Continue the canonical source extraction by enumerating every rule between 1801 and 1896, preserving exact bodies and source offsets, then build a machine-readable dependency matrix for:

- `gl-current-build-item`
- `gl-build-progress`
- `gl-escrow-state`
- `up-pending-placement`
- `up-pending-objects`
- `up-find`
- `up-get-point`
- `up-set-target-point`
- `up-set-target-object`
- `up-build`
- `up-assign-builders`
- `build`
- `release-escrow`
- `set-escrow-percentage`
- construction timers and strategic preemption.

The source extraction must remain DIRECT evidence; semantic transplantation and AEGIS improvements are separate analytical layers.
