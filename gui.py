import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('TP DataScience')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #0f0f3d; color: white;")

        # * Central Widget
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        
        # * Main Layout
        mainLayout = QHBoxLayout()
        centralWidget.setLayout(mainLayout)
        
        # * Menu Bar
        menuBar = self.menuBar()
        menuBar.setStyleSheet("background-color: aliceblue; color: #0f0f3d; border: 2px solid #0f0f3d; font-family: 'Times New Roman', Times, serif;")
        fileMenu = menuBar.addMenu('FILE')
        
        exportedFile = QAction('Exporter', self)
        exportedFile.triggered.connect(self.exportImage)
        exportedFile.setObjectName("exportedFile")
        fileMenu.addAction(exportedFile)
        fileMenu.setStyleSheet("background-color: aliceblue; border: 2px solid #0f0f3d;")
        
        # * Left Side Layout
        leftLayout = QVBoxLayout()
        mainLayout.addLayout(leftLayout)
        
        # * Import Image Button
        self.importButton = QPushButton("Cliquer pour importer une image")
        self.importButton.setIcon(QIcon('add_icon.png'))
        self.importButton.setIconSize(QSize(50, 50))
        self.importButton.setObjectName("importButton")
        self.importButton.clicked.connect(self.importImage)
        
        leftLayout.addWidget(self.importButton)
        self.importButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # * Right Side Layout
        rightLayout = QVBoxLayout()
        mainLayout.addLayout(rightLayout)
        rightLayout.setObjectName("rightLayout")
        
        # * Image Processing Layout
        processingLayout = QVBoxLayout()
        # Add these lines in the `initUI` method after creating the `processingLayout`

        # Zoom Buttons
        zoomInButton = QPushButton("Zoom In")
        zoomInButton.setObjectName("zoomInButton")
        zoomInButton.clicked.connect(self.zoomIn)

        zoomOutButton = QPushButton("Zoom Out")
        zoomOutButton.setObjectName("zoomOutButton")
        zoomOutButton.clicked.connect(self.zoomOut)
        
        processingGroup = QWidget()
        processingGroup.setLayout(processingLayout)
        processingGroup.setObjectName("processingGroup")
        
        self.processingLabel = QLabel("TRAITEMENT DE L'IMAGE")
        self.processingLabel.setAlignment(Qt.AlignCenter)
        self.processingLabel.setFont(QFont('Times New Roman', 10, QFont.Bold))
        self.processingLabel.setObjectName("processingLabel")
        
        self.processingCombo = QComboBox()
        self.processingCombo.addItems(["Selection du traitement", "Traitement 1", "Traitement 2", "Traitement 3"])
        self.processingCombo.setObjectName("processingCombo")
        
        buttonsLayout = QHBoxLayout()
        self.rejectButton = QPushButton("Rejeter")
        self.rejectButton.setObjectName("rejectButton")
        self.rejectButton.clicked.connect(self.rejectAction)
        
        self.applyButton = QPushButton("Appliquer")
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.applyAction)
        
        buttonsLayout.addWidget(self.rejectButton)
        buttonsLayout.addWidget(self.applyButton)
        
        processingLayout.addWidget(self.processingLabel)
        # Add zoom buttons to the processing layout
        processingLayout.addWidget(zoomInButton)
        processingLayout.addWidget(zoomOutButton)
        processingLayout.addWidget(self.processingCombo)
        processingLayout.addLayout(buttonsLayout)
        
        # * Image Recognition Layout
        recognitionLayout = QVBoxLayout()
        recognitionGroup = QWidget()
        recognitionGroup.setLayout(recognitionLayout)
        recognitionGroup.setObjectName("recognitionLayout")
        
        self.recognitionLabel = QLabel("DESCRIPTION DE L'IMAGE")
        self.recognitionLabel.setAlignment(Qt.AlignCenter)
        self.recognitionLabel.setFont(QFont('Times New Roman', 10, QFont.Bold))
        self.recognitionLabel.setObjectName("recognitionLabel")
        
        self.textLabel = QLabel("Text")
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        
        recognitionLayout.addWidget(self.recognitionLabel)
        recognitionLayout.addWidget(self.textLabel)
        
        # * Add Groups to Right Layout
        rightLayout.addWidget(processingGroup)
        rightLayout.addWidget(recognitionGroup)
        
        self.show()
    
        self.traitementMapping = {
            "Traitement 1": self.traitement_1,
            "Traitement 2": self.traitement_2,
            "Traitement 3": self.traitement_3
        }

        # * Load the CSS file
        self.loadStylesheet("styles.css")
        
    def setButtonImage(self, fileName):
        # * Supprimer le texte du bouton
        self.importButton.setText('')  
        pixmap = QPixmap(fileName)
        # scaledPixmap = pixmap.scaled(self.importButton.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        scaledPixmap = pixmap.scaled(self.importButton.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.importButton.setIcon(QIcon(scaledPixmap))
        self.importButton.setIconSize(self.importButton.size())
        # * Supprimer la bordure pour un remplissage complet
        self.importButton.setStyleSheet("border: none;")

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())
            
    def zoomIn(self):
        currentIconSize = self.importButton.iconSize()
        newSize = QSize(int(currentIconSize.width() * 1.2), int(currentIconSize.height() * 1.2))
        self.importButton.setIconSize(newSize)

    def zoomOut(self):
        currentIconSize = self.importButton.iconSize()
        newSize = QSize(int(currentIconSize.width() * 0.8), int(currentIconSize.height() * 0.8))
        self.importButton.setIconSize(newSize)

    def applyAction(self):
        traitement = self.processingCombo.currentText()
        if traitement in self.traitementMapping:
            self.traitementMapping[traitement]()
        else:
            print("Veuillez sélectionner un traitement valide.")

    def rejectAction(self):
        # TODO more here
        print("Traitement rejeté.")

    def traitement_1(self):
        # TODO more here
        print("Traitement 1 appliqué.")

    def traitement_2(self):
        # TODO more here
        print("Traitement 2 appliqué.")

    def traitement_3(self):
        # TODO more here
        print("Traitement 3 appliqué.")
        
    def exportImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Exporter l'image", "", "Images (*.png *.xpm *.jpg)", options=options)
        if fileName:
            # TODO code for image exporting
            pass
    
    def importImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Image Files (*.png;*.jpg;*.jpeg)", options=options)
        if fileName:
            self.setButtonImage(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())