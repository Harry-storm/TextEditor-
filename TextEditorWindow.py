from TextEditor import Ui_TextEditor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QFontDialog, QColorDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, Qt, QTime, QDate
from PyQt5.QtGui import QFont, QColor, QKeySequence
from PyQt5.QtWidgets import QTextEdit, QShortcut
import time
import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#create user interface method action statement
class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# statement triggred
        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.Printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreveiw )
        self.actionExport_Pdf.triggered.connect(self.exportPdf)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.textbold)
        self.actionItalic.triggered.connect(self.italic)
        self.actionUndreline.triggered.connect(self.underLine)
        self.actionCenter.triggered.connect(self.alignCenter)
        self.actionLeft.triggered.connect(self.alignLeft)
        self.actionRight.triggered.connect(self.alignRight)
        self.actionJustify.triggered.connect(self.alignJustify)
        self.actionDate.triggered.connect(self.showDate)
        self.actionTime.triggered.connect(self.showTime)
        self.actionAbout.triggered.connect(self.clicked)
        self.actionHighlit.triggered.connect(self.highlight)
        self.actionSave_As.triggered.connect(self.fileSaveas)
        self.actionAbout_2.triggered.connect(self.about)
        #self.actionRemove.triggered.connect(self.Remove())
        self.shortcut_open=QShortcut(QKeySequence('ctrl+O'),self)
        self.shortcut_open.activated.connect(self.openFile)
        self.shortcut_save = QShortcut(QKeySequence('ctrl+s'), self)
        self.shortcut_save.activated.connect(self.fileSave)
        self.shortcut_New = QShortcut(QKeySequence('ctrl+n'), self)
        self.shortcut_New.activated.connect(self.fileNew)
        self.shortcut_print = QShortcut(QKeySequence('ctrl+p'), self)
        self.shortcut_print.activated.connect(self.Printfile)
        self.shortcut_priew = QShortcut(QKeySequence('ctrl+shift+p'), self)
        self.shortcut_priew.activated.connect(self.printPreveiw )
        self.shortcut_pdf = QShortcut(QKeySequence('ctrl+e'), self)
        self.shortcut_pdf.activated.connect(self.exportPdf)
        self.shortcut_exit = QShortcut(QKeySequence('ctrl+q'), self)
        self.shortcut_exit.activated.connect(self.exitApp)
        self.shortcut_copy = QShortcut(QKeySequence('ctrl+c'), self)
        self.shortcut_copy.activated.connect(self.copy)
        self.shortcut_cut = QShortcut(QKeySequence('ctrl+x'), self)
        self.shortcut_cut.activated.connect(self.cut)
        self.shortcut_paste = QShortcut(QKeySequence('ctrl+v'), self)
        self.shortcut_paste.activated.connect(self.paste)
        self.shortcut_undo= QShortcut(QKeySequence('ctrl+shift+u'), self)
        self.shortcut_undo.activated.connect(self.underLine)
        self.shortcut_redo = QShortcut(QKeySequence('ctrl+h'), self)
        self.shortcut_redo.activated.connect(self.highlight)
        self.shortcut_font = QShortcut(QKeySequence('ctrl+f'), self)
        self.shortcut_font.activated.connect(self.fontDialog)
        self.shortcut_color = QShortcut(QKeySequence('ctrl+t'), self)
        self.shortcut_color.activated.connect(self.colorDialog)
        self.shortcut_bold = QShortcut(QKeySequence('ctrl+b'), self)
        self.shortcut_bold.activated.connect(self.textbold)
        self.shortcut_italic = QShortcut(QKeySequence('ctrl+i'), self)
        self.shortcut_italic.activated.connect(self.italic)
        self.shortcut_left = QShortcut(QKeySequence('ctrl+l'), self)
        self.shortcut_left.activated.connect(self.alignLeft)
        self.shortcut_center = QShortcut(QKeySequence('ctrl+shift+c'), self)
        self.shortcut_center.activated.connect(self.alignCenter)
        self.shortcut_right= QShortcut(QKeySequence('ctrl+r'), self)
        self.shortcut_right.activated.connect(self.alignRight)
        self.shortcut_justif = QShortcut(QKeySequence('ctrl+j'), self)
        self.shortcut_justif.activated.connect(self.alignJustify)
        self.shortcut_time = QShortcut(QKeySequence('ctrl+shift+t'), self)
        self.shortcut_time.activated.connect(self.showTime)
        self.shortcut_date = QShortcut(QKeySequence('ctrl+d'), self)
        self.shortcut_date.activated.connect(self.showDate)
        self.shortcut_speek = QShortcut(QKeySequence('ctrl+shift+s'), self)
        self.shortcut_speek.activated.connect(self.clicked)
        self.shortcut_help = QShortcut(QKeySequence('shift+f1'), self)
        self.shortcut_help.activated.connect(self.about)
        self.shortcut_remove = QShortcut(QKeySequence('ctrl+g'), self)
        self.shortcut_remove.activated.connect(self.Remove)
        self.shortcut_zoom=QShortcut(QKeySequence('ctrl+ +'), self)
        self.shortcut_zoom.activated.connect(self.zoomo)

        self.show()


