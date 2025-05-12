from celery import Celery
from llm_utils import analyze_transcript
from submit import submit_result
import json

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def process_transcript(transcript_id, content):
    print(f"Processing {transcript_id}...")
    try:
        result_text = analyze_transcript(content)
        result_json = json.loads(result_text)
        status, response = submit_result(transcript_id, result_json)
        print(f"{transcript_id} submitted: {status}")
    except Exception as e:
        print(f"Error with {transcript_id}: {e}")
