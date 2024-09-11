import wx


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Esempio wxPython", size=(300, 400))
        panel = wx.Panel(frame)

        vbox = wx.BoxSizer(wx.VERTICAL)

        label1 = wx.StaticText(panel, label="Scrivi un numero")
        vbox.Add(label1, flag=wx.ALL, border=10)

        self.text_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text_ctrl, flag=wx.EXPAND | wx.ALL, border=10)

        label2 = wx.StaticText(panel, label="Scrivi un numero")
        vbox.Add(label2, flag=wx.ALL, border=10)

        self.text1_ctrl = wx.TextCtrl(panel)
        vbox.Add(self.text1_ctrl, flag=wx.EXPAND | wx.ALL, border=10)



        button = wx.Button(panel, label="Somma")
        vbox.Add(button, flag=wx.ALL, border=10)

        button.Bind(wx.EVT_BUTTON, self.Somma)

        panel.SetSizer(vbox)
        frame.Show()
        return True

    def Somma(self, event):
        # Ottiene il testo inserito dall'utente
        num1 = self.text_ctrl.GetValue()
        num2 = self.text1_ctrl.GetValue()

        somma = int(num1) + int(num2)

        # Mostra un messaggio di dialogo con il testo inserito
        wx.MessageBox(f"Las somma dei  nuemri è: {somma}", "Sommatore", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

