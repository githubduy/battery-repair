# AgentC: đặc tả bài test v1

AgentC nhận ảnh một bo mạch và xuất sơ đồ KiCad (`.kicad_sch`). Bài test chấm ba tầng: linh kiện, kết nối (net), và file có mở được trong KiCad hay không.

## 1. Quyết định đã chốt

| Mục | Lựa chọn |
|---|---|
| Loại bo | Bo BMS pin lithium trước; mạch tiêu dùng mở rộng sau khi đạt ngưỡng v1 |
| Tiêu chí đạt | Sơ đồ mở được trong KiCad |
| Cách chấm | Tự động so với đáp án đo tay (`score.py`) |

## 2. Cảnh báo về tiêu chí "mở được"

Một sơ đồ rỗng cũng mở được trong KiCad, nên tiêu chí này chưa đảm bảo AgentC đúng. Đề xuất: đạt khi vừa mở được, vừa vượt ngưỡng F1 linh kiện và điểm net. `score.py` đã có tham số `--min-comp-f1` và `--min-net-score`. Giá trị ngưỡng do bạn đặt trước khi chạy; hiện tôi chưa có căn cứ thực nghiệm để đề xuất con số cụ thể.

## 3. Bộ mẫu

- **Nguồn:** bo bạn sở hữu hoặc có quyền sử dụng. Không dùng bo thương mại để nhân bản.
- **Số lượng:** đề xuất tối thiểu 10 bo BMS, trong đó 3 bo làm bộ dev và phần còn lại làm bộ test. Con số này là đề xuất, chưa có căn cứ thống kê.
- **Đa dạng:** số cell, hãng BMS, có hoặc không cổng cân bằng riêng, một hoặc nhiều lớp mạch.
- **Điều kiện v1:** bo có ký hiệu linh kiện in trên mạch (silkscreen). Chấm net cần cùng tên linh kiện giữa đáp án và dự đoán. Bo không có ký hiệu để dành cho v2, khi có thuật toán ghép tên.
- **Chụp:** hai mặt, vuông góc, đèn đều, có thước đo, thêm ảnh cận cảnh từng IC. Bo đã tháo khỏi cell và không cấp nguồn khi chụp.

## 4. Đáp án đo tay

- **Linh kiện:** đọc ký hiệu và giá trị. Dùng đồng hồ hoặc LCR cho R, C, L; tra datasheet cho IC.
- **Kết nối:** dò bằng đồng hồ thông mạch hoặc suy từ ảnh. Mỗi net ghi rõ nguồn: "đã đo" hoặc "suy từ ảnh". Net đi qua lớp trong không đo được thì không đưa vào đáp án, và ghi rõ là đã bỏ qua.
- **Kiểm tra chéo:** hai người đo độc lập trên 3 bo dev, rồi so kết quả. Nếu hai bản không khớp, sửa quy trình đo trước khi làm bộ test.
- **Lưu:** `agentc/answer/<board_id>.json`, theo định dạng ở mục 5.

## 5. Định dạng

Đáp án (`answer.json`):

```json
{
  "board_id": "bms-001",
  "components": [
    {"ref": "U1", "part": "MCU-X", "pin_count": 8},
    {"ref": "R1", "value": "10k"}
  ],
  "nets": [
    {"name": "GND", "pins": ["U1.4", "R2.2"]}
  ]
}
```

- `ref` dùng đúng ký hiệu in trên bo.
- Chỉ net có từ hai chân trở lên được chấm.
- Tên net chỉ để đọc, không dùng để chấm.

Kết quả của AgentC: file `.kicad_sch` (đích cuối), và nếu có thể, kèm file JSON cùng định dạng để chấm từng tầng.

## 6. Chỉ số

| Tầng | Đo | Cách tính |
|---|---|---|
| A. Linh kiện | precision, recall, F1 | So khớp đa tập theo (tiền tố ref, giá trị hoặc part đã chuẩn hóa) |
| B. Kết nối | điểm net, số net khớp đúng | Mỗi net đáp án ghép với net dự đoán có Jaccard lớn nhất chưa dùng; điểm là trung bình Jaccard |
| C. KiCad | mở được hay không | `kicad-cli` xuất netlist thành công |
| D. Công sức | số thao tác sửa tay | Người sửa sơ đồ đến khi khớp đáp án. Đo tay, không tự động |

## 7. Quy tắc chạy

1. Đặt ngưỡng trước khi chạy và ghi vào mục 2.
2. AgentC không được xem đáp án. Không sửa prompt hay mã theo kết quả bộ test; chỉ chỉnh theo bộ dev.
3. Mỗi lần chạy lưu: phiên bản AgentC, ngày, file dự đoán, và báo cáo JSON.

## 8. Lệnh

```
python3 agentc/tests/test_score.py

python3 agentc/score.py --gold agentc/examples/answer_key.json --pred agentc/examples/pred_good.json

python3 agentc/score.py --gold <answer.json> --pred <output.kicad_sch> --require-open --min-comp-f1 <ngưỡng> --min-net-score <ngưỡng>
```

Lệnh chấm file `.kicad_sch` cần `kicad-cli`. Có thể xuất netlist XML trước rồi truyền file `.xml` nếu không có `kicad-cli`.

## 9. Giới hạn đã biết

- **Lớp trong:** bo nhiều lớp có đường mạch nằm trong lớp trong, không thấy trên ảnh. Net đi qua lớp trong dễ sai, và đáp án cần đo tay.
- **Linh kiện nhỏ:** điện trở và tụ SMD cỡ nhỏ có thể không đọc được giá trị từ ảnh. Giá trị trống hoặc sai sẽ làm giảm điểm tầng A.
- **IC mờ ký hiệu:** nếu không đọc được tên part thì không chấm được phần này.
- **KiCad chưa kiểm chứng:** lệnh `kicad-cli sch export netlist --format kicadxml` cần kiểm lại với phiên bản KiCad đang dùng. Bộ chấm chưa chạy thử với file KiCad thật.
- **Bộ mẫu nhỏ:** 10 bo cho độ tin cậy thấp. Đây là đề xuất, cần mở rộng khi kết quả ổn định.

## 10. An toàn và bản quyền

- Chỉ dùng bo bạn sở hữu hoặc được phép. Vẽ lại bo thương mại để nhân bản có thể vi phạm bản quyền và sở hữu trí tuệ.
- Khi chụp và đo: bo đã tháo khỏi cell, không cấp nguồn, không chạm vào mạch khi còn điện.
