dia 24/12
https://notion.so/Python-dia-26-12-168bc5c3824d80a5a79fe35448c7bdda
Hoje aprendemos que; podemos passar o instanciamento de uma classe, nos atributo de uma outra.
E decrementar atributos, sem quebrar a cabeça.
 

dia 23/12
https://www.notion.so/Python-dia-23-12-165bc5c3824d80469283fb1bf18a52d4
Hoje eu terminei o meu projeto de contatos, da rocketSeat, onde; 
* A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
* Deve ser possível adicionar um contato
    * O contato pode ter os dados:
    * Nome
    * Telefone
    * Email
    * Favorito (está opção é para poder marcar um contato como favorito)
* Deve ser possível visualizar a lista de contatos cadastrados
* Deve ser possível editar um contato
* Deve ser possível marcar/desmarcar um contato como favorito
* Deve ser possível ver uma lista de contatos favoritos
* Deve ser possível apagar um contato
Atribuição depois da verificação.

POO, onde tudo na programação é um objeto.
self é o this;
atribuições a parâmetros
Corpo class;
Constructor;
Método;
Instancias(OBJETOS kkk);
Pontos negativos: complexidade.
Pontos positivos: herança, polimorfismo, encapsulamento e abstração.

dia 24/12
https://notion.so/Python-dia-24-12-166bc5c3824d80f8af50cb346167d861
Hoje vimos dnv sobre os 4 pilares da POO
abstração; onde uma classe que advêm dela é obrigatória ter os métodos que nela(class abstract) tem.
encapsulamento; onde os atributos construtores de uma classe( aqueles que são instanciais), podem ser privado <self.__nome>, ou publico <self.nome>.
herança; onde uma classe pode herdar de outra, ou heranças múltiplas, onde uma classe herdar mais de 1 classe por vez; < class Morcego(Mamifero, Ave)>.
polimorfismo; onde as subclasses provém métodos de uma superclasse, só que ambas usam os métodos diferentemente entre sí.
Vimos também sobre decoradores, onde podemos aplicar alterações em uma função, método... Passando a função decoradora em cima do método desejado. Vimos também um módulos padrões do python. Temos decoradores comuns do python que são:
classmethod; onde um método de uma classe não precisa ser instanciada, e não têm direito ao acesso dos atributos instancias(constructor), apenas acesso ao atributo da classe.
staticmethod; onde um método de uma classe não precisa ser instanciado, não tem acesso tanto atributos do construtor, quanto os atributos da classe. Caso haja, uma ocorrência onde, precisamos colocar um atributoC em um método de superclasse, podemos concatenar.
super, podemos deixar em métodos, que herdamos, caso não necessite de ajusta, assim vale também para os atributosC de uma superclasse
