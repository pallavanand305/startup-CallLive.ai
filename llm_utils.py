import openai

def analyze_transcript(transcript: str):
    prompt = f"""
You are an AI assistant analyzing customer support transcripts.

Transcript:
{transcript}

1. Provide a concise summary.
2. List key customer concerns.
3. Sentiment (positive, neutral, negative).
4. Agent performance (good, average, poor).

Return as JSON: {{
  "summary": "...",
  "concerns": [...],
  "sentiment": "...",
  "performance": "..."
}}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message['content']
