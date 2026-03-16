import time
import sys
from database import (
    criar_tabela_inicial,
    cadastrar_funcionario,
    listar_funcionario,
    atualizar_nome_funcionario,
    atualizar_departamento_funcionario,
    deletar_funcionario
)


def apresentacao():
    print("\n" + "=" * 30)
    print("   SISTEMA DE FUNCIONÁRIOS")
    print("=" * 30)
def mostrar_funcionario(id):
    busca_BD = listar_funcionario(id)
    if busca_BD is None:
        print('ID NÃO ENCONTRADO!')
        return False

    if type(busca_BD) == tuple:
        id_funcionario, nome, departamento = busca_BD
        dados_retornados = f'ID: {id_funcionario} | NOME: {nome} | DEPARTAMENTO: {departamento}\n'
        print(dados_retornados)
        return True

def iniciar_banco():
    tentativas = 5
    while tentativas > 0:
        try:
            criar_tabela_inicial()
            print("✅ Conexão com o banco estabelecida!")
            return True
        except Exception as e:
            print(f"⏳ Aguardando banco de dados... ({tentativas} tentativas restantes)")
            time.sleep(3)
            tentativas -= 1
    print("❌ Não foi possível conectar ao banco de dados.")
    return False

if __name__ == "__main__":
    if not iniciar_banco():
        print("❌ Erro: O banco de dados não está respondendo.")
        sys.exit(1)

    while True:
        apresentacao()
        resposta = input("""
        1 - CADASTRAR FUNCIONÁRIO
        2 - LISTAR FUNCIONÁRIO
        3 - ATUALIZAR FUNCIONÁRIO
        4 - DELETAR FUNCIONÁRIO
        S - SAIR
            """).upper().strip()

        if resposta == '1':
            nome_escolhido = input('DIGITE NOME: ')
            departamento_escolhido = input('DIGITE DEPARTAMENTO: ')

            print(f'\nNOME: {nome_escolhido} | DEPARTAMENTO: {departamento_escolhido}\n')

            confirmacao = input('CONFIRMA? (S/N)').upper()

            if confirmacao != 'S':
                print('VOLTANDO AO MENU PRINCIPAL...')
                continue

            cadastrar_funcionario(nome_escolhido, departamento_escolhido)
            print('FUNCIONÁRIO CADASTRADO COM SUCESSO!')
        elif resposta == '2':
            try:
                id_pesquisado = int(input('\nDIGITE ID DO FUNCIONÁRIO: '))
                mostrar_funcionario(id_pesquisado)
            except ValueError:
                print('ERRO: POR FAVOR, DIGITE APENAS NÚMEROS PARA O ID!')
                continue
            except Exception as e:
                print(f'ERRO INESPERADO: {e}')
                print('VERIFIQUE A CONEXÃO COM O BANCO DE DADOS OU OS DADOS DIGITADOS')
                continue
        elif resposta == '3':
            try:
                id_pesquisado = int(input('\nDIGITE ID DO FUNCIONÁRIO: '))
                id_valido = mostrar_funcionario(id_pesquisado)

                if id_valido:
                    opcao_alteracao = input("1 - ALTERAR NOME | 2 - ALTERAR DEPARTAMENTO ").upper()

                    if opcao_alteracao == '1':
                        novo_nome = input('QUAL SERÁ O NOVO NOME? ')
                        checagem_nome = input(f'\nNOVO NOME: "{novo_nome}". CONFIRMA? (S/N) ').upper()

                        if checagem_nome != 'S':
                            print('VOLTANDO AO MENU PRINCIPAL...')
                            continue

                        atualizar_nome_funcionario(id_pesquisado, novo_nome)
                        print('DADOS ATUALIZADOS COM SUCESSO!')
                        continue
                    elif opcao_alteracao == '2':
                        novo_departamento = input('QUAL SERÁ O NOVO DEPARTAMENTO? ')
                        checagem_departamento = input(f'\nNOVO DEPARTAMENTO: "{novo_departamento}". CONFIRMA? (S/N) ').upper()

                        if checagem_departamento != 'S':
                            print('VOLTANDO AO MENU PRINCIPAL...')
                            continue

                        atualizar_departamento_funcionario(id_pesquisado, novo_departamento)
                        print('DADOS ATUALIZADOS COM SUCESSO!')
                        continue
                    else:
                        print('ERRO! VOLTANDO AO MENU PRINCIPAL...')
                        continue
            except ValueError:
                print('ERRO: POR FAVOR, DIGITE APENAS NÚMEROS PARA O ID!')
                continue
            except Exception as e:
                print(f'ERRO INESPERADO: {e}')
                print('VERIFIQUE A CONEXÃO COM O BANCO DE DADOS OU OS DADOS DIGITADOS')
                continue
        elif resposta == '4':
            try:
                id_pesquisado = int(input('\nDIGITE ID DO FUNCIONÁRIO: '))
                id_valido = mostrar_funcionario(id_pesquisado)

                if id_valido:
                    confirmacao_delete = input('TEM CERTEZA QUE DESEJA EXCLUIR ESTE REGISTRO? (S/N)').upper()

                    if confirmacao_delete != 'S':
                        print('VOLTANDO AO MENU PRINCIPAL...')
                        continue

                    deletar_funcionario(id_pesquisado)
                    print('REGISTRO EXCLUÍDO COM SUCESSO!')
                    continue
            except ValueError:
                print('ERRO: POR FAVOR, DIGITE APENAS NÚMEROS PARA O ID!')
                continue
            except Exception as e:
                print(f'ERRO INESPERADO: {e}')
                print('VERIFIQUE A CONEXÃO COM O BANCO DE DADOS OU OS DADOS DIGITADOS')
                continue
        elif resposta == 'S':
            break
        else:
            continue