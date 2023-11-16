"""
Proposta: Exemplo random, a ser apresentado em aula.
Autor:    Gisele Nunes
Data:     15 de novembro de 2023
"""
# importing a library is nothing more than importing code packages that someone
# has already created.
# importar uma biblioteca, nada mais é do que a importação de pacotes de código
# que alguém já criou.
# random is a package that allows the generation of random numbers.
# random é um pacote que permite a geração de números aleatórios.
import random

# Control variable.
# The control variable is of type boolean (can only have one of two values
# possible: true or false ).
# Variável de controle.
# A váriavel de controle é do tipo boolean ( pode ter apenas um de dois valores
# possíveis: verdadeiro ou falso ).

advance = True

# List variable.
# Lists are a type of data structure that allows you to store a collection
# of items in a single variable.
# Variável lista.
# As listas são um tipo de estrutura de dados que permite armazenar uma coleção
# de itens em uma única variável.

list_students = []
list_groups = []
group_list = []
options_groups = []
options_themes = []

#### Populating the list_students.
#### Preenchendo a list_students.

# This while repetition structure will be used to fill a list with
# the name of all students.
# Esta estrutura de repetição while será utilizada para preencher uma lista com
# o nome de todos os alunos.

while advance:
    # The student_name variable will be used to store the digitized name.
    # A váriavel student_name será utilizada para armazenar o nome digitato.
    # Input is the function that allows you to request information from the user.
    # Input é a função que permite que você solicite uma informação ao usuário.
    # The strip() function is used to remove white spaces at the beginning and
    # end of what was typed.
    # A função strip() é utilizada para para remover os espaços em branco no
    # início e no final do que foi digitado.
    # The upper() function is used to convert text to uppercase letters.
    # A função upper() é utilizada para converter um texto em letras maiúsculas.

    student_name = (
        input("Digite por gentileza o nome do aluno: ").strip().upper()
    )

    # This conditional if structure checks whether the student_name is already
    # in the student_list, thus avoiding duplication in the registration.
    # Esta estrutura condicional if verifica se o student_name já consta na
    # list_students evitando assim duplicidade no cadastro.

    if student_name in list_students:
        # The print function displays messages on the screen.
        # A função print  exibir mensagens na tela.

        print(f"O aluno {student_name} já consta na lista de alunos.")

    # The else command is executed if the result of the expression reported in
    # the if statement is false.
    # O comando else é executado caso o resultado expressão informada na
    # instrução if seja falso.

    else:
        # The append method adds the student_name to the end of the student_list.
        # O método append adiciona o student_name ao final da list_students.

        list_students.append(student_name)

    # The follows variable will be used to store the entered decision.
    # A váriavel follows será utilizada para armazenar a decisão digitada.
    # The strip() function is used to remove white spaces at the beginning and
    # end of what was typed.
    # A função strip() serve para remover os espaços em branco no início e no
    # final do que foi digitado.
    # The split() method breaks the entered string and in the case below it only
    # obtains the first letter as position 0 was entered.
    # The upper() function is used to convert text to uppercase letters.
    # A função upper() serve para converter um texto em letras maiúsculas.
    # O método split() quebra a string digitada e no caso abaixo obtem apenas a
    # primeira letra pois foi informado a posição [0].

    follows = (
        input(
            "Deseja incluir mais um nome de aluno a lista de alunos ? [s/n] "
        )
        .strip()
        .upper()
        .split()[0]
    )

    # This if conditional structure checks whether the follows variable is the
    # letter s.
    # Esta estrutura condicional if verifica se a variável follows é a letra s.

    if "N" in follows:
        # The advance variable becomes false.
        # A variável advance passa a ser falsa.

        advance = False

# After the completion of the while repetition structure, the advance variable
# returns to the True value.
# Após a finalização da estrutura de repetição while a variável advance volta a
# receber o valor True.

advance = True

#### Populating options_groups.
#### Preenchendo a options_groups.

# The size_list_students variable will be used to store the number of names
# saved in the list_students.
# A váriavel size_list_students será utilizada para armazenar a quantidade de
# nomes salvos na list_students.
# The len() function used to obtain the number of items in a given object.
# A função len() utilizada para obter o número de itens em um determinado objeto.

size_list_students = len(list_students)

# Esta estrutura de repetição while será utilizada para preencher uma lista com
# os a quantidade de grupos possiveis.

