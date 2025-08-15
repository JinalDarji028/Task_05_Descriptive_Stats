# Prompt Refinement Notes — 2013 Dataset

## Case 1
**Initial (Failed):** “Who was the most improved player?”
- **Issue:** Dataset doesn’t define “improved” (no prior-year comparison, no player trend metrics).

**Refined:** “Which player had the highest total points (G + A) in 2013?”
- **Why it works:** Uses available per-player G/A if you have a player table; otherwise mark N/A.
- **Expected outcome:** ✅ LLM can rank by Pts when provided.

---

## Case 2
**Initial (Failed):** “What was Syracuse’s shooting percentage in away games?”
- **Issue:** Dataset doesn’t include home/away split for shots/goals.

**Refined:** “What was Syracuse’s overall shooting percentage for 2013?”
- **Why it works:** We have Shots (700) and Goals (332). Shooting % = Goals/Shots.
- **Expected outcome:** ✅ LLM computes 332/700 ≈ 47.43%.
- **Note:** If using Shots on Goal % = SOG/Shots, it’s 533/700 ≈ 76.14%.

---

## Case 3
**Initial (Ambiguous):** “Which half did Syracuse dominate?”
- **Issue:** The 2013 PDF groups stats by halves (or periods), but wording can confuse the model.

**Refined:** “Using ‘Goals by Period’ for 2013, which half shows the larger Syracuse goal differential vs opponents?”
- **Why it works:** Forces model to compare Syracuse vs Opponents within the exact table/rows you paste.
