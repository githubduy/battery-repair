import re, copy, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_COLOR_INDEX, WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

SRC, OUT = sys.argv[1], sys.argv[2]
doc = Document(SRC)
body = doc.element.body
tbls = [c for c in body if c.tag == qn('w:tbl')]
assert len(tbls) == 2
hdr_tbl, sig_tbl = tbls

def norm(s):
    return ' '.join(s.replace('“', '"').replace('”', '"').split())

orig = list(doc.paragraphs)

def src(key):
    m = [p for p in orig if key in norm(p.text)]
    assert len(m) == 1, (key, len(m))
    el = copy.deepcopy(m[0]._p)
    for r in el.findall(qn('w:r')):
        if r.find(qn('w:footnoteReference')) is not None:
            el.remove(r)
    return el

T_TITLE = src('BÁO CÁO')
T_H = src('I. TRÊN LĨNH VỰC KINH TẾ')
T_BODY = src('Hoạt động thương mại - dịch vụ trên địa bàn cơ bản')

def strip_runs(el):
    for c in list(el):
        if c.tag != qn('w:pPr'):
            el.remove(c)
    return el

def add_text(p, text, size=14, bold=False, italic=False):
    for part in re.split(r'(\*\*[^*]+\*\*|\[[^\]]*\])', text):
        if not part:
            continue
        b, hl, t = bold, False, part
        if part.startswith('**') and part.endswith('**'):
            t, b = part[2:-2], True
        elif part.startswith('[') and part.endswith(']'):
            hl = True
        r = p.add_run(t)
        r.font.size = Pt(size)
        r.bold = b
        r.italic = italic
        if hl:
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW

def mk(tpl, text, size=14, bold=False, italic=False, keep=False):
    el = strip_runs(copy.deepcopy(tpl))
    p = Paragraph(el, doc._body)
    add_text(p, text, size, bold, italic)
    if keep:
        p.paragraph_format.keep_with_next = True
    return el

def P(text):
    return mk(T_BODY, text)

def BUL(text, tail=False):
    if tail:
        text += ' — Chủ trì: […]; hoàn thành: […]; kết quả: […].'
    el = mk(T_BODY, '- ' + text)
    p = Paragraph(el, doc._body)
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    return el

def H1(text):
    el = mk(T_H, text, bold=True, keep=True)
    Paragraph(el, doc._body).paragraph_format.first_line_indent = Cm(0)
    Paragraph(el, doc._body).paragraph_format.space_before = Pt(10)
    return el

def H2(text):
    el = mk(T_H, text, bold=True, keep=True)
    Paragraph(el, doc._body).paragraph_format.first_line_indent = Cm(0)
    return el

def H3(text):
    el = mk(T_H, text, bold=True, italic=True, keep=True)
    Paragraph(el, doc._body).paragraph_format.first_line_indent = Cm(0)
    return el

def CAP(text):
    return mk(T_BODY, text, size=12, bold=True, italic=True, keep=True)

def REUSE(key):
    return src(key)

def shade(cell, fill='D9D9D9'):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)

def TABLE(headers, rows, widths, size=9.5, center=(), blank_cols=()):
    rows = [[('' if ci in blank_cols else v) for ci, v in enumerate(r)] for r in rows]
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tblPr = t._tbl.tblPr
    mar = OxmlElement('w:tblCellMar')
    for side in ('left', 'right'):
        e = OxmlElement('w:' + side); e.set(qn('w:w'), '57'); e.set(qn('w:type'), 'dxa'); mar.append(e)
    tblPr.append(mar)
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement('w:' + edge)
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4')
        e.set(qn('w:space'), '0'); e.set(qn('w:color'), '000000')
        borders.append(e)
    tblPr.append(borders)
    t.autofit = False
    for i, w in enumerate(widths):
        t.columns[i].width = Cm(w)
    for ri, row in enumerate([headers] + rows):
        tr = t.rows[ri]
        if ri == 0:
            trPr = tr._tr.get_or_add_trPr()
            th = OxmlElement('w:tblHeader'); trPr.append(th)
        for ci, val in enumerate(row):
            cell = tr.cells[ci]
            cell.width = Cm(widths[ci])
            p = cell.paragraphs[0]
            pf = p.paragraph_format
            pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing = 1.0
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (ci in center or ri == 0 and ci in center) else WD_ALIGN_PARAGRAPH.LEFT
            pf.first_line_indent = Cm(0)
            add_text(p, val, size=size, bold=(ri == 0))
            if ri == 0:
                shade(cell)
    sig_tbl.addprevious(t._tbl)
    emit(mk(T_BODY, '', size=6))

def emit(el):
    sig_tbl.addprevious(el)

# ---------- collect reusable source paragraphs BEFORE deleting old body ----------
# ---------- remove old body content between header table and signature table ----------
el = hdr_tbl.getnext()
while el is not sig_tbl:
    nxt = el.getnext()
    body.remove(el)
    el = nxt

# ---------- title & intro ----------
emit(mk(T_TITLE, 'BÁO CÁO', bold=True))
emit(mk(T_TITLE, 'Tình hình thực hiện kế hoạch phát triển kinh tế - xã hội', bold=True))
emit(mk(T_TITLE, '10 tháng và ước năm 2026; xây dựng kế hoạch, phương án và kịch bản tăng trưởng năm 2027', bold=True))
emit(mk(T_TITLE, 'của xã An Nhơn Tây', bold=True))
emit(mk(T_BODY, ''))
emit(P('Thực hiện Thông báo số 1004/TB-UBND ngày 12/11/2026 kèm Phụ lục 02 - Đề cương định hướng báo cáo; '
       'Quyết định số 99/QĐ-UBND và Quyết định số 100/QĐ-UBND ngày 09/01/2026 của UBND tỉnh Gia Lai về giao chỉ tiêu '
       'kế hoạch phát triển kinh tế - xã hội năm 2026; Công văn số 11567/STC-TH ngày 05/11/2026 của Sở Tài chính, '
       'UBND xã An Nhơn Tây báo cáo tình hình thực hiện kế hoạch phát triển kinh tế - xã hội 10 tháng và ước năm 2026; '
       'xây dựng kế hoạch, phương án và kịch bản tăng trưởng năm 2027 như sau:'))
