```markdown
# Hướng dẫn sử dụng PyInstaller

PyInstaller là một công cụ để đóng gói ứng dụng Python thành các tệp thực thi độc lập (executable) có thể chạy trên các hệ điều hành khác nhau như Windows, macOS và Linux.

## Các tùy chọn cơ bản của PyInstaller

### 1. Các lệnh chính

- **scriptname**: Tên của tệp script `.py` hoặc `.spec` mà bạn muốn PyInstaller xử lý. Nếu bạn chỉ định tệp `.spec`, hầu hết các tùy chọn khác sẽ bị bỏ qua.

### 2. Các tùy chọn chung

- **-h, --help**: Hiển thị trợ giúp về các lệnh và tùy chọn của PyInstaller.
  
  ```bash
  pyinstaller --help
  ```

- **-v, --version**: Hiển thị phiên bản của PyInstaller.

  ```bash
  pyinstaller --version
  ```

### 3. Định dạng đầu ra và tệp tin

- **--distpath DIR**: Đường dẫn nơi PyInstaller sẽ đặt ứng dụng đã được đóng gói. Mặc định là `./dist`.
  
  ```bash
  pyinstaller --distpath ./mydist myscript.py
  ```

- **--workpath WORKPATH**: Đường dẫn nơi PyInstaller lưu các tệp tạm thời trong quá trình đóng gói. Mặc định là `./build`.

  ```bash
  pyinstaller --workpath ./mybuild myscript.py
  ```

- **-y, --noconfirm**: Thay thế thư mục đầu ra mà không cần xác nhận. Ví dụ, nếu bạn muốn thay thế thư mục `dist` mà không cần hỏi lại.

  ```bash
  pyinstaller --noconfirm myscript.py
  ```

- **--upx-dir UPX_DIR**: Đường dẫn đến công cụ nén UPX (nếu có).

  ```bash
  pyinstaller --upx-dir /path/to/upx myscript.py
  ```

- **--clean**: Xóa bộ nhớ đệm và các tệp tạm thời của PyInstaller trước khi xây dựng lại.

  ```bash
  pyinstaller --clean myscript.py
  ```

### 4. Các loại đầu ra (What to generate)

- **-D, --onedir**: Tạo một thư mục chứa ứng dụng và tất cả các phụ thuộc của nó. Đây là mặc định của PyInstaller.

  ```bash
  pyinstaller --onedir myscript.py
  ```

- **-F, --onefile**: Tạo một tệp thực thi duy nhất (bundled executable).

  ```bash
  pyinstaller --onefile myscript.py
  ```

- **--specpath DIR**: Đặt thư mục để lưu tệp `.spec` được tạo ra. Mặc định là thư mục hiện tại.

  ```bash
  pyinstaller --specpath ./myspecs myscript.py
  ```

- **-n NAME, --name NAME**: Đặt tên cho ứng dụng và tệp `.spec`. Mặc định là tên của tệp `.py` không có phần mở rộng.

  ```bash
  pyinstaller --name myapp myscript.py
  ```

- **--contents-directory CONTENTS_DIRECTORY**: Dành cho chế độ `--onedir`, xác định thư mục chứa các tệp hỗ trợ (ngoài tệp thực thi).

  ```bash
  pyinstaller --onedir --contents-directory mydir myscript.py
  ```

### 5. Đóng gói dữ liệu và tệp tin nhị phân

- **--add-data SOURCE:DEST**: Thêm các tệp dữ liệu hoặc thư mục vào ứng dụng. `SOURCE` là đường dẫn tệp hoặc thư mục, còn `DEST` là thư mục đích trong ứng dụng.

  ```bash
  pyinstaller --add-data "data.txt:." myscript.py
  ```

- **--add-binary SOURCE:DEST**: Tương tự như `--add-data`, nhưng dành cho các tệp nhị phân.

  ```bash
  pyinstaller --add-binary "libmylib.so:." myscript.py
  ```

- **-p DIR, --paths DIR**: Thêm đường dẫn tìm kiếm module Python (tương tự như `PYTHONPATH`).

  ```bash
  pyinstaller --paths /path/to/mymodules myscript.py
  ```

- **--hidden-import MODULENAME**: Bao gồm một module mà PyInstaller không tự động phát hiện nhưng cần thiết cho ứng dụng.

  ```bash
  pyinstaller --hidden-import "myhiddenmodule" myscript.py
  ```

### 6. Các tùy chọn gỡ lỗi và tối ưu hóa

- **-d {all, imports, bootloader, noarchive}, --debug {all, imports, bootloader, noarchive}**: Cung cấp các tùy chọn gỡ lỗi giúp phát hiện lỗi trong quá trình biên dịch và khi chạy ứng dụng.
    - **all**: Mở tất cả các tùy chọn gỡ lỗi.
    - **imports**: Hiển thị thông tin về các module đang được import.
    - **bootloader**: Hiển thị thông tin về các bước khởi động ứng dụng.
    - **noarchive**: Lưu các tệp mã nguồn Python như các tệp riêng biệt thay vì đóng gói chúng thành một tệp duy nhất.

  ```bash
  pyinstaller --debug all myscript.py
  ```

- **--optimize LEVEL**: Mức độ tối ưu hóa mã bytecode khi đóng gói. Các mức độ bao gồm 0 (không tối ưu) đến 2 (tối ưu hóa mạnh).

  ```bash
  pyinstaller --optimize 2 myscript.py
  ```

- **--python-option PYTHON_OPTION**: Truyền thêm các tùy chọn cho trình thông dịch Python khi chạy ứng dụng.

  ```bash
  pyinstaller --python-option "v" myscript.py
  ```

### 7. Nén và loại bỏ tệp

- **-s, --strip**: Loại bỏ bảng ký hiệu và thông tin gỡ lỗi từ tệp thực thi và thư viện (không khuyến nghị trên Windows).

  ```bash
  pyinstaller --strip myscript.py
  ```

- **--noupx**: Không sử dụng công cụ nén UPX (mặc dù nó có sẵn).

  ```bash
  pyinstaller --noupx myscript.py
  ```

### 8. Các tùy chọn riêng biệt cho Windows và macOS

#### Windows:
- **-c, --console, --nowindowed**: Mở cửa sổ console (I/O chuẩn). Mặc định, nếu tệp Python có phần mở rộng `.pyw`, PyInstaller sẽ tự động sử dụng `--windowed`.
  
  ```bash
  pyinstaller --console myscript.py
  ```

- **-w, --windowed, --noconsole**: Không mở cửa sổ console (thường dùng cho các ứng dụng GUI).

  ```bash
  pyinstaller --windowed myscript.py
  ```

- **--hide-console {hide-late, minimize-late, minimize-early, hide-early}**: Ẩn hoặc thu nhỏ cửa sổ console khi ứng dụng khởi động trên Windows.

  ```bash
  pyinstaller --hide-console hide-late myscript.py
  ```

- **-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">**: Thêm biểu tượng cho tệp thực thi.

  ```bash
  pyinstaller --icon myicon.ico myscript.py
  ```

- **--disable-windowed-traceback**: Vô hiệu hóa việc hiển thị thông báo lỗi chi tiết trong chế độ cửa sổ (windowed mode).

#### macOS:
- **--argv-emulation**: Bật chế độ giả lập argv cho các gói ứng dụng macOS.

  ```bash
  pyinstaller --argv-emulation myscript.py
  ```

- **--osx-bundle-identifier BUNDLE_IDENTIFIER**: Đặt một mã định danh duy nhất cho gói ứng dụng macOS.

  ```bash
  pyinstaller --osx-bundle-identifier com.mycompany.app myscript.py
  ```

- **--codesign-identity IDENTITY**: Định danh chữ ký mã để ký ứng dụng trên macOS.

  ```bash
  pyinstaller --codesign-identity "Developer ID" myscript.py
  ```
