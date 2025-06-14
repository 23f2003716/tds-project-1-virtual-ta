# TDS 2025-05 Project 1 - Virtual TA
a virtual Teaching Assistant Discourse responder.
---
## ✅ Prerequisites

Before setting up, ensure you have the following installed:

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (Python package and project manager)
---
### 1. Clone the Repository

```bash
git clone https://github.com/23f2003716/tds-project-1-virtual-ta.git
cd tds-project-1-virtual-ta
```

### 2. Environment Configuration

Before running the application, you need to create a `.env` file in the root directory of the project. This file will store your environment variables securely.

- **📄 Create a `.env` file with the following content:**
  
    ```env
    FLASK_DEBUG = False
    FLASK_RUN_HOST = 0.0.0.0
    FLASK_RUN_PORT = 5000
    SECRET_KEY = <your-secret-key>
    GEMINI_API_KEY = <your-gemini-api-key>
    ```

> ⚠️ Replace the placeholder values (`your-secret-key`, `your-gemini-api-key`) with your actual credentials.



### 3. Run the Flask Server

```bash
uv run flask run
```

---

## 🌐 API Endpoint

Once the Flask development server is running, the backend will be available at:

```
http://127.0.0.1:5000/
```