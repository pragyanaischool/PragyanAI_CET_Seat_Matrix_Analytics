"""
config/prompts.py

Master Prompts
"""

COLLEGE_RESEARCH_PROMPT = """

You are an educational researcher.

Analyze the college and provide:

1. College Overview
2. History
3. Accreditation
4. Placements
5. Infrastructure
6. Hostel
7. Fees
8. Rankings
9. Recruiters
10. Overall Recommendation

College:
{college_name}

"""

COLLEGE_CHAT_PROMPT = """

You are Smart CET AI Counsellor.

Answer using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

SEAT_MATRIX_EXTRACTION_PROMPT = """

Extract the following information.

Return JSON only.

Fields:

college_name
district
course_name
total_intake
kea_seats
hk_seats
rk_seats
year

Input:

{text}

"""

RECOMMENDATION_PROMPT = """

Recommend colleges.

Student Rank:
{rank}

Branch Preference:
{branch}

District Preference:
{district}

Provide:

Dream Colleges
Moderate Colleges
Safe Colleges

Reason for each recommendation.

"""

DISTRICT_EXTRACTION_PROMPT = """

Identify district information.

College Name:
{college_name}

Address:
{address}

Return district only.

"""

SUMMARY_PROMPT = """

Generate detailed summary.

Input:
{text}

Provide:

Overview
Key Insights
Important Statistics
Recommendations

"""
