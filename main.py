from BTC import dataBTC

data = dataBTC()
def main():
    data.created_data()
    data.save_data_to_csv()
if __name__ == "__main__":
    main()