#Funtion creation

    def fileNew(self):
        self.textEdit.clear()


    def openFile(self):
        filename= QFileDialog.getOpenFileName(self, 'open File ','/home')

        if filename[0]:
            f=open(filename[0],'r')
            with f:
                data=f.read()
                self.textEdit.setText(data)




    def fileSave(self):
        filename=QFileDialog.getSaveFileName(self,'Save File')
        if filename[0]:
            f=open(filename[0], 'w')

            with f:
                text=self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self,'Svae File','File Saved Successfully')

    def fileSaveas(self):
        filename=QFileDialog.getSaveFileName(self,'Save File')
        if filename[0]:
            f=open(filename[0], 'w')

            with f:
                text=self.textEdit.toPlainText()
                f.write(text)


    def Printfile(self):
        printer=QPrinter(QPrinter.HighResolution)
        dialog=QPrintDialog(printer, self)

        if dialog.exec_() ==QPrintDialog.Accepted:
            self.textEdit.print_(printer)


    def printPreveiw(self):
        printer=QPrinter(QPrinter.HighResolution)
        previewDialog=QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()


    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def exportPdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF Files (.pdf) ;; All Files")
        if fn != "":
            if QFileInfo(fn).suffix() == "" :fn +='.pdf'
            printer=QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)



    def exitApp(self):
        self.close()

    def copy(self):
        cursor= self.textEdit.textCursor()
        textSelected= cursor.selectedText()
        self.copiedText = textSelected


    def paste(self):
        self.textEdit.append(self.copiedText)



    def cut(self):
        cursor=self.textEdit.textCursor()
        textSelected=cursor.selectedText()
        self.copiedText= textSelected
        self.textEdit.cut()


    def fontDialog(self):
        font, ok= QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)


    def colorDialog(self):

        font=QColorDialog.getColor()
        self.textEdit.setTextColor(font)


    def textbold(self):
        font=QFont()
        font.setBold(True)
        self.textEdit.setFont(font)


    def italic(self):
        font=QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)


    def underLine(self):
        font=QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def zoom(self):
        self.textEdit.zoomIn(100)

    def zoomo(self):
        self.textEdit.zoomOut(100)

    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)



    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)




    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)


    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)


    def showTime(self):
        time=QTime.currentTime()
        self.textEdit.setText(time.toString(Qt.DefaultLocaleLongDate))


    def showDate(self):
        date=QDate.currentDate()
        self.textEdit.setText(date.toString(Qt.DefaultLocaleLongDate))

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()


    def clicked(self):
        cursor = self.textEdit.textCursor()
        text= cursor.selectedText()
        self.speak(text)
        self.speak(time.sleep(5))


    def highlight(self):
         self.textEdit.setTextBackgroundColor(QColor(Qt.yellow).lighter(160))

    def Remove(self):
        self.textEdit.toPlainText()

    def about(self):
        QMessageBox.about(self,  "this is a advance notepad")





