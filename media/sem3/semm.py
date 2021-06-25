from fpdf import FPDF


class PDF3(FPDF):
    def header(self):
        self.image('Sem3_header.jpg', 1.4, 0.5, w=227, h=64)
        # self.add_font('NotoSansKannada-Bold', '', "NotoSansKannada-Bold.ttf", uni=True)
        # self.set_font('NotoSansKannada-Bold', '', 11.9)
        # self.cell(0, 0, '', align='L')

    def footer(self):
        self.image('Sem3_footer.jpg', 0, 196, 228)

    def add_icon(self):
        self.image('icon.png', 20.1, 50, w=3.35, h=3.35)

    def add_watermark(self):
        self.image('VTU_logo_light.png', 74, 25, 121)

    def add_USN_Name(self, USN, Name, Sem):
        self.add_font('DroidSerif-Bold', '', "DroidSerif-Bold.ttf", uni=True)
        self.add_font('NotoSerif-Regular', '', "NotoSerif-Regular.ttf", uni=True)
        self.set_font('DroidSerif-Bold', '', 11.9)
        self.ln(63.2)
        self.cell(-67, 0, 'University Seat Number    :', align='')
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(0, 0, USN, align='C')
        self.ln(7)
        self.set_font('DroidSerif-Bold', '', 11.9)
        self.cell(57.5, 0, 'Student Name                       :', align='', border=0)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(0, 0, Name, ln=1, align='L')
        self.ln(11.6)
        self.set_font('DroidSerif-Bold', '', 12)
        self.cell(0, 0, f'Semester : {Sem}', ln=1, align='C')

    def add_table_title(self):
        self.image('TableTitle.png', 7.7, 96, 213.6)

    def add_tableForOne(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 109.9, 213.6)
        self.ln(22)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(19.8, 0, f"{sCode}", align='R', border=0)
        self.cell(74.8, 0, sName, align='R')
        self.cell(47.05, 0, iMarks, align='R')
        self.cell(23.9, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForOne1(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 117.8, 213.6)
        self.ln(7.8)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.1, 0, f"{sCode}", align='R', border=0)
        self.cell(83.8, 0, sName, align='R')
        self.cell(40.7, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(16.9, 0, result, align='R')

    def add_tableForOne2(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 125.75, 213.6)
        self.ln(7.9)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.1, 0, f"{sCode}", align='R', border=0)
        self.cell(86, 0, sName, align='R')
        self.cell(38.55, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForOne3(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 133.65, 213.6)
        self.ln(7.9)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.1, 0, f"{sCode}", align='R', border=0)
        self.cell(64, 0, sName, align='R')
        self.cell(60.55, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForOne4(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 141.6, 213.6)
        self.ln(7.9)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.1, 0, f"{sCode}", align='R', border=0)
        self.cell(76.5, 0, sName, align='R')
        self.cell(48, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForOne5(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 149.5, 213.6)
        self.ln(7.9)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.1, 0, f"{sCode}", align='R', border=0)
        self.cell(90.3, 0, sName, align='R')
        self.cell(34.2, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForTwo(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForTwo.png', 7.7, 157.4, 213.6)
        self.ln(8)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(18.5, 0, f"{sCode}", align='R', border=0)
        self.cell(83, 0, sName[:-10], align='R')
        self.cell(40.1, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')
        self.ln(5.7)
        self.cell(52.5, 0, 'LABORATORY', align='R')

    def add_tableForOne6(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 171.1, 213.6)
        self.ln(7.9)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(18.6, 0, f"{sCode}", align='R', border=0)
        self.cell(74, 0, sName, align='R')
        self.cell(49, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')

    def add_tableForOne7(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 179, 213.6)
        self.ln(7.95)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(19.3, 0, f"{sCode}", align='R', border=0)
        self.cell(37.5, 0, sName, align='R', border=0)
        self.cell(84.9, 0, iMarks, align='R')
        self.cell(24, 0, eMarks, align='R')
        self.cell(21, 0, total, align='R')
        self.cell(17, 0, result, align='R')
