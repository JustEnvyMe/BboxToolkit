import pickle

if __name__ == '__main__':
    file = "/media/alex/AC6A2BDB6A2BA0D6/alex_dataset/DOTA/DOTA-v1.0/split_ms_dota1_0/train/annfiles/patch_annfile.pkl"
    data = pickle.load(open(file, 'rb'))
    print(data)