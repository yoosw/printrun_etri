import wx
import os

from printrun.utils import imagefile

def Motor_Control(root, parentpanel):

    # motor image
    root.bmp_motor_0 = wx.Bitmap(imagefile("flexor/motor_0.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_1 = wx.Bitmap(imagefile("flexor/motor_1.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_10 = wx.Bitmap(imagefile("flexor/motor_10.png"), wx.BITMAP_TYPE_PNG)

    root.bmp_motor_0_ch = wx.Bitmap(imagefile("flexor/motor_0_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_1_ch = wx.Bitmap(imagefile("flexor/motor_1_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_10_ch = wx.Bitmap(imagefile("flexor/motor_10_ch.png"), wx.BITMAP_TYPE_PNG)

    bmp_motor_x_arrow1 = wx.Bitmap(imagefile("flexor/motor_x_arrow1.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_x_arrow2 = wx.Bitmap(imagefile("flexor/motor_x_arrow2.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y_arrow1 = wx.Bitmap(imagefile("flexor/motor_y_arrow1.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y_arrow2 = wx.Bitmap(imagefile("flexor/motor_y_arrow2.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z_arrow1 = wx.Bitmap(imagefile("flexor/motor_z_arrow1.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z_arrow2 = wx.Bitmap(imagefile("flexor/motor_z_arrow2.png"), wx.BITMAP_TYPE_PNG)

    bmp_motor_x_box = wx.Bitmap(imagefile("flexor/motor_x_box.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y_box = wx.Bitmap(imagefile("flexor/motor_y_box.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z_box = wx.Bitmap(imagefile("flexor/motor_z_box.png"), wx.BITMAP_TYPE_PNG)
    bmp_zoffset = wx.Bitmap(imagefile("flexor/zoffset.png"), wx.BITMAP_TYPE_PNG)

    bmp_motor_x = wx.Bitmap(imagefile("flexor/motor_x.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y = wx.Bitmap(imagefile("flexor/motor_y.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z = wx.Bitmap(imagefile("flexor/motor_z.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_a = wx.Bitmap(imagefile("flexor/motor_a.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_off = wx.Bitmap(imagefile("flexor/motor_off.png"), wx.BITMAP_TYPE_PNG)

    # image connect
    root.text_motor_x_position = wx.StaticText(parentpanel, label=':0.0', pos=(540, 47))
    root.text_motor_x_position.SetFont(root.font_motor)
    root.text_motor_x_position.SetForegroundColour("#FF3300")

    root.text_motor_y_position = wx.StaticText(parentpanel, label=':0.0', pos=(540, 103))
    root.text_motor_y_position.SetFont(root.font_motor)
    root.text_motor_y_position.SetForegroundColour("#00CC00")

    root.text_motor_z_position = wx.StaticText(parentpanel, label=':0.0', pos=(540, 161))
    root.text_motor_z_position.SetFont(root.font_motor)
    root.text_motor_z_position.SetForegroundColour("#0000FF")

    imsi_zoffset = float(root.build_dimensions_list[5])
    root.text_zoffset = wx.StaticText(parentpanel, label=':' + str(imsi_zoffset), pos=(540, 210))
    root.text_zoffset.SetFont(root.font_base)
    root.text_zoffset.SetForegroundColour("#000000")

    # motor
    if os.name == "nt":
        dis_panel = root.bitmap2
    else:
        dis_panel = parentpanel

    root.btn_bmp_motor_0 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_0_ch, (399, 37), style=wx.NO_BORDER)
    root.btn_bmp_motor_0.Bind(wx.EVT_BUTTON, lambda e: root.move_set(0.1))
    root.btn_bmp_motor_1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_1, (399, 118), style=wx.NO_BORDER)
    root.btn_bmp_motor_1.Bind(wx.EVT_BUTTON, lambda e: root.move_set(1))
    root.btn_bmp_motor_10 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_10, (399, 196), style=wx.NO_BORDER)
    root.btn_bmp_motor_10.Bind(wx.EVT_BUTTON, lambda e: root.move_set(10))

    btn_bmp_motor_x_arrow1 = wx.BitmapButton(dis_panel, -1, bmp_motor_x_arrow1, (74, 100), style=wx.NO_BORDER)
    btn_bmp_motor_x_arrow1.SetBackgroundColour('#949494')
    btn_bmp_motor_x_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("x", 1, "unit"))

    btn_bmp_motor_x_arrow2 = wx.BitmapButton(dis_panel, -1, bmp_motor_x_arrow2, (172, 82), style=wx.NO_BORDER)
    btn_bmp_motor_x_arrow2.SetBackgroundColour('#949494')
    btn_bmp_motor_x_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("x", -1, "unit"))

    btn_bmp_motor_y_arrow1 = wx.BitmapButton(dis_panel, -1, bmp_motor_y_arrow1, (23, 192), style=wx.NO_BORDER)
    btn_bmp_motor_y_arrow1.SetBackgroundColour('#f2f2f3')
    btn_bmp_motor_y_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("y", -1, "unit"))

    btn_bmp_motor_y_arrow2 = wx.BitmapButton(dis_panel, -1, bmp_motor_y_arrow2, (98, 219), style=wx.NO_BORDER)
    btn_bmp_motor_y_arrow2.SetBackgroundColour('#f2f2f3')
    btn_bmp_motor_y_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("y", 1, "unit"))

    btn_bmp_motor_z_arrow1 = wx.BitmapButton(dis_panel, -1, bmp_motor_z_arrow1, (219, 264), style=wx.NO_BORDER)
    btn_bmp_motor_z_arrow1.SetBackgroundColour('#f2f2f3')
    btn_bmp_motor_z_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("z", 1, "unit"))

    btn_bmp_motor_z_arrow2 = wx.BitmapButton(dis_panel, -1, bmp_motor_z_arrow2, (218, 183), style=wx.NO_BORDER)
    btn_bmp_motor_z_arrow2.SetBackgroundColour('#f2f2f3')
    btn_bmp_motor_z_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_distance("z", -1, "unit"))

    btn_bmp_motor_x_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_x_box, (495, 40), style=wx.NO_BORDER)
    btn_bmp_motor_x_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("x"))
    btn_bmp_motor_y_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_y_box, (495, 96), style=wx.NO_BORDER)
    btn_bmp_motor_y_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("y"))
    btn_bmp_motor_z_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_z_box, (495, 153), style=wx.NO_BORDER)
    btn_bmp_motor_z_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("z"))
    btn_bmp_zoffset_cal = wx.BitmapButton(dis_panel, -1, bmp_zoffset, (460, 210), style=wx.NO_BORDER)
    btn_bmp_zoffset_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("zoffset"))

    btn_bmp_motor_x = wx.BitmapButton(dis_panel, -1, bmp_motor_x, (373, 289), style=wx.NO_BORDER)
    btn_bmp_motor_x.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("x"))
    btn_bmp_motor_y = wx.BitmapButton(dis_panel, -1, bmp_motor_y, (469, 289), style=wx.NO_BORDER)
    btn_bmp_motor_y.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("y"))
    btn_bmp_motor_z = wx.BitmapButton(dis_panel, -1, bmp_motor_z, (569, 289), style=wx.NO_BORDER)
    btn_bmp_motor_z.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("z"))
    btn_bmp_motor_a = wx.BitmapButton(dis_panel, -1, bmp_motor_a, (361, 395), style=wx.NO_BORDER)
    btn_bmp_motor_a.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("all"))
    btn_bmp_motor_off = wx.BitmapButton(dis_panel, -1, bmp_motor_off, (515, 395), style=wx.NO_BORDER)
    btn_bmp_motor_off.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("Motors off"))

    return
