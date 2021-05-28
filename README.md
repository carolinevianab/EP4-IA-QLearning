# Q-Learning: Carro autônomo
### Programa feito para a matéria de Inteligência Artificial do 5° Semestre de Ciência da Computação

### Por Caroline Viana e Richard Santino

---

## Descrição
O projeto é a construção de uma simulação para guiar um carro autônomo por um estacionamento até o seu proprietário (nesse problema, Vanessa).

Para isso, foi utilizado o modelo de Q-Learning com exploração para testar os estado válidos. O formato do estacionamento do problema é estático, mas o usuário pode escolher onde quer que Vanessa e seu Carro iniciem.

## Conteúdo e execução

O projeto, possui dois arquivos necessários: main.py e settings.py. É necessário baixar e manter ambos os arquivos na mesma pasta, pois o arquivo principal main necessita do conteúdo presente no arquivo settings.

Para iniciar o programa, deve-se executar o arquivo main.py, tanto por IDE quanto por terminal, mas é importante haver espaço para que as informações possam ser impressas da forma desejada.

A impressão utiliza cores para imprimir a posição de Vanessa, do carro e do caminho ideal. No entanto, essa cores podem não funcionar em alguns sistemas, pois ele imprime [códigos de escape ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code) para conseguir esse resultado.


