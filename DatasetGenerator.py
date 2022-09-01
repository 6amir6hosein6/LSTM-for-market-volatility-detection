from DataLoader import TrainableDataset

def generator(normalizer,labels,model = None):

    features = normalizer.bucket_books.reshape(normalizer.bucket_books.shape[0], -1)

    trainable_dataset = TrainableDataset(
        features=features,
        label=labels,
        input_width=10,
        label_width=1,
        shift=1,
        train_portion=0.8,
        validation_portion=0.1,
        test_portion=0.1,
    )
    if model:
        trainable_dataset.plot(model=model)

    return trainable_dataset

