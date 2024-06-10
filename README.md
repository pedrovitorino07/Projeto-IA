# Projeto de Inteligência Artificial - Detecção de Objetos com YOLO

Este projeto utiliza o método YOLO (You Only Look Once) para detectar e classificar objetos em imagens e vídeos. A interface foi desenvolvida com Tkinter, oferecendo três funcionalidades principais.

## Interface

A interface possui três funcionalidades simples:

### 1. Detectar pela Câmera
- **Descrição:** Ativa a webcam para fazer o reconhecimento de objetos em tempo real.
- **Nota:** Em PCs mais fracos, pode haver travamentos devido ao uso intensivo de recursos.
- **Controles:**
  - Pressione `ESC` para sair dessa opção.
  - Pressione e segure a tecla `ESPAÇO` para congelar a imagem em um frame.

### 2. Detectar pela Imagem
- **Descrição:** Permite selecionar uma imagem do computador e realiza o reconhecimento de objetos nela.

### 3. Detectar por Vídeo
- **Descrição:** Permite selecionar um vídeo do computador e realiza o reconhecimento de objetos com baixa taxa de quadros por segundo (FPS) para facilitar a observação.
- **Controles:**
  - Pressione `ESC` para sair desse modo.
  - Pressione e segure a tecla `ESPAÇO` para segurar um frame.

## Requisitos

Para rodar corretamente o projeto, você precisará dos seguintes arquivos e softwares:

- `yolov4.cfg`
- `yolov4.weights`
- `coco.names`
- Python
- OpenCV

## Passos para Utilização do Código

1. **Baixe os Arquivos Necessários**
   - Baixe os arquivos `yolov4.cfg`, `yolov4.weights` e `coco.names` do [repositório darknet](https://github.com/AlexeyAB/darknet?tab=readme-ov-file#pre-trained-models).
   - Coloque os arquivos no diretório do projeto.

2. **Instale o Python**
   - Caso não tenha, [baixe e instale o Python](https://www.python.org/downloads/).

3. **Instale o OpenCV**
   - Abra o CMD (prompt de comando) e execute:
     ```bash
     pip install opencv-python
     ```

4. **Execute o Projeto**
   - Abra o terminal no diretório do projeto e execute:
     ```bash
     python main.py
     ```
   - Se tudo estiver configurado corretamente, a interface será iniciada e estará pronta para uso.




