# Berinteraksi dengan Data

Materi ini adalah catatan pembelajaran Python tentang **data dan tipe data**.

Tujuan saya mempelajari materi ini adalah memahami bagaimana Python menyimpan, mengenali, dan mengubah data.

---

## 1. Apa itu Data?

Data adalah informasi yang digunakan oleh program.

Contohnya:

```python
name = "Abdul"
age = 25
height = 174.5
is_student = True
```

Di sini:

* `"Abdul"` adalah data berupa teks.
* `25` adalah data berupa bilangan bulat.
* `174.5` adalah data berupa bilangan desimal.
* `True` adalah data berupa benar/salah.

Komputer perlu mengetahui **jenis data** yang sedang digunakan supaya bisa memperlakukannya dengan benar.

---

# 2. Variable

Variable bisa dibayangkan seperti **kotak yang memiliki nama** untuk menyimpan data.

Contoh:

```python
name = "Abdul"
age = 25
```

Kita mempunyai dua variable:

```text
name → "Abdul"
age  → 25
```

Isi variable dapat digunakan kembali:

```python
print(name)
print(age)
```

Hasil:

```text
Abdul
25
```

---

# 3. Deklarasi dan Inisialisasi

## Deklarasi

Deklarasi berarti membuat variable dan menentukan tipe datanya.

Contoh pada bahasa seperti C/C++:

```cpp
int age;
float salary;
```

Artinya:

```text
age    → integer
salary → float
```

## Inisialisasi

Inisialisasi berarti memberikan nilai kepada variable.

```cpp
int age = 17;
float salary = 5000000;
```

### Bagaimana dengan Python?

Python lebih sederhana.

Kita tidak perlu menentukan tipe data terlebih dahulu.

Langsung saja:

```python
age = 17
salary = 5000000.0
```

Python akan mengetahui tipe datanya.

Kita dapat mengeceknya menggunakan `type()`:

```python
print(type(age))
print(type(salary))
```

Hasil:

```text
<class 'int'>
<class 'float'>
```

---

# 4. Tipe Data

Tipe data adalah **jenis dari sebuah data**.

Contohnya:

```text
25       → integer
3.14     → float
"Abdul"  → string
True     → boolean
```

Secara sederhana, tipe data Python yang dipelajari di materi ini dapat dibagi menjadi:

1. Primitive
2. Collection

---

# 5. Tipe Data Primitif

Tipe data primitif adalah data sederhana yang biasanya menyimpan **satu nilai**.

## 5.1 Integer (`int`)

Integer adalah bilangan bulat.

Contoh:

```python
age = 25
temperature = -5
score = 100
zero = 0
```

Tidak memiliki angka desimal.

```text
25
-5
100
0
```

---

## 5.2 Float (`float`)

Float digunakan untuk angka yang memiliki desimal.

Contoh:

```python
height = 174.5
price = 15000.50
pi = 3.14
```

---

## 5.3 Complex (`complex`)

Complex digunakan untuk bilangan kompleks.

Contoh:

```python
number = 1 + 2j
```

Untuk saat ini saya belum perlu terlalu fokus pada tipe data ini.

---

# 6. Boolean (`bool`)

Boolean hanya mempunyai dua kemungkinan:

```python
True
False
```

Contoh:

```python
is_student = True
is_married = False
```

Boolean biasanya digunakan untuk pertanyaan yang jawabannya hanya **ya atau tidak**.

Contoh:

```python
age = 20

print(age >= 17)
```

Hasil:

```text
True
```

Karena umur 20 memang lebih besar atau sama dengan 17.

---

# 7. String (`str`)

String adalah **teks atau kumpulan karakter**.

String ditulis menggunakan tanda kutip.

```python
name = "Abdul"
city = 'Jakarta'
```

Keduanya sama-sama string.

```python
print(name)
print(city)
```

Contoh string lainnya:

```python
message = "Hello Python"
```

---

# 8. Tipe Data Collection

Kalau tipe data primitif biasanya menyimpan satu nilai, collection dapat digunakan untuk menyimpan **beberapa data sekaligus**.

Ada empat collection yang dipelajari:

```text
List
Tuple
Set
Dictionary
```

---

# 9. List

List digunakan untuk menyimpan beberapa data secara berurutan.

List menggunakan tanda:

```text
[]
```

Contoh:

```python
data = [1, 2.2, "Dicoding"]
```

