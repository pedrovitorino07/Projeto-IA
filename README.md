# Projeto-IA
Projeto da cadeira de Inteligencia artificial, usando o metodo YOLO, consultando imagem ou video.

# Interface
Interface feita com o Tkinter, com 3 funcionalidades simples:

1- Detectar pela camera: Nessa opção a webcam é ativada, fazendo o reconhecimento da imagem. Com PC's mais fracos trava bastante por conta da utilização de varios recursos simultaneos. Para sair dessa opção, pressione "ESC", e para a imagem congelar em um frame aperte e segura a teclada "ESPAÇO".

2- Detectar pela imagem: Nessa opção é possivel escolher uma imagem do proprio computador, e após isso o computador faz o reconhecimento. 

3- Detectar por video: É selecionado um video do computador do usuario, e ele roda fazendo o reconhecimento, o video é transmitido com baixo FPS, facilitando a observação das categorias de objetos reconhecidos. E para sair desse modo de detecção de video basta apertar "ESC" e para segurar em um único frame, basta apertar "ESPAÇO" e segurar.

# Requisitos para rodar corretamente:

- yolov4.cfg

- yolov4.weights

- coco.names

- python

- opencv

# Utilização do Codigo

1. Baixe o yolov3.cfg, o yolov4.weights, e o coco.names, são encontrados nesse link:

   "https://github.com/AlexeyAB/darknet?tab=readme-ov-file#pre-trained-models"

   Baixe e coloque no diretorio do projeto.

2. Baixe o python, caso não tenha

3. Instale o opencv pelo cmd

   "pip install opencv-python"

4. Após isso, só colocar o código no vs code e para rodar basta ir no terminal e escrever "python main.py", assim, se tudo estiver correto, irá rodar.





