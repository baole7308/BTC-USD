from BTC import dataBTC
from Train import model
def main():
    with open('E:\Python\Bitcoin\BTC.csv', mode="w", newline="", encoding="utf-8") as file:
        pass
    data = dataBTC()
    data.created_data()
    data.save_data_to_csv()
    data.exit()
    df = model('E:\Python\Bitcoin\BTC.csv')
    df.preprocess()
    df.build_model()
    df.train_model(1000,32)
    print('Predict:', df.predict_and_format())
    df.plot_loss()
if __name__ == "__main__":
    main()
    