import os
import subprocess
import sys
import shutil

def instalar():
    print("\n" + "=" * 40)
    print("🚀 CONFIGURADOR DE AMBIENTE - SISTEMA CRUD")
    print("=" * 40)

    # 1. Instalação de dependências
    print("\n📦 Passo 1: Instalando bibliotecas do requirements.txt...")
    try:
        # Usa o sys.executable para garantir que instale no mesmo Python/Venv que está rodando
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Bibliotecas instaladas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        print("💡 Dica: Verifique se o seu pip está atualizado ou se o arquivo requirements.txt existe.")

    # 2. Configuração do arquivo de ambiente (.env)
    print("\n📝 Passo 2: Configurando variáveis de ambiente...")
    if not os.path.exists(".env"):
        # Prioridade 1: Copiar do .env.example
        if os.path.exists(".env.example"):
            print("➡ Criando .env a partir do .env.example...")
            shutil.copy(".env.example", ".env")
        else:
            # Prioridade 2: Criar um padrão funcional para PostgreSQL local
            print("➡ Criando novo arquivo .env com valores padrão...")
            with open(".env", "w") as f:
                f.write('DB_USER=postgres\n')
                f.write('DB_PASS=SUA_SENHA_AQUI\n')
                f.write('DB_NAME=empresa\n')
                f.write('DB_HOST=localhost\n')
                f.write('DB_PORT=5432\n')

        print("⚠️  IMPORTANTE: Edite o arquivo '.env' e coloque a senha do seu banco local.")
    else:
        print("✅ Arquivo .env já detectado. Nenhuma alteração feita.")

    print("\n" + "=" * 40)
    print("✨ TUDO PRONTO!")
    print("\n🔹 OPÇÃO A (Docker):")
    print("   docker compose run --rm app")
    print("\n🔹 OPÇÃO B (Local):")
    print("   python main.py")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    instalar()