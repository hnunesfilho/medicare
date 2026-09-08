# databse conexão
import pymysql

# —————————————— CONFIGURAÇÕES ——————————————
# Altere abaixo com os dados do SEU MySQL
host = 'localhost'
usuario = 'root'
senha = ''          # sua senha do mysql
banco = 'medicare_db'
# ————————————————————————————————————————————

def obter_conexao():
    """
    Cria e retorna uma conexão com o banco MySQL.
    Sempre que precisar do banco, chame essa função.
    """
    conexao = pymysql.connect(
        host=host,
        user=usuario,
        password= senha,
        database=banco,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)    # retorna dicionários
    )
    return conexao
def testar_conexao():
    """Testa se a conexao está funcionando. Use para depurar."""
    try:
        conn = obter_conexao()
        print('✅ Conexão com MySQL OK!')
        conn.close()
    except Exception as e:
        print(f'❌ Erro na conexão: {e}')
# Teste ao rodar o arquivo diretamente
if __name__ == '__main__':
    testar_conexao()

