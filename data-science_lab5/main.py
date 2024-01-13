from clustering import main_cluster
from object_counter import counter_image


if __name__ == "__main__":
    print('Оберіть завдання лабораторної:\n')
    print('1 - Кластеризація даних\n')
    print('2 - Підрахувати кількість об`єктів на фото\n')
    mode = int(input('Режим:'))

    if mode == 1:
        main_cluster()
    elif mode == 2:
        counter_image('keycaps.jpg')
        counter_image('keycaps-5.jpg')
