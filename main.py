from DataLoader import Dataset
from PreProcessor import preProcessor
from ModelTraining import GruModel
from Evaluation import evaluation

if __name__ == "__main__":
    dataset = Dataset()
    size = dataset.read_data()

    trainable_dataset = preProcessor(dataset)

    model = GruModel(trainable_dataset)
    history = model.fit()
    model.evaluate()
    model.save_model()

    trainable_dataset = preProcessor(dataset, model)

    evaluation(history)
