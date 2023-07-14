from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import random
from infra.entities import aposta
from infra.entities.aposta import Aposta
from infra.repository.aposta_repository import ApostaRepository
from infra.configs.connection import DBConnectionHandler
import datetime

class Home(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 681)

        conn = DBConnectionHandler()

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navbar_Bet = QFrame(self.frame)
        self.navbar_Bet.setObjectName(u"navbar_Bet")
        self.navbar_Bet.setStyleSheet(u"image: url(:/images/bet365.png);")

        self.navbar_Bet.setFrameShape(QFrame.StyledPanel)
        self.navbar_Bet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.navbar_Bet)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 129, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.navbar_Bet)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txt_nome_apostador = QLineEdit(self.frame_5)
        self.txt_nome_apostador.setObjectName(u"txt_nome_apostador")
        self.txt_nome_apostador.setGeometry(QRect(133, 10, 133, 20))
        self.lbl_nome_apostador = QLabel(self.frame_5)
        self.lbl_nome_apostador.setObjectName(u"lbl_nome_apostador")
        self.lbl_nome_apostador.setGeometry(QRect(10, 10, 80, 16))
        self.lbl_vencedor = QLabel(self.frame_5)
        self.lbl_vencedor.setObjectName(u"lbl_vencedor")
        self.lbl_vencedor.setGeometry(QRect(10, 36, 58, 16))
        self.rb_visitante = QRadioButton(self.frame_5)
        self.rb_visitante.setObjectName(u"rb_visitante")
        self.rb_visitante.setGeometry(QRect(127, 36, 64, 17))
        self.rb_casa = QRadioButton(self.frame_5)
        self.rb_casa.setObjectName(u"rb_casa")
        self.rb_casa.setGeometry(QRect(74, 36, 47, 17))
        self.lbl_valor = QLabel(self.frame_5)
        self.lbl_valor.setObjectName(u"lbl_valor")
        self.lbl_valor.setGeometry(QRect(380, 10, 47, 13))
        self.txt_valor = QLineEdit(self.frame_5)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(470, 10, 113, 20))

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_placar = QLabel(self.frame_4)
        self.lbl_placar.setObjectName(u"lbl_placar")

        self.gridLayout_2.addWidget(self.lbl_placar, 0, 0, 1, 1)

        self.lbl_casa_aposta = QLabel(self.frame_4)
        self.lbl_casa_aposta.setObjectName(u"lbl_casa_aposta")

        self.gridLayout_2.addWidget(self.lbl_casa_aposta, 0, 1, 1, 1)

        self.txt_casa_aposta = QLineEdit(self.frame_4)
        self.txt_casa_aposta.setObjectName(u"txt_casa_aposta")

        self.gridLayout_2.addWidget(self.txt_casa_aposta, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.lbl_visitante_aposta = QLabel(self.frame_4)
        self.lbl_visitante_aposta.setObjectName(u"lbl_visitante_aposta")

        self.gridLayout_2.addWidget(self.lbl_visitante_aposta, 0, 4, 1, 1)

        self.txt_visitante_aposta = QLineEdit(self.frame_4)
        self.txt_visitante_aposta.setObjectName(u"txt_visitante_aposta")

        self.gridLayout_2.addWidget(self.txt_visitante_aposta, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.btn_add_aposta = QPushButton(self.frame_4)
        self.btn_add_aposta.setObjectName(u"btn_add_aposta")

        self.gridLayout_2.addWidget(self.btn_add_aposta, 0, 7, 1, 1)

        self.lbl_casa_resultado = QLabel(self.frame_4)
        self.lbl_casa_resultado.setObjectName(u"lbl_casa_resultado")

        self.gridLayout_2.addWidget(self.lbl_casa_resultado, 1, 1, 1, 1)

        self.txt_casa_resultado = QLineEdit(self.frame_4)
        self.txt_casa_resultado.setObjectName(u"txt_casa_resultado")

        self.gridLayout_2.addWidget(self.txt_casa_resultado, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.lbl_visitante_resultado = QLabel(self.frame_4)
        self.lbl_visitante_resultado.setObjectName(u"lbl_visitante_resultado")

        self.gridLayout_2.addWidget(self.lbl_visitante_resultado, 1, 4, 1, 1)

        self.txt_visitante_resultado = QLineEdit(self.frame_4)
        self.txt_visitante_resultado.setObjectName(u"txt_visitante_resultado")

        self.gridLayout_2.addWidget(self.txt_visitante_resultado, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.btn_gerar_resultado = QPushButton(self.frame_4)
        self.btn_gerar_resultado.setObjectName(u"btn_gerar_resultado")

        self.gridLayout_2.addWidget(self.btn_gerar_resultado, 1, 7, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_apostas = QTableWidget(self.frame_2)
        if (self.tb_apostas.columnCount() < 3):
            self.tb_apostas.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_apostas.setObjectName(u"tb_apostas")
        self.tb_apostas.horizontalHeader().setVisible(True)
        self.tb_apostas.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_apostas.horizontalHeader().setMinimumSectionSize(70)
        self.tb_apostas.horizontalHeader().setDefaultSectionSize(252)
        self.tb_apostas.horizontalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_2.addWidget(self.tb_apostas)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_add_aposta.clicked.connect(self.salvar_aposta)
        # self.popula_tabela_apostas()
        # self.popula_tabela_apostas("", "")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_nome_apostador.setText(QCoreApplication.translate("MainWindow", u"Nome Apostador", None))
        self.lbl_vencedor.setText(QCoreApplication.translate("MainWindow", u"Vencedor:   ", None))
        self.rb_visitante.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.rb_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.lbl_valor.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.lbl_placar.setText(QCoreApplication.translate("MainWindow", u"Placar ", None))
        self.lbl_casa_aposta.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.lbl_visitante_aposta.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.btn_add_aposta.setText(QCoreApplication.translate("MainWindow", u"Add Aposta", None))
        self.lbl_casa_resultado.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.lbl_visitante_resultado.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.btn_gerar_resultado.setText(QCoreApplication.translate("MainWindow", u"Gerar Resultado", None))
        ___qtablewidgetitem = self.tb_apostas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_apostas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tb_apostas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor Ganho", None));
    # retranslateUi

    def visulizar_aposta(self, row):
        dbAposta = ApostaRepository()
        pedido = dbAposta.select(self.tb_apostas.item(row, 0).text())


        self.window = QMainWindow()
        self.ui = Aposta()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.popula_visualizacao(Aposta)
        self.mainWindow.hide()

    def popula_tabela_apostas(self):
        self.tb_apostas.setRowCount(0)
        db = ApostaRepository()
        lista_aposta = db.select_all()
        self.tb_apostas.setRowCount(len(lista_aposta))

        for linha, pedido in enumerate(lista_aposta):
            valores_aposta = [aposta.nome_apostador, aposta.valor_aposta, aposta.valor_ganho]
            for coluna, valor in enumerate(valores_aposta):
                self.tb_apostas.setItem(linha, coluna, QTableWidgetItem(str(valor)))

    def salvar_aposta(self):
        dbAposta = ApostaRepository()


        if self.btn_add_aposta:
                aposta = Aposta(
                    nome_apostador=self.txt_nome_apostador.text(),
                    time_casa=self.txt_casa_aposta.text(),
                    time_visitante=self.txt_visitante_aposta.text(),
                    valor_aposta=self.txt_valor.text()
                )

                retornoPedido = dbAposta.insert(aposta)

    # def GerarResultado(self):
    #     def gerar_placar():
    #         gols_casa = random.randint(0, 5)
    #         gols_vistante = random.randint(0, 5)
    #
    #         placar = [
    #             {"time": "Time da casa", "gols": gols_casa},
    #             {"time": "Time Visitante", "gols": gols_vistante}
    #         ]
    #
    #         return placar
    #
    #     def exibir_placar(placar):
    #         print("Placar final:")
    #         for resultado in placar:
    #             print(f"{resultado['time']}: {resultado['gols']}")
    #
    #     def validar_vencedor(placar):
    #         if placar[0]['gols'] > placar[1]['gols']:
    #             return placar[0]['time']
    #         elif placar[1]['gols'] > placar[0]['gols']:
    #             return placar[1]['time']
    #         else:
    #             return "Empate"
    #
    #     placar = gerar_placar()
    #     exibir_placar(placar)
    #
    #     ganhador = validar_vencedor(placar)
    #     print(f"Vencedor: {ganhador} ganhou")
    #
    #
    #
    #
                    # self.home()