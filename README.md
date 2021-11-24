# Django_To_Do_project

<i>TO DO APP - SERVICE</i>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#imagens">Imagens</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#links_apps">Links Úteis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
 
</p>

## <a id="projeto"> 💻 SOBRE ESTE PROJETO </a>

Este projeto teve como intuito criar um APP de CRUD de LISTAS DE TAREFAS, com a possibilidade de trazer as seguintes funcionalidades:

    *CRUD de Tarefas;
      *Criação de Tarefas;
      *Edição de Tarefas;
      *Exclusão de Tarefas;    
    *Trás também a tela de confirmação da edição;
    *Trás também a tela de exclusão + confirmação;

> 🟩 Status do projeto: FINALIZADO <br>

<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS UTILIZADAS NESTE PROJETO </a>

Front-End:

![HTML 5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

Desenvolvimento da parte do Back End:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

Banco de Dados:

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Desenvolvido no:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows

<b>-Clone o repositório com o camando:</b> `https://github.com/renatamoon/Django_To_Do_project.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'ediaristas',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```

 *Migre o banco de dados com: `python manage.py migrate` <br>
 *Execute o servidor: `python manage.py runserver` <br>
  
------

# <a id="imagens">ALGUMAS IMAGENS DO PROJETINHO</a> 

- Abaixo a tela de cadastro e mostrando todas as tarefas cadastradas.

![image](https://user-images.githubusercontent.com/87100340/139124262-58c0990e-ee68-4b89-9f87-b5901fd8da34.png)

- TELA DE ATUALIZAÇÃO DA TAREFA - com botão de completar - caso esteja completada, ele mostra a tarefa como feita:

![image](https://user-images.githubusercontent.com/87100340/139124570-af0ac2bf-6290-48d2-9218-e07cfc8892b9.png)

- Tarefas feitas e não feitas:

![image](https://user-images.githubusercontent.com/87100340/139124634-34bf74a2-40a2-45d2-b64d-bd1139d5e950.png)

- TELA DE EXCLUSÃO DE TAREFAS:

![image](https://user-images.githubusercontent.com/87100340/139124667-94881373-9cab-48c4-a4ff-573038474f91.png)
  
<hr>

## <a id="links_apps"> 🔴 LINKS ÚTEIS </a> 

*USANDO O ADMINLTE3 - Bootstrap Admin Dashboard Template<br>
<br>
https://adminlte.io/<br>  
<hr>
