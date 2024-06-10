def criar_contato(nome, telefone):
    contato = {"Nome": nome, "Telefone": telefone}
    return contato


def adicionar_contato(lista_contatos, dicionario_contatos):
    lista_contatos.append(dicionario_contatos)
    return lista_contatos


def remover_contato_por_telefone(lista_contatos, telefone):
    for elemento in lista_contatos:
        if elemento["Telefone"] == telefone:
            lista_contatos.remove(elemento)
    return lista_contatos


def listar_contatos(lista_contatos):
    print("Lista de contatos:")
    for i in range(len(lista_contatos)):
        contato = lista_contatos[i]
        print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")