__author__ = 'yoo'

import wx

from .utils import make_autosize_button

# swyoo 2015.08.31 for image display in linux
from printrun.utils import imagefile

def HomeToolbar(root, parentpanel=None, use_wrapsizer=False):
    if not parentpanel: parentpanel = root.panel

    ToolbarSizer = wx.WrapSizer if use_wrapsizer and wx.VERSION > (2, 9) else wx.BoxSizer
    self = ToolbarSizer(wx.HORIZONTAL)

    # swyoo remove and open at original control
    if 0:
        root.rescanbtn = make_autosize_button(parentpanel, _("Port"), root.rescanports,
                                              _("Communication Settings\nClick to rescan ports"))
        self.Add(root.rescanbtn, 0, wx.TOP | wx.LEFT, 10)

        root.serialport = wx.ComboBox(parentpanel, -1, choices=root.scanserial(),
                                      style=wx.CB_DROPDOWN)
        root.serialport.SetToolTip(wx.ToolTip(_("Select Port Printer is connected to")))
        root.rescanports()
        self.Add(root.serialport, 0, wx.TOP | wx.LEFT, 10)
        root.baud = 115200

    root.dis_ch1 = make_autosize_button(parentpanel, _("View Ch"), root.display_ch, _("View size change"))
    self.Add(root.dis_ch1, 0, wx.TOP | wx.LEFT, 10)
    ########################################################################
    bmp_home_name = wx.Bitmap(imagefile("flexor/home_name.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_connect = wx.Bitmap(imagefile("flexor/home_connect.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_ready = wx.Bitmap(imagefile("flexor/home_ready.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_print = wx.Bitmap(imagefile("flexor/home_print.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_motor = wx.Bitmap(imagefile("flexor/home_motor.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_setting = wx.Bitmap(imagefile("flexor/home_setting.png"), wx.BITMAP_TYPE_ANY)

    wx.StaticBitmap(parentpanel, -1, bmp_home_name, (25, 355))
    # btn_bmp_home_connect = wx.BitmapButton( parentpanel, -1, bmp_home_connect, (48, 348), style=wx.NO_BORDER)
    # btn_bmp_home_connect.Bind(wx.EVT_BUTTON, root.connect)
    btn_bmp_home_ready = wx.BitmapButton(parentpanel, -1, bmp_home_ready, (25, 408), style=wx.NO_BORDER)
    btn_bmp_home_ready.Bind(wx.EVT_BUTTON, root.connect)
    btn_bmp_home_print = wx.BitmapButton(parentpanel, -1, bmp_home_print, (367, 117), style=wx.NO_BORDER)
    btn_bmp_home_print.Bind(wx.EVT_BUTTON, root.loadfile)
    btn_bmp_home_motor = wx.BitmapButton(parentpanel, -1, bmp_home_motor, (367, 286), style=wx.NO_BORDER)
    # btn_bmp_home_motor.Bind(wx.EVT_BUTTON, lambda e: onChangeSelection(parentpanel, 2))
    btn_bmp_home_motor.Bind(wx.EVT_BUTTON, lambda e: root.switch_tab(2))
    btn_bmp_home_setting = wx.BitmapButton(parentpanel, -1, bmp_home_setting, (508, 286), style=wx.NO_BORDER)
    # btn_bmp_home_setting.Bind(wx.EVT_BUTTON, lambda e: onChangeSelection(parentpanel, 3))
    btn_bmp_home_setting.Bind(wx.EVT_BUTTON, lambda e: root.switch_tab(3))
    ########################################################################

    return self
