import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AjenticAI API",
    description="Agentic AI Backend & Playground",
    version="1.0.0"
)

class PromptRequest(BaseModel):
    prompt: str
    provider: str = "groq"  # "groq", "mistral", or "gemini"

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>⚡ AjenticAI Hub</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg: #0b0f19;
                --card-bg: rgba(23, 32, 54, 0.7);
                --card-border: rgba(255, 255, 255, 0.08);
                --accent: #38bdf8;
                --accent-glow: rgba(56, 189, 248, 0.25);
                --text: #f8fafc;
                --text-muted: #94a3b8;
                --green: #10b981;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                font-family: 'Inter', sans-serif;
                background: radial-gradient(circle at 50% 0%, #172554 0%, var(--bg) 75%);
                color: var(--text);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem 1rem;
            }
            .container {
                max-width: 650px;
                width: 100%;
                background: var(--card-bg);
                backdrop-filter: blur(16px);
                border: 1px solid var(--card-border);
                border-radius: 1.5rem;
                padding: 2.5rem;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5), 0 0 40px var(--accent-glow);
                text-align: center;
            }
            .badge {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: rgba(16, 185, 129, 0.15);
                border: 1px solid rgba(16, 185, 129, 0.3);
                color: #34d399;
                padding: 0.35rem 0.9rem;
                border-radius: 9999px;
                font-size: 0.85rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
            }
            .dot {
                width: 8px;
                height: 8px;
                background: #34d399;
                border-radius: 50%;
                box-shadow: 0 0 10px #34d399;
            }
            h1 {
                font-family: 'Outfit', sans-serif;
                font-size: 2.4rem;
                font-weight: 700;
                background: linear-gradient(135deg, #ffffff 0%, #93c5fd 50%, #38bdf8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.75rem;
            }
            p.sub {
                color: var(--text-muted);
                font-size: 1.05rem;
                line-height: 1.6;
                margin-bottom: 2rem;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
                margin-bottom: 2rem;
            }
            .stat-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid var(--card-border);
                border-radius: 0.85rem;
                padding: 1rem 0.5rem;
                text-align: center;
            }
            .stat-title {
                font-size: 0.8rem;
                color: var(--text-muted);
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .stat-value {
                font-size: 1.1rem;
                font-weight: 600;
                margin-top: 0.25rem;
                color: #e2e8f0;
            }
            .btn-group {
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
            }
            .btn {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.8rem 1.6rem;
                border-radius: 0.75rem;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: all 0.2s ease;
            }
            .btn-primary {
                background: linear-gradient(135deg, #2563eb, #0284c7);
                color: white;
                box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
            }
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
            }
            .btn-secondary {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid var(--card-border);
                color: var(--text);
            }
            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.1);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="badge">
                <span class="dot"></span> Service Live & Running
            </div>
            <h1>⚡ AjenticAI Engine</h1>
            <p class="sub">Your agentic workflows, LangChain chains, and LLM integrations are successfully deployed on Render.</p>
            
            <div class="grid">
                <div class="stat-card">
                    <div class="stat-title">Platform</div>
                    <div class="stat-value">Render</div>
                </div>
                <div class="stat-card">
                    <div class="stat-title">Framework</div>
                    <div class="stat-value">FastAPI</div>
                </div>
                <div class="stat-card">
                    <div class="stat-title">Python</div>
                    <div class="stat-value">3.11.9</div>
                </div>
            </div>

            <div class="btn-group">
                <a href="/docs" class="btn btn-primary" target="_blank">📖 Open Interactive API Docs</a>
                <a href="/health" class="btn btn-secondary">🩺 Health Check</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AjenticAI",
        "has_groq_key": bool(os.environ.get("GROQ_API_KEY")),
        "has_mistral_key": bool(os.environ.get("MISTRAL_API_KEY")),
        "has_gemini_key": bool(os.environ.get("GEMINI_API_KEY")),
    }

@app.post("/ask")
def ask_llm(req: PromptRequest):
    provider = req.provider.lower()
    prompt = req.prompt
    
    if provider == "groq":
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="GROQ_API_KEY not configured")
        from groq import Groq
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return {"response": chat_completion.choices[0].message.content, "provider": "groq"}
    
    elif provider == "mistral":
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="MISTRAL_API_KEY not configured")
        from mistralai.client import Mistral
        client = Mistral(api_key=api_key)
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
        )
        return {"response": chat_response.choices[0].message.content, "provider": "mistral"}
        
    else:
        raise HTTPException(status_code=400, detail=f"Provider '{provider}' not supported. Choose 'groq' or 'mistral'.")

def main():
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting AjenticAI server on port {port}...")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

if __name__ == "__main__":
    main()
