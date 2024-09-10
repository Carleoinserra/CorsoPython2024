import wx


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Esempio wxPython", size=(300, 150))
        panel = wx.Panel(frame)

        vbox = wx.BoxSizer(wx.VERTICAL)

        label1 = wx.StaticText(panel, label="Questa è la prima etichetta")
        vbox.Add(label1, flag=wx.ALL, border=10)

        label2 = wx.StaticText(panel, label="Questa è la seconda etichetta")
        vbox.Add(label2, flag=wx.ALL, border=10)

        button = wx.Button(panel, label="Chiudi")
        vbox.Add(button, flag=wx.ALL, border=10)

        button.Bind(wx.EVT_BUTTON, self.OnClose)

        panel.SetSizer(vbox)
        frame.Show()
        return True

    def OnClose(self, event):
        self.GetTopWindow().Close(True)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

