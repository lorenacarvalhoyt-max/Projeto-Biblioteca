# Esta lista vazia vai armazenar os  livros da biblioteca 
livros = []

def menu_principal():
    menu = True
    print("Bem-vindo à Biblioteca!")
    while menu == True:
        print("======Menu Principal======")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair\n")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Adicionar Livro")
            adicionar_livro()
        elif escolha == "2":
            print("Listar Livros")
            listar_livros()
        elif escolha == "3":
            print("Emprestar Livro")
            emprestar_livro()
        elif escolha == "4":
            print("Devolver Livro")
            devolver_livro()
        elif escolha == "5":
            print("Saindo...")
            menu = False
        else:
            print("Opção inválida. Tente novamente.")



#Lógica para adicionar, listar, emprestar e devolver livros será implementada posteriormente.
def adicionar_livro():
    #pede para o usuário colocar o nome do livro
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")

    livros.append({'titulo': titulo, 'autor': autor, 'disponivel': True})
    print(f"Livro '{titulo}' adicionado com sucesso!")  

def listar_livros():
    #exibe todos os livros da biblioteca 
    if not livros: #verifica se a lista está vazia
        print("Nenhum livro disponível na biblioteca.")
        return #sai da função
    print("Livros disponíveis na biblioteca:")
    for i , livro in enumerate(livros):
        print("\n")

        print(f"{i + 1}. {livro['titulo']} por {livro['autor']} ")
def emprestar_livro():
    #empresta um livro,mudando seu status para indisponivel
    listar_livros() #mostra os livros disponíveis
    if not livros:
        return
    try:
        escolha = int(input("Digite o número do livro que deseja emprestar: "))
        if 1 <= escolha <= len(livros):
            livro = livros[escolha - 1]
            if livro['disponivel']:
                livro['disponivel'] = False
                print(f"Você emprestou o livro '{livro['titulo']}' com sucesso!")
            else:
                print(f"O livro '{livro['titulo']}' não está disponível no momento.")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
def devolver_livro():
    #devolver um livro, mudando seu status para disponivel
    listar_livros()
    if not livros:
        return
    
    try:
        escolha = int(input("Digite o número do livro que deseja devolver: "))
        if 1 <= escolha <= len(livros):
            livro = livros[escolha - 1]
            if not livro['disponivel']:
                livro['disponivel'] = True
                print(f"Você devolveu o livro '{livro['titulo']}' com sucesso!")
            else:
                print(f"O livro '{livro['titulo']}' já está disponível na biblioteca.")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
     

if __name__ == "__main__":
    menu_principal()