emit(P('Trên cơ sở Quyết định số 123/QĐ-UBND ngày 21/01/2026 và Quyết định số 1019/QĐ-UBND [ngày ban hành cần bổ sung] '
       'của UBND xã về giao và điều chỉnh chỉ tiêu kế hoạch năm 2026; Quyết định số 195/QĐ-UBND ngày 30/01/2026 ban hành '
       'Chương trình công tác trọng tâm năm 2026, UBND xã đã giao chỉ tiêu cho từng cơ quan, đơn vị và thôn để triển khai '
       'theo tháng, quý. Các cơ quan, đơn vị và thôn trên địa bàn đã chấp hành nghiêm túc các chỉ đạo của UBND tỉnh, '
       'Đảng ủy, HĐND xã; kinh tế - xã hội năm 2026 đạt nhiều kết quả tích cực trong bối cảnh còn khó khăn do biến động '
       'kinh tế thế giới, thời tiết diễn biến phức tạp và dịch bệnh trên cây trồng, vật nuôi.'))

# ---------- I ----------
emit(H1('I. ĐÁNH GIÁ TÌNH HÌNH THỰC HIỆN 10 THÁNG VÀ ƯỚC NĂM 2026'))
emit(H2('1. Kết quả thực hiện các chỉ tiêu chủ yếu'))
emit(P('Bảng 1 tổng hợp kết quả thực hiện 10 tháng, ước cả năm 2026 và mức độ hoàn thành các chỉ tiêu được giao. '
       'Cột “TH 10 tháng” để trống, sẽ điền khi có số liệu 10 tháng của các cơ quan chuyên môn.'))
emit(CAP('Bảng 1. Kết quả thực hiện chỉ tiêu chủ yếu năm 2026'))
TABLE(
    ['STT', 'Chỉ tiêu', 'ĐVT', 'KH 2026', 'TH 10 tháng', 'Ước năm 2026', '% so KH', 'Ghi chú'],
    [
        ['1', 'Tốc độ tăng giá trị sản phẩm', '%', '9,2', '[…]', '9,2', '100%', 'Theo giá so sánh 2020'],
        ['', '- Nông, lâm, thủy sản', '%', '3,97', '[…]', '3,97', '100%', ''],
        ['', '- Công nghiệp và xây dựng', '%', '11,22', '[…]', '11,22', '100%', ''],
        ['', '- Dịch vụ', '%', '9,01', '[…]', '9,01', '100%', ''],
        ['2', 'Tổng thu ngân sách phát sinh trên địa bàn', 'tỷ đồng', '53,143', '[…]', '60', '113%', ''],
        ['', '- Tiền sử dụng đất', 'tỷ đồng', '26', '[…]', '30', '115%', ''],
        ['3', 'Kim ngạch xuất khẩu', 'nghìn USD', '7.900', '[…]', '7.900', '100%', ''],
        ['4', 'Doanh thu bán lẻ hàng hóa và dịch vụ', 'tỷ đồng', '661', '[…]', '661', '100%', ''],
        ['5', 'Tỷ lệ dân số tham gia bảo hiểm y tế', '%', '98,9', '[…]', '98,81', '99,9%', '[Thống nhất: mục II ghi 98,81%; mục khác ghi 98,9%]'],
        ['6', 'Tỷ lệ trẻ em dưới 5 tuổi suy dinh dưỡng thể thấp còi', '%', '7,89', '[…]', '7,3', 'Vượt KH', 'Chỉ tiêu càng thấp càng tốt'],
        ['7', 'Giảm tỷ lệ hộ nghèo đa chiều', '%', '0', '[…]', '0', 'Đạt', ''],
        ['8', 'Bảo hiểm xã hội tự nguyện', 'người', '282', '[…]', '287', '101,77%', ''],
        ['9', 'Đào tạo nghề lao động nông thôn', 'người', '54', '[…]', '54', '100%', '03 lớp, 54 học viên'],
        ['10', 'Tỷ lệ che phủ rừng', '%', '47,82', '[…]', '47,82', '100%', ''],
        ['11', 'Tỷ lệ dân cư nông thôn sử dụng nước sạch qua hệ thống cấp nước tập trung', '%', '63,5', '[…]', '69,5', '109,4%', ''],
        ['12', 'Tỷ lệ chất thải rắn ở nông thôn được thu gom', '%', '89', '[…]', '89', '100%', '[Mục I.6 ghi 89,48% cho đô thị; cần xác nhận]'],
        ['13', 'Thu hút dự án mới', 'dự án', '2', '[…]', '3', '150%', '[Làm rõ: nhà đầu tư hay dự án]'],
        ['14', 'Công trình, dự án hoàn thành GPMB so với tổng số dự án trên địa bàn', '%', '≥ 50', '[…]', '50', 'Đạt', '[Mục I.4 ghi 7/10 công trình = 70%; cần thống nhất]'],
        ['15', 'Giảm tỷ lệ đơn khiếu nại về lĩnh vực đất đai phát sinh mới', '%', '10', '[…]', '10', 'Đạt', ''],
        ['16', 'Tỷ lệ giải quyết số vụ khiếu nại thuộc thẩm quyền', '%', '87', '[…]', '87', '100%', ''],
        ['17', 'Tỷ lệ giải ngân vốn đầu tư công so với kế hoạch HĐND tỉnh giao', '%', '100', '[…]', '100', '100%', '[Cần xác nhận số liệu giải ngân]'],
    ],
    [0.9, 4.6, 1.5, 1.5, 1.6, 1.7, 1.7, 3.0],
    center=(0, 2, 3, 4, 5, 6),
    blank_cols=(4,),
)
emit(P('Tổng giá trị sản phẩm trên địa bàn xã năm 2026 (theo giá so sánh 2020) ước đạt 4.603.890 triệu đồng, tăng 9,2% so cùng kỳ; '
       'trong đó nông, lâm, thủy sản ước đạt 1.113.493 triệu đồng (tăng 3,97%); công nghiệp - xây dựng ước đạt 3.109.692 triệu đồng '
       '(tăng 11,22%), gồm công nghiệp 2.089.845 triệu đồng (tăng 11,83%) và xây dựng 1.019.902 triệu đồng (tăng 9,99%); '
       'thương mại - dịch vụ ước đạt 380.705 triệu đồng (tăng 9,01%).'))
