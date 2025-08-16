Task 05 – Descriptive Statistics and LLM Evaluation

## 📘 Overview

This project is part of Research Task 05: **Descriptive Statistics and Large Language Models (LLMs)**. The goal is to explore how well LLMs like ChatGPT interpret and reason over real-world structured data. The dataset includes 2013 performance statistics of the Syracuse University Women’s Lacrosse team.

The task involves:
- Extracting stats from a PDF
- Cleaning and saving structured data as CSV files
- Asking LLMs natural language questions based on that data
- Evaluating when the LLM gets the answer right — or fails

---

## 📊 Dataset

The dataset was taken from the SU Athletics official page: 

It includes:
- Game results  
- Goals by half  
- Saves, shots, and shots on goal  
- Win/loss summary  

⚠️ The raw PDF is excluded from this GitHub repository as per project instructions.

---

## 🧱 Project Structure

Task_05_Descriptive_Stats/
├── data/ # PDF file (excluded)
├── scripts/ # PDF extraction and processing scripts
│ └── descriptive_stats.py
├── outputs/
│ └── extracted_tables/ # Extracted and cleaned CSV tables
├── prompts/
│ └── prompt_examples.txt # Prompts, GPT responses, and evaluations
├── README.md

## 🛠 Key Components

- `descriptive_stats.py`: Extracts all tables from the PDF and formats them into clean CSV files.
- `prompt_examples.txt`: Includes prompts submitted to ChatGPT, responses, and whether the model succeeded or failed.

---

## 🧠 LLM Prompt Evaluation

This task emphasizes understanding the capabilities and limitations of LLMs.

### ✅ Example Success
**Prompt:** How many total goals did Syracuse score?  
**Response:** 332  
**Evaluation:** ✅ Correct based on the table

### ❌ Example Failure
**Prompt:** Who was the top scorer?  
**Response:** "Kayla Treanor with 79 goals"  
**Evaluation:** ❌ Hallucinated player and stat not present in the dataset

All such evaluations are recorded in the `prompts/` folder.

---

## 🚀 How to Run the Code

In terminal:- 

python scripts/descriptive_stats.py

This will extract all tables from the PDF and save them as CSVs to:
outputs/extracted_tables/ 

period2-expansion

## Period 2 Expansion — 2013 Data

- Added `prompts/expanded_prompts_2013.txt` (even split of success/failure prompts).
- Added `prompt_refinement_2013.md`, `insights_2013.md`, and `ai_street_interview_2013.md`.
- Focus remains on evaluating LLMs on the 2013 SU Women’s Lacrosse tables (goals, saves, shots, SOG, record).

main
