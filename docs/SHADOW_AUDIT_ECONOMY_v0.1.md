# Shadow Economic Audit v0.1

## Scope

This artifact isolates the economic, escrow, transaction, research, construction, market and progression machinery in `Shadow DC7(1).per`.

## 1. Escrow

The donor uses percentage escrow, direct escrow modification, release operations, escrow-aware construction, escrow-aware research, escrow-aware training and an escrow-state carrier. Static counts are approximately 178 percentage writes, 18 direct modifications and 107 releases.

Policy coefficients include LOW-ESCROW 25, MID-ESCROW 35, MID-HIGH-ESCROW 40 and HIGH-ESCROW 60.

The FINISHED state sets food, wood, gold and stone escrow percentages to zero and releases those resources. Other release rules respond to excessive escrow and progression conditions.

Finding: escrow is an economic commitment-enforcement mechanism. It should not be made the strategic decision-maker.

Disposition: KEEP + FORMALIZE + IMPROVE.

## 2. Resource saving

Saving is coupled to progression and work-item state. A strategic requirement can therefore protect the resources needed for a later transaction without directly executing that transaction.

Disposition: PRESERVE; expose the reason for saving to the higher control plane.

## 3. Affordability

Escrow-aware affordability predicates provide a feasibility gate. They answer whether a transaction can be funded under the current reservation state.

Important epistemic rule: affordability proves feasibility, not strategic correctness and not completion.

Disposition: PRESERVE.

## 4. Transaction machinery

Build, research and train paths repeatedly use a sequence equivalent to:

work item → resource protection → affordability → transaction → observation → progression.

This common pattern is one of the donor's strongest architectural assets.

Disposition: PRESERVE + FORMALIZE as a generic transaction contract.

## 5. Progression

Current work item, progress and pause state are coupled to resource policy and transaction execution. Research and construction can advance only after relevant completion evidence.

Disposition: PRESERVE behavior; formalize as a commitment/work-item state machine.

## 6. Technology

Armor, ranged, economic, age and military technologies participate in the same transaction/progression architecture. Technology should therefore not receive a completely separate strategic execution system.

Disposition: PRESERVE execution; subordinate strategic priority to AEGIS.

## 7. Construction

Houses, camps, mills, ranges, barracks, stables, monasteries, markets, universities, castles, towers and farms use placement, pending-object state and escrow-aware transactions.

Construction is both an economic and spatial feasibility system.

Disposition: PRESERVE executor; improve strategic input.

## 8. Market

Food, wood, gold and stone trading uses age-sensitive need/excess/trading thresholds. This is liquidity management, not an independent strategic objective.

Disposition: PRESERVE + IMPROVE.

## 9. Emergency economic policy

Town safety changes building cancellation policy. Unsafe state selects a 65 cancellation policy; safe state returns it to zero.

This is evidence of survival-driven capital reallocation.

Disposition: PRESERVE + FORMALIZE as emergency policy.

## 10. Economic authority boundary

Shadow should answer:

Can we fund it?
How should resources be protected?
When is the transaction feasible?
How should temporary reservation be released?
What completion evidence advances progression?

AEGIS should answer:

Why are we doing it?
What capability is required?
Which competing requirement wins?
When should the commitment be cancelled or preempted?

## 11. Required improvements

1. Attribute reservations to explicit commitments.
2. Add expiry and release semantics.
3. Distinguish policy, commitment and transaction reservation.
4. Preserve minimum viable funding during preemption.
5. Add starvation/deadlock observability.
6. Keep affordability separate from strategic desirability.
7. Make postconditions explicit per transaction type.
8. Prevent unauthorized production rules from mutating strategic reservations.

## Conclusion

The economic donor is the part of Shadow least justified for wholesale replacement. It already implements resource protection, transaction feasibility, execution sequencing and progression feedback. The correct AEGIS move is to supply better intent and commitment semantics above it.