for k in ['Năm 2026, trong điều kiện tổ chức bộ máy', 'Kinh tế địa phương tiếp tục duy trì đà tăng trưởng',
          'Các lĩnh vực văn hóa - xã hội được quan tâm', 'Công tác cải cách hành chính, chuyển đổi số tiếp tục',
          'Quốc phòng - an ninh được giữ vững']:
    emit(src(k))

# I.2 kinh tế
emit(H2('2. Lĩnh vực kinh tế'))
emit(H3('2.1 Thương mại và dịch vụ'))
emit(src('Hoạt động thương mại - dịch vụ trên địa bàn'))
emit(src('Trong năm, thực hiện cấp mới trên 108'))
emit(H3('2.2 Sản xuất công nghiệp - xây dựng'))
emit(src('Hoạt động sản xuất công nghiệp tiếp tục'))
emit(P('Công tác thu hút đầu tư trong năm 2026 đã thu hút 03 [dự án/nhà đầu tư – cần làm rõ đơn vị tính], đạt 150% chỉ tiêu tỉnh giao '
       '(02). Trong năm, xã đã tiếp nhận và cấp 39 giấy phép xây dựng; tổ chức triển khai các dự án, công trình trong kế hoạch đầu tư năm 2026 '
       '(giải ngân trên 23,812 tỷ đồng).'))
emit(H3('2.3 Sản xuất nông, lâm nghiệp và thủy sản'))
emit(src('UBND xã tập trung triển khai kế hoạch sản xuất'))
emit(P('Chỉ đạo sản xuất vụ Đông Xuân 2025-2026 với tổng diện tích thực hiện 1.232,5 ha, tổng sản lượng lương thực có hạt ước tính 3.361,94 tấn; '
       'sản xuất vụ Hè Thu năm 2026 với tổng diện tích 1.220,1 ha, tổng sản lượng lương thực có hạt ước tính 7.095,35 tấn. '
       '[Cần kiểm tra lại số liệu vụ Đông Xuân: năng suất ước khoảng 2,7 tấn/ha, thấp hơn nhiều so với vụ Hè Thu khoảng 5,8 tấn/ha.]'))
emit(src('Công tác theo dõi, giám sát và áp dụng'))
emit(H3('2.4 Quy hoạch và đầu tư'))
for k in ['Công tác quy hoạch được tập trung', 'Đã phê duyệt chủ trương đầu tư',
          'Công tác bồi thường, hỗ trợ, tái định cư', 'Phê duyệt phương án đánh số']:
    emit(src(k))
emit(H3('2.5 Tài chính - ngân sách'))
emit(src('Tổng thu ngân sách xã năm 2026'))
emit(src('Chi ngân sách địa phương năm 2026'))
emit(P('[Cần kiểm tra: chi ngân sách địa phương cũng ghi 172 tỷ đồng, trùng với tổng thu ngân sách xã.]'))
emit(H3('2.6 Quản lý đất đai, tài nguyên khoáng sản và bảo vệ môi trường'))
emit(src('Công tác quản lý đất đai được thực hiện'))
emit(src('Công tác phòng, chống thiên tai được chủ động'))

# I.3 văn hóa - xã hội
emit(H2('3. Lĩnh vực văn hóa - xã hội'))
emit(H3('3.1 Nội vụ, tổ chức bộ máy và cải cách hành chính'))
for k in ['Công tác tổ chức bộ máy, quản lý cán bộ', 'Công tác sắp xếp đơn vị hành chính thôn',
          'Đề án thành lập phường An Nhơn Tây được xây dựng', 'Công tác cải cách hành chính, chấn chỉnh']:
    emit(src(k))
emit(H3('3.2 Văn hóa, thông tin, thể thao và chuyển đổi số'))
for k in ['Các hoạt động thông tin, tuyên truyền', 'Công tác phát triển khoa học', 'Công tác tuyên truyền, hướng dẫn người dân']:
    emit(src(k))
emit(H3('3.3 Giáo dục và đào tạo'))
for k in ['Công tác quản lý nhà nước về giáo dục', 'Công tác kiểm tra điều kiện hoạt động giáo dục', 'Công tác đào tạo nghề cho lao động nông thôn được chú trọng']:
    emit(src(k))
emit(H3('3.4 Y tế, dân số, bảo hiểm và an sinh xã hội'))
for k in ['Công tác chăm sóc sức khỏe Nhân dân', 'Công tác quản lý nhà nước về hành nghề y',
          'Công tác thực hiện chính sách người có công', 'Công tác vận động người dân tham gia bảo hiểm']:
    emit(src(k))
emit(H3('3.5 Hoạt động của Trung tâm Phục vụ hành chính công'))
for k in ['Trung tâm Phục vụ hành chính công xã hoạt động', 'Trong năm 2026, Trung tâm tiếp nhận', 'Nhìn chung, chất lượng phục vụ']:
    emit(src(k))
emit(H3('3.6 Quốc phòng, an ninh và nội chính'))
for k in ['Công tác quốc phòng, quân sự địa phương', 'Công tác huấn luyện dân quân tự vệ',
          'Công tác giáo dục quốc phòng và an ninh', 'Triển khai đồng bộ các biện pháp bảo đảm an ninh',
          'Triển khai thực hiện "Chiến dịch', 'Công tác tiếp công dân được duy trì']:
    emit(src(k))

# I.4 dự án trọng điểm, đất đai, KPI
emit(H2('4. Tiến độ công trình, dự án trọng điểm; quy hoạch, đất đai và KPI năm 2026'))
emit(P('Công trình, dự án trọng điểm: [danh sách công trình, tiến độ thi công, giải ngân, dự kiến hoàn thành – cần bổ sung]. '
       'Hoàn thành GPMB 7/10 công trình, dự án (70%) theo báo cáo; [nêu các công trình còn vướng mắc và nguyên nhân].'))
