
class Funcionario:

    def  __init__(self, nome, email, telefone):
        self.__nome= nome
        self.__email = email
        self.__telefone = telefone

    def calcula_salario(self, horas_trabalhadas, valor_hora):
        salario = round((float(horas_trabalhadas) * float(valor_hora)), 2)
        return salario



    @property
    def nome (self):
            return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email (self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email= email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone



    def __eq__(self, other):
        if self.nome != other.nome:
            return False
        elif self.email != other.email:
            return False
        elif self.telefone != other.telefone:
            return False
        else:
            return True


    def __str__(self):
        return f'Nome: {self.nome}; email: {self.email}; telefone: {self.telefone}'

# _______________________________________________________
funcionario1 =Funcionario('José', 'jose@jose.com', '14 1234-5678')

print(funcionario1.__str__())



