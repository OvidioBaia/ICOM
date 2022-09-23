import pandas as pd
#from openpyxl.workbook import Workboo
#csv

alternative_music = pd.read_csv("alternative_music_data.csv") 
blues_music = pd.read_csv("blues_music_data.csv")
hiphop_music = pd.read_csv("hiphop_music_data.csv")

print(alternative_music.shape)
print(blues_music.shape)
print(hiphop_music.shape)

print(alternative_music.info())
print(blues_music.info())
print(hiphop_music.info())

alternative_music["nova_coluna"] = 1
blues_music["nova_coluna"] = 2
hiphop_music["nova_coluna"] = 3
# print(alternative_music.info())
# print(blues_music.info())
# print(hiphop_music.head())

new_data_frame = pd.concat([alternative_music, blues_music, hiphop_music], axis=0)
new_data_frame.to_csv("C:/Users/ovidi/OneDrive/Área de Trabalho/IFCE-cedro/ICOM/data_musica.csv", index=False)
print(new_data_frame.info())
print(new_data_frame.shape)

novo = new_data_frame[new_data_frame["track_href"].notna()]
print(novo.info())
print(novo.shape)

data_frame_sem_string = novo.select_dtypes(exclude=['object'])
print(data_frame_sem_string.info())