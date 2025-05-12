import httpx
from config import API_KEY, API_URL

def submit_result(transcript_id, result_json):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "transcript_id": transcript_id,
        "result": result_json
    }
    try:
        response = httpx.post(API_URL, json=payload, headers=headers)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