emit(P('Sắp xếp cán bộ, công chức theo vị trí việc làm; xử lý trụ sở, nhà đất và tài sản công dôi dư theo phương án UBND tỉnh phê duyệt: '
       '[số trụ sở, nhà đất đã xử lý; tiến độ bàn giao, tiếp nhận – cần bổ sung].'))
emit(P('Số hóa dữ liệu đất đai năm 2026: khối lượng hồ sơ đã rà soát […] thửa đất; đã chuẩn hóa, số hóa, cập nhật vào cơ sở dữ liệu […]; '
       'tỷ lệ hoàn thành so với nhiệm vụ được giao […]%. Số liệu còn thiếu, sai lệch và nguyên nhân: […].'))
emit(P('Đánh giá KPI năm 2026 đối với cơ quan, bộ phận, cán bộ, công chức: số nhiệm vụ, chỉ tiêu đã giao […]; mức độ hoàn thành […]; '
       'kết quả nổi bật […]; nhiệm vụ chậm và biện pháp khắc phục […]. Chỉ báo cáo kết quả đã có căn cứ.'))

# I.5 tồn tại
emit(H2('5. Tồn tại, hạn chế; chỉ tiêu chưa đạt và khả năng hoàn thành năm 2026'))
emit(src('Bên cạnh những kết quả đạt được'))
emit(P('Các chỉ tiêu chưa đạt hoặc có nguy cơ chưa đạt đến hết năm 2026: [nêu chỉ tiêu, nguyên nhân và khả năng hoàn thành trong tháng cuối năm – cần bổ sung].'))

# ---------- II ----------
emit(H1('II. TIỀM NĂNG, LỢI THẾ VÀ DƯ ĐỊA TĂNG TRƯỞNG NĂM 2027'))
emit(P('Rà soát các lợi thế có thể khai thác ngay trong năm 2027:'))
emit(BUL('**Quỹ đất, quy hoạch:** quy hoạch chi tiết tỷ lệ 1/500 đã phê duyệt cho các khu dân cư, điểm dân cư xen kẹt và nhà, đất dôi dư; '
         'quỹ đất tại Khu dân cư phía Đông đường Tân Lập 4 và Khu dân cư Nam Tượng khu vực 2.'))
emit(BUL('**Hạ tầng giao thông và cụm công nghiệp:** cụm công nghiệp với các ngành chế biến nông sản, chế biến gỗ, cơ khí, may mặc, thép và vận tải; '
         'tuyến đường ĐX.314 (đoạn cầu ông Tạo đến tràn Hồ núi I) dự kiến thảm nhựa trong năm 2027.'))
emit(BUL('**Vùng sản xuất, sản phẩm chủ lực:** làng nghề rượu Bàu Đá, bánh tráng Trường Cửu; sản phẩm OCOP; vùng sản xuất lúa vụ Đông Xuân và Hè Thu; chăn nuôi nông hộ.'))
emit(BUL('**Doanh nghiệp, hợp tác xã, hộ kinh doanh đang hoạt động:** 30 doanh nghiệp và 2.124 cơ sở kinh doanh cá thể (Tổng điều tra kinh tế năm 2026); '
         'hợp tác xã sau hợp nhất; 108 giấy phép đăng ký kinh doanh cấp mới trong năm 2026.'))
emit(BUL('**Dự án khởi công, thi công, hoàn thành:** [danh sách cụ thể theo tên dự án, giai đoạn – cần bổ sung].'))
emit(BUL('**Điểm du lịch, cơ sở lưu trú, thương mại và dịch vụ:** nguồn lực từ di sản Hát Bội Bình Định và nghệ thuật Bài Chòi; '
         '[cần bổ sung danh sách điểm du lịch, cơ sở lưu trú hiện có].'))
emit(P('Lựa chọn 5 động lực tăng trưởng có tác động lớn nhất và lượng hóa theo quý (Bảng 2). Mỗi động lực có số liệu năm 2026 làm cơ sở so sánh; '
       'số liệu chưa có được để trong ngoặc vuông và đánh dấu.'))
emit(CAP('Bảng 2. Các động lực tăng trưởng năm 2027 (tránh tính trùng giữa các động lực)'))
TABLE(
    ['STT', 'Động lực tăng trưởng', 'Doanh nghiệp / cơ sở / dự án', 'Cơ sở so sánh năm 2026', 'Mức tăng dự kiến 2027 và phân kỳ quý', 'Đơn vị theo dõi; vướng mắc cần giải quyết'],
    [
        ['1', 'Sản lượng và giá trị sản xuất tăng thêm (công nghiệp, chế biến, nông nghiệp CNC, OCOP)', '[Tên DN, cơ sở trong CCN – cần bổ sung]',
         'Công nghiệp 2.089.845 triệu đồng (+11,83%); nông, lâm, thủy sản 1.113.493 triệu đồng (+3,97%)',
         'Tăng […]% (…triệu đồng); Q1 […] · Q2 […] · Q3 […] · Q4 […]', '[Đơn vị theo dõi]; vướng mắc: […]'],
        ['2', 'Doanh thu dịch vụ', 'Điểm thương mại - dịch vụ trong các khu quy hoạch dân cư; hộ kinh doanh, cơ sở lưu trú',
         'Thương mại - dịch vụ 380.705 triệu đồng (+9,01%); bán lẻ hàng hóa và dịch vụ 661 tỷ đồng',
         'Bán lẻ 664 tỷ đồng (+0,5%) [mức tăng thấp, cần xem xét lại]; Q1 […] · Q2 […] · Q3 […] · Q4 […]', '[Đơn vị theo dõi]'],
        ['3', 'Khối lượng xây dựng thực hiện', 'Khu dân cư phía Đông đường Tân Lập 4; Khu dân cư Nam Tượng khu vực 2 (giai đoạn 3); đường D8',
         'Giá trị xây dựng 1.019.902 triệu đồng (+9,99%)',
         'Tăng […]%; Q1 […] · Q2 […] · Q3 […] · Q4 […]', 'Vướng mắc chính: GPMB; [đơn vị theo dõi]'],
        ['4', 'Dự án mới khởi công, hoàn thành, đưa vào vận hành', '[Tên dự án thu hút mới; dự án đang thi công]',
         '2026: 03 dự án thu hút mới; [số dự án khởi công, hoàn thành 2026 – cần bổ sung]',
         '2027: 02 dự án mới (KH); khởi công […]; hoàn thành […]', '[Đơn vị theo dõi]'],
        ['5', 'Sự kiện kích cầu', 'Hội chợ, xúc tiến thương mại, OCOP, du lịch – ghi cụ thể theo quý',
         '[Số sự kiện, lượt khách, doanh thu 2026 – cần bổ sung]',
         'Ít nhất 01 hoạt động, sự kiện mỗi quý (theo nhóm nhiệm vụ 4)', '[Đơn vị tổ chức]'],
    ],
    [1.0, 2.9, 3.1, 3.3, 3.2, 3.0],
    center=(0,),
)

