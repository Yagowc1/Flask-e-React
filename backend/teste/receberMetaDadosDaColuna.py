# from sqlalchemy import create_engine, MetaData

# # Criar uma instância de engine do SQLAlchemy
# engine = create_engine('sqlite:///backend\instance\mydatabase.db')

# # Criar uma instância de MetaData
# metadata = MetaData()

# # Refletir as tabelas existentes no banco de dados para o objeto MetaData
# metadata.reflect(bind=engine)

# # Agora você pode acessar as tabelas refletidas
# for table in metadata.tables.values():
#     print("Nome da tabela:", table.name)
#     for column in table.c:
#         print("  - Nome da coluna:", column.name)
#         print("    - Tipo da coluna:", column.type)
#         print("    - Restrições da coluna:", column.constraints)
#         print("    - É nulo?", column.nullable)
#         print("    - Valor padrão:", column.default)
#         print("    - Comentário da coluna:", column.comment)
#         print("    - Outras propriedades da coluna:", column.info)