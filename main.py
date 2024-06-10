import contact_manager

contatos = []
contato1 = contact_manager.criar_contato("Gutemberg", 83986731485)
contato2 = contact_manager.criar_contato("Amanda Lanay", 83987498273)

contact_manager.adicionar_contato(contatos, contato1)
contact_manager.adicionar_contato(contatos, contato2)

contact_manager.listar_contatos(contatos)

contact_manager.remover_contato_por_telefone(contatos, 83986731485)

contact_manager.listar_contatos(contatos)
