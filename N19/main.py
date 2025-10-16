# main.py
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import tempfile
import os
from spell_matcher import detect_spell
# import whisperx
import whisper

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return f.read()

@app.post("/transcribe")
def transcribe_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name
    model = whisper.load_model("base", device="cpu")  # Use smaller model for speed
    result = model.transcribe(tmp_path)
    text = result["text"]
    spell = detect_spell(text, cutoff=0.1)  # Lower cutoff for fuzzy matching
    os.remove(tmp_path)
    return JSONResponse({"transcription": text, "spell": spell})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
