import wx

import os
from .widgets import TempGauge

from printrun.utils import imagefile

def Setting_Control(root, parentpanel):

    mainsizer = wx.BoxSizer(wx.VERTICAL)

    panel_1 = root.newPanel(parentpanel)
    panel_1.SetBackgroundColour('#E6E7E7')
    panel_2 = root.newPanel(parentpanel)
    panel_2.SetBackgroundColour('#E6E7E7')

    image_file = 'flexor/setting_bg.png'
    bmp3 = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    background_image = wx.StaticBitmap(panel_1, -1, bmp3, (0, 0))

    mainsizer.Add(panel_1, 0, wx.EXPAND)
    mainsizer.Add(panel_2, 0, wx.EXPAND)
    # =============
    bmp_setting_setting = wx.Bitmap(imagefile("flexor/setting_setting.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_prepare = wx.Bitmap(imagefile("flexor/setting_prepare.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_nozzle1 = wx.Bitmap(imagefile("flexor/setting_nozzle1.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_nozzle2 = wx.Bitmap(imagefile("flexor/setting_nozzle2.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_filament1 = wx.Bitmap(imagefile("flexor/setting_filament1.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_filament2 = wx.Bitmap(imagefile("flexor/setting_filament2.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_nozzle_down = wx.Bitmap(imagefile("flexor/setting_nozzle_down.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_nozzle_up = wx.Bitmap(imagefile("flexor/setting_nozzle_up.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_filament_in = wx.Bitmap(imagefile("flexor/setting_filament_in.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_filament_out = wx.Bitmap(imagefile("flexor/setting_filament_out.png"), wx.BITMAP_TYPE_PNG)

    # bmp_setting_nozzle_text = wx.Bitmap(imagefile("flexor/setting_nozzle_text.png"), wx.BITMAP_TYPE_ANY)
    bmp_nozzle1 = wx.Bitmap(imagefile("flexor/nozzle1.png"), wx.BITMAP_TYPE_PNG)
    bmp_nozzle2 = wx.Bitmap(imagefile("flexor/nozzle2.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_on = wx.Bitmap(imagefile("flexor/setting_on.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_off = wx.Bitmap(imagefile("flexor/setting_off.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_ice = wx.Bitmap(imagefile("flexor/setting_ice.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_fire = wx.Bitmap(imagefile("flexor/setting_fire.png"), wx.BITMAP_TYPE_PNG)

    # image connect
    wx.StaticBitmap(panel_1, -1, bmp_setting_setting, (23, 21))
    wx.StaticBitmap(panel_1, -1, bmp_setting_prepare, (23, 298))


    root.text_temp_1 = wx.StaticText(panel_1, label=(str(root.var_temp_1_value) + u"\u00B0C"), pos=(176, 98))
    root.text_temp_1.SetFont(root.font_16)
    root.text_temp_1.SetBackgroundColour(wx.WHITE)
    root.text_temp_2 = wx.StaticText(panel_1, label=(str(root.var_temp_2_value) + u"\u00B0C"), pos=(504, 98))
    root.text_temp_2.SetFont(root.font_16)
    root.text_temp_2.SetBackgroundColour(wx.WHITE)

    wx.StaticBitmap(panel_1, -1, bmp_setting_nozzle1, (33, 67))
    wx.StaticBitmap(panel_1, -1, bmp_setting_nozzle2, (367, 67))
    wx.StaticBitmap(panel_1, -1, bmp_setting_filament1, (21, 178))
    wx.StaticBitmap(panel_1, -1, bmp_setting_filament2, (356, 178))

    wx.StaticBitmap(panel_1, -1, bmp_nozzle1, (28, 362))
    wx.StaticBitmap(panel_2, -1, bmp_nozzle2, (28, 20))

    wx.StaticBitmap(panel_1, -1, bmp_setting_ice, (175, 326))
    wx.StaticBitmap(panel_1, -1, bmp_setting_fire, (545, 326))

    if os.name == "nt":
        dis_panel = background_image
    else:
        dis_panel = panel_1

    btn_bmp_setting_nozzle_down1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_down, (110, 80), style=wx.NO_BORDER)
    btn_bmp_setting_nozzle_down1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "down"))
    btn_bmp_setting_nozzle_up1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_up, (249, 80), style=wx.NO_BORDER)
    btn_bmp_setting_nozzle_up1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "up"))
    btn_bmp_setting_nozzle_down2 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_down, (440, 80), style=wx.NO_BORDER)
    btn_bmp_setting_nozzle_down2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "down"))
    btn_bmp_setting_nozzle_up2 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_up, (579, 80), style=wx.NO_BORDER)
    btn_bmp_setting_nozzle_up2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "up"))

    btn_bmp_setting_filament_in1 = wx.BitmapButton(dis_panel, -1, bmp_setting_filament_in, (110, 190), style=wx.NO_BORDER)
    btn_bmp_setting_filament_in1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude1"))
    btn_bmp_setting_filament_out1 = wx.BitmapButton(dis_panel, -1, bmp_setting_filament_out, (248, 190), style=wx.NO_BORDER)
    btn_bmp_setting_filament_out1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse1"))
    btn_bmp_setting_filament_in2 = wx.BitmapButton(dis_panel, -1, bmp_setting_filament_in, (440, 190), style=wx.NO_BORDER)
    btn_bmp_setting_filament_in2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude2"))
    btn_bmp_setting_filament_out2 = wx.BitmapButton(dis_panel, -1, bmp_setting_filament_out, (577, 190), style=wx.NO_BORDER)
    btn_bmp_setting_filament_out2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse2"))

    if os.name == "nt":
        btn_bmp_setting_on1 = wx.BitmapButton(dis_panel, -1, bmp_setting_on, (78, 343), style=wx.NO_BORDER)
        btn_bmp_setting_on1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "on"))
        btn_bmp_setting_off1 = wx.BitmapButton(dis_panel, -1, bmp_setting_off, (584, 343), style=wx.NO_BORDER)
        btn_bmp_setting_off1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "off"))
    else:
        btn_bmp_setting_on1 = wx.BitmapButton(dis_panel, -1, bmp_setting_on, (78, 343), style=wx.NO_BORDER)
        btn_bmp_setting_on1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "on"))
        btn_bmp_setting_off1 = wx.BitmapButton(dis_panel, -1, bmp_setting_off, (584, 343), style=wx.NO_BORDER)
        btn_bmp_setting_off1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "off"))

    btn_bmp_setting_on2 = wx.BitmapButton(panel_2, -1, bmp_setting_on, (78, 0), style=wx.NO_BORDER)
    btn_bmp_setting_on2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "on"))
    btn_bmp_setting_off2 = wx.BitmapButton(panel_2, -1, bmp_setting_off, (584, 0), style=wx.NO_BORDER)
    btn_bmp_setting_off2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "off"))

    temp1_sizer = wx.BoxSizer(wx.HORIZONTAL)
    temp2_sizer = wx.BoxSizer(wx.HORIZONTAL)

    root.hottgauge = TempGauge(panel_1, size = (420, 32), title = _("Heater1:"), maxval = 300, bgcolor = '#E6E7E7')
    root.hottgauge2 = TempGauge(panel_2, size = (420, 32), title = _("Heater2:"), maxval = 300, bgcolor = '#E6E7E7')

    text_left = wx.StaticText(panel_1, label='')
    text_right = wx.StaticText(panel_1, label='')
    text_left2 = wx.StaticText(panel_2, label='')
    text_right2 = wx.StaticText(panel_2, label='')

    temp1_sizer.Add(text_left, 0, flag=wx.LEFT, border=160)
    temp1_sizer.Add(root.hottgauge, 0, flag=wx.TOP, border=356)
    temp1_sizer.Add(text_right, 0, flag=wx.TOP, border=382)

    temp2_sizer.Add(text_left2, 0, flag=wx.LEFT, border=160)
    temp2_sizer.Add(root.hottgauge2, 0, flag=wx.TOP, border=13)
    # temp2_sizer.Add(text_right2, 0, flag=wx.LEFT, border=0)
    temp2_sizer.Add(text_right2, 0, flag=wx.TOP, border=50)

    panel_1.SetSizer(temp1_sizer)
    panel_2.SetSizer(temp2_sizer)

    parentpanel.SetSizer(mainsizer)

    return

def Setting_Temp_Gauge_One(root, parentpanel):
    # Temperature gauges #
    temp1_sizer = wx.BoxSizer(wx.HORIZONTAL)

    root.hottgauge = TempGauge(parentpanel, size = (-1, 30), title = _("Heater1:"), maxval = 300, bgcolor = '#E6E7E7')

    text_left = wx.StaticText(parentpanel, label=' ')
    text_right = wx.StaticText(parentpanel, label=' ')

    temp1_sizer.Add(text_left, 0,  flag=wx.LEFT, border=200)
    temp1_sizer.Add(root.hottgauge, 1,  flag=wx.TOP, border=328)
    temp1_sizer.Add(text_right, 0,  flag=wx.LEFT, border=120)

    parentpanel.SetSizer(temp1_sizer)

    return

