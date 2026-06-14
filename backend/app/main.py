from fastapi import FastAPI
from pydantic_settings import BaseSettings
from sqlmodel import create_engine, Session, text

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/dse_learn_lab"
    PROJECT_NAME: str = "DSE.LearnLab API"

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Plataforma Open Source para Aprendizagem Baseada em Prática, Pesquisa, Escrita e Evidências."
)

# Cria o engine do SQLAlchemy/SQLModel com fallback dinâmico para SQLite
try:
    # Se a URL for do postgres, tentamos carregar o dialeto para ver se o driver está instalado
    if settings.DATABASE_URL.startswith("postgresql"):
        import psycopg2
    engine = create_engine(settings.DATABASE_URL)
    # Testa a inicialização do dialeto
    _ = engine.dialect
except (ImportError, Exception) as e:
    print(f"Alerta: Falha ao carregar driver PostgreSQL ({e}). Usando SQLite local (sqlite:///dse_learn_lab.db) como fallback.")
    engine = create_engine("sqlite:///dse_learn_lab.db")


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo ao DSE.LearnLab — Laboratório de Aprendizagem, Pesquisa e Produção de Conhecimento",
        "philosophy": "Aprendizagem baseada em prática, escrita, pesquisa e evidências.",
        "status": "online"
    }

@app.get("/health")
def health_check():
    db_status = "healthy"
    try:
        # Tenta executar uma consulta simples de teste no banco de dados
        with Session(engine) as session:
            session.exec(text("SELECT 1")).one()
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    return {
        "api_status": "healthy",
        "database_status": db_status
    }
