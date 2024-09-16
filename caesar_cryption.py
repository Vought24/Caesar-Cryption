import pyperclip as pc
from tkinter import *
from tkinter import ttk
import string


root = Tk()
root.title('Шифр Цезаря')
root.geometry('600x600')
root.iconbitmap(default="icon.ico")
root.resizable(False, False)

label = Label(text='Зашифровать сообщение!', font=('Arial', 13))
label.place(x=200, y=20)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def cryption():
    result = ''
    selected_lang = language.get()
    step = int(step_entry.get())
    user_text = user_text_entry.get().upper()

    if selected_lang == 'Русский':
        current_alphabet = alphabet_RU
    else:
        current_alphabet = alphabet
    
    for char in user_text:
        if char in current_alphabet:
            index = current_alphabet.find(char)
            new_index = (index + step) % len(current_alphabet)
            result += current_alphabet[new_index]
        else:
            result += char
    
    result_label.config(text=f'Результат: {result.upper()}')
    copy_btn.place(x=50, y=450)



#ФУНКЦИЯ КОПИРУЕТ РЕЗУЛЬТАТ ШИФРА ВМЕСТЕ СО СЛОВОМ "РЕЗУЛЬТАТ"\\\\
#  TO FIX!!!!
#05.09.2024 21:3 -- FIXED
def copy():
    result_text = result_label.cget("text")
    #Поставил индекс с 11 символа чтобы не копировалось в буфер слово "Результат"
    pc.copy(result_text[10:])

def copy_dec(result_label_dec):
    result_text_dec = result_label_dec.cget("text")
    pc.copy(result_text_dec[10:])

#Ввод только букв в поле ввода "Введите текст сообщения"
def paste_text(entry_widget):
    entry_widget.delete(0, END)  # Очистить текущее содержимое
    entry_widget.insert(0, pc.paste())

def validate_char_lang(sentence):
    allowed_chars = string.ascii_letters + string.punctuation + ' '    #знаки препинания и пробел
    if all(char in allowed_chars for char in sentence):
        return True
    return False

check_char = (root.register(validate_char_lang,))
# не работает ввод русской раскладки

#сделать минуc в поле ввода шаг шифра 

# Ввод только чисел и цифр в поле "Введите шаг шифра" энак минус
def input_step_validate(number):
    if number == '' or number == '-' or number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
        return True
    return False

check_number = (root.register(input_step_validate), '%P')



eng = 'Английский'
rus = 'Русский'
language = StringVar(value=eng)

select_lang_label = ttk.Label(text='Выберите язык', font=('Arial', 13))
select_lang_label.place(x=30, y=60)

eng_btn = ttk.Radiobutton(text=eng, value=eng, variable=language, cursor='hand2')
eng_btn.place(x=50, y=100)

rus_btn = ttk.Radiobutton(text=rus, value=rus, variable=language, cursor='hand2')
rus_btn.place(x=50, y=130)


# Ввод шага шифра
step_label = ttk.Label(text='Введите шаг шифра', font=('Arial, 13')) 
step_label.place(x=30, y=170)



clue_label = ttk.Label(text='* Введите число', font=('Arial', ))
clue_label.place(x=120, y=200)


step_entry = ttk.Entry(width=7, font=('Arial', 11), justify=CENTER, 
                       validate='key', validatecommand=check_number)
step_entry.place(x=50, y=200)

# Ввод текста для шифрования
user_text_label = ttk.Label(text='Введите текст', font=('Arial', 13))
user_text_label.place(x=30, y=250)
user_text_entry = ttk.Entry(width=50, font=('Arial', 11), validate='key', 
                            validatecommand=(check_char, '%P'))
user_text_entry.place(x=50, y=300)



copy_btn = ttk.Button(text='Скопировать текст', command=copy) 
#.place()  выведен в функцию def decryption() чтобы кнопка появлялась только после результата


# Кнопка шифровать

photo = PhotoImage(file="but.png")
shifr_btn = ttk.Button(text='Зашифровать!', command=cryption, underline=0, image=photo, cursor='hand2')
shifr_btn.place(x=200, y=330)


# резкльатаы
result_label = Label(text='', font=('Arial', 13))
result_label.place(x=30, y=420)

def decryption_in_new_window(step_entry_dec, user_text_entry_dec, language_dec, result_label_dec):
    result = ''
    selected_lang = language_dec.get()
    
    step_value = step_entry_dec.get()
    if step_value.isdigit():
        step = int(step_value)
    else:
        step = 0  # Если шаг не указан
    
    user_text = user_text_entry_dec.get().upper()

    if selected_lang == 'Русский':
        current_alphabet = alphabet_RU
    else:
        current_alphabet = alphabet
    
    for char in user_text:
        if char in current_alphabet:
            index = current_alphabet.find(char)
            new_index = (index - step) % len(current_alphabet)
            result += current_alphabet[new_index]
        else:
            result += char
    
    result_label_dec.config(text=f'Результат: {result.upper()}')

def new_window():
    window = Toplevel(root)
    window.title('Расшифровка сообщений')
    window.geometry('600x600')
    window.resizable(False, False)
    
    eng_dec = 'Английский'
    rus_dec = 'Русский'
    language_dec = StringVar(value=eng_dec)
    
    select_lang_label_dec = ttk.Label(window, text='Выберите язык', font=('Arial', 13))
    select_lang_label_dec.place(x=30, y=60)
    
    eng_dec_btn = ttk.Radiobutton(window, text=eng_dec, value=eng_dec, variable=language_dec, cursor='hand2')
    eng_dec_btn.place(x=50, y=100)
    
    rus_dec_btn = ttk.Radiobutton(window, text=rus_dec, value=rus_dec, variable=language_dec, cursor='hand2')
    rus_dec_btn.place(x=50, y=130)

    step_label_dec = ttk.Label(window, text='Введите шаг шифра', font=('Arial', 13)) 
    step_label_dec.place(x=30, y=170)
    
    clue_label_dec = ttk.Label(window, text='* Введите число', font=('Arial', ))
    clue_label_dec.place(x=120, y=200)
    
    step_entry_dec = ttk.Entry(window, width=7, font=('Arial', 11), justify=CENTER, 
                               validate='key', validatecommand=check_number)
    step_entry_dec.place(x=50, y=200)

    user_text_label_dec = ttk.Label(window, text='Введите зашифрованное сообщение', font=('Arial', 13))
    user_text_label_dec.place(x=30, y=250)

    user_text_entry_dec = ttk.Entry(window, width=50, font=('Arial', 11), validate='key', 
                                    validatecommand=check_char)
    user_text_entry_dec.place(x=50, y=300)

    result_label_dec = Label(window, text='', font=('Arial', 13))
    result_label_dec.place(x=30, y=420)

    # Кнопка для расшифровки
    decrypt_btn_dec = ttk.Button(window, 
                                 text='Расшифровать!', 
                                 command=lambda: decryption_in_new_window(step_entry_dec,
                                                                          user_text_entry_dec, 
                                                                          language_dec, 
                                                                          result_label_dec),
                                 cursor='hand2')
    decrypt_btn_dec.place(x=200, y=330)
    paste_btn_dec = ttk.Button(window, text='Вставить', 
                                command=lambda: paste_text(user_text_entry_dec))
    paste_btn_dec.place(x=400, y=300)
new_window_btn = ttk.Button(text='Расшифровать сообщение', command=new_window)
new_window_btn.place(x=400, y=100)

paste_btn = ttk.Button(text='Вставить', command=lambda: paste_text(user_text_entry))
paste_btn.place(x=400, y=300)

root.mainloop()
