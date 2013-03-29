# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import v4l2
import fcntl
import pygame.camera
import SimpleCV

###########################################################################
## Class MainFrame
###########################################################################
search = dict()
img = wx.EmptyImage(640,480)
class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SimpleShow", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
        
        
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()
        pygame.quit()
        
        ChooseCameraChoices = list()
        i=0
        for item in camlist:
            vd = open(item, 'r')
            cp = v4l2.v4l2_capability()
            fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)
            search[cp.card] = int(item[len(item)-1])
            ChooseCameraChoices.append(cp.card)
            i=i+1
            
        self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
        
        BSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.ChooseCamera = wx.ComboBox( self, wx.ID_ANY, u"Select Camera", wx.DefaultPosition, wx.DefaultSize, ChooseCameraChoices, wx.CB_READONLY)
        BSizer.Add( self.ChooseCamera, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        BSizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.PictureShow = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PictureShow.SetMinSize( wx.Size( 640,480 ) )
        
        BSizer.Add( self.PictureShow, 0, wx.ALL, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        BSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        
        ApplyFeatureChoices = [ u"c", u"d" ]
        self.ApplyFeature = wx.ComboBox( self, wx.ID_ANY, u"Select Feature", wx.Point( -1,-1 ), wx.DefaultSize, ApplyFeatureChoices, 0 )
        BSizer.Add( self.ApplyFeature, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        BSizer.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
        
        GridSizer = wx.GridSizer( 0, 2, 0, 0 )
        
        self.saveButton = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        GridSizer.Add( self.saveButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.SelectDirectory = wx.DirPickerCtrl( self, wx.ID_ANY, u"/home/sushilthe", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        GridSizer.Add( self.SelectDirectory, 0, wx.ALL, 5 )
        
        
        BSizer.Add( GridSizer, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( BSizer )
        self.Layout()
        BSizer.Fit( self )
        self.FileMenuBar = wx.MenuBar( 0 )
        self.FileMenu = wx.Menu()
        self.AboutMenu = wx.MenuItem( self.FileMenu, wx.ID_ABOUT, u"About", u"About this app", wx.ITEM_NORMAL )
        self.FileMenu.AppendItem( self.AboutMenu )
        
        self.FileMenu.AppendSeparator()
        
        self.ExitMenu = wx.MenuItem( self.FileMenu, wx.ID_EXIT, u"Exit", u"Exit this app", wx.ITEM_NORMAL )
        self.FileMenu.AppendItem( self.ExitMenu )
        
        self.FileMenuBar.Append( self.FileMenu, u"File" ) 
        
        self.SetMenuBar( self.FileMenuBar )
        
        
        self.Centre( wx.BOTH )
    
        # Connect Events
        self.Bind(wx.EVT_MENU, self.OnAbout, self.AboutMenu)
        self.Bind(wx.EVT_MENU, self.OnExit, self.ExitMenu)
        self.ChooseCamera.Bind( wx.EVT_COMBOBOX, self.capture )
        
    def __del__( self ):
        self.Destroy()
    
    # event handlers
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "Developed by: Sushil Dahal \n\nContact:"+
        "\nE-mail: sushilthe@gmail.com\nFollow me on Twitter: www.twitter.com/sushilthe", "SimpleShow", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)
        
    def capture( self, event ):
        device = search[self.ChooseCamera.GetValue()]
        cam = SimpleCV.Camera(device)
        while True:
            img = cam.getImage().show()
            
class SimpleShow(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__":
    app = SimpleShow()
    app.MainLoop()
    
    