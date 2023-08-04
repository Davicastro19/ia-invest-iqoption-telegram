## Bot Automático de Investimento em Opções Binárias via Telegram

Este é um bot automatizado de investimento em opções binárias desenvolvido utilizando a biblioteca aiogram para interação com o Telegram, a API da IQ Option para execução de operações de investimento e o Redis para controle de usuários e armazenamento de dados temporários.

### Funcionalidades do Bot:

1. **Controle de Usuários**: O bot permite que os usuários se cadastrem e façam login utilizando o número de telefone ou outro método de autenticação seguro. Os dados dos usuários, como saldo da conta, histórico de operações e configurações personalizadas, são armazenados no Redis para serem recuperados durante o uso do bot.

2. **Estratégia Torres Gêmeas (M15)**: O bot implementa a estratégia "Torres Gêmeas" para realizar operações de investimento em opções binárias. A estratégia é baseada em análise técnica usando gráficos de candlesticks M15, onde ocorre uma negociação de compra (call) ou venda (put) dependendo das condições do mercado.

3. **Investimento Automático**: O bot realiza as operações de investimento automaticamente, com base nas informações da estratégia Torres Gêmeas e no saldo disponível na conta do usuário.

4. **Agendamento de Investimentos**: As operações de investimento são agendadas para ocorrer a cada hora, de acordo com as configurações do usuário.

### Comandos do Bot:

- `/start`: Inicia a interação com o bot e apresenta o menu principal.
- `/login`: Permite que os usuários façam login na plataforma da IQ Option.
- `/config`: Permite ao usuário configurar as preferências do bot, como valor de Stop Win, Stop Loss, PayOut, Paridade, Fator Gale, Gale e Valor do Investimento.
- `/play`: Inicia o bot e começa a realizar operações automáticas de acordo com a configuração definida pelo usuário.
- `/stop`: Pausa o bot e interrompe as operações automáticas em andamento.

### Contato:

- Telegram: [https://t.me/reactdavicastro](https://t.me/reactdavicastro)

### Aviso Legal:

Este bot de investimento em opções binárias foi desenvolvido apenas para fins educacionais e informativos. A negociação em opções binárias envolve riscos significativos e pode levar à perda de capital. Não garantimos lucros e recomendamos que você tenha conhecimento sólido do mercado financeiro antes de usar o bot para investir dinheiro real. Você é responsável por suas próprias decisões de investimento.
