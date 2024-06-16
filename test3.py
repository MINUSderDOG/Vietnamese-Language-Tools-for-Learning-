from tkinter import *

root = Tk()
root.title("越南语转国际音标小工具")

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 500
wh = 300
x = (sw - ww) / 2
y = (sh - wh) / 2 - 50
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

lb2 = Label(root, text="输入越南语转换为国际音标")
lb3 = Label(root, text="Ver1.0(beta)")
lb2.place(relx=0, rely=0.05)
lb3.place(relx=0, rely=0.13)

txt = Text(root, font=("宋体", 20))
txt.place(rely=0.6, relheight=0.4, relwidth=1)

inp1 = Entry(root, font=("", 20))
inp1.place(relx=0, rely=0.2, relwidth=1, relheight=0.25)

def vietnamese_to_ipa(word):
    # 定义越南语字母和对应的IPA符号
    vietnamese_ipa_mapping = {
        'ộ':'o',
        'ya':'iə',
        'ia':'iə',
        'yê':'iə',
        'iê':'iə',
        'ưa':'ɯə',
        'ươ':'ɯə',
        'ua':'uə',
        'uô':'uə',
        'iu':'iw',
        'yu':'iw',
        'êu':'ew',
        'ao':'aw',
        'au':'ɐw',
        'ưu':'ɯw',
        'âu':'ʌw',
        'ai':'aj',
        'ay':'ɐj',
        'ưi':'ɯj',
        'ơi':'ɤj',
        'ây':'ʌj',
        'oi':'ɔj',
        'ôi':'oj',
        'ui':'uj',
        'a': 'ə',
        'ă': 'ɐ',
        'â': 'ʌ',
        'b': 'b',
        'c': 'k',
        'd': 'd',
        'đ': 'ɗ',
        'e': 'ɛ',
        'ê': 'e',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        'o': 'ɤ',
        'ô': 'o',
        'ơ': 'ɔ',
        'p': 'p',
        'q': 'k',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'ư': 'ɯ',
        'v': 'v',
        'x': 's',
        'y': 'i',
        'z': 'z'

        # ...（省略了其他映射）
    }

    # 将越南语单词转换为IPA符号
    ipa = ''
    for char in word:
        if char in vietnamese_ipa_mapping:
            ipa += vietnamese_ipa_mapping[char]
        elif char.isspace():
            ipa += ' '
        else:
            ipa += char

    return ipa

def button1():
    # 获取输入的越南语单词
    word = inp1.get()

    try:
        # 将越南语单词转换为IPA符号
        ipa = vietnamese_to_ipa(word)

        # 显示结果
        txt.delete("1.0", END)
        txt.insert("1.0", ipa)
    except Exception as e:
        # 处理错误
        txt.delete("1.0", END)
        txt.insert("1.0", "错误：%s" % str(e))

# 创建按钮
btn1 = Button(root, text='结果如下', font=("", 12), command=button1)
btn1.place(relx=0.35, rely=0.45, relwidth=0.2, relheight=0.15)

# 启动主循环
root.mainloop()