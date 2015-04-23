#@PydevCodeAnalysisIgnore
from wx import *
import os


class media_player(wx.Frame):
    
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'SH Media Player', size=(500,400))      
#         self.init_gui()
        
    def __init__(self, *args, **kwargs):
        super(media_player,self).__init__(*args, **kwargs)
        self.init_gui()
        
    def init_gui(self):
        
#         panel = wx.Panel(self)
        # Create menu bar
        menubar = wx.MenuBar()
        menu_first = wx.Menu()
         
        menu_second = wx.Menu()
        menu_thirth = wx.Menu()
        menu_fourth = wx.Menu()
        menu_fifth = wx.Menu()
                 
        menu_open = menu_first.Append(wx.NewId(),"&Open\tCtrl+O", "This is a new window")
        self.Bind(wx.EVT_MENU, self.on_load_file, menu_open)
        
        menu_first.Append(wx.NewId(),'Open &URL\tCtrl+U',"This will open media online")
        menu_first.Append(wx.NewId(),"&Save as\tCtrl+S", "Save a new playlist")
        
        menu_close = menu_first.Append(wx.NewId(),"Close\tCtrl+Q","This will close windows")
        self.Bind(wx.EVT_MENU, self.close_button, menu_close)
        menu_first.AppendSeparator()
         
         
        menu_first_first = wx.Menu()
        menu_first_first.Append(wx.NewId(),"Music")
        menu_first_first.Append(wx.NewId(),"Videos")
        menu_first_first.Append(wx.NewId(),"Pictures")
        menu_first_first.Append(wx.NewId(),"Recorded TV")
        menu_first.AppendMenu(wx.NewId(),"Manage Libraries ", menu_first_first)
         
         
        menu_second.Append(wx.NewId(),"Library", "This is a new window")
        
        menu_second.Append(wx.NewId(),"Skin","This will open media online")
        menu_second.Append(wx.NewId(),"Now Playing", "Save a new playlist")
        menu_second.Append(wx.NewId(),"Skin Chooser","This will close windows")
         
        menu_thirth.Append(wx.NewId(),"Play/Pause", "This is a new window")
        menu_thirth.Append(wx.NewId(),"Stop","This will open media online")
        menu_thirth.Append(wx.NewId(),"Play Speed Playing", "Save a new playlist")
        menu_thirth.Append(wx.NewId(),"Skin Chooser","This will close windows")
         
        menu_fourth.Append(wx.NewId(),"Download", "This is a new window")
        menu_fourth.Append(wx.NewId(),"Apply media information changes","This will open media online")
        menu_fourth.Append(wx.NewId(),"Plug-ins", "Save a new playlist")
        menu_fourth.Append(wx.NewId(),"Option","This will close windows")
        menu_fourth.Append(wx.NewId(),"Advanced","This will close windows")
         
        menu_fifth.Append(wx.NewId(),"Media Player Help", "This is a new window")
        menu_fifth.Append(wx.NewId(),"Media Player Online","This will open media online")
        menu_fifth.Append(wx.NewId(),"Check Updates", "Save a new playlist")
        menu_fifth.Append(wx.NewId(),"Privacy Statement Online ","This will close windows")
        menu_fifth.Append(wx.NewId(),"About Media Player SH","This will close windows")
         
        menubar.Append(menu_first, "File")
        menubar.Append(menu_second, "View")
        menubar.Append(menu_thirth, "Play")
        menubar.Append(menu_fourth, "Tools")
        menubar.Append(menu_fifth, "Help")
        try:
            self.mc = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER,pos=(0,100), size=(550,200))
        except NotImplementedError:
            self.Destroy()
            raise
        # Create button
