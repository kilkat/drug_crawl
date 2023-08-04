import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments

# 예시로 BERT를 사용합니다. 다른 모델로 변경할 수도 있습니다.
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 훈련 데이터와 레이블을 준비합니다.
train_texts = [
    "This is a safe sentence.",
    "Avoid harmful words.",
    "Let's promote positivity.",
    "Stop spreading hate."
]

train_labels = [1, 1, 1, 0]  # 1: 안전, 0: 유해

# 인코딩 및 데이터셋 만들기
train_encodings = tokenizer(train_texts, truncation=True, padding=True)
train_dataset = torch.utils.data.TensorDataset(
    torch.tensor(train_encodings['input_ids']),
    torch.tensor(train_encodings['attention_mask']),
    torch.tensor(train_labels)
)

# 훈련 인자 설정
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir='./logs',
    logging_steps=100,
    evaluation_strategy="epoch",
)

# 트레이너 생성 및 훈련 시작
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

trainer.train()

# 훈련이 완료된 모델을 저장합니다.
model.save_pretrained('./trained_model')