List dapat berisi berbagai tipe data.

Hal penting yang harus diingat:

> Index list dimulai dari angka 0.

Contoh:

```python
fruits = ["Apple", "Banana", "Orange"]
```

Index-nya:

```text
Apple  → 0
Banana → 1
Orange → 2
```

Jadi:

```python
print(fruits[0])
```

hasilnya:

```text
Apple
```

---

# 10. Tuple

Tuple mirip seperti list, tetapi isi tuple **tidak dapat diubah** setelah dibuat.

Tuple menggunakan:

```text
()
```

Contoh:

```python
data = (1, "Dicoding", 1 + 3j)
```

Perbedaan sederhananya:

```text
List  → bisa diubah
Tuple → tidak bisa diubah
```

---

# 11. Set

Set adalah kumpulan data yang:

* Tidak memiliki urutan tetap.
* Hanya menyimpan nilai yang unik.
* Tidak boleh memiliki data duplikat.

Set menggunakan:

```text
{}
```

Contoh:

```python
numbers = {1, 2, 3, 7, 13}
```

Jika terdapat data yang sama, set hanya menyimpannya satu kali.

Contoh:

```python
numbers = {1, 2, 2, 3, 3}
print(numbers)
```

Hasilnya hanya berisi:

```text
{1, 2, 3}
```

---

# 12. Dictionary

Dictionary menyimpan data dalam bentuk:

```text
key → value
```

Bisa dibayangkan seperti **kamus**.

Misalnya:

```text
name → Abdul
age  → 25
```

Dalam Python:

```python
person = {
    "name": "Abdul",
    "age": 25,
    "isMarried": False
}
```

Di sini:

```text
"name"      → key
"Abdul"     → value

"age"       → key
25          → value

"isMarried" → key
False       → value
```

Contoh mengambil data:

```python
print(person["name"])
```

Hasil:

```text
Abdul
```

Cara mudah mengingat:

> **Dictionary = data yang mempunyai label.**

---

# 13. Perbandingan Collection

| Tipe       | Contoh              | Ciri utama                      |
| ---------- | ------------------- | ------------------------------- |
| List       | `[1, 2, 3]`         | Berurutan dan bisa diubah       |
| Tuple      | `(1, 2, 3)`         | Berurutan dan tidak bisa diubah |
| Set        | `{1, 2, 3}`         | Nilai unik, tidak berurutan     |
| Dictionary | `{"name": "Abdul"}` | Data berupa key dan value       |

---

# 14. Konversi Tipe Data

Kadang kita perlu mengubah satu tipe data menjadi tipe data lain.

Misalnya:

```python
age = "25"
```

Saat ini `age` adalah string.

```python
print(type(age))
```

Hasil:

```text
<class 'str'>
```

Kita bisa mengubahnya menjadi integer:

```python
age = int(age)
```

Sekarang:

```python
print(type(age))
```

Hasil:

```text
<class 'int'>
```

Beberapa fungsi yang penting:

```text
int()   → menjadi integer
float() → menjadi float
str()   → menjadi string
```

Contoh:

```python
number = 10

number_float = float(number)
number_string = str(number)
```

---

# 15. Mengubah Huruf pada String

Python mempunyai banyak fungsi untuk mengolah string.

## Huruf besar

```python
text = "hello python"

print(text.upper())
```

Hasil:

```text
HELLO PYTHON
```

## Huruf kecil

```python
text = "HELLO PYTHON"

print(text.lower())
```

Hasil:

```text
hello python
```

---

# 16. Menghapus Spasi

Beberapa fungsi yang bisa digunakan:

```text
strip()
lstrip()
rstrip()
```

Contoh:

```python
text = "  Hello Python  "

print(text.strip())
```

Hasil:

```text
Hello Python
```

Sederhananya:

```text
strip()  → hapus spasi kiri dan kanan
lstrip() → hapus spasi kiri
rstrip() → hapus spasi kanan
```

---

# 17. Memisahkan dan Menggabungkan String

## `split()`

Digunakan untuk memisahkan string.

```python
text = "Saya belajar Python"

result = text.split()
```

Hasilnya menjadi beberapa bagian:

```text
["Saya", "belajar", "Python"]
```

## `join()`

Digunakan untuk menggabungkan beberapa string.

Contoh:

```python
words = ["Saya", "belajar", "Python"]

result = " ".join(words)
```

Hasil:

```text
Saya belajar Python
```

