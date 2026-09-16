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

## Canonical placement/search anchor: rules 1890–1896

The direct `.per` extraction confirms the earlier construction index's identification of rule 1890 as the placement/search control point. The sequence is a GOLDMC2 search/placement transaction followed by the STONEMC1 search/placement transaction.

### Rule 1890 — lines 21969–21987

```lisp
(defrule
    (false)
    (goal gl-progression-pause -1)
    (can-build-with-escrow mining-camp)
    (goal gl-current-build-item GOLDMC2)
    (up-set-target-object search-remote c: 0)
    ;	(up-timer-status t-build-delay != timer-running)
=>
    (up-get-point position-object point-x)
    (up-set-target-point point-x)
    (chat-to-player me "Second Gold Mining Camp")
    (set-strategic-number sn-placement-zone-size 15)
    (set-strategic-number sn-placement-fail-delta 2)
    (set-strategic-number sn-allow-adjacent-dropsites 0)
    (set-strategic-number sn-dropsite-separation-distance 25)
    (release-escrow wood)
    (up-build place-point 0 c: mining-camp)
    ;	(enable-timer t-build-delay 3)
)
```

### Rule 1891 — lines 21989–21995

```lisp
(defrule	;come back if skipped
    (goal gl-strategy FLUSH)
    (building-type-count-total mining-camp < 3)
    (up-compare-goal gl-build-progress > GoldMC2Number)
=>
    (set-goal gl-build-progress GoldMC2Number)
)
```

### Rule 1892 — lines 21997–22005

```lisp
(defrule
    (goal gl-strategy FLUSH)
    (up-compare-goal gl-current-build-item != GOLDMC2)
    (up-compare-goal gl-build-progress == GoldMC2Number)
=>
    ;	(chat-to-player me "Setting current build item to GOLDMC2")
    (set-goal gl-current-build-item GOLDMC2)
    (set-escrow-percentage wood LOW-ESCROW)
)
```

### Rule 1893 — lines 22007–22013

```lisp
(defrule
    (goal gl-current-build-item GOLDMC2)
    (building-type-count-total mining-camp >= 3)
=>
    (up-modify-goal gl-build-progress c:+ 1)
    ;	(chat-to-player me "Second Gold Mining Camp Built")
)
```

### Rule 1894 — lines 22016–22030

```lisp
(defrule
    (goal gl-fifth-turn 1)
    (goal gl-progression-pause -1)
    (can-build-with-escrow mining-camp)
    (goal gl-current-build-item STONEMC1)
=>
    (set-strategic-number sn-focus-player-number 0)
    (up-full-reset-search)
    (up-set-target-point home-x)
    (up-filter-distance c: -1 c: 30)
    (up-find-remote c: stone-mine c: 40)
    (up-modify-sn sn-focus-player-number s:= sn-target-player-number)
    (up-clean-search search-remote object-data-distance search-order-asc)
    (up-remove-objects search-remote -1 > 0)
)
```

### Rule 1895 — lines 22032–22050

```lisp
(defrule
    (goal gl-fifth-turn 1)
    (goal gl-progression-pause -1)
    (can-build-with-escrow mining-camp)
    (goal gl-current-build-item STONEMC1)
    ;	(building-type-count-total farm >= 12)
    (up-set-target-object search-remote c: 0)
=>
    ;	(chat-to-player me "First Stone Mining Camp")
    (up-get-point position-object point-x)
    (up-set-target-point point-x)
    ;	(up-send-flare point-x)
    (set-strategic-number sn-placement-zone-size 5)
    (set-strategic-number sn-placement-fail-delta 10)
    (set-strategic-number sn-allow-adjacent-dropsites 0)
    (set-strategic-number sn-dropsite-separation-distance 10)
    (release-escrow wood)
    (set-escrow-percentage wood 0)
    (up-build place-point 0 c: mining-camp)
)
```

### Rule 1896 — lines 22052–22058

```lisp
(defrule	;come back if skipped
    (goal gl-strategy FLUSH)
    (dropsite-min-distance stone >= 5)
    (up-compare-goal gl-build-progress > StoneMC1Number)
=>
    (set-goal gl-build-progress StoneMC1Number)
)
```

## Directly observed construction architecture

The canonical sequence now gives a clean source-level decomposition:

1. **Search state:** `gl-current-build-item` selects a transaction; `up-full-reset-search`, `up-set-target-point`, `up-filter-distance`, and `up-find-remote` establish candidate geometry.
2. **Candidate selection:** `up-set-target-object search-remote c: 0` selects the search result.
3. **Placement point:** `up-get-point position-object point-x` and `up-set-target-point point-x` transfer the selected object into placement state.
4. **Placement policy:** strategic numbers explicitly control zone size, failure delta, adjacency, and dropsite separation.
5. **Resource boundary:** `release-escrow wood`, and in the STONEMC1 path `set-escrow-percentage wood 0`, mutate resource/escrow state before the engine-facing build operation.
6. **Engine-facing execution:** `up-build place-point 0 c: mining-camp` issues the placement/build operation.
7. **Verification/recovery:** subsequent rules use building counts, dropsite distance, and `gl-build-progress` to advance or rewind the construction state.

These are source-level facts. They do **not** establish that the engine accepted the command, that a building was actually placed, or that the resulting world state persisted. Runtime verification remains separate evidence.

## Next forensic pass

Continue the canonical source extraction by enumerating every rule between 1801 and 1896, preserving exact bodies and source offsets, then build a machine-readable dependency matrix for:

- `gl-current-build-item`
- `gl-build-progress`
- `gl-escrow-state`
- `up-pending-placement`
- `up-pending-objects`
- `up-find`
- `up-find-remote`
- `up-get-point`
- `up-set-target-point`
- `up-set-target-object`
- `up-build`
- `up-assign-builders`
- `build`
- `release-escrow`
- `set-escrow-percentage`
- construction timers and strategic preemption.

The source extraction remains **DIRECT** evidence; semantic transplantation and AEGIS improvements are separate analytical layers.
