Port Scanner
Este repositório contém um projeto de um scanner de portas desenvolvido como parte de um desafio do FreecodeCamp. O objetivo deste projeto é verificar quais portas estão abertas em um determinado alvo (endereço IP ou URL) e identificar os serviços que estão rodando nessas portas.

Funcionalidades
Varredura de Portas: O scanner verifica um intervalo de portas especificado pelo usuário e retorna uma lista das portas abertas.
Identificação de Serviços: Utiliza um dicionário de portas comuns para identificar os serviços que estão rodando nas portas abertas.
Modo Verbose: Um modo opcional que fornece uma saída descritiva com o endereço IP, nome de host (se disponível) e os serviços associados às portas abertas.
Tratamento de Erros: Identifica e retorna erros para nomes de host e endereços IP inválidos.

Estrutura do Projeto
port_scanner.py: Contém a função principal get_open_ports que realiza a varredura de portas e retorna os resultados.
common_ports.py: Um dicionário de portas comuns e seus serviços associados, utilizado para identificar os serviços.
main.py: Script de exemplo para testar o scanner de portas.
test_module.py: Testes unitários para garantir que a função get_open_ports funcione corretamente.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.
