import face_recognition
import sqlite3
def db_set():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('''INSERT INTO persons_data(path, Full_Name, q_user, t_user, phone_number, season, stay) VALUES (
    "image_known/abdulaziz_2.jpg", "Firdavs Yusupov", "yusupov_f", "@Firdavs_Yusupov", "+998977224286", "3", 
    "0/16")''')
    con.commit()
    con.close()


def select():
    mas = []
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    s_els = cursor.execute("INSERT INTO 'persons_data'('user_id') VALUES ('5161784802')")
    for s_el in s_els:
        mas.append(s_el)
        print(s_el)
    con.commit()
    con.close()


image_1 = face_recognition.load_image_file("persons.jpeg")
image_2 = face_recognition.load_image_file("image_unknown/abdulaziz_2.jpg")
image_1_en = face_recognition.face_encodings(image_1)[0]
image_2_en = face_recognition.face_encodings(image_2)[0]
res = face_recognition.compare_faces([image_1_en], image_2_en)

print(res)
if res == [True]:
    print("This is Abdulaziz")


select()
