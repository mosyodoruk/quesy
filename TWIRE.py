import sys

DESIGN = """
  _________          _______ _____  ______
 |__   __\ \        / /_   _|  __ \|  ____|
    | |   \ \  /\  / /  | | | |__) | |__
    | |    \ \/  \/ /   | | |  _  /|  __|
    | |     \  /\  /   _| |_| | \ \| |____
    |_|      \/  \/   |_____|_|  \_\______|
"""

data_stack = []

# input type 0 = normal
# input type 1 = data
def get_input(text, input_type=0):
    if input_type == 0:
        res = input(text)
        data_stack.append(res)
        return res
    else:
        res = input(text)
        if res == 'q':
            print("[!] Bilgi alma islemi durduruldu. Kelime uretmeye geciliyor.")
            return res, False
        else:
            data_stack.append(res)
            return res, True

def get_data():
    data_count = 1
    continue_input = True
    while continue_input:
        response, restart = get_input(f"> {data_count}. Bilgi: ", 1)
        data_count += 1
        continue_input = restart

def generate_keys(low_memory):
    fp = open(f"{data_stack[0]}.txt", "w+")

    generated_keys = []
    for i in range(0, len(data_stack)):
        for j in range(0, len(data_stack)):
            if data_stack[i] != data_stack[j]:
                if low_memory:
                    fp.write(f"\n{data_stack[i]+data_stack[j]}")
                else:
                    generated_keys.append(data_stack[i] + data_stack[j])

    fp.write("\n".join(generated_keys))

    fp.close()

print(DESIGN)
if "--low-memory" in sys.argv:
    print("[!] Dusuk RAM modunda baslatildi. Daha az RAM kullanimi saglanacak.")
print("[!] Bilgi alinan yerlerde 'q' yazarsaniz daha fazla bilgi giremezsiniz!")
victim = get_input("Kurbanin adi: ")
get_data()
generate_keys("--low-memory" in sys.argv)
print(f"[+] Kelime uretme islemi tamamlandi. Uretilen kelimeler {data_stack[0]}.txt isimli dosyaya kaydedildi.")
