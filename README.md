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