while advance:
    # This conditional if structure checks whether the remainder of dividing
    # value i in the interaction is equal to 0.
    # Esta estrutura condicional if verifica se o resto da divisão do valor i
    # na interação é igual a 0.

    # O método append adiciona a quantidade de grupos possiveis ao final da
    # options_groups.

    if (size_list_students % 2) == 0:
        options_groups.append(str(2))

    if (size_list_students % 3) == 0:
        options_groups.append(str(3))

    if (size_list_students % 4) == 0:
        options_groups.append(str(4))

    if (size_list_students % 5) == 0:
        options_groups.append(str(5))

    if len(options_groups) == 0:
        list_students.append("ausente")
        size_list_students = size_list_students + 1
    else:
        advance = False

# After the completion of the while repetition structure, the advance variable
# returns to the True value.
# Após a finalização da estrutura de repetição while a variável advance volta a
# receber o valor True.

advance = True

#### Populating project_theme.
#### Preenchendo a project_theme.

# The size_list_groups variable will be used to store the number of names saved
# in the options_groups.
# A váriavel size_list_groups será utilizada para armazenar a quantidade de
# nomes salvos na options_groups.
# The len() function used to obtain the number of items in a given object.
# A função len() utilizada para obter o número de itens em um determinado objeto.

size_list_groups = len(options_groups)

# The print function displays messages on the screen.
# A função print  exibir mensagens na tela.

print(f"Para este grupo é necessário o minimo de {size_list_groups} temas.")

# This while repetition structure will be used to fill a list with the themes
# to be developed.
# Esta estrutura de repetição while será utilizada para preencher uma lista com
# os tema a ser desenvolvidos.

while advance:
    # The project_theme variable will be used to store the digitized theme.
    # A váriavel project_theme será utilizada para armazenar o tema digitato.
    # Input is the function that allows you to request information from the user.
    # Input é a função que permite que você solicite uma informação ao usuário.
    # The strip() function is used to remove white spaces at the beginning and
    # end of what was typed.
    # A função strip() é utilizada para para remover os espaços em branco no
    # início e no final do que foi digitado.
    # The upper() function is used to convert text to uppercase letters.
    # A função upper() é utilizada para converter um texto em letras maiúsculas.

    project_theme = (
        input(f"Digite por gentileza um tema a ser desenvolvido: ")
        .strip()
        .upper()
    )

    # This conditional if structure checks whether the project_theme is already
    # in the options_themes, thus avoiding duplication in the registration.
    # Esta estrutura condicional if verifica se o project_theme já consta na
    # options_themes evitando assim duplicidade no cadastro.

    if project_theme in options_themes:
        # The print function displays messages on the screen.
        # A função print  exibir mensagens na tela.
        print(
            f"O tema {project_theme} ja consta na lista de temas para projeto."
        )

    # The else command is executed if the result of the expression reported in
    # the if statement is false.
    # O comando else é executado caso o resultado expressão informada na
    # instrução if seja falso.

    else:
        # The append method adds the project_theme to the end of the
        # options_themes.
        # O método append adiciona o project_theme ao final da options_themes.

        options_themes.append(project_theme)

    # This conditional if structure checks whether the number of items in the
    # options_themes list is greater than the value of the size_list_groups
    # variable.
    # Esta estrutura condicional if verifica se a quantidade itens da lista
    # options_themes é maior que o valor da variável size_list_groups.

    if len(options_themes) >= size_list_groups:
        # The follows variable will be used to store the entered decision.
        # A váriavel follows será utilizada para armazenar a decisão digitada.
        # The strip() function is used to remove white spaces at the beginning and
        # end of what was typed.
        # A função strip() serve para remover os espaços em branco no início e no
        # final do que foi digitado.
        # The split() method breaks the entered string and in the case below it only
        # obtains the first letter as position 0 was entered.
        # The upper() function is used to convert text to uppercase letters.
        # A função upper() serve para converter um texto em letras maiúsculas.
        # O método split() quebra a string digitada e no caso abaixo obtem apenas a
        # primeira letra pois foi informado a posição [0].

        follows = (
            input("""Deseja incluir mais um tema a lista de temas ? [s/n] """)
            .strip()
            .upper()
            .split()[0]
        )

        # This if conditional structure checks whether the follows variable is
        # the letter s.
        # Esta estrutura condicional if verifica se a variável follows é a
        # letra s.

        if "N" in follows:
            # The advance variable becomes false.
            # A variável advance passa a ser falsa.

            advance = False

# After the completion of the while repetition structure, the advance variable
# returns to the True value.
# Após a finalização da estrutura de repetição while a variável advance volta a
# receber o valor True.

advance = True

#### Populating the group_list.
#### Preenchendo a group_list.

