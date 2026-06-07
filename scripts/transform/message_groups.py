MESSAGE_GROUPS = {
    "A-737": {
        "317": {
            "description": "Từ nhận dạng",
        },
        "210": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "211": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "010": {
            "description": "Vĩ độ mở rộng / kinh độ mở rộng",
            "fields": [
                {
                    "name": "vi_do_mo_rong",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 0.000086,
                },
                {
                    "name": "kinh_do_mo_rong",
                    "start_pos": 12,
                    "end_pos": 22,
                    "min_val": 0,
                    "max_val": 0.000086,
                },
            ],
        },
        "223": {
            "description": "Độ cao của anten vệ tinh so với mực nước biển (m)",
            "fields": [
                {
                    "name": "do_cao_cua_anten_ve_tinh_so_voi_muc_nuoc_bien",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 131072,
                },
            ],
        },
        "266": {
            "description": "Vận tốc theo hướng bắc (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_bac",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ],
        },
        "267": {
            "description": "Vận tốc theo phương đông (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_dong",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ]
        },
        "264": {
            "description": "Vận tốc theo hướng thẳng (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_thang",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ],
        },
        "324": {
            "description": "Thời gian ghi dữ liệu (giờ - phút - giây)",
            "fields": [
                {
                    "name": "gio",
                    "start_pos": 3,
                    "end_pos": 8,
                    "min_val": 0,
                    "max_val": 32,
                },
                {
                    "name": "phut",
                    "start_pos": 8,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 64,
                },
                {
                    "name": "giay",
                    "start_pos": 14,
                    "end_pos": 20,
                    "min_val": 0,
                    "max_val": 64,
                },
            ],
        },
        "127": {
            "description": "Sai lệch thời gian (us)",
            "fields": [
                {
                    "name": "sai_lech_thoi_gian",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 209715.2,
                },
            ],
        },
        "320": {
            "description": "Sai số vị trí ước tính (m)",
            "fields": [
                {
                    "name": "sai_lech_vi_tri_uoc_tinh",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 32768,
                },
            ],
        },
        "126": {
            "description": "Thời gian (năm - tháng - ngày)",
            "fields": [
                {
                    "name": "nam",
                    "start_pos": 3,
                    "end_pos": 10,
                    "min_val": 0,
                    "max_val": 128,
                },
                {
                    "name": "thang",
                    "start_pos": 10,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 16,
                },
                {
                    "name": "ngay",
                    "start_pos": 14,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 32,
                },
            ],
        },
        "031": {
            "description": "Loại vệ tinh (số hiệu vị trí - hệ số suy hao - số lượng vệ tinh)",
            "fields": [
                {
                    "name": "so_hieu_vi_tri",
                    "start_pos": 3,
                    "end_pos": 9,
                    "min_val": 0,
                    "max_val": 64,
                },
                {
                    "name": "he_so_suy_hao",
                    "start_pos": 9,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 102.4,
                },
                {
                    "name": "so_luong_ve_tinh",
                    "start_pos": 19,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 16,
                },
            ],
        },
        "030": {
            "description": "Số lượng vệ tinh - tỷ số tín trên tạp - số kênh thu",
            "fields": [
                {
                    "name": "so_luong_ve_tinh",
                    "start_pos": 3,
                    "end_pos": 7,
                    "min_val": 0,
                    "max_val": 16,
                },
                {
                    "name": "ty_so_tin_tren_tap",
                    "start_pos": 7,
                    "end_pos": 15,
                    "min_val": 0,
                    "max_val": 25.6,
                },
                {
                    "name": "so_kenh_thu",
                    "start_pos": 15,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 16,
                },
            ],
        },
        "377": {
            "description": "Góc phương vị - góc ngẩng",
            "fields": [
                {
                    "name": "goc_phuong_vi",
                    "start_pos": 2,
                    "end_pos": 11,
                    "min_val": 0,
                    "max_val": 360,
                },
                {
                    "name": "goc_ngang",
                    "start_pos": 11,
                    "end_pos": 18,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "153": {
            "description": "Mã phiên bản phần mềm (năm - tháng - lĩnh vực - loại phần mềm - mã số PMO)",
        },
    },
    "Kh-31A (3B, 4B)": {
        "157": {
            "description": "Từ mã kiểm tra",
        },
        "141": {
            "description": "Cự ly",
            "fields": [
                {
                    "name": "cu_ly",
                    "start_pos": 5,
                    "end_pos": 16,
                    "min_val": 0,
                    "max_val": 120,
                },
            ],
        },
        "154": {
            "description": "Tốc độ tiếp cận",
            "fields": [
                {
                    "name": "toc_do_tiep_can",
                    "start_pos": 6,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 1.1,
                },
            ],
        },
        "156": {
            "description": "Cự ly kích hoạt",
            "fields": [
                {
                    "name": "cu_ly_kich_hoat",
                    "start_pos": 6,
                    "end_pos": 16,
                    "min_val": -60,
                    "max_val": -1,
                },
            ],
        },
        "150": {
            "description": "Góc nghiêng",
            "fields": [
                {
                    "name": "goc_nghieng",
                    "start_pos": 9,
                    "end_pos": 17,
                    "min_val": -45,
                    "max_val": 45,
                },
            ],
        },
        "151": {
            "description": "Góc ngẩng",
            "fields": [
                {
                    "name": "goc_ngang",
                    "start_pos": 9,
                    "end_pos": 17,
                    "min_val": -45,
                    "max_val": 45,
                },
            ],
        },
        "155": {
            "description": "Lệnh đơn",
        },
        "201": {
            "description": "Từ mã SUO",
        },
    },
    "PNK (5A)": {
        "331": {
            "description": "Góc nghiêng tanga hiện tại - pitch",
            "fields": [
                {
                    "name": "goc_nghieng_tanga_hien_tai",
                    "start_pos": 0,
                    "end_pos": 15,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "330": {
            "description": "Góc nghiêng kren hiện tại - roll",
            "fields": [
                {
                    "name": "goc_nghieng_kren_hien_tai",
                    "start_pos": 0,
                    "end_pos": 15,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "277": {
            "description": "Khóa la bàn từ tính (con quay hồi chuyển)",
            "fields": [
                {
                    "name": "khoa_la_ban_tu_tinh",
                    "start_pos": 0,
                    "end_pos": 10,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "273": {
            "description": "Bản tin 10",
            "fields": [
                {
                    "name": "ban_tin_10",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
    },
    "PNK (12A)": {
        "340": {
            "description": "Chiều cao hình học",
            "fields": [
                {
                    "name": "chieu_cao_hinh_hoc",
                    "start_pos": 2,
                    "end_pos": 20,
                    "min_val": 0,
                    "max_val": 6000,
                },
            ],
        },
    },
    "PNK (18A)": {
        "223": {
            "description": "Độ cao tuyệt đối theo áp suất",
            "fields": [
                {
                    "name": "do_cao_tuyet_doi_theo_ap_suat",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -500,
                    "max_val": 30000,
                },
            ],
        },
        "224": {
            "description": "Độ cao tương đối theo áp suất",
            "fields": [
                {
                    "name": "do_cao_tuong_doi_theo_ap_suat",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 30000,
                },
            ],
        },
        "226": {
            "description": "Vận tốc chỉ thị",
            "fields": [
                {
                    "name": "van_toc_chi_thi",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 150,
                    "max_val": 1600,
                },
            ],
        },
        "230": {
            "description": "Vận tốc không khí thực",
            "fields": [
                {
                    "name": "van_toc_khong_khi_thuc",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 150,
                    "max_val": 3500,
                },
            ],
        },
        "225": {
            "description": "Số mach hiện tại",
            "fields": [
                {
                    "name": "so_mach_hien_tai",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0.3,
                    "max_val": 3.5,
                },
            ],
        },
        "221": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 1000,
                },
            ],
        },
    },
    "PNK (20A)": {
        "211": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "210": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "266": {
            "description": "Vận tốc thành phần",
            "fields": [
                {
                    "name": "van_toc_thanh_phan",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -2500,
                    "max_val": 2500,
                },
            ],
        },
        "212": {
            "description": "Vận tốc hành trình",
            "fields": [
                {
                    "name": "van_toc_hanh_trinh",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 2500,
                },
            ],
        },
        "376": {
            "description": "Lệnh đơn",
        },
        "214": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
    },
    "PNK (21A)": {
        "000": {
            "description": "Dự phòng",
        },
        "240": {
            "description": "Dấu hiệu",
        },
        "241": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "242": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "204": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "272": {
            "description": "Tầm bay còn lại theo nhiên liệu",
            "fields": [
                {
                    "name": "tam_bay_con_lai_theo_nhien_lieu",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 20000,
                },
            ],
        },
    },
    "PNK (25A)": {
        "370": {
            "description": "Góc tấn công",
            "fields": [
                {
                    "name": "goc_tan_cong",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -10,
                    "max_val": 45,
                },
            ],
        },
        "322": {
            "description": "Góc tấn công tối đa cho phép",
            "fields": [
                {
                    "name": "goc_tan_cong_toi_da_cho_phep",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 5,
                    "max_val": 40,
                },
            ],
        },
        "323": {
            "description": "Góc tấn công tối thiểu",
            "fields": [
                {
                    "name": "goc_tan_cong_toi_thieu",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -10,
                    "max_val": 5,
                },
            ],
        },
        "371": {},
        "346": {
            "description": "Bản tin 14",
            "fields": [
                {
                    "name": "ban_tin_14",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -4,
                    "max_val": 10,
                },
            ],
        },
        "333": {},
        "326": {},
        "327": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -4,
                    "max_val": 1.5,
                },
            ],
        },
        "227": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 500,
                    "max_val": 1800,
                },
            ],
        },
        "321": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 200,
                    "max_val": 500,
                },
            ],
        },
        "373": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0.7,
                    "max_val": 3,
                },
            ],
        },
    },
    "PNK (11B, 41A)": {
        "332": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 16,
                    "min_val": -80,
                    "max_val": 80,
                },
            ],
        },
        "346": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 16,
                    "min_val": -0.2,
                    "max_val": 5,
                },
            ],
        },
        "376": {},
        "214": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 18,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "221": {},
        "230": {},
    },
    "SUO (9A)": {
        "241": {},
        "242": {},
        "243": {},
        "244": {},
        "245": {},
        "246": {},
        "247": {},
        "250": {},
        "251": {},
        "252": {},
    },
    "SUO (LS1)": {
        "211": {
            "description": "Vĩ độ địa lý",
            "fields": [
                {
                    "name": "vi_do_dia_ly",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "210": {
            "description": "Kinh độ địa lý",
            "fields": [
                {
                    "name": "kinh_do_dia_ly",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "245": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "242": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "240": {
            "description": "Hướng bay định trước",
            "fields": [
                {
                    "name": "huong_bay_dinh_truoc",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "214": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "215": {
            "description": "Chỉ thị mục tiêu theo góc phương vị",
            "fields": [
                {
                    "name": "chi_thi_muc_tieu_theo_goc_phuong_vi",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "216": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "217": {
            "description": "Bản tin số 10",
        },
        "220": {
            "description": "Bản tin số 11",
        },
        "221": {
            "description": "Vận tốc Wn",
            "fields": [
                {
                    "name": "van_toc_wn",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 3500,
                },
            ],
        },
        "222": {
            "description": "Vận tốc We",
            "fields": [
                {
                    "name": "van_toc_we",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 3500,
                },
            ],
        },
        "223": {
            "description": "Mức độ bẻ cần điều khiển",
            "fields": [
                {
                    "name": "ux",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 5,
                },
                {
                    "name": "uy",
                    "start_pos": 13,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 5,
                },
            ],
        },
        "224": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "225": {
            "description": "Bản tin số 16",
        },
        "226": {
            "description": "Bản tin số 17",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "227": {
            "description": "Bản tin số 18",
        },
        "230": {
            "description": "Bản tin số 19",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 40,
                },
            ],
        },
        "231": {
            "description": "Thành phần vận tốc theo trục X",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_x",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 3500,
                },
            ],
        },
        "232": {
            "description": "Thành phần vận tốc theo trục Y",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_y",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 3500,
                },
            ],
        },
        "233": {
            "description": "Thành phần vận tốc theo trục Z",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_z",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 3500,
                },
            ],
        },
    },
    "SUO (LS3)": {
        "320": {
            "description": "Xác nhận lệnh MFK",
        },
        "323": {
            "description": "Góc phương vị",
            "fields": [
                {
                    "name": "goc_phuong_vi",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "324": {
            "description": "Góc phương vị theo hướng bắc",
            "fields": [
                {
                    "name": "goc_phuong_vi_theo_huong_bac",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "325": {
            "description": "Khoảng cách",
            "fields": [
                {
                    "name": "khoang_cach",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 400,
                },
            ],
        },
        "326": {
            "description": "Tốc độ tiếp cận",
        },
        "327": {
            "description": "Thành phần vận tốc theo trục X",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_x",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 2000,
                },
            ],
        },
        "330": {
            "description": "Thành phần vận tốc theo trục Y",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_y",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 2000,
                },
            ],
        },
        "331": {
            "description": "Thành phần vận tốc theo trục Z",
            "fields": [
                {
                    "name": "thanh_phan_van_toc_theo_truc_z",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 2000,
                },
            ],
        },
        "332": {
            "description": "Bản tin 9",
        },
        "340": {
            "description": "Bản tin 10",
        },
        "341": {
            "description": "Cự ly bản đồ số",
            "fields": [
                {
                    "name": "d_max",
                    "start_pos": 4,
                    "end_pos": 13,
                    "min_val": 0,
                    "max_val": 400,
                },
                {
                    "name": "d_min",
                    "start_pos": 14,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 400,
                },
            ],
        },
        "342": {
            "description": "Bản tin 12",
        },
        "343": {
            "description": "Số hóa thang đo góc phương vị",
            "fields": [
                {
                    "name": "gioi_han_trai",
                    "start_pos": 5,
                    "end_pos": 13,
                    "min_val": 0,
                    "max_val": 180,
                },
                {
                    "name": "gioi_han_phai",
                    "start_pos": 15,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "344": {
            "description": "Vị trí máy bay trên bản đồ",
            "fields": [
                {
                    "name": "x",
                    "start_pos": 13,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 320,
                },
                {
                    "name": "y",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 240,
                },
            ],
        },
        "345": {
            "description": "Bản tin 15",
            "fields": [
                {
                    "name": "goc_dinh_huong_may_bay_tren_ban_do",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "346": {
            "description": "Bản tin 16",
            "fields": [
                {
                    "name": "vi_tri_diem_dau_anten",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 60,
                },
                {
                    "name": "vi_tri_diem_dau_anten",
                    "start_pos": 13,
                    "end_pos": 22,
                    "min_val": 0,
                    "max_val": 240,
                },
            ],
        },
        "347": {
            "description": "Bản tin 17",
        },
        "350": {
            "description": "Bản tin 18",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 333.5,
                },
                {
                    "name": "data_2",
                    "start_pos": 17,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 63,
                },
            ],
        },
        "351": {
            "description": "Bản tin 19",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 3,
                    "end_pos": 13,
                    "min_val": 0,
                    "max_val": 150,
                },
                {
                    "name": "data_2",
                    "start_pos": 13,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 110,
                },
            ],
        },
        "352": {
            "description": "Bản tin 20",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 3,
                    "end_pos": 13,
                    "min_val": 0,
                    "max_val": 110,
                },
                {
                    "name": "data_2",
                    "start_pos": 13,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 110,
                },
            ],
        },
        "353": {
            "description": "Bản tin 21",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "354": {
            "description": "Bản tin 22",
            "fields": [
                {
                    "name": "r_max",
                    "start_pos": 1,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 400,
                },
                {
                    "name": "r_min",
                    "start_pos": 12,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 400,
                },
            ],
        },
        "355": {
            "description": "Bản tin 23",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 2,
                    "end_pos": 10,
                    "min_val": 0,
                    "max_val": 400,
                },
                {
                    "name": "data_2",
                    "start_pos": 10,
                    "end_pos": 21,
                    "min_val": 0,
                    "max_val": 400,
                },
            ],
        },
        "356": {
            "description": "Bản tin 24",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 70,
                },
            ],
        },
        "357": {
            "description": "Bản tin 25",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 1152,
                },
            ],
        },
        "360": {
            "description": "Bản tin 26",
        },
        "361": {
            "description": "Bản tin 27",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 2,
                    "end_pos": 9,
                    "min_val": 0,
                    "max_val": 90,
                },
                {
                    "name": "data_2",
                    "start_pos": 13,
                    "end_pos": 20,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "362": {
            "description": "Bản tin 28",
            "fields": [
                {
                    "name": "data_1",
                    "start_pos": 10,
                    "end_pos": 16,
                    "min_val": 0,
                    "max_val": 45,
                },
                {
                    "name": "data_2",
                    "start_pos": 17,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 45,
                },
            ],
        },
        "310": {
            "description": "Vĩ độ tâm bản đồ rada",
            "fields": [
                {
                    "name": "vi_do_tam_ban_do_rada",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "311": {
            "description": "Kinh độ tâm bản đồ rada",
            "fields": [
                {
                    "name": "kinh_do_tam_ban_do_rada",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "312": {
            "description": "Bản tin 31",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "313": {
            "description": "Bản tin 32",
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 800,
                },
            ],
        },
        "314": {
            "description": "Bản tin 33",
        },
    },
}
