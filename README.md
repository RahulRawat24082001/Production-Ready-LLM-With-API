# 🚀 Production-Ready LLM API with FastAPI & TinyLlama

This project is a **production-ready Large Language Model (LLM) service** built using **FastAPI** and powered by **TinyLlama**. It exposes a scalable, low-latency REST API for text generation and can be easily deployed in cloud or on-prem environments.

---

## ✨ Features

* ⚡ **FastAPI-based REST API** for high-performance inference
* 🧠 **TinyLlama** for lightweight, efficient LLM inference
* 🏭 **Production-ready architecture** (modular, scalable, maintainable)
* 🔒 Input validation & error handling
* 📈 Easy to integrate with frontend, microservices, or agents
* 🐳 Docker-ready for containerized deployment
* 🔁 Supports batch and single-prompt inference


## 🧠 Model Details

* **Model**: TinyLlama
* **Use case**: Lightweight text generation, chat, and prompt-based inference
* **Why TinyLlama?**

  * Low memory footprint
  * Fast inference
  * Ideal for edge devices and cost-efficient deployments

---

## 🚦 API Endpoints

### 🔹 Generate Text

**POST** `/generate`

**Request Body**

```json
{
  "prompt": "Explain transformers in simple terms",
  "max_tokens": 150,
  "temperature": 0.7
}
```

**Response**

```json
{
  "response": "Transformers are neural network models that..."
}
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/llm-fastapi-tinyllama.git
cd llm-fastapi-tinyllama
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Visit API docs:

* Swagger UI → `http://localhost:8000/docs`
* ReDoc → `http://localhost:8000/redoc`

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t tinyllama-api .
```

### Run Container

```bash
docker run -p 8000:8000 tinyllama-api
```

---

## 📈 Production Considerations

* ✅ Model loaded once at startup (no reload per request)
* ✅ Async FastAPI endpoints
* ✅ Configurable inference parameters
* ✅ Ready for:

  * Kubernetes
  * AWS ECS / EKS
  * Azure Container Apps
* 🔄 Can be extended with:

  * Redis caching
  * Request queuing
  * Authentication (JWT / API keys)
  * Observability (Prometheus, OpenTelemetry)

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🔐 Security Notes

* Validate and sanitize user inputs
* Limit max tokens to prevent abuse
* Add rate limiting for public APIs
* Use HTTPS in production

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **TinyLlama**
* **Uvicorn**
* **Docker**

