# CS317 Lab 1 - MLOps

## Mô Tả

Đây là project MLOps Lab 1, nơi triển khai pipeline cho bài toán phân loại hình ảnh với sử dụng các công cụ như Optuna, ClearML, Neptune, DVC và nhiều công cụ khác. Các bước chính của pipeline bao gồm:

- Tiền xử lý dữ liệu
- Huấn luyện mô hình với Optuna để tối ưu hóa hyperparameters
- Sử dụng ClearML để theo dõi quá trình huấn luyện và các kết quả
- Sử dụng Neptune để ghi nhận các thông số và kết quả
- Sử dụng DVC cho quản lý dữ liệu

## Các Công Cụ Sử Dụng

- **Optuna**: Dùng để tối ưu hóa hyperparameters của mô hình.
- **ClearML**: Dùng để theo dõi và quản lý các experiment trong quá trình huấn luyện.
- **Neptune**: Ghi nhận các thông số, mô hình, và kết quả huấn luyện.
- **DVC**: Quản lý dữ liệu và giúp version hóa dữ liệu huấn luyện.
- **PyTorch & Torchvision**: Dùng để xây dựng và huấn luyện mô hình học sâu.
- **Scikit-learn**: Dùng để đánh giá mô hình và tính toán các chỉ số như accuracy.

## Cấu Trúc Dự Án

