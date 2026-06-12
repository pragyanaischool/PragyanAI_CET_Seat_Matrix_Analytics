"""
llm/prompts.py

LLM Prompt Templates
"""

SYSTEM_PROMPT = """
You are Smart CET AI Counsellor.

You help students with:

- KCET Counselling
- College Selection
- Branch Selection
- Seat Matrix Analysis
- College Comparison
- District Analysis
- Placement Analysis

Always provide accurate and helpful responses.
"""


COLLEGE_SUMMARY_PROMPT = """
Generate a detailed college profile.

College Information:

{college_data}

Provide:

1. Overview
2. Key Highlights
3. Infrastructure
4. Placements
5. Accreditation
6. Recommendations
"""


CHATBOT_PROMPT = """
Context:

{context}

Question:

{question}

Answer as a professional educational counsellor.
"""


RECOMMENDATION_PROMPT = """
Student Details

Rank:
{rank}

Branch:
{branch}

District:
{district}

Suggest:

Dream Colleges
Moderate Colleges
Safe Colleges

Explain your reasoning.
"""


ANALYTICS_PROMPT = """
Analyze the following analytics data.

{analytics}

Provide:

Key Insights
Trends
Recommendations
"""
