import wx
import os

from printrun.utils import imagefile

def Print_Control(root, parentpanel):

    if os.name == "nt":
        root.text_loading_file = wx.StaticText(parentpanel, label=str(root.var_loading_file_name), pos=(75, 33))
    else:
        root.text_loading_file = wx.StaticText(parentpanel, label=str(root.var_loading_file_name), pos=(75, 35))
    root.text_loading_file.SetFont(root.font_base)
    root.text_loading_file.SetBackgroundColour(wx.WHITE)
    #======================= gauge start
    root.timer = wx.Timer(parentpanel, 1)
    root.count = 0
    root.gauge = wx.Gauge(parentpanel, range=99, pos=(56, 106), size=(470, 26))

    root.Bind(wx.EVT_TIMER, root.TimerHandler)
    root.timer = wx.Timer(root)
    root.timer.Start(100)

    # gauge count
    root.text_gauge = wx.StaticText(parentpanel, label=str(root.var_loading_count) + "%", pos=(550, 102))
    root.text_gauge.SetFont(root.font_gauge)
    #======================= guage end
    # past time
    bmp_print_home = wx.Bitmap(imagefile("flexor/print_time.png"), wx.BITMAP_TYPE_ANY)
    wx.StaticBitmap(parentpanel, -1, bmp_print_home, (405, 162))

    root.text_print_time = wx.StaticText(parentpanel, label='00:00:00', pos=(510, 158))
    root.text_print_time.SetFont(root.font_base)

    # nozle, start
    bmp_print_list = wx.Bitmap(imagefile("flexor/print_list.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_nozzle_temp1 = wx.Bitmap(imagefile("flexor/print_nozzle_temp1.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_nozzle_temp2 = wx.Bitmap(imagefile("flexor/print_nozzle_temp2.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_output_speed = wx.Bitmap(imagefile("flexor/print_output_speed.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_fan_speed = wx.Bitmap(imagefile("flexor/print_fan_speed.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_start = wx.Bitmap(imagefile("flexor/print_start.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_stop = wx.Bitmap(imagefile("flexor/print_stop.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_pause = wx.Bitmap(imagefile("flexor/print_pause.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_resume = wx.Bitmap(imagefile("flexor/print_resume.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_filament_ch = wx.Bitmap(imagefile("flexor/print_filamentch.png"), wx.BITMAP_TYPE_PNG)
    bmp_print_emergency = wx.Bitmap(imagefile("flexor/print_emergency.png"), wx.BITMAP_TYPE_PNG)

    # nozzle1
    wx.StaticBitmap(parentpanel, -1, bmp_print_nozzle_temp1, (34, 233))
    root.text_print_nozzle_temp1_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(111, 247))
    root.text_print_nozzle_temp1_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(111, 281))
    root.text_print_nozzle_temp1_set.SetFont(root.font_base)
    root.text_print_nozzle_temp1_on.SetFont(root.font_base)
    root.text_print_nozzle_temp1_set.SetForegroundColour("#3399FF") # set text color
    root.text_print_nozzle_temp1_on.SetForegroundColour("#FF3300")

    # nozzle2
    wx.StaticBitmap(parentpanel, -1, bmp_print_nozzle_temp2, (230, 233))
    root.text_print_nozzle_temp2_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(305, 247))
    root.text_print_nozzle_temp2_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(305, 281))
    root.text_print_nozzle_temp2_set.SetFont(root.font_base)
    root.text_print_nozzle_temp2_on.SetFont(root.font_base)
    root.text_print_nozzle_temp2_set.SetForegroundColour("#3399FF") # set text color
    root.text_print_nozzle_temp2_on.SetForegroundColour("#FF3300")

    # print_speed, pan speed
    wx.StaticBitmap(parentpanel, -1, bmp_print_output_speed, (26, 370))
    wx.StaticBitmap(parentpanel, -1, bmp_print_fan_speed, (223, 358))

    # swyoo 2015.09.15 for combobox select
    #======================= combobox start
    root.speed_values = ['50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150']
    select_speed_val = ['50%', '60%', '70%', '80%', '90%', '100%', '110%', '120%', '130%', '140%', '150%']

    root.pan_values = ['0', '25', '51', '76', '102', '127', '153', '178', '204', '229', '255']
    select_pan_val = ['OFF', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']

    if os.name == "nt":
        root.speed_combo = wx.ComboBox(root.bitmap1, -1, value="100%", pos=(123, 380), size=(80, -1), choices=select_speed_val, style=wx.CB_READONLY)
    else:
        root.speed_combo = wx.ComboBox(parentpanel, -1, value="100%", pos=(123, 380), size=(80, 40), choices=select_speed_val, style=wx.CB_READONLY)
    root.Bind(wx.EVT_COMBOBOX, root.On_Speed_Select, id = root.speed_combo.GetId())

    root.speed_combo.SetFont(root.font_combo)

    if os.name == "nt":
        root.pan_combo = wx.ComboBox(root.bitmap1, -1, value="100%", pos=(310, 380), size=(80, -1), choices=select_pan_val, style=wx.CB_READONLY)
    else:
        root.pan_combo = wx.ComboBox(parentpanel, -1, value="100%", pos=(310, 380), size=(80, 40), choices=select_pan_val, style=wx.CB_READONLY)
    root.Bind(wx.EVT_COMBOBOX, root.On_Pan_Select, id = root.pan_combo.GetId())
    root.pan_combo.SetFont(root.font_combo)
    #======================= combobox end

    # start, pause, stop
    if os.name == "nt":
        dis_panel = root.bitmap1
    else:
        dis_panel = parentpanel

    if os.name == "nt":
        root.btn_bmp_print_list = wx.BitmapButton(dis_panel, -1, bmp_print_list, (34, 34), style=wx.NO_BORDER)
    else:
        root.btn_bmp_print_list = wx.BitmapButton(dis_panel, -1, bmp_print_list, (30, 30), style=wx.NO_BORDER)
    root.btn_bmp_print_list.Bind(wx.EVT_BUTTON, root.loadfile)
    root.btn_bmp_print_start = wx.BitmapButton(dis_panel, -1, root.bmp_print_start, (425, 234), style=wx.NO_BORDER)
    root.btn_bmp_print_start.Bind(wx.EVT_BUTTON, root.printfile)
    btn_bmp_print_stop = wx.BitmapButton(dis_panel, -1, bmp_print_stop, (563, 234), style=wx.NO_BORDER)
    btn_bmp_print_stop.Bind(wx.EVT_BUTTON, root.off)

    btn_bmp_print_filament_ch = wx.BitmapButton(dis_panel, -1, bmp_print_filament_ch, (428, 351), style=wx.NO_BORDER)
    btn_bmp_print_filament_ch.Bind(wx.EVT_BUTTON, root.On_Filament_Change)
    btn_bmp_print_emergency = wx.BitmapButton(dis_panel, -1, bmp_print_emergency, (561, 351), style=wx.NO_BORDER)
    btn_bmp_print_emergency.Bind(wx.EVT_BUTTON, root.reset)
    return
