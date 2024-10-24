from datasets import Dataset, Features, Value, load_from_disk
from transformers import RagRetriever, RagTokenizer

def create_knowledge_dataset(sentences):
    data = {'text': sentences}
    features = Features({'text': Value('string')})
    dataset = Dataset.from_dict(data, features=features)
    dataset.save_to_disk('data/knowledge_dataset')
    return dataset

def index_knowledge_base(model_name):
    tokenizer = RagTokenizer.from_pretrained(model_name)
    dataset = load_from_disk('data/knowledge_dataset')

    retriever = RagRetriever.from_pretrained(
        model_name,
        index_name="exact",
        passages=dataset
    )

    retriever.save_pretrained('models/retriever')