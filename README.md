# Collocation

Project Data Mining

0. pip install -r requiments.txt
1. Dữ liệu được lấy từ folder data
1. Trong file collocations.py
   Sửa đường dẫn ở đoạn

   # Loading the data

   words = [w.lower() for w in webtext.words(
   ROOT_DIR+'/data/testdata.txt')]

1. Chạy file collocations.py ở terminal:
   py collocations.py
