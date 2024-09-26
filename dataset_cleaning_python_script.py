#mengimpor pandas sebagai pd
import pandas as pd

#membuat variabel dataset yang berisi dataset yang asli
dataset = pd.read_csv('movie_sample_dataset.csv')

#menampilkan 10 baris pertama dataset
dataset.head(10)

#menampilkan informasi tipe data tiap kolom dan jumlah data yang kosong/missing
dataset.info()
dataset.isnull().sum()

#menghapus kolom yang memiliki data missing
dataset = dataset.dropna()

#menampilkan jumlah data yang kosong/missing
dataset.isnull().sum()

#mengubah kata 'color' ke 'Color' yang ada pada kolom 'color'
dataset['color'] = dataset['color'].replace('color','Color')

#mengubah kata 'color ' ke 'Color' yang ada pada kolom 'color'
dataset['color'] = dataset['color'].replace('color ','Color')

#menampilkan baris yang pada kolom 'country' berisi kata 'usa'
dataset[dataset['country'] == 'usa']

#mengubah kata 'usa' ke 'USA' yang ada pada kolom 'country'
dataset['country'] = dataset['country'].replace('usa','USA')

#menampilkan baris yang pada kolom 'duration' terdapat nilai negatif  
dataset[dataset['duration']< 0]


#menampilkan baris yang pada kolom 'imdb_score' terdapat nilai negatif  
dataset[dataset['imdb_score']< 0]

#mengubah variabel dataset untuk hanya menampilkan baris yang pada kolom 'duration' berisi nilai >=0
dataset = dataset[dataset['duration'] >= 0]

#mengubah variabel dataset untuk hanya menampilkan baris yang pada kolom 'imdb_score' berisi nilai >=0
dataset = dataset[dataset['imdb_score'] >= 0]

#mengubah tipedata pada kolom 'gross' ke int
dataset['gross'] = dataset['gross'].astype(int)

#mengubah tipedata pada kolom 'budget' ke int
dataset['budget'] = dataset['budget'].astype(int)

#menampilkan dataset
dataset

#menyimpan dataset ke bentuk csv dengan nama file 'movie_dataset_cleaning.csv'
dataset.to_csv('movie_dataset_cleaned.csv')


