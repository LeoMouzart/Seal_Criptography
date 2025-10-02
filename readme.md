<h1>🔐 Seal Criptography</h1><br>

<img src="https://img.shields.io/badge/Python-3.8+-blue.svg">
<img src="https://img.shields.io/badge/CustomTkinter-5.2.0-green.svg">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg"


<p>O projeto Seal Cryptograph trata-se de uma atividade prática supervisionada que visa avaliar o aprendizado de um determinado conceito, onde aplica-se um projeto prático embasado por uma pesquisa. Neste projeto o desafio é criar um sistema que criptografa e descriptografa uma mensagem, utilizando a linguagem python.</p>


<h2>✨ Funcionalidades</h2><br>

<ul>
    <li> 🔒 Criptografia Simétrica AES-256 - Proteção robusta de mensagens; </li>
    <li> 🔓 Descriptografia Segura - Recuperação de mensagem criptografada; </li>
    <li> 👥 Sistema de Autenticação - Autenticação de entrada de usuário; </li>
    <li> 🎨 Interface Moderna - UI desenvolvida com CustomTkinter </li>
    <li> 🔑 Gerenciamento de Chaves - Geração automática de chaves de sessão </li>
    <li> ⚡ Processamento Rápido - Operações de criptografia em tempo real </li>
</ul><br>

<h2> 🛠️ Tecnologias Utilizadas </h2><br>

<ul>
    <li> Python 3.8+; </li>
    <li> CustomTkinter - Interface Gráfica; </li>
    <li> PyCryptodome - Criptografia AES - 256; </li>
    <li> Datetime - Registro de data e hora de operações </li>
</ul><br>

<h2> 📦 Estrutura do Projeto </h2><br>

<div>

<p>
Seal_Criptography/<br>
├── graphics.py     -------------           # Ponto de entrada da aplicação<br>
├───── login.py     -------------           # Sistema de autenticação<br>
├───── principal.py -------------           # Interface principal de criptografia<br>
├── criptografia.py -------------           # Módulo de operações criptográficas<br>
├── requirements.txt-------------           # Dependências do projeto<br>
├── README.md       -------------           # Documentação<br>
└──.gitignore       -------------           # Gerenciamento de cache<br>
</p>
</div>


<h2> 🔧 Módulos Principais </h2>

<h3>login.py</h3>

<ul>

<li>Interface de validação de usuário</li>
<li>Autenticação</li>
<li>Redirecionamento para a interface principal</li>

</ul>

<h3>principal.py</h3>

<ul>

<li>Interface principal do sistema de criptografia</li>
<li>Operações de criptografar e descriptografar</li>

</ul>

<h3>criptografia.py</h3>

<ul>

<li>Funções de criptografar e descriptografar</li><br>

<p>def criptografia_simetrica(mensagem: str, chave: bytes) -> str></p>
<p>def descriptografia_simetrica(mensagem_cripto: str, chave: bytes) -> str</p>


</ul>


<h2> 🚀 Instalação e Execução </h2><br>

<h2>Pré-requisitos</h2>

<ul>
    <li>Python 3.8 ou superior</li>
    <li>pip (gerenciador de pacotes Python)</li>
</ul>


<div>

<h2>📝 Como Usar</h2>

<h3>🔐 Primeiro Acesso</h3>

<ol>

<li>EXECUTE login.py</li>
<li>Digite o nome para autenticação</li>

</ol>

<p>______________________________________________________________________________</p>

<h3>💻 Interface Principal</h3>

<ol>

<li>Digite sua mensagem na área de texto de entrada</li>

<li>Clique em "Criptografar" para proteger sua mensagem</li>

<li>Visualize o resultado na área de texto de saída</li>

<li>Use "Descriptografar" para realizar o processo inverso</li>

</ol>

<p>______________________________________________________________________________</p>

<h3>🔒 Criptografia e Segurança</h3>

<ol>

<li><b>Criptografia AES-256</b> - Algoritmo de criptografia simétrica robusto</li>

<li><b>Chaves de Sessão Únicas</b> - Geradas automaticamente para cada execução</li>

<li><b>Validação de Entrada</b> - Tratamento de erros e exceções</li>

</ol>

</div>


<h2>👨‍💻 Desenvolvedores</h2>

<h3>Leonardo Mouzart</h3>
GitHub: <a href"https://github.com/LeoMouzart">@LeoMouzart</a><br>
Projeto: Seal Criptography<br>
<p>_______________________________________________________________</p>
<h3>Julia Salim</h3><br>
<p>_______________________________________________________________</p>
<h3>Enzo Correr</h3>




<h2>🙏 Agradecimentos</h2>

<ul>
<li>CustomTkinter pela incrível biblioteca de UI</li>
<li>PyCryptodome pelas implementações criptográficas</li>
<li>Comunidade Python por recursos e suporte</li>
</ul>

<h3>⭐ Se este projeto foi útil, considere dar uma estrela no repositório!</h3>
