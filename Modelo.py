from transformers import pipeline

# Baixa um modelo especializado em sumarização
resumidor = pipeline("summarization", model="facebook/bart-large-cnn")

def gerar_resumo(texto):
    resumo = resumidor(texto, max_length=200, min_length=50, do_sample=False)
    return resumo[0]['summary_text']

# Testando
if __name__ == "__main__":
    texto_exemplo = "A inteligência artificial está transformando diversas áreas..."
    print(gerar_resumo(texto_exemplo))