# ---------- III ----------
emit(H1('III. DỰ KIẾN KHUNG CHỈ TIÊU VÀ KỊCH BẢN PHÁT TRIỂN KINH TẾ - XÃ HỘI NĂM 2027'))
emit(P('UBND xã phối hợp Sở Tài chính, Thống kê tỉnh và các sở chuyên ngành đề xuất khung chỉ tiêu, phấn đấu tổng giá trị sản phẩm trên địa bàn '
       'tăng từ 10% trở lên theo định hướng của tỉnh, phù hợp điều kiện thực tế; đồng thời xây dựng mục tiêu tăng thu nhập bình quân đầu người. '
       'Đối với 02 chỉ tiêu tổng hợp cấp xã (tổng giá trị sản phẩm trên địa bàn và thu nhập bình quân đầu người), sử dụng phương pháp, mẫu biểu và '
       'hướng dẫn của cơ quan có thẩm quyền; số liệu do địa phương đề xuất không thay thế kết quả thống kê chính thức.'))
emit(CAP('Bảng 3. Khung chỉ tiêu phát triển kinh tế - xã hội năm 2027'))
Q = 'Q1 […] · Q2 […] · Q3 […] · Q4 […]'
TABLE(
    ['STT', 'Chỉ tiêu', 'ĐVT', 'Ước 2026', 'KH 2027', 'Mức tăng', 'Tiến độ theo quý', 'Nguồn số liệu; cơ quan chịu trách nhiệm'],
    [
        ['1', 'Tổng giá trị sản phẩm trên địa bàn (giá so sánh 2020) – chỉ tiêu tổng hợp cấp xã', 'triệu đồng', '4.603.890 (+9,2%)', '≥ 10% (khoảng 5.064.279 triệu đồng)', '≥ 10%', Q, 'Thống kê xã, phối hợp Thống kê tỉnh'],
        ['2', 'Thu nhập bình quân đầu người – chỉ tiêu tổng hợp cấp xã', 'triệu đồng/người', '[…]', '[…]', '[…]', Q, '[Cần bổ sung]'],
        ['3', 'Sản lượng nông nghiệp: lương thực có hạt (hai vụ)', 'tấn', '10.457,29 [cần kiểm tra]', '[…]', '[…]', Q, '[Cơ quan nông nghiệp]'],
        ['4', 'Giá trị sản xuất công nghiệp - xây dựng (tăng trưởng)', '%', '11,22', '11,24 [cần tính lại]', '—', Q, '[Cần bổ sung]'],
        ['5', 'Sản lượng công nghiệp', '[đơn vị]', '[…]', '[…]', '[…]', Q, '[Cần bổ sung]'],
        ['6', 'Doanh thu bán lẻ hàng hóa và dịch vụ', 'tỷ đồng', '661', '664', '+0,5%', Q, '[Cơ quan Thống kê, Thuế]'],
        ['7', 'Tổng thu ngân sách phát sinh trên địa bàn', 'tỷ đồng', '60', '43,79', '−27,0% [cần giải trình]', Q, 'Cơ quan thuế phối hợp; Sở Tài chính'],
        ['8', 'Tiền sử dụng đất', 'tỷ đồng', '30', '25', '−16,7%', Q, 'Cơ quan quản lý đất đai; cơ quan thuế'],
        ['9', 'Tỷ lệ giải ngân vốn đầu tư công', '%', '100', '100', '—', Q, '[Đơn vị chủ đầu tư; Kho bạc]'],
        ['10', 'Thu hút dự án mới', 'dự án', '3', '2', '—', Q, '[Đơn vị chủ trì]'],
        ['11', 'Số dự án khởi công, hoàn thành', 'dự án', '[…]', '[…]', '—', Q, '[Cần bổ sung]'],
        ['12', 'Doanh nghiệp thành lập mới', 'doanh nghiệp', '[…] [cần xác nhận]', '[…]', '[…]', Q, '[Cơ quan đăng ký kinh doanh]'],
        ['13', 'Việc làm mới', 'người', '[…]', '[…]', '[…]', Q, '[Cần bổ sung]'],
        ['14', 'Tỷ lệ hộ nghèo đa chiều giảm', '%', '0', '0', '—', Q, '[Cần bổ sung]'],
        ['15', 'Tỷ lệ dân số tham gia bảo hiểm y tế', '%', '98,81', '98,9', '—', Q, 'Bảo hiểm xã hội'],
        ['16', 'Bảo hiểm xã hội tự nguyện', 'người', '287', '287 [cần xem xét tăng]', '—', Q, 'Bảo hiểm xã hội'],
        ['17', 'Đào tạo nghề lao động nông thôn', 'người', '54', '50 [cần xem xét lại]', '−7,4%', Q, '[Đơn vị đào tạo]'],
        ['18', 'Tỷ lệ che phủ rừng', '%', '47,82', '47,82', '—', Q, '[Cơ quan nông nghiệp]'],
        ['19', 'Tỷ lệ dân cư nông thôn dùng nước sạch qua cấp nước tập trung', '%', '69,5', '85', '+15,5 điểm %', Q, '[Đơn vị cấp nước]'],
        ['20', 'Tỷ lệ chất thải rắn nông thôn được thu gom', '%', '89', '90', '+1 điểm %', Q, '[Đơn vị môi trường]'],
        ['21', 'Tỷ lệ trẻ em dưới 5 tuổi suy dinh dưỡng thể thấp còi', '%', '7,3', '7,00', 'Giảm 0,3 điểm %', Q, 'Trạm Y tế xã'],
        ['22', 'Số công trình, dự án hoàn thành GPMB so với tổng số dự án', '%', '50 [thống nhất với 70%]', '≥ 50', '—', Q, '[Bộ phận GPMB]'],
        ['23', 'Tỷ lệ giải quyết khiếu nại thuộc thẩm quyền', '%', '87', '100', '+13 điểm %', Q, '[Bộ phận tiếp công dân]'],
        ['24', 'Giảm tỷ lệ đơn khiếu nại đất đai phát sinh mới', '%', '10', '10', '—', Q, '[Bộ phận tiếp công dân]'],
    ],
    [1.0, 3.8, 1.7, 1.9, 2.1, 1.6, 2.5, 1.9],
    size=8.5,
    center=(0, 2, 3, 4, 5),
)
emit(P('Mức tăng tính so với ước năm 2026. Các chỉ tiêu tổng hợp cấp xã (STT 1 và 2) áp dụng phương pháp, mẫu biểu do cơ quan có thẩm quyền ban hành.'))
emit(P('[Cần rà soát: nếu các ngành tăng theo KH (nông, lâm, thủy sản 3,97%; công nghiệp - xây dựng 11,24%; dịch vụ 9,5%) thì tổng giá trị sản phẩm '
       'chỉ đạt khoảng 9,3%, chưa đạt mục tiêu từ 10% trở lên; cần điều chỉnh tỷ trọng ngành.]'))
