pais = {'Nome': 'Alagoas', 'Capital': 'Maceió'}
print(pais)
print(pais['Capital'])
# pais.clear()

# Método get()
print(pais.get("Nome", "Não existe"))
print(pais.get("Qualquer", "Não existe"))
