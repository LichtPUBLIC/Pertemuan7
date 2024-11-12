import tkinter as tk

def hasil_prediksi():
    # Menulis "Teknologi Informasi" ke dalam label hasil prediksi
    result_label.config(text="Prodi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry('500x500')  # Ukuran jendela yang lebih besar agar muat semua elemen

# Label Judul Aplikasi
judul_label = tk.Label(root, text='Aplikasi Prediksi Prodi Pilihan', font=('Arial', 20, 'bold'), fg='#007bff')
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Input Nilai Mata Pelajaran
nilai_entries = []
for i in range(10):
    label_nilai = tk.Label(input_frame, text=f'Nilai {i+1}:', width=15, anchor=tk.W)
    entry_nilai = tk.Entry(input_frame, width=5)
    
    label_nilai.grid(row=i, column=0, pady=5)
    entry_nilai.grid(row=i, column=1, pady=5)
    
    nilai_entries.append(entry_nilai)

# Button untuk mendapatkan hasil prediksi
button_hasil_prediksi = tk.Button(root, text='Hasil Prediksi', command=hasil_prediksi, font=('Arial', 12), bg='#28a745', fg='white')
button_hasil_prediksi.pack(pady=20)

# Label untuk menampilkan hasil prediksi
result_label = tk.Label(root, text='', font=('Arial', 16), fg='#007bff')
result_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