emit(H2('Kịch bản tăng trưởng năm 2027'))
emit(CAP('Bảng 4. Ba kịch bản tăng trưởng năm 2027'))
TABLE(
    ['Kịch bản', 'Điều kiện giả định', 'GTSP tăng', 'Thu ngân sách phát sinh'],
    [
        ['Cơ sở', 'Đạt các chỉ tiêu tại Bảng 3; GPMB và đấu giá quyền sử dụng đất đúng tiến độ; dự án đầu tư khởi công đúng kế hoạch', '10%', '43,79 tỷ đồng (KH 2027)'],
        ['Thận trọng', '[Nêu giả định, ví dụ: chậm GPMB tại … ; đấu giá đất chuyển sang năm sau]', '[…]%', '[…] tỷ đồng'],
        ['Phấn đấu cao', '[Nêu giả định, ví dụ: khởi công thêm … dự án; đẩy nhanh đấu giá đất]', '[…]%', '[…] tỷ đồng'],
    ],
    [2.6, 7.6, 2.4, 3.9],
)

# ---------- IV ----------
emit(H1('IV. NHIỆM VỤ, GIẢI PHÁP TRỌNG TÂM NĂM 2027'))
emit(P('UBND xã lựa chọn nhiệm vụ phù hợp địa bàn, xác định rõ đầu việc, kết quả, mốc hoàn thành, lãnh đạo phụ trách và đơn vị phối hợp. '
       'Mỗi nhiệm vụ ghi rõ: việc gì – ai chủ trì – hoàn thành khi nào – kết quả bao nhiêu; các ô […] cần điền trước khi trình ký.'))
emit(H2('A. Các nhiệm vụ chung'))
for k in ['Thường xuyên rà soát, triển khai các Chương trình', 'Tiếp tục quán triệt và chỉ đạo, điều hành theo hướng bám sát',
          'Toàn bộ hệ thống chính quyền chuyển đổi', 'Cán bộ, công chức phải nâng cao tinh thần trách nhiệm']:
    emit(src(k))
emit(H2('B. Các nhiệm vụ cụ thể'))

emit(H3('Nhóm 1. Nông nghiệp, lâm nghiệp và thủy sản'))
for t in ['Xác định cây trồng, vật nuôi, vùng nguyên liệu, sản phẩm chủ lực và cơ sở chế biến; giao chỉ tiêu diện tích, năng suất, sản lượng theo vụ, quý',
          'Chuyển đổi diện tích kém hiệu quả; phát triển liên kết doanh nghiệp - hợp tác xã - nông dân; mã số vùng trồng, OCOP, truy xuất nguồn gốc',
          'Đôn đốc dự án trang trại, chế biến, thủy sản và lâm nghiệp đủ điều kiện đi vào hoạt động; tháo gỡ đất đai, nước tưới, dịch bệnh, môi trường và đầu ra sản phẩm',
          'Phát triển chăn nuôi an toàn thực phẩm, thí điểm truy xuất nguồn gốc trong chăn nuôi; tái đàn phù hợp, kiểm soát dịch bệnh đàn vật nuôi',
          'Kêu gọi, tạo điều kiện triển khai dự án nông nghiệp ứng dụng công nghệ cao; xây dựng thương hiệu sản phẩm OCOP']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 2. Công nghiệp, tiểu thủ công nghiệp và năng lượng'))
for t in ['Lập danh sách doanh nghiệp, cơ sở sản xuất đang hoạt động theo từng ngành, lĩnh vực; cập nhật hằng tháng công suất, sản lượng, đơn hàng, lao động, khó khăn và khả năng tăng trưởng',
          'Hỗ trợ doanh nghiệp chủ lực mở rộng sản xuất, nâng công suất, cải tiến công nghệ; phát huy làng nghề rượu Bàu Đá, bánh tráng Trường Cửu',
          'Theo dõi tiến độ dự án chế biến, năng lượng, hạ tầng khu, cụm công nghiệp; lượng hóa giá trị sản xuất tăng thêm theo quý']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 3. Quy hoạch, xây dựng, hạ tầng và giải ngân đầu tư công'))
