# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

if 1==1: 

    from random import randint

    def ch_konf (name, n_konf): # Определение количества конфет
        print (f"{name}, ведите количество конфет, которое возьмете (1-{n_konf}): ")
        ch = int (input ())
        while ch < 1 or ch > n_konf:
            print (f"{name}, не будьте таким жадным. Введите количество конфет, которое возьмете (1-{n_konf}): ")
            ch = int (input ())
        return ch

    def ch_konf_komp (konf, n_konf): # Сколько конфет возьмет комп
        ch = konf  % ( n_konf + 1 )   
        return ch
        
    def play_game (hum): 
        print ("Введите количество конфет: ")
        konf = int (input ())
        print ("Введите максимальное количество конфет, которое можно взять: ")
        n_konf = int (input ())            

        if hum: # Человек против человека
            print ("Игра человека против человека")
            print ("Введите имя первого человека: ")
            hum_1 = input ()
            print ("Введите имя второго человека: ")
            hum_2 = input ()
            
        else: # Игра против компьютера   
            print ("Игра человека против компьютера")
            print ("Введите имя человека: ")
            hum_1 = input ()
            hum_2 = 'Компьютер'
            
        one = randint (0,2)  # кто первый берет конфеты
    
        if one:
            print(f"Ходит {hum_1}")
        else:
            print(f"Ходит {hum_2}")

        ch1 = 0 
        ch2 = 0
        while konf > 0:
            if one:
                n = ch_konf (hum_1, n_konf)
                ch1 = ch1 + n
                konf = konf - n
                one = False
                print (f"Первый игорк взял {n} конфет. В сумме у него {ch1}. Осталось {konf} конфет.")
            else:
                if hum:
                    n = ch_konf (hum_2, n_konf)
                else:
                    n = ch_konf_komp (konf, n_konf)
                
                ch2 = ch2 + n
                konf = konf - n
                one = True
                if hum:    
                    st1="Второй игрок" 
                else:
                    st1="Компьютер"
                
                print (f"{st1} взял {n} конфет. В сумме у него {ch2}. Осталось {konf} конфет.")    

        if one:
            print (f"Выиграл {hum_2}")
        else:
            print (f"Выиграл {hum_1}")

    print ("Выберите тип игры: 1-человек с человеком, иначе-человек с компьютером: ")
    if (int(input ())==1):
        play_game (True)
    else:
        play_game (False)   