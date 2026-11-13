import pandas as pd


def load_course_data():
    file_path = "전공, 교양 파일.xlsx"

    sheet_names = {
        "컴학 전공": "컴학전공",
        "타과 전공": "타과전공",
        "교양": "교양",
    }

    courses = {}

    for sheet_name, key in sheet_names.items():
        df = pd.read_excel(
            file_path,
            sheet_name=sheet_name,
            dtype={"강좌번호": str},
        )

        # 행 전체가 비어 있을 때만 제외
        df = df.dropna(how="all")

        # pandas의 NaN을 Python의 None으로 변환
        df = df.astype(object).where(pd.notna(df), None)

        # 각 행을 딕셔너리로 바꿔 저장
        courses[key] = df.to_dict(orient="records")

    return courses

if __name__ == "__main__":
    data = load_course_data()

    print(data.keys())
    print(data["교양"][1])
    print(data["교양"][0]["교과목명"])