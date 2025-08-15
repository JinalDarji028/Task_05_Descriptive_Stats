# Insights — Syracuse Women’s Lacrosse (2013)

## What the LLM handled well (✅)
- **Direct lookups** from tables: correctly returned totals such as
  - Goals: **Syracuse 332**, Opponents 188
  - Saves: **Syracuse 129**, Opponents 201
  - Shots: **Syracuse 700**, Opponents 413
  - Shots on Goal (SOG): **Syracuse 533**, Opponents 317
- **Simple math when inputs are provided in the prompt**:
  - SOG% (defined in the prompt as SOG ÷ Shots): **533 ÷ 700 ≈ 76.14%** (Syracuse).
- **Comparisons** (max/min, higher/lower) once the relevant rows/columns are pasted with the question.

## Where the LLM struggled (❌)
- **Missing dimensions** not in the dataset:
  - Home vs Away splits (e.g., “shooting % in away games”).
  - Per-period penalties (e.g., “yellow cards by period”).
  - Game-winning goals (no GWG column).
- **Subjective/undefined metrics**:
  - “Most improved player” (no prior-season baseline or rule for “improvement”).
  - “Who should be a game changer and why?” (requires criteria definition).
- **Ambiguous phrasing**:
  - “Second half” (season vs game) or “best game” (best by which metric?).

## Prompting patterns that worked for accuracy (🎯)
- **Paste the exact table snippet** with the question (compact, clean headings).
- **Define the formula in the prompt** (e.g., *Shooting % = Goals ÷ Shots*).
- **Ask for uncertainty**: “If the data is insufficient, say so rather than guessing.”
- **Constrain the scope**: “Answer only from the table provided below.”

## Example prompt template (reliable)
> *Using only the table below, answer the question. If the data is insufficient, say “not determinable from this table.”*  
> **Table:** (paste the 2–6 relevant rows/cols)  
> **Question:** *What is Syracuse’s SOG%? Use SOG ÷ Shots.*

## Takeaway for coaching questions (🧠➡️🏑)
- The 2013 tables support **efficiency** insights (e.g., SOG%, goal differential by period) better than player-level narratives.
- For “offense vs defense” questions, define clear metrics (e.g., *Offense = Goals/Shot*, *Defense = Saves/Shots on goal allowed*), paste those numbers, and ask the LLM to compare.

## Next steps (Period 2+)
- Add a **metrics.md** with explicit definitions (Shooting %, SOG%, Goal Diff by half) so prompts are unambiguous.
- If you obtain player-level CSVs, add prompts for **Pts (G+A)** ranking and **usage efficiency** (G/Shot).
