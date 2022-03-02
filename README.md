# alura-python-oo
Alura - Curso de Python 3: Introdução a Orientação a objetos
# Python 3

## Procedural vs Orientação a Objetos
> Orientação a Objetos:
> Organização do código

- Aula 1: Dados e comportamento
- Dicionário 
- Funções 
- Encapsulamento de código

## Classe e Objeto
> .Classe
> .Objeto
> .Referência

1 - Uma classe é uma especificação de um tipo, definindo valores e comportamentos.

2- Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos.

3- Uma boa analogia é considerar a classe como a receita para a criação de algum prato; por exemplo, um delicioso bolo de cenoura ;-)

4- Classe: Receita do objeto

Declaração a classe
```python
#arquivo classe.py
class Conta:
    ...código...
    pass 
````

Criando um objeto a partir da clase
```python
Conta()
>>> <conta.Conta instance at 0x10fe26f00>
```

Criando o objeto, guardando o retorno dentro da referência **conta**
```python
>>> conta = Conta()
# 
>>> conta
<conta.Conta object at  0x10715fe10>
```
### Construtor
Função de construtor:
> O Python constrói o objeto, cria um lugar na memória e depois chama a função __init__
```python
    def __init__(self):
```
**Self:** 
- O Python cria automaticamente self
- self é a referência que sabe encontrar o objeto construído em memória.

Com o endereço, utilizaremos self para acessar o objeto e definir seus atributos e características. 
```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

# Passando os parâmetros    
>>> from conta import Conta
>>> conta = Conta(123, "Nico", 55.5, 1000.0)
```

### Atributos
Acessando atributos dos objetos
```python
conta = Conta()
conta.atributo1
```

### Método
Criando métodos
```python
class Conta:
...
def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))
```
Utilizando métodos
```python
conta = Conta()
conta.extrato()
>> Saldo 55.5 do titular Nico

```

### None e coletor de lixo
Gargabe colletor
> "Quando criamos um programa, são gerados diversos objetos que em algum momento serão abandonados. Dentro da máquina virtual, na execução do Python, existe um processo que procura esses objetos esquecidos. Os itens inutilizados serão apagados e o espaço livre em memória será reutilizado. No caso, o responsável por jogar fora esses objetos em desuso é o coletor de lixo (garbage collector, em inglês) do Python"

None
> "Com o uso do None, indicamos que a variável já não aponta para um objeto. A palavra None é equivalente a palavra-chave null nas linguagens C# ou Java"

### Atributos privados

Em algumas linguagens como Java, a palavra private define o atributo como **privado** e é chamado como modificador de visibilidade. Porém, em Python, foi convencionado o uso de **__(undescore)**. Com isso, nós renomeamos os atributos seguindo uma nomenclatura especial, por exemplo, numero passou a se chamar __numero.
Assim informamos para quem lê o código que esse atributo é privado. 
obs: Porém o Python não impede que o atributo seja acesso diretamente. É apenas uma convensão.
````python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite
````

### Um pouco de SOLID
- Pensar na coesão das responsabilidades dos métodos e atributos dentro de uma classe.
- S - Single responsibility principle
- O - Open/closed principle
- L - Liskov substitution principle
- I - Interface segregation principle
- D - Dependency inversion principle

### Getters e Setters
Criar getters e setters para acessar e alterar o valor de atributos privados
- Get
```python
# get
def get_saldo(self):
    return self.__saldo
```

- Set
```python
# set
def set_limite(self, limite): 
    self.__limite = limite
```

### Property
Para manter as funções mais concisa e legível, usamos as propriedades nos métodos get e set. Assim evitando colocaro prefixo 'get' e 'set'
no nome dos métodos. 
> Propriedades são elementos acessados externamente como se fossem atributos, mas que internamente (à classe), são manipulados por funções.

No get:
```python
@property
def saldo(self):
    return self.__saldo
```

No set:
```python
@limite.setter
def limite(self, limite):
    self.__limite = limite
```