---

# 18. Mengganti String

Gunakan `replace()`.

```python
text = "Saya belajar Java"

text = text.replace("Java", "Python")

print(text)
```

Hasil:

```text
Saya belajar Python
```

---

# 19. Mengecek String

Python juga bisa digunakan untuk mengecek isi sebuah string.

Contoh:

```python
text = "PYTHON"

print(text.isupper())
```

Hasil:

```text
True
```

Beberapa fungsi yang dipelajari:

```text
isupper()
islower()
isalpha()
isalnum()
isdecimal()
isspace()
istitle()
```

Sederhananya, fungsi-fungsi tersebut digunakan untuk bertanya kepada Python:

> "Apakah teks ini memenuhi kondisi tertentu?"

Hasilnya biasanya berupa:

```text
True
atau
False
```

---

# 20. Formatting String

Python juga mempunyai beberapa fungsi untuk mengatur posisi teks.

Contoh:

```text
zfill()
rjust()
ljust()
center()
```

Misalnya:

```python
number = "25"

print(number.zfill(5))
```

Hasil:

```text
00025
```

---

# 21. String Literal

String literal adalah teks yang ditulis di antara tanda kutip.

Contoh:

```python
name = "Abdul"
city = 'Jakarta'
```

Ada dua pilihan:

```python
"Hello"
'Hello'
```

Keduanya merupakan string.

---

# 22. Escape Character

Bagaimana jika kita ingin menulis tanda kutip di dalam string?

Misalnya:

```text
Dicoding's Cat
```

Kita bisa menggunakan tanda kutip berbeda:

```python
text = "Dicoding's Cat"
```

Atau menggunakan escape character:

```python
text = 'Dicoding\'s Cat'
```

Beberapa escape character yang perlu diingat:

| Escape | Fungsi       |
| ------ | ------------ |
| `\'`   | Single quote |
| `\"`   | Double quote |
| `\t`   | Tab          |
| `\n`   | Baris baru   |
| `\\`   | Backslash    |

Contoh:

```python
print("Hello\nPython")
```

Hasil:

```text
Hello
Python
```

---

# 23. Raw String

Raw string digunakan ketika kita ingin Python membaca teks **apa adanya**, terutama ketika terdapat banyak backslash.

Caranya dengan menambahkan `r` sebelum string.

```python
print(r'Dicoding\tIndonesia')
```

Hasil:

```text
Dicoding\tIndonesia
```

Tanpa `r`, `\t` akan dianggap sebagai karakter tab.

Raw string sering berguna ketika bekerja dengan **regular expression (regex)** dan teks yang menggunakan banyak backslash.

---

# 24. Hal yang Saya Pelajari

Dari materi ini, saya mulai memahami bahwa Python tidak hanya tentang menulis kode, tetapi juga tentang **bagaimana data disimpan dan diperlakukan**.

Hal-hal yang sudah saya pelajari:

* [x] Apa itu data
* [x] Variable
* [x] Deklarasi dan inisialisasi
* [x] `type()`
* [x] Integer
* [x] Float
* [x] Boolean
* [x] String
* [x] List
* [x] Tuple
* [x] Set
* [x] Dictionary
* [x] Konversi tipe data
* [x] Manipulasi string
* [x] `upper()` dan `lower()`
* [x] `strip()`
* [x] `split()` dan `join()`
* [x] `replace()`
* [x] Pengecekan string
* [x] Formatting string
* [x] Escape character
* [x] Raw string

---

# 25. Kesimpulan Sederhana

Kalau disederhanakan:

```text
DATA
│
├── Data sederhana
│   ├── int
│   ├── float
│   ├── bool
│   └── str
│
└── Kumpulan data
    ├── list
    ├── tuple
    ├── set
    └── dictionary
```

Dan Python bisa membantu kita:

```text
Menyimpan data
      ↓
Mengetahui tipe data
      ↓
Mengubah tipe data
      ↓
Mengolah data
      ↓
Menggunakan data dalam program
```

Ini adalah salah satu dasar penting sebelum melanjutkan ke materi Python berikutnya.

---

## Catatan Pribadi

Saya masih dalam tahap belajar Python dari dasar.

Tidak perlu langsung menghafal semua fungsi.

Yang paling penting untuk saat ini adalah **memahami konsep dan sering berlatih**.

Jika lupa, saya bisa kembali ke README ini dan melihat contoh sederhananya.
