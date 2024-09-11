import wx

class MyApp(wx.App):
    def OnInit(self):
        # Codice per inizializzare l'applicazione


        frame = wx.Frame(None, title="Esempio prima finestra", size=(800, 800))
        panel = wx.Panel(frame)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label2 = wx.StaticText(panel, label="Inserisci il tuo nome")
        vbox.Add(self.label2, flag=wx.ALL, border=10)

        # secondo widget: campo di input
        self.text_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl, flag=wx.EXPAND | wx.ALL, border=10)
        self.text_ctrl.GetParent().Layout()  # Ricalcola il layout del pannello

        # primo widget: bottone
        button = wx.Button(panel, label="Clikkami")
        vbox.Add(button, flag=wx.ALL, border=10)
        button.GetParent().Layout()  # Ricalcola il layout del pannello
        # associo al bottone un evento e la funzione saluti
        button.Bind(wx.EVT_BUTTON, self.saluti)
        panel.SetSizer(vbox)
        frame.Show()
        return True
    def saluti(self, event):
        nome = self.text_ctrl.GetValue()


        wx.MessageBox(f"Hello world da {nome}", "Saluti", wx.OK | wx.ICON_INFORMATION)



if __name__ == "__main__":
 app = MyApp()
 app.MainLoop()
