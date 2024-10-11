import keyboard

pressed_keys = []

def on_key_event(event):
    try:
        print(f"Tecla pressionada: {event.name}")
        pressed_keys.append(event.name)
    except Exception as e:
        print(f"Erro ao processar o evento de tecla: {e}")

try:
    keyboard.on_press(on_key_event)
    print("Aguardando a tecla 'esc' ser pressionada para finalizar...")
    keyboard.wait('esc')
except Exception as e:
    print(f"Erro ao configurar o monitoramento do teclado: {e}")

try:
    with open('keys.txt', 'w') as file:
        for key in pressed_keys:
            file.write(f"{key}\n")
    print("Teclas pressionadas foram salvas em 'keys.txt'.")
except Exception as e:
    print(f"Erro ao escrever no arquivo 'keys.txt': {e}")