#         button = wx.Button(panel, label = "exit", pos=(130,10), size=(30,30))
#         self.Bind(wx.EVT_BUTTON, self.close_button, button)
#         self.Bind(wx.EVT_CLOSE, self.close_windows)
        
        # Create Media Player with wxPython
        
        # Button Get File from directory
        btn_load = wx.Button(self,-1,"Load File")
        self.Bind(wx.EVT_BUTTON, self.on_load_file, btn_load)
        
        # Button Play Video, music...
        btn_play = wx.Button(self, -1, "Play")
        self.Bind(wx.EVT_BUTTON, self.on_play, btn_play)
        
        # Button Pause
        btn_pause = wx.Button(self, -1, "Pause")
        self.Bind(wx.EVT_BUTTON, self.on_pause, btn_pause)
        
        # Button Stop
        btn_stop = wx.Button(self, -1, "Stop")
        self.Bind(wx.EVT_BUTTON, self.on_stop, btn_stop)
        
        slider = wx.Slider(self, -1, 0,0.0001,3000, pos=(120,680), style = wx.SL_HORIZONTAL | wx.SL_LABELS, size = (400, -1))
        self.slider = slider
        self.Bind(wx.EVT_SLIDER, self.on_seek, slider)
        
        self.st_file = wx.StaticText(self, -1, ".mid .mp3 .wav .au .avi .mpg", size=(200,-1))
        self.st_size = wx.StaticText(self, -1, size=(100,-1))
        self.st_len  = wx.StaticText(self, -1, size=(100,-1))
        self.st_pos  = wx.StaticText(self, -1, size=(100,-1))
        
        # setup the button/label layout using a sizer
        sizer = wx.GridBagSizer(5,5)
        sizer.Add(btn_load, (1,1))
        sizer.Add(btn_play, (2,1))
        sizer.Add(btn_pause, (3,1))
        sizer.Add(btn_stop, (4,1))
        
        sizer.Add(self.st_file, (1, 2))
        sizer.Add(self.st_size, (2, 2))
        sizer.Add(self.st_len,  (3, 2))
        sizer.Add(self.st_pos,  (4, 2))
        sizer.Add(self.mc, (5,1), span=(5,1))  # for .avi .mpg video files        
        self.SetSizer(sizer)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer)
        self.timer.Start(100)
        self.SetMenuBar(menubar)
        self.SetSize((550,450))
        self.SetTitle('SH Media Player')
        self.Center()
        self.Show(1)
        
    def on_seek(self, evt):
        offset = self.slider.GetValue()
        self.mc.Seek(offset)
        
    def on_timer(self, evt):
        offset = self.mc.Tell()
        self.slider.SetValue(offset)
        self.st_size.SetLabel('size: %s ms' % self.mc.Length())
        self.st_len.SetLabel('( %d seconds )' % (self.mc.Length()/1000))
        self.st_pos.SetLabel('position: %d ms' % offset)
        
    def on_load_file(self, evt):
        dlg = wx.FileDialog(self, message="Choose a media file",
                             defaultDir=os.getcwd(), defaultFile="",
                             style=wx.OPEN | wx.CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
             path = dlg.GetPath()
             self.do_load_file(path)
        dlg.Destroy()
        
    def do_load_file(self, path):
        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            folder, filename = os.path.split(path)
            self.st_file.SetLabel('%s' % filename)
            
            self.mc.SetBestFittingSize(wx.Size(450,450))
            self.GetSizer().Layout()
            self.slider.SetRange(0, self.mc.Length())
            self.mc.Play()
    
    def on_play(self, evt):
        self.mc.Play()
    
    def on_pause(self, evt):
        self.mc.Pause()
        
    def on_stop(self, evt):
        self.mc.Stop()
            
    def close_button(self, event):
        self.Close(True)
        
    def close_windows(self, event):
        self.Destroy()

def main():
        ex = wx.App()
        media_player(None)
        ex.MainLoop()
if __name__=='__main__':
    main()
#     app = wx.PySimpleApp()
#     frame = media_player(parent = None, id = 1)
#     frame.Show()
#     app.MainLoop()
