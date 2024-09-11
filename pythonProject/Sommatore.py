import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Sommatore", size=(800, 800))

        panel = wx.Panel(frame)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Inserisci un numero")

        self.label.SetFont(wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.label.SetForegroundColour("Green")

        vbox.Add(self.label, flag=wx.ALL, border=10)
        # secondo widget: campo di input
        self.text_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl, flag=wx.EXPAND | wx.ALL, border=10)
        self.text_ctrl.GetParent().Layout()  # Ricalcola il layout del pannello

        self.label1 = wx.StaticText(panel, label="Inserisci un numero")
        vbox.Add(self.label1, flag=wx.ALL, border=10)

        self.label1.SetFont(wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.label1.SetForegroundColour("Green")

        # secondo widget: campo di input
        self.text_ctrl1 = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl1, flag=wx.EXPAND | wx.ALL, border=10)
        self.text_ctrl1.GetParent().Layout()  # Ricalcola il layout del pannello

        # primo widget: bottone
        button = wx.Button(panel, label="Somma")
        vbox.Add(button, flag=wx.ALL, border=10)
        button.GetParent().Layout()  # Ricalcola il layout del pannello
        # associo al bottone un evento e la funzione saluti
        button.Bind(wx.EVT_BUTTON, self.somma)
        # Cambia il colore di sfondo del pannello
        panel.SetBackgroundColour(wx.Colour(100, 149, 237))  # Usa un colore RGB
        panel.SetSizer(vbox)
        frame.Show()
        return True
    def somma(self, event):
        num1 = int(self.text_ctrl1.GetValue())
        num2 = int(self.text_ctrl.GetValue())
        somma = num1 + num2
        wx.MessageBox(f"La somma dei due numeri è {somma}", "Somma", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()