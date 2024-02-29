from BTC import dataBTC
from Train import model
def main():
    data = dataBTC()
    data.created_data()
    data.save_data_to_csv()
    data.exit()
    df = model('BTC.csv')
    df.preprocess()
    df.build_model()
    df.train_model(10000,256)
    print('Predict:', df.predict_and_format())
    df.plot_loss()
if __name__ == "__main__":
    main()