for t in ['Đẩy nhanh bồi thường, giải phóng mặt bằng để triển khai: Đầu tư hạ tầng Khu dân cư phía Đông đường Tân Lập 4; Đầu tư hạ tầng Khu dân cư Nam Tượng khu vực 2 (giai đoạn 3); Đầu tư xây dựng tuyến đường D8',
          'Thảm nhựa tuyến đường ĐX.314 (đoạn cầu ông Tạo đến tràn Hồ núi I); lát gạch block hoa viên vòng xuyến thôn Cù Lâm và hoa viên phía Bắc nhà ông Huỳnh Ngọc Anh, thôn Nhơn Lộc',
          'Giải ngân 100% kế hoạch vốn được giao; báo cáo hằng tháng khối lượng xây dựng thực hiện và tỷ lệ giải ngân; không đồng nhất giải ngân với giá trị sản xuất xây dựng',
          'Rà soát danh mục dự án đầu tư công, dự án ngoài ngân sách; xác định dự án chuẩn bị khởi công, đang thi công, dự kiến hoàn thành; lập tiến độ giải phóng mặt bằng, thi công, nghiệm thu, thanh toán theo từng quý',
          'Phối hợp các xã có liên quan rà soát quy hoạch liên địa bàn; xác định nội dung điều chỉnh, cơ quan có thẩm quyền và thời hạn đề xuất']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 4. Thương mại, dịch vụ, du lịch và tổ chức sự kiện'))
for t in ['Theo dõi theo từng nhóm ngành các cơ sở bán lẻ, chợ, vận tải, logistics, nhà hàng, khách sạn, lưu trú, du lịch; cập nhật cơ sở hoạt động, doanh thu, lượt khách theo mẫu biểu thống nhất',
          'Mỗi quý chủ động tổ chức hoặc phối hợp tổ chức ít nhất 01 hoạt động, sự kiện phù hợp thế mạnh địa phương (xúc tiến thương mại, hội chợ, văn hóa - thể thao, du lịch, giới thiệu sản phẩm OCOP), có kế hoạch trước',
          'Hoàn thành việc đấu giá quyền sử dụng đất để thực hiện dự án trên địa bàn; đẩy mạnh bán đấu giá quyền sử dụng đất ở tại các khu quy hoạch dân cư gắn với điểm thương mại - dịch vụ',
          'Phát triển thương mại điện tử, thanh toán số và sản phẩm du lịch mới; kiểm tra thị trường, an toàn thực phẩm, chống buôn lậu và gian lận thương mại']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 5. Thu hút đầu tư, khởi công và đẩy nhanh tiến độ dự án'))
for t in ['Chủ động chuẩn bị danh mục dự án kêu gọi đầu tư, thông tin quy hoạch, quỹ đất, hạ tầng, điều kiện tiếp nhận nhà đầu tư; phấn đấu thu hút ít nhất 01 dự án mới phù hợp tiềm năng và điều kiện thực tế',
          'Lập danh mục theo 04 nhóm: (i) đang xúc tiến, nghiên cứu; (ii) đã chấp thuận đầu tư, cần hoàn thiện thủ tục khởi công; (iii) đã khởi công, đang thi công; (iv) sắp hoàn thành, đưa vào hoạt động',
          'Chủ tịch UBND xã trực tiếp theo dõi các dự án trọng điểm; đôn đốc nhà đầu tư hoàn thiện hạ tầng kỹ thuật; báo cáo UBND tỉnh các vướng mắc vượt thẩm quyền']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 6. Thu ngân sách, nhất là thu từ đất; quản lý nguồn lực và tài sản công'))
for t in ['Xây dựng kịch bản thu năm 2027 theo từng nguồn thu, địa bàn, doanh nghiệp, dự án; phối hợp cơ quan thuế quản lý nguồn thu, chống thất thu, xử lý nợ đọng',
          'Lập danh mục từng khu đất, dự án, quỹ đất có khả năng đấu giá hoặc tạo nguồn thu: diện tích, pháp lý, quy hoạch, giải phóng mặt bằng, giá trị dự kiến, thời điểm tổ chức đấu giá và khả năng nộp ngân sách theo quý; chỉ đưa vào kịch bản các khoản có căn cứ',
          'Trụ sở, nhà đất và tài sản công dôi dư sau sắp xếp: lập danh mục theo hiện trạng, đơn vị quản lý, hình thức xử lý, tiến độ bàn giao; không để tài sản bỏ trống, xuống cấp hoặc sử dụng sai mục đích',
          'Sử dụng ngân sách tiết kiệm, hiệu quả; rà soát, xử lý vướng mắc thuộc thẩm quyền']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 7. Phát triển doanh nghiệp, việc làm và các lĩnh vực xã hội'))
for t in ['Thiết lập danh sách, phân nhóm doanh nghiệp, hợp tác xã, hộ kinh doanh theo ngành, lĩnh vực, địa bàn; phân công đầu mối thường xuyên nắm tình hình sản xuất, kinh doanh, đơn hàng, lao động, nhu cầu mở rộng và khó khăn',
          'Khuyến khích thành lập doanh nghiệp, chuyển đổi hộ kinh doanh đủ điều kiện, khởi nghiệp và ứng dụng khoa học - công nghệ',
          'Gắn phát triển sản xuất, dịch vụ với tạo việc làm, tăng thu nhập, đào tạo nghề theo nhu cầu doanh nghiệp, giảm nghèo, giáo dục, y tế, an sinh xã hội và bảo vệ môi trường; lượng hóa kết quả theo quý',
          'Xem xét điều chỉnh chỉ tiêu bảo hiểm xã hội tự nguyện 2027 (287 người, bằng kết quả 2026) và chỉ tiêu đào tạo nghề (50 người, thấp hơn 2026)']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 8. Tổ chức bộ máy, nhân sự, chuyển đổi số và quản trị theo kết quả'))
