import os
import pickle
import wx
from contoMac import ContoMac

# Percorso del file dove i conti vengono salvati
pickle_file = 'macchinetta.pkl'

# Caricamento della lista dei conti se esiste, altrimenti usa una lista vuota
if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as f:

        listaM = pickle.load(f)
else:
    listaM = []  # Se il file non esiste, inizializza con una lista vuota










class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Esempio wxPython", size=(300, 400))
        panel = wx.Panel(frame)

        vbox = wx.BoxSizer(wx.VERTICAL)

        label1 = wx.StaticText(panel, label="Inserisci il codice")
        vbox.Add(label1, flag=wx.ALL, border=10)

        self.text_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl, flag=wx.EXPAND | wx.ALL, border=10)




        self.button = wx.Button(panel, label="Invia")
        vbox.Add(self.button, flag=wx.ALL, border=10)

        self.label2 = wx.StaticText(panel, label="Aggiungi credito")
        vbox.Add(self.label2, flag=wx.ALL, border=10)
        self.label2.Hide()

        self.text_ctrl1 = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl1, flag=wx.EXPAND | wx.ALL, border=10)
        self.text_ctrl1.Hide()

        self.button.Bind(wx.EVT_BUTTON, self.Mostra)

        self.buttonAdd = wx.Button(panel, label="Aggiungi")
        vbox.Add(self.buttonAdd, flag=wx.ALL, border=10)
        self.buttonAdd.Hide()  # N
        self.buttonAdd.Bind(wx.EVT_BUTTON, self.Add)



        self.buttonCof = wx.Button(panel, label="Coffe")
        vbox.Add(self.buttonCof, flag=wx.ALL, border=10)
        self.buttonCof.Hide()  # N
        self.buttonCof.Bind(wx.EVT_BUTTON, self.ErogaCof)

        self.buttonThe = wx.Button(panel, label="The")
        vbox.Add(self.buttonThe, flag=wx.ALL, border=10)
        self.buttonThe.Hide()  # N
        self.buttonThe.Bind(wx.EVT_BUTTON, self.ErogaThe)

        self.buttonWat = wx.Button(panel, label="Acqua")
        vbox.Add(self.buttonWat, flag=wx.ALL, border=10)
        self.buttonWat.Hide()  # N
        self.buttonWat.Bind(wx.EVT_BUTTON, self.ErogaWat)






        '''
        button = wx.Button(panel, label="Coffe")
        vbox.Add(button, flag=wx.ALL, border=10)

        button.Bind(wx.EVT_BUTTON, self.ErogaCof)

        
        self.buttonThe.Hide()
        self.buttonWat.Hide()
        '''
        panel.SetSizer(vbox)
        frame.Show()
        return True

    def Mostra(self, event):

        conto = self.text_ctrl.GetValue()
        for i in listaM:
            if i.numConto == conto:


                # Ottiene il testo inserito dall'utente
                self.buttonCof.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.buttonCof.GetParent().Layout()  # Ricalcola il layout del pannello
                # Mostra un messaggio di dialogo con il testo inserito
                # Ottiene il testo inserito dall'utente
                self.buttonThe.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.buttonThe.GetParent().Layout()  # Ricalcola il layout del pannello
                # Mostra un messaggio di dialogo con il testo inserito
                self.buttonWat.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.buttonWat.GetParent().Layout()  # Ricalcola il layout del pannello
                # Mostra un messaggio di dialogo con il testo inserito
                # Mostra un messaggio di dialogo con il testo inserito
                self.buttonAdd.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.buttonAdd.GetParent().Layout()  # Ricalcola il layout del pannello

                self.label2.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.label2.GetParent().Layout()  # Ricalcola il layout del pannello
                # Mostra un messaggio di dialogo con il testo inserito
                # Mostra un messaggio di dialogo con il testo inserito
                self.text_ctrl1.Show()
                # Ricalcola il layout per evitare sovrapposizioni
                self.text_ctrl1.GetParent().Layout()  # Ricalcola il layout del pannello
                # Mostra un messaggio di dialogo con il testo inserito



    def ErogaCof(self, event):
        conto = self.text_ctrl.GetValue()
        for i in listaM:
            if i.numConto == conto:
                if i.credito >= 2:
                 i.credito -= 2
                 wx.MessageBox(f"Il saldo residuo è: {i.credito}", "Caffè in erogazione", wx.OK | wx.ICON_INFORMATION)
                 f = open("macchinetta.pkl", "wb")
                 pickle.dump(listaM, f)
                 f.close()
                else:
                    wx.MessageBox(f"Il saldo residuo è: {i.credito}", "Credito esaurito",
                                  wx.OK | wx.ICON_INFORMATION)

    def ErogaThe(self, event):
        conto = self.text_ctrl.GetValue()
        for i in listaM:
            if i.numConto == conto:
                if i.credito >= 3:
                 i.credito -= 3
                 wx.MessageBox(f"Il saldo residuo è: {i.credito}", "The in erogazione", wx.OK | wx.ICON_INFORMATION)
                 f = open("macchinetta.pkl", "wb")
                 pickle.dump(listaM, f)
                 f.close()
                else:
                    wx.MessageBox(f"Il saldo residuo è: {i.credito}", "Credito esaurito",
                                  wx.OK | wx.ICON_INFORMATION)

    def ErogaWat(self, event):
        conto = self.text_ctrl.GetValue()
        for i in listaM:
            if i.numConto == conto:
                if i.credito >= 1:
                    i.credito -= 1
                    wx.MessageBox(f"Il saldo residuo è: {i.credito}", "Acqua in erogazione", wx.OK | wx.ICON_INFORMATION)
                    f = open("macchinetta.pkl", "wb")
                    pickle.dump(listaM, f)
                    f.close()
                else:
                    wx.MessageBox(f"Il saldo residuo è: {i.credito}", "Credito esaurito",
                                  wx.OK | wx.ICON_INFORMATION)

    def Add(self, event):
        print("ciao")
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

