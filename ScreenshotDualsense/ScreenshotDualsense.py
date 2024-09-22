import pygame
from datetime import datetime
import time
import sys
import win32gui
import win32ui
import win32con

# ScreenshotDualsense v0.1


def main():
    pygame.init()
    # Create a flag to understand if the controller is connected
    controller_connected = True

    # Check for a connected gamepad
    def checkGamepad():
        try:
            joystick = pygame.joystick.Joystick(0)
            time.sleep(1)
            pygame.joystick.init()
            joystick.init()
            print('DualSense connected')

        except:
            print("Checking...")
            time.sleep(5)
            checkGamepad()

    checkGamepad()
    joystick = pygame.joystick.Joystick(0)

    while True:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if the controller is connected
        if not pygame.joystick.get_count():
            if controller_connected:
                print("DualSense disabled")
                controller_connected = False
                main()
            continue
        else:
            if not controller_connected:
                print("DualSense connected!")
                controller_connected = True

        # Customizing the Screenshot Button
        if controller_connected:
            if joystick.get_button(4): # 4 = Share | 5 = PS | 6 = Option | 7 = L3 | 8 = R3 | 9 = L2 | 10 = R2 | 15 = Touch surface | 16 = micro

                # Clicking on the gamepad
                print("screen")
                now = datetime.now() 
                start = now.strftime("%S") 

                # Get a device context (DC) handle for the entire screen
                hdesktop = win32gui.GetDesktopWindow()
                desktop_dc = win32gui.GetWindowDC(hdesktop)
                dc = win32ui.CreateDCFromHandle(desktop_dc)

                # Get screen dimensions
                width = dc.GetDeviceCaps(win32con.HORZRES)
                height = dc.GetDeviceCaps(win32con.VERTRES)

                # Create a bitmap to save the image
                bitmap = win32ui.CreateBitmap()
                bitmap.CreateCompatibleBitmap(dc, width, height)
                dc_with_bitmap = dc.CreateCompatibleDC()

                # Copy the image to the bitmap
                dc_with_bitmap.SelectObject(bitmap)
                dc_with_bitmap.BitBlt((0, 0), (width, height), dc, (0, 0), win32con.SRCCOPY)


                # Save image to file
                current_time = now.strftime("%Y%B%d %H-%M-%S-%f")
                bitmap.SaveBitmapFile(dc_with_bitmap, f"ScreenShots/{current_time}.png")

                # Free up resources
                dc.DeleteDC()
                dc_with_bitmap.DeleteDC()
                win32gui.ReleaseDC(hdesktop, desktop_dc)
                win32gui.DeleteObject(bitmap.GetHandle())

                # Measure Screenshot Delay
                now = datetime.now() 
                stop = now.strftime("%S") 
                print("Delay: ",abs(int(start) - int(stop)), " sec")
    

        pygame.time.wait(3)


if __name__== "__main__":
    main()
