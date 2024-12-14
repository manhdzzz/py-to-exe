import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert_to_exe():
    print("Python to EXE by MENJMOI")
    print("=================================")

    try:
        subprocess.run(["pyinstaller", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: PyInstaller is not installed or not found in PATH. Please install it with 'pip install pyinstaller'.")
        return
    Tk().withdraw()
    py_file_path = askopenfilename(filetypes=[("Python Files", "*.py")], title="Chọn file python muốn chuyển đổi:")

    if not py_file_path:
        print("Error: Không có file nào được chọn.")
        return
    try:
        print("Đang chuyển đổi...")
        subprocess.run(["pyinstaller", "--onefile", py_file_path], check=True)
        file_name = os.path.basename(py_file_path).replace(".py", ".exe")
        exe_file_path = os.path.join("manh", file_name)

        if os.path.exists(exe_file_path):
            print(f"Thành công: {exe_file_path}")
        else:
            print("Quá trình chuyển đổi đã hoàn tất, nhưng file EXE đã đi trốn, hãy thử lại hoặc đổi tên khác!")
    except subprocess.CalledProcessError as e:
        print("MENJMOI: Lỗi không mong muốn:")
        print(f"Chi tiết: {e}")
    except Exception as e:
        print(f"MENJMOI: Lỗi không xác định {e}")

if __name__ == "__main__":
    convert_to_exe()