for t in ['Rà soát, bố trí cán bộ, công chức theo vị trí việc làm đã phê duyệt; xác định vị trí thiếu, thừa, kiêm nhiệm chưa phù hợp; đề xuất phương án kiện toàn, đào tạo, bồi dưỡng',
          'Hoàn thiện giao nhiệm vụ, chỉ tiêu, sản phẩm công việc năm 2027 theo từng vị trí, bộ phận; xác định người chịu trách nhiệm, thời hạn, tiêu chí đánh giá, chế độ kiểm tra và xử lý nhiệm vụ chậm tiến độ',
          'Tiếp tục chuẩn hóa, số hóa, cập nhật dữ liệu đất đai, ưu tiên hồ sơ tồn đọng; phối hợp cơ quan chuyên môn kiểm tra chất lượng dữ liệu',
          'Đẩy mạnh cải cách hành chính, nâng cao chất lượng Trung tâm Phục vụ hành chính công; triển khai dịch vụ công trực tuyến toàn trình, thanh toán không dùng tiền mặt, phong trào Bình dân học vụ số',
          'Duy trì theo dõi chỉ tiêu hằng tháng, đánh giá theo quý; cung cấp số liệu đúng biểu mẫu cho cơ quan chuyên môn']:
    emit(BUL(t, tail=True))

emit(H3('Nhóm 9. Quốc phòng, an ninh và nội chính (bổ sung ngoài 8 nhóm của đề cương)'))
for t in ['Thực hiện nghiêm chế độ trực sẵn sàng chiến đấu; bảo đảm 100% chỉ tiêu tuyển chọn, gọi công dân nhập ngũ và giao quân năm 2027',
          'Huấn luyện dân quân tự vệ đạt 100% chỉ tiêu, nâng tỷ lệ khá, giỏi; bảo đảm an toàn tuyệt đối về người và trang bị',
          'Phòng ngừa, đấu tranh với tội phạm và tệ nạn xã hội; tuần tra, kiểm soát, quản lý cư trú, phòng cháy chữa cháy, bảo đảm trật tự an toàn giao thông',
          'Tiếp công dân, giải quyết khiếu nại, tố cáo, kiến nghị đúng pháp luật; ưu tiên các vụ việc về đất đai, bồi thường, giải phóng mặt bằng có nguy cơ khiếu kiện đông người, vượt cấp',
          'Nâng cao hiệu quả hòa giải ở cơ sở; xây dựng xã đạt chuẩn tiếp cận pháp luật']:
    emit(BUL(t, tail=True))

# ---------- V ----------
emit(H1('V. KHÓ KHĂN, VƯỚNG MẮC VÀ KIẾN NGHỊ, ĐỀ XUẤT'))
emit(P('Lựa chọn 4 điểm nghẽn lớn nhất ảnh hưởng trực tiếp đến tăng trưởng, thu ngân sách (đặc biệt thu từ đất), giải ngân, khởi công và tiến độ dự án, '
       'số hóa dữ liệu đất đai. Mỗi kiến nghị nêu rõ tên dự án hoặc nội dung, tình trạng, nguyên nhân, việc địa phương đã xử lý, cơ quan có thẩm quyền, '
       'phương án đề xuất và thời hạn cần giải quyết.'))
emit(H2('1. Giải phóng mặt bằng các dự án chuyển tiếp và dự án mới'))
for t in ['Nội dung: Đầu tư hạ tầng Khu dân cư phía Đông đường Tân Lập 4; Đầu tư hạ tầng Khu dân cư Nam Tượng khu vực 2 (giai đoạn 3); tuyến đường D8',
          'Tình trạng: đã hoàn thành GPMB 7/10 công trình, dự án (70%); [nêu công trình còn vướng mắc]',
          'Nguyên nhân: […]; việc địa phương đã xử lý: […]',
          'Cơ quan có thẩm quyền: […]; đề xuất: […]; thời hạn: […]']:
    emit(BUL(t))
emit(H2('2. Dự toán thu ngân sách, nhất là thu tiền sử dụng đất năm 2027'))
for t in ['Nội dung: dự kiến thu ngân sách phát sinh 43,79 tỷ đồng, thu tiền sử dụng đất 25 tỷ đồng, thấp hơn ước năm 2026 (60 tỷ đồng và 30 tỷ đồng)',
          'Nguyên nhân: [quỹ đất đấu giá, pháp lý, quy hoạch – cần làm rõ]; việc địa phương đã xử lý: […]',
          'Đề xuất: đề nghị Sở Tài chính hướng dẫn xác định lại khung dự toán 2027 gắn với danh mục quỹ đất có căn cứ; thời hạn: […]']:
    emit(BUL(t))
emit(H2('3. Nâng tỷ lệ dân cư nông thôn dùng nước sạch từ 69,5% lên 85% năm 2027'))
for t in ['Tình trạng: tỷ lệ hiện đạt 69,5%; đang vận động hộ dân đấu nối, sử dụng nước sạch',
          'Nguyên nhân: [thiếu đường ống, kinh phí, tỷ lệ đấu nối – cần bổ sung]',
          'Đề xuất: đề nghị cơ quan chuyên môn cấp tỉnh hỗ trợ nguồn vốn, đơn vị cấp nước mở rộng mạng đường ống; thời hạn: […]']:
    emit(BUL(t))
emit(H2('4. Số hóa dữ liệu đất đai và đánh giá KPI năm 2026'))
for t in ['Tình trạng: khối lượng hồ sơ đã rà soát, chuẩn hóa, số hóa […]; tỷ lệ hoàn thành so với nhiệm vụ giao […]%; số liệu còn thiếu, sai lệch […]',
          'Nguyên nhân: […]; việc địa phương đã xử lý: […]',
          'Đề xuất: đề nghị cơ quan chuyên môn hướng dẫn thống nhất dữ liệu đã chuẩn hóa với dữ liệu tích hợp; thời hạn: […]']:
    emit(BUL(t))

# closing
emit(mk(T_BODY, ''))
emit(P('Trên đây là Báo cáo tình hình thực hiện kế hoạch phát triển kinh tế - xã hội 10 tháng và ước năm 2026; kế hoạch, phương án và kịch bản '
       'tăng trưởng năm 2027 trên địa bàn xã An Nhơn Tây. Kính báo cáo Sở Tài chính biết để theo dõi, chỉ đạo./.'))

doc.save(OUT)
print('saved', OUT)
