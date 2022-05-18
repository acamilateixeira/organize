from os import listdir, path, mkdir, rename, system
import shutil
from os.path import isfile, join, expanduser
from datetime import datetime


class Organizar:
    time = datetime.now()

    def __init__(self, local):
        self.local = local

        self.nome = [file for file in listdir(
            self.local) if isfile(join(self.local, file))]
        self.log = ["RELATÓRIO:", " "]
        self.pastaLog = self.local + f'\\log'
        self.data = Organizar.time.strftime('%d-%m-%Y_%H-%M-%S')
        self.novoLog = f'{self.pastaLog}\\{self.data}.txt'

    def organizando(self):
        novasPastas = 0
        arquivosMovidos = 0

        print('Processo Iniciado...')

        if len(self.nome) == 0:
            self.log.append(f"Não há arquivos na pasta {self.local}."
                            f" Não houve nenhuma alteração!")
        else:
            for c in range(len(self.nome)):
                arquivo = self.nome[c].split('.')

                if not path.exists(self.pastaLog):
                    mkdir(self.pastaLog)

                if not path.exists(self.local + f'\\{arquivo[-1]}'):
                    mkdir(self.local + f'\\{arquivo[-1]}')

                    self.log.append(
                        f"'pasta criada para os arquivos: {arquivo[-1]} ")

                    novasPastas += 1
                try:
                    shutil.move(
                        self.local + f'\\{self.nome[c]}', self.local + f'\\{arquivo[-1]}')

                    self.log.append(f'arquivo {self.nome[c]} '
                                    f'foi movido para a pasta {self.local}\\{arquivo[-1]}')

                    arquivosMovidos += 1
                except shutil.Error:
                    verificarPasta = self.local + f'\\{arquivo[-1]}'
                    verificando = [file for file in listdir(
                        verificarPasta) if isfile(join(verificarPasta, file))]

                    if f'{arquivo[0]}-_-(1.{arquivo[-1]}' not in verificando:

                        rename(
                            self.local + f'\\{self.nome[c]}', self.local + f'\\{arquivo[0]}-_-(1.{arquivo[-1]}')
                        shutil.move(
                            self.local + f'\\{arquivo[0]}-_-(1.{arquivo[-1]}', self.local + f'\\{arquivo[-1]}')
                        self.log.append(f'ja existe um arquivo com o nome {self.nome[c]}na pasta {arquivo[-1]}  '
                                        f', ele foi renomeado para {arquivo[0]}(1).{arquivo[-1]}  ')
                        arquivosMovidos += 1
                    else:
                        analisar = f"{self.local}\\{arquivo[-1]}"

                        analisandoPasta = [file for file in listdir(
                            analisar) if isfile(join(analisar, file))]

                        analisandoArquivo = list()

                        for cont in range(len(analisandoPasta)):
                            if arquivo[0] in analisandoPasta[cont]:
                                try:
                                    analisandoArquivo.append(
                                        int(analisandoPasta[cont].rstrip(f'.{arquivo[-1]}').split('-_-(')[-1]))
                                    arquivosMovidos += 1
                                except ValueError:
                                    pass
                        novoNome = f"{arquivo[0]}-_-({max(analisandoArquivo) + 1}.{arquivo[-1]}"

                        rename(
                            self.local + f'\\{self.nome[c]}', self.local + f'\\{novoNome}')
                        try:
                            shutil.move(
                                self.local + f'\\{novoNome}', self.local + f'\\{arquivo[-1]}')
                            self.log.append(f'Existe um arquivo com o nome {self.nome[c]} na pasta {arquivo[-1]}'
                                            f', ele foi renomeado para {novoNome}  ')

                            arquivosMovidos += 1
                        except shutil.Error:
                            novoNome2 = f"{arquivo[0]}-_-({max(analisandoArquivo) + 2}.{arquivo[-1]}"
                            rename(
                                self.local + f'\\{novoNome}', self.local + f'\\{novoNome2}')
                            shutil.move(
                                self.local + f'\\{novoNome2}', self.local + f'\\{arquivo[-1]}')
                            arquivosMovidos += 1

        self.log.append(f'Arquivos movidos:  {arquivosMovidos}  ')
        self.log.append(f'Pastas criadas:  {novasPastas}  ')

        print('Processo finalizado!')

        with open(self.novoLog, 'a') as arquivo:
            if len(self.log) == 0:
                arquivo.write(
                    'Não foi localizado nenhum arquivo fora da pasta de sua extensão')
            else:
                for linha in self.log:
                    arquivo.write(linha + '\n')

    def abrirLog(self):
        system(f'start {path.realpath(self.novoLog)}')