# The group_students list stores the names of participating students and the topic.
# A lista group_students armazena os nomes dos alunos que participam e o tema.

group_students = []

# The selected_students list stores the names of students who already
# participate in a group.
# A lista selected_students armazena os nomes dos alunos que já
# participam de algum grupo.

selected_students = []

# The theme_unavailable list stores tems that are already assigned to a group.
# A lista theme_unavailable armazena os tems que já estão designados a um grupo.

theme_unavailable = []

# This while repetition structure will be used to validate the reported
# quantity_groups.
# Esta estrutura de repetição while será utilizada para validar a
# quantity_groups informada.

while True:
    # This for loop is used to traverse the options_themes list.
    # Este laço for é utilizado para percorrer a lista options_themes.

    for i in options_groups:
        print("Você pode formar ", end="")
        print(f"{i}", end=" ")
        print("grupos de alunos.")

    # The number of groups variable will be used to store the number of groups to
    # be formed.
    # A váriavel quantity_groups será utilizada para armazenar a quantidade de
    # grupos a ser formado.
    # Input is the function that allows you to request information from the user.
    # Input é a função que permite que você solicite uma informação ao usuário.

    quantity_groups = input(
        "Digite por gentileza quantos grupos deseja formar: "
    )

    # This conditional if structure checks whether quantity_groups is part of
    # options_groups.
    # Esta estrutura condicional if verifica se quantity_groups faz parte de
    # options_groups.

    if quantity_groups in options_groups:
        # The int() function is used to convert a typed text into an integer value.
        # A função int() é utilizada para converter um texto digitado em um valor
        # inteiro.

        quantity_groups = int(quantity_groups)

        break

# The number_students_group variable will be used to store the number of
# students in each group.
# A váriavel number_students_group será utilizada para armazenar a quantidade de
# estudantes integram cada grupo.

number_students_group = int(size_list_students / quantity_groups)

# This while repetition structure will be used to fill the list_groups with
# group_students.
# Esta estrutura de repetição while será utilizada para preencher o list_groups
# com os group_students.

while len(list_groups) < quantity_groups:
    # This while repetition structure will be used to fill the group_students.
    # Esta estrutura de repetição while será utilizada para preencher o
    # group_students.

    while len(group_students) < number_students_group:
        # The student_name variable will be used to store the
        # student's name in the group to be formed.
        # A váriavel student_name será utilizada para armazenar nome
        # do aluno a ser inserido no grupo a ser formado.
        # random.choice() selects a random element from a list.
        # random.choice() seleciona um elemento aleatório de uma lista.

        selected_name = random.choice(list_students)

        # This conditional if structure checks whether the indicated
        # student_name is included in selected_studenwhilets.
        # Esta estrutura condicional if verifica se o student_name
        # indicada consta na selected_students.

        if selected_name not in selected_students:
            # The append method adds the selected name value to the end of the
            # group_students list.
            # O método append adiciona o o valor selected_name ao final
            # da lista group_students.
            # The append method adds the selected name value to the end of the
            # selected_students list.
            # O método append adiciona o o valor selected_name ao final
            # da lista selected_students.

            group_students.append(selected_name)
            selected_students.append(selected_name)

    # This while repetition structure will be used to fill the theme in
    # group_students.
    # Esta estrutura de repetição while será utilizada para preencher o
    # tema no group_students.

    while True:
        # The defined_theme variable will be used to store the theme to be
        # inserted into the group to be formed.
        # A váriavel defined_theme será utilizada para armazenar tema a ser
        # inserido no grupo a ser formado.
        # random.choice() selects a random element from a list.
        # random.choice() seleciona um elemento aleatório de uma lista.

        selected_theme = random.choice(options_themes)

        # This conditional if structure checks whether the indicated
        # defined_theme is included in theme_unavailable.
        # Esta estrutura condicional if verifica se o defined_theme indicada
        # consta na theme_unavailable.

        if selected_theme not in theme_unavailable:
            # The append method adds the selected_theme value to the end of the
            # group_students list.
            # O método append adiciona o o valor selected_theme ao final
            # da lista group_students.
            # The append method adds the selected_theme name value to the end of the
            # selected_students list.
            # O método append adiciona o o valor selected_theme ao final
            # da lista selected_students.

            group_students.append(selected_theme)
            theme_unavailable.append(selected_theme)

            break

    # The append method adds group_students to the end of list_groups.
    # O método append adiciona group_students ao final da list_groups.

    list_groups.append(group_students[:])

    print(f"group_students: {group_students}")

    # The clear() method clears the group_students list.
    # O método clear() limpa a lista group_students.

    group_students.clear()
