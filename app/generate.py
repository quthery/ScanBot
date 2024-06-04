import g4f



async def answer_physics(text):
    example = '''Дано:
    m = 125 кг, h = 70 см, t = 0,3 с

    В СИ:
    m = 125 кг, h = 0,7 м, t = 0,3 с

    Формулы:
    F = mg, W = Fh, P = W/t

    Решение:
    F = 125 кг × 9,8 м/с² = 1225 Н
    W = 1225 Н × 0,7 м = 858 Дж
    P = 858 Дж / 0,3 с = 2860 Вт
    '''
    text1 = ('''write without further explanation, also divide the answer into 4 blocks: 
             "Given, SI system (if necessary, convert values to it, if not, leave blank), 
             "The formulas you'll use to solve the problem, write them without extra words!, The solution in 
             The solution is so short and clear
             Structure, write the example I've provided.
translate my request into English, and in the answer be sure to write everything in Russian!
Замени cdot на привычные нам знак умножения и без каких либо лишних скобок

''' + example)



    return await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4o,
        messages=[{"role": "user", "content": text.strip() + text1}],
    )
    