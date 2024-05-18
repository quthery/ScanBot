import g4f
from scan_img import scan

def answering(text):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[
            {'role': 'user', 'content': text}
        ]

    )
    return response
txt = scan('ss.png', languages="eng+rus", write_txt=False)
text = "Decompose the answer into 4 columns Given:,SI(if you need to translate values into SI system),Formulas(Write in original characters i.e. meters in m etc.),Solution.Be sure to write the answer in Russian'."
print(answering(f'{txt}.{text}'))