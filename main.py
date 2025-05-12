import os
from tasks import process_transcript

TRANSCRIPT_DIR = "./transcripts"

def load_transcripts():
    for file in os.listdir(TRANSCRIPT_DIR):
        if file.endswith(".txt"):
            path = os.path.join(TRANSCRIPT_DIR, file)
            with open(path, "r") as f:
                content = f.read()
            yield file.replace(".txt", ""), content

def dispatch_jobs():
    for transcript_id, content in load_transcripts():
        process_transcript.delay(transcript_id, content)

if __name__ == "__main__":
    dispatch_jobs()
