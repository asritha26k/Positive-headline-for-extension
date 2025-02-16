from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "asritha22bce/bart-positive-tone"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def predict(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
