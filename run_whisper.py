import os

from whisper import load_model
from whisper.utils import get_writer
from whisper.transcribe import transcribe

# parser.add_argument("--model", default="small", type=valid_model_name, help="name of the Whisper model to use")
# parser.add_argument("--task", type=str, default="transcribe", choices=["transcribe", "translate"], help="whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')")
# parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu", help="device to use for PyTorch inference")
# parser.add_argument("--output_format", "-f", type=str, default="all", choices=["txt", "vtt", "srt", "tsv", "json", "all"], help="format of the output file; if not specified, all available formats will be produced")
# parser.add_argument("--model_dir", type=str, default=None, help="the path to save model files; uses ~/.cache/whisper by default")
# parser.add_argument("--temperature", type=float, default=0, help="temperature to use for sampling")

os.makedirs("json", exist_ok=True)
os.makedirs("vtt", exist_ok=True)
os.makedirs("txt", exist_ok=True)

print("loading model")
model = load_model("small", device="cuda")
print("loaded model")
json_writer = get_writer("json", "json")
vtt_writer = get_writer("vtt", "vtt")
txt_writer = get_writer("txt", "txt")

for filename in os.listdir('videos'):
    print(filename)
    audio_path = f"videos/{filename}"
    json_filename = filename.replace(".webm", ".json")
    json_path = f"json/{json_filename}"
    if os.path.exists(json_path):
        print(f"{json_path} exists, skip")
        continue
    result = transcribe(model, audio_path, verbose=True, language="en")
    json_writer(result, audio_path)
    vtt_writer(result, audio_path)
    txt_writer(result, audio_path)
