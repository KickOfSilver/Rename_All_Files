import os
import re


input_folder = r"D:\Arquivos de Programas\Google\Arquivos\Drives compartilhados\Debauchery Tea Party\04┇Nomenclatura"  # caminho principal
folder_skip = "@"  # pula a pasta se ela entrar na condição do "folder_skip"
lista = ["1080", "720", "480"]  # se você tiver números extras no arquivo

try:
    os.system("cls")
    os.remove("data_log.txt")
except:
    pass


def check_folders_sub_folders_files():

    path = input_folder  # salvar caminho principal
    path_skip = folder_skip  # salvar o skip

    def check_folders(path, path_skip):

        # cria uma lista dos arquivos
        for folders in os.listdir(path):

            path_main = f"{path}/{folders}"  # novo caminho
            check_path = os.path.isfile(path_main)  # verifica se é um arquivo

            if path_skip in folders:  # pula a pasta se ela entrar na condição do "path_skip"
                check_path = True

            if check_path == False:  # False = pasta, True = arquivo

                name_folder_one = folders  # salva o nome da pasta
                check_sub_folders(path_main, name_folder_one)

        manager_move_log(path)

    def check_sub_folders(path_main, name_folder_one):

        # cria uma lista dos arquivos
        for quality in os.listdir(path_main):

            path_road = f"{path_main}/{quality}"  # novo caminho
            check_path = os.path.isfile(path_road)  # verifica se é um arquivo

            if check_path == False:  # False = pasta, True = arquivo

                name_folder_two = quality  # salva o nome da subpasta
                check_separate_name(
                    path_road, name_folder_one, name_folder_two)

    def check_separate_name(path_road, name_folder_one, name_folder_two):

        # verifica o nome da subpasta
        if "[Multi-Dub-Subs]" in name_folder_two or "[LEG-NO-FIX]" in name_folder_two:
            name_quality = name_folder_two.split(
                "[")[2]  # splita ate o segundo colchete

        elif "[DUB]" in name_folder_two or "[LEG]" in name_folder_two:
            name_quality = name_folder_two.split(
                "[")[2]  # splita ate o segundo colchete

        else:
            name_quality = name_folder_two.split(
                "[")[1]  # splita ate o primeiro colchete

        name_quality = re.sub(
            "[][]", "", name_quality)  # remove os colchete "[]"
        name_quality = re.sub(
            " ", "", name_quality)  # remover qualquer espaço vazio

        # cria uma lista com os dados
        check_list = [
            name_folder_one, name_folder_two, name_quality, path_road]

        check_path_files(check_list)

    def check_path_files(check_list):

        # cria uma lista dos arquivos
        for file in os.listdir(check_list[3]):  # "check_list[3] = path_road"

            # checa o tipo de arquivo
            path = f"{check_list[3]}/{file}"  # "check_list[3] = path_road"
            check_file = os.path.isfile(path)  # verifica se é um arquivo

            # salva o nome do arquivo
            if check_file == True:  # False = pasta, True = arquivo

                file_name = file
                manager(check_list, file_name)

    check_folders(path, path_skip)


def manager(check_list, file_name):

    n_split_ext = os.path.splitext(file_name)

    def manager_processed_number(check_list, n_split_ext):

        number_raw = ""  # armazena o valor
        name_sp = n_split_ext[0]  # n_split_ext[0] = nome sem extensão

        # cria uma lista da qualidade
        for quality in lista:

            if (quality in name_sp):  # verifica se o nome do arquivo tem a qualidade
                # remove a qualidade do nome
                name_sp = re.sub(quality, "", name_sp)

        # cria uma lista com o nome do arquivo
        for file_number in name_sp:
            try:
                int(file_number)  # verifique se é numero
                number_raw += file_number

            except:
                pass

        if not number_raw:  # verifica se a string está vazia
            number_raw = "*&-&*"

        elif number_raw in name_sp:  # verifica se o nome do arquivo tem o numero
            number_raw = int(number_raw)  # converter valor para inteiro

            if number_raw < 10:  # se o número for menor que 10 adicione um zero
                number_raw = f"0{number_raw}"

        manager_processed_name(check_list, n_split_ext, number_raw)

    def list_processed_anime(number_raw):

        if "[OVA]" in check_list[1]:
            signature = f"{str(number_raw)} [OVA] [{check_list[2]}] [Debauchery Tea Party]"

        elif "[OAD]" in check_list[1]:
            signature = f"{str(number_raw)} [OAD] [{check_list[2]}] [Debauchery Tea Party]"

        elif "[ONA]" in check_list[1]:
            signature = f"{str(number_raw)} [ONA] [{check_list[2]}] [Debauchery Tea Party]"

        elif "[Extra]" in check_list[1]:
            signature = f"{str(number_raw)} [Extra] [{check_list[2]}] [Debauchery Tea Party]"

        elif "[Especial]" in check_list[1]:
            signature = f"{str(number_raw)} [Especial] [{check_list[2]}] [Debauchery Tea Party]"

        else:
            signature = f"{str(number_raw)} [{check_list[2]}] [Debauchery Tea Party]"

        return signature

    def manager_processed_name(check_list, n_split_ext, number_raw):

        if "° Temporada" in check_list[1]:  # check_list[1] = "subpasta"

            signature = list_processed_anime(number_raw)

        elif "[Filme]" in check_list[1]:  # check_list[1] = "subpasta"

            if "*&-&*" in number_raw:  # verifica se tem "&-&"
                signature = f"[{check_list[2]}] [Debauchery Tea Party]"

            else:
                signature = f"{str(number_raw)} [{check_list[2]}] [Debauchery Tea Party]"

        old_name = (  # n_split_ext[0] + n_split_ext[1] = "nome + extensão"
            n_split_ext[0] + n_split_ext[1])

        new_name = (  # caminho + assinatura + extensão
            check_list[0] + " - " + signature + n_split_ext[1])

        manager_save_result(check_list, old_name, new_name)

    def manager_save_result(check_list, old_name, new_name):

        # dados para save
        data_old_name = f"{old_name}\n"  # antigo nome
        data_new_name = f"{new_name}\n\n"  # novo nome

        # salvando dados
        try:
            data = open("data_log.txt", "a", encoding="utf-8")
            data.write(data_old_name)  # salva o nome antigo
            data.write(data_new_name)  # salva o novo nome
            data.close()  # encerado

        except:
            pass

        replace_name(check_list, old_name, new_name)

    def replace_name(check_list, old_name, new_name):

        if "*&-&*" in new_name:
            return

        # trocando o nome dos arquivos
        re.sub("  ", " ", new_name)  # remover espaços duplicados
        old_name = f"{check_list[3]}/{old_name}"  # pasta main + nome antigo
        new_name = f"{check_list[3]}/{new_name}"  # pasta main + nome novo3

        os.rename(old_name, new_name)  # antigo para novo nome

    manager_processed_number(check_list, n_split_ext)


def manager_move_log(path):

    try:
        data_log = "data_log.txt"  # arquivo de log
        path_move = f"{path}/{data_log}"  # move o log pra pasta main

        try:
            os.rename(data_log, path_move)  # move o log para main pasta
            print("Finishi")

        except:
            os.replace(data_log, path_move)  # move o log para main pasta
            print("Finishi")

    except:
        pass


check_folders_sub_folders_files()
