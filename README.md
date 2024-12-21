Cinema
Uma aplicação para um Cinema precisa armazenar informações sobre os filmes, as salas de
exibição de filmes e sobre cada sessão (ou seja, a exibição de um filme em determinada sala). Os
dados a serem armazenados sobre cada uma dessas entidades são apresentados a seguir:
Sala = (Código, Nome, capacidade, Tipo de exibição, Acessibilidade)
Filme = (Código, Nome, Ano de lançamento, gênero, Atores)
Sessão = (Código do Filme, Código da Sala, Data, Horário, Preço do Ingresso)

Menu de Opções:
1 Submenu de Salas
2 Submenu de Filmes
3 Submenu de Sessões
4 Relatório
5 Sair

Cada Submenu oferece as opções: Listar todos, Listar um elemento específico do
conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um elemento do
conjunto. Observe que atributos no plural indicam que deverá ser possível incluir vários itens
daquele mesmo atributo. Por exemplo, o atributo Atores indica que um filme pode ter um número
indefinido de atores. Portanto, deve-se utilizar uma estrutura que seja adequada para armazenar
todos eles.

A opção “Relatório”:
• Mostra o código do filme, nome do filme, atores, código da sala, nome da sala e os
demais atributos de todas as sessões exibidas a partir de uma data inicial X até uma data
final Y, onde ambas as datas são fornecidas pelo usuário
