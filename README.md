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