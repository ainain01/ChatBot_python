from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Use offline model path
print("Loading model...")
model_path = "./model_cache/models--microsoft--DialoGPT-small/snapshots/49c537161a457d5256512f9d2d38a87d81ae0f0e"

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # Encode user input and generate response
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt").to(device)
    output_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    response_text = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return jsonify({"reply": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
