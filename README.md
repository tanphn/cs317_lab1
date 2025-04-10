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

## 📁 Cấu Trúc Pipeline

- `data/`
  - `raw/`: 📦 Dữ liệu gốc (DVC quản lý)
  - `processed/`: 🧹 Dữ liệu đã xử lý (DVC quản lý)

- `src/` — 💻 Mã nguồn chính:
  - `data_preprocessing.py`: 🌸 Tiền xử lý dữ liệu (Stage: preprocess)
  - `train.py`: 🧠 Huấn luyệnrepro
  Pipeline được định nghĩa trong dvc.yaml và điều phối bởi ClearML. Các bước chính bao gồm: preprocess, train, và evaluate:
  - **Preprocess**: Xử lý dữ liệu từ data/raw và lưu vào data/processed.
  - **Train**: Huấn luyện mô hình ResNet18 với 10 epoch, sử dụng Optuna để tối ưu lr và batch_size.
  - **Evaluate**: Đánh giá mô hình trên tập validation và lưu metric vào metrics/eval.json.\n
#### 4.2 **Chạy Pineline với ClearML**
  Chạy pipeline bằng lệnh:
     python clearml_pipeline.py
     
### 5. **Theo dõi kết quả**
  - **ClearML**:  
    Sau khi chạy pipeline, bạn sẽ thấy link ClearML results page trong log (ví dụ: `https://app.clear.ml/projects/...`).  
    Truy cập link để xem trạng thái pipeline, log, và artifact (như checkpoint mô hình, file metric).  
  
  - **Neptune**:  
    Truy cập `app.neptune.ai` để xem metric (loss, accuracy), checkpoint mô hình, và hyperparameters.  
  
  - **DVC**:  
    Dữ liệu được quản lý trong thư mục `data/processed`. Dùng lệnh sau để kéo dữ liệu mới nhất nếu cần:  
    ```bash
    dvc pull
