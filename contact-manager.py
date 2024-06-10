def criar_contato(nome, telefone):
    contato = {"NOME": nome, "TELEFONE": telefone}
    return contato

def adicionar_contato(lista_contatos, dicionario_contatos):
    lista_contatos.append(dicionario_contatos)
    return lista_contatos

def remover_contato_por_telefone(lista_contatos, telefone):
    for elemento in lista_contatos:
         if (elemento["TELEFONE"] == telefone):
             lista_contatos.remove(elemento)
    return lista_contatos

def listar_contatos(dicionario_contatos):
    print("Lista de contatos:")
    for nome, telefone in dicionario_contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")
