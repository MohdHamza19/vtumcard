from fpdf import FPDF
from django.views.static import serve
from django.http import HttpResponse
from .models import Pdf_mc
import os
import shutil


# hamza
# 1234

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


from fpdf import FPDF


class PDF5(FPDF):
    def header(self):
        self.image('Sem5_header.jpg', 0, 3.5, 228)

    def footer(self):
        self.image('Sem5_footer.jpg', 0, 196, 228)

    def add_watermark(self):
        self.image('VTU_logo_light.png', 74, 25, 121)

    def add_USN_Name(self, USN, Name, Sem):
        self.add_font('DroidSerif-Bold', '', "DroidSerif-Bold.ttf", uni=True)
        self.add_font('NotoSerif-Regular', '', "NotoSerif-Regular.ttf", uni=True)
        self.set_font('DroidSerif-Bold', '', 11.9)
        self.ln(63.2)
        self.cell(-67, 0, 'University Seat Number    :', align='')
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(0, 0, USN, ln=1, align='C')
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

    def add_tableForTwo(self, sCode, sName, iMarks, eMarks, total, result):
        self.ln(67)
        self.image('TableForTwo.png', 7.7, 109.9, 213.6)
        # self.image('TableForTwo.png', 7.7, self.y_count, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(17.5, -90, sCode, align='R')
        self.cell(91, -90, sName[:-9], align='R')
        self.cell(-62.5, -79, 'INDUSTRY', align='R')
        self.cell(95.5, -90, iMarks, align='R')
        self.cell(24, -90, eMarks, align='R')
        self.cell(21, -90, total, align='R')
        self.cell(17, -90, result, align='R')

    def add_tableForOne(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 123.8, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-96.5, -63, f"{sName}", align='R')
        # self.cell(-58, -63, f"{sName}                                    {iMarks}", align='R')
        self.cell(-195, -63, sCode, align='C')
        self.cell(0, -63,
                  f"                                                                                                                                              {iMarks}",
                  border=0,
                  align="C")
        self.cell(-43.5, -63, eMarks, align='R')
        self.cell(21, -63, total, align='R')
        self.cell(17, -63, result, align='R')

    def add_tableForOne1(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 132, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-130.5, -47, f"{sName}", align='R')
        self.cell(-55.5, -47, sCode, align='R')
        self.cell(241.5, -47, f"                      {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-151.3, -47, total, align='C', border=0)
        self.cell(96, -47, result, align='R')

    def add_tableForOne2(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 140.2, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-107, -31, f"{sName}", align='R')
        self.cell(-79.5, -31, sCode, align='R')
        self.cell(241.5, -31,
                  f"                       {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-151, -31, total, align='C', border=0)
        self.cell(96, -31, result, align='R')

    def add_tableForTwo2(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForTwo.png', 7.7, 148, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-101, -15, f"{sName[:-11]}", align='R')
        self.cell(-46, -3.5, f"DEVELOPMENT", align='R')
        self.cell(-38.1, -15, sCode, align='R', border=0)
        self.cell(241.5, -15,
                  f"                    {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-153.7, -15, total, align='C', border=0)
        self.cell(97.4, -15, result, align='R')

    def add_tableForOne3(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 161.7, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-91, 12.5, f"{sName}", align='R')
        self.cell(-95.5, 12.5, sCode, align='R', border=0)
        self.cell(244.5, 12.5,
                  f"                    {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-156.8, 12.5, total, align='C', border=0)
        self.cell(98.6, 12.5, result, align='R')

    def add_tableForOne4(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 169.6, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-103.5, 29, f"{sName}", align='R')
        self.cell(-81, 29, sCode, align='R', border=0)
        self.cell(241, 29,
                  f"                    {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-154, 29, total, align='C', border=0)
        self.cell(97.5, 29, result, align='R')

    def add_tableForOne5(self, sCode, sName, iMarks, eMarks, total, result):
        self.image('TableForOne.png', 7.7, 177.5, 213.6)
        self.set_font('NotoSerif-Regular', '', 11.9)
        self.cell(-94.5, 45, f"{sName}", align='R')
        self.cell(-90, 45, sCode, align='R', border=0)
        self.cell(241, 45,
                  f"                    {iMarks}                  {eMarks}", border=0,
                  align="C")
        self.cell(-154, 45, total, align='C', border=0)
        self.cell(97.5, 45, result, align='R')


from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'VTU/index.html')


def marks3(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        usn = request.POST.get('usn', '')

        enI = request.POST.get('enI', '')
        enE = request.POST.get('enE', '')
        enP = request.POST.get('enP', '')
        enT = int(enI) + int(enE)

        anI = request.POST.get('anI', '')
        anE = request.POST.get('anE', '')
        anP = request.POST.get('anP', '')
        anT = int(anI) + int(anE)

        daI = request.POST.get('daI', '')
        daE = request.POST.get('daE', '')
        daP = request.POST.get('daP', '')
        daT = int(daI) + int(daE)

        coI = request.POST.get('coI', '')
        coE = request.POST.get('coE', '')
        coP = request.POST.get('coP', '')
        coT = int(coI) + int(coE)

        unI = request.POST.get('unI', '')
        unE = request.POST.get('unE', '')
        unP = request.POST.get('unP', '')
        unT = int(unI) + int(unE)

        diI = request.POST.get('diI', '')
        diE = request.POST.get('diE', '')
        diP = request.POST.get('diP', '')
        diT = int(diI) + int(diE)

        anlI = request.POST.get('anlI', '')
        anlE = request.POST.get('anlE', '')
        anlP = request.POST.get('anlP', '')
        anlT = int(anlI) + int(anlE)

        dalI = request.POST.get('dalI', '')
        dalE = request.POST.get('dalE', '')
        dalP = request.POST.get('dalP', '')
        dalT = int(dalI) + int(dalE)

        kaI = request.POST.get('kaI', '')
        kaE = request.POST.get('kaE', '')
        kaP = request.POST.get('kaP', '')
        kaT = int(kaI) + int(kaE)

        pdf = PDF3('P', 'mm', (229, 324))
        # USN = '3AE17CS045'
        # Name = 'MOHAMMAD HAMZA'
        Sem = '3'
        pdf.add_page()
        pdf.add_icon()
        pdf.add_watermark()
        pdf.add_USN_Name(usn, name, Sem)
        pdf.add_table_title()
        pdf.add_tableForOne('17MAT31', 'ENGINEERING MATHEMATICS - III', enI, enE, str(enT), enP)
        pdf.add_tableForOne1('17CS32', ' ANALOG AND DIGITAL ELECTRONICS', anI, anE, str(anT), anP)
        pdf.add_tableForOne2('17CS33', 'DATA STRUCTURES AND APPLICATION', daI, daE, str(daT), daP)
        pdf.add_tableForOne3('17CS34', 'COMPUTER ORGANIZATION', coI, coE, str(coT), coP)
        pdf.add_tableForOne4('17CS35', 'UNIX AND SHELL PROGRAMMING', unI, unE, str(unT), unP)
        pdf.add_tableForOne5('17CS36', 'DISCRETE MATHEMATICAL STRUCTURES', diI, diE, str(diT), diP)
        pdf.add_tableForTwo('17CSL37', 'ANALOG AND DIGITAL ELECTRONICS LABORATORY', anlI, anlE, str(anlT), anlP)
        pdf.add_tableForOne6('17CSL38', 'DATA STRUCTURES LABORATORY', dalI, dalE, str(dalT), dalP)
        pdf.add_tableForOne7('17KKK39', 'KANNADA KALI', kaI, kaE, str(kaT), kaP)

        nameR = name.replace(" ", "")

        pdf.output(f'{nameR}{Sem}.pdf')

        pdf_e = Pdf_mc(name_m=name, pdf_m=nameR + Sem + '.pdf')
        pdf_e.save()
        # name = "Mohammad Hamza"
        # shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
        shutil.move(f'{nameR}{Sem}.pdf', f'media\{nameR}{Sem}.pdf')
        # os.replace(f'{name}.pdf', f"VTU_d/VTU/media/{name}.pdf")

        # filepath = f'{name}-sem3@.pdf'
        # return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
        # filepath = f'{dd[:-5]}.pdf'
        # filepath = f'{nameR}{Sem}.pdf'
        # if request.method == "POST":
        #     return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
        namesem = f'{nameR}{Sem}'
        return render(request, 'VTU/sem3.html', {'namesem': namesem})

    return render(request, 'VTU/sem3.html')


def marks5(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        usn = request.POST.get('usn', '')

        mgI = request.POST.get('mgI', '')
        mgE = request.POST.get('mgE', '')
        mgP = request.POST.get('mgP', '')
        mgT = int(mgI) + int(mgE)

        inI = request.POST.get('inI', '')
        inE = request.POST.get('inE', '')
        inP = request.POST.get('inP', '')
        inT = int(inI) + int(inE)

        coI = request.POST.get('coI', '')
        coE = request.POST.get('coE', '')
        coP = request.POST.get('coP', '')
        coT = int(coI) + int(coE)

        daI = request.POST.get('daI', '')
        daE = request.POST.get('daE', '')
        daP = request.POST.get('daP', '')
        daT = int(daI) + int(daE)

        dnI = request.POST.get('dnI', '')
        dnE = request.POST.get('dnE', '')
        dnP = request.POST.get('dnP', '')
        dnT = int(dnI) + int(dnE)

        auI = request.POST.get('auI', '')
        auE = request.POST.get('auE', '')
        auP = request.POST.get('auP', '')
        auT = int(auI) + int(auE)

        cmI = request.POST.get('cmI', '')
        cmE = request.POST.get('cmE', '')
        cmP = request.POST.get('cmP', '')
        cmT = int(cmI) + int(cmE)

        dbI = request.POST.get('dbI', '')
        dbE = request.POST.get('dbE', '')
        dbP = request.POST.get('dbP', '')
        dbT = int(dbI) + int(dbE)

        pdf5 = PDF5('P', 'mm', (229, 324))
        # print("Enter USN")
        # print("Enter name")
        # USN = '3AE17CS045'
        # Name = 'MOHAMMAD HAMZA'
        Sem = '5'
        pdf5.add_page()
        pdf5.add_watermark()
        pdf5.add_USN_Name(usn, name, Sem)
        pdf5.add_table_title()
        pdf5.add_tableForTwo('17CS51', 'MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY', mgI, mgE, str(mgT), mgP)
        pdf5.add_tableForOne('17CS552', 'INTRODUCTION TO SOFTWARE TESTING', inI, inE, str(inT), inP)
        pdf5.add_tableForOne1('17CS52', 'COMPUTER NETWORKS', coI, coE, str(coT), coP)
        pdf5.add_tableForOne2('17CS53', 'DATABASE MANAGEMENT SYSTEM', daI, daE, str(daT), daP)
        pdf5.add_tableForTwo2('17CS564', '.NET FRAMEWORK FOR APPLICATION DEVELOPMENT', dnI, dnE, str(dnT), dnP)
        pdf5.add_tableForOne3('17CS54', 'AUTOMATA THEORY AND COMPUTABILITY', auI, auE, str(auT), auP)
        pdf5.add_tableForOne4('17CSL57', 'COMPUTER NETWORK LABORATORY', cmI, cmE, str(cmT), cmP)
        pdf5.add_tableForOne5('17CSL58', 'DBMS LABORATORY WITH MINI PROJECT', dbI, dbE, str(dbT), dbP)

        nameR = name.replace(" ", "")

        pdf5.output(f'{nameR}{Sem}.pdf')

        pdf_e = Pdf_mc(name_m=name, pdf_m=nameR + Sem + '.pdf')
        pdf_e.save()

        shutil.move(f'{nameR}{Sem}.pdf', f'media\{nameR}{Sem}.pdf')

        namesem = f'{nameR}{Sem}'
        return render(request, 'VTU/sem3.html', {'namesem': namesem})

    return render(request, 'VTU/sem5.html')


def download(request, dd):
    filepath = f'media\{dd[:-5]}.pdf'
    print(filepath)
    if request.method == "POST":
        return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
    return render(request, 'VTU/download.html', {'dd': dd})


def calc(request):
    return render(request, 'VTU/calc.html')


def selectSem(request):
    return render(request, 'VTU/select_sem.html')
