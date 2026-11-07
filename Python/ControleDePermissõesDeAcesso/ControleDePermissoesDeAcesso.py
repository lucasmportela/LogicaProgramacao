# 6: Controle de Permissões de Acesso - RBAC
# Uma rota administrativa da API exige o seguinte conjunto de permissões para ser
# executada:
# PERMISSOES_ROTA =  {"AUTH_READ, "AUTH_WRITE", "DB_ADMIN, "LOG_EXPORT"}
# O sistema recuperou as permissões atribuídas a dois perfis de usuários distintos:
# ● usuario_analista = {"AUTH_READ", "LOG_EXPORT"}
# ● usuario_techlead = {"AUTH_READ", "AUTH_WRITE", "DB_ADMIN",
# "LOG_EXPORT", "BILLING_ACCESS"}
# Desenvolva a lógica que:
# 1. Identifique se cada um dos usuários tem acesso permitido à rota (todas as
# permissões de permissoes_rota devem estar contidas no conjunto do
# usuário).
# 2. Para o usuário que não tiver acesso, calcule e exiba via diferença entre
# conjuntos (difference ou operador -) exatamente
permissoes_rota = {"AUTH_READ","AUTH_WRITE","DB_ADMIN","LOG_EXPORT"}
usuario_analista = {"AUTH_READ", "LOG_EXPORT"}
usuario_techlead = {"AUTH_READ", "AUTH_WRITE", "DB_ADMIN","LOG_EXPORT", "BILLING_ACCESS"}
if permissoes_rota.issubset(usuario_analista):
    print("Analista: Acesso concedido")
else:
    print("Analista: Acesso negado")
    faltantes = permissoes_rota - usuario_analista
    print("Permissões faltantes:", faltantes)
if permissoes_rota.issubset(usuario_techlead):
    print("Tech Lead: Acesso concedido")
else:
    print("Tech Lead: Acesso negado")
    faltantes = permissoes_rota - usuario_techlead
    print("Permissões faltantes:", faltantes)
