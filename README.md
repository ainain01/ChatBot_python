# ChatBot_python
Here's a professional and clear `README.md` file for your chatbot project using Hugging Face's DialoGPT with both **online** and **offline** options:

---

### ✅ `README.md`

# 🧠 DialoGPT Chatbot (Online + Offline Mode)

This is a Flask-based chatbot interface powered by Microsoft's [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium) for generating conversational responses. It supports both **online model loading from Hugging Face** and **offline usage** from a locally cached model.

---

## 🚀 Features

- Built using **Flask** for the backend
- Uses **Transformers (DialoGPT)** for generating replies
- Supports **GPU acceleration** via PyTorch
- Two modes:
  - `chat_api.py`: Loads model from Hugging Face online
  - `chatbot_offline.py`: Loads model from local cache (offline mode)

---

## 📂 Project Structure

```

.
├── chat\_api.py              # Online mode chatbot using Hugging Face API
├── chatbot\_offline.py       # Offline mode chatbot using local model files
├── templates/
│   └── index.html           # Frontend interface
├── model\_cache/             # Offline model storage
│   └── models--microsoft--DialoGPT-small/...
└── README.md                # You're reading it!

````

---

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install flask torch transformers
````

To run on GPU, ensure you have:

* CUDA-compatible GPU
* PyTorch with CUDA support installed

---

## 🌐 Running the App (Online Mode)

```bash
python chat_api.py
```

This will:

* Load the model from Hugging Face Hub (`DialoGPT-medium`)
* Start a Flask server at `http://localhost:5000/`

---

## 📴 Running the App (Offline Mode)

Ensure you have the DialoGPT model downloaded locally. You can do this using:

```bash
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/DialoGPT-small"
AutoTokenizer.from_pretrained(model_name, cache_dir="./model_cache")
AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./model_cache")
```

Then run:

```bash
python chatbot_offline.py
```

---

## 🖥️ Frontend UI

A basic HTML interface is available at `/`:

* Send messages to the chatbot
* Receive AI-generated responses in real-time

Customize `templates/index.html` to change the design.

---

## 🤖 Example API Usage

Send a POST request to `/chat`:

```json
POST /chat
Content-Type: application/json

{
  "message": "Hello, how are you?"
}
```

Response:

```json
{
  "reply": "I'm doing great, thanks! How can I help you today?"
}
```

---

## 📌 Notes

* Offline mode avoids internet dependencies (great for secure or low-bandwidth environments).
* You can switch between `DialoGPT-small`, `medium`, or `large` depending on memory constraints.

---

## 📃 License

MIT License. See `LICENSE` for details.

---

## 🙌 Author

**Muhammad AinAin Khan**
[GitHub](https://github.com/ainain01) | [LinkedIn](https://linkedin.com/in/mainain)
📧 [ainainkhan714@gmail.com](mailto:ainainkhan714@gmail.com)

```
