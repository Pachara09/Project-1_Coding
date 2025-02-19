import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณความหนาแน่น
def calculate_density():
    try:
        # รับค่าจากผู้ใช้
        mass = float(mass_entry.get())
        volume = float(volume_entry.get())

        # ตรวจสอบปริมาตรที่เป็นค่าลบหรือศูนย์
        if volume <= 0:
            messagebox.showerror("Input Error", "Volume must be greater than zero.")
            return

        # คำนวณความหนาแน่น
        density = mass / volume

        # ฟังก์ชันแบ่งประเภทความหนาแน่น
        if density < 1000:
            density_type = "Low Density"
        elif density < 5000:
            density_type = "Mid Density"
        else:
            density_type = "High Density"

        # แสดงผลลัพธ์
        result_label.config(text=f"Density: {density:.2f} kg/m³\nThis material is: {density_type}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# ฟังก์ชันล้างข้อมูล
def clear_fields():
    mass_entry.delete(0, tk.END)
    volume_entry.delete(0, tk.END)
    result_label.config(text="")

# ฟังก์ชันออกจากโปรแกรม
def exit_program():
    root.quit()

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Density Calculator")
root.geometry("400x350")  # กำหนดขนาดหน้าต่าง

# กำหนดสีพื้นหลังและสีฟอนต์
root.config(bg="#f0f8ff")  # สีฟ้าอ่อน

# สร้างป้ายข้อความ (Label) และช่องกรอกข้อมูล (Entry) ด้วยฟอนต์และการจัดวาง
mass_label = tk.Label(root, text="Enter Mass (kg):", bg="#f0f8ff", font=("Arial", 12))
mass_label.pack(pady=10)  # เพิ่มระยะห่างระหว่างป้าย

mass_entry = tk.Entry(root, font=("Arial", 12), width=20)
mass_entry.pack(pady=5)

volume_label = tk.Label(root, text="Enter Volume (m³):", bg="#f0f8ff", font=("Arial", 12))
volume_label.pack(pady=10)

volume_entry = tk.Entry(root, font=("Arial", 12), width=20)
volume_entry.pack(pady=5)

# สร้างปุ่มเพื่อคำนวณความหนาแน่น
calculate_button = tk.Button(root, text="Calculate Density", command=calculate_density, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, height=2)
calculate_button.pack(pady=10)

# สร้างป้ายข้อความแสดงผลลัพธ์
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#333333")
result_label.pack(pady=10)

# สร้างปุ่ม "Clear" เพื่อล้างข้อมูล
clear_button = tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white", font=("Arial", 12), width=20, height=2)
clear_button.pack(pady=5)

# สร้างปุ่ม "Exit" ออกจากโปรแกรม
exit_button = tk.Button(root, text="Exit", command=exit_program, bg="#d32f2f", fg="white", font=("Arial", 12), width=20, height=2)
exit_button.pack(pady=5)

# เริ่มต้น GUI
root.mainloop()
