from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.configurations.configuration import configuration
from api.utilities.app_response import AppResponse

app = FastAPI(
    title="Meet Kimmy - My Digital Sidekick!",
    description="Kimmy is a smart, friendly, and helpful AI chatbot designed to be my portfolio's ultimate tour guide. She's here to answer all your questions about me (JC) — from my work experience, technical skills, and portfolio projects to my goals, passions, and accolades.",
    version="1.0.0"
)

# MIDDLEWARE FOR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ROOT ENDPOINT
@app.get("/", tags=["Root"])
async def read_root():
    return AppResponse.send_successful(
        data=None,
        message="Welcom to the Official Documentation of my Personal ChatBot (Kimmy)",
        code=200
    )

# RUN THE SERVER
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.main:app",
        port= int(configuration["app"]["port"]),
        reload=